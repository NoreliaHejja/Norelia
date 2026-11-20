#!/usr/bin/env python3
"""Screen-Free Winter Break Planner – nyomtatható kísérő a „Give Them Back Their Wonder” könyvhöz (Etsy-csatorna, C) feladat).
Új, saját munkalapok (nem a könyv szövege → KDP Select-kizárólagosság nem sérül). → termekek/screen-free-break-planner/"""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "screen-free-break-planner"
NAME = "Screen-Free Break Planner"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """:root{ --dark:#2f5d6b; --sage:#d9573b; --tint:#fbefe9; --line:#ecd3c8; --accent:#e0a526; --warm:#eaf2f3; --warmline:#c9dde1; --cream:#fdf8f3; }
.cv{ background:linear-gradient(180deg,#fdf8f3,#eaf2f3); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.ln{ border-bottom:1.5px solid var(--line); height:.36in; }
.box{ border:2px solid var(--line); border-radius:14px; padding:12px 14px; background:#fff; margin-bottom:12px; }
.box h3{ margin:0 0 6px; color:var(--sage); font-size:13pt; }
.tick{ display:flex; gap:8px; align-items:center; font-size:12pt; margin:6px 0; } .tick em{ font-style:normal; flex:1; min-width:0; } .tick span{ width:16px; height:16px; border:2px solid var(--dark); border-radius:4px; flex:0 0 auto; }
.sig{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:auto; margin-bottom:.15in; } .sig div{ border-top:2px solid var(--dark); padding-top:4px; font-size:9.5pt; color:var(--dark); }
.days{ display:grid; grid-template-columns:repeat(2,1fr); gap:10px; flex:1; margin-bottom:.1in; }
.day{ border:1.5px solid var(--line); border-radius:12px; padding:8px 10px; background:#fff; font-size:10pt; }
.day b{ color:var(--sage); font-size:12pt; } .day .r{ display:grid; grid-template-columns:auto 1fr; gap:2px 8px; margin-top:4px; } .day .r i{ color:var(--dark); font-style:normal; font-weight:600; } .day .r u{ text-decoration:none; border-bottom:1px solid var(--line); }
.slips{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; flex:1; margin-bottom:.1in; }
.slips div{ border:1.5px dashed var(--sage); border-radius:10px; padding:8px; font-size:10.6pt; line-height:1.3; display:flex; align-items:center; justify-content:center; text-align:center; background:#fff; }
.slips div:nth-child(odd){ border-color:var(--dark); }
.cd{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:12px; }
.cd div{ border:2px dashed var(--dark); border-radius:14px; text-align:center; padding:14px 6px; } .cd b{ display:block; font-size:30pt; color:var(--sage); } .cd span{ font-size:10.5pt; }
.two{ display:grid; grid-template-columns:1fr 1fr; gap:12px; flex:1; margin-bottom:.1in; }
"""

SLIPS = ["Build a blanket fort and read inside it", "Draw a map of our street", "Make a paper airplane contest", "Bake something with 4 ingredients",
         "Start a family band with pots and spoons", "Write a letter to a grandparent", "Invent a new board game", "Do a puzzle together",
         "Go on a winter walk and count birds", "Put on a puppet show with socks", "Make a bird feeder from a pine cone", "Play hide and seek",
         "Build a marble run from paper rolls", "Learn three card tricks", "Make a time capsule for next year", "Have an indoor picnic",
         "Design a comic strip about the dog or cat", "Play charades", "Make paper snowflakes", "Have a dance party: 3 songs",
         "Make salt dough ornaments", "Build the tallest tower you can", "Sort old toys to donate", "Write a story with one word each",
         "Cook dinner with a grown-up", "Do a scavenger hunt in the house", "Make a thank-you card for a neighbor", "Play I spy in the dark with a flashlight",
         "Try a new card game", "Make a nature collage", "Practice a magic show", "Plant seeds in a cup"]
AGREE = ["Screens stay out of bedrooms at night", "No screens at meals", "We give a 10-minute warning before screens go off",
         "Movie night is a family screen time", "Grown-ups put phones away at play time too", "We say 'I'm bored' and then pick from the jar"]
