"""Sincronizza i PDF delle ripetizioni da Google Drive, li trascrive con Gemini
e genera pagine Markdown per il sito MkDocs.

Struttura attesa su Drive:
    <ROOT>/<Nome Studente>/...qualsiasi sottocartella.../*.pdf
Le cartelle che iniziano con "_" vengono ignorate.

Variabili d'ambiente:
    (credenziali)    ADC da google-github-actions/auth (WIF), oppure GDRIVE_SA_JSON
    DRIVE_ROOT_ID    ID della cartella radice (es. "Classroom")
    GEMINI_API_KEY   chiave API Gemini (free tier va bene)
    GEMINI_MODEL     modello (default: gemini-flash-latest)
    MAX_FILES        PDF massimi da elaborare per run (default: 15)
    DRY_RUN          "1" = elenca cosa farebbe senza chiamare Gemini
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
STATE_FILE = ROOT / "pipeline" / "state.json"
PROMPT = (ROOT / "pipeline" / "prompt.md").read_text(encoding="utf-8")

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


# ---------------------------------------------------------------- utilità

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "senza-titolo"


def find_date(*candidates: str) -> str | None:
    for c in candidates:
        if c and (m := DATE_RE.search(c)):
            return "-".join(m.groups())
    return None


def _load_yaml(text: str) -> dict | None:
    """YAML del frontmatter, tollerante: Gemini scrive spesso LaTeX tra virgolette doppie
    (es. "Formula del $\\Delta/4$"), dove in YAML il backslash è un escape non valido.
    In quel caso le stringhe vengono riscritte tra apici singoli, dove il backslash è letterale."""
    try:
        meta = yaml.safe_load(text)
        return meta if isinstance(meta, dict) else None
    except yaml.YAMLError:
        pass
    fixed = re.sub(
        r'"((?:[^"\\\n]|\\.)*)"',
        lambda m: "'" + m.group(1).replace('\\"', '"').replace("'", "''") + "'",
        text,
    )
    # Valori non tra virgolette che contengono ": " (es. "titolo: Geometria: ellisse").
    fixed = re.sub(
        r"^(\s*(?:- )?[\w-]+: )(?!['\"\[{|>])(.*: .*)$",
        lambda m: m.group(1) + "'" + m.group(2).replace("'", "''") + "'",
        fixed,
        flags=re.M,
    )
    try:
        meta = yaml.safe_load(fixed)
        return meta if isinstance(meta, dict) else None
    except yaml.YAMLError:
        return None


def split_frontmatter(md: str) -> tuple[dict, str]:
    md = md.strip()
    md = re.sub(r"^```(?:markdown|md)?\s*\n", "", md)
    md = re.sub(r"\n```\s*$", "", md)
    meta: dict = {}
    # Anche più frontmatter in fila (pagine generate prima della correzione): si uniscono,
    # e i campi più interni (quelli scritti da Gemini) prevalgono.
    while md.startswith("---"):
        parts = md.split("---", 2)
        if len(parts) < 3:
            break
        inner = _load_yaml(parts[1])
        if inner is None:
            break
        meta = {**meta, **inner}
        md = parts[2].strip()
    return meta, md


def join_frontmatter(meta: dict, body: str) -> str:
    fm = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{fm}\n---\n\n{body.strip()}\n"


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- Drive

def drive_service():
    """Credenziali via Workload Identity Federation (ADC creato da
    google-github-actions/auth); fallback su chiave JSON in GDRIVE_SA_JSON."""
    import google.auth
    from googleapiclient.discovery import build

    scopes = ["https://www.googleapis.com/auth/drive.readonly"]
    if os.environ.get("GDRIVE_SA_JSON"):
        from google.oauth2 import service_account

        creds = service_account.Credentials.from_service_account_info(
            json.loads(os.environ["GDRIVE_SA_JSON"]), scopes=scopes
        )
    else:
        creds, _ = google.auth.default(scopes=scopes)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def list_children(svc, folder_id: str) -> list[dict]:
    items, token = [], None
    while True:
        resp = svc.files().list(
            q=f"'{folder_id}' in parents and trashed = false",
            fields="nextPageToken, files(id, name, mimeType, modifiedTime, createdTime, webViewLink)",
            pageSize=1000,
            pageToken=token,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        ).execute()
        items += resp.get("files", [])
        token = resp.get("nextPageToken")
        if not token:
            return items


FOLDER = "application/vnd.google-apps.folder"


def walk_pdfs(svc, folder_id: str, path: tuple[str, ...] = ()):
    for f in list_children(svc, folder_id):
        if f["mimeType"] == FOLDER:
            if not f["name"].startswith("_"):
                yield from walk_pdfs(svc, f["id"], path + (f["name"],))
        elif f["mimeType"] == "application/pdf":
            f["folders"] = path
            yield f


def download(svc, file_id: str) -> bytes:
    from googleapiclient.http import MediaIoBaseDownload

    buf = io.BytesIO()
    req = svc.files().get_media(fileId=file_id, supportsAllDrives=True)
    dl = MediaIoBaseDownload(buf, req)
    done = False
    while not done:
        _, done = dl.next_chunk()
    return buf.getvalue()


# ---------------------------------------------------------------- Gemini

class RateLimited(Exception):
    pass


class ConfigError(Exception):
    """Errore che si ripeterebbe su ogni file (modello inesistente, chiave non valida...)."""


_client = None


def gemini():
    """Client Gemini condiviso e nome del modello."""
    from google import genai
    from google.genai import types

    global _client
    if _client is None:
        # v1beta: è la versione che espone tutti i modelli e gli alias "-latest";
        # da google-genai 3.x il default è v1, dove molti modelli risultano 404.
        _client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"],
            http_options=types.HttpOptions(api_version="v1beta"),
        )
    return _client, os.environ.get("GEMINI_MODEL") or "gemini-flash-latest"


def generate(**kwargs):
    """generate_content con nuovi tentativi sugli errori temporanei di Gemini
    (500/503/504, es. "model is currently experiencing high demand")."""
    from google.genai import errors

    client, model = gemini()
    waits = [30, 90]
    for attempt in range(len(waits) + 1):
        try:
            return client.models.generate_content(model=model, **kwargs)
        except errors.APIError as e:
            if getattr(e, "code", None) not in (500, 503, 504) or attempt == len(waits):
                raise
            print(f"  Gemini non disponibile ({e.code}), riprovo tra {waits[attempt]}s")
            time.sleep(waits[attempt])


def transcribe(pdf: bytes) -> str:
    from google.genai import types, errors

    _, model = gemini()
    try:
        resp = generate(
            contents=[types.Part.from_bytes(data=pdf, mime_type="application/pdf"), PROMPT],
            config=types.GenerateContentConfig(temperature=0.2),
        )
    except errors.APIError as e:
        code = getattr(e, "code", None)
        if code == 429:
            raise RateLimited(str(e)) from e
        if code in (401, 403, 404):
            raise ConfigError(f"modello '{model}': {e}") from e
        raise
    return resp.text or ""


# ---------------------------------------------------------------- revisione

REVIEW_PROMPT = (ROOT / "pipeline" / "review_prompt.md").read_text(encoding="utf-8")


def review_md(pdf: bytes, body: str) -> str:
    """Seconda passata: Gemini rilegge PDF + trascrizione da revisore e restituisce solo
    correzioni puntuali {originale, corretto, motivo}. Si applicano quelle il cui testo
    originale compare una e una sola volta, così non può riscrivere la pagina a caso."""
    from google.genai import types

    try:
        resp = generate(
            contents=[
                types.Part.from_bytes(data=pdf, mime_type="application/pdf"),
                REVIEW_PROMPT + "\n\n--- TRASCRIZIONE DA REVISIONARE ---\n\n" + body,
            ],
            config=types.GenerateContentConfig(temperature=0, response_mime_type="application/json"),
        )
        fixes = json.loads(resp.text or "[]")
    except Exception as e:  # la revisione è un miglioramento: se fallisce si tiene la trascrizione
        print(f"  revisione non riuscita: {e}", file=sys.stderr)
        return body
    applied = 0
    for fix in fixes if isinstance(fixes, list) else []:
        if not isinstance(fix, dict):
            continue
        old = str(fix.get("originale", ""))
        new = str(fix.get("corretto", ""))
        if not old or old == new or body.count(old) != 1:
            continue
        body = body.replace(old, new)
        applied += 1
        print(f"  revisione: {str(fix.get('motivo', ''))[:150]}")
    if applied:
        print(f"  {applied} correzioni applicate dalla revisione")
    return body


# ---------------------------------------------------------------- formule

def _math_hook():
    """Il modulo hooks/math.py del sito: stessa estrazione delle formule usata in build."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("site_math", ROOT / "hooks" / "math.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def extract_math(md: str) -> list[tuple[str, bool]]:
    hook = _math_hook()
    found: list[tuple[str, bool]] = []
    text = hook._CODE.sub("", md)
    for rx, display in hook._PATTERNS:
        found += [(hook.fix_tex(m.group(1)), display) for m in rx.finditer(text)]
        text = rx.sub(" ", text)  # come nel hook: una formula non viene riletta dal pattern successivo
    return found


