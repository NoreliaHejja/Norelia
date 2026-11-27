#!/usr/bin/env python3
"""Névre szóló POD-dizájn renderelése (Nóra jóváhagyta 2026-11-14).
   python3 personalized/render.py <design_key> "<név>" <kimenet.png>
Dizájnok: personalized/designs.json. Név-ellenőrzés: csak betű, szóköz, kötőjel, aposztróf, pont; max 18 karakter."""
import json, re, sys, unicodedata
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT.parent / "assets" / "fonts"
NAME_RE = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿĀ-ž' .\-]{1,18}$")


def clean_name(raw: str) -> str:
    n = unicodedata.normalize("NFC", (raw or "").strip())
    n = re.sub(r"\s+", " ", n)
    if not NAME_RE.match(n):
        raise ValueError(f"érvénytelen név: {raw!r}")
    return n


def fit_font(draw, text, path, max_w, start):
    size = start
    while size > 20:
        f = ImageFont.truetype(str(path), size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(str(path), 20)


def panel(design, name, W, H):
    """Egy oldal (bögre fél / póló eleje): illusztráció + szövegsorok, átlátszó háttér."""
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    art = Image.open(ROOT / design["art"]).convert("RGBA")
    ah = int(H * design.get("art_h", 0.62))
    s = min(W * 0.92 / art.width, ah / art.height)
    a = art.resize((int(art.width * s), int(art.height * s)), Image.LANCZOS)
    top = int(H * design.get("art_top", 0.0))
    c.alpha_composite(a, ((W - a.width) // 2, top))
    y = top + a.height + int(H * 0.02)
    for line in design["lines"]:
        txt = line["text"].replace("{name}", name)
        if line.get("upper"):
            txt = txt.upper()
        f = fit_font(d, txt, FONTS / line["font"], W * line.get("max_w", 0.9), int(H * line["size"]))
        d.text((W // 2, y), txt, font=f, fill=line["color"], anchor="ma")
        bb = d.textbbox((W // 2, y), txt, font=f, anchor="ma")
        y = bb[3] + int(H * line.get("gap", 0.02))
    return c


def render(key, raw_name, out):
    D = json.loads((ROOT / "designs.json").read_text())[key]
    name = clean_name(raw_name)
    if D["type"] == "mug":   # 11oz wrap 2700x1120 (Printify placeholder), minta mindkét oldalon
        W, H = 2700, 1120
        c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        p = panel(D, name, 1150, 1080)
        for cx in (W // 4, 3 * W // 4):
            c.alpha_composite(p, (cx - p.width // 2, (H - p.height) // 2))
    else:                    # póló eleje 4500x5400
        c = panel(D, name, 4500, 5400)
    c.save(out)
    return out


if __name__ == "__main__":
    print(render(sys.argv[1], sys.argv[2], sys.argv[3]))
