#!/usr/bin/env python3
"""Cook With Me – 20 Toddler Recipe Cards → termekek/cook-with-me-recipe-cards/*.html"""
from pathlib import Path
from common import page_head, icon, footer, cover, ICONS

SLUG = "cook-with-me-recipe-cards"
NAME = "Cook With Me"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

# (title, minutes, little chef jobs [(icon, text)], grown-up jobs, ingredients)
R = [
 ("Rainbow Fruit Skewers", 10, [("wash","Wash the fruit"),("count","Count 6 pieces"),("stack","Slide fruit on a stick")], "Cut fruit, use blunt sticks", ["strawberries","melon","kiwi","grapes, quartered","blueberries"]),
 ("Banana Oat Cookies", 25, [("mash","Mash 2 bananas"),("stir","Stir in the oats"),("shape","Roll little balls")], "Oven 350°F / 175°C, 12 min", ["2 ripe bananas","1 cup oats","a handful of raisins"]),
 ("Berry Yogurt Bark", 15, [("spread","Spread the yogurt"),("sprinkle","Sprinkle berries"),("wait","Wait for the freezer")], "Freeze 2 hours, break pieces", ["2 cups plain yogurt","1 tsp honey (1 yr+)","mixed berries"]),
 ("Veggie Face Toast", 10, [("spread","Spread the cream cheese"),("shape","Make eyes and a smile"),("count","Count the veggie pieces")], "Toast bread, slice veggies", ["whole-grain toast","cream cheese","cucumber, pepper, carrot"]),
 ("Mini Pita Pizzas", 20, [("spread","Spread the sauce"),("sprinkle","Sprinkle the cheese"),("shape","Add a veggie topping")], "Oven 400°F / 200°C, 8 min", ["mini pitas","tomato sauce","mozzarella","sweetcorn, spinach"]),
 ("Sunny Smoothie Bowl", 10, [("pour","Pour into the blender"),("press","Press the button with help"),("sprinkle","Add toppings")], "Blend, check temperature", ["1 frozen banana","1/2 cup mango","1/2 cup yogurt","oats, berries"]),
 ("Cucumber Sandwich Bites", 10, [("spread","Spread the butter"),("stack","Stack the layers"),("shape","Cut shapes with a cutter")], "Slice cucumber thinly", ["whole-grain bread","butter","cucumber","dill (optional)"]),
 ("Overnight Oats Jar", 10, [("pour","Pour the milk"),("stir","Stir it all up"),("sprinkle","Top with fruit")], "Fridge overnight", ["1/2 cup oats","1/2 cup milk","2 tbsp yogurt","berries"]),
 ("Apple Donuts", 10, [("spread","Spread the yogurt"),("sprinkle","Add sprinkles of seeds"),("count","Count the rings")], "Core and slice the apple", ["1 apple","yogurt or nut butter","hemp seeds, coconut"]),
 ("Hummus Rainbow Plate", 10, [("wash","Wash the veggies"),("sort","Sort by color"),("dip","Dip and taste")], "Cut veggie sticks", ["hummus","carrot","pepper","cucumber","snap peas"]),
 ("Banana Sushi", 10, [("spread","Spread the butter"),("roll","Roll it up tight"),("count","Count the slices")], "Slice into rounds", ["1 tortilla","sunflower or nut butter","1 banana"]),
 ("Frozen Yogurt Drops", 10, [("pour","Spoon yogurt into a bag"),("press","Squeeze little drops"),("wait","Wait for the freezer")], "Snip the bag corner, freeze 2 h", ["1 cup yogurt","1 tbsp berry puree"]),
 ("Muffin Tin Egg Bites", 30, [("crack","Crack the eggs (with help)"),("stir","Whisk, whisk, whisk"),("sprinkle","Add veggies to each cup")], "Oven 350°F / 175°C, 18 min", ["6 eggs","spinach","pepper","cheese"]),
 ("Pick & Mix Snack Cups", 5, [("sort","Sort into bowls"),("count","Count 5 of each"),("pour","Pour into a cup")], "Choose age-safe pieces", ["whole-grain cereal","pumpkin seeds","dried apple","popped sorghum"]),
 ("Berry Chia Jam", 15, [("mash","Mash the berries"),("stir","Stir in chia seeds"),("wait","Wait 20 minutes")], "Warm berries gently", ["2 cups berries","2 tbsp chia seeds","1 tsp lemon juice"]),
 ("Quesadilla Triangles", 15, [("sprinkle","Sprinkle the cheese"),("spread","Spread the beans"),("count","Count the triangles")], "Cook in a pan, cut", ["2 tortillas","cheese","black beans","sweetcorn"]),
 ("Pancake Faces", 25, [("pour","Pour the milk"),("stir","Stir the batter"),("shape","Make a fruit face")], "Cook pancakes at the stove", ["1 cup flour","1 egg","1 cup milk","fruit for faces"]),
 ("Frozen Banana Pops", 15, [("dip","Dip in yogurt"),("sprinkle","Roll in toppings"),("wait","Wait for the freezer")], "Cut bananas, add sticks", ["2 bananas","yogurt","crushed cereal"]),
 ("Mash-It Guacamole", 10, [("mash","Mash the avocado"),("pour","Squeeze the lime"),("stir","Stir and taste")], "Halve avocado, chop tomato", ["2 avocados","1/2 lime","1 small tomato","pinch of salt"]),
 ("Cinnamon Apple Cups", 20, [("wash","Wash the apples"),("sprinkle","Sprinkle cinnamon"),("stir","Stir the oats on top")], "Chop apples, microwave 3 min", ["2 apples","cinnamon","2 tbsp oats","yogurt to serve"]),
]

