#!/usr/bin/env python3
"""
KDP paperback bundle: több kész termék funkcionális oldalaiból egy 24+ oldalas könyv.

  python3 scripts/build_kdp_bundle.py

Kimenet: kdp/<book-slug>/ → interior.pdf (8.5x11, no bleed), cover.pdf (teljes borító, gerinccel),
KDP_FELTOLTES.md (mezőnként kitöltve). Feltöltés KÉZZEL (kdp.amazon.com) – KDP-t nem automatizálunk.
"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common import icon  # noqa: E402

BOOK = {
    "slug": "busy-family-planner-book",
    "title": "The Busy Family Planner",
    "subtitle": "Meal Plans, Kids Routines, Cooking Together and Pet Care Pages for Families with Little Kids",
    "author": "AureliaVenn",
    "price_usd": "9.99",
    "sections": [  # (termék-slug, szakaszcím, rövid leírás, ikon, borítókép-kulcs)
        ("family-meal-planner", "Meals & Groceries", "Plan the week, write one grocery list, let your child pick a meal.", "cart", "meal"),
        ("cook-with-me-recipe-cards", "Cook With Me", "Picture recipes your preschooler can follow, step by step.", "spoon", "cook"),
        ("routine-cards", "Morning & Bedtime", "Calm routines with picture steps for little ones.", "sun", "routine"),
        ("ready-for-a-dog-kit", "Ready for a Dog?", "A gentle family plan before saying yes to a dog.", "heart", "dog"),
        ("cat-enrichment-planner", "Happy Indoor Cat", "Play, rest and safe-home pages for the family cat.", "cat", "cat"),
    ],
    "pages": [3, 4, 5, 6, 7],  # minden termék funkcionális oldalai
}
COLORS = ["#2E8B57", "#E4572E", "#E85D75", "#D7263D", "#13889B"]


def wrapper_html(out: Path):
    css = (ROOT / "assets/base.css").read_text()
    s = BOOK["sections"]
    pages = []
    pages.append(f'''<div class="page cover"><div class="eyebrow">A planner &amp; activity book</div>
      <h1 style="margin-top:18px">{BOOK["title"]}</h1><div class="tag">{BOOK["subtitle"]}</div>
      <div class="accent-line"></div><div class="foot">{BOOK["author"]}</div></div>''')
    pages.append(f'''<div class="page"><div style="position:absolute;bottom:1in;left:.75in;right:.75in" class="mini">
      <p><b>{BOOK["title"]}</b><br>{BOOK["subtitle"]}</p>
      <p>Copyright &copy; 2026 {BOOK["author"]}. All rights reserved. No part of this book may be reproduced for resale.</p>
      <p>Designed by our small shop, AureliaVenn, with the help of AI tools. The pet pages are a planning aid, not veterinary advice.
      The cooking pages are meant for cooking together with an adult; always check for allergies.</p></div></div>''')
    rows = "".join(f'<div class="ck"><span class="chk" style="border-color:{COLORS[i]}"></span><b style="width:2.6in">{t}</b><span class="mini">{d}</span></div>'
                   for i, (_, t, d, _, _) in enumerate(s))
    pages.append(f'''<div class="page"><div class="eyebrow">Inside this book</div><h1 class="page-title">Contents</h1>
      <p class="subtitle">Five small systems for a calmer family week. Use them in any order. Write in pencil if you want to reuse a page.</p>
      <div class="card">{rows}</div>
      <div class="card warm" style="margin-top:18px"><h3>How to use this book</h3><p class="mini">Pick one section for this week.
      Fill it in together with your child at the kitchen table, then come back next week. Small steps, every week.</p></div></div>''')
    divs = []
    for i, (_, t, d, ic, _) in enumerate(s):
        divs.append(f'''<div class="page" style="background:{COLORS[i]};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff">
          <div style="width:1.6in;height:1.6in;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center">{icon(ic, 80, COLORS[i], 1.4)}</div>
          <div style="font-size:11pt;letter-spacing:.25em;margin-top:30px">PART {i+1}</div>
          <h1 style="font-size:36pt;margin:10px 0 0">{t}</h1><p style="font-size:12pt;max-width:5in;line-height:1.5">{d}</p></div>''')
    notes = '''<div class="page"><div class="eyebrow">Notes</div><h1 class="page-title">Family notes</h1>''' + '<div class="wline"></div>' * 24 + '</div>'
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pages)}{"".join(divs)}{notes*3}</body></html>'
    out.write_text(html, encoding="utf-8")


def run(*a):
    subprocess.run(a, check=True, cwd=ROOT)


def build():
    od = ROOT / "kdp" / BOOK["slug"]
    (od / "tmp").mkdir(parents=True, exist_ok=True)
    w = od / "tmp" / "wrapper.html"
    wrapper_html(w)
    run("node", "scripts/render_pdf.js", str(w))
    wp = w.with_suffix(".pdf")
    run("pdfseparate", str(wp), str(od / "tmp/w-%d.pdf"))
    parts = [od / "tmp/w-1.pdf", od / "tmp/w-2.pdf", od / "tmp/w-3.pdf"]
    for i, (slug, *_r) in enumerate(BOOK["sections"]):
        parts.append(od / f"tmp/w-{4+i}.pdf")
        src = ROOT / "termekek" / slug / f"{slug}.pdf"
        for p in BOOK["pages"]:
            o = od / f"tmp/{slug}-{p}.pdf"
            run("pdfseparate", "-f", str(p), "-l", str(p), str(src), str(o))
            parts.append(o)
    for n in range(9, 12):
        parts.append(od / f"tmp/w-{n}.pdf")
    run("pdfunite", *map(str, parts), str(od / "interior.pdf"))
    n = int([l for l in subprocess.run(["pdfinfo", str(od / "interior.pdf")], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages:")][0].split()[1])
    cover(od, n)
    return od, n


def cover(od: Path, pages: int):
    dpi = 300
    spine = pages * 0.002252
    W, H = int((0.125 * 2 + 8.5 * 2 + spine) * dpi), int(11.25 * dpi)
    img = Image.new("RGB", (W, H), "#FFF8EC")
    d = ImageDraw.Draw(img)
    FX = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
    FB = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
    FR = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
    fx0 = int((0.125 + 8.5 + spine) * dpi)  # front panel x
    fw = int(8.625 * dpi)
    # front: colorful top band + 2x2 photo grid + 1
    d.rectangle((fx0, 0, W, int(3.2 * dpi)), fill="#E4572E")
    cx = fx0 + int(4.25 * dpi)
    d.text((cx, int(1.35 * dpi)), BOOK["title"], font=ImageFont.truetype(FX, 150), fill="white", anchor="mm")
    sub = ImageFont.truetype(FB, 62)
    for k, line in enumerate(["Meal Plans · Kids Routines · Cooking Together", "Pet Care Pages for Families with Little Kids"]):
        d.text((cx, int(2.2 * dpi) + k * 95), line, font=sub, fill="white", anchor="mm")
    src = Path("/tmp/claude-0/-home-user-Norelia/2c49c0c7-1128-5551-a1d7-05adc4d6a783/scratchpad/covers")
    keys = [s[4] for s in BOOK["sections"]]
    tile_w, tile_h = int(2.6 * dpi), int(3.25 * dpi)
    pos = [(0, 0), (1, 0), (2, 0), (0.5, 1), (1.5, 1)]
    gx0 = fx0 + int(0.4 * dpi)
    gy0 = int(3.5 * dpi)
    for (col, row), k in zip(pos, keys):
        p = src / f"{k}.png"
        if not p.exists():
            p = ROOT / "termekek" / [s[0] for s in BOOK["sections"] if s[4] == k][0] / "kepek/01-cover.jpg"
        t = Image.open(p).convert("RGB")
        r = max(tile_w / t.width, tile_h / t.height)
        t = t.resize((int(t.width * r), int(t.height * r)))
        t = t.crop(((t.width - tile_w) // 2, (t.height - tile_h) // 2, (t.width - tile_w) // 2 + tile_w, (t.height - tile_h) // 2 + tile_h))
        x, y = gx0 + int(col * (tile_w + 0.13 * dpi)), gy0 + int(row * (tile_h + 0.15 * dpi))
        img.paste(t, (x, y))
        d.rectangle((x, y, x + tile_w, y + tile_h), outline="white", width=14)
    d.text((cx, H - int(0.55 * dpi)), BOOK["author"].upper(), font=ImageFont.truetype(FB, 60), fill="#1F2A44", anchor="mm")
    # back
    bx = int(0.125 * dpi) + int(0.6 * dpi)
    d.rectangle((0, 0, fx0 - int(spine * dpi), H), fill="#13889B")
    by = int(1.0 * dpi)
    d.text((bx, by), "A calmer family week,", font=ImageFont.truetype(FX, 100), fill="white")
    d.text((bx, by + 130), "one page at a time.", font=ImageFont.truetype(FX, 100), fill="white")
    body = ["Five small systems in one book:", "", "• Weekly meal plans and grocery lists", "• Picture recipe cards to cook with your preschooler",
            "• Morning and bedtime routine charts", "• A gentle 'Ready for a dog?' family plan", "• Play and safe-home pages for the family cat",
            "", "8.5 × 11 in · write-in pages · for families with kids ages 2–6", "", "Designed by AureliaVenn with the help of AI tools.",
            "Pet pages are a planning aid, not veterinary advice."]
    fr = ImageFont.truetype(FR, 54)
    for k, line in enumerate(body):
        d.text((bx, by + 420 + k * 80), line, font=fr, fill="white")
    # barcode-hely (KDP teszi rá): 2 x 1.2 in, jobb alsó sarok, 0.25 in-re a széltől
    bw, bh = int(2 * dpi), int(1.2 * dpi)
    bxe = fx0 - int(spine * dpi) - int(0.25 * dpi) - int(0.125 * dpi)
    d.rectangle((bxe - bw, H - int(0.375 * dpi) - bh, bxe, H - int(0.375 * dpi)), fill="white")
    img.save(od / "cover.pdf", "PDF", resolution=dpi)
    img.resize((W // 6, H // 6)).save(od / "cover-preview.jpg", quality=85)


def sheet(od: Path, n: int):
    s = BOOK
    md = f"""# KDP feltöltés – {s['title']}

