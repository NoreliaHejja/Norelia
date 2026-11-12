#!/usr/bin/env python3
"""
KDP teljes borító (hát + gerinc + elő) fekete-fehér papírkönyvhöz, 8.5 x 11 in, bleed 0.125 in.

  python3 scripts/kdp_cover.py <slug> <front-art.png> "Title" "Subtitle" "#hex" "back line 1|back line 2|..."

Gerinc = oldalszám × 0.002252 in (fehér papír). Gerincfelirat csak 80+ oldalnál (KDP-szabály).
A hátoldal jobb alsó sarkában fehér vonalkódhely (2 × 1.2 in).
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FX = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FB = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
FR = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
DPI = 300


def fit(d, text, font, maxw, start):
    s = start
    while s > 20 and d.textlength(text, font=ImageFont.truetype(font, s)) > maxw:
        s -= 4
    return ImageFont.truetype(font, s)


def wrap(d, text, font, maxw):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            out.append(cur); cur = w
    return out + [cur]


def main(slug, art, title, sub, color, back):
    od = ROOT / "kdp" / slug
    pages = json.loads((od / "meta.json").read_text())["pages"]
    spine = pages * 0.002252
    W, H = int((0.125 * 2 + 8.5 * 2 + spine) * DPI), int(11.25 * DPI)
    img = Image.new("RGB", (W, H), color)
    d = ImageDraw.Draw(img)
    fx0 = int((0.125 + 8.5 + spine) * DPI)
    fw = W - fx0
    a = Image.open(art).convert("RGB")
    r = max(fw / a.width, H / a.height)
    a = a.resize((int(a.width * r), int(a.height * r)), Image.LANCZOS)
    a = a.crop(((a.width - fw) // 2, (a.height - H) // 2, (a.width - fw) // 2 + fw, (a.height - H) // 2 + H))
    img.paste(a, (fx0, 0))
    # címdoboz
    m = int(0.55 * DPI)
    bx0, by0, bx1 = fx0 + m, int(0.6 * DPI), W - m
    ft = fit(d, title, FX, bx1 - bx0 - 120, 190)
    lines = wrap(d, title, ft, bx1 - bx0 - 120) if d.textlength(title, font=ft) > bx1 - bx0 - 120 else [title]
    fs = ImageFont.truetype(FB, 64)
    sublines = wrap(d, sub, fs, bx1 - bx0 - 140)
    bh = 80 + len(lines) * (ft.size + 20) + len(sublines) * 84 + 60
    d.rounded_rectangle((bx0, by0, bx1, by0 + bh), 60, fill=(255, 252, 245))
    y = by0 + 60
    for ln in lines:
        d.text(((bx0 + bx1) // 2, y), ln, font=ft, fill="#1F2A44", anchor="ma"); y += ft.size + 20
    for ln in sublines:
        d.text(((bx0 + bx1) // 2, y), ln, font=fs, fill=color, anchor="ma"); y += 84
    d.text((fx0 + fw // 2, H - int(0.6 * DPI)), "AURELIAVENN", font=ImageFont.truetype(FB, 64), fill="white", anchor="mm", stroke_width=6, stroke_fill="#1F2A44")
    # hát
    bx = int(0.6 * DPI)
    y = int(1.0 * DPI)
    d.text((bx, y), title, font=fit(d, title, FX, int(7.2 * DPI), 110), fill="white"); y += 190
    fr = ImageFont.truetype(FR, 54)
    for para in back.split("|"):
        for ln in wrap(d, para, fr, int(7.2 * DPI)):
            d.text((bx, y), ln, font=fr, fill="white"); y += 78
        y += 30
    d.text((bx, H - int(1.0 * DPI)), "Designed by AureliaVenn with the help of AI tools.", font=ImageFont.truetype(FR, 42), fill="white")
    bxe = fx0 - int(spine * DPI) - int(0.375 * DPI)
    d.rectangle((bxe - int(2 * DPI), H - int(0.375 * DPI) - int(1.2 * DPI), bxe, H - int(0.375 * DPI)), fill="white")
    # gerinc
    if pages >= 80:
        sx0 = fx0 - int(spine * DPI)
        sp = Image.new("RGB", (H, int(spine * DPI)), color)
        sd = ImageDraw.Draw(sp)
        sd.text((H // 2, sp.height // 2), title.upper(), font=ImageFont.truetype(FB, max(20, int(sp.height * 0.45))), fill="white", anchor="mm")
        img.paste(sp.rotate(-90, expand=True), (sx0, 0))
    img.save(od / "cover.pdf", "PDF", resolution=DPI)
    img.resize((W // 6, H // 6)).save(od / "cover-preview.jpg", quality=85)
    print(od / "cover.pdf", f"{W/DPI:.3f} x {H/DPI:.3f} in, gerinc {spine:.3f} in, {pages} oldal")


if __name__ == "__main__":
    main(*sys.argv[1:7])
