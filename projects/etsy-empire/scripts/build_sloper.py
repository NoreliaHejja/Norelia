#!/usr/bin/env python3
"""Szabásminta-generátor (szabas/README.md). Paraméteres szerkesztés mérettáblázatból, egymásba ágyazott méretekkel.
  python3 scripts/build_sloper.py szabas/mintak/<slug>
pattern.json: {"slug","type": "skirt_block"|..., "sizes": [...], "name_en","name_de", ...}
Kimenet a mappában: <slug>-A4.pdf, <slug>-Letter.pdf (csempézett, átfedő jelekkel, tesztnégyzettel),
<slug>-A0.pdf (copyshop), <slug>-layout.png (listingképhez), majd az útmutató HTML-jét a build_sloper_guide() írja.
Új típus: írj egy draft_<type>(m) függvényt, ami darabokat ad vissza: [{"name","cut","paths":[[(x,y),...]], "lines":[...], "notches":[...], "grain":((x,y),(x,y)), "fold": bool}] cm-ben."""
import json, math, sys
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch

# Női testméret-táblázat (cm) – saját, általános táblázat
SIZES = {
    "XS": dict(bust=80, waist=62, hip=88, hipdepth=20.0), "S": dict(bust=86, waist=68, hip=94, hipdepth=20.5),
    "M": dict(bust=92, waist=74, hip=100, hipdepth=21.0), "L": dict(bust=100, waist=82, hip=108, hipdepth=21.0),
    "XL": dict(bust=108, waist=90, hip=116, hipdepth=21.5), "2X": dict(bust=116, waist=98, hip=124, hipdepth=22.0),
    "3X": dict(bust=124, waist=106, hip=132, hipdepth=22.0),
}
COLORS = {"XS": (0.55, 0.2, 0.7), "S": (0.1, 0.4, 0.8), "M": (0.0, 0.55, 0.45), "L": (0.85, 0.55, 0.0),
          "XL": (0.8, 0.15, 0.15), "2X": (0.45, 0.3, 0.15), "3X": (0.2, 0.2, 0.2)}
DASH = {"XS": [], "S": [6, 3], "M": [], "L": [2, 2], "XL": [], "2X": [8, 3, 2, 3], "3X": [4, 4]}


def qbez(p0, p1, p2, n=24):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]) for t in (i / n for i in range(n + 1))]


def draft_skirt_block(m, length=60.0):
    """Egyenes alapszoknya: eleje (hajtásra) + háta (2 db), varrásráhagyás nélkül. Hip ease 4 cm, waist ease 1 cm."""
    pieces = []
    for side in ("front", "back"):
        sh = 0.5 if side == "front" else -0.5
        hx = m["hip"] / 4 + 1 + sh                     # csípő negyed + bőség
        wfin = m["waist"] / 4 + 0.25 + sh              # kész derék negyed
        sup = hx - wfin                                # elvétel összesen
        side_take = min(max(sup * 0.45, 1.5), 4.0)
        dart_total = sup - side_take
        if side == "front":
            n = 2 if dart_total > 3.0 else 1; dlen = 9.0; centers = [8.0, 12.0] if n == 2 else [9.0]
        else:
            n = 2 if dart_total > 4.0 else 1; dlen = 14.0; centers = [7.5, 12.5] if n == 2 else [9.5]
        d = dart_total / n
        wx = hx - side_take; raise_ = 1.25
        cb = 1.0 if side == "back" else 0.0          # hátközép derék 1 cm-rel lejjebb
        yw = lambda x: cb - (cb + raise_) * (x / wx) ** 2
        hd = m["hipdepth"]
        # waist line with darts
        waist = [(0.0, yw(0.0))]; darts = []
        for c in centers:
            l, r = c - d / 2, c + d / 2
            waist += [(l, yw(l)), (c, dlen), (r, yw(r))]
            darts.append([(l, yw(l)), (c, dlen), (r, yw(r))])
        waist.append((wx, yw(wx)))
        side_curve = qbez((wx, yw(wx)), (hx, hd * 0.25), (hx, hd))
        outline = waist + side_curve[1:] + [(hx, length), (0.0, length), (0.0, yw(0.0))]
        pieces.append(dict(name=side, outline=outline, darts=darts, hipline=((0, hd), (hx, hd)),
                           grain=((hx * 0.55, 8), (hx * 0.55, length - 8)), fold=(side == "front"),
                           cut={"front": "1 on fold", "back": "2"}[side], w=hx, h=length))
    return pieces


