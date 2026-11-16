#!/usr/bin/env python3
"""Classroom Kindness Calendar – tanároknak: 24 osztálykedvesség-feladat, faliposzter-naptár, osztály-tracker, tanulói oklevelek, szülői levél.
Manó nélkül (a „Classroom Elf” alig kap forgalmat). → termekek/classroom-kindness-calendar/"""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "classroom-kindness-calendar"
NAME = "Classroom Kindness Calendar"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """:root{ --dark:#2f5d6b; --sage:#c0392b; --tint:#fbefe9; --line:#ecd3c8; --accent:#e0a526; --warm:#eaf2f3; --warmline:#c9dde1; --cream:#fdf8f3; }
.cv{ background:linear-gradient(180deg,#fdf8f3,#eaf2f3); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.grid{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:repeat(3,1fr); gap:12px; flex:1; margin-bottom:.1in; }
.kc{ border:2px dashed var(--line); border-radius:16px; padding:14px 16px; display:flex; flex-direction:column; gap:6px; background:#fff; }
.kc:nth-child(4n+2), .kc:nth-child(4n+3){ background:var(--warm); border-color:var(--warmline); }
.kc .d{ font-size:28pt; font-weight:800; color:var(--sage); line-height:1; } .kc b{ font-size:15pt; line-height:1.2; } .kc p{ margin:0; font-size:12.6pt; line-height:1.45; }
.kc .tip{ margin-top:auto; font-size:10.5pt; color:var(--dark); }
.poster{ display:grid; grid-template-columns:repeat(4,1fr); grid-template-rows:repeat(6,1fr); gap:8px; flex:1; margin-bottom:.1in; }
.poster div{ border:2px solid var(--line); border-radius:12px; padding:6px 8px; background:#fff; font-size:11pt; line-height:1.25; display:flex; flex-direction:column; }
.poster div b{ font-size:16pt; color:var(--sage); } .poster div:nth-child(even) b{ color:var(--dark); }
.track{ width:100%; border-collapse:collapse; margin-bottom:.15in; } .track th, .track td{ border:1.5px solid var(--line); height:.62in; font-size:11.5pt; text-align:center; }
.track th{ background:var(--warm); color:var(--dark); } .track td:first-child{ text-align:left; padding-left:8px; width:2.2in; }
.certs{ display:grid; grid-template-rows:1fr 1fr; gap:16px; flex:1; margin-bottom:.15in; }
.certs > div{ border:6px double var(--accent); border-radius:18px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:16px; background:#fff; }
.certs h2{ font-size:28pt; color:var(--sage); margin:6px 0; } .certs p{ font-size:12.5pt; margin:4px 0; } .certs .ln{ width:3.6in; border-bottom:2px solid var(--dark); height:.45in; margin:4px auto 8px; }
.letter{ flex:1; margin-bottom:.15in; background:#fff; border:2px solid var(--line); border-radius:18px; padding:.4in .5in; } .letter p{ font-size:13pt; line-height:1.6; margin:0 0 12px; }
"""

K = [("Kind words wall", "Each student writes one kind sentence about a classmate on a sticky note for the wall.", "Pair names from a hat so nobody is left out."),
     ("Thank the custodian", "Make a big class thank-you card for the school custodian or cleaning staff.", "Deliver it together."),
     ("Compliment circle", "Sit in a circle; everyone gives the person on their left a real compliment.", "Model one first."),
     ("Hold the door day", "Hold the door for anyone coming behind you all day.", "Count the doors at the end of the day."),
     ("Reading buddies", "Read a picture book to a younger class or a classmate.", "Older grades love this one."),
     ("Tidy-up team", "Leave the classroom cleaner than you found it in 5 minutes.", "Play a song and race the clock."),
     ("Thank-you for the lunch staff", "Draw pictures or write notes for the lunch team.", "Tape them near the lunch line."),
     ("Include someone", "At recess, invite someone new to play.", "Talk about how it felt afterwards."),
     ("Kindness rocks", "Paint or draw on small stones with kind words to hide around school.", "Paper stones work too."),
     ("Help a classmate", "Offer help with something you are good at: reading, math, drawing, tying shoes.", "Make a 'we can help' list."),
     ("Letters to seniors", "Write holiday cards for a local senior home.", "Ask families to help deliver."),
     ("Mystery kindness", "Do one secret kind act today and don't tell anyone.", "Share how it felt, not what it was."),
     ("Teacher appreciation", "Make thank-you cards for another teacher or the principal.", "Every class has a favorite."),
     ("Gratitude chain", "Each student adds a paper link with something they're thankful for.", "Hang it across the room."),
     ("Animal kindness", "Collect old towels or blankets for an animal shelter.", "Send a note home the week before."),
     ("Kind voice day", "Use calm, kind voices all day. Notice when others do too.", "Give 'kind voice' shout-outs."),
     ("Welcome sign", "Make a welcome sign for the school entrance.", "Ask the office first."),
     ("Thank the bus drivers", "Write notes or draw pictures for the bus drivers.", "Hand them out at dismissal."),
     ("Pick up litter", "Spend 10 minutes picking up litter on the playground (with gloves).", "Count and graph it for math."),
     ("Kindness bookmarks", "Make bookmarks with kind messages for the school library.", "Ask the librarian to tuck them in books."),
     ("Partner praise", "Tell your partner one thing they did well this week.", "Use 'I noticed…' sentences."),
     ("Cards for hospitals", "Make cheerful cards for a children's hospital.", "Check the hospital's card guidelines."),
     ("Kindness pledge", "Write one way you will keep being kind over the break.", "Display the pledges on the door."),
     ("Kindness party", "Celebrate 24 days of kindness with a class party and certificates.", "Hand out the Kindness Champion awards.")]


