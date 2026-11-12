#!/usr/bin/env python3
"""Etsy listingképek a termék PDF-oldalaiból (ingyenes, Higgsfield nélkül).
Használat: python3 scripts/listing_kepek.py termekek/<slug>
Kimenet: termekek/<slug>/kepek/01-cover.jpg, 02-inside.jpg, 03-kids.jpg (2000×2500, 4:5)."""
import json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 2000, 2500
CREAM, DARK, SOFT, ACCENT = (250, 248, 242), (79, 107, 88), (95, 111, 102), (224, 164, 88)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def pages(pdf, tmp):
    subprocess.run(["pdftoppm", "-r", "110", "-png", str(pdf), f"{tmp}/p"], check=True)
    return sorted(Path(tmp).glob("p-*.png"))


def card(img, w):
    im = Image.open(img).convert("RGB")
    im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    pad = 40
    sh = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([pad, pad + 14, pad + im.width, pad + im.height + 14], 18, fill=(79, 107, 88, 60))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    sh.paste(im, (pad, pad))
    return sh


def canvas(title, sub):
    c = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(c)
    d.text((W // 2, 150), title, font=ImageFont.truetype(FB, 92), fill=DARK, anchor="mm")
    d.text((W // 2, 260), sub, font=ImageFont.truetype(FR, 46), fill=SOFT, anchor="mm")
    d.rounded_rectangle([W // 2 - 60, 320, W // 2 + 60, 328], 4, fill=ACCENT)
    return c


def main():
    folder = Path(sys.argv[1]).resolve()
    data = json.loads((folder / "listing.json").read_text(encoding="utf-8"))
    out = folder / "kepek"
    out.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        ps = pages(folder / data["files"][0], tmp)
        n = len(ps)
        k = data.get("kepszoveg", {})
        t1, t2, t3 = k.get("cim1", "Printable Family Planner"), k.get("cim2", "What's inside"), k.get("cim3", "Made for little helpers")
        s2, s3 = k.get("al2", "Checklist · Budget · Chore chart · 30-day challenge · Intro plan"), k.get("al3", "Picture-based jobs for ages 3+ · color a dot, earn a reward")
        kids = k.get("gyerekoldalak", [4, 5])
        # 1) borító + 2 oldal legyezőben
        c = canvas(t1, f"{n} pages · Instant download · US Letter & A4")
        for i, (idx, x, y, rot) in enumerate([(2, 960, 640, -6), (4, 180, 660, 6)]):
            if idx < n:
                cd = card(ps[idx], 900).rotate(rot, expand=True, resample=Image.BICUBIC)
                c.paste(cd, (x, y), cd)
        cv = card(ps[0], 1100)
        c.paste(cv, ((W - cv.width) // 2, 520), cv)
        c.save(out / "01-cover.jpg", quality=92)
        # 2) mi van benne – rács
        c = canvas(t2, s2)
        cols, cw = 3, 560
        for i, p in enumerate(ps[1:7]):
            cd = card(p, cw)
            c.paste(cd, (110 + (i % cols) * (cw + 50), 420 + (i // cols) * 1000), cd)
        c.save(out / "02-inside.jpg", quality=92)
        # 3) gyerekeknek
        c = canvas(t3, s3)
        for p, x in [(ps[kids[0]] if n > kids[0] else ps[0], 120), (ps[kids[1]] if n > kids[1] else ps[0], 1020)]:
            cd = card(p, 860)
            c.paste(cd, (x, 480), cd)
        c.save(out / "03-kids.jpg", quality=92)
        # 4) egy oldal nagyban (részletek)
        c = canvas(k.get("cim4", "Look closer"), k.get("al4", "Clean, calm design · printer friendly"))
        big = card(ps[2] if n > 2 else ps[0], 1500)
        c.paste(big, ((W - big.width) // 2, 420), big)
        c.save(out / "04-detail.jpg", quality=92)
        # 5) hogyan működik
        c = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(c)
        d.text((W // 2, 260), "How it works", font=ImageFont.truetype(FB, 110), fill=DARK, anchor="mm")
        d.rounded_rectangle([W // 2 - 60, 360, W // 2 + 60, 368], 4, fill=ACCENT)
        steps = [("1", "Buy", "Checkout on Etsy"), ("2", "Download", "Instant PDF – US Letter & A4"), ("3", "Print", "At home or at a print shop"), ("4", "Enjoy", "Reprint as often as you need")]
        for i, (nr, t, sub) in enumerate(steps):
            y = 560 + i * 430
            d.ellipse([260, y, 520, y + 260], outline=ACCENT, width=8, fill=(255, 255, 255))
            d.text((390, y + 130), nr, font=ImageFont.truetype(FB, 120), fill=DARK, anchor="mm")
            d.text((620, y + 85), t, font=ImageFont.truetype(FB, 96), fill=DARK, anchor="lm")
            d.text((620, y + 185), sub, font=ImageFont.truetype(FR, 56), fill=SOFT, anchor="lm")
        d.text((W // 2, H - 110), "No physical item will be shipped", font=ImageFont.truetype(FR, 46), fill=SOFT, anchor="mm")
        c.save(out / "05-how-it-works.jpg", quality=92)
    print("Kész:", ", ".join(sorted(x.name for x in out.glob("*.jpg"))))


if __name__ == "__main__":
    main()
