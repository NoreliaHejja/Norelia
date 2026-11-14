#!/usr/bin/env python3
"""Morning & Bedtime Routine Cards (preschool) → termekek/routine-cards/*.html"""
from pathlib import Path
from common import page_head, icon, footer, cover

SLUG = "routine-cards"
NAME = "Morning & Bedtime Routine"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MORNING = [("sun", "Wake up & smile"), ("potty", "Potty & wash hands"), ("shirt", "Get dressed"), ("bowl", "Eat breakfast"),
           ("tooth", "Brush teeth"), ("heart", "Hair & face"), ("shoe", "Shoes & jacket on"), ("hug", "Hug & go!")]
BEDTIME = [("toy", "Tidy up toys"), ("bath", "Bath time"), ("shirt", "Pajamas on"), ("tooth", "Brush teeth"),
           ("potty", "Potty & wash hands"), ("book", "Story time"), ("hug", "Hugs & kisses"), ("moon", "Lights out")]
EXTRA = [("leaf", "Water the plants"), ("cat", "Feed the cat"), ("spoon", "Help set the table"), ("star", "Quiet play"),
         ("calendar", "Look at today's plan"), ("heart", "Say something kind"), ("check", "Pack my bag"), ("child", "Get ready for preschool")]

CSS = """
.rt{ table-layout:fixed; } .rt tbody td{ height:0.98in; text-align:center; } .rt th{ text-align:center; } .rt th:first-child{ text-align:left; width:2.55in; }
.rt tbody td:first-child{ text-align:left; }
.task{ display:flex; align-items:center; gap:10px; font-size:10.5pt; font-weight:600; color:var(--dark); }
.task .ic{ width:40px; height:40px; border-radius:50%; background:var(--tint); display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.dot{ width:0.38in; height:0.38in; border:1.6px dashed var(--sage); border-radius:50%; display:inline-block; }
.cards{ display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(4,1fr); gap:0; flex:1; border:1.5px dashed var(--line); }
.cc{ border:1px dashed var(--line); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px; padding:10px; text-align:center; }
.cc .big{ width:1.15in; height:1.15in; border-radius:50%; background:var(--tint); display:flex; align-items:center; justify-content:center; }
.cc.n .big{ background:var(--warm); }
.cc b{ font-size:12pt; color:var(--dark); }
.stars{ display:grid; grid-template-columns:repeat(7,1fr); gap:10px; }
.stars div{ display:flex; flex-direction:column; align-items:center; font-size:8pt; color:var(--soft); line-height:1; }
.star{ width:0.72in; height:0.72in; margin:0 auto 4px; }
.tips .ck{ font-size:10.4pt; padding:13px 0; }
.cert{ border:2px dashed var(--accent); border-radius:18px; padding:22px; text-align:center; margin-top:14px; background:var(--cream); }
.cert h2{ margin:4px 0; color:var(--dark); font-size:20pt; }
"""
STAR = '<svg class="star" viewBox="0 0 24 24" fill="none" stroke="#e0a458" stroke-width="1.2" stroke-dasharray="2 1.6" stroke-linejoin="round"><path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/></svg>'


def chart(eyebrow, title, ic, rows, night=False):
    body = "".join(f'<tr><td><div class="task"><span class="ic">{icon(i,22)}</span>{t}</div></td>' + "".join('<td><span class="dot"></span></td>' for _ in DAYS) + "</tr>" for i, t in rows)
    return (f'<div class="page">{page_head(eyebrow, title, ic)}'
            f'<div class="row" style="margin-bottom:8px"><div class="col"><span class="lbl">Name</span><div class="wline" style="height:.26in"></div></div><div class="col"><span class="lbl">Week of</span><div class="wline" style="height:.26in"></div></div></div>'
            f'<table class="rt"><thead><tr><th>{"Tonight I…" if night else "This morning I…"}</th>' + "".join(f"<th>{d}</th>" for d in DAYS) + f'</tr></thead><tbody>{body}</tbody></table>'
            f'{footer(NAME, title)}</div>')