def draft_aline_skirt(m, length=58.0, flare=5.0, sa=1.5):
    """A-vonalú szoknya a blokkból: oldalvarrás a csípővonaltól a szegélyig flare cm-rel kifelé + egyenes derékpánt.
    Varrásráhagyás nélkül rajzolva (sa csak a leírásban)."""
    pcs = draft_skirt_block(m, length)
    for pc in pcs:
        hd = pc["hipline"][1][1]; hx = pc["w"]
        pc["outline"] = [pt for pt in pc["outline"] if not (pt[1] == length)]
        out = []
        for x, y in pc["outline"]:
            out.append((x, y))
            if abs(x - hx) < 1e-9 and abs(y - hd) < 1e-9:
                out += [(hx + flare, length), (0.0, length)]
        pc["outline"] = out + [pc["outline"][0]]; pc["w"] = hx + flare
    wb_len = m["waist"] + 1 + 3          # derék + bőség + átfedés
    hl = wb_len / 2                      # fél bund, a hajtás az elején (eleje közép)
    pcs.append(dict(name="waistband", outline=[(0, 0), (7, 0), (7, hl), (0, hl), (0, 0)], darts=[], hipline=None,
                    grain=((3.5, 4), (3.5, hl - 4)), fold=False, cut="1", w=7, h=hl))
    return pcs


DRAFTS = {"skirt_block": draft_skirt_block, "aline_skirt": draft_aline_skirt}


def layout(p):
    """Darabok elhelyezése (cm): minden darab a legnagyobb méretének szélességével egymás mellett."""
    sizes = p["sizes"]; drafts = {s: DRAFTS[p["type"]](SIZES[s], **p.get("params", {})) for s in sizes}
    n = len(drafts[sizes[0]]); x = 3.0; placed = []
    for i in range(n):
        wmax = max(drafts[s][i]["w"] for s in sizes); hmax = max(drafts[s][i]["h"] for s in sizes)
        placed.append(dict(ox=x, oy=9.0, items={s: drafts[s][i] for s in sizes}, w=wmax, h=hmax)); x += wmax + 5
    W = x; H = 9 + max(pl["h"] for pl in placed) + 5
    return placed, W, H


