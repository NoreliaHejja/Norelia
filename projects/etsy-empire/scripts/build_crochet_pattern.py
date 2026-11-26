#!/usr/bin/env python3
"""Horgolásminta PDF generátor (EN + DE) – horgolas/README.md.
  python3 scripts/build_crochet_pattern.py horgolas/mintak/<slug> [--draft]
pattern.json → <slug>-EN.html/.pdf és <slug>-DE.html/.pdf (render_pdf.js-sel).
Soronként: {"label_en","label_de","en","de","count", opcionális "prev","change"}: ha prev és change megvan,
ellenőrzi, hogy prev + change == count (szemszám-kapu). --draft: „TEST VERSION” vízjel a tesztelőnek."""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ABBR = {  # kulcs: (US, UK, DE, HU, EN magyarázat, DE magyarázat)
    "ch": ("ch", "ch", "Lm", "lsz", "chain", "Luftmasche"),
    "sl st": ("sl st", "ss", "Km", "hsz", "slip stitch", "Kettmasche"),
    "sc": ("sc", "dc", "fM", "rp", "single crochet", "feste Masche"),
    "hdc": ("hdc", "htr", "hStb", "félp", "half double crochet", "halbes Stäbchen"),
    "dc": ("dc", "tr", "Stb", "ep", "double crochet", "Stäbchen"),
    "sc2tog": ("sc2tog", "dc2tog", "2 fM zus abm", "2 rp összehorg.", "single crochet 2 together (decrease)", "2 feste Maschen zusammen abmaschen (Abnahme)"),
    "inc": ("inc", "inc", "zun", "szap.", "2 sc in the same stitch (increase)", "2 fM in eine Masche (Zunahme)"),
    "MR": ("MR", "MR", "MR", "varázsgyűrű", "magic ring", "Fadenring"),
    "st": ("st(s)", "st(s)", "M", "szem", "stitch(es)", "Masche(n)"),
    "BLO": ("BLO", "BLO", "hMg", "hsz", "back loop only", "nur in das hintere Maschenglied"),
    "FLO": ("FLO", "FLO", "vMg", "esz", "front loop only", "nur in das vordere Maschenglied"),
}
ABBR_HU = {  # magyar rövidítés + magyarázat
    "ch": ("lsz", "láncszem"), "sl st": ("ksz", "kúszószem (hamis láncszem)"), "sc": ("rp", "rövidpálca"), "hdc": ("fp", "félpálca"),
    "dc": ("ep", "egyráhajtásos pálca"), "sc2tog": ("fogy", "fogyasztás: 2 rövidpálca összehorgolva"), "inc": ("szap", "szaporítás: 2 rövidpálca ugyanabba a szembe"),
    "MR": ("vgy", "varázsgyűrű"), "st": ("szem", "szem(ek)"), "BLO": ("hsz", "csak a hátsó szálba"), "FLO": ("esz", "csak az elülső szálba"),
}
T = {
    "hu": dict(level="Nehézség", size="Kész méret", mat="Amire szükséged lesz", hook="Horgolótű", gauge="Sűrűség", abbr="Rövidítések",
               uk="US", notes="Tudnivalók", fin="Befejezés", copy="A minta saját használatra és kis mennyiségű kézműves eladásra szól, az AureliaVenn megjelölésével. Kérlek, magát a mintát ne oszd meg és ne add el.",
               draft="TESZTVÁLTOZAT – kérlek, jelezd a hibákat", hu="UK", lang="hu", tested="A mintát valódi horgoló tesztelte. A szöveg AI-eszközök segítségével készült.", sts="szem"),
    "en": dict(level="Skill level", size="Finished size", mat="You will need", hook="Hook", gauge="Gauge", abbr="Abbreviations (US terms)",
               uk="UK", notes="Notes", fin="Finishing", copy="This pattern is for personal use and for selling small handmade batches with credit to AureliaVenn. Please don't share or resell the pattern itself.",
               draft="TEST VERSION – please report any errors", hu="HU", lang="en", tested="Pattern tested by a real maker. Written with the help of AI tools.", sts="sts"),
    "de": dict(level="Schwierigkeit", size="Größe", mat="Du brauchst", hook="Häkelnadel", gauge="Maschenprobe", abbr="Abkürzungen",
               uk="US", notes="Hinweise", fin="Fertigstellen", copy="Diese Anleitung ist für den privaten Gebrauch und den Verkauf kleiner handgemachter Mengen mit Hinweis auf AureliaVenn. Bitte die Anleitung selbst nicht weitergeben oder verkaufen.",
               draft="TESTVERSION", hu="HU", lang="de", tested="Anleitung von einer echten Häklerin getestet. Mit Hilfe von KI-Werkzeugen geschrieben.", sts="M"),
}

