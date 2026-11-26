#!/usr/bin/env python3
"""Horgolás-ábrák SVG-ben (jelkulcsos diagram + kész forma vázlata). A build_crochet_pattern.py hívja a pattern.json "figures" listájából.
Jelek (nemzetközi jelkulcs szerint): lsz = ovális, ksz = pont, rp = ×, fp = T, ep = T ferde vonallal, szaporítás = piros, fogyasztás = kék."""
import math

INK = "#3a2e28"; INC = "#c8102e"; DEC = "#1f5fa8"; SOFT = "#b9a89c"
LEG = {
    "hu": dict(ch="láncszem (lsz)", sl="kúszószem (ksz)", sc="rövidpálca (rp)", hdc="félpálca (fp)", dc="egyráhajtásos pálca (ep)", inc="szaporítás (piros)", dec="fogyasztás (kék)", mr="varázsgyűrű", start="kezdés", rnd="kör", row="sor", title="Jelmagyarázat"),
    "en": dict(ch="chain (ch)", sl="slip stitch (sl st)", sc="single crochet (sc)", hdc="half double crochet (hdc)", dc="double crochet (dc)", inc="increase (red)", dec="decrease (blue)", mr="magic ring", start="start", rnd="rounds", row="row", title="Symbol key"),
    "de": dict(ch="Luftmasche (Lm)", sl="Kettmasche (Km)", sc="feste Masche (fM)", hdc="halbes Stäbchen (hStb)", dc="Stäbchen (Stb)", inc="Zunahme (rot)", dec="Abnahme (blau)", mr="Fadenring", start="Start", rnd="Runden", row="Reihe", title="Zeichenerklärung"),
}


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-height:4.6in">{body}</svg>'


def sym(kind, x, y, ang=0.0, s=7, col=INK):
    """Egy jel (x,y) középponttal; ang = a jel „felfelé” iránya radiánban (kifelé mutat)."""
    c, sn = math.cos(ang), math.sin(ang)
    P = lambda dx, dy: (x + dx * sn + dy * c, y - dx * c + dy * sn)  # dx: érintő, dy: kifelé
    if kind == "sc":
        a, b, cc, d = P(-s * .6, -s * .6), P(s * .6, s * .6), P(-s * .6, s * .6), P(s * .6, -s * .6)
        return f'<path d="M{a[0]:.1f},{a[1]:.1f}L{b[0]:.1f},{b[1]:.1f}M{cc[0]:.1f},{cc[1]:.1f}L{d[0]:.1f},{d[1]:.1f}" stroke="{col}" stroke-width="1.6"/>'
    if kind == "ch":
        return f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{s * .75:.1f}" ry="{s * .4:.1f}" transform="rotate({math.degrees(ang):.0f} {x:.1f} {y:.1f})" fill="none" stroke="{col}" stroke-width="1.3"/>'
    if kind == "sl":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{s * .35:.1f}" fill="{col}"/>'
    if kind in ("hdc", "dc"):
        h = s * (1.5 if kind == "hdc" else 2.0)
        b0, t0 = P(0, -h / 2), P(0, h / 2); l, r = P(-s * .55, h / 2), P(s * .55, h / 2)
        out = f'<path d="M{b0[0]:.1f},{b0[1]:.1f}L{t0[0]:.1f},{t0[1]:.1f}M{l[0]:.1f},{l[1]:.1f}L{r[0]:.1f},{r[1]:.1f}" stroke="{col}" stroke-width="1.6"/>'
        if kind == "dc":
            a, b = P(-s * .4, -h * .05), P(s * .4, h * .25)
            out += f'<path d="M{a[0]:.1f},{a[1]:.1f}L{b[0]:.1f},{b[1]:.1f}" stroke="{col}" stroke-width="1.4"/>'
        return out
    return ""


