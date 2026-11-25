#!/usr/bin/env python3
"""A pattern.json első horgolásrajzából (nem shape) illustration.jpg-t készít a listingképhez (Playwright).
  python3 scripts/chart_cover.py horgolas/mintak/<slug>"""
import json, sys, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent)); import crochet_charts as CC
f = Path(sys.argv[1]).resolve(); p = json.loads((f / "pattern.json").read_text())
fig = next(x for x in p["figures"] if x["fn"] != "shape")
svg = CC.render(fig, "en").replace("max-height:4.6in", "max-height:1300px"); (f / "kepek").mkdir(exist_ok=True)
html = f / "kepek" / "_chart.html"; html.write_text(f'<html><body style="margin:0;background:#fff;display:flex;align-items:center;justify-content:center;width:1500px;height:1350px"><div style="width:1250px">{svg}</div></body></html>')
js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1500,height:1350}}}});await pg.goto('file://{html}');await pg.screenshot({{path:'{f / 'kepek' / 'illustration.png'}'}});await b.close()}})()"
subprocess.run(["node", "-e", js], check=True)
from PIL import Image
Image.open(f / "kepek" / "illustration.png").convert("RGB").save(f / "kepek" / "illustration.jpg", quality=92); (f / "kepek" / "illustration.png").unlink(); html.unlink()
print("OK", f / "kepek" / "illustration.jpg")
