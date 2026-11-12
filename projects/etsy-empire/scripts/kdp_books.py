#!/usr/bin/env python3
"""
Amazon KDP fekete-fehér papírkönyvek (8.5 x 11 in, no bleed) – etsy-empire.

  python3 scripts/kdp_books.py coloring   # Christmas Coloring Book for Toddlers
  python3 scripts/kdp_books.py activity   # Kids Christmas Activity Book
  python3 scripts/kdp_books.py planner    # 2027 Family Planner
  python3 scripts/kdp_books.py pet        # Pet Care Journal
  python3 scripts/kdp_books.py familybw   # The Busy Family Planner – fekete-fehér változat

Kimenet: kdp/<slug>/interior.pdf (+ HTML a tmp/-ben). A borítót a kdp_cover.py készíti.
Vonalrajzok: kdp/linework/*.png (Higgsfield, ff). Feltöltés KÉZZEL (KDP-t nem automatizálunk).
"""
import json, random, subprocess, sys, calendar, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KDP = ROOT / "kdp"
LINE = KDP / "linework"

CSS = """
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:'Inter','DejaVu Sans',sans-serif;color:#111;background:#fff}
.page{width:8.5in;height:11in;padding:0.75in 0.75in 0.8in;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column}
.page:last-child{page-break-after:auto}
h1{font-size:30pt;margin:0 0 .15in;text-align:center;font-weight:800}
h2{font-size:20pt;margin:0 0 .12in;font-weight:800}
.sub{font-size:11pt;color:#444;margin:0 0 .2in}
.center{align-items:center;justify-content:center;text-align:center}
.img{flex:1;display:flex;align-items:center;justify-content:center}
.img img{max-width:100%;max-height:8.6in;object-fit:contain}
.foot{position:absolute;bottom:.4in;left:.75in;right:.75in;text-align:center;font-size:8pt;color:#777}
.box{border:2px solid #111;border-radius:12px;padding:.18in}
.line{border-bottom:1px solid #999;height:.36in}
table{border-collapse:collapse;width:100%}
td,th{border:1px solid #333;font-size:9pt;padding:4px;vertical-align:top}
th{background:#eee;font-weight:700}
.trace{font-size:58pt;letter-spacing:.08em;color:#bbb;font-weight:300;text-align:center;border-bottom:1px dashed #999;line-height:1.25}
"""


def html(pages, out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(pages)}</body></html>", encoding="utf-8")


