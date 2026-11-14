#!/usr/bin/env python3
"""Arc nélküli karakter → átlátszó háttér + átlátszó arclyuk (PNG).
   python3 scripts/face_hole.py be.png ki.png
A legnagyobb, a kép szélétől elzárt, közel fehér régió a felső 60%-ban = arc."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage
im = Image.open(sys.argv[1]).convert("RGBA"); a = np.array(im)
white = (a[..., :3].min(axis=2) > 235)
lab, n = ndimage.label(white)
h, w = white.shape
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
alpha = np.full((h, w), 255, np.uint8)
for b in border: alpha[lab == b] = 0  # háttér
# arc: elzárt fehér régiók közül a legnagyobb, a felső 60%-ban, legalább a kép 1,2%-a
best, bs = None, 0
for i in range(1, n + 1):
    if i in border: continue
    m = lab == i; s = m.sum()
    ys = np.nonzero(m)[0]
    xs_ = np.nonzero(m)[1]
    bh_, bw_ = ys.max() - ys.min() + 1, xs_.max() - xs_.min() + 1
    fill, asp = s / (bh_ * bw_), bw_ / bh_
    # arc = ellipszis: kitöltés ~0,785 (0,68–0,86), arány 0,55–1,45 (az angyal fehér ruhája nem ilyen)
    if s > bs and s > 0.012 * h * w and ys.mean() < 0.6 * h and 0.68 < fill < 0.86 and 0.55 < asp < 1.45:
        best, bs = i, s
if best is None:
    sys.exit("HIBA: nincs arc-régió")
face = ndimage.binary_dilation(lab == best, iterations=3)
alpha[face] = 0
a[..., 3] = alpha
ys, xs = np.nonzero(alpha)
Image.fromarray(a).crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)).save(sys.argv[2])
fy, fx = np.nonzero(lab == best)
print(f"OK {sys.argv[2]} arc: {bs/(h*w)*100:.1f}% közép=({fx.mean()/w:.2f},{fy.mean()/h:.2f})")
