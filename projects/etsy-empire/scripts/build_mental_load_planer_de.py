#!/usr/bin/env python3
"""Mental-Load-Planer (DE) – deutscher Begleit-Planer zu „Und wer kümmert sich um Mama?” (Gentle Life Guides, Etsy-csatorna, 2026-11-28).
Saját munkalapok, a build_mental_load_planner.py CSS-ével. → termekek/mental-load-planer/"""
from pathlib import Path
from common import page_head, icon, footer
from build_mental_load_planner import CSS

SLUG = "mental-load-planer"
NAME = "Mental-Load-Planer"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

TASKS = {
    "Kinder": ["Elternbriefe und Formulare", "Arzt- und Zahnarzttermine", "Geburtstagsgeschenke und Kindergeburtstage", "Zu kleine Kleidung aussortieren", "Kurse, Anmeldungen, Termine", "Hausaufgaben und Lesen", "Abendroutine"],
    "Haushalt": ["Essensplanung", "Einkaufsliste und Einkauf", "Abendessen kochen", "Wäsche von Anfang bis Ende", "Sehen, was geputzt werden muss", "Klopapier, Seife & Co. nachkaufen", "Reparaturen und Handwerker"],
    "Familienleben": ["Familienkalender", "Feiertage und Geschenke", "Geburtstage der Verwandten", "Wochenenden planen", "Haustier und Tierarzt", "Rechnungen und Papierkram", "Danke sagen, Karten schreiben"],
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    L = lambda n: "".join('<div class="ln"></div>' for _ in range(n))
    pg = [f'<div class="page cv"><div>{icon("heart",110,"#b0607a",1.2)}</div><div class="eyebrow">Planer zum Ausdrucken · Für Paare und Familien</div>'
          f'<h1>Mental-Load-<br>Planer</h1><div class="tg">Mach jede unsichtbare Aufgabe sichtbar, verteile sie fair und plane ein ruhiges Gespräch darüber. Arbeitsblätter für eine gerechtere Woche zu Hause.</div>'
          f'<div class="pill">9 Seiten · A4 + US Letter</div></div>']
    pg.append(f"""<div class="page">{page_head("So geht's", "So nutzt du den Planer", "book")}
<p class="subtitle">Mental Load ist das Mitdenken, Erinnern und Planen, das eine Familie am Laufen hält. Es ist echte Arbeit, auch wenn sie niemand sieht. Dieser Planer macht sie sichtbar, damit ihr sie teilen könnt.</p>
<div class="step"><div class="num">1</div><div><b>Alles aufschreiben</b><p>Trag in die Aufgabenliste alles ein, was in deinem Kopf wohnt. Ergänze, was in eurer Familie fehlt.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Wer macht was?</b><p>Für jede Aufgabe: Wer denkt daran, wer plant, wer erledigt? Die meisten Paare staunen über die Spalte „denkt daran“.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Einmal ruhig sprechen</b><p>Bereite das Gespräch mit der Gesprächsseite vor. Wähl einen ruhigen Moment, nicht mitten im vollen Abend.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Ganze Aufgaben abgeben</b><p>Nicht „hilf mir dabei“, sondern „das gehört jetzt dir, vom Daran-Denken bis zum Erledigen“. Dann startet ihr den 7-Tage-Neustart.</p></div></div>
{footer(NAME, "Start")}</div>""")
    for area, tasks in TASKS.items():
        rows = "".join(f"<tr><td>{t}</td><td class='c'></td><td class='c'></td><td class='c'></td></tr>" for t in tasks) + "".join("<tr><td></td><td class='c'></td><td class='c'></td><td class='c'></td></tr>" for _ in range(5))
        pg.append(f'<div class="page">{page_head("Aufgabenliste", f"{area}: wer denkt, plant, macht?", "check")}<p class="subtitle">Kürzel in jede Spalte schreiben. Eigene Aufgaben in die leeren Zeilen.</p><table class="inv"><tr><th>Aufgabe</th><th>Denkt</th><th>Plant</th><th>Macht</th></tr>{rows}</table>{footer(NAME, "Aufgaben")}</div>')
    pg.append(f"""<div class="page">{page_head("Was ich sehe", "Meine unsichtbare Liste", "star")}
<div class="two"><div class="box"><h3>Woran ich immer denke</h3>{L(6)}</div><div class="box"><h3>Was mich nachts wach hält</h3>{L(6)}</div></div>
<div class="box"><h3>Eine Sache, an die ich nie wieder denken möchte</h3>{L(2)}</div><div class="box"><h3>Was ich gerade am meisten brauche</h3>{L(2)}</div>{footer(NAME, "Meine Liste")}</div>""")
    pg.append(f"""<div class="page">{page_head("Vorbereiten", "Das ruhige Gespräch", "heart")}
<div class="box"><h3>Wann und wo</h3><div class="mini">Ein ruhiger Moment, ohne Bildschirm, nicht kurz vor dem Schlafen: ______________________________</div></div>
<div class="box"><h3>Sätze, die du sagen kannst</h3><div class="say">„Ich möchte, dass wir uns wie ein Team fühlen. Schauen wir uns die Liste zusammen an?“</div>
<div class="say">„Ich bitte nicht um Hilfe. Ich wünsche mir, dass du ein paar Aufgaben ganz übernimmst, vom Anfang bis zum Ende.“</div>
<div class="say">„Welche drei Aufgaben möchtest du ganz übernehmen?“</div></div>
<div class="box"><h3>Worum ich bitten möchte</h3>{L(3)}</div><div class="box"><h3>Was wir vereinbart haben</h3>{L(3)}</div>{footer(NAME, "Gespräch")}</div>""")
    days = "".join(f'<div class="dy"><b>Tag {d}</b><div><div class="tick"><span></span><em>{t}</em></div><div class="ln" style="height:.22in"></div></div></div>' for d, t in enumerate(
        ["Aufgabenliste gemeinsam ausfüllen", "3 Aufgaben komplett abgeben", "Die abgegebenen Aufgaben an den Kühlschrank hängen", "Bemerken, nicht korrigieren: die neue Person macht es auf ihre Art",
         "15 Minuten nur für mich", "Gemeinsame Wochenplanung (10 Minuten)", "Rückblick: Was fühlt sich leichter an?"], 1))
    pg.append(f'<div class="page">{page_head("Jeden Tag ein kleiner Schritt", "7-Tage-Neustart", "calendar")}<div class="days">{days}</div>{footer(NAME, "7 Tage")}</div>')
    pg.append(f"""<div class="page">{page_head("Jeden Sonntag", "Familien-Check-in", "check")}
<div class="two"><div class="box"><h3>Termine dieser Woche</h3>{L(5)}</div><div class="box"><h3>Wer übernimmt was diese Woche</h3>{L(5)}</div></div>
<div class="box"><h3>Was gut lief</h3>{L(2)}</div><div class="box"><h3>Was wir nächste Woche ändern</h3>{L(2)}</div>
<div class="card warm" style="margin-bottom:.15in"><h3>Mehr dazu?</h3><div class="mini">Dieser Planer begleitet das Buch <b>„Und wer kümmert sich um Mama?”</b> von Clara Whitfield (Gentle Life Guides), einen sanften Ratgeber zur unsichtbaren Last. Erhältlich bei Amazon.</div></div>
{footer(NAME, "Nur für den privaten Gebrauch · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
