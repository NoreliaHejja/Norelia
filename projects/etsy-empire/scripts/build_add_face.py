#!/usr/bin/env python3
"""Add-Your-Face Christmas Friends → termekek/add-your-face-christmas/
Bemenet: termekek/add-your-face-christmas/png/*.png (átlátszó háttér + arclyuk, scripts/face_hole.py)
Kimenet: <slug>.html → PDF (nyomtatható lapok: karakter nagyban, arclyuk helyén fehér kör „glue photo here”),
         + faliújság-betűk, + útmutató; a PNG-k ZIP-ben (Etsy-fájl)."""
import base64, zipfile
from pathlib import Path
from common import page_head, icon, footer

SLUG = "add-your-face-christmas"
NAME = "Add-Your-Face Christmas Friends"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG
PNG = OUT / "png"

CSS = """:root{ --dark:#2f6b4f; --sage:#b23a3a; --tint:#f6ece6; --line:#e6cfc6; --accent:#c9a227; --warm:#eef3ec; --warmline:#cfe0d3; --cream:#fdf8f3; }
.char{ flex:1; display:flex; align-items:center; justify-content:center; margin-bottom:.2in;
  background:#fff; border-radius:18px; border:2px dashed var(--line); }
.char img{ max-height:8.0in; max-width:6.6in; }
.nm{ text-align:center; font-size:11pt; color:var(--dark); font-weight:600; margin-top:-.1in; }
.grid{ display:grid; grid-template-columns:repeat(5,1fr); gap:10px; flex:1; }
.grid div{ background:#fff; border:1px solid var(--line); border-radius:10px; display:flex; align-items:center; justify-content:center; padding:4px; }
.grid img{ max-width:100%; max-height:1.55in; }
.letters{ display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(2,1fr); gap:14px; flex:1; margin-bottom:.1in; }
.letters div{ border:3px solid var(--sage); border-radius:18px; display:flex; align-items:center; justify-content:center;
  font-size:120pt; font-weight:800; color:var(--sage); background:#fff; }
.letters div:nth-child(even){ color:var(--dark); border-color:var(--dark); }
.cv{ background:linear-gradient(180deg,#fdf8f3,#eef3ec); align-items:center; text-align:center; }
.cv h1{ font-size:36pt; color:var(--sage); margin:.2in 0 4px; line-height:1.05; }
.cv .tg{ font-size:12.5pt; color:var(--dark); max-width:6in; line-height:1.4; margin:0 auto; }
.cv .row3{ display:flex; gap:12px; justify-content:center; margin-top:.3in; } .cv .row3 img{ height:3.2in; }
"""


def img_tag(p):
    return f'<img src="pdfimg/{p.stem}.jpg">'  # PDF: fehér hátterű JPG (papíron ide ragasztják a fotót), ZIP: átlátszó PNG


def main():
    files = sorted(PNG.glob("*.png"))
    assert len(files) >= 30, f"csak {len(files)} PNG"
    names = [f.stem.split("-", 1)[1].replace("-", " ").title() for f in files]
    pg = [f'<div class="page cv"><div class="eyebrow">Printable · PNG · Classroom &amp; family</div>'
          f'<h1>Add-Your-Face<br>Christmas Friends</h1><div class="tg">{len(files)} faceless Christmas characters: add a photo of your child\'s face and turn them into an elf, Santa, a reindeer, a gingerbread friend and more.</div>'
          f'<div class="row3">{img_tag(files[0])}{img_tag(files[1])}{img_tag(files[2])}</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "Two ways to add a face", "book")}
<div class="step"><div class="num">1</div><div><b>On paper (no tech needed)</b><p>Print a character page. Print or cut out a photo of your child's face, slightly bigger than the white circle, and glue it on top. Great for classrooms, bulletin boards and cards.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Digitally (phone or computer)</b><p>Open a PNG from the download folder in a free app such as Canva, Google Slides or PowerPoint. Place your photo on the layer <i>behind</i> the character and move it until the face shows through the hole. Save and share.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Make a bulletin board</b><p>Print the "OUR LITTLE ELVES" letters and line up the whole class or family underneath.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>What's included</h3><div class="mini">{len(files)} PNG characters with transparent background and a see-through face hole (high resolution), {len(files)} printable pages, bulletin board letters, US Letter + A4.</div></div>
<div class="card warm col"><h3>License</h3><div class="mini">Personal and single-classroom use. Do not resell or share the files. Characters designed by our small shop with the help of AI tools.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    for i in range(0, len(files), 20):
        g = "".join(f"<div>{img_tag(f)}</div>" for f in files[i:i+20])
        pg.append(f'<div class="page">{page_head("All characters", f"Characters {i+1}–{min(i+20, len(files))}", "star")}<div class="grid">{g}</div>{footer(NAME, "Overview")}</div>')
    for f, n in zip(files, names):
        pg.append(f'<div class="page" style="padding-top:.55in"><div class="char">{img_tag(f)}</div><div class="nm">{n} · glue a face photo in the circle</div>{footer(NAME, n)}</div>')
    for word in ["OUR", "LITTLE", "ELVES"]:
        for i in range(0, len(word), 6):
            ls = "".join(f"<div>{c}</div>" for c in word[i:i+6])
            pg.append(f'<div class="page">{page_head("Bulletin board letters", word, "check")}<div class="letters">{ls}</div>{footer(NAME, "Letters")}</div>')
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    with zipfile.ZipFile(OUT / f"{SLUG}-PNG.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, f"Add-Your-Face-Christmas/{f.name}")
    print("wrote", OUT / f"{SLUG}.html", len(pg), "pages;", len(files), "PNG")


if __name__ == "__main__":
    main()
