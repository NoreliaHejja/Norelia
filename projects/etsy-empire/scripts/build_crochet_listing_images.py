#!/usr/bin/env python3
"""Horgolásminta listingképek (2000x2000): 01 illusztráció + cím + „Illustration” jelölés, 02 mintaoldal, 03 tartalom.
  python3 scripts/build_crochet_listing_images.py horgolas/mintak/<slug>
Előfeltétel: kepek/illustration.jpg (rajzolt akvarell, NEM fotó) és a <slug>-EN.pdf."""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BG = (253, 243, 238); RED = (184, 50, 42); DARK = (107, 63, 34)


def main():
    f = Path(sys.argv[1]).resolve(); p = json.loads((f / "pattern.json").read_text()); k = f / "kepek"; k.mkdir(exist_ok=True)
    title = p["name_en"].split(" – ")[0]
    c = Image.new("RGB", (2000, 2000), BG); d = ImageDraw.Draw(c)
    il = Image.open(k / "illustration.jpg").convert("RGB"); il.thumbnail((1500, 1350)); c.paste(il, ((2000 - il.width) // 2, 330))
    d.text((1000, 120), title, font=ImageFont.truetype(FB, 78), fill=RED, anchor="mm")
    d.text((1000, 230), "Crochet pattern · PDF · English + Deutsch", font=ImageFont.truetype(FR, 52), fill=DARK, anchor="mm")
    d.text((1000 + il.width // 2 - 20, 330 + il.height - 20), "stitch chart", font=ImageFont.truetype(FR, 34), fill=(120, 120, 120), anchor="rd")
    d.rounded_rectangle([330, 1820, 1670, 1940], 55, fill=RED); d.text((1000, 1880), f'{p["level_en"].upper()} · PDF PATTERN ONLY', font=ImageFont.truetype(FB, 52), fill="white", anchor="mm")
    c.save(k / "01-cover-square.jpg", quality=92)
    subprocess.run(["pdftoppm", "-r", "150", "-png", "-f", "1", "-l", "1", "-singlefile", str(f / f'{p["slug"]}-EN.pdf'), str(k / "pg1")], check=True)
    c = Image.new("RGB", (2000, 2000), BG); d = ImageDraw.Draw(c); pg = Image.open(k / "pg1.png").convert("RGB"); pg.thumbnail((1400, 1750))
    c.paste(pg, ((2000 - pg.width) // 2, 180)); d.text((1000, 95), "Clear written pattern, row by row", font=ImageFont.truetype(FB, 64), fill=DARK, anchor="mm"); c.save(k / "02-page.jpg", quality=92)
    (k / "pg1.png").unlink()
    c = Image.new("RGB", (2000, 2000), BG); d = ImageDraw.Draw(c)
    d.text((1000, 140), "What's included", font=ImageFont.truetype(FB, 86), fill=RED, anchor="mm")
    items = ["PDF pattern in English (US terms)", "PDF pattern in German (Deutsch)", "UK + Hungarian abbreviation table", "Stitch count for every round",
             f'Hook: {p["hook"]}', f'Size: {p["size_en"]}', f'Skill level: {p["level_en"]}']
    for i, t in enumerate(items): d.text((200, 380 + i * 190), "✓  " + t, font=ImageFont.truetype(FR, 58), fill=(40, 40, 40))
    c.save(k / "03-included.jpg", quality=92); print("OK", k)


if __name__ == "__main__":
    main()
