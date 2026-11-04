"""Sincronizza i PDF delle ripetizioni da Google Drive, li trascrive con Gemini
e genera pagine Markdown per il sito MkDocs.

Struttura attesa su Drive:
    <ROOT>/<Nome Studente>/...qualsiasi sottocartella.../*.pdf
Le cartelle che iniziano con "_" vengono ignorate.

Variabili d'ambiente:
    (credenziali)    ADC da google-github-actions/auth (WIF), oppure GDRIVE_SA_JSON
    DRIVE_ROOT_ID    ID della cartella radice (es. "Classroom")
    GEMINI_API_KEY   chiave API Gemini (free tier va bene)
    GEMINI_MODEL     modello (default: gemini-2.5-flash)
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


def split_frontmatter(md: str) -> tuple[dict, str]:
    md = md.strip()
    md = re.sub(r"^```(?:markdown|md)?\s*\n", "", md)
    md = re.sub(r"\n```\s*$", "", md)
    if md.startswith("---"):
        parts = md.split("---", 2)
        if len(parts) == 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
                return meta, parts[2].lstrip("\n")
            except yaml.YAMLError:
                pass
    return {}, md


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


def transcribe(pdf: bytes) -> str:
    from google import genai
    from google.genai import types, errors

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    model = os.environ.get("GEMINI_MODEL") or "gemini-2.5-flash"
    try:
        resp = client.models.generate_content(
            model=model,
            contents=[types.Part.from_bytes(data=pdf, mime_type="application/pdf"), PROMPT],
            config=types.GenerateContentConfig(temperature=0.2),
        )
    except errors.APIError as e:
        if getattr(e, "code", None) == 429:
            raise RateLimited(str(e)) from e
        raise
    return resp.text or ""


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
            md = transcribe(download(svc, f["id"]))
        except RateLimited:
            print("Limite di richieste Gemini raggiunto: riprendo al prossimo run.")
            break
        except Exception as e:  # un file rotto non deve bloccare gli altri
            print(f"  errore: {e}", file=sys.stderr)
            continue

        meta, body = split_frontmatter(md)
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
    print(f"Fatto: {processed} PDF elaborati.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