def invalid_math(md: str) -> list[dict] | None:
    """Formule che KaTeX non riesce a renderizzare. None se il validatore non è disponibile."""
    import subprocess

    formulas = list(dict.fromkeys(extract_math(md)))
    if not formulas:
        return []
    try:
        out = subprocess.run(
            ["node", str(ROOT / "pipeline" / "check_math.js")],
            input=json.dumps(formulas), capture_output=True, text=True, check=True, timeout=120,
        )
    except (OSError, subprocess.SubprocessError) as e:
        print(f"  validatore formule non disponibile ({e}); salto il controllo", file=sys.stderr)
        return None
    return json.loads(out.stdout)


REPAIR_PROMPT = """Queste formule LaTeX, prese da appunti di matematica trascritti, non sono valide per KaTeX.
Per ciascuna scrivi la versione corretta che esprime la stessa cosa usando solo comandi supportati da KaTeX
(es. una macro inesistente va sostituita col simbolo standard che il contesto suggerisce).
Non cambiare il contenuto matematico. Rispondi SOLO con un array JSON di oggetti
{"originale": "<formula esatta ricevuta>", "corretta": "<formula corretta>"}.

Formule ed errori:
"""


def repair_math(md: str, rounds: int = 2) -> str:
    """Fa correggere a Gemini solo le formule non valide e applica le correzioni che passano KaTeX."""
    from google.genai import types

    for _ in range(rounds):
        bad = invalid_math(md)
        if not bad:
            return md
        print(f"  {len(bad)} formule non valide, chiedo la correzione a Gemini")
        try:
            resp = generate(
                contents=[REPAIR_PROMPT + json.dumps(bad, ensure_ascii=False, indent=1)],
                config=types.GenerateContentConfig(temperature=0, response_mime_type="application/json"),
            )
            fixes = json.loads(resp.text or "[]")
        except Exception as e:  # la pagina si salva comunque: KaTeX mostra in rosso solo la formula rotta
            print(f"  correzione formule non riuscita: {e}", file=sys.stderr)
            return md
        wanted = {b["tex"] for b in bad}
        for fix in fixes if isinstance(fixes, list) else []:
            orig, new = str(fix.get("originale", "")).strip(), str(fix.get("corretta", "")).strip()
            if orig in wanted and new and new != orig:
                md = md.replace(orig, new)
    return md


