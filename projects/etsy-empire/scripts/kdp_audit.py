#!/usr/bin/env python3
"""Minden KDP-csomag ellenőrzése: belív mérete, borító = 2×W+0,25+oldal×gerinc × H+0,25, 0,25 in-es biztonsági sáv a belívben.
   python3 scripts/kdp_audit.py   (kdp/* és books/*/out)"""
import subprocess, re, json, sys
from pathlib import Path
import numpy as np
from PIL import Image
ROOT = Path(__file__).resolve().parent.parent
def info(p):
    t = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True).stdout
    w, h = re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", t).groups(); n = int(re.search(r"Pages:\s+(\d+)", t).group(1))
    return float(w) / 72, float(h) / 72, n
def band_hits(pdf, tmp):
    tmp.mkdir(exist_ok=True); subprocess.run(["pdftoppm", "-r", "30", "-gray", "-png", str(pdf), str(tmp / "a")], check=True)
    bad = []; b = int(.25 * 30)
    for f in sorted(tmp.glob("a-*.png")):
        a = np.array(Image.open(f)); e = np.concatenate([a[:b].ravel(), a[-b:].ravel(), a[:, :b].ravel(), a[:, -b:].ravel()])
        if (e < 200).sum() > 3: bad.append(int(f.stem.split("-")[1]))
        f.unlink()
    return bad
folders = sorted(p for p in (ROOT / "kdp").iterdir() if (p / "interior.pdf").exists()) + sorted(p / "out" for p in (ROOT / "books").iterdir() if (p / "out" / "interior.pdf").exists())
ok = True
for d in folders:
    w, h, n = info(d / "interior.pdf")
    color = "color" in (d / "KDP_FELTOLTES.md").read_text().lower().split("paperback")[-1][:300] if (d / "KDP_FELTOLTES.md").exists() else False
    sp = 0.002347 if color else 0.002252
    msg = [f"belív {w:.3f}x{h:.3f}, {n} old."]
    if (d / "cover.pdf").exists():
        cw, ch, _ = info(d / "cover.pdf"); ew, eh = 2 * w + .25 + n * sp, h + .25
        good = abs(cw - ew) < .015 and abs(ch - eh) < .015
        msg.append(f"borító {cw:.3f}x{ch:.3f} (elvárt {ew:.3f}x{eh:.3f}) {'OK' if good else 'HIBÁS'}")
        ok &= good
    bad = band_hits(d / "interior.pdf", d / "_audit")
    (d / "_audit").rmdir()
    msg.append("szélső sáv OK" if not bad else f"KILÓG {len(bad)} oldalon: {bad[:12]}")
    ok &= not bad
    print(f"{d.relative_to(ROOT)}: " + " | ".join(msg))
sys.exit(0 if ok else 1)
