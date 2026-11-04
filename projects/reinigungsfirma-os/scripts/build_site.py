#!/usr/bin/env python3
"""Build the deployable landing page.

Reads  src/landing.src.html  (page fragment: <title>, Google-Fonts links, <style>, markup, <script>)
Writes site/index.html       (full HTML document, fonts served locally from site/fonts/)

Why: Google Fonts loaded from Google's servers are a known DSGVO/Abmahnung risk in Germany
(LG München, 2022). The deployed page must never contact fonts.googleapis.com.

Usage:  python3 scripts/build_site.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "landing.src.html"
OUT = ROOT / "site" / "index.html"
FONTS = ROOT / "site" / "fonts"

TITLE = "Stundensatz-Rechner für Reinigungsfirmen | Reinigungsfirma OS"
DESCRIPTION = (
    "Kostenloser Stundensatz-Rechner für Gebäudereiniger in Deutschland, Österreich und der Schweiz. "
    "Lohn, Nebenkosten, Ausfallzeit und Gemeinkosten in einer Minute kalkulieren."
)

FACES = [("Schibsted Grotesk", "schibsted-grotesk", w) for w in (400, 500, 600, 700, 800)] + [
    ("JetBrains Mono", "jetbrains-mono", w) for w in (400, 500, 600)
]


def main() -> int:
    s = SRC.read_text(encoding="utf-8")

    # 1) drop Google Fonts links
    s = re.sub(r'<link rel="preconnect"[^>]*>\n', "", s)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n', "", s)

    # 2) local @font-face rules
    missing = []
    ff = ""
    for family, slug, w in FACES:
        fname = f"{slug}-latin-{w}-normal.woff2"
        if not (FONTS / fname).exists():
            missing.append(fname)
        ff += (
            f'@font-face{{font-family:"{family}";font-weight:{w};font-style:normal;'
            f'font-display:swap;src:url(fonts/{fname}) format("woff2")}}\n'
        )
    if missing:
        print("Missing font files in site/fonts/ — run scripts/fetch_fonts.sh first:", *missing, sep="\n  ")
        return 1
    s = s.replace("<style>\n", "<style>\n" + ff, 1)

    # 3) move <title>/<style> into a proper <head>
    s = re.sub(r"<title>.*?</title>\n", "", s, count=1)
    head = (
        '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{TITLE}</title>\n"
        f'<meta name="description" content="{DESCRIPTION}">\n'
        "<style>body{margin:0}</style>\n"
    )
    i = s.index("</style>") + len("</style>")
    out = head + s[:i] + "\n</head>\n<body>\n" + s[i:] + "\n</body>\n</html>\n"

    assert "googleapis" not in out, "Google Fonts reference left in output"
    OUT.write_text(out, encoding="utf-8")
    print(f"OK  {OUT.relative_to(ROOT)}  ({len(out):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