def draw_all(c, p, placed, H, lang="en"):
    """Rajz cm-koordinátákban; a canvas előtte (0,0)-ra van tolva. y lefelé nő → átfordítjuk."""
    T = lambda x, y: (x * cm, (H - y) * cm)
    labels = p["labels"][lang]
    for pl in placed:
        ox, oy = pl["ox"], pl["oy"]
        for s, pc in pl["items"].items():
            col = COLORS[s]; c.setStrokeColorRGB(*col); c.setLineWidth(0.9); c.setDash(DASH[s])
            path = c.beginPath(); pts = [T(ox + x, oy + y) for x, y in pc["outline"]]
            path.moveTo(*pts[0]); [path.lineTo(*q) for q in pts[1:]]; c.drawPath(path, stroke=1, fill=0)
            c.setLineWidth(0.5)
            for dpts in pc["darts"]:
                q = [T(ox + x, oy + y) for x, y in dpts]; dp = c.beginPath(); dp.moveTo(*q[0]); dp.lineTo(*q[1]); dp.lineTo(*q[2]); c.drawPath(dp)
        pc0 = pl["items"][p["sizes"][len(p["sizes"]) // 2]]
        c.setDash([]); c.setStrokeColorRGB(0, 0, 0); c.setLineWidth(0.6)
        (a, b) = pc0["grain"]; c.line(*T(ox + a[0], oy + a[1]), *T(ox + b[0], oy + b[1]))
        c.line(*T(ox + b[0], oy + b[1]), *T(ox + b[0] - 0.4, oy + b[1] - 0.8)); c.line(*T(ox + b[0], oy + b[1]), *T(ox + b[0] + 0.4, oy + b[1] - 0.8))
        if pc0["hipline"]:
            c.setDash([3, 3]); (h0, h1) = pc0["hipline"]; c.line(*T(ox, oy + h0[1]), *T(ox + pl["w"], oy + h1[1])); c.setDash([])
        if pc0["fold"]:
            c.setFont("Helvetica-Bold", 11); c.saveState(); c.translate(*T(ox - 0.7, oy + 35)); c.rotate(90); c.drawString(0, 0, labels["fold"]); c.restoreState()
        c.setFillColorRGB(0.1, 0.1, 0.1); cx = ox + pl["w"] * 0.3; ly = 26 if pc0["w"] > 12 else 3
        c.setFont("Helvetica-Bold", 22 if ly > 3 else 10); c.drawString(*T(cx, oy + ly), labels[pc0["name"]].upper())
        c.setFont("Helvetica", 12 if ly > 3 else 6)
        c.drawString(*T(cx, oy + ly + (2 if ly > 3 else 1.0)), f'{labels["cut"]}: {labels["cut_" + pc0["name"]]} · {labels["nosa"]}')
        if ly > 3: c.drawString(*T(cx, oy + ly + 3.6), p["name_" + lang])
        if pc0["hipline"]: c.drawString(*T(cx, oy + pc0["hipline"][0][1] - 0.4), labels["hipline"])
    # méret-jelmagyarázat
    c.setFont("Helvetica-Bold", 12); y = H - 2.0; x = 3.0
    for s in p["sizes"]:
        c.setStrokeColorRGB(*COLORS[s]); c.setDash(DASH[s]); c.setLineWidth(1.2); c.line(*T(x, y), *T(x + 2, y)); c.setDash([])
        c.setFillColorRGB(*COLORS[s]); c.drawString(*T(x + 2.3, y + 0.35), s); x += 4.2
    c.setFillColorRGB(0, 0, 0)


def test_square(c, x, y):
    c.setLineWidth(1); c.setStrokeColorRGB(0, 0, 0); c.rect(x, y, 5 * cm, 5 * cm); c.rect(x + 5.6 * cm, y, 2 * inch, 2 * inch)
    c.setFont("Helvetica", 8); c.drawString(x + 0.3 * cm, y + 2.3 * cm, "5 cm"); c.drawString(x + 5.9 * cm, y + 2.3 * cm, "2 in")


def tiled(p, placed, W, H, out, pagesize, lang):
    pw, ph = pagesize; m = 1.0 * cm; vw, vh = pw - 2 * m, ph - 2 * m
    cols = math.ceil(W * cm / vw); rows = math.ceil(H * cm / vh); c = canvas.Canvas(str(out), pagesize=pagesize)
    for r in range(rows):
        for k in range(cols):
            c.saveState(); clip = c.beginPath(); clip.rect(m, m, vw, vh); c.clipPath(clip, stroke=0, fill=0)
            c.translate(m - k * vw, m - (H * cm - (r + 1) * vh)); draw_all(c, p, placed, H, lang); c.restoreState()
            c.setStrokeColorRGB(0.6, 0.6, 0.6); c.setLineWidth(0.4); c.rect(m, m, vw, vh)
            c.setFont("Helvetica-Bold", 14); c.setFillColorRGB(0.5, 0.5, 0.5); c.drawString(pw / 2 - 10, ph - 0.7 * cm, f"{chr(65 + r)}{k + 1}")
            c.setFont("Helvetica", 7); c.drawString(m, 0.35 * cm, f"{p['name_' + lang]} · {chr(65 + r)}{k + 1} · {rows * cols} pages · print at 100% / actual size")
            if r == 0 and k == 0: test_square(c, m + 0.5 * cm, ph - m - 6 * cm)
            c.showPage()
    c.save(); return rows * cols


def single(p, placed, W, H, out, lang):
    c = canvas.Canvas(str(out), pagesize=(max(W, 84.1) * cm, max(H, 118.9 if W <= 84.1 else 84.1) * cm))
    c.translate(0, (max(H, 118.9 if W <= 84.1 else 84.1) - H) * cm); draw_all(c, p, placed, H, lang); test_square(c, 3 * cm, 1 * cm); c.save()


def main():
    folder = Path(sys.argv[1]).resolve(); p = json.loads((folder / "pattern.json").read_text())
    placed, W, H = layout(p); slug = p["slug"]; res = {}
    for lang in ("en", "de"):
        L = lang.upper()
        res[f"A4-{L}"] = tiled(p, placed, W, H, folder / f"{slug}-A4-{L}.pdf", (21.0 * cm, 29.7 * cm), lang)
        res[f"Letter-{L}"] = tiled(p, placed, W, H, folder / f"{slug}-Letter-{L}.pdf", (8.5 * inch, 11 * inch), lang)
        single(p, placed, W, H, folder / f"{slug}-A0-{L}.pdf", lang)
    pv = canvas.Canvas(str(folder / "layout.pdf"), pagesize=(W * cm, H * cm)); draw_all(pv, p, placed, H, "en"); pv.save()
    # méretek ellenőrzése: kész derék/csípő vs. táblázat
    for s in p["sizes"]:
        pcs = DRAFTS[p["type"]](SIZES[s], **p.get("params", {}))
        hip = 2 * sum(pc["w"] - (p.get("params", {}).get("flare", 5.0) if p["type"] != "skirt_block" else 0) for pc in pcs if pc["name"] in ("front", "back"))
        print(f"{s}: csípő minta {hip:.1f} cm (test {SIZES[s]['hip']} + 4 bőség)")
    print("oldalak:", res, f"· elrendezés {W:.0f} × {H:.0f} cm")


if __name__ == "__main__":
    main()