def cards(title, items, night=False):
    cs = "".join(f'<div class="cc{" n" if night else ""}"><span class="big">{icon(i,60,sw=1.3)}</span><b>{t}</b></div>' for i, t in items)
    return f'<div class="page" style="padding-bottom:0.75in">{page_head("Cut along the dashed lines", title, "check")}<div class="cards">{cs}</div>{footer(NAME, title)}</div>'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [cover("Morning &amp; Bedtime Routine", "Picture cards and charts that turn \"hurry up!\" into \"I did it!\" – for little ones ages 3–6.",
                "A printable routine kit", "8 pages · 2 charts · 24 cut-out cards · Ages 3–6", "sun")]
    pg.append(f"""<div class="page">{page_head("Start here", "How to use the routine kit", "book")}
<p class="subtitle">Pre-readers follow pictures, not words. Put the chart where the routine happens – the bathroom door, the bedroom wall – and let your child color a dot for every step.</p>
<div class="step"><div class="num">1</div><div><b>Pick the chart</b><p>Morning and bedtime charts with 8 steps each. Print a new one every week, or use a sheet protector.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Or build your own strip</b><p>Cut out the picture cards and stick them in order with tape or velcro dots. Swap cards as your routine changes.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Do it together for a week</b><p>Point at the next card instead of giving the next instruction. Less talking, fewer power struggles.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Celebrate</b><p>Color a star on the reward chart for each finished routine. Seven stars? Time for a small family treat.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Printing tips</h3><div class="mini">US Letter and A4 PDFs included. Print the cards on card stock and laminate them for a routine that survives toddler hands.</div></div>
<div class="card warm col"><h3>Good to know</h3><div class="mini">Every child is different. Use the steps that fit your family and skip the rest – this is a gentle planning tool, not parenting advice.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    pg.append(chart("Every morning", "Morning Routine Chart", "sun", MORNING))
    pg.append(chart("Every evening", "Bedtime Routine Chart", "moon", BEDTIME, night=True))
    pg.append(cards("Morning Picture Cards", MORNING + EXTRA[:4]))
    pg.append(cards("Bedtime Picture Cards", BEDTIME + EXTRA[4:6] + [("bowl", "Healthy snack"), ("heart", "Calm breathing")], night=True))
    st = "".join(f"<div>{STAR}{d}</div>" for d in DAYS)
    pg.append(f"""<div class="page">{page_head("Collect the stars", "I Did It! Reward Chart", "star")}
<p class="subtitle">Color one star for each routine your child finished. Two weeks, morning and bedtime.</p>
<div class="card" style="margin-bottom:12px"><h3>{icon('sun',16)} Week 1 · Morning</h3><div class="stars">{st}</div></div>
<div class="card warm" style="margin-bottom:12px"><h3>{icon('moon',16)} Week 1 · Bedtime</h3><div class="stars">{st}</div></div>
<div class="card" style="margin-bottom:12px"><h3>{icon('sun',16)} Week 2 · Morning</h3><div class="stars">{st}</div></div>
<div class="card warm" style="margin-bottom:12px"><h3>{icon('moon',16)} Week 2 · Bedtime</h3><div class="stars">{st}</div></div>
<div class="row"><div class="card col"><span class="lbl">My reward for 7 stars</span><div class="wline"></div></div><div class="card col"><span class="lbl">My reward for 14 stars</span><div class="wline"></div></div></div>
{footer(NAME, "Reward chart")}</div>""")
    tips = ["Keep the same order every day – predictability is the magic.", "Give a 5-minute warning before routines start.",
            "Offer two small choices: \"red pajamas or blue?\"", "Praise the effort, not the speed.",
            "Lay out clothes the night before.", "Use a song or timer for teeth brushing (2 minutes).",
            "On hard days, do the routine together instead of skipping it."]
    tp = "".join(f'<div class="ck"><span class="chk"></span>{t}</div>' for t in tips)
    pg.append(f"""<div class="page">{page_head("For grown-ups", "Make It Stick", "heart")}
<div class="card tips">{tp}</div>
<div class="row" style="margin-top:14px"><div class="card col"><span class="lbl">Wake-up time</span><div class="wline"></div></div><div class="card col"><span class="lbl">Leave the house</span><div class="wline"></div></div><div class="card warm col"><span class="lbl">Lights out</span><div class="wline"></div></div></div>
<div class="cert" style="margin-top:auto"><div class="eyebrow">Certificate</div><h2>Routine Superstar</h2><div class="mini">awarded to</div><div class="wline" style="width:60%;margin:8px auto 4px"></div><div class="mini">for finishing a whole week of routines</div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME} Cards</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"{SLUG}.html")


if __name__ == "__main__":
    main()
