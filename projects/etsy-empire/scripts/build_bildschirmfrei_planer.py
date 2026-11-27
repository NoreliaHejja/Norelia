#!/usr/bin/env python3
"""Bildschirmfrei-Planer für die Weihnachtsferien – deutscher Begleit-Planer zu „Gib ihnen ihr Staunen zurück” (Gentle Life Guides, Etsy-csatorna, C) feladat).
Saját munkalapok (nem a könyv szövege → KDP Select rendben). Stílus: a build_screenfree_planner.py CSS-e. → termekek/bildschirmfrei-ferien-planer/"""
from pathlib import Path
from common import page_head, icon, footer
from build_screenfree_planner import CSS

SLUG = "bildschirmfrei-ferien-planer"
NAME = "Bildschirmfrei-Ferienplaner"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

SLIPS = ["Eine Deckenhöhle bauen und darin lesen", "Eine Karte von unserer Straße malen", "Papierflieger-Wettbewerb", "Etwas mit nur 4 Zutaten backen",
         "Familienband mit Töpfen und Löffeln", "Einen Brief an Oma oder Opa schreiben", "Ein eigenes Brettspiel erfinden", "Zusammen ein Puzzle legen",
         "Winterspaziergang: Vögel zählen", "Sockenpuppen-Theater", "Vogelfutter aus einem Tannenzapfen", "Verstecken spielen",
         "Murmelbahn aus Klopapierrollen", "Drei Kartentricks lernen", "Eine Zeitkapsel fürs nächste Jahr", "Picknick im Wohnzimmer",
         "Einen Comic über unser Haustier zeichnen", "Pantomime raten", "Schneeflocken aus Papier schneiden", "Tanzparty: 3 Lieder",
         "Salzteig-Anhänger formen", "Den höchsten Turm bauen", "Altes Spielzeug zum Verschenken sortieren", "Eine Geschichte: jeder sagt ein Wort",
         "Mit einem Erwachsenen das Abendessen kochen", "Schatzsuche in der Wohnung", "Eine Dankeskarte für die Nachbarn", "Taschenlampen-Ich-sehe-was",
         "Ein neues Kartenspiel ausprobieren", "Natur-Collage kleben", "Eine Zaubershow üben", "Samen in einem Becher pflanzen"]
AGREE = ["Nachts bleiben Bildschirme aus dem Kinderzimmer", "Beim Essen keine Bildschirme", "Wir sagen 10 Minuten vorher Bescheid, bevor der Bildschirm ausgeht",
         "Filmabend ist gemeinsame Bildschirmzeit", "Auch Erwachsene legen beim Spielen das Handy weg", "Bei „Mir ist langweilig” ziehen wir einen Zettel aus dem Glas"]