def text(x, y, t, size=11, col=INK, anchor="middle", bold=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="DejaVu Sans" font-size="{size}" fill="{col}" text-anchor="{anchor}"{" font-weight=\"bold\"" if bold else ""}>{t}</text>'


def legend(kinds, lang):
    L = LEG[lang]; items = [k for k in kinds]; w = 520; h = 26 * ((len(items) + 1) // 2) + 30
    body = text(10, 18, L["title"], 12, anchor="start", bold=True)
    for i, k in enumerate(items):
        x = 20 + (i % 2) * 260; y = 40 + (i // 2) * 26
        if k == "inc": body += sym("sc", x, y - 4, col=INC)
        elif k == "dec": body += sym("sc", x, y - 4, col=DEC)
        elif k == "mr": body += f'<circle cx="{x}" cy="{y - 4}" r="6" fill="none" stroke="{INK}" stroke-width="1.3" stroke-dasharray="2 2"/>'
        else: body += sym(k, x, y - 4)
        body += text(x + 16, y, L[k], 11, anchor="start")
    return svg(w, h, body)


def circle_chart(counts, lang, start="mr", stitch="sc", inc_pattern=True, ring_ch=0, dec_from=None, max_draw=None, note=""):
    """Lapos/spirál körök. counts: körönkénti szemszám. A szaporító szemek pirosak, a fogyasztók kékek.
    ring_ch>0: láncszem-gyűrűvel kezdődik (koszorú). max_draw: legfeljebb ennyi kört rajzol (amigurumi)."""
    L = LEG[lang]; cs = counts[:max_draw] if max_draw else counts
    n = len(cs); step = 22; r0 = 26 if ring_ch == 0 else 70; R = r0 + step * n + 16; W = 2 * R + 40; cx = cy = W / 2
    body = ""
    if ring_ch:
        for j in range(ring_ch):
            a = 2 * math.pi * j / ring_ch; body += sym("ch", cx + (r0 - 14) * math.cos(a), cy + (r0 - 14) * math.sin(a), a + math.pi / 2, 5)
    else:
        body += f'<circle cx="{cx}" cy="{cy}" r="{r0 - 14}" fill="none" stroke="{INK}" stroke-width="1.3" stroke-dasharray="3 3"/>'
    prev = None
    for i, c in enumerate(cs):
        r = r0 + step * i; col_idx = set()
        if prev is not None and c > prev and inc_pattern:
            per = c // 6; col_idx = {k * per + per - 1 for k in range(6)} | {k * per + per - 2 for k in range(6)}; colr = INC
        elif prev is not None and c < prev:
            per = c // 6; col_idx = {k * per + per - 1 for k in range(6)}; colr = DEC
        for j in range(c):
            a = 2 * math.pi * j / c - math.pi / 2
            body += sym(stitch, cx + r * math.cos(a), cy + r * math.sin(a), a, 5.5 if c < 50 else 4.2, colr if j in col_idx else INK)
        body += text(cx + 4, cy - r - 8 + (0 if i else 0), str(i + 1), 9, SOFT, "start")
        prev = c
    body += sym("sl", cx, cy - r0 - step * (n - 1) - 12 + 0, 0, 7, INC) if False else ""
    body += text(cx, W - 6, f'{n} {L["rnd"]}: ' + " → ".join(str(x) for x in cs) + (f" · {note}" if note else ""), 10, INK)
    return svg(W, W + 6, body)


def row_chart(widths, lang, stitch="sc", found_ch=None, dec_ends=True, label_every=1):
    """Soros munka alulról felfelé; a sor eleji forduló lsz-ek a sor végén. Fogyasztás a két szélen (kék)."""
    L = LEG[lang]; gap = 14; rowh = 22 if stitch == "sc" else 28; maxw = max(widths); n = len(widths)
    W = maxw * gap + 120; H = (n + (1 if found_ch else 0)) * rowh + 50; body = ""
    y0 = H - 30
    if found_ch:
        for j in range(found_ch):
            body += sym("ch", 60 + (maxw - found_ch) * gap / 2 + j * gap + gap / 2 - (found_ch - maxw) * gap / 2, y0, math.pi / 2, 6)
        body += text(20, y0 + 4, "lsz" if lang == "hu" else "ch", 9, SOFT); y0 -= rowh
    prev = None
    for i, w in enumerate(widths):
        x0 = 60 + (maxw - w) * gap / 2; dec = prev is not None and w < prev
        for j in range(w):
            col = DEC if dec and dec_ends and (j == 0 or j == w - 1) else INK
            body += sym(stitch, x0 + j * gap + gap / 2, y0 - i * rowh, -math.pi / 2, 5.5, col)
        if (i + 1) % label_every == 0 or i == 0 or i == n - 1:
            side = (i % 2 == 0)
            body += text(x0 - 10 if not side else x0 + w * gap + 10, y0 - i * rowh + 4, f'{i + 1}{"→" if side else ""}' if side else f'←{i + 1}', 10, SOFT, "end" if not side else "start")
        prev = w
    return svg(W, H, body)


def granny_chart(rounds, lang):
    """Klasszikus nagymama-négyzet. 1. kör: oldalanként 1 csoport (3 ep), sarkokban 2 lsz.
    n. kör (n≥2): sarkokban 3 ep, 2 lsz, 3 ep; oldalanként n-2 közbenső 3 ep-csoport; a csoportok között 1 lsz."""
    W = 520; cx = cy = W / 2; body = f'<circle cx="{cx}" cy="{cy}" r="10" fill="none" stroke="{INK}" stroke-width="1.3" stroke-dasharray="3 3"/>'
    for i in range(1, rounds + 1):
        h = 34 + (i - 1) * 52          # a kör „sugara” (az oldal fele)
        for k in range(4):
            ang = [-math.pi / 2, 0, math.pi / 2, math.pi][k]; ux, uy = math.cos(ang), math.sin(ang); tx, ty = -uy, ux
            line = lambda t: (cx + ux * h + tx * t, cy + uy * h + ty * t)
            groups = [0.0] if i == 1 else [-h + 22, h - 22] + [(-h + 22) + (2 * h - 44) * (g + 1) / (i - 1) for g in range(i - 2)]
            groups = sorted(groups)
            for gpos in groups:
                for d in (-1, 0, 1):
                    x, y = line(gpos + d * 9); body += sym("dc", x, y, ang, 5)
            for a_, b_ in zip(groups, groups[1:]):
                x, y = line((a_ + b_) / 2); body += sym("ch", x, y, ang + math.pi / 2, 4.5)
            # sarok (2 lsz) a k. és k+1. oldal között
            cxn, cyn = cx + (ux + tx) * (h + 4), cy + (uy + ty) * (h + 4)
            body += sym("ch", cxn - tx * 6, cyn - ty * 6, ang + math.pi / 4, 4.5) + sym("ch", cxn - ux * 6, cyn - uy * 6, ang + math.pi / 4, 4.5)
        body += text(cx + h + 14, cy - h - 4, str(i), 10, INC, "start", True)
        body += sym("sl", cx + 0, cy - h - 0, 0, 0) if False else ""
    body += text(cx, W - 6, f'{rounds} {LEG[lang]["rnd"]}: ' + " → ".join(str(12 * k) for k in range(1, rounds + 1)) + (" ep" if lang == "hu" else " Stb" if lang == "de" else " dc"), 11)
    return svg(W, W, body)


def snowflake_chart(lang):
    """1. kör: 12 rp. 2. kör: 6 rp + 6 db 5 lsz-ív. 3. kör: minden ívbe 3 rp, 3 lsz (pikó), 3 rp; ksz a 2. kör rp-jébe."""
    W = 460; cx = cy = W / 2; body = f'<circle cx="{cx}" cy="{cy}" r="12" fill="none" stroke="{INK}" stroke-width="1.3" stroke-dasharray="3 3"/>'
    P = lambda ang, r: (cx + r * math.cos(ang), cy + r * math.sin(ang))
    for j in range(12):
        a = 2 * math.pi * j / 12 - math.pi / 2; x, y = P(a, 30); body += sym("sc", x, y, a, 5)
    for k in range(6):
        a0 = 2 * math.pi * k / 6 - math.pi / 2; x, y = P(a0, 52); body += sym("sc", x, y, a0, 5)
        for f in (1 / 6, 2 / 6, 3 / 6, 4 / 6, 5 / 6):
            ang = a0 + f * math.pi / 3; r = 52 + 46 * math.sin(math.pi * f); x, y = P(ang, r); body += sym("ch", x, y, ang + math.pi / 2, 4.5)
        for f in (0.16, 0.29, 0.40, 0.60, 0.71, 0.84):
            ang = a0 + f * math.pi / 3; r = 68 + 50 * math.sin(math.pi * f); x, y = P(ang, r); body += sym("sc", x, y, ang, 4.8)
        mid = a0 + math.pi / 6
        for d, rr in ((-0.07, 128), (0, 140), (0.07, 128)):
            x, y = P(mid + d, rr); body += sym("ch", x, y, mid + math.pi / 2 + d * 8, 4.5, INC)
        x, y = P(a0 + math.pi / 3, 64); body += sym("sl", x, y, 0, 6)
    body += text(cx, W - 8, {"hu": "1: 12 rp · 2: 6 rp + 6 × 5 lsz · 3: minden ívbe 3 rp, 3 lsz (piros pikó), 3 rp",
                              "en": "R1: 12 sc · R2: 6 sc + 6 ch-5 arcs · R3: in each arc 3 sc, ch 3 (red picot), 3 sc",
                              "de": "R1: 12 fM · R2: 6 fM + 6 Bögen à 5 Lm · R3: in jeden Bogen 3 fM, 3 Lm (rote Picot), 3 fM"}[lang], 10)
    return svg(W, W, body)


def heart_chart(lang):
    """Egykörös szív: minden szem a varázsgyűrűbe, a szemek a gyűrűtől a szív körvonaláig érnek."""
    W, H = 420, 400; C = (210, 150)
    def heart(t):
        x = 16 * math.sin(t) ** 3; y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        return C[0] + x * 10.5, C[1] - y * 10.5 + 20
    outline = " ".join(f"{heart(math.radians(d))[0]:.1f},{heart(math.radians(d))[1]:.1f}" for d in range(0, 361, 3))
    body = f'<polygon points="{outline}" fill="#fbe9ec" stroke="#e8b9c2" stroke-width="1.5"/>'
    ring = (C[0], C[1] + 30); body += f'<circle cx="{ring[0]}" cy="{ring[1]}" r="12" fill="none" stroke="{INK}" stroke-width="1.4" stroke-dasharray="3 3"/>'
    seq = ["c3", "dc", "dc", "dc", "hdc", "hdc", "hdc", "ch", "tip", "ch", "hdc", "hdc", "hdc", "dc", "dc", "dc", "c3"]
    ts = [math.radians(22 + (338 - 22) * i / (len(seq) - 1)) for i in range(len(seq))]
    for kind, t in zip(seq, ts):
        ox, oy = heart(t); dx, dy = ox - ring[0], oy - ring[1]; L_ = math.hypot(dx, dy); ux, uy = dx / L_, dy / L_
        sx, sy = ring[0] + ux * 14, ring[1] + uy * 14; ex, ey = ox - ux * 8, oy - uy * 8
        col = INC if kind == "tip" else INK
        if kind in ("ch", "c3"):
            n = 1 if kind == "ch" else 3
            for j in range(n):
                f = (j + 1) / (n + 0.3) if n > 1 else 0.85; body += sym("ch", sx + (ex - sx) * f, sy + (ey - sy) * f, math.atan2(uy, ux) + math.pi / 2, 5)
        else:
            body += f'<path d="M{sx:.1f},{sy:.1f}L{ex:.1f},{ey:.1f}" stroke="{col}" stroke-width="1.6"/>'
            px, py = -uy, ux; body += f'<path d="M{ex - px * 6:.1f},{ey - py * 6:.1f}L{ex + px * 6:.1f},{ey + py * 6:.1f}" stroke="{col}" stroke-width="1.6"/>'
            if kind in ("dc", "tip"):
                mx, my = sx + (ex - sx) * .55, sy + (ey - sy) * .55; body += f'<path d="M{mx - px * 5 - ux * 3:.1f},{my - py * 5 - uy * 3:.1f}L{mx + px * 5 + ux * 3:.1f},{my + py * 5 + uy * 3:.1f}" stroke="{col}" stroke-width="1.4"/>'
    body += sym("sl", C[0], C[1] + 8, 0, 8)
    body += text(W / 2, H - 14, {"hu": "3 lsz, 3 ep, 3 fp, 1 lsz, 1 ep (csúcs, piros), 1 lsz, 3 fp, 3 ep, 3 lsz, ksz",
                                 "en": "ch 3, 3 dc, 3 hdc, ch 1, 1 dc (point, red), ch 1, 3 hdc, 3 dc, ch 3, sl st",
                                 "de": "3 Lm, 3 Stb, 3 hStb, 1 Lm, 1 Stb (Spitze, rot), 1 Lm, 3 hStb, 3 Stb, 3 Lm, Km"}[lang], 10)
    return svg(W, H, body)


# ---------------- kész forma vázlatok (méretnyilakkal)
def dim(x1, y1, x2, y2, label, off=0):
    return (f'<path d="M{x1},{y1}L{x2},{y2}" stroke="{SOFT}" stroke-width="1" marker-start="url(#a)" marker-end="url(#a)"/>'
            + text((x1 + x2) / 2 + off, (y1 + y2) / 2 - 6, label, 11, INK))


DEFS = f'<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="{SOFT}"/></marker></defs>'


def shape(kind, lang, **k):
    b = DEFS; W, H = 420, 300; F = "#efe4dc"; S = "#6b3f22"
    if kind == "circle":
        b += f'<circle cx="210" cy="140" r="100" fill="{F}" stroke="{S}" stroke-width="2"/>' + dim(110, 260, 310, 260, k["d"])
    elif kind == "square":
        b += f'<rect x="110" y="40" width="200" height="200" fill="{F}" stroke="{S}" stroke-width="2"/>' + dim(110, 262, 310, 262, k["w"]) + dim(330, 40, 330, 240, k["h"], 26)
    elif kind == "tree":
        b += f'<path d="M210,40L320,220L100,220z" fill="#cfe3cf" stroke="{S}" stroke-width="2"/><rect x="190" y="220" width="40" height="30" fill="#c9a98a" stroke="{S}" stroke-width="2"/><path d="M210,22l6,12 13,1-10,9 3,13-12-7-12,7 3-13-10-9 13-1z" fill="#f2d16b" stroke="{S}"/>' + dim(100, 272, 320, 272, k["w"]) + dim(345, 30, 345, 250, k["h"], 26)
    elif kind == "wreath":
        b += f'<circle cx="210" cy="140" r="100" fill="none" stroke="#7fae86" stroke-width="44"/><circle cx="210" cy="140" r="100" fill="none" stroke="{S}" stroke-width="1"/><path d="M190,230 l-30,-14 0,28z M230,230 l30,-14 0,28z" fill="#d95a5a" stroke="{S}"/><circle cx="210" cy="230" r="8" fill="#b83a3a"/>' + dim(88, 278, 332, 278, k["d"])
    elif kind == "ball":
        b += f'<circle cx="210" cy="140" r="100" fill="{F}" stroke="{S}" stroke-width="2"/>' + "".join(f'<ellipse cx="210" cy="140" rx="{rx}" ry="100" fill="none" stroke="{SOFT}" stroke-dasharray="4 3"/>' for rx in (40, 75)) + text(210, 145, k.get("label", ""), 12) + dim(110, 262, 310, 262, k["d"])
    elif kind == "chick":
        b += (f'<ellipse cx="210" cy="150" rx="90" ry="100" fill="#f6dc6e" stroke="{S}" stroke-width="2"/><circle cx="180" cy="125" r="6" fill="#222"/><circle cx="240" cy="125" r="6" fill="#222"/>'
              f'<path d="M200,140 L220,140 L210,158z" fill="#f0912f" stroke="{S}"/><ellipse cx="118" cy="162" rx="16" ry="30" fill="#eec94f" stroke="{S}"/><ellipse cx="302" cy="162" rx="16" ry="30" fill="#eec94f" stroke="{S}"/>'
              f'<path d="M205,52 q-6,-22 5,-26 M210,52 q2,-24 12,-22" stroke="#d9b23a" stroke-width="3" fill="none"/>'
              + text(330, 120, k["eyes"], 10, INK, "start") + f'<path d="M246,124L326,116" stroke="{SOFT}"/>'
              + text(330, 166, k["wings"], 10, INK, "start") + f'<path d="M318,162L326,163" stroke="{SOFT}"/>' + dim(345, 50, 345, 250, k["h"], 26))
        W = 480
    elif kind == "basket":
        b += (f'<path d="M90,70 L330,70 L330,240 Q330,250 320,250 L100,250 Q90,250 90,240z" fill="{F}" stroke="{S}" stroke-width="2"/>'
              f'<rect x="130" y="82" width="40" height="14" rx="7" fill="white" stroke="{S}"/><rect x="250" y="82" width="40" height="14" rx="7" fill="white" stroke="{S}"/>'
              + "".join(f'<path d="M92,{y}L328,{y}" stroke="{SOFT}" stroke-dasharray="2 4"/>' for y in range(110, 240, 12))
              + text(210, 238, k["base"], 10) + dim(90, 272, 330, 272, k["d"]) + dim(350, 70, 350, 250, k["h"], 26))
    return svg(W, H, b)


def render(fig, lang):
    f = fig["fn"]; a = dict(fig.get("args", {}))
    if f == "shape":
        kind = a.pop("kind"); lab = {kk: (v[lang] if isinstance(v, dict) else v) for kk, v in a.items()}; return shape(kind, lang, **lab)
    return {"circle_chart": circle_chart, "row_chart": row_chart, "granny_chart": granny_chart, "snowflake_chart": snowflake_chart, "heart_chart": heart_chart}[f](lang=lang, **a)