def card(n, t, d, tip):
    return f'<div class="kc"><div class="d">{n}</div><b>{t}</b><p>{d}</p><div class="tip">Teacher tip: {tip}</div></div>'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("heart",110,"#c0392b",1.2)}</div><div class="eyebrow">For teachers · December 1–24 · Grades K–5</div>'
          f'<h1>Classroom<br>Kindness Calendar</h1><div class="tg">24 whole-class kindness missions with teacher tips, a printable wall calendar, a class tracker, student certificates and a letter for families. No elf needed.</div>'
          f'<div class="pill">11 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to run your kindness calendar", "book")}
<p class="subtitle">A December routine that takes five minutes in the morning meeting and fills the classroom with good feelings, not more sugar.</p>
<div class="step"><div class="num">1</div><div><b>Hang the wall calendar</b><p>Print the poster pages and display them by the door. Students color a square each day.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Reveal one mission a day</b><p>Read the mission card at morning meeting. Most missions take 5–20 minutes and need no shopping.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Track and celebrate</b><p>Use the class tracker to tick each finished mission. On the last day, hand out the Kindness Champion certificates.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Bring families in</b><p>Send the family letter home on day one so parents can talk about the missions at dinner.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Swap freely</h3><div class="mini">School days, not calendar days: skip weekends and swap missions to fit your schedule.</div></div>
<div class="card warm col"><h3>Check first</h3><div class="mini">For deliveries outside school (seniors, hospitals, shelters) check guidelines and permissions first.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    for i in range(0, 24, 6):
        pg.append(f'<div class="page">{page_head("Mission cards · cut along the dashed lines", f"Missions {i+1}–{i+6}", "star")}<div class="grid">{"".join(card(i+j+1, *K[i+j]) for j in range(6))}</div>{footer(NAME, f"Missions {i+1}–{i+6}")}</div>')
    po = "".join(f"<div><b>{n+1}</b>{K[n][0]}</div>" for n in range(24))
    pg.append(f'<div class="page">{page_head("Wall poster · color a square each day", "Our class kindness calendar", "calendar")}<div class="poster">{po}</div>{footer(NAME, "Wall calendar")}</div>')
    rows = "".join(f"<tr><td>Mission {n+1}: {K[n][0]}</td><td></td><td></td></tr>" for n in range(12))
    rows2 = "".join(f"<tr><td>Mission {n+1}: {K[n][0]}</td><td></td><td></td></tr>" for n in range(12, 24))
    for part, rr in ((1, rows), (2, rows2)):
        pg.append(f'<div class="page">{page_head("Teacher page", f"Class kindness tracker ({part}/2)", "check")}<table class="track"><tr><th>Mission</th><th>Done ✓</th><th>Who helped / notes</th></tr>{rr}</table>{footer(NAME, "Tracker")}</div>')
    cert = '<div>{0}<h2>Kindness Champion</h2><p>This award goes to</p><div class="ln"></div><p>for making our classroom kinder this December.</p><p style="font-size:10pt">Teacher: _______________ &nbsp; Date: _________</p></div>'.format(icon("star", 44, "#e0a526", 1.2))
    pg.append(f'<div class="page">{page_head("Cut in half", "Student certificates", "star")}<div class="certs">{cert}{cert}</div>{footer(NAME, "Certificates")}</div>')
    pg.append(f"""<div class="page">{page_head("Send home on day one", "Letter for families", "heart")}<div class="letter">
<p>Dear families,</p>
<p>This December our class is counting down to the winter break with a <b>Kindness Calendar</b>. Every school day we will complete one small kindness mission together: thanking school helpers, including classmates, making cards for our community and more.</p>
<p>You can help at home by asking your child, "What was today's kindness mission?" and by talking about the kind things you notice in your family.</p>
<p>A few missions may ask for donated items such as old towels for an animal shelter. We will always send a note home first, and joining in is completely optional.</p>
<p>Thank you for helping us grow kind hearts this season!</p>
<p style="margin-top:28px">Warmly,<br>______________________ (teacher)</p></div>{footer(NAME, "For single-classroom use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
