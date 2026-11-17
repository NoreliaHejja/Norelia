#!/usr/bin/env python3
"""Meglévő KDP papírborító javítása (2026-11-17):
- vonalkód-doboz pontosan a KDP helyére (2 x 1,2 in, 0,25 in-re a gerinctől és az alsó vágóéltől); a régi (0,375 in) doboz helyét háttérszínnel fedi
- 100 oldal alatt a gerincfelirat eltávolítása (KDP-szabály)
  python3 scripts/kdp_cover_fix.py kdp/<csomag> <trim_w> <trim_h>
"""
import subprocess, sys, shutil
from pathlib import Path
from PIL import Image, ImageDraw
d = Path(sys.argv[1]); TW, TH = float(sys.argv[2]), float(sys.argv[3]); DPI = 300
n = int([l for l in subprocess.run(["pdfinfo", str(d / "interior.pdf")], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages")][0].split()[1])
sp = n * 0.002252
bak = d / "cover-regi.pdf"
if not bak.exists(): shutil.copy(d / "cover.pdf", bak)
tmp = d / "_fix"; subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-singlefile", str(bak), str(tmp)], check=True)
im = Image.open(str(tmp) + ".png").convert("RGB"); Path(str(tmp) + ".png").unlink()
W, H = im.size; dr = ImageDraw.Draw(im)
xs0, xs1 = int((0.125 + TW) * DPI), int((0.125 + TW + sp) * DPI)  # gerinc
# régi doboz: jobb éle 0,375 in-re a gerinctől, alja 0,375 in-re a lap aljától
ox1, oy1 = xs0 - int(0.375 * DPI), H - int(0.375 * DPI)
bg = im.getpixel((ox1 - int(2 * DPI) - 30, oy1 - int(1.2 * DPI) - 30))
dr.rectangle((ox1 - int(2 * DPI) - 3, oy1 - int(1.2 * DPI) - 3, xs0 - 1, oy1 + 3), fill=bg)
nx1, ny1 = xs0 - int(0.25 * DPI), H - int(0.375 * DPI)
dr.rectangle((nx1 - int(2 * DPI), ny1 - int(1.2 * DPI), nx1, ny1), fill="white")
if n < 100:
    sc = im.getpixel(((xs0 + xs1) // 2, 3))
    dr.rectangle((xs0, 0, xs1, H), fill=sc)
im.save(d / "cover.pdf", "PDF", resolution=DPI)
print(d, f"{W/DPI:.3f} x {H/DPI:.3f} in, {n} oldal, gerinc {sp:.3f}, háttér {bg}")
