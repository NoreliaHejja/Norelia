#!/usr/bin/env python3
"""Weekly Family Meal Planner + Grocery List → termekek/family-meal-planner/*.html"""
from pathlib import Path
from common import page_head, icon, footer, cover

SLUG = "family-meal-planner"
NAME = "Family Meal Planner"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """
.plan{ table-layout:fixed; } .plan tbody td{ height:1.02in; vertical-align:top; padding-top:6px; border-left:1px solid var(--line); }
.plan tbody td:first-child{ border-left:0; }
.plan tbody td:first-child{ font-weight:600; color:var(--dark); font-size:9pt; width:0.85in; vertical-align:middle; }
.aisles{ display:grid; grid-template-columns:1fr 1fr; gap:12px; flex:1; }
.aisle{ border:1px solid var(--line); border-radius:14px; padding:10px 14px; background:#fff; }
.aisle:nth-child(4n+2),.aisle:nth-child(4n+3){ background:var(--cream); }
.aisle h3{ margin:0 0 4px; font-size:10pt; color:var(--dark); display:flex; align-items:center; gap:7px; }
.aisle .ck{ font-size:8.5pt; padding:4px 0; }
.aisle .ck .l{ flex:1; border-bottom:1px solid var(--line); height:14px; }
.pick{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }
.pickcol{ border-radius:16px; padding:12px; text-align:center; border:1px solid var(--line); }
.pickcol h3{ margin:0 0 8px; font-size:10.5pt; color:var(--dark); }
.food{ display:flex; align-items:center; gap:10px; justify-content:flex-start; font-size:11pt; padding:13px 6px; border-bottom:1px dotted var(--line); }
.food .dot{ width:22px; height:22px; border:1.6px dashed var(--accent); border-radius:50%; flex:0 0 auto; }
.ideas{ columns:2; column-gap:22px; font-size:9.8pt; }
.idea{ break-inside:avoid; display:flex; gap:8px; align-items:flex-start; padding:12px 0; border-bottom:1px dotted var(--line); }
.idea b{ color:var(--dark); font-weight:600; }
.idea .tg{ font-size:7pt; letter-spacing:.1em; text-transform:uppercase; color:var(--sage); display:block; }
.prep .ck{ font-size:10pt; padding:12px 0; }
.pan .ck{ font-size:10pt; padding:10px 0; }
"""

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
AISLES = [("leaf", "Fruit & veggies", 9), ("fridge", "Dairy & eggs", 6), ("spoon", "Protein", 6), ("cart", "Pantry & grains", 8),
          ("star", "Freezer", 5), ("child", "Kids' snacks & lunchbox", 6), ("check", "Home & other", 5), ("book", "Don't forget", 5)]
IDEAS = [("Sheet-pan chicken & veggies", "one pan · 35 min"), ("Turkey taco bowls", "kid builds own"), ("Veggie pasta bake", "freezer-friendly"),
         ("Salmon, rice & peas", "25 min"), ("Bean & cheese quesadillas", "meatless"), ("Mini meatballs & tomato sauce", "batch cook"),
         ("Egg fried rice", "uses leftovers"), ("Lentil & carrot soup", "slow cooker"), ("Homemade pizza night", "kid tops own"),
         ("Chicken noodle soup", "cozy"), ("Breakfast for dinner", "pancakes & fruit"), ("Fish tacos & slaw", "20 min"),
         ("Baked potato bar", "toppings buffet"), ("Teriyaki tofu & broccoli", "meatless"), ("Turkey burgers & sweet potato", "grill or oven"),
         ("Pesto pasta with peas", "15 min"), ("Chili with beans", "big batch"), ("Hummus wrap night", "no cook"),
         ("Shepherd's pie", "make ahead"), ("Leftover remix night", "zero waste")]
