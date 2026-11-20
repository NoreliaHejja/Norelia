#!/usr/bin/env python3
"""
Német KDP-változatok (amazon.de) – 8.5 x 11 in, fekete-fehér, no bleed.

  python3 scripts/kdp_books_de.py malbuch | raetsel | planer | haustier

Kimenet: kdp/<slug>/interior.pdf + meta.json (borító: kdp_cover.py, ugyanaz mint az angolnál).
Német naptár: hétfővel kezdődő hét, német hónapnevek. Szövegek: természetes német, du-forma.
"""
import json, sys, datetime, calendar
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from kdp_books import KDP, html, render, maze_svg, wordsearch, dots_svg, lineart, foot  # noqa: E402

MONATE = ["", "Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
TAGE_LANG = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]


def front(title, sub, owner="Dieses Buch gehört"):
    return [
        f"<div class='page center'><h1>{title}</h1><p class='sub'>{sub}</p><div class='box' style='width:5in;margin-top:.4in'><b>{owner}:</b><div class='line'></div></div></div>",
        "<div class='page'><div style='margin-top:auto' class='sub'>Copyright © 2026 AureliaVenn. Alle Rechte vorbehalten. Gestaltet von unserem kleinen Shop AureliaVenn "
        "mit Unterstützung von KI-Werkzeugen. Kein Teil dieses Buches darf zum Weiterverkauf vervielfältigt werden.</div></div>",
    ]


