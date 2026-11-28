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


def draft_circle_skirt(m, length=55.0, ease=1.0):
    """Teljes körszoknya: 1 negyedkör-darab, 2x hajtásra szabva (= 2 félkör). Derékív r = (derék+bőség)/(2π).
    Varrásráhagyás nélkül. + fél bund (álló, hajtás az elején)."""
    wc = m["waist"] + ease; r = wc / (2 * math.pi); R = r + length
    waist = [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in range(0, 91, 3)]
    hem = [(R * math.cos(math.radians(a)), R * math.sin(math.radians(a))) for a in range(90, -1, -3)]
    outline = waist + hem + [waist[0]]
    panel = dict(name="panel", outline=outline, darts=[], hipline=None, grain=((R * 0.35, r + 6), (R * 0.35, R - 8)), fold=True,
                 cut="2", w=R, h=R, waist_arc=wc)
    hl = (wc + 3) / 2
    band = dict(name="waistband", outline=[(0, 0), (7, 0), (7, hl), (0, hl), (0, 0)], darts=[], hipline=None,
                grain=((3.5, 4), (3.5, hl - 4)), fold=False, cut="1", w=7, h=hl)
    return [panel, band]


def draft_rect_skirt(m, length=60.0, fullness=1.5, casing=3.5):
    """Gumis derekú ráncolt szoknya: 2 téglalap (eleje, háta), mindkettő hajtásra. Teljes bőség = (csípő+4) × fullness.
    Fél darab szélessége w = (csípő+4)·fullness/4; magasság = hossz + gumialagút. Varrásráhagyás nélkül."""
    w = (m["hip"] + 4) * fullness / 4; h = length + casing
    pc = dict(name="panel", outline=[(0, 0), (w, 0), (w, h), (0, h), (0, 0)], darts=[], hipline=((0, casing), (w, casing)),
              grain=((w * 0.55, 6), (w * 0.55, h - 6)), fold=True, cut="2", w=w, h=h, elastic=m["waist"] - 5)
    return [pc]


# Karácsonyi zokni (2026-11-27): nem testméretes, 3 méret. A méretkulcsot (S/M/L) a SIZES csípőértékéből vesszük, hogy a közös layout működjön.
STOCKING = {94: ("S", 25.0, 11.0, 17.0), 100: ("M", 40.0, 16.0, 25.0), 108: ("L", 50.0, 20.0, 31.0)}  # név, magasság, szár szélesség, talphossz (kész, cm)


def draft_stocking(m, cuff=8.0):
    """Csizma alakú karácsonyi zokni: zoknitest (2 külső tükrözve + 2 bélés), hajtott mandzsetta, akasztó. Varrásráhagyás nélkül."""
    name, H, w, L = STOCKING[m["hip"]]
    fh = w * 0.62                                    # lábfej magassága
    out = [(0.0, 0.0), (w, 0.0), (w, H - fh)]
    out += qbez((w, H - fh), (L - fh * 0.25, H - fh), (L, H - fh * 0.45))[1:]
    out += qbez((L, H - fh * 0.45), (L, H), (L - fh * 0.5, H))[1:]
    out += [(fh * 0.5, H)]
    out += qbez((fh * 0.5, H), (0.0, H), (0.0, H - fh * 0.6))[1:]
    out += [(0.0, 0.0)]
    body = dict(name="stocking", outline=out, darts=[], hipline=None, grain=((w * 0.5, 3), (w * 0.5, H - fh - 2)), fold=False,
                cut="2+2", w=L, h=H, size=name, height=H, width=w, foot=L)
    cw = 2 * w; ch = 2 * cuff
    band = dict(name="cuff", outline=[(0, 0), (cw, 0), (cw, ch), (0, ch), (0, 0)], darts=[], hipline=((0, cuff), (cw, cuff)),
                grain=((cw * 0.5, 2), (cw * 0.5, ch - 2)), fold=False, cut="1", w=cw, h=ch)
    loop = dict(name="loop", outline=[(0, 0), (3, 0), (3, 15), (0, 15), (0, 0)], darts=[], hipline=None,
                grain=((1.5, 2), (1.5, 13)), fold=False, cut="1", w=3, h=15)
    return [body, band, loop]