CSS = """@page{size:Letter;margin:.6in .65in}body{font-family:'DejaVu Sans',sans-serif;font-size:10.5pt;color:#2f2a26;line-height:1.45}
h1{font-size:24pt;color:#b8322a;margin:0 0 4px}.sub{color:#6b3f22;font-size:11.5pt;margin-bottom:12px}
.hero{width:100%;max-height:4.3in;object-fit:cover;border-radius:12px;margin:6px 0 12px}
.meta{display:grid;grid-template-columns:1fr 1fr;gap:8px 18px;background:#fdf3ee;border-radius:12px;padding:12px 16px;margin-bottom:14px}
.meta b{display:block;color:#b8322a;font-size:9pt;text-transform:uppercase;letter-spacing:.05em}
h2{font-size:14pt;color:#6b3f22;border-bottom:2px solid #efd2c6;padding-bottom:3px;margin:16px 0 8px;page-break-after:avoid}
table{border-collapse:collapse;width:100%;font-size:9.5pt;margin-bottom:10px}td,th{border:1px solid #e3d3cc;padding:3px 6px;text-align:left}th{background:#fdf3ee}
.row{display:grid;grid-template-columns:1.0in 1fr 1.0in;gap:8px;padding:4px 0;border-bottom:1px dotted #e3d3cc;page-break-inside:avoid}
.row .l{font-weight:700;color:#b8322a}.row .c{text-align:right;color:#6b3f22;font-weight:700}
.note{background:#eef6ef;border-radius:10px;padding:8px 12px;margin:8px 0}.foot{margin-top:18px;font-size:8.5pt;color:#7a6f68}
.draft{position:fixed;top:40%;left:5%;transform:rotate(-30deg);font-size:46pt;color:rgba(184,50,42,.12);font-weight:700;white-space:nowrap}
.figh{page-break-before:always}.figs{display:grid;grid-template-columns:1fr 1fr;gap:12px}.fig{border:1px solid #efd2c6;border-radius:10px;padding:8px;background:#fff;page-break-inside:avoid}.fig .cap{font-size:9pt;color:#6b3f22;text-align:center;margin-top:4px}.leg{margin-top:10px}
.photos{display:grid;grid-template-columns:1fr 1fr;gap:8px}.photos img{width:100%;border-radius:8px}"""


def check(p):
    err = []
    for s in p["sections"]:
        for r in s["rows"]:
            if "prev" in r and "change" in r and "count" in r and r["prev"] + r["change"] != r["count"]:
                err.append(f'{s["title_en"]} {r["label_en"]}: {r["prev"]} + {r["change"]} != {r["count"]}')
    # Pozíció-kapu (STILUS.md, 2026-11-26): minden felvarrás / szembehelyezés körszámmal
    import re as _re
    for f in p.get("finishing", []):
        en = f.get("text_en", "")
        if _re.search(r"\b(sew|attach|insert)\b", en, _re.I) and _re.search(r"\b(eye|beak|wing|ear|arm|leg|nose|tail|head|handle)s?\b", en, _re.I) and not _re.search(r"\d", en):
            err.append(f"összeállítás körszám nélkül: {en[:60]}")
    return err


