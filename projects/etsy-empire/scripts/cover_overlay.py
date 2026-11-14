#!/usr/bin/env python3
"""
Színes borító (01-cover.jpg) egy AI-mockupból: felirat-szalag + "INSTANT DOWNLOAD" sáv.

  python3 scripts/cover_overlay.py <mockup.png> <ki.jpg> "Cím" "Alcím" [akcentszín]

A mockup Higgsfield-ből jön (lásd CLAUDE.md, "Borító és képek"); a szöveget mi tesszük rá,
hogy olvasható és helyesírásilag pontos legyen.
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FB = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
FX = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
W, H = 2000, 2500


def fit(d, text, font_path, max_w, start):
    s = start
    while s > 20:
        f = ImageFont.truetype(font_path, s)
        if d.textlength(text, font=f) <= max_w:
            return f
        s -= 4
    return ImageFont.truetype(font_path, 20)


def main(src, out, title, sub, accent="#E4572E", band="Printable PDF  ·  US Letter + A4", badge="PRINT|AT HOME"):
    img = Image.open(src).convert("RGB")
    # 4:5 kitöltés
    r = max(W / img.width, H / img.height)
    img = img.resize((int(img.width * r), int(img.height * r)), Image.LANCZOS)
    x0, y0 = (img.width - W) // 2, (img.height - H) // 2
    img = img.crop((x0, y0, x0 + W, y0 + H))

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # felső címkártya árnyékkal
    box = (110, 90, W - 110, 520)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((box[0] + 10, box[1] + 18, box[2] + 10, box[3] + 18), 60, fill=(0, 0, 0, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    layer = Image.alpha_composite(sh, layer)
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(box, 60, fill=(255, 252, 245, 245))
    ft = fit(d, title, FX, box[2] - box[0] - 120, 150)
    d.text((W // 2, 250), title, font=ft, fill="#1F2A44", anchor="mm")
    fs = fit(d, sub, FB, box[2] - box[0] - 160, 70)
    d.text((W // 2, 410), sub, font=fs, fill=accent, anchor="mm")

    # alsó sáv
    d.rectangle((0, H - 260, W, H), fill=accent)
    fb = ImageFont.truetype(FX, 96)
    d.text((W // 2, H - 150), "INSTANT DOWNLOAD", font=fb, fill="white", anchor="mm")
    d.text((W // 2, H - 60), band, font=ImageFont.truetype(FB, 52), fill="white", anchor="mm")

    # sarok-badge
    cx, cy, rad = W - 260, 700, 170
    d.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill="#FFC93C", outline="white", width=12)
    d.text((cx, cy - 40), badge.split("|")[0], font=ImageFont.truetype(FX, 64), fill="#1F2A44", anchor="mm")
    d.text((cx, cy + 40), badge.split("|")[1], font=ImageFont.truetype(FX, 52), fill="#1F2A44", anchor="mm")

    out_img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    out_img.save(out, "JPEG", quality=90)
    print("OK", out)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    main(*sys.argv[1:8])