def render(src: Path, dest: Path):
    subprocess.run(["node", "scripts/render_pdf.js", str(src)], check=True, cwd=ROOT)
    src.with_suffix(".pdf").replace(dest)
    n = int([l for l in subprocess.run(["pdfinfo", str(dest)], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages:")][0].split()[1])
    print(f"{dest} – {n} oldal")
    return n


def foot(t="AureliaVenn"):
    return f"<div class='foot'>{t}</div>"


def front_matter(title, sub, owner_line="This book belongs to"):
    return [
        f"<div class='page center'><h1>{title}</h1><p class='sub'>{sub}</p><div class='box' style='width:5in;margin-top:.4in'><b>{owner_line}:</b><div class='line'></div></div></div>",
        "<div class='page'><div style='margin-top:auto' class='sub'>Copyright © 2026 AureliaVenn. All rights reserved. Designed by our small shop, AureliaVenn, with the help of AI tools. "
        "No part of this book may be reproduced for resale.</div></div>",
    ]


def lineart():
    imgs = sorted(LINE.glob("*.png"))
    if len(imgs) < 24:
        sys.exit(f"Kevés vonalrajz: {len(imgs)} (kell 24) – {LINE}")
    return imgs


# ---------- puzzles ----------
def maze_svg(w, h, seed, cell=34):
    rnd = random.Random(seed)
    walls = {(x, y): {"N", "S", "E", "W"} for x in range(w) for y in range(h)}
    seen, stack = {(0, 0)}, [(0, 0)]
    d = {"N": (0, -1, "S"), "S": (0, 1, "N"), "E": (1, 0, "W"), "W": (-1, 0, "E")}
    while stack:
        x, y = stack[-1]
        opts = [(k, x + dx, y + dy, o) for k, (dx, dy, o) in d.items() if (x + dx, y + dy) in walls and (x + dx, y + dy) not in seen]
        if not opts:
            stack.pop(); continue
        k, nx, ny, o = rnd.choice(opts)
        walls[(x, y)].discard(k); walls[(nx, ny)].discard(o); seen.add((nx, ny)); stack.append((nx, ny))
    walls[(0, 0)].discard("W"); walls[(w - 1, h - 1)].discard("E")
    L = []
    for (x, y), ws in walls.items():
        X, Y = x * cell, y * cell
        if "N" in ws: L.append((X, Y, X + cell, Y))
        if "S" in ws: L.append((X, Y + cell, X + cell, Y + cell))
        if "W" in ws: L.append((X, Y, X, Y + cell))
        if "E" in ws: L.append((X + cell, Y, X + cell, Y + cell))
    lines = "".join(f"<line x1='{a}' y1='{b}' x2='{c}' y2='{e}'/>" for a, b, c, e in L)
    return (f"<svg viewBox='-40 -10 {w*cell+80} {h*cell+20}' width='100%' style='max-height:7.8in'><g stroke='#111' stroke-width='4' stroke-linecap='round'>{lines}</g>"
            f"<text x='-36' y='{cell*0.65}' font-size='20'>▶</text><text x='{w*cell+8}' y='{h*cell-cell*0.35}' font-size='20'>★</text></svg>")


def wordsearch(words, seed, n=12):
    rnd = random.Random(seed)
    g = [[""] * n for _ in range(n)]
    dirs = [(1, 0), (0, 1), (1, 1)]
    for wd in words:
        wd = wd.upper().replace(" ", "")
        for _ in range(500):
            dx, dy = rnd.choice(dirs)
            x, y = rnd.randrange(n - dx * (len(wd) - 1)), rnd.randrange(n - dy * (len(wd) - 1))
            if all(g[y + dy * i][x + dx * i] in ("", c) for i, c in enumerate(wd)):
                for i, c in enumerate(wd): g[y + dy * i][x + dx * i] = c
                break
    for row in g:
        for i in range(n):
            if not row[i]: row[i] = rnd.choice("ABCDEFGHIJKLMNOPRSTUVWY")
    cells = "".join("<tr>" + "".join(f"<td style='text-align:center;font-size:20pt;font-weight:600;width:{100/n}%;height:.48in;vertical-align:middle;border:none'>{c}</td>" for c in r) + "</tr>" for r in g)
    return f"<table style='border:3px solid #111;border-radius:10px'>{cells}</table>"


SHAPES = {  # dot-to-dot alakzatok (0..100 koordináták)
    "Star": [(50, 5), (61, 38), (96, 38), (68, 59), (79, 93), (50, 72), (21, 93), (32, 59), (4, 38), (39, 38)],
    "Christmas Tree": [(50, 4), (66, 28), (58, 28), (76, 52), (66, 52), (88, 78), (56, 78), (56, 95), (44, 95), (44, 78), (12, 78), (34, 52), (24, 52), (42, 28), (34, 28)],
    "Bell": [(50, 6), (58, 12), (62, 24), (64, 44), (70, 62), (84, 76), (16, 76), (30, 62), (36, 44), (38, 24), (42, 12)],
    "Stocking": [(30, 6), (62, 6), (62, 52), (84, 66), (86, 82), (72, 92), (44, 88), (30, 72)],
    "Gift": [(14, 30), (86, 30), (86, 46), (80, 46), (80, 94), (20, 94), (20, 46), (14, 46)],
    "Candy Cane": [(40, 94), (40, 30), (44, 16), (56, 8), (70, 12), (78, 24), (78, 36), (68, 36), (66, 24), (58, 20), (52, 26), (52, 94)],
    "Heart": [(50, 30), (60, 16), (76, 12), (90, 22), (92, 40), (80, 60), (50, 88), (20, 60), (8, 40), (10, 22), (24, 12), (40, 16)],
    "House": [(50, 8), (90, 44), (80, 44), (80, 92), (20, 92), (20, 44), (10, 44)],
}


def dots_svg(pts):
    s = "".join(f"<circle cx='{x*6}' cy='{y*6}' r='5'/><text x='{x*6+8}' y='{y*6-8}' font-size='20' font-weight='700'>{i+1}</text>" for i, (x, y) in enumerate(pts))
    return f"<svg viewBox='-20 -20 650 650' width='100%' style='max-height:7.6in'><g fill='#111'>{s}</g></svg>"


# ---------- books ----------
def coloring():
    slug = "christmas-coloring-book-toddlers"
    imgs = lineart()
    pages = front_matter("My Big Christmas Coloring Book", "24 cute holiday pictures for little hands · ages 2–5")
    pages.append("<div class='page'><h2>Hello, little artist!</h2><p class='sub'>Every picture has a blank back so markers don't bleed through. "
                 "Try your colors on this page first.</p><div style='display:grid;grid-template-columns:repeat(4,1fr);gap:.2in;margin-top:.3in'>"
                 + "".join("<div class='box' style='height:1.2in'></div>" for _ in range(12)) + "</div></div>")
    for p in imgs[:24]:
        pages.append(f"<div class='page'><div class='img'><img src='../../linework/{p.name}'></div>{foot()}</div>")
        pages.append("<div class='page'></div>")
    pages.append("<div class='page center'><h1>Great job!</h1><p class='sub'>You finished your Christmas coloring book.</p><div class='box' style='width:5in'>Signed by Santa's helper: <div class='line'></div></div></div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


def activity():
    slug = "kids-christmas-activity-book"
    imgs = lineart()
    words = [["SANTA", "ELF", "TREE", "STAR", "GIFT", "SNOW", "BELL", "TOYS"], ["COOKIE", "MILK", "SLEIGH", "REINDEER", "ANGEL", "CANDY"],
             ["WREATH", "STOCKING", "HOLLY", "LIGHTS", "MITTEN", "SCARF"], ["SNOWMAN", "CAROL", "PEACE", "JOY", "HUG", "FAMILY"],
             ["PENGUIN", "OWL", "BEAR", "PUPPY", "KITTEN", "BUNNY"], ["CHIMNEY", "GLOVES", "SLED", "ICE", "SKATE", "COCOA"],
             ["RIBBON", "BOW", "WRAP", "CARD", "NOEL", "MERRY"], ["GINGER", "BAKE", "SPRINKLE", "PIE", "CAKE", "TREAT"]]
    pages = front_matter("Kids Christmas Activity Book", "Mazes, word search, dot-to-dot, tracing and coloring · ages 4–8")
    pages.append("<div class='page'><h2>What's inside</h2><div class='box'><p>• 10 Christmas mazes</p><p>• 8 word searches</p><p>• 8 dot-to-dot pictures</p>"
                 "<p>• 6 tracing & drawing pages</p><p>• 12 coloring pages</p><p>• Answers are easy to check with a grown-up!</p></div></div>")
    acts = []
    for i in range(10):
        acts.append(f"<div class='page'><h2>Maze {i+1}: Help Santa find the star!</h2><div class='img'>{maze_svg(10+i//2, 12+i//2, 100+i)}</div>{foot()}</div>")
    for i, ws in enumerate(words):
        acts.append(f"<div class='page'><h2>Word Search {i+1}</h2><p class='sub'>Find: {' · '.join(ws)}</p>{wordsearch(ws, 200+i)}{foot()}</div>")
    for name, pts in SHAPES.items():
        acts.append(f"<div class='page'><h2>Connect the dots: {name}</h2><p class='sub'>Start at 1 and connect all the dots, then color it in!</p><div class='img'>{dots_svg(pts)}</div>{foot()}</div>")
    for wd in ["MERRY", "CHRISTMAS", "SANTA", "SNOW"]:
        acts.append(f"<div class='page'><h2>Trace the word</h2>" + "".join(f"<div class='trace'>{wd}</div>" for _ in range(5)) + f"{foot()}</div>")
    acts.append("<div class='page'><h2>Draw your Christmas tree</h2><div class='box' style='flex:1'></div></div>")
    acts.append("<div class='page'><h2>My letter to Santa</h2><p class='sub'>Dear Santa, this year I was kind when I…</p>" + "<div class='line'></div>" * 16 + "</div>")
    for k, p in enumerate(imgs[:12]):
        acts.insert(4 * k + 2, f"<div class='page'><div class='img'><img src='../../linework/{p.name}'></div>{foot()}</div>")
    pages += acts
    pages.append("<div class='page center'><h1>Christmas Champion!</h1><p class='sub'>This certificate is awarded to</p><div class='box' style='width:5in'><div class='line'></div></div><p class='sub' style='margin-top:.3in'>for finishing the whole activity book.</p></div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


def planner():
    slug = "family-planner-2027"
    pages = front_matter("2027 Family Planner", "Monthly & weekly pages for busy parents · Jan–Dec 2027", "This planner belongs to")
    cal = calendar.Calendar(firstweekday=6)
    yr = "".join(f"<div class='box' style='padding:.08in'><b>{calendar.month_name[m]}</b><table style='margin-top:4px'>" + "<tr>" + "".join(f"<th style='font-size:7pt'>{d}</th>" for d in "SMTWTFS") + "</tr>"
                 + "".join("<tr>" + "".join(f"<td style='font-size:7pt;text-align:center;border:none'>{d or ''}</td>" for d in wk) + "</tr>" for wk in cal.monthdayscalendar(2027, m)) + "</table></div>" for m in range(1, 13))
    pages.append(f"<div class='page'><h2>2027 at a glance</h2><div style='display:grid;grid-template-columns:repeat(3,1fr);gap:.12in'>{yr}</div></div>")
    pages.append("<div class='page'><h2>Our family goals for 2027</h2>" + "".join(f"<div class='box' style='margin-bottom:.12in'><b>{t}</b><div class='line'></div><div class='line'></div></div>" for t in ["Health", "Home", "Money", "Fun & trips", "Kids", "Just for me"]) + "</div>")
    pages.append("<div class='page'><h2>Birthdays & important dates</h2><table>" + "".join(f"<tr><th style='width:1.4in'>{calendar.month_name[m]}</th><td style='height:.62in'></td></tr>" for m in range(1, 13)) + "</table></div>")
    for m in range(1, 13):
        rows = "".join("<tr>" + "".join(f"<td style='height:1.3in;font-size:9pt'>{d or ''}</td>" for d in wk) + "</tr>" for wk in cal.monthdayscalendar(2027, m))
        pages.append(f"<div class='page'><h2>{calendar.month_name[m]} 2027</h2><table><tr>" + "".join(f"<th>{d}</th>" for d in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]) + f"</tr>{rows}</table></div>")
        pages.append(f"<div class='page'><h2>{calendar.month_name[m]}: plans & notes</h2><div style='display:grid;grid-template-columns:1fr 1fr;gap:.2in;flex:1'>"
                     + "".join(f"<div class='box'><b>{t}</b>" + "<div class='line'></div>" * 8 + "</div>" for t in ["Top 3 this month", "Appointments", "Meals to try", "Kids & school"]) + "</div></div>")
        for wk in [datetime.date(2027, 1, 3) + datetime.timedelta(days=7 * i) for i in range(52)]:
            if wk.month != m:
                continue
            days = "".join(f"<div class='box' style='padding:.08in'><b>{(wk+datetime.timedelta(days=i)).strftime('%a %b %-d')}</b>" + "<div class='line' style='height:.3in'></div>" * 3 + "</div>" for i in range(7))
            pages.append(f"<div class='page'><h2>Week of {wk.strftime('%B %-d')}</h2><div style='display:grid;grid-template-columns:1fr 1fr;gap:.1in'>{days}"
                         "<div class='box' style='padding:.08in'><b>Meals · To-do · Kids</b>" + "<div class='line' style='height:.3in'></div>" * 3 + "</div></div></div>")
    for _ in range(4):
        pages.append("<div class='page'><h2>Notes</h2>" + "<div class='line'></div>" * 24 + "</div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


def pet():
    slug = "pet-care-journal"
    pages = front_matter("My Pet Care Journal", "Health, vet visits, feeding and happy memories · for cats and dogs", "My pet's name")
    pages.append("<div class='page'><h2>Pet profile</h2><div class='box' style='height:3in;margin-bottom:.2in;text-align:center'>Paste a photo here</div><table>"
                 + "".join(f"<tr><th style='width:2.2in'>{t}</th><td style='height:.4in'></td></tr>" for t in ["Name", "Species / breed", "Birthday / adoption day", "Color & markings", "Microchip number", "Favorite food", "Favorite toy", "Vet & phone", "Emergency vet", "Insurance"]) + "</table></div>")
    pages.append("<div class='page'><h2>Vaccinations</h2><table><tr><th>Date</th><th>Vaccine</th><th>Next due</th><th>Vet</th></tr>" + "<tr><td style='height:.42in'></td><td></td><td></td><td></td></tr>" * 18 + "</table></div>")
    pages.append("<div class='page'><h2>Flea, tick & worm treatments</h2><table><tr><th>Date</th><th>Product</th><th>Next due</th><th>Notes</th></tr>" + "<tr><td style='height:.42in'></td><td></td><td></td><td></td></tr>" * 18 + "</table></div>")
    pages.append("<div class='page'><h2>Weight log</h2><table><tr><th>Date</th><th>Weight</th><th>Notes</th></tr>" + "<tr><td style='height:.42in'></td><td></td><td></td></tr>" * 18 + "</table></div>")
    for i in range(12):
        pages.append(f"<div class='page'><h2>Vet visit</h2><table>" + "".join(f"<tr><th style='width:2in'>{t}</th><td style='height:.5in'></td></tr>" for t in ["Date", "Reason", "Weight", "Diagnosis", "Treatment / medicine", "Cost", "Follow-up"]) + "</table><p class='sub' style='margin-top:.2in'>Notes</p>" + "<div class='line'></div>" * 6 + "</div>")
    for w in range(52):
        rows = "".join(f"<tr><th>{d}</th><td></td><td></td><td></td><td></td></tr>" for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        pages.append(f"<div class='page'><h2>Weekly care log</h2><p class='sub'>Week of: ______________</p><table><tr><th style='width:.8in'>Day</th><th>Food</th><th>Water</th><th>Walk / play</th><th>Mood & notes</th></tr>{rows.replace('<td></td>', '<td style=\"height:.9in\"></td>')}</table>"
                     "<p class='sub' style='margin-top:.15in'>Planning aid, not veterinary advice.</p></div>")
    for _ in range(6):
        pages.append("<div class='page'><h2>Happy memories</h2><div class='box' style='flex:1'></div></div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


def familybw():
    slug = "busy-family-planner-bw"
    src = KDP / "busy-family-planner-book" / "interior.pdf"
    out = KDP / slug / "interior.pdf"; out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.parent / "tmp"; tmp.mkdir(exist_ok=True)
    subprocess.run(["pdftoppm", "-r", "300", "-gray", "-png", str(src), str(tmp / "p")], check=True)
    subprocess.run(["convert", *sorted(map(str, tmp.glob("p-*.png"))), "-units", "PixelsPerInch", "-density", "300", str(out)], check=True)
    n = int([l for l in subprocess.run(["pdfinfo", str(out)], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages:")][0].split()[1])
    print(out, n)
    return slug, n


if __name__ == "__main__":
    fn = {"coloring": coloring, "activity": activity, "planner": planner, "pet": pet, "familybw": familybw}[sys.argv[1]]
    slug, n = fn()
    meta = KDP / slug / "meta.json"
    meta.write_text(json.dumps({"slug": slug, "pages": n}, indent=2))
