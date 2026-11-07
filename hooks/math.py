"""Hook MkDocs: rendering robusto delle formule LaTeX scritte da Gemini.

Prima che Markdown elabori la pagina, ogni formula ($...$, $$...$$, \\(...\\), \\[...\\])
viene sostituita da un segnaposto alfanumerico che Markdown non può alterare; dopo il
rendering il segnaposto torna formula, pronta per KaTeX. Così le formule funzionano
anche dentro elenchi indentati, tabelle, <details> e attaccate al testo, cose su cui
pymdownx.arithmatex fallisce lasciando LaTeX grezzo o "$" di troppo.
"""

from __future__ import annotations

import hashlib
import html
import re

_MATH: dict[str, tuple[str, bool]] = {}  # token -> (tex, display)

# Codice da non toccare: blocchi recintati e `inline code`.
_CODE = re.compile(r"(^[ \t]*(```|~~~).*?^[ \t]*\2[^\n]*$|`[^`\n]+`)", re.S | re.M)

_PATTERNS = [
    (re.compile(r"\$\$(.+?)\$\$", re.S), True),
    (re.compile(r"\\\[(.+?)\\\]", re.S), True),
    (re.compile(r"\\\((.+?)\\\)", re.S), False),
    # $...$ su una riga: niente spazio subito dentro i dollari, niente cifra subito dopo
    # (evita "costa 5$ e 6$").
    (re.compile(r"(?<![\\$])\$(?=\S)([^$\n]+?)(?<=[^\s\\])\$(?!\d)"), False),
]

_TOKEN = re.compile(r"KMATH([0-9a-f]{12})X")
_DETAILS = re.compile(r"<details(?![^>]*\bmarkdown=)([^>]*)>")


def _stash(tex: str, display: bool) -> str:
    key = hashlib.sha1(f"{display}{tex}".encode()).hexdigest()[:12]
    _MATH[key] = (tex.strip(), display)
    return f"KMATH{key}X"


_LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")


def _loosen_lists(text: str) -> str:
    """Python-Markdown vuole una riga vuota tra un paragrafo e l'elenco che lo segue;
    Gemini spesso la omette e l'elenco finisce incollato nel paragrafo."""
    out: list[str] = []
    for line in text.split("\n"):
        prev = out[-1] if out else ""
        if (
            _LIST_ITEM.match(line)
            and prev.strip()
            and not _LIST_ITEM.match(prev)
            and not prev.lstrip().startswith(("|", "<", "#", ">"))
        ):
            out.append("")
        out.append(line)
    return "\n".join(out)


def _protect(text: str) -> str:
    for rx, display in _PATTERNS:
        text = rx.sub(lambda m, d=display: _stash(m.group(1), d), text)
    return _loosen_lists(text)


def on_page_markdown(markdown: str, **kwargs) -> str:
    # Markdown dentro <details> (soluzioni degli esercizi) va elaborato anch'esso.
    markdown = _DETAILS.sub(r'<details markdown="1"\1>', markdown)
    parts, last = [], 0
    for m in _CODE.finditer(markdown):
        parts.append(_protect(markdown[last : m.start()]))
        parts.append(m.group(0))
        last = m.end()
    parts.append(_protect(markdown[last:]))
    return "".join(parts)


def _render(m: re.Match) -> str:
    tex, display = _MATH.get(m.group(1), (m.group(0), False))
    tex = html.escape(tex, quote=False)
    if display:
        return f'<span class="math math-display">\\[{tex}\\]</span>'
    return f'<span class="math">\\({tex}\\)</span>'


def _plain(m: re.Match) -> str:
    return html.escape(_MATH.get(m.group(1), (m.group(0), False))[0], quote=False)


def on_page_content(html_: str, **kwargs) -> str:
    return _TOKEN.sub(_render, html_)


def on_post_page(output: str, **kwargs) -> str:
    # Rimasugli in titoli, indice laterale e navigazione.
    def fix_title(m: re.Match) -> str:
        return _TOKEN.sub(_plain, m.group(0))

    output = re.sub(r"<title>.*?</title>", fix_title, output, flags=re.S)
    output = re.sub(r'(?<=title=")[^"]*', fix_title, output)
    return _TOKEN.sub(_render, output)
