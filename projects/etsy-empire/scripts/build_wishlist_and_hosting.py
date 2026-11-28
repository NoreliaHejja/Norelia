#!/usr/bin/env python3
"""Két printable (termekotletek A7 + A6), 2026-11-28:
  kids-christmas-wish-list: gyerek kívánságlista levél a Mikulásnak (3 korosztály-változat) + rajzolós lista + 12 köszönőkártya (töltsd ki / rajzold le)
  christmas-hosting-planner: karácsonyi vacsora- és vendéglátás-tervező: visszaszámláló teendők, menü, bevásárlólista, vendéglista/ültetés, időbeosztás a nagy napra, ajándéklista, költségvetés
  python3 scripts/build_wishlist_and_hosting.py [wish|host]"""
import sys
from pathlib import Path
from common import page_head, icon, footer

ROOT = Path(__file__).resolve().parent.parent / "termekek"


def html(name, css, pages, lang="en"):
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>{name}</title><link rel="stylesheet" href="../../assets/base.css"><style>{css}</style></head><body>{"".join(pages)}</body></html>'


def wish():
    slug, name = "kids-christmas-wish-list", "Kids Christmas Wish List and Thank You Notes"
    css = """:root{ --dark:#1f4d3a; --sage:#b8322a; --tint:#fdf1ee; --line:#efd2c6; --accent:#d9a441; --warm:#eef6ef; --warmline:#cfe3d2; --cream:#fffaf3; }
.cv{ background:linear-gradient(180deg,#fffaf3,#fdeee6); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:38pt; color:var(--sage); margin:10px 0 6px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; }
.cv .pill{ margin-top:18px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.letter{ border:3px double var(--sage); border-radius:18px; padding:18px 24px; background:#fff; flex:1; margin-bottom:.15in; display:flex; flex-direction:column; }
.letter h2{ color:var(--sage); text-align:center; font-size:24pt; margin:0 0 8px; } .ln{ border-bottom:1.6px solid var(--line); height:.42in; font-size:12pt; color:#999; padding-top:.12in; }
.big .ln{ height:.55in; } .wish{ display:grid; grid-template-columns:repeat(3,1fr); gap:10px; flex:1; margin:8px 0; } .wish div{ border:2px dashed var(--line); border-radius:12px; display:flex; align-items:flex-end; justify-content:center; padding:6px; font-size:10pt; color:#999; }
.cards{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:repeat(3,1fr); gap:12px; flex:1; margin-bottom:.12in; }
.card2{ border:1.5px dashed #999; border-radius:14px; padding:12px 14px; display:flex; flex-direction:column; gap:4px; background:#fff; } .card2 h3{ margin:0; color:var(--sage); font-size:14pt; text-align:center; }
.card2 .l{ border-bottom:1.3px solid var(--line); height:.26in; font-size:9.5pt; color:#999; } .card2 .d{ flex:1; border:1.5px dashed var(--line); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:9pt; color:#bbb; }"""
    pg = [f'<div class="page cv"><div>{icon("star",110,"#d9a441",1.2)}</div><div class="eyebrow">Printable · Ages 3 to 10 · Christmas</div><h1>My Christmas<br>Wish List</h1>'
          f'<div class="tg">Letters to Santa for little ones and big kids, a draw-your-wishes page and 12 thank-you notes for after Christmas.</div><div class="pill">8 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("For grown-ups", "How to use this set", "book")}
<div class="step"><div class="num">1</div><div><b>Pick the right letter</b><p>Ages 3–5: the picture letter (draw or glue wishes). Ages 5–7: the big-line letter. Ages 7–10: the full letter with a "kind thing I did this year" line.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Keep it calm</b><p>Ask for three wishes: something I want, something I need, something to share. It helps you shop and keeps the list short.</p></div></div>
<div class="step"><div class="num">3</div><div><b>After Christmas</b><p>Use the thank-you notes for grandparents, teachers and friends. Little kids can draw, older kids can write.</p></div></div>
{footer(name, "How to use")}</div>""")
    pg.append(f"""<div class="page"><div class="letter big"><h2>Dear Santa,</h2><div class="mini" style="text-align:center">Draw or glue in your 3 wishes</div>
<div class="wish"><div>something I want</div><div>something I need</div><div>something to share</div></div><div class="ln">My name is</div><div class="ln">I am ___ years old</div></div>{footer(name, "Ages 3–5")}</div>""")
    lines = "".join(f'<div class="ln">{x}</div>' for x in ["My name is", "I am ___ years old", "This year I was kind when", "Wish 1: something I want", "Wish 2: something I need", "Wish 3: something to share", "Love from"])
    pg.append(f'<div class="page"><div class="letter big"><h2>Dear Santa,</h2>{lines}</div>{footer(name, "Ages 5–7")}</div>')
    lines = "".join(f'<div class="ln">{x}</div>' for x in ["Hello Santa! My name is", "and I am ___ years old.", "The best thing that happened this year", "Something kind I did for someone", "I am getting better at", "Wish 1 (want)", "Wish 2 (need)", "Wish 3 (to share)", "A question for you", "Love,"])
    pg.append(f'<div class="page"><div class="letter">{"<h2>Dear Santa,</h2>"}{lines}</div>{footer(name, "Ages 7–10")}</div>')
    for k in range(2):
        cs = "".join(f'<div class="card2"><h3>Thank you!</h3><div class="l">Dear</div><div class="l">Thank you for</div><div class="d">draw it here</div><div class="l">Love,</div></div>' for _ in range(6))
        pg.append(f'<div class="page">{page_head("Cut along the dashed lines", f"Thank-you notes {k * 6 + 1}–{k * 6 + 6}", "heart")}<div class="cards">{cs}</div>{footer(name, "Thank you notes")}</div>')
    pg.append(f"""<div class="page">{page_head("For grown-ups", "Gift tracker", "check")}<table style="width:100%;border-collapse:collapse;font-size:10pt">
<tr><th style="background:var(--tint);border:1px solid var(--line);padding:4px">Child</th><th style="background:var(--tint);border:1px solid var(--line)">Want</th><th style="background:var(--tint);border:1px solid var(--line)">Need</th><th style="background:var(--tint);border:1px solid var(--line)">Share</th><th style="background:var(--tint);border:1px solid var(--line)">Bought ✓</th></tr>
{"".join("<tr>" + "".join('<td style="border:1px solid var(--line);height:.38in"></td>' for _ in range(5)) + "</tr>" for _ in range(14))}</table>
{footer(name, "For personal use only · © AureliaVenn")}</div>""")
    return slug, html(name, css, pg)


def host():
    slug, name = "christmas-hosting-planner", "Christmas Hosting Planner"
    css = """:root{ --dark:#3a2a22; --sage:#9c2f2b; --tint:#f8efe8; --line:#e6d3c4; --accent:#c9a04a; --warm:#f5f0e8; --warmline:#e3d8c8; --cream:#fcf9f4; }
.cv{ background:linear-gradient(180deg,#fcf9f4,#f3e7da); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:38pt; color:var(--sage); margin:10px 0 6px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; }
.cv .pill{ margin-top:18px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.ln{ border-bottom:1.5px solid var(--line); height:.32in; } .box{ border:2px solid var(--line); border-radius:12px; padding:9px 12px; background:#fff; margin-bottom:9px; } .box h3{ margin:0 0 3px; color:var(--sage); font-size:11.5pt; }
.two{ display:grid; grid-template-columns:1fr 1fr; gap:10px; } .tick{ display:flex; gap:8px; align-items:center; font-size:10.5pt; margin:4px 0; } .tick span{ width:14px; height:14px; border:2px solid var(--dark); border-radius:3px; flex:0 0 auto; }
table.t{ width:100%; border-collapse:collapse; font-size:9.6pt; } table.t th{ background:var(--tint); color:var(--dark); } table.t td, table.t th{ border:1.2px solid var(--line); height:.3in; padding:2px 6px; text-align:left; }"""
    L = lambda n: "".join('<div class="ln"></div>' for _ in range(n))
    T = lambda items: "".join(f'<div class="tick"><span></span><em>{x}</em></div>' for x in items)
    tbl = lambda heads, n: "<table class='t'><tr>" + "".join(f"<th>{h}</th>" for h in heads) + "</tr>" + "".join("<tr>" + "".join("<td></td>" for _ in heads) + "</tr>" for _ in range(n)) + "</table>"
    pg = [f'<div class="page cv"><div>{icon("star",110,"#c9a04a",1.2)}</div><div class="eyebrow">Printable planner · Christmas dinner & guests</div><h1>Christmas<br>Hosting Planner</h1>'
          f'<div class="tg">Host Christmas without the last-minute panic: countdown to-do list, menu and shopping list, guests and seating, a timeline for the big day, gifts and budget.</div><div class="pill">10 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "Your hosting plan at a glance", "book")}
<div class="box"><h3>Date and time</h3>{L(1)}</div><div class="box"><h3>Number of guests · kids · special diets</h3>{L(2)}</div>
<div class="box"><h3>What I want this Christmas to feel like</h3>{L(2)}</div><div class="box"><h3>What I can ask others to bring or do</h3>{L(3)}</div>{footer(name, "Overview")}</div>""")
    pg.append(f"""<div class="page">{page_head("Countdown", "To-do list by week", "calendar")}<div class="two">
<div class="box"><h3>3 weeks before</h3>{T(["Send invitations", "Ask about diets and allergies", "Plan the menu", "Order turkey or roast", "Check plates, chairs, glasses"])}{L(1)}</div>
<div class="box"><h3>2 weeks before</h3>{T(["Buy drinks and dry goods", "Plan the seating", "Wrap gifts", "Book help or delegate dishes", "Decorate"])}{L(1)}</div>
<div class="box"><h3>1 week before</h3>{T(["Clean guest areas", "Make freezer-friendly dishes", "Iron tablecloth and napkins", "Confirm guest numbers", "Plan the day's timeline"])}{L(1)}</div>
<div class="box"><h3>1–2 days before</h3>{T(["Buy fresh food", "Thaw the roast", "Set the table", "Chill drinks", "Prep vegetables and desserts"])}{L(1)}</div></div>{footer(name, "Countdown")}</div>""")
    pg.append(f"""<div class="page">{page_head("Menu", "What we're eating", "heart")}<div class="two">
<div class="box"><h3>Starters & snacks</h3>{L(4)}</div><div class="box"><h3>Main course</h3>{L(4)}</div><div class="box"><h3>Sides</h3>{L(4)}</div><div class="box"><h3>Desserts</h3>{L(4)}</div></div>
<div class="box"><h3>Drinks (with and without alcohol)</h3>{L(3)}</div>{footer(name, "Menu")}</div>""")
    pg.append(f'<div class="page">{page_head("Shopping", "Shopping list", "check")}{tbl(["Item", "Amount", "Shop", "✓"], 24)}{footer(name, "Shopping")}</div>')
    pg.append(f'<div class="page">{page_head("Guests", "Guest list and diets", "star")}{tbl(["Name", "Coming?", "Diet / allergy", "Bringing", "Gift"], 20)}{footer(name, "Guests")}</div>')
    seats = "".join(f'<div style="border:1.5px solid var(--line);border-radius:10px;height:.55in;padding:4px 8px;font-size:9pt;color:#999">Seat {i}</div>' for i in range(1, 15))
    pg.append(f"""<div class="page">{page_head("Seating", "Who sits where", "heart")}<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin:10px 0">{seats}</div>
<div style="border:3px solid var(--sage);border-radius:30px;height:1.1in;margin:6px 0 14px;display:flex;align-items:center;justify-content:center;color:var(--sage);font-weight:700">TABLE</div>
<div class="box"><h3>Kids' table / notes</h3>{L(4)}</div>{footer(name, "Seating")}</div>""")
    pg.append(f'<div class="page">{page_head("The big day", "Cooking and hosting timeline", "calendar")}{tbl(["Time", "What", "Oven / hob", "Who"], 20)}{footer(name, "Timeline")}</div>')
    pg.append(f'<div class="page">{page_head("Gifts", "Gift list", "star")}{tbl(["For", "Idea", "Budget", "Bought", "Wrapped"], 22)}{footer(name, "Gifts")}</div>')
    pg.append(f"""<div class="page">{page_head("Budget & after", "Budget and notes for next year", "check")}{tbl(["Category", "Planned", "Spent"], 9)}
<div class="box" style="margin-top:10px"><h3>What worked well this year</h3>{L(3)}</div><div class="box"><h3>Next year I will…</h3>{L(3)}</div>{footer(name, "For personal use only · © AureliaVenn")}</div>""")
    return slug, html(name, css, pg)


if __name__ == "__main__":
    for which in (sys.argv[1:] or ["wish", "host"]):
        slug, h = {"wish": wish, "host": host}[which]()
        (ROOT / slug).mkdir(parents=True, exist_ok=True); (ROOT / slug / f"{slug}.html").write_text(h, encoding="utf-8"); print("wrote", slug)
