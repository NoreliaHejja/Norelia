#!/usr/bin/env python3
"""Christmas on My Own Planner – nyomtatható kísérő a „Still Lit” könyvhöz (Etsy-csatorna, C) feladat).
Új, saját munkalapok (nem a könyv szövege → KDP Select rendben). → termekek/christmas-on-my-own-planner/"""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "weihnachten-allein-planer"
NAME = "Weihnachten allein – Planer"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """:root{ --dark:#3b4a6b; --sage:#b5485d; --tint:#f8eef0; --line:#e6d3d8; --accent:#d9a441; --warm:#eef1f7; --warmline:#cfd6e6; --cream:#fcf8f5; }
.cv{ background:linear-gradient(180deg,#fcf8f5,#eef1f7); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:38pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.ln{ border-bottom:1.5px solid var(--line); height:.36in; }
.box{ border:2px solid var(--line); border-radius:14px; padding:12px 14px; background:#fff; margin-bottom:12px; }
.box h3{ margin:0 0 6px; color:var(--sage); font-size:13pt; }
.tick{ display:flex; gap:8px; align-items:center; font-size:11.5pt; margin:5px 0; } .tick em{ font-style:normal; flex:1; min-width:0; } .tick span{ width:15px; height:15px; border:2px solid var(--dark); border-radius:4px; flex:0 0 auto; }
.two{ display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:.1in; }
.cal{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; flex:1; margin-bottom:.1in; }
.cal div{ border:1.5px solid var(--line); border-radius:10px; padding:7px 8px; background:#fff; font-size:10pt; line-height:1.3; }
.cal b{ display:block; color:var(--sage); font-size:13pt; margin-bottom:2px; }
.slot{ display:grid; grid-template-columns:1.1in 1fr; gap:6px 10px; align-items:end; margin:4px 0; } .slot i{ font-style:normal; font-weight:600; color:var(--dark); font-size:11pt; } .slot u{ text-decoration:none; border-bottom:1.5px solid var(--line); height:.34in; }
.quote{ border-left:4px solid var(--accent); padding:6px 12px; background:var(--tint); border-radius:0 10px 10px 0; font-size:11pt; margin:6px 0; }
"""

ADVENT = ["Zünde eine Kerze an und mach dir ein warmes Getränk", "Hör ein Lied, das du mit 16 geliebt hast", "Geh dorthin spazieren, wo Lichter leuchten", "Schreib 3 Dinge auf, die heute gut liefen",
          "Gönn dir eine kleine Leckerei, ohne Grund", "Schreib jemandem, den du vermisst, eine kurze Nachricht", "Schau einen Film deiner Wahl, mit Snacks",
          "Räum eine kleine Ecke auf und freu dich daran", "Stell eine Playlist für Heiligabend zusammen", "Fotografiere etwas Schönes", "Koch ein Rezept, das du noch nie probiert hast",
          "Plane dein Frühstück für den 24. Dezember", "Sag Nein zu einer Sache, die du nicht willst", "Spende etwas oder hinterlass eine liebe Notiz",
          "Telefoniere oder videochatte 10 Minuten mit jemandem", "Nimm ein langes Bad oder eine Dusche mit Musik", "Schreib eine Karte an dich selbst fürs nächste Jahr",
          "Besuch einen Weihnachtsmarkt, ein Kirchenkonzert oder die Bücherei", "Geh früh mit einem Buch ins Bett", "Stell frische Blumen oder Tannenzweige auf den Tisch",
          "Pack deine Notfall-Kiste für schwere Momente", "Such dir dein Heiligabend-Outfit aus, nur für dich", "Bereite alles für einen gemütlichen morgigen Tag vor",
          "Heiligabend: Mach das eine, was sich am meisten nach dir anfühlt"]
COMFORT = ["Ein Spaziergang bei Sonnenauf- oder -untergang", "Mein Lieblingsfilm oder meine Lieblingsserie", "Ein warmes Essen, das ich nur für mich koche", "Ein langes Telefonat",
           "10 Minuten Tagebuch schreiben", "Laute Musik, Tanzen in der Küche", "Ein Puzzle, Basteln oder ein Buch", "Ein paar Stunden ehrenamtlich helfen"]
