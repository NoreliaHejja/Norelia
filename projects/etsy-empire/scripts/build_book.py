#!/usr/bin/env python3
"""
Tartalmas (high-content) könyv: Markdown-fejezetek → KDP papírkönyv (6x9, ff belív) + Kindle EPUB (színes képekkel).

  python3 scripts/build_book.py books/<slug>

books/<slug>/book.json: title, subtitle, author, series, price_paperback, price_kindle, color, chapters (fájlnevek),
                        illus (fejezet → kép a books/<slug>/img/ alatt), back, description, keywords, categories
Kimenet: books/<slug>/out/interior.pdf, book.epub, KDP_FELTOLTES.md  (borító: kdp_cover.py-hoz hasonló, de 6x9 → cover_6x9())
Szabály: nincs kitalált kutatás/idézet/vélemény; nincs orvosi/terápiás ígéret; minden könyvben „not a substitute for professional help” + segélyvonalak.
"""
import json, re, subprocess, sys, html as H
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent

CSS = """
@page{size:__TW__in __TH__in;margin:.75in .7in .8in .75in}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:#111;font-family:'Liberation Serif','DejaVu Serif',serif;font-size:11.6pt;line-height:1.58}
.page{height:__PH__in;position:relative;page-break-after:always;overflow:hidden}
.flow{}
h1{font-family:'DejaVu Sans',sans-serif;font-size:21pt;line-height:1.15;margin:.2in 0 .12in;font-weight:700;page-break-before:always}
h2{font-family:'DejaVu Sans',sans-serif;font-size:13pt;margin:.25in 0 .06in;font-weight:700}
h3{font-family:'DejaVu Sans',sans-serif;font-size:11pt;margin:.18in 0 .04in}
p{margin:0 0 .1in;text-align:justify;hyphens:auto}
ul,ol{margin:.02in 0 .12in .1in;padding-left:.2in}
li{margin-bottom:.04in}
blockquote{margin:.12in 0;padding:.1in .15in;border-left:3px solid #555;background:#f2f2f2;font-style:italic}
.chimg{display:block;width:100%;max-height:3.2in;object-fit:contain;margin:.05in 0 .15in;filter:grayscale(1)}
.lines div{border-bottom:1px solid #888;height:.32in}
.box{border:1.5px solid #333;border-radius:8px;padding:.12in .15in;margin:.12in 0;page-break-inside:avoid}
.center{text-align:center}
.title{font-family:'DejaVu Sans',sans-serif;font-size:24pt;font-weight:700;margin-top:2in;text-align:center;line-height:1.15}
.sub{text-align:center;font-size:12pt;margin-top:.15in;color:#333}
.small{font-size:9pt;color:#333}
"""


