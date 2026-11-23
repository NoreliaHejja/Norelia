#!/usr/bin/env python3
"""Szabásminta útmutató (EN + DE PDF) + Etsy listingképek + listing.json váz.
  python3 scripts/build_sloper_guide.py szabas/mintak/<slug>
Előfeltétel: build_sloper.py már lefutott (layout.pdf). A pattern.json "guide" mezője adja a típus-specifikus szöveget."""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_sloper import SIZES

ROOT = Path(__file__).resolve().parent.parent
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
CSS = """@page{size:Letter;margin:.6in}body{font-family:'DejaVu Sans',sans-serif;font-size:10.5pt;line-height:1.5;color:#2b2b2b}
h1{color:#3f5f73;font-size:22pt;margin:0}h2{color:#3f5f73;border-bottom:2px solid #d5e0e6;padding-bottom:3px;margin-top:18px;page-break-after:avoid}
.sub{color:#555;margin-bottom:12px}table{border-collapse:collapse;width:100%;font-size:9.5pt}td,th{border:1px solid #cfd8dc;padding:4px 6px;text-align:center}th{background:#eef3f5}
.box{background:#f4f7f8;border-radius:10px;padding:10px 14px;margin:10px 0}img{width:100%;border:1px solid #ddd;border-radius:8px}li{margin-bottom:4px}"""


def chart(lang, sizes):
    hd = {"en": ("Size", "Bust", "Waist", "Hip", "Hip depth"), "de": ("Größe", "Brust", "Taille", "Hüfte", "Hüfttiefe")}[lang]
    rows = "".join(f"<tr><td><b>{s}</b></td><td>{SIZES[s]['bust']} cm / {SIZES[s]['bust']/2.54:.1f}\"</td><td>{SIZES[s]['waist']} cm / {SIZES[s]['waist']/2.54:.1f}\"</td><td>{SIZES[s]['hip']} cm / {SIZES[s]['hip']/2.54:.1f}\"</td><td>{SIZES[s]['hipdepth']} cm</td></tr>" for s in sizes)
    return f"<table><tr>{''.join(f'<th>{h}</th>' for h in hd)}</tr>{rows}</table>"


def main():
    folder = Path(sys.argv[1]).resolve(); p = json.loads((folder / "pattern.json").read_text()); slug = p["slug"]
    subprocess.run(["pdftoppm", "-r", "40", "-png", "-singlefile", str(folder / "layout.pdf"), str(folder / "layout")], check=True)
    for lang in ("en", "de"):
        g = p["guide"][lang]
        secs = "".join(f"<h2>{t}</h2>{body}" for t, body in g["sections"])
        html = f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>{p['name_' + lang]}</title><style>{CSS}</style></head><body>
<h1>{p['name_' + lang]}</h1><div class="sub">{g['sub']}</div><img src="layout.png">
<h2>{g['chart_title']}</h2>{chart(lang, p['sizes'])}<div class="box">{g['chart_note']}</div>{secs}
<p style="font-size:8.5pt;color:#777;margin-top:20px">© AureliaVenn · {g['license']}</p></body></html>"""
        f = folder / f"{slug}-Guide-{lang.upper()}.html"; f.write_text(html, encoding="utf-8")
        subprocess.run(["node", str(ROOT / "scripts" / "render_pdf.js"), str(f)], check=True)
    # listingképek 2000x2000
    k = folder / "kepek"; k.mkdir(exist_ok=True); lay = Image.open(folder / "layout.png").convert("RGB")
    def canvas_(title, sub, bg=(244, 247, 248)):
        c = Image.new("RGB", (2000, 2000), bg); d = ImageDraw.Draw(c)
        d.text((1000, 110), title, font=ImageFont.truetype(FB, 86), fill=(63, 95, 115), anchor="mm")
        d.text((1000, 215), sub, font=ImageFont.truetype(FR, 50), fill=(70, 70, 70), anchor="mm"); return c, d
    c, d = canvas_(p["img"]["title"], p["img"]["sub"])
    im = lay.copy(); im.thumbnail((1800, 1500)); c.paste(im, ((2000 - im.width) // 2, 300))
    d.rounded_rectangle([350, 1850, 1650, 1960], 50, fill=(63, 95, 115)); d.text((1000, 1905), p["img"]["band"], font=ImageFont.truetype(FB, 52), fill="white", anchor="mm")
    c.save(k / "01-cover-square.jpg", quality=92)
    c, d = canvas_("Size chart (body measurements)", "XS to 3X · cm and inches"); y = 360
    f1 = ImageFont.truetype(FB, 54); f2 = ImageFont.truetype(FR, 52)
    for i, h in enumerate(("Size", "Bust", "Waist", "Hip")): d.text((300 + i * 430, y), h, font=f1, fill=(63, 95, 115), anchor="mm")
    for s in p["sizes"]:
        y += 170; m = SIZES[s]
        for i, v in enumerate((s, f"{m['bust']} / {m['bust']/2.54:.0f}\"", f"{m['waist']} / {m['waist']/2.54:.0f}\"", f"{m['hip']} / {m['hip']/2.54:.0f}\"")):
            d.text((300 + i * 430, y), v, font=f1 if i == 0 else f2, fill=(40, 40, 40), anchor="mm")
    d.text((1000, 1880), "Choose by hip measurement for skirts", font=f2, fill=(90, 90, 90), anchor="mm"); c.save(k / "02-size-chart.jpg", quality=92)
    c, d = canvas_("What's included", "Instant PDF download")
    for i, t in enumerate(p["img"]["included"]): d.text((220, 420 + i * 175), "✓  " + t, font=ImageFont.truetype(FR, 62), fill=(40, 40, 40))
    c.save(k / "03-included.jpg", quality=92)
    pg = folder / "pg"; subprocess.run(["pdftoppm", "-r", "150", "-png", "-f", "1", "-l", "1", str(folder / f"{slug}-Guide-EN.pdf"), str(pg)], check=True)
    c, d = canvas_("Step-by-step guide", "English + Deutsch"); g1 = Image.open(sorted(folder.glob("pg*.png"))[0]).convert("RGB"); g1.thumbnail((1300, 1600)); c.paste(g1, ((2000 - g1.width) // 2, 320)); c.save(k / "04-guide.jpg", quality=92)
    for x in folder.glob("pg*.png"): x.unlink()
    print("OK", k)


if __name__ == "__main__":
    main()