def html(p, lang, folder, draft):
    t = T[lang]; g = lambda d, k: d.get(f"{k}_{lang}", d.get(k, ""))
    photos = sorted((folder / "fotok").glob("*.jpg")) if (folder / "fotok").exists() else []
    hero = f'<img class="hero" src="fotok/{photos[0].name}">' if photos else ""
    if lang == "hu":
        abbr = "".join(f"<tr><td><b>{ABBR_HU[k][0]}</b></td><td>{ABBR_HU[k][1]}</td><td>{v[0]}</td><td>{v[1]}</td></tr>" for k, v in ABBR.items() if k in p["abbr"])
    else:
        abbr = "".join(f"<tr><td><b>{(v[0] if lang == 'en' else v[2])}</b></td><td>{(v[4] if lang == 'en' else v[5])}</td><td>{(v[1] if lang == 'en' else v[0])}</td><td>{ABBR_HU[k][0]}</td></tr>"
                       for k, v in ABBR.items() if k in p["abbr"])
    mats = "".join(f"<li>{g(m, 'text')}</li>" for m in p["materials"])
    secs = ""
    for s in p["sections"]:
        rows = "".join(f'<div class="row"><div class="l">{g(r, "label")}</div><div>{r[lang]}</div><div class="c">{"(" + str(r["count"]) + " " + t["sts"] + ")" if "count" in r else ""}</div></div>' for r in s["rows"])
        note = f'<div class="note">{g(s, "note")}</div>' if g(s, "note") else ""
        secs += f'<h2>{g(s, "title")}</h2>{note}{rows}'
    fin = "".join(f"<li>{g(f, 'text')}</li>" for f in p["finishing"])
    notes = "".join(f"<li>{g(n, 'text')}</li>" for n in p.get("notes", []))
    more = "".join(f'<img src="fotok/{x.name}">' for x in photos[1:5])
    sys.path.insert(0, str(Path(__file__).resolve().parent)); import crochet_charts as CC
    FT = {"hu": "Ábrák: kész forma és horgolásrajz", "en": "Diagrams: finished shape and stitch chart", "de": "Diagramme: fertige Form und Häkelschrift"}[lang]
    figs = "".join(f'<div class="fig">{CC.render(fg, lang)}<div class="cap">{fg.get("cap_" + lang, fg.get("cap_en", ""))}</div></div>' for fg in p.get("figures", []))
    if figs:
        kinds = p.get("legend", ["ch", "sl", "sc", "inc", "dec", "mr"])
        figs = f'<h2 class="figh">{FT}</h2><div class="figs">{figs}</div><div class="fig leg">{CC.legend(kinds, lang)}</div>'
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>{g(p, 'name')}</title><style>{CSS}</style></head><body>
{'<div class="draft">' + t['draft'] + '</div>' if draft else ''}
<h1>{g(p, 'name')}</h1><div class="sub">{g(p, 'tagline')}</div>{hero}
<div class="meta"><div><b>{t['level']}</b>{g(p, 'level')}</div><div><b>{t['size']}</b>{g(p, 'size')}</div>
<div><b>{t['hook']}</b>{p['hook']}</div><div><b>{t['gauge']}</b>{g(p, 'gauge')}</div></div>
<h2>{t['mat']}</h2><ul>{mats}</ul>
<h2>{t['abbr']}</h2><table><tr><th></th><th></th><th>{t['uk']}</th><th>{t['hu']}</th></tr>{abbr}</table>
{('<h2>' + t['notes'] + '</h2><ul>' + notes + '</ul>') if notes else ''}
{figs}
{secs}<h2>{t['fin']}</h2><ul>{fin}</ul>{('<div class="photos">' + more + '</div>') if more else ''}
<div class="foot">© AureliaVenn · {t['copy']}<br>{t['tested'] if not draft else ''}</div></body></html>"""


def main():
    folder = Path(sys.argv[1]).resolve(); draft = "--draft" in sys.argv
    p = json.loads((folder / "pattern.json").read_text())
    err = check(p)
    if err:
        print("SZEMSZÁM-HIBA:\n" + "\n".join(err)); sys.exit(1)
    for lang in p.get("langs", ["en", "de"]):
        f = folder / f'{p["slug"]}-{lang.upper()}.html'
        f.write_text(html(p, lang, folder, draft), encoding="utf-8")
        subprocess.run(["node", str(ROOT / "scripts" / "render_pdf.js"), str(f)], check=True)
    print("OK", folder, "(draft)" if draft else "")


if __name__ == "__main__":
    main()
