#!/usr/bin/env python3
"""Kindle e-könyv borító a papírkönyv cover.pdf-jéből (KDP-szabály: min. 625 x 1000 px, max. 10 000 px mindkét irányban;
ajánlott magasság 2560 px; JPG, RGB). A cover.pdf jobb oldali (elülső) paneljét vágja ki a kifutó (0,125 in) nélkül.
   python3 scripts/kdp_ebook_cover.py kdp/<csomag>/            → kdp/<csomag>/ebook-cover.jpg
   python3 scripts/kdp_ebook_cover.py --all                    → minden kdp/*/cover.pdf"""
import sys, subprocess, tempfile, re
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parent.parent
TRIM_W, TRIM_H, BLEED, DPI, TARGET_H = 8.5, 11.0, 0.125, 300, 2560

def one(d: Path):
    pdf = d / "cover.pdf"
    size = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    w_pt, h_pt = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", size).groups())
    trim_h = h_pt / 72 - 2 * BLEED
    trim_w = TRIM_W if abs(trim_h - TRIM_H) < 0.05 else trim_h * (6 / 9)   # 8.5x11 csomagok; más trimnél 6x9 arány
    with tempfile.TemporaryDirectory() as t:
        subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-singlefile", str(pdf), f"{t}/c"], check=True)
        im = Image.open(f"{t}/c.png").convert("RGB")
    px = im.width / (w_pt / 72)
    x1 = im.width - BLEED * px; x0 = x1 - trim_w * px; y0 = BLEED * px; y1 = y0 + trim_h * px
    front = im.crop((round(x0), round(y0), round(x1), round(y1)))
    h = TARGET_H; w = round(front.width * h / front.height)
    front = front.resize((w, h), Image.LANCZOS)
    assert 625 <= w <= 10000 and 1000 <= h <= 10000, (w, h)
    out = d / "ebook-cover.jpg"; front.save(out, quality=92, dpi=(300, 300))
    print(f"OK {out} {w}x{h}")
    return out

if __name__ == "__main__":
    dirs = sorted(p.parent for p in (ROOT / "kdp").glob("*/cover.pdf")) if "--all" in sys.argv else [Path(a) for a in sys.argv[1:]]
    for d in dirs: one(d)
