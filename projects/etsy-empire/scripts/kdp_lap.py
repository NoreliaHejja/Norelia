#!/usr/bin/env python3
"""KDP_FELTOLTES.md → KDP_FELTOLTES.pdf jól olvasható formában (Nóra, 2026-11-14: nagy betű, nagy sorköz).
   python3 scripts/kdp_lap.py <mappa>/KDP_FELTOLTES.md"""
import subprocess, sys
from pathlib import Path
md = Path(sys.argv[1]).resolve(); html = md.with_suffix(".html"); pdf = md.with_suffix(".pdf")
body = subprocess.run(["pandoc", str(md), "-t", "html"], capture_output=True, text=True, check=True).stdout
css = """body{font-family:'DejaVu Sans',sans-serif;font-size:20pt;line-height:1.9;color:#111;margin:0}
h1{font-size:28pt;line-height:1.3;margin:0 0 .4em}h2{font-size:24pt;margin:1.2em 0 .4em}
table{border-collapse:collapse;width:100%;table-layout:fixed}td,th{overflow-wrap:anywhere}td,th{border:1px solid #999;padding:.45em .55em;vertical-align:top;text-align:left}
td:first-child,th:first-child{font-weight:700;width:28%}p,li{margin:0 0 .7em}code{font-size:18pt}"""
html.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>", encoding="utf-8")
subprocess.run(["node", "-e", f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{html}');await p.pdf({{path:'{pdf}',format:'A4',margin:{{top:'18mm',bottom:'18mm',left:'16mm',right:'16mm'}}}});await b.close();}})();"""], check=True)
html.unlink(); print("OK", pdf)
