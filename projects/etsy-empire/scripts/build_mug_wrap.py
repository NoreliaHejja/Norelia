#!/usr/bin/env python3
"""Mug wrap PNG (11oz 2550x1050, 15oz 2625x1140, 300 DPI, átlátszó, minta mindkét oldalon) egy POD-dizájnból.
   python3 scripts/build_mug_wrap.py pod/<design>.png <slug>   → termekek/mug-wrap-<slug>/ (+ kepek/04-files.jpg)"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
src, slug = sys.argv[1], sys.argv[2]
OUT = Path(__file__).resolve().parent.parent / "termekek" / f"mug-wrap-{slug}"; (OUT / "kepek").mkdir(parents=True, exist_ok=True)
d = Image.open(src).convert("RGBA"); d = d.crop(d.getbbox())
for name, (W, H) in {"11oz": (2550, 1050), "15oz": (2625, 1140)}.items():
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0)); s = min(W * 0.42 / d.width, H * 0.9 / d.height)
    p = d.resize((int(d.width * s), int(d.height * s)), Image.LANCZOS)
    for cx in (W // 4, 3 * W // 4):
        c.alpha_composite(p, (cx - p.width // 2, (H - p.height) // 2))
    c.save(OUT / f"{slug}-mug-wrap-{name}.png", dpi=(300, 300), optimize=True)
# 04-files: a 11oz fájl sakktábla-háttéren (átlátszóság jelzése) + méretek
w = Image.open(OUT / f"{slug}-mug-wrap-11oz.png"); C = Image.new("RGB", (2000, 2500), (253, 248, 243)); dr = ImageDraw.Draw(C)
ck = Image.new("RGB", (1800, 741), "white"); cd = ImageDraw.Draw(ck)
for y in range(0, 741, 40):
    for x in range(0, 1800, 40):
        if (x // 40 + y // 40) % 2: cd.rectangle((x, y, x + 39, y + 39), fill=(232, 232, 232))
ww = w.resize((1800, 741), Image.LANCZOS); ck.paste(ww, (0, 0), ww); C.paste(ck, (100, 700))
F = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"; B = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
dr.text((1000, 300), "What you get", font=ImageFont.truetype(F, 120), fill=(31, 42, 68), anchor="ma")
dr.text((1000, 470), "Transparent PNG · design on both sides", font=ImageFont.truetype(B, 64), fill=(178, 42, 48), anchor="ma")
for i, t in enumerate(["11oz: 2550 x 1050 px · 300 DPI", "15oz: 2625 x 1140 px · 300 DPI", "Sublimation ready · instant download"]):
    dr.text((1000, 1650 + i * 150), t, font=ImageFont.truetype(B, 72), fill=(47, 107, 79), anchor="ma")
C.save(OUT / "kepek" / "04-files.jpg", quality=90); print("OK", OUT)