PREP = ["Check the calendar: busy nights = quick meals", "Ask everyone for one wish meal", "Write the plan and the grocery list",
        "Wash & cut veggies for 3 days", "Cook a big batch of rice or pasta", "Portion snacks into grab-and-go boxes",
        "Prep overnight oats for 2 mornings", "Defrost Monday's protein", "Clear one fridge shelf for leftovers", "Pin the plan on the fridge"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [cover(NAME, "Plan a week of calm, wholesome family meals in 15 minutes – with a page where your little one picks the menu too.",
                "A printable kitchen planner", "8 pages · Weekly planner · Grocery list by aisle", "calendar")]
    pg.append(f"""<div class="page">{page_head("Start here", "Your 15-minute Sunday plan", "book")}
<p class="subtitle">Print the weekly plan and grocery list as many times as you like. Sit down for 15 minutes on Sunday, follow the prep list, and the weeknights take care of themselves.</p>
<div class="step"><div class="num">1</div><div><b>Look at the week</b><p>Mark sports, late meetings and busy evenings. Those nights get a 20-minute idea from the list.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Let your child pick</b><p>Use the Kids' Menu Picker: one veggie, one fruit, one favorite. Kids eat more of what they chose.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Fill the weekly plan</b><p>Breakfast, lunch, dinner and snacks. Repeat favorites – nobody needs seven new recipes a week.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Write one grocery list</b><p>Sorted by aisle, so the shop takes half the time.</p></div></div>
<div class="step"><div class="num">5</div><div><b>Prep once</b><p>Follow the Sunday Prep checklist. One hour on Sunday saves a lot of weeknight stress.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Printing tips</h3><div class="mini">US Letter and A4 PDFs included. Slip the weekly plan into a sheet protector and use a dry-erase marker to reuse it.</div></div>
<div class="card warm col"><h3>Good to know</h3><div class="mini">A planning tool for busy families, not nutrition or medical advice. Adjust portions and foods to your family's needs and allergies.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    rows = "".join(f"<tr><td>{d}</td><td></td><td></td><td></td><td></td></tr>" for d in DAYS)
    pg.append(f"""<div class="page">{page_head("Every week", "Weekly Meal Plan", "calendar")}
<div class="row" style="margin-bottom:10px"><div class="col"><span class="lbl">Week of</span><div class="wline" style="height:.26in"></div></div><div class="col"><span class="lbl">Busy nights</span><div class="wline" style="height:.26in"></div></div></div>
<table class="plan"><thead><tr><th>Day</th><th>Breakfast</th><th>Lunch</th><th>Dinner</th><th>Snack</th></tr></thead><tbody>{rows}</tbody></table>
{footer(NAME, "Weekly plan")}</div>""")
    ai = "".join(f'<div class="aisle"><h3>{icon(i,16)}{t}</h3>' + "".join('<div class="ck"><span class="chk"></span><span class="l"></span></div>' for _ in range(n)) + "</div>" for i, t, n in AISLES)
    pg.append(f"""<div class="page">{page_head("Shop once", "Grocery List by Aisle", "cart")}<div class="aisles">{ai}</div>{footer(NAME, "Grocery list")}</div>""")
    cols = [("Pick a veggie", ["carrot", "cucumber", "peas", "broccoli", "corn", "pepper", "tomato"], "var(--tint)"),
            ("Pick a fruit", ["apple", "banana", "berries", "grapes", "pear", "orange", "melon"], "var(--cream)"),
            ("Pick a favorite", ["pasta", "rice", "pancakes", "tacos", "soup", "pizza", "eggs"], "var(--warm)")]
    pc = "".join(f'<div class="pickcol" style="background:{bg}"><h3>{h}</h3>' + "".join(f'<div class="food"><span class="dot"></span>{x}</div>' for x in fs) + '<div class="food"><span class="dot"></span>__________</div></div>' for h, fs, bg in cols)
    pg.append(f"""<div class="page">{page_head("For little hands", "Kids' Menu Picker", "child")}
<p class="subtitle">Read the words together and let your child color one circle in each column. Write the picks into the weekly plan – and tell them it was their idea.</p>
<div class="pick">{pc}</div>
<div class="card warm" style="margin-top:auto"><h3>This week, {'{'}name{'}'} chose…</h3><div class="wline"></div><div class="wline"></div></div>
{footer(NAME, "Kids' menu picker")}</div>""".replace("{name}", "our little chef"))
    ide = "".join(f'<div class="idea"><span class="chk" style="margin-top:2px"></span><span><b>{t}</b><span class="tg">{tag}</span></span></div>' for t, tag in IDEAS)
    pg.append(f"""<div class="page">{page_head("When you're stuck", "20 Easy Family Dinners", "spoon")}
<p class="subtitle">Tick the ones your family loves. On a busy night, just pick the next tick.</p><div class="ideas">{ide}</div>{footer(NAME, "Dinner ideas")}</div>""")
    pr = "".join(f'<div class="ck"><span class="chk"></span>{x}</div>' for x in PREP)
    pg.append(f"""<div class="page">{page_head("One hour on Sunday", "Sunday Prep Checklist", "check")}
<div class="card prep">{pr}</div>
<div class="row" style="margin-top:14px"><div class="card col"><span class="lbl">Leftovers to use first</span><div class="wline"></div><div class="wline"></div></div>
<div class="card warm col"><span class="lbl">Next week I'd like to try</span><div class="wline"></div><div class="wline"></div></div></div>
{footer(NAME, "Sunday prep")}</div>""")
    pan = ["Rolled oats", "Rice", "Pasta", "Canned tomatoes", "Beans", "Lentils", "Olive oil", "Stock cubes", "Flour", "Eggs", "Frozen peas", "Frozen berries",
           "Peanut / sunflower butter", "Whole-grain bread", "Spices: cinnamon, paprika, cumin", "Honey or maple syrup"]
    ck = lambda xs: "".join(f'<div class="ck"><span class="chk"></span>{x}</div>' for x in xs)
    pg.append(f"""<div class="page">{page_head("Always on hand", "Pantry Staples Checklist", "fridge")}
<p class="subtitle">Keep these at home and you can always make a quick dinner. Tick what you have; circle what to buy.</p>
<div class="row"><div class="card col pan"><h3>Pantry</h3>{ck(pan[:8])}</div><div class="card col pan"><h3>Fridge &amp; freezer</h3>{ck(pan[8:])}</div></div>
<div class="card" style="margin-top:14px"><h3>Add your own staples</h3><div class="row"><div class="col"><div class="wline"></div><div class="wline"></div></div><div class="col"><div class="wline"></div><div class="wline"></div></div></div></div>
<div class="card warm" style="margin-top:auto"><h3>Our family's go-to meal</h3><div class="wline"></div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"{SLUG}.html")


if __name__ == "__main__":
    main()
