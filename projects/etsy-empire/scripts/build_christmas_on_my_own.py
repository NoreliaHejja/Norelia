#!/usr/bin/env python3
"""Christmas on My Own Planner – nyomtatható kísérő a „Still Lit” könyvhöz (Etsy-csatorna, C) feladat).
Új, saját munkalapok (nem a könyv szövege → KDP Select rendben). → termekek/christmas-on-my-own-planner/"""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "christmas-on-my-own-planner"
NAME = "Christmas on My Own Planner"
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

ADVENT = ["Light a candle and make a warm drink", "Put on one song you loved at 16", "Walk somewhere with lights", "Write down 3 things that went okay today",
          "Buy yourself one small treat, no reason needed", "Send a short message to someone you miss", "Watch a film you choose, with snacks",
          "Clean one small corner and enjoy it", "Make a playlist for Christmas Day", "Take a photo of something beautiful", "Cook one recipe you never tried",
          "Plan your Christmas Day breakfast", "Say no to one thing you don't want to do", "Donate something or leave a kind note",
          "Call or video-call someone for 10 minutes", "Take a long bath or shower with music", "Write a card to yourself for next year",
          "Visit a market, a church concert or a library event", "Go to bed early with a book", "Put fresh flowers or greenery on the table",
          "Prepare your 'hard moment' kit", "Choose your Christmas Day outfit, just for you", "Get everything ready for a lazy tomorrow",
          "Christmas Eve: do the one thing that feels most like you"]
COMFORT = ["A walk at sunrise or sunset", "My favorite film or series", "A warm meal I cook just for me", "A long phone call",
           "Journaling for 10 minutes", "Music loud, dancing in the kitchen", "A puzzle, a craft or a book", "Volunteering for a few hours"]
SCRIPTS = [("When someone asks \"Are you still single?\"", "\"Yes, and my life is full right now. How are you doing?\""),
           ("When you want to say no to an invitation", "\"Thank you so much for thinking of me. This year I'm keeping it quiet, but I'd love to see you in January.\""),
           ("When you want to say yes, on your terms", "\"I'd love to come for dessert. I'll head home around nine.\""),
           ("When you want to reach out", "\"I'm spending Christmas quietly this year. Would you like to video-call on the 25th for a cup of tea?\"")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#d9a441",1.2)}</div><div class="eyebrow">Printable planner · For anyone spending the holidays alone</div>'
          f'<h1>Christmas<br>on My Own</h1><div class="tg">A gentle, practical plan for a quiet Christmas that feels like yours: a December of small comforts, a Christmas Day plan, words for the family questions and a plan for the hard moments.</div>'
          f'<div class="pill">10 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to use your planner", "book")}
<p class="subtitle">Spending the holidays alone can feel heavy, or it can feel free, and often it is both. This planner gives the season a shape, so the hardest days don't arrive unprepared.</p>
<div class="step"><div class="num">1</div><div><b>Decide what you want</b><p>Start with "My December, my way". You choose what stays, what goes and what is new this year.</p></div></div>
<div class="step"><div class="num">2</div><div><b>One small comfort a day</b><p>The 24-day comfort calendar gives each December day one small, kind thing to do for yourself. Tick it off or swap it.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Plan Christmas Day</b><p>An empty day feels longest. Give it a few anchors: a breakfast, a walk, a call, a film, a meal.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Prepare for the hard moments</b><p>Fill in your plan and your people list on a good day, so it's ready on a hard one.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>This is a plan, not a test</h3><div class="mini">If a day doesn't go as planned, that's fine. Tomorrow is a new page.</div></div>
<div class="card warm col"><h3>You are not the only one</h3><div class="mini">Many people spend the holidays alone, by choice or not. Nothing is wrong with you.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    pg.append(f"""<div class="page">{page_head("Your season, your rules", "My December, my way", "heart")}
<div class="two"><div class="box"><h3>Traditions I want to keep</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>Things I'm letting go of this year</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="two"><div class="box"><h3>One new thing I want to try</h3><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>My holiday budget</h3><div class="ln"></div><div class="ln"></div></div></div>
<div class="box"><h3>How I want to feel on December 31</h3><div class="ln"></div><div class="ln"></div></div>
{footer(NAME, "My December")}</div>""")
    for i in (0, 12):
        cells = "".join(f"<div><b>{d + 1}</b>{ADVENT[d]}</div>" for d in range(i, i + 12))
        pg.append(f'<div class="page">{page_head("One small comfort a day", f"Comfort calendar · December {i + 1}–{i + 12}", "calendar")}<div class="cal">{cells}</div>{footer(NAME, "Comfort calendar")}</div>')
    slots = "".join(f'<div class="slot"><i>{t}</i><u></u></div>' for t in ["Wake up", "Breakfast", "Morning", "Get outside", "Lunch", "Afternoon", "Call / message", "Dinner", "Evening", "Before bed"])
    pg.append(f"""<div class="page">{page_head("Give the day a shape", "My Christmas Day plan", "star")}
<p class="subtitle">Fill in a few anchors, not every hour. Leave room for rest.</p>
<div class="box">{slots}</div>
<div class="box"><h3>One thing that will make the day feel special</h3><div class="ln"></div></div>
{footer(NAME, "Christmas Day")}</div>""")
    sc = "".join(f'<div class="box"><h3>{q}</h3><div class="quote">{a}</div><div class="mini">My version:</div><div class="ln"></div></div>' for q, a in SCRIPTS)
    pg.append(f'<div class="page">{page_head("Words ready before you need them", "What to say", "book")}{sc}{footer(NAME, "What to say")}</div>')
    comf = "".join(f'<div class="tick"><span></span><em>{x}</em></div>' for x in COMFORT)
    pg.append(f"""<div class="page">{page_head("Fill this in on a good day", "My plan for the hard moments", "heart")}
<div class="box"><h3>Early signs that a hard moment is coming</h3><div class="ln"></div><div class="ln"></div></div>
<div class="two"><div class="box"><h3>My comfort menu (tick yours)</h3>{comf}<div class="ln"></div></div>
<div class="box"><h3>People I can reach</h3><div class="mini">Name · how · when</div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="card warm" style="margin-bottom:.15in"><h3>If it gets too heavy</h3><div class="mini">You don't have to carry it alone. In the US call or text <b>988</b>; in the UK and Ireland call Samaritans on <b>116 123</b>; elsewhere call your local emergency number or a crisis line. If you are in danger, call emergency services now.</div></div>
{footer(NAME, "Hard moments")}</div>""")
    pg.append(f"""<div class="page">{page_head("A gentle look back", "My season, in review", "check")}
<div class="two"><div class="box"><h3>What went better than I feared</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>What I'll do differently next year</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>
<div class="box"><h3>Three good moments from this December</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="box"><h3>A note to myself for next December</h3><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
{footer(NAME, "Review")}</div>""")
    pg.append(f"""<div class="page">{page_head("Extra pages", "Notes and lists", "book")}
<div class="two"><div class="box"><h3>Gifts I'm giving (or not)</h3>{''.join('<div class="ln"></div>' for _ in range(8))}</div>
<div class="box"><h3>Cards and messages to send</h3>{''.join('<div class="ln"></div>' for _ in range(8))}</div></div>
<div class="card warm" style="margin-bottom:.15in"><h3>Want the whole guide?</h3><div class="mini">This planner is a companion to the book <b>Still Lit</b> by Clara Whitfield (Gentle Life Guides): a gentle, practical guide for women who feel alone at Christmas. Available on Amazon. The planner works on its own too.</div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