SCRIPTS = [("Wenn jemand fragt: „Bist du immer noch Single?“", "„Ja, und mein Leben ist gerade ganz schön voll. Wie geht es dir?“"),
           ("Wenn du eine Einladung absagen möchtest", "„Danke, dass du an mich denkst. Dieses Jahr halte ich es ruhig, aber im Januar sehe ich dich sehr gern.“"),
           ("Wenn du zusagen möchtest, zu deinen Bedingungen", "„Zum Nachtisch komme ich gern. Gegen neun mache ich mich auf den Heimweg.“"),
           ("Wenn du dich melden möchtest", "„Ich verbringe Weihnachten dieses Jahr ruhig. Hast du Lust, am 25. per Video eine Tasse Tee mit mir zu trinken?“")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#d9a441",1.2)}</div><div class="eyebrow">Planer zum Ausdrucken · Für alle, die die Feiertage allein verbringen</div>'
          f'<h1>Weihnachten<br>allein</h1><div class="tg">Ein sanfter, praktischer Plan für ein ruhiges Weihnachten, das sich nach dir anfühlt: ein Dezember voller kleiner Lichtblicke, ein Plan für Heiligabend, Worte für die Fragen der Familie und ein Plan für die schweren Momente.</div>'
          f'<div class="pill">10 Seiten · A4 + US Letter</div></div>']
    pg.append(f"""<div class="page">{page_head("Hier anfangen", "So nutzt du deinen Planer", "book")}
<p class="subtitle">Die Feiertage allein zu verbringen kann sich schwer anfühlen oder frei, und oft ist es beides. Dieser Planer gibt der Zeit eine Form, damit die schwersten Tage dich nicht unvorbereitet treffen.</p>
<div class="step"><div class="num">1</div><div><b>Entscheide, was du willst</b><p>Beginne mit „Mein Dezember, mein Weg“. Du bestimmst, was bleibt, was geht und was dieses Jahr neu ist.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Jeden Tag ein kleiner Lichtblick</b><p>Der 24-Tage-Kalender schenkt jedem Dezembertag eine kleine, freundliche Sache für dich. Abhaken oder austauschen.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Heiligabend planen</b><p>Ein leerer Tag fühlt sich am längsten an. Gib ihm ein paar Anker: ein Frühstück, ein Spaziergang, ein Anruf, ein Film, ein Essen.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Vorsorgen für schwere Momente</b><p>Füll deinen Plan und deine Kontaktliste an einem guten Tag aus, dann ist sie an einem schweren bereit.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Ein Plan, keine Prüfung</h3><div class="mini">Wenn ein Tag anders läuft, ist das in Ordnung. Morgen ist eine neue Seite.</div></div>
<div class="card warm col"><h3>Du bist nicht die Einzige</h3><div class="mini">Viele Menschen verbringen die Feiertage allein, freiwillig oder nicht. Mit dir ist alles in Ordnung.</div></div></div>
{footer(NAME, "Hier anfangen")}</div>""")
    pg.append(f"""<div class="page">{page_head("Deine Zeit, deine Regeln", "Mein Dezember, mein Weg", "heart")}
<div class="two"><div class="box"><h3>Traditionen, die ich behalten will</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Was ich dieses Jahr loslasse</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="two"><div class="box"><h3>Etwas Neues, das ich ausprobieren will</h3><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Mein Budget für die Feiertage</h3><div class="ln"></div><div class="ln"></div></div></div>
<div class="box"><h3>Wie ich mich am 31. Dezember fühlen möchte</h3><div class="ln"></div><div class="ln"></div></div>
{footer(NAME, "Mein Dezember")}</div>""")
    for i in (0, 12):
        cells = "".join(f"<div><b>{d + 1}</b>{ADVENT[d]}</div>" for d in range(i, i + 12))
        pg.append(f'<div class="page">{page_head("Jeden Tag ein Lichtblick", f"Lichtblick-Kalender · {i + 1}.–{i + 12}. Dezember", "calendar")}<div class="cal">{cells}</div>{footer(NAME, "Lichtblick-Kalender")}</div>')
    slots = "".join(f'<div class="slot"><i>{t}</i><u></u></div>' for t in ["Aufwachen", "Frühstück", "Vormittag", "Raus an die Luft", "Mittag", "Nachmittag", "Anruf / Nachricht", "Abendessen", "Abend", "Vor dem Schlafen"])
    pg.append(f"""<div class="page">{page_head("Gib dem Tag eine Form", "Mein Plan für Heiligabend", "star")}
<p class="subtitle">Trag ein paar Anker ein, nicht jede Stunde. Lass Raum für Ruhe.</p>
<div class="box">{slots}</div>
<div class="box"><h3>Eine Sache, die den Tag besonders macht</h3><div class="ln"></div></div>
{footer(NAME, "Heiligabend")}</div>""")
    sc = "".join(f'<div class="box"><h3>{q}</h3><div class="quote">{a}</div><div class="mini">Meine Version:</div><div class="ln"></div></div>' for q, a in SCRIPTS)
    pg.append(f'<div class="page">{page_head("Worte, bevor du sie brauchst", "Was ich sagen kann", "book")}{sc}{footer(NAME, "Was ich sagen kann")}</div>')
    comf = "".join(f'<div class="tick"><span></span><em>{x}</em></div>' for x in COMFORT)
    pg.append(f"""<div class="page">{page_head("An einem guten Tag ausfüllen", "Mein Plan für schwere Momente", "heart")}
<div class="box"><h3>Erste Anzeichen, dass ein schwerer Moment kommt</h3><div class="ln"></div><div class="ln"></div></div>
<div class="two"><div class="box"><h3>Mein Trostmenü (ankreuzen)</h3>{comf}<div class="ln"></div></div>
<div class="box"><h3>Menschen, die ich erreichen kann</h3><div class="mini">Name · wie · wann</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="card warm" style="margin-bottom:.15in"><h3>Wenn es zu schwer wird</h3><div class="mini">Du musst das nicht allein tragen. Die <b>Telefonseelsorge</b> ist rund um die Uhr kostenlos erreichbar: <b>0800 111 0 111</b> oder <b>0800 111 0 222</b>. Österreich: <b>142</b>, Schweiz: <b>143</b>. Wenn du in Gefahr bist, ruf sofort <b>112</b> an.</div></div>
{footer(NAME, "Schwere Momente")}</div>""")
    pg.append(f"""<div class="page">{page_head("Ein sanfter Rückblick", "Meine Feiertage im Rückblick", "check")}
<div class="two"><div class="box"><h3>Was besser lief als befürchtet</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Was ich nächstes Jahr anders mache</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="box"><h3>Drei gute Momente aus diesem Dezember</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Eine Notiz an mich für den nächsten Dezember</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
{footer(NAME, "Rückblick")}</div>""")
    pg.append(f"""<div class="page">{page_head("Extra-Seiten", "Notizen und Listen", "book")}
<div class="two"><div class="box"><h3>Geschenke, die ich mache (oder nicht)</h3>{''.join('<div class="ln"></div>' for _ in range(8))}</div>
<div class="box"><h3>Karten und Nachrichten</h3>{''.join('<div class="ln"></div>' for _ in range(8))}</div></div>
<div class="card warm" style="margin-bottom:.15in"><h3>Du möchtest mehr?</h3><div class="mini">Dieser Planer begleitet das Buch <b>Noch brennt das Licht</b> von Clara Whitfield (Gentle Life Guides): ein sanfter, praktischer Ratgeber für Frauen, die sich an Weihnachten allein fühlen. Erhältlich bei Amazon. Der Planer funktioniert auch für sich allein.</div></div>
{footer(NAME, "Nur für den privaten Gebrauch · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