# Bélelt vászontáska (2026-11-28): 3 méret, a méretkulcs a SIZES csípőértékéből (mint a zoknié).
TOTE = {94: ("S", 30.0, 32.0, 0.0, 55.0), 100: ("M", 38.0, 38.0, 8.0, 60.0), 108: ("L", 44.0, 40.0, 12.0, 65.0)}  # név, kész szélesség, magasság, talpmélység, fülhossz


def draft_tote(m):
    """Táskatest (külső 2 + bélés 2, kivágott sarkokkal a talphoz), belső zseb, 2 fül. Varrásráhagyás nélkül."""
    name, W, H, D, strap = TOTE[m["hip"]]
    pw = W + D; ph = H + D / 2; c = D / 2
    if c > 0:
        out = [(0, 0), (pw, 0), (pw, ph - c), (pw - c, ph - c), (pw - c, ph), (c, ph), (c, ph - c), (0, ph - c), (0, 0)]
    else:
        out = [(0, 0), (pw, 0), (pw, ph), (0, ph), (0, 0)]
    body = dict(name="body", outline=out, darts=[], hipline=None, grain=((pw * 0.5, 4), (pw * 0.5, ph - c - 4)), fold=False,
                cut="2+2", w=pw, h=ph, size=name, W=W, H=H, D=D)
    zw, zh = round(W * 0.55), round(H * 0.45)
    pocket = dict(name="pocket", outline=[(0, 0), (zw, 0), (zw, zh), (0, zh), (0, 0)], darts=[], hipline=None,
                  grain=((zw * 0.5, 2), (zw * 0.5, zh - 2)), fold=False, cut="1", w=zw, h=zh)
    st = dict(name="strap", outline=[(0, 0), (10, 0), (10, strap), (0, strap), (0, 0)], darts=[], hipline=None,
              grain=((5, 4), (5, strap - 4)), fold=False, cut="2", w=10, h=strap, strap=strap)
    return [body, pocket, st]


DRAFTS = {"skirt_block": draft_skirt_block, "aline_skirt": draft_aline_skirt, "circle_skirt": draft_circle_skirt, "rect_skirt": draft_rect_skirt, "stocking": draft_stocking, "tote": draft_tote}


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
        if p["type"] == "tote":
            b, pk, st = pcs; print(f"{b['size']}: kész táska {b['W']:.0f}×{b['H']:.0f} cm, talp {b['D']:.0f} cm; szabott test {b['w']:.0f}×{b['h']:.0f} cm (= szél.+talp × mag.+talp/2); zseb {pk['w']}×{pk['h']}; fül 10×{st['strap']:.0f}"); continue
        if p["type"] == "stocking":
            b, cf, _ = pcs; print(f"{b['size']}: zokni {b['height']:.0f} cm magas, szár {b['width']:.0f} cm, talp {b['foot']:.0f} cm; mandzsetta {cf['w']:.0f}×{cf['h']:.0f} cm (= 2×szár)"); continue
        if p["type"] == "rect_skirt":
            pn = pcs[0]; print(f"{s}: teljes bőség {pn['w'] * 4:.1f} cm = (csípő {SIZES[s]['hip']} + 4) × 1,5; gumi {pn['elastic']} cm"); continue
        if p["type"] == "circle_skirt":
            pn = pcs[0]; arc = sum(math.dist(a, b) for a, b in zip(pn["outline"][:31], pn["outline"][1:31])) * 4
            print(f"{s}: derékív a mintán {arc:.1f} cm (test {SIZES[s]['waist']} + 1 bőség), darab {pn['w']:.0f} cm")
            continue
        hip = 2 * sum(pc["w"] - (p.get("params", {}).get("flare", 5.0) if p["type"] != "skirt_block" else 0) for pc in pcs if pc["name"] in ("front", "back"))
        print(f"{s}: csípő minta {hip:.1f} cm (test {SIZES[s]['hip']} + 4 bőség)")
    print("oldalak:", res, f"· elrendezés {W:.0f} × {H:.0f} cm")


if __name__ == "__main__":
    main()