def report_math() -> None:
    """Riepilogo a fine run: formule ancora non valide nel sito, come warning di GitHub Actions."""
    total = 0
    for page in sorted(DOCS.glob("*/*.md")):
        if page.name == "index.md":
            continue
        bad = invalid_math(page.read_text(encoding="utf-8"))
        if bad is None:
            return
        for b in bad:
            total += 1
            print(f"::warning file={page.relative_to(ROOT)}::Formula non valida: {b['tex'][:120]} ({b['error'][:160]})")
    print(f"Controllo formule: {total} non valide nel sito.")


# ---------------------------------------------------------------- indici

def collect_pages() -> dict[str, list[dict]]:
    by_student: dict[str, list[dict]] = {}
    for md in sorted(DOCS.glob("*/*.md")):
        if md.name == "index.md":
            continue
        meta, body = split_frontmatter(md.read_text(encoding="utf-8"))
        title = meta.get("titolo") or md.stem
        by_student.setdefault(md.parent.name, []).append({**meta, "titolo": title, "file": md.name})
    return by_student


def write_indexes() -> None:
    by_student = collect_pages()
    home = ["# Ripetizioni\n"]
    for student_slug, pages in sorted(by_student.items()):
        name = pages[0].get("studente", student_slug)
        pages.sort(key=lambda p: str(p.get("data", "")), reverse=True)
        home.append(f"- [{name}]({student_slug}/index.md) — {len(pages)} lezioni")

        lines = [f"# {name}\n", "| Data | Materia | Lezione | Esercizi |", "|---|---|---|---|"]
        for p in pages:
            es = ", ".join(str(e) for e in p.get("esercizi") or [])
            lines.append(f"| {p.get('data', '')} | {p.get('materia', '')} | [{p['titolo']}]({p['file']}) | {es} |")

        topics: dict[str, list[dict]] = {}
        for p in pages:
            topics.setdefault(str(p.get("argomento", "Altro")), []).append(p)
        lines.append("\n## Per argomento\n")
        for topic in sorted(topics):
            links = ", ".join(f"[{p.get('data', '')}]({p['file']})" for p in topics[topic])
            lines.append(f"- **{topic}**: {links}")

        errs = sorted({e for p in pages for e in (p.get("errori_tipici") or [])})
        if errs:
            lines.append("\n## Errori ricorrenti\n")
            lines += [f"- {e}" for e in errs]

        (DOCS / student_slug / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (DOCS / "index.md").write_text("\n".join(home) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- main

def main() -> int:
    dry = os.environ.get("DRY_RUN") == "1"
    max_files = int(os.environ.get("MAX_FILES") or 15)
    state = load_state()
    svc = drive_service()

    todo = []
    for student in list_children(svc, os.environ["DRIVE_ROOT_ID"]):
        if student["mimeType"] != FOLDER or student["name"].startswith("_"):
            continue
        for f in walk_pdfs(svc, student["id"]):
            prev = state.get(f["id"])
            if not prev or prev["modifiedTime"] != f["modifiedTime"]:
                todo.append((student["name"], f))

    print(f"{len(todo)} PDF nuovi o modificati; ne elaboro al massimo {max_files}.")
    processed = 0
    for student_name, f in sorted(todo, key=lambda t: t[1]["createdTime"]):
        if processed >= max_files:
            break
        print(f"→ {student_name} / {'/'.join(f['folders'] + (f['name'],))}")
        if dry:
            processed += 1
            continue
        try:
            pdf = download(svc, f["id"])
            md = transcribe(pdf)
        except RateLimited:
            print("Limite di richieste Gemini raggiunto: riprendo al prossimo run.")
            break
        except ConfigError as e:
            print(f"Errore di configurazione Gemini, interrompo: {e}", file=sys.stderr)
            print("Controlla GEMINI_API_KEY e GEMINI_MODEL (es. gemini-flash-latest).", file=sys.stderr)
            write_indexes()
            return 1
        except Exception as e:  # un file rotto non deve bloccare gli altri
            print(f"  errore: {e}", file=sys.stderr)
            continue

        meta, body = split_frontmatter(md)
        if body.strip():
            body = review_md(pdf, body)
        body = repair_math(body)
        if not body.strip():
            print("  risposta vuota, salto", file=sys.stderr)
            continue
        date = find_date(f["name"], *f["folders"]) or f["createdTime"][:10]
        slug = slugify(str(meta.get("slug") or meta.get("titolo") or Path(f["name"]).stem))
        meta = {
            "titolo": meta.get("titolo") or Path(f["name"]).stem,
            "data": date,
            "studente": student_name,
            **{k: v for k, v in meta.items() if k not in {"titolo", "slug", "data", "studente"}},
            "fonte": f["webViewLink"],
            "generato": datetime.now().strftime("%Y-%m-%d"),
        }

        out_dir = DOCS / slugify(student_name)
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / f"{date}-{slug}.md"
        old = state.get(f["id"], {}).get("output")
        if old and old != str(out.relative_to(ROOT)):
            (ROOT / old).unlink(missing_ok=True)
        out.write_text(join_frontmatter(meta, body), encoding="utf-8")

        state[f["id"]] = {"modifiedTime": f["modifiedTime"], "output": str(out.relative_to(ROOT))}
        save_state(state)
        processed += 1
        time.sleep(int(os.environ.get("SLEEP_SECONDS") or 15))  # gentile col free tier

    write_indexes()
    report_math()
    print(f"Fatto: {processed} PDF elaborati.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