CSS_EXTRA = """
.cards{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:14px; flex:1; margin-bottom:6px; }
.rc{ border:1px solid var(--line); border-radius:16px; padding:12px 14px 10px; background:#fff; display:flex; flex-direction:column; position:relative; }
.rc:nth-child(2),.rc:nth-child(3){ background:var(--cream); }
.rc .no{ position:absolute; top:10px; right:12px; font-size:7pt; letter-spacing:.14em; color:var(--sage); font-weight:600; }
.rc h3{ margin:0; font-size:12.5pt; color:var(--dark); font-weight:700; line-height:1.1; padding-right:30px; }
.rc .time{ font-size:7.5pt; color:var(--soft); margin:3px 0 8px; display:flex; align-items:center; gap:5px; }
.rc .sec{ font-size:6.8pt; letter-spacing:.16em; text-transform:uppercase; color:var(--sage); font-weight:600; margin:4px 0 4px; }
.job{ display:flex; align-items:center; gap:8px; font-size:9pt; font-weight:500; color:var(--ink); margin-bottom:4px; }
.job .ic{ width:28px; height:28px; border-radius:50%; background:var(--tint); display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.job .n{ width:16px; height:16px; border-radius:50%; border:1.4px solid var(--accent); font-size:7pt; font-weight:700; color:var(--dark); display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.ing{ font-size:8pt; color:var(--ink); line-height:1.45; margin:0; padding-left:13px; }
.adult{ font-size:7.8pt; color:var(--soft); background:var(--warm); border-radius:8px; padding:5px 8px; margin-top:6px; }
.rate{ margin-top:auto; display:flex; align-items:center; justify-content:space-between; padding-top:6px; border-top:1px dotted var(--line); font-size:7pt; letter-spacing:.12em; text-transform:uppercase; color:var(--soft); }
.faces{ display:flex; gap:6px; }
.badges{ display:grid; grid-template-columns:repeat(5,1fr); gap:12px; }
.badge{ text-align:center; font-size:7.6pt; color:var(--ink); }
.badge .c{ width:0.95in; height:0.95in; border:1.8px dashed var(--accent); border-radius:50%; margin:0 auto 5px; display:flex; align-items:center; justify-content:center; color:var(--line); font-size:16pt; font-weight:700; }
.rules{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.rule{ display:flex; gap:10px; align-items:center; background:var(--tint); border:1px solid var(--line); border-radius:12px; padding:10px 12px; font-size:9.2pt; font-weight:500; color:var(--dark); }
"""

