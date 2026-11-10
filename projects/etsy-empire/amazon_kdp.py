#!/usr/bin/env python3
"""
Amazon KDP csomagoló – etsy-empire

Az Amazon KDP-nek NINCS nyilvános feltöltő API-ja, és a böngésző-robotos
feltöltés sérti a KDP feltételeit (fióktiltás kockázata). Ezért ez a script
nem tölt fel: elkészíti a feltöltésre kész csomagot, amit Nóra ~10 perc
alatt kézzel feltölt a kdp.amazon.com-on.

Használat
  python3 amazon_kdp.py termekek/<slug>

Kimenet: termekek/<slug>/kdp/
  KDP_FELTOLTES.md  – mezőnként kitöltött adatlap + ellenőrzőlista
  (a belív/borító PDF-et a termék HTML-jéből a kdp-build lépés készíti, ha eligible)
"""
import json
import subprocess
import sys
from pathlib import Path

MIN_PAGES = 24  # KDP paperback minimum


def pdf_pages(pdf: Path) -> int:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    folder = Path(sys.argv[1]).resolve()
    data = json.loads((folder / "listing.json").read_text(encoding="utf-8"))
    pdf = folder / data["files"][0]
    pages = pdf_pages(pdf)
    e = data["etsy"]

    if pages < MIN_PAGES:
        msg = (f"{data['slug']}: {pages} oldal < {MIN_PAGES} → KDP paperbackre nem alkalmas. "
               "Javaslat: 3 rokon termék összevonása egy 24+ oldalas workbookba.")
        data["kdp"] = {"eligible": False, "reason": msg}
        (folder / "listing.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(msg)
        return

    out = folder / "kdp"
    out.mkdir(exist_ok=True)
    keywords = e["tags"][:7]
    md = f"""# KDP feltöltés – {e['title'][:80]}

| Mező | Érték |
|---|---|
| Formátum | Paperback, 8.5 × 11 in, no bleed, white paper |
| Title | {e['title'].split(',')[0]} |
| Subtitle | {', '.join(e['title'].split(',')[1:3]).strip()} |
| Author | Norelia Studio |
| Low-content book | IGEN (pipáld be) |
| AI-generated content | Képek/szöveg: igen, AI-segítséggel – a kérdőívet ennek megfelelően töltsd ki |
| Keywords (7) | {' · '.join(keywords)} |
| Ár (javaslat) | 8.99 USD |
| Oldalszám | {pages} |

## Ellenőrzőlista
- [ ] Belív PDF feltöltve, Previewer: nincs hiba
- [ ] Borító PDF feltöltve (gerincszélesség a KDP kalkulátorral)
- [ ] Territories: worldwide
- [ ] Publish → státusz a listing.json-ba: kdp_beküldve
"""
    (out / "KDP_FELTOLTES.md").write_text(md, encoding="utf-8")
    data["kdp"] = {"eligible": True, "package": "kdp/KDP_FELTOLTES.md"}
    (folder / "listing.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Kész:", out / "KDP_FELTOLTES.md")


if __name__ == "__main__":
    main()
