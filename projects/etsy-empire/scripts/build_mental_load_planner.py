#!/usr/bin/env python3
"""Mental Load Reset Planner – nyomtatható kísérő a „Who Takes Care of Mom?” könyvhöz (Gentle Life Guides, Etsy-csatorna, C) feladat, 2026-11-27).
Saját munkalapok (nem a könyv szövege → KDP Select rendben). → termekek/mental-load-reset-planner/"""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "mental-load-reset-planner"
NAME = "Mental Load Reset Planner"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """:root{ --dark:#4a3b52; --sage:#b0607a; --tint:#f9eef2; --line:#ecd3dc; --accent:#d9a441; --warm:#f3f0f6; --warmline:#ddd5e6; --cream:#fdf9fa; }
.cv{ background:linear-gradient(180deg,#fdf9fa,#f3eaf1); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.ln{ border-bottom:1.5px solid var(--line); height:.34in; }
.box{ border:2px solid var(--line); border-radius:14px; padding:10px 14px; background:#fff; margin-bottom:10px; } .box h3{ margin:0 0 4px; color:var(--sage); font-size:12.5pt; }
table.inv{ width:100%; border-collapse:collapse; font-size:9.6pt; margin-bottom:.1in; } table.inv th{ background:var(--tint); color:var(--dark); }
table.inv td, table.inv th{ border:1.2px solid var(--line); height:.3in; padding:2px 6px; text-align:left; } table.inv td.c{ text-align:center; width:.55in; }
.two{ display:grid; grid-template-columns:1fr 1fr; gap:12px; } .say{ background:var(--warm); border-left:4px solid var(--sage); border-radius:8px; padding:8px 12px; margin:6px 0; font-size:11pt; font-style:italic; }
.days{ display:grid; grid-template-columns:1fr; gap:8px; flex:1; margin-bottom:.1in; } .dy{ border:1.5px solid var(--line); border-radius:12px; padding:6px 12px; display:grid; grid-template-columns:1.1in 1fr; gap:6px; align-items:center; }
.dy b{ color:var(--sage); } .tick{ display:flex; gap:8px; align-items:center; font-size:11pt; margin:5px 0; } .tick span{ width:15px; height:15px; border:2px solid var(--dark); border-radius:4px; flex:0 0 auto; }"""

TASKS = {
    "Kids": ["School forms and permission slips", "Doctor and dentist appointments", "Birthday gifts and parties", "Clothes that no longer fit", "Activities, sign-ups, schedules", "Homework and reading", "Bedtime routine"],
    "Home": ["Meal planning", "Grocery list and shopping", "Cooking dinner", "Laundry start to finish", "Noticing what needs cleaning", "Running out of toilet paper, soap, etc.", "Repairs and appointments"],
    "Family life": ["Family calendar", "Holidays and gifts", "Remembering relatives' birthdays", "Planning weekends", "Pet care and vet visits", "Bills and paperwork", "Saying thank you, sending cards"],
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    L = lambda n: "".join('<div class="ln"></div>' for _ in range(n))
    pg = [f'<div class="page cv"><div>{icon("heart",110,"#b0607a",1.2)}</div><div class="eyebrow">Printable planner · For couples and families</div>'
          f'<h1>Mental Load<br>Reset Planner</h1><div class="tg">See every invisible task on paper, share it fairly, and plan one calm conversation about it. Worksheets for a fairer week at home.</div>'
          f'<div class="pill">9 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to use your planner", "book")}
<p class="subtitle">The mental load is the noticing, remembering and planning that keeps a family running. It is real work, even when nobody sees it. This planner makes it visible, so it can be shared.</p>
<div class="step"><div class="num">1</div><div><b>Write it all down</b><p>Use the task inventory to list everything that lives in your head. Add what's missing for your family.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Mark who does what</b><p>For each task: who notices, who plans, who does it. Most couples are surprised by the "notices" column.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Talk once, calmly</b><p>Use the conversation page to prepare. Pick a quiet time, not the middle of a busy evening.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Hand over whole tasks</b><p>Not "help me with", but "this is yours, from noticing to finishing". Then try the 7-day reset.</p></div></div>
{footer(NAME, "Start here")}</div>""")
    for area, tasks in TASKS.items():
        rows = "".join(f"<tr><td>{t}</td><td class='c'></td><td class='c'></td><td class='c'></td></tr>" for t in tasks) + "".join("<tr><td></td><td class='c'></td><td class='c'></td><td class='c'></td></tr>" for _ in range(5))
        pg.append(f'<div class="page">{page_head("Task inventory", f"{area}: who notices, plans, does?", "check")}<p class="subtitle">Write initials in each column. Add your own tasks in the empty rows.</p><table class="inv"><tr><th>Task</th><th>Notices</th><th>Plans</th><th>Does</th></tr>{rows}</table>{footer(NAME, "Inventory")}</div>')
    pg.append(f"""<div class="page">{page_head("What I see", "My invisible list", "star")}
<div class="two"><div class="box"><h3>Things I always remember</h3>{L(6)}</div><div class="box"><h3>Things that keep me up at night</h3>{L(6)}</div></div>
<div class="box"><h3>One thing I would love to never think about again</h3>{L(2)}</div><div class="box"><h3>What I need most right now</h3>{L(2)}</div>{footer(NAME, "My list")}</div>""")
    pg.append(f"""<div class="page">{page_head("Prepare", "The calm conversation", "heart")}
<div class="box"><h3>When and where</h3><div class="mini">A quiet time, no screens, not at bedtime: ______________________________</div></div>
<div class="box"><h3>Words you can use</h3><div class="say">"I want us to feel like a team. Can we look at this list together?"</div>
<div class="say">"I'm not asking for help. I'd like you to own a few of these, from start to finish."</div>
<div class="say">"Which three tasks would you like to take over completely?"</div></div>
<div class="box"><h3>What I want to ask for</h3>{L(3)}</div><div class="box"><h3>What we agreed</h3>{L(3)}</div>{footer(NAME, "Conversation")}</div>""")
    days = "".join(f'<div class="dy"><b>Day {d}</b><div><div class="tick"><span></span><em>{t}</em></div><div class="ln" style="height:.22in"></div></div></div>' for d, t in enumerate(
        ["Fill in the task inventory together", "Pick 3 tasks to hand over completely", "Write the handed-over tasks on the fridge", "Notice without fixing: let the new owner do it their way",
         "15 minutes just for me", "Weekly planning together (10 minutes)", "Look back: what felt lighter?"], 1))
    pg.append(f'<div class="page">{page_head("One small step a day", "7-day reset", "calendar")}<div class="days">{days}</div>{footer(NAME, "7 days")}</div>')
    pg.append(f"""<div class="page">{page_head("Every Sunday", "Weekly family check-in", "check")}
<div class="two"><div class="box"><h3>This week's appointments</h3>{L(5)}</div><div class="box"><h3>Who owns what this week</h3>{L(5)}</div></div>
<div class="box"><h3>What went well</h3>{L(2)}</div><div class="box"><h3>What we change next week</h3>{L(2)}</div>
<div class="card warm" style="margin-bottom:.15in"><h3>Want the whole story?</h3><div class="mini">This planner is a companion to <b>Who Takes Care of Mom?</b> by Clara Whitfield (Gentle Life Guides), a gentle guide to the invisible load. Available on Amazon.</div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