LAND = ["A snack at the table", "A puzzle waiting on the floor", "Music on, five minutes of dancing", "A walk around the block",
        "Drawing paper and new markers", "Read one picture book together"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#e0a526",1.2)}</div><div class="eyebrow">Printable planner · School break · Ages 3–12</div>'
          f'<h1>Screen-Free<br>Winter Break</h1><div class="tg">A calm, printable plan for fewer screens and more laughing: family agreement, 14-day rhythm, boredom jar slips and screen-off countdown cards.</div>'
          f'<div class="pill">9 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to use your planner", "book")}
<p class="subtitle">Screens are not the enemy. Long, empty days are. This planner gives the break a shape so that screens become one part of the day, not the whole day.</p>
<div class="step"><div class="num">1</div><div><b>Fill in the agreement together</b><p>Before the first day off, sit down with the kids and agree on a few simple rules. Kids follow rules they helped make.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Plan your rhythm</b><p>Use the 14-day planner: one outdoor time, one quiet time and one "together" activity per day. Leave space for nothing at all.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Fill the boredom jar</b><p>Cut out the 32 slips and add your own. "I'm bored" now has an answer that is not a screen.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Use the countdown cards</b><p>Show the 10-5-1 cards before screens go off and have a landing activity ready. Fewer meltdowns, promise.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>First days are bumpy</h3><div class="mini">Many families notice the first two or three days are the hardest. Keep going: it usually gets easier.</div></div>
<div class="card warm col"><h3>Be kind to yourself</h3><div class="mini">A movie on a hard afternoon is not a failure. This is a plan, not a test.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    rules = "".join(f'<div class="tick"><span></span><em>{r}</em></div>' for r in AGREE)
    pg.append(f"""<div class="page">{page_head("Make it together", "Our family break agreement", "heart")}
<div class="box"><h3>Our goals for this break</h3><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Our screen rules (tick or add your own)</h3>{rules}<div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Screen time on a normal break day</h3><div class="mini">When: ____________________ &nbsp; How long: ______________ &nbsp; Where: ____________________</div></div>
<div class="box"><h3>If we forget the rules, we will…</h3><div class="ln"></div></div>
<div class="sig"><div>Signed</div><div>Signed</div><div>Signed</div></div>{footer(NAME, "Agreement")}</div>""")
    for start in (1, 8):
        ds = "".join(f'<div class="day"><b>Day {d}</b> &nbsp;<span style="color:#888">date ______</span><div class="r"><i>Outside</i><u></u><i>Quiet</i><u></u><i>Together</i><u></u><i>Screens</i><u></u></div></div>' for d in range(start, start + 7))
        ds += '<div class="day"><b>Notes</b><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>'
        pg.append(f'<div class="page">{page_head("One small plan a day", f"Break rhythm · days {start}–{start+6}", "calendar")}<div class="days">{ds}</div>{footer(NAME, "Planner")}</div>')
    for i in (0, 16):
        s = "".join(f"<div>{x}</div>" for x in SLIPS[i:i + 16])
        pg.append(f'<div class="page">{page_head("Cut, fold, put in a jar", "Boredom jar slips", "star")}<div class="slips">{s}</div>{footer(NAME, "Jar slips")}</div>')
    land = "".join(f'<div class="tick"><span></span><em>{x}</em></div>' for x in LAND)
    pg.append(f"""<div class="page">{page_head("When the screen goes off", "Countdown cards + landing activities", "check")}
<div class="cd"><div><b>10</b><span>minutes left.<br>Find a good stopping point.</span></div><div><b>5</b><span>minutes left.<br>Save your game.</span></div><div><b>1</b><span>minute left.<br>Time to land!</span></div></div>
<div class="two"><div class="box"><h3>Our landing activities</h3>{land}<div class="ln"></div></div>
<div class="box"><h3>Good screen time we enjoy together</h3><div class="mini">Movie night, video calls with family, making something (stop-motion, music), learning about something we love.</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
{footer(NAME, "Countdown")}</div>""")
    pg.append(f"""<div class="page">{page_head("End of the break", "What changed?", "heart")}
<div class="two"><div class="box"><h3>Before the break</h3><div class="mini">How did evenings feel? How did the kids play?</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>After the break</h3><div class="mini">What felt different? What do we want to keep?</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="box"><h3>Our favorite memory from this break</h3><div class="ln"></div><div class="ln"></div></div>
<div class="card warm" style="margin-bottom:.15in"><h3>Want the whole story?</h3><div class="mini">This planner is a companion to the book <b>Give Them Back Their Wonder</b> by Clara Whitfield (Gentle Life Guides), with 100 screen-free games and a full guide for the break. Available on Amazon.</div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