Kézi feltöltés: kdp.amazon.com → Create → **Paperback**. (~15 perc)

| Mező | Érték |
|---|---|
| Language | English |
| Book Title | {s['title']} |
| Subtitle | {s['subtitle']} |
| Author | {s['author']} |
| Description | lásd lent |
| Publishing rights | I own the copyright |
| Primary audience | Adult content: No; reading age: üresen |
| Categories (3) | Self-Help › Journal Writing; Family & Relationships › Parenting › General; House & Home › Cooking for Kids (vagy: Crafts, Hobbies & Home › Home Management) |
| Keywords (7) | family planner for moms; meal planner with grocery list; toddler routine chart book; cooking with kids recipe book; new dog planner for kids; cat care planner; weekly family organizer |
| AI-generated content | **Yes** – Images: AI-generated (borító fotók); Text: AI-assisted, edited |
| ISBN | Free KDP ISBN |
| Print options | Black & white interior? **NEM → Premium color interior**, white paper, **8.5 × 11 in**, **No bleed**, Matte cover |
| Manuscript | `interior.pdf` ({n} oldal) |
| Book cover | Upload a cover you already have → `cover.pdf` |
| Price | {s['price_usd']} USD (prémium színes nyomásnál a nyomdaköltség ~$7–8, ezért ennél lejjebb ne) – a Previewer után nézd meg a royalty-t, ha 0,5 $ alatt van, emeld 12,99-re |

## Description (bemásolható)
Plan the week, cook together, build calm routines and get the family ready for a pet – all in one write-in book.

**Inside ({n} pages, 8.5 × 11 in):**
- Weekly meal plans, a "my pick" page for kids and grocery lists
- Picture recipe cards your preschooler can follow
- Morning and bedtime routine charts with picture steps
- A gentle "Ready for a dog?" family plan with a kids helper chart
- Play, rest and safe-home pages for the family cat
- Family notes pages

Made for busy parents of kids ages 2–6 who want a calmer, more organized week.

Designed by our small shop, AureliaVenn, with the help of AI tools. Pet pages are a planning aid, not veterinary advice.

## Ellenőrzés feltöltés előtt
- [ ] A Previewerben nincs „text outside margin” hiba (ha van: Nóra jelez, javítom)
- [ ] Gerinc: {n} oldalnál nincs gerincfelirat (79 oldal alatt a KDP nem enged) – a borító ezt tudja
"""
    (od / "KDP_FELTOLTES.md").write_text(md, encoding="utf-8")


if __name__ == "__main__":
    od, n = build()
    sheet(od, n)
    print("Kész:", od, n, "oldal")
