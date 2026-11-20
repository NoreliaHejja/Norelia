#!/usr/bin/env python3
"""Christmas Elf & Kindness Bundle = Elf Lifesaver Letters + Easy Elf Ideas + Kindness Advent Calendar (34 oldal)
→ termekek/elf-kindness-bundle/ (borító + tartalomjegyzék HTML → PDF, majd pypdf-összefűzés Letter + A4)."""
import subprocess
from pathlib import Path
from pypdf import PdfWriter, PdfReader
from common import page_head, icon, footer

ROOT = Path(__file__).resolve().parent.parent
SLUG = "elf-kindness-bundle"; NAME = "Elf & Kindness Bundle"
OUT = ROOT / "termekek" / SLUG
PARTS = [("elf-lifesaver-letters", "Elf Lifesaver Letters", "30 ready-to-print letters from your elf: arrival, late arrival, touched, 'are you real?', goodbye"),
         ("easy-elf-ideas", "Easy Christmas Elf Ideas", "30 no-mess, 5-minute setups, a 24-day planner and elf-size signs"),
         ("kindness-advent-cards", "Kindness Advent Calendar", "24 kindness missions, tracker, talk cards and a Kindness Champion certificate")]
CSS = """:root{ --dark:#2f6b4f; --sage:#b23a3a; --tint:#f6ece6; --line:#e6cfc6; --accent:#c9a227; --warm:#eef3ec; --warmline:#cfe0d3; --cream:#fdf8f3; }
.cv{ background:linear-gradient(180deg,#fdf8f3,#eef3ec); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.part{ border:2px dashed var(--line); border-radius:16px; padding:16px 20px; margin-bottom:14px; background:#fff; } .part b{ font-size:17pt; color:var(--sage); } .part p{ margin:6px 0 0; font-size:12.5pt; }
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pages = [PdfReader(ROOT / "termekek" / s / f"{s}.pdf") for s, _, _ in PARTS]
    start, rows = 3, []
    for (s, t, d), r in zip(PARTS, pages):
        rows.append(f'<div class="part"><b>{t}</b> <span style="float:right;color:#2f6b4f">page {start}</span><p>{d}</p></div>'); start += len(r.pages)
    html = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>'
            f'<div class="page cv"><div>{icon("star",110,"#c9a227",1.2)}</div><div class="eyebrow">Printable bundle · 3 kits in one</div><h1>Christmas Elf &amp;<br>Kindness Bundle</h1>'
            f'<div class="tg">Everything for a calm, kind and magical December: elf letters, easy elf ideas and a kindness advent calendar.</div><div class="pill">3 kits · {start - 1} pages · US Letter + A4</div></div>'
            f'<div class="page">{page_head("Inside this bundle", "What you get", "book")}{"".join(rows)}'
            f'<div class="card warm" style="margin-top:auto"><h3>Good to know</h3><div class="mini">"Christmas Elf" is a generic name for this activity. Not affiliated with any elf doll brand. For personal and single-classroom use only.</div></div>{footer(NAME, "Contents")}</div></body></html>')
    h = OUT / f"{SLUG}-front.html"; h.write_text(html, encoding="utf-8")
    subprocess.run(["node", str(ROOT / "scripts/render_pdf.js"), str(h)], check=True)
    subprocess.run(["node", str(ROOT / "scripts/render_a4.js"), str(h)], check=True)
    for suf in ["", "-A4"]:
        w = PdfWriter()
        for f in [OUT / f"{SLUG}-front{suf}.pdf"] + [ROOT / "termekek" / s / f"{s}{suf}.pdf" for s, _, _ in PARTS]:
            for p in PdfReader(f).pages:
                w.add_page(p)
        w.write(OUT / f"{SLUG}{suf}.pdf")
    print("kész", start - 1, "oldal")


if __name__ == "__main__":
    main()