def md_to_html(md: str, slug: str, print_ver=True):
    """Kicsi Markdown-értelmező: #, ##, ###, -, 1., >, [[lines:N]], [[box]]...[[/box]], **bold**, *italic*, ![](img)."""
    out, lst = [], None
    def inline(t):
        t = H.escape(t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
        t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
        return t
    def close():
        nonlocal lst
        if lst: out.append(f"</{lst}>"); lst = None
    for raw in md.splitlines():
        l = raw.rstrip()
        m = re.match(r"\[\[lines:(\d+)\]\]", l)
        if m: close(); out.append("<div class='lines'>" + "<div></div>" * int(m.group(1)) + "</div>"); continue
        if l == "[[page]]": close(); out.append("<div style='page-break-after:always'></div>"); continue
        if l == "[[box]]": close(); out.append("<div class='box'>"); continue
        if l == "[[/box]]": close(); out.append("</div>"); continue
        m = re.match(r"!\[\]\((.+?)\)", l)
        if m: close(); out.append(f"<img class='chimg' src='../img/{m.group(1)}'>"); continue
        if l.startswith("### "): close(); out.append(f"<h3>{inline(l[4:])}</h3>"); continue
        if l.startswith("## "): close(); out.append(f"<h2>{inline(l[3:])}</h2>"); continue
        if l.startswith("# "): close(); out.append(f"<h1>{inline(l[2:])}</h1>"); continue
        if l.startswith("> "): close(); out.append(f"<blockquote>{inline(l[2:])}</blockquote>"); continue
        if re.match(r"^[-*] ", l):
            if lst != "ul": close(); out.append("<ul>"); lst = "ul"
            out.append(f"<li>{inline(l[2:])}</li>"); continue
        if re.match(r"^\d+\. ", l):
            if lst != "ol": close(); out.append("<ol>"); lst = "ol"
            out.append(f"<li>{inline(re.sub(r'^\d+\. ', '', l))}</li>"); continue
        if not l.strip(): close(); continue
        close(); out.append(f"<p>{inline(l)}</p>")
    close()
    return "\n".join(out)


def backmatter(b, folder: Path) -> str:
    """Sorozat-lánc a könyv végére (books/series.json): következő lépés + többi kötet + értékelés-kérés."""
    sp = folder.parent / "series.json"
    key = b.get("series_key")
    if not key or not sp.exists():
        return ""
    S = json.loads(sp.read_text())["books"]
    de = b.get("lang") == "de"
    L = "de" if de else "en"
    st = lambda k: S[k].get("status_de" if de else "status")
    soon = " (erscheint bald)" if de else " (coming soon)"
    t = lambda k: f"*{S[k][L]}*" + ("" if st(k) == "ready" else soon)
    me = S[key]
    out = ["# Wie es weitergeht" if de else "# Where to Go From Here", ""]
    out.append("Du hast dieses Buch durchgearbeitet – das ist mehr, als die meisten Menschen tun. Wenn du den nächsten Schritt gehen möchtest:" if de else
               "You made it through this book, and that is more than most people ever do. If you'd like to take the next step:")
    out.append("")
    for k in me.get("next", []):
        out.append(f"- {t(k)}: {S[k]['hook_' + L]}")
    out += ["", "## Weitere Gentle Life Guides" if de else "## More Gentle Life Guides", ""]
    for k, v in S.items():
        if k != key and k not in me.get("next", []):
            out.append(f"- {t(k)}: {v['hook_' + L]}")
    out += ["", ("Alle Bände findest du auf Amazon unter „Clara Whitfield“." if de else "You can find every guide on Amazon by searching for \"Clara Whitfield\"."), "",
            "## Eine kleine Bitte" if de else "## A Small Favor", "",
            ("Wenn dir auch nur eine Seite dieses Buches geholfen hat, würdest du eine ehrliche Bewertung auf Amazon hinterlassen? Es dauert eine Minute und hilft anderen Menschen, ein Buch zu finden, das ihnen vielleicht auch hilft." if de else
             "If even one page of this book helped you, would you consider leaving an honest review on Amazon? It takes a minute, and it helps someone else find a book that might help them too."),
            ""]
    return "\n".join(out)


def build(folder: Path):
    b = json.loads((folder / "book.json").read_text())
    od = folder / "out"; od.mkdir(exist_ok=True)
    de = b.get("lang") == "de"
    body = "".join(md_to_html((folder / c).read_text(), b["slug"]) for c in b["chapters"]) + md_to_html(backmatter(b, folder), b["slug"])
    front = (f"<div class='page'><div class='title'>{H.escape(b['title'])}</div><div class='sub'>{H.escape(b['subtitle'])}</div>"
             f"<div class='sub' style='margin-top:1.2in'>{H.escape(b['author'])}</div></div>"
             f"<div class='page'><div style='position:absolute;bottom:0;left:0;right:0' class='small'>"
             f"<p>Copyright © 2026 {H.escape(b['author'])}. {'Alle Rechte vorbehalten.' if de else 'All rights reserved.'}</p>"
             + ("<p>Dieses Buch dient der allgemeinen Information und Ermutigung. Es ersetzt keine ärztliche, psychologische, rechtliche oder finanzielle Beratung. "
                "Wenn du in einer Krise bist oder daran denkst, dir etwas anzutun, wende dich sofort an den Notruf 112 oder die Telefonseelsorge "
                "(Deutschland 0800 111 0 111 oder 0800 111 0 222, Österreich 142, Schweiz 143).</p>"
                "<p>Mit Unterstützung von KI-Werkzeugen geschrieben und sorgfältig bearbeitet. Illustrationen mit Unterstützung von KI erstellt.</p></div></div>" if de else
                "<p>This book is for general information and encouragement only. It is not medical, psychological, legal or financial advice and "
             "is not a substitute for help from a qualified professional. If you are in crisis or thinking about harming yourself, contact your local emergency number "
             "or a crisis line right away (in the US, call or text 988; in the UK, call Samaritans at 116 123).</p>"
             "<p>Written with the help of AI tools and carefully edited. Illustrations created with the help of AI.</p></div></div>"))
    TW, TH = trim(b)
    css = CSS.replace("__TW__", str(TW)).replace("__TH__", str(TH)).replace("__PH__", f"{TH - 1.6:.2f}")
    (od / "interior.html").write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{front}<div class='flow'>{body}</div></body></html>", encoding="utf-8")
    pdf = od / "interior.pdf"
    subprocess.run(["node", "-e", f"""
const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{od/'interior.html'}',{{waitUntil:'networkidle'}});
await p.pdf({{path:'{pdf}',width:'{TW}in',height:'{TH}in',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="width:100%;text-align:center;font-size:8px;font-family:serif;color:#444"><span class="pageNumber"></span></div>'}});await b.close();}})();"""], check=True)
    n = int([l for l in subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages:")][0].split()[1])
    if n % 2: n += 0
    # EPUB (Kindle) – színes képekkel
    md_all = "\n\n".join((folder / c).read_text() for c in b["chapters"]) + "\n\n" + backmatter(b, folder)
    md_all = re.sub(r"\[\[lines:(\d+)\]\]", lambda m: "\n" + "\n".join(["_____________________________"] * min(4, int(m.group(1)))) + "\n", md_all)
    md_all = md_all.replace("[[box]]", "").replace("[[/box]]", "").replace("[[page]]", "")
    md_all = re.sub(r"!\[\]\((.+?)\)", lambda m: f"![]({folder/'img'/m.group(1)})", md_all)
    (od / "book.md").write_text(md_all, encoding="utf-8")
    subprocess.run(["pandoc", str(od / "book.md"), "-o", str(od / "book.epub"), "--toc", "--metadata", f"title={b['title']}",
                    "--metadata", f"subtitle={b['subtitle']}", "--metadata", f"author={b['author']}", "--metadata", "lang=" + ("de-DE" if de else "en-US")]
                   + (["--epub-cover-image", str(od / "front.jpg")] if (od / "front.jpg").exists() else []), check=True)
    words = len(re.findall(r"\w+", md_all))
    print(f"{pdf}: {n} oldal, {words} szó; EPUB kész")
    return b, n, words


def trim(b):
    """Vágott méret hüvelykben – PONTOSAN ezt kell a KDP-ben is választani (book.json "trim": [szél, mag], alap 6x9)."""
    t = b.get("trim", [6, 9])
    return float(t[0]), float(t[1])


def cover(folder: Path, b, pages, art: Path):
    DPI = 300
    TW, TH = trim(b)
    spine = pages * 0.002252
    W, Hh = round((0.125 * 2 + TW * 2 + spine) * DPI), round((TH + 0.25) * DPI)
    color = b["color"]
    img = Image.new("RGB", (W, Hh), color); d = ImageDraw.Draw(img)
    fx0 = int((0.125 + TW + spine) * DPI); fw = W - fx0
    a = Image.open(art).convert("RGB"); r = max(fw / a.width, Hh / a.height)
    a = a.resize((int(a.width * r), int(a.height * r)), Image.LANCZOS)
    a = a.crop(((a.width - fw) // 2, (a.height - Hh) // 2, (a.width - fw) // 2 + fw, (a.height - Hh) // 2 + Hh)); img.paste(a, (fx0, 0))
    FX, FB, FR = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf", "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf", "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
    def wrap(text, font, maxw):
        o, c = [], ""
        for w in text.split():
            t = (c + " " + w).strip()
            if d.textlength(t, font=font) <= maxw: c = t
            else: o.append(c); c = w
        return o + [c]
    m = int(.45 * DPI); bx0, bx1 = fx0 + m, W - m
    ft = ImageFont.truetype(FX, 150); tl = wrap(b["title"], ft, bx1 - bx0 - 100)
    fs = ImageFont.truetype(FB, 54); sl = wrap(b.get("cover_sub", b["subtitle"]), fs, bx1 - bx0 - 120)
    bh = 70 + len(tl) * 170 + len(sl) * 72 + 50
    d.rounded_rectangle((bx0, int(.5 * DPI), bx1, int(.5 * DPI) + bh), 50, fill=(255, 252, 245))
    y = int(.5 * DPI) + 55
    for t in tl: d.text(((bx0 + bx1) // 2, y), t, font=ft, fill="#1F2A44", anchor="ma"); y += 170
    for t in sl: d.text(((bx0 + bx1) // 2, y), t, font=fs, fill=color, anchor="ma"); y += 72
    fa = ImageFont.truetype(FB, 70)
    d.rounded_rectangle((fx0 + fw // 2 - 560, Hh - int(1.05 * DPI), fx0 + fw // 2 + 560, Hh - int(.6 * DPI)), 40, fill=(255, 252, 245))
    d.text((fx0 + fw // 2, Hh - int(.825 * DPI)), b["author"].upper(), font=fa, fill="#1F2A44", anchor="mm")
    bx = int(.55 * DPI); y = int(.8 * DPI); fr = ImageFont.truetype(FR, 46)
    for para in b["back"].split("|"):
        for t in wrap(para, fr, int(5.0 * DPI)): d.text((bx, y), t, font=fr, fill="white"); y += 66
        y += 30
    assert y < Hh - int(1.75 * DPI), "HIBA: a hátsó borító szövege belelóg a vonalkód-területbe – rövidítsd a 'back' szöveget"
    bxe = fx0 - int(spine * DPI) - int(.375 * DPI)
    d.rectangle((bxe - int(2 * DPI), Hh - int(.375 * DPI) - int(1.2 * DPI), bxe, Hh - int(.375 * DPI)), fill="white")
    if pages >= 100:  # KDP: gerincszöveg csak 100+ oldaltól, 0,0625 in szabad hellyel mindkét oldalon (Nóra, 2026-11-14)
        sp = Image.new("RGB", (Hh, int(spine * DPI)), color); sd = ImageDraw.Draw(sp)
        sd.text((Hh // 2, sp.height // 2), f"{b['title'].upper()}   ·   {b['author'].upper()}", font=ImageFont.truetype(FB, int((spine - 0.14) * DPI * 0.95)), fill="white", anchor="mm")
        img.paste(sp.rotate(-90, expand=True), (fx0 - int(spine * DPI), 0))
    od = folder / "out"
    img.save(od / "cover.pdf", "PDF", resolution=DPI)
    img.resize((W // 6, Hh // 6)).save(od / "cover-preview.jpg", quality=85)
    img.crop((fx0, 0, W, Hh)).resize((1600, int(1600 * Hh / fw))).save(od / "front.jpg", quality=90)  # Kindle-borító
    print(od / "cover.pdf", f"{W/DPI:.3f} x {Hh/DPI:.3f} in, gerinc {spine:.3f}")


def sheet(folder: Path, b, n, words):
    (folder / "out" / "KDP_FELTOLTES.md").write_text(f"""# KDP – {b['title']}

Két külön feltöltés ugyanazzal az adattal: **Paperback** és **Kindle eBook** (a KDP összekapcsolja őket).

| Mező | Érték |
|---|---|
| Language | {'German' if b.get('lang') == 'de' else 'English'} |
| Title | {b['title']} |
| Subtitle | {b['subtitle']} |
| Series | {b.get('series','')} |
| Author (pen name) | {b['author']} |
| Categories | {' / '.join(b['categories'])} |
| Keywords (7) | {'; '.join(b['keywords'])} |
| AI-generated content | **Yes** – Text: AI-assisted (edited); Images: AI-generated |
| **Trim size** | **{trim(b)[0]:g} x {trim(b)[1]:g} in** – a KDP-ben PONTOSAN ezt válaszd, különben a borító/belív mérete hibás lesz |
| Paperback | **Black & white**, white paper, no bleed, matte cover; `interior.pdf` ({n} oldal) + `cover.pdf`; ár **{b['price_paperback']}{'' if 'EUR' in b['price_paperback'] else ' $'}** |
| Kindle | `book.epub` (színes képekkel) + `front.jpg` borító; ár **{b['price_kindle']}{'' if 'EUR' in b['price_kindle'] else ' $'}** (70% royalty sáv: 2,99–9,99 $); {'**KDP Select: NEM** – a német e-könyv Draft2Digitalon a Tolino-boltokba is megy' if b.get('lang') == 'de' else '**KDP Select: IGEN** (angol: Kindle Unlimited, csak Amazon)'} |

## Description
{b['description']}

(~{words} szó)
""", encoding="utf-8")


def kdp_check(folder: Path, b, n):
    """KDP-kapu (Nóra, 2026-11-14): méret pontosan a KDP-képlet szerint, és semmi nem lóg ki a biztonsági sávba."""
    import numpy as np
    TW, TH = trim(b); od = folder / "out"; hibak = []
    def size(pdf):
        l = [x for x in subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout.splitlines() if x.startswith("Page size")][0]
        w, h = l.split(":")[1].split("x")[0], l.split("x")[1].split()[0]
        return float(w) / 72, float(h) / 72
    w, h = size(od / "interior.pdf")
    if abs(w - TW) > 0.01 or abs(h - TH) > 0.01:
        hibak.append(f"belív {w:.3f}x{h:.3f}, elvárt {TW}x{TH}")
    if (od / "cover.pdf").exists():
        ew, eh = 2 * TW + 0.25 + n * 0.002252, TH + 0.25
        w, h = size(od / "cover.pdf")
        if abs(w - ew) > 0.01 or abs(h - eh) > 0.01:
            hibak.append(f"borító {w:.3f}x{h:.3f}, elvárt {ew:.3f}x{eh:.3f} (KDP: 2×{TW}+0,25+{n}×0,002252 × {TH}+0,25)")
    # biztonsági sáv: a lap szélétől 0,25 in-en belül nem lehet tinta (KDP no-bleed: min. 0,25 in külső margó)
    tmp = od / "_chk"; tmp.mkdir(exist_ok=True)
    subprocess.run(["pdftoppm", "-r", "40", "-gray", "-png", str(od / "interior.pdf"), str(tmp / "p")], check=True)
    band = int(0.25 * 40)
    for f in sorted(tmp.glob("p-*.png")):
        a = np.array(Image.open(f))
        edge = np.concatenate([a[:band].ravel(), a[-band:].ravel(), a[:, :band].ravel(), a[:, -band:].ravel()])
        if (edge < 200).any():
            hibak.append(f"{f.stem}: tartalom a 0,25 in-es szélső sávban")
        f.unlink()
    tmp.rmdir()
    if hibak:
        sys.exit("KDP-KAPU HIBA:\n- " + "\n- ".join(hibak))
    print(f"KDP-kapu OK: belív {TW}x{TH} in, {n} oldal; borító méret és biztonsági sáv rendben")


if __name__ == "__main__":
    f = ROOT / sys.argv[1]
    b, n, words = build(f)
    art = f / "img" / "cover.png"
    if art.exists():
        cover(f, b, n, art)
        build(f)  # EPUB a front.jpg borítóval
    sheet(f, b, n, words)
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'kdp_lap.py'), str(f / 'out' / 'KDP_FELTOLTES.md')], check=True)
    kdp_check(f, b, n)