LAND = ["Ein Snack am Tisch", "Ein Puzzle liegt schon bereit", "Musik an, fünf Minuten tanzen", "Einmal um den Block gehen",
        "Papier und neue Stifte", "Zusammen ein Bilderbuch lesen"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#e0a526",1.2)}</div><div class="eyebrow">Planer zum Ausdrucken · Ferien · 3–12 Jahre</div>'
          f'<h1>Bildschirmfrei<br>in den Ferien</h1><div class="tg">Ein ruhiger Plan für weniger Bildschirm und mehr Lachen: Familienvereinbarung, 14-Tage-Rhythmus, Langeweile-Glas-Zettel und Countdown-Karten.</div>'
          f'<div class="pill">9 Seiten · A4 + US Letter</div></div>']
    pg.append(f"""<div class="page">{page_head("So geht's", "So nutzt du den Planer", "book")}
<p class="subtitle">Nicht der Bildschirm ist das Problem, sondern lange, leere Tage. Dieser Planer gibt den Ferien eine Form, damit der Bildschirm ein Teil des Tages wird und nicht der ganze Tag.</p>
<div class="step"><div class="num">1</div><div><b>Füllt die Vereinbarung gemeinsam aus</b><p>Setzt euch vor dem ersten freien Tag mit den Kindern zusammen und einigt euch auf ein paar einfache Regeln. Kinder halten sich eher an Regeln, die sie mitgemacht haben.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Plant euren Rhythmus</b><p>Im 14-Tage-Planer: pro Tag eine Zeit draußen, eine ruhige Zeit und eine gemeinsame Sache. Lass auch Platz für gar nichts.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Füllt das Langeweile-Glas</b><p>Schneide die 32 Zettel aus und ergänzt eigene Ideen. Auf „Mir ist langweilig” gibt es jetzt eine Antwort, die kein Bildschirm ist.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Nutzt die Countdown-Karten</b><p>Zeig die Karten 10-5-1, bevor der Bildschirm ausgeht, und halte eine „Landeaktivität” bereit. So gibt es weniger Tränen.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Die ersten Tage holpern</h3><div class="mini">Viele Familien merken: Die ersten zwei, drei Tage sind die schwersten. Bleib dran, meistens wird es leichter.</div></div>
<div class="card warm col"><h3>Sei nett zu dir</h3><div class="mini">Ein Film an einem schweren Nachmittag ist kein Versagen. Das ist ein Plan, keine Prüfung.</div></div></div>
{footer(NAME, "Start")}</div>""")
    rules = "".join(f'<div class="tick"><span></span><em>{r}</em></div>' for r in AGREE)
    pg.append(f"""<div class="page">{page_head("Gemeinsam machen", "Unsere Ferien-Vereinbarung", "heart")}
<div class="box"><h3>Unsere Ziele für diese Ferien</h3><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Unsere Bildschirm-Regeln (ankreuzen oder ergänzen)</h3>{rules}<div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Bildschirmzeit an einem normalen Ferientag</h3><div class="mini">Wann: ____________________ &nbsp; Wie lange: ______________ &nbsp; Wo: ____________________</div></div>
<div class="box"><h3>Wenn wir die Regeln vergessen, dann…</h3><div class="ln"></div></div>
<div class="sig"><div>Unterschrift</div><div>Unterschrift</div><div>Unterschrift</div></div>{footer(NAME, "Vereinbarung")}</div>""")
    for start in (1, 8):
        ds = "".join(f'<div class="day"><b>Tag {d}</b> &nbsp;<span style="color:#888">Datum ______</span><div class="r"><i>Draußen</i><u></u><i>Ruhig</i><u></u><i>Zusammen</i><u></u><i>Bildschirm</i><u></u></div></div>' for d in range(start, start + 7))
        ds += '<div class="day"><b>Notizen</b><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>'
        pg.append(f'<div class="page">{page_head("Jeden Tag ein kleiner Plan", f"Ferien-Rhythmus · Tag {start}–{start+6}", "calendar")}<div class="days">{ds}</div>{footer(NAME, "Planer")}</div>')
    for i in (0, 16):
        s = "".join(f"<div>{x}</div>" for x in SLIPS[i:i + 16])
        pg.append(f'<div class="page">{page_head("Ausschneiden, falten, ins Glas", "Zettel fürs Langeweile-Glas", "star")}<div class="slips">{s}</div>{footer(NAME, "Glas-Zettel")}</div>')
    land = "".join(f'<div class="tick"><span></span><em>{x}</em></div>' for x in LAND)
    pg.append(f"""<div class="page">{page_head("Wenn der Bildschirm ausgeht", "Countdown-Karten + Landeaktivitäten", "check")}
<div class="cd"><div><b>10</b><span>Minuten noch.<br>Such eine gute Stelle zum Aufhören.</span></div><div><b>5</b><span>Minuten noch.<br>Spiel speichern.</span></div><div><b>1</b><span>Minute noch.<br>Zeit zum Landen!</span></div></div>
<div class="two"><div class="box"><h3>Unsere Landeaktivitäten</h3>{land}<div class="ln"></div></div>
<div class="box"><h3>Gute Bildschirmzeit, die wir gemeinsam mögen</h3><div class="mini">Filmabend, Videoanruf mit der Familie, etwas erschaffen (Trickfilm, Musik), etwas lernen, das wir lieben.</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
{footer(NAME, "Countdown")}</div>""")
    pg.append(f"""<div class="page">{page_head("Ende der Ferien", "Was hat sich verändert?", "heart")}
<div class="two"><div class="box"><h3>Vor den Ferien</h3><div class="mini">Wie haben sich die Abende angefühlt? Wie haben die Kinder gespielt?</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Nach den Ferien</h3><div class="mini">Was war anders? Was wollen wir behalten?</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="box"><h3>Unsere schönste Erinnerung an diese Ferien</h3><div class="ln"></div><div class="ln"></div></div>
<div class="card warm" style="margin-bottom:.15in"><h3>Mehr dazu?</h3><div class="mini">Dieser Planer begleitet das Buch <b>„Gib ihnen ihr Staunen zurück”</b> von Clara Whitfield (Gentle Life Guides), mit 100 Spielen ohne Bildschirm und einem ganzen Ferien-Plan. Erhältlich bei Amazon.</div></div>
{footer(NAME, "Nur für den privaten Gebrauch · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