def malbuch():
    slug = "weihnachts-malbuch-kleinkinder"
    imgs = lineart()
    pages = front("Mein großes Weihnachts-Malbuch", "24 süße Weihnachtsbilder für kleine Hände · 2–5 Jahre")
    pages.append("<div class='page'><h2>Hallo, kleiner Künstler!</h2><p class='sub'>Jedes Bild hat eine leere Rückseite, damit Filzstifte nicht durchdrücken. "
                 "Probiere deine Farben zuerst hier aus.</p><div style='display:grid;grid-template-columns:repeat(4,1fr);gap:.2in;margin-top:.3in'>"
                 + "".join("<div class='box' style='height:1.2in'></div>" for _ in range(12)) + "</div></div>")
    for p in imgs[:24]:
        pages.append(f"<div class='page'><div class='img'><img src='../../linework/{p.name}'></div>{foot()}</div>")
        pages.append("<div class='page'></div>")
    pages.append("<div class='page center'><h1>Super gemacht!</h1><p class='sub'>Du hast dein ganzes Weihnachts-Malbuch ausgemalt.</p><div class='box' style='width:5in'>Unterschrift vom Weihnachtswichtel: <div class='line'></div></div></div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


def raetsel():
    slug = "weihnachts-raetselbuch-kinder"
    imgs = lineart()
    woerter = [["NIKOLAUS", "ENGEL", "BAUM", "STERN", "GESCHENK", "SCHNEE", "GLOCKE", "KERZE"], ["PLÄTZCHEN", "MILCH", "SCHLITTEN", "RENTIER", "WICHTEL", "ZIMT"],
               ["KRANZ", "STIEFEL", "MISTEL", "LICHTER", "MÜTZE", "SCHAL"], ["SCHNEEMANN", "LIED", "FRIEDEN", "FREUDE", "FAMILIE", "KAKAO"],
               ["PINGUIN", "EULE", "BÄR", "HUND", "KATZE", "HASE"], ["KAMIN", "HANDSCHUH", "EIS", "SCHLITTSCHUH", "WINTER", "MARKT"],
               ["SCHLEIFE", "PAPIER", "KARTE", "ADVENT", "KRIPPE", "TANNE"], ["LEBKUCHEN", "BACKEN", "KEKS", "STOLLEN", "NUSS", "APFEL"]]
    # a rácsba ékezet nélkül (Ä→AE stb.), a listán az eredeti alak
    def plain(w): return w.replace("Ä", "AE").replace("Ö", "OE").replace("Ü", "UE")
    pages = front("Weihnachts-Rätselbuch für Kinder", "Labyrinthe, Suchsel, Punkt-zu-Punkt, Schwungübungen und Ausmalbilder · 4–8 Jahre")
    pages.append("<div class='page'><h2>Was ist drin?</h2><div class='box'><p>• 10 Weihnachts-Labyrinthe</p><p>• 8 Wortsuchrätsel (Suchsel)</p><p>• 8 Punkt-zu-Punkt-Bilder</p>"
                 "<p>• Schreib- und Malseiten</p><p>• 12 Ausmalbilder</p><p>• Eine Urkunde zum Schluss!</p></div></div>")
    acts = []
    for i in range(10):
        acts.append(f"<div class='page'><h2>Labyrinth {i+1}: Hilf dem Weihnachtsmann zum Stern!</h2><div class='img'>{maze_svg(10+i//2, 12+i//2, 300+i)}</div>{foot()}</div>")
    for i, ws in enumerate(woerter):
        acts.append(f"<div class='page'><h2>Suchsel {i+1}</h2><p class='sub'>Finde: {' · '.join(ws)} (Ä = AE, Ö = OE, Ü = UE)</p>{wordsearch([plain(w) for w in ws], 400+i)}{foot()}</div>")
    from kdp_books import SHAPES
    namen = {"Star": "Stern", "Christmas Tree": "Tannenbaum", "Bell": "Glocke", "Stocking": "Nikolausstiefel", "Gift": "Geschenk", "Candy Cane": "Zuckerstange", "Heart": "Herz", "House": "Haus"}
    for name, pts in SHAPES.items():
        acts.append(f"<div class='page'><h2>Punkt zu Punkt: {namen[name]}</h2><p class='sub'>Beginne bei 1, verbinde alle Punkte und male das Bild dann aus!</p><div class='img'>{dots_svg(pts)}</div>{foot()}</div>")
    for wd in ["FROHE", "WEIHNACHTEN", "STERN", "SCHNEE"]:
        acts.append("<div class='page'><h2>Schreib das Wort nach</h2>" + "".join(f"<div class='trace'>{wd}</div>" for _ in range(5)) + f"{foot()}</div>")
    acts.append("<div class='page'><h2>Male deinen Weihnachtsbaum</h2><div class='box' style='flex:1'></div></div>")
    acts.append("<div class='page'><h2>Mein Wunschzettel</h2><p class='sub'>Liebes Christkind, lieber Weihnachtsmann, dieses Jahr war ich lieb, als ich …</p>" + "<div class='line'></div>" * 16 + "</div>")
    for k, p in enumerate(imgs[12:24]):
        acts.insert(4 * k + 2, f"<div class='page'><div class='img'><img src='../../linework/{p.name}'></div>{foot()}</div>")
    pages += acts
    pages.append("<div class='page center'><h1>Weihnachts-Champion!</h1><p class='sub'>Diese Urkunde bekommt</p><div class='box' style='width:5in'><div class='line'></div></div><p class='sub' style='margin-top:.3in'>für das ganze Rätselbuch.</p></div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


def planer():
    slug = "familienplaner-2027"
    pages = front("Familienplaner 2027", "Monats- und Wochenplaner für Mamas und Familien · Januar bis Dezember 2027", "Dieser Planer gehört")
    cal = calendar.Calendar(firstweekday=0)
    yr = "".join(f"<div class='box' style='padding:.08in'><b>{MONATE[m]}</b><table style='margin-top:4px'><tr>" + "".join(f"<th style='font-size:7pt'>{d}</th>" for d in TAGE) + "</tr>"
                 + "".join("<tr>" + "".join(f"<td style='font-size:7pt;text-align:center;border:none'>{d or ''}</td>" for d in wk) + "</tr>" for wk in cal.monthdayscalendar(2027, m)) + "</table></div>" for m in range(1, 13))
    pages.append(f"<div class='page'><h2>2027 auf einen Blick</h2><div style='display:grid;grid-template-columns:repeat(3,1fr);gap:.12in'>{yr}</div></div>")
    pages.append("<div class='page'><h2>Unsere Familienziele für 2027</h2>" + "".join(f"<div class='box' style='margin-bottom:.12in'><b>{t}</b><div class='line'></div><div class='line'></div></div>" for t in ["Gesundheit", "Zuhause", "Finanzen", "Ausflüge & Urlaub", "Kinder", "Nur für mich"]) + "</div>")
    pages.append("<div class='page'><h2>Geburtstage & wichtige Termine</h2><table>" + "".join(f"<tr><th style='width:1.4in'>{MONATE[m]}</th><td style='height:.62in'></td></tr>" for m in range(1, 13)) + "</table></div>")
    mondays = [datetime.date(2027, 1, 4) + datetime.timedelta(days=7 * i) for i in range(52)]
    for m in range(1, 13):
        rows = "".join("<tr>" + "".join(f"<td style='height:1.3in;font-size:9pt'>{d or ''}</td>" for d in wk) + "</tr>" for wk in cal.monthdayscalendar(2027, m))
        pages.append(f"<div class='page'><h2>{MONATE[m]} 2027</h2><table><tr>" + "".join(f"<th>{d}</th>" for d in TAGE_LANG) + f"</tr>{rows}</table></div>")
        pages.append(f"<div class='page'><h2>{MONATE[m]}: Pläne & Notizen</h2><div style='display:grid;grid-template-columns:1fr 1fr;gap:.2in;flex:1'>"
                     + "".join(f"<div class='box'><b>{t}</b>" + "<div class='line'></div>" * 8 + "</div>" for t in ["Top 3 diesen Monat", "Termine", "Neue Rezepte", "Kinder & Schule/Kita"]) + "</div></div>")
        for wk in [d for d in mondays if d.month == m]:
            days = "".join(f"<div class='box' style='padding:.08in'><b>{TAGE_LANG[i]}, {(wk+datetime.timedelta(days=i)).day}. {MONATE[(wk+datetime.timedelta(days=i)).month]}</b>"
                           + "<div class='line' style='height:.3in'></div>" * 3 + "</div>" for i in range(7))
            pages.append(f"<div class='page'><h2>Woche ab {wk.day}. {MONATE[wk.month]} (KW {wk.isocalendar()[1]})</h2><div style='display:grid;grid-template-columns:1fr 1fr;gap:.1in'>{days}"
                         "<div class='box' style='padding:.08in'><b>Essen · To-dos · Kinder</b>" + "<div class='line' style='height:.3in'></div>" * 3 + "</div></div></div>")
    for _ in range(4):
        pages.append("<div class='page'><h2>Notizen</h2>" + "<div class='line'></div>" * 24 + "</div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


def haustier():
    slug = "haustier-gesundheitsheft"
    pages = front("Mein Haustier-Gesundheitsheft", "Impfungen, Tierarztbesuche, Gewicht und Pflege-Tagebuch für Katze und Hund", "Name meines Haustiers")
    pages.append("<div class='page'><h2>Steckbrief</h2><div class='box' style='height:3in;margin-bottom:.2in;text-align:center'>Hier ein Foto einkleben</div><table>"
                 + "".join(f"<tr><th style='width:2.2in'>{t}</th><td style='height:.4in'></td></tr>" for t in ["Name", "Tierart / Rasse", "Geburtstag / Einzugstag", "Farbe & Merkmale", "Chip-Nummer", "Lieblingsfutter", "Lieblingsspielzeug", "Tierarzt & Telefon", "Tiernotdienst", "Versicherung"]) + "</table></div>")
    for titel, cols in [("Impfungen", ["Datum", "Impfung", "Nächste fällig", "Tierarzt"]), ("Floh-, Zecken- & Wurmbehandlung", ["Datum", "Mittel", "Nächste fällig", "Notizen"])]:
        pages.append(f"<div class='page'><h2>{titel}</h2><table><tr>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr>" + "<tr><td style='height:.42in'></td><td></td><td></td><td></td></tr>" * 18 + "</table></div>")
    pages.append("<div class='page'><h2>Gewichtsverlauf</h2><table><tr><th>Datum</th><th>Gewicht</th><th>Notizen</th></tr>" + "<tr><td style='height:.42in'></td><td></td><td></td></tr>" * 18 + "</table></div>")
    for _ in range(12):
        pages.append("<div class='page'><h2>Tierarztbesuch</h2><table>" + "".join(f"<tr><th style='width:2in'>{t}</th><td style='height:.5in'></td></tr>" for t in ["Datum", "Grund", "Gewicht", "Diagnose", "Behandlung / Medikament", "Kosten", "Kontrolle"]) + "</table><p class='sub' style='margin-top:.2in'>Notizen</p>" + "<div class='line'></div>" * 6 + "</div>")
    for _ in range(52):
        rows = "".join(f"<tr><th>{d}</th>" + "<td style='height:.9in'></td>" * 4 + "</tr>" for d in TAGE)
        pages.append(f"<div class='page'><h2>Wöchentliches Pflege-Tagebuch</h2><p class='sub'>Woche vom: ______________</p><table><tr><th style='width:.8in'>Tag</th><th>Futter</th><th>Wasser</th><th>Gassi / Spielen</th><th>Stimmung & Notizen</th></tr>{rows}</table>"
                     "<p class='sub' style='margin-top:.15in'>Eine Planungshilfe – kein Ersatz für tierärztlichen Rat.</p></div>")
    for _ in range(6):
        pages.append("<div class='page'><h2>Schöne Erinnerungen</h2><div class='box' style='flex:1'></div></div>")
    out = KDP / slug / "tmp" / "interior.html"; html(pages, out)
    return slug, render(out, KDP / slug / "interior.pdf")


if __name__ == "__main__":
    fn = {"malbuch": malbuch, "raetsel": raetsel, "planer": planer, "haustier": haustier}[sys.argv[1]]
    slug, n = fn()
    (KDP / slug / "meta.json").write_text(json.dumps({"slug": slug, "pages": n, "lang": "de"}, indent=2))
