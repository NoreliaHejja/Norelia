#!/usr/bin/env python3
"""Elf Family Role Shirts – 24 saját szerep PNG (átlátszó, 300 DPI, póló-kész) → termekek/elf-family-role-shirts/
A manósapka Higgsfield-illusztráció (art/hat-src.png, fehér háttér → átlátszó flood-fill), a szöveg PIL (helyesírás biztos).
Védjegy: nincs (csak általános „elf”)."""
import sys, zipfile
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "termekek" / "elf-family-role-shirts"
F = ROOT / "assets" / "fonts"
RED, GREEN, CREAM, GOLD = (178, 42, 48), (36, 98, 64), (255, 248, 236), (201, 162, 39)
ROLES = ["Cookie Taster", "Sleepy", "Bossy", "Snacky", "Wrapping", "Shopping", "Sassy", "Grumpy", "Cocoa", "Selfie",
         "Dancing", "Lazy", "Jolly", "Sparkly", "Messy", "Loud", "Silly", "Hungry", "Cozy", "Baking", "Late", "Head",
         "Coffee", "Baby"]
W, H = 3000, 3600


def hat():
    p = OUT / "art" / "hat.png"
    if p.exists():
        return Image.open(p)
    im = Image.open(OUT / "art" / "hat-src.png").convert("RGB")
    a = np.asarray(im).astype(int)
    white = (a.min(axis=2) > 232)
    lab, _ = ndimage.label(white)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(border))
    bg = ndimage.binary_erosion(~bg, iterations=1)  # 1 px szél-tisztítás
    alpha = (bg * 255).astype(np.uint8)
    rgba = im.convert("RGBA"); rgba.putalpha(Image.fromarray(alpha))
    rgba = rgba.crop(rgba.getbbox())
    rgba.save(p)
    return rgba


def fit(d, text, path, max_w, size):
    while size > 40:
        f = ImageFont.truetype(str(path), size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 10
    return f


def render(role, out, w=W, h=H):
    c = Image.new("RGBA", (w, h * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    hp = hat()
    s = w * 0.50 / hp.width
    hi = hp.resize((int(hp.width * s), int(hp.height * s)), Image.LANCZOS)
    c.alpha_composite(hi, ((w - hi.width) // 2, int(h * 0.04)))
    y = int(h * 0.04) + hi.height + int(h * 0.02)
    sw = int(w * 0.012)
    for txt, font, size, col, mw in [("I'M THE", "LilitaOne-Regular.ttf", 0.075, GREEN, 0.6),
                                     (role, "Shrikhand-Regular.ttf", 0.14, RED, 0.94),
                                     ("ELF", "LilitaOne-Regular.ttf", 0.25, GREEN, 0.8)]:
        f = fit(d, txt, F / font, w * mw, int(h * size))
        d.text((w // 2, y), txt, font=f, fill=col, anchor="ma", stroke_width=sw, stroke_fill=CREAM)
        bb = d.textbbox((w // 2, y), txt, font=f, anchor="ma", stroke_width=sw)
        y = bb[3] + int(h * 0.012)
    c = c.crop(c.getbbox())
    canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sc = min(w * 0.92 / c.width, h * 0.94 / c.height)
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    canvas.alpha_composite(c, ((w - c.width) // 2, (h - c.height) // 2))
    canvas.save(out, dpi=(300, 300), optimize=True)
    return out


def slug(r):
    return r.lower().replace(" ", "-") + "-elf"


def main():
    png = OUT / "png"; png.mkdir(parents=True, exist_ok=True)
    roles = sys.argv[1:] or ROLES
    for r in roles:
        render(r, png / f"{slug(r)}.png")
    if not sys.argv[1:]:
        with zipfile.ZipFile(OUT / "elf-family-role-shirts-PNG.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for r in ROLES:
                z.write(png / f"{slug(r)}.png", f"Elf-Family-Role-Shirts/{slug(r)}.png")
    print("kész:", len(roles))


if __name__ == "__main__":
    main()
