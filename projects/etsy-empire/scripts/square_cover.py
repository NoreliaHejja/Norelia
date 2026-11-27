#!/usr/bin/env python3
"""Négyzetes, kivágás-biztos első kép (Etsy shop-rács + mobil négyzetes kivágás).
A 4:5-ös borító teljes egészében középre kerül 2000x2000-es vásznon, oldalt ugyanaz a kép elmosva.
   python3 scripts/square_cover.py termekek/<slug>/kepek/01-cover.jpg [ki.jpg]"""
import sys
from PIL import Image, ImageFilter, ImageEnhance
src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else src.replace("01-cover.jpg", "01-cover-square.jpg")
im = Image.open(src).convert("RGB"); S = 2000
bg = im.resize((S, int(im.height * S / im.width)), Image.LANCZOS)
bg = bg.crop((0, (bg.height - S) // 2, S, (bg.height - S) // 2 + S)).filter(ImageFilter.GaussianBlur(40))
bg = ImageEnhance.Brightness(bg).enhance(0.85)
fg = im.resize((int(im.width * S / im.height), S), Image.LANCZOS)
bg.paste(fg, ((S - fg.width) // 2, 0)); bg.save(out, quality=92); print("OK", out)