FACE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#8aa893" stroke-width="1.6" stroke-linecap="round"><circle cx="12" cy="12" r="9"/>{m}<circle cx="9" cy="10" r=".8" fill="#8aa893"/><circle cx="15" cy="10" r=".8" fill="#8aa893"/></svg>'
FACES = "".join(FACE.format(m=m) for m in ['<path d="M8 15c2 2 6 2 8 0"/>', '<path d="M8 15h8"/>', '<path d="M8 16c2-2 6-2 8 0"/>'])
CLOCK = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#5f6f66" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'


def card(i, r):
    t, m, jobs, adult, ing = r
    js = "".join(f'<div class="job"><span class="n">{k+1}</span><span class="ic">{icon(ic,16)}</span>{tx}</div>' for k, (ic, tx) in enumerate(jobs))
    li = "".join(f"<li>{x}</li>" for x in ing)
    return (f'<div class="rc"><span class="no">No. {i:02d}</span><h3>{t}</h3><div class="time">{CLOCK} about {m} min</div>'
            f'<div class="sec">Little chef jobs</div>{js}<div class="sec">You need</div><ul class="ing">{li}</ul>'
            f'<div class="adult"><b>Grown-up:</b> {adult}</div><div class="sec" style="margin-top:8px">Our notes</div><div class="wline" style="height:.26in"></div><div class="wline" style="height:.26in"></div><div class="rate"><span>Did we like it?</span><span class="faces">{FACES}</span></div></div>')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pages = [cover(NAME, "20 picture-step recipe cards for little hands. Real food, simple jobs, big helper pride.",
                   "A printable kitchen kit", "8 pages · 20 cards · Ages 3+ with a grown-up", "spoon")]
    rules = ["Wash hands first", "Ask before you touch the oven", "Knives are for grown-ups", "Taste with a clean spoon",
             "Spills are okay – we wipe together", "Tie hair back, sleeves up", "One job at a time", "Clean up, then celebrate"]
    pages.append(f"""<div class="page">{page_head("Start here", "How to cook together", "book")}
<p class="subtitle">Pick a card, put it on the fridge, and let your child do the numbered jobs. Grown-up jobs are listed at the bottom of each card. Print on card stock and cut along the gaps – four cards per page.</p>
<div class="sec" style="font-size:8pt;letter-spacing:.2em;color:var(--sage);font-weight:600;margin:6px 0 10px">LITTLE CHEF RULES</div>
<div class="rules">{''.join(f'<div class="rule">{icon("star",18)}{x}</div>' for x in rules)}</div>
<div class="row" style="margin-top:auto">
 <div class="card col"><h3>Allergy check</h3><div class="mini">Swap any ingredient your family avoids. Nut butters can be swapped for sunflower butter. Cut round foods like grapes in quarters for small children.</div></div>
 <div class="card warm col"><h3>A note for parents</h3><div class="mini">Always supervise. Oven, stove and knife steps are grown-up jobs. These are simple family recipes, not nutrition or medical advice.</div></div>
</div>{footer(NAME, "Start here")}</div>""")
    for p in range(5):
        cs = "".join(card(p * 4 + k + 1, R[p * 4 + k]) for k in range(4))
        pages.append(f'<div class="page" style="padding-bottom:0.75in">{page_head(f"Recipe cards {p*4+1}–{p*4+4}", "Let\'s cook!", "spoon")}<div class="cards">{cs}</div>{footer(NAME, f"Cards {p*4+1}–{p*4+4}")}</div>')
    bs = "".join(f'<div class="badge"><div class="c">{i+1}</div>{R[i][0]}</div>' for i in range(20))
    pages.append(f"""<div class="page">{page_head("Collect them all", "Little Chef Badge Chart", "star")}
<p class="subtitle">Color the circle or add a sticker every time you cook a recipe. Twenty circles = a real Little Chef!</p>
<div class="badges">{bs}</div>
<div class="row" style="margin-top:auto">
 <div class="card col"><span class="lbl">My favorite recipe</span><div class="wline"></div></div>
 <div class="card warm col"><span class="lbl">Little chef's name</span><div class="wline"></div></div>
</div>{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME} – Toddler Recipe Cards</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS_EXTRA}</style></head><body>{"".join(pages)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"{SLUG}.html")


if __name__ == "__main__":
    main()
