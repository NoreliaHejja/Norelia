#!/usr/bin/env python3
"""
Kattintásra optimalizált Pinterest-pin (1000x1500, 2:3) egy termékből.

  python3 scripts/pin_image.py termekek/<slug> "Headline sor 1|sor 2" "Ígéret-alcím" [kép1] [kép2] [szín]

Felépítés (Nóra, 2026-11-19 – a régi pinekre senki nem kattintott):
  1. felső harmad: nagy, olvasható ELŐNY-cím (mit kap a szülő), nem terméknév
  2. közép: a nyomtatható oldalak közelről (2 oldal, enyhén elforgatva) = látszik, mit vesz
  3. alsó sáv: "PRINTABLE · INSTANT DOWNLOAD" + "Tap to see all pages" cselekvésre hívás
Kimenet: termekek/<slug>/kepek/pin-<n>.jpg
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FB = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
FX = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FR = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
if not os.path.exists(FR):
    FR = FB
W, H = 1000, 1500
CREAM = (253, 247, 238)
INK = (45, 35, 30)


def fit(d, text, path, max_w, start):
    s = start
    while s > 18:
        f = ImageFont.truetype(path, s)
        if d.textlength(text, font=f) <= max_w:
            return f
        s -= 2
    return ImageFont.truetype(path, 18)


def card(img_path, w):
    im = Image.open(img_path).convert("RGB")
    r = w / im.width
    im = im.resize((w, int(im.height * r)), Image.LANCZOS)
    return im


def paste_rot(base, im, cx, cy, angle):
    pad = 24
    fr = Image.new("RGBA", (im.width + pad, im.height + pad), (255, 255, 255, 255))
    fr.paste(im, (pad // 2, pad // 2))
    rot = fr.rotate(angle, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", rot.size, (0, 0, 0, 0))
    sh.paste((0, 0, 0, 90), mask=rot.split()[3])
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    x, y = int(cx - rot.width / 2), int(cy - rot.height / 2)
    base.alpha_composite(sh, (x + 10, y + 16))
    base.alpha_composite(rot, (x, y))


def main(folder, headline, sub, img1=None, img2=None, accent="#C8102E", out_name="pin-1.jpg"):
    kep = os.path.join(folder, "kepek")
    img1 = img1 or os.path.join(kep, "02-inside.jpg")
    img2 = img2 or os.path.join(kep, "03-kids.jpg")
    acc = tuple(int(accent.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))

    base = Image.new("RGBA", (W, H), CREAM + (255,))
    d = ImageDraw.Draw(base)
    # finom háttérminta: halvány pöttyök a középső zónában
    for yy in range(470, 1290, 46):
        for xx in range(23 + (yy // 46 % 2) * 23, W, 46):
            d.ellipse((xx - 3, yy - 3, xx + 3, yy + 3), fill=(240, 228, 212, 255))

    # 1) előny-cím
    lines = headline.split("|")
    y = 70
    for ln in lines:
        f = fit(d, ln, FX, W - 110, 104)
        tw = d.textlength(ln, font=f)
        d.text(((W - tw) / 2, y), ln, font=f, fill=INK)
        y += int(f.size * 1.12)
    fs = fit(d, sub, FR, W - 140, 44)
    tw = d.textlength(sub, font=fs)
    d.rounded_rectangle(((W - tw) / 2 - 26, y + 14, (W + tw) / 2 + 26, y + 14 + fs.size + 30), 40, fill=acc)
    d.text(((W - tw) / 2, y + 28), sub, font=fs, fill=(255, 255, 255))
    top_end = y + fs.size + 60

    # 2) oldalak közelről
    a = card(img1, 560)
    b = card(img2, 520)
    mid = (top_end + 1290) / 2
    paste_rot(base, b, W * 0.66, mid + 30, -6)
    paste_rot(base, a, W * 0.38, mid - 10, 4)

    # 3) alsó sáv
    d = ImageDraw.Draw(base)
    d.rectangle((0, 1300, W, H), fill=acc)
    f1 = fit(d, "PRINTABLE  ·  INSTANT DOWNLOAD", FX, W - 120, 50)
    tw = d.textlength("PRINTABLE  ·  INSTANT DOWNLOAD", font=f1)
    d.text(((W - tw) / 2, 1338), "PRINTABLE  ·  INSTANT DOWNLOAD", font=f1, fill=(255, 255, 255))
    cta = "Tap to see all pages  →"
    f2 = fit(d, cta, FR, W - 200, 38)
    tw = d.textlength(cta, font=f2)
    d.text(((W - tw) / 2, 1420), cta, font=f2, fill=(255, 236, 214))

    out = os.path.join(kep, out_name)
    base.convert("RGB").save(out, quality=90)
    print(out)
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 3:
        sys.exit(__doc__)
    main(a[0], a[1], a[2], *[x or None for x in a[3:7]])
