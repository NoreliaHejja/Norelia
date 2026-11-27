#!/usr/bin/env python3
"""
Tiszta hátterű termékborító (Nóra, 2026-11-22): csak a termék látszik, kellék és életkép nélkül.
A PDF 3 oldala (borító + 2 belső) legyezőszerűen, puha árnyékkal, egyszínű világos háttéren.

  python3 scripts/clean_cover.py termekek/<slug> [oldal1 oldal2 oldal3] [--bg "#F6F3EE"]

Kimenet: kepek/01-cover.jpg (2000x2500, 4:5) és kepek/01-cover-square.jpg (2000x2000) – ez legyen az images[0].
"""
import sys, os, subprocess, tempfile, json
from PIL import Image, ImageFilter

def render_pages(pdf, pages, tmp):
    out = []
    for p in pages:
        base = os.path.join(tmp, f"p{p}")
        subprocess.run(["pdftoppm", "-r", "150", "-png", "-f", str(p), "-l", str(p), "-singlefile", pdf, base], check=True)
        out.append(Image.open(base + ".png").convert("RGB"))
    return out

def place(canvas, page, cx, cy, h, angle):
    r = h / page.height
    pg = page.resize((int(page.width * r), int(h)), Image.LANCZOS).convert("RGBA")
    rot = pg.rotate(angle, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", rot.size, (0, 0, 0, 0))
    sh.paste((60, 45, 30, 70), mask=rot.split()[3])
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    x, y = int(cx - rot.width / 2), int(cy - rot.height / 2)
    canvas.alpha_composite(sh, (x + 14, y + 24))
    canvas.alpha_composite(rot, (x, y))

def make(pages, W, H, bg):
    c = Image.new("RGBA", (W, H), bg + (255,))
    ph = H * 0.70
    place(c, pages[2], W * 0.68, H * 0.52, ph * 0.92, -8)
    place(c, pages[1], W * 0.33, H * 0.52, ph * 0.92, 7)
    place(c, pages[0], W * 0.50, H * 0.50, ph, 0)
    return c.convert("RGB")

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    bg = "#F6F3EE"
    if "--bg" in sys.argv:
        bg = sys.argv[sys.argv.index("--bg") + 1]
        a = [x for x in a if x != bg]
    folder = a[0]
    slug = os.path.basename(folder.rstrip("/"))
    pdf = os.path.join(folder, f"{slug}.pdf")
    pages = [int(x) for x in a[1:4]] if len(a) >= 4 else [1, 3, 5]
    bgc = tuple(int(bg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    with tempfile.TemporaryDirectory() as t:
        imgs = render_pages(pdf, pages, t)
    kep = os.path.join(folder, "kepek"); os.makedirs(kep, exist_ok=True)
    make(imgs, 2000, 2500, bgc).save(os.path.join(kep, "01-cover.jpg"), quality=92)
    make(imgs, 2000, 2000, bgc).save(os.path.join(kep, "01-cover-square.jpg"), quality=92)
    print("OK", kep)

if __name__ == "__main__":
    main()
