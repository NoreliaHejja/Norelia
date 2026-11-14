#!/usr/bin/env python3
"""Easy Christmas Elf Ideas – 30 no-mess 5-minute setups + December planner + elf-size props → termekek/easy-elf-ideas/*.html
A Kindness Elf Kit rokon terméke. Védjegy: csak „Christmas Elf”."""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "easy-elf-ideas"
NAME = "Easy Elf Ideas"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

XMAS = """:root{ --dark:#2f6b4f; --sage:#b23a3a; --tint:#f6ece6; --line:#e6cfc6; --accent:#c9a227; --warm:#eef3ec; --warmline:#cfe0d3; --cream:#fdf8f3; }
.grid{ display:grid; grid-template-columns:1fr 1fr; gap:12px; flex:1; margin-bottom:.1in; }
.id{ border:2px dashed var(--line); border-radius:14px; padding:12px 14px; display:flex; flex-direction:column; gap:6px; background:#fff; }
.id .t{ display:flex; align-items:center; gap:8px; } .id .t b{ font-size:13.5pt; color:var(--sage); line-height:1.15; }
.id .n{ width:28px; height:28px; border-radius:50%; background:var(--dark); color:#fff; font-weight:700; font-size:10pt; display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.id p{ margin:0; font-size:12.4pt; line-height:1.5; }
.id .need{ margin-top:auto; font-size:9.5pt; color:var(--dark); background:var(--warm); border-radius:8px; padding:5px 8px; }
.cal{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; flex:1; margin-bottom:.1in; }
.cal div{ border:1.5px solid var(--line); border-radius:10px; padding:6px 8px; font-size:8pt; color:var(--soft); }
.cal div b{ display:block; font-size:15pt; color:var(--sage); }
.props{ display:grid; grid-template-columns:1fr 1fr; gap:14px; flex:1; margin-bottom:.1in; }
.pr{ border:2px dashed var(--sage); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:10px; }
.pr b{ font-size:17pt; color:var(--sage); line-height:1.1; } .pr span{ font-size:9pt; color:var(--dark); margin-top:6px; }
.cv{ background:linear-gradient(180deg,#fdf8f3,#eef3ec); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; }
.cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
"""

I = [  # (cím, mit csinál, mi kell)
 ("Marshmallow Bath", "The elf relaxes in a mug or bowl full of mini marshmallows, with a tiny towel on its head.", "Mug, mini marshmallows, napkin"),
 ("Toilet Paper Snowman", "Stack three rolls, add a scarf and a paper face. The elf proudly stands next to its snowman.", "3 TP rolls, scarf, paper"),
 ("Zip-Line Ride", "Tie a string between two chairs and hang the elf from it with a clothespin.", "String, clothespin"),
 ("Fishing for Goldfish", "The elf sits on the sink edge with a pencil fishing rod over a bowl of fish crackers.", "Pencil, string, crackers"),
 ("Reading Corner", "The elf reads a picture book to a circle of stuffed animals.", "Book, stuffed toys"),
 ("Hide and Seek Note", "The elf hides with a note: 'Count to 20 and come find me!'", "Note from the props page"),
 ("Elf-Sized Breakfast", "A tiny pancake or cereal bowl waits on the table with a 'Good morning!' note.", "Cereal, small bowl"),
 ("Paper Snowflake Party", "Paper snowflakes all over the table, and the elf holds the scissors (handles only).", "Paper, child-safe scissors"),
 ("Stuck in the Garland", "The elf is tangled in the Christmas garland, waving for help.", "Garland or tinsel"),
 ("Lego Builder", "The elf built a tiny house out of blocks, with a 'Do Not Disturb: Elf at Work' sign.", "Building blocks, sign"),
 ("Kindness Mission", "The elf holds a card with today's kind mission: 'Make a card for Grandma'.", "Note card"),
 ("Hot Cocoa Bar", "Three mugs and a packet of cocoa, ready for an after-school treat.", "Cocoa packets, mugs"),
 ("Selfie Elf", "The elf poses with your phone (camera app open) as if it took a selfie overnight.", "Phone, 1 photo"),
 ("Sock Snowball Fight", "Rolled-up white socks everywhere, the elf hiding behind a pillow fort.", "White socks, pillow"),
 ("Candy Cane Fishing", "Candy canes hooked over the edge of a bowl, the elf holding one like a fishing pole.", "Candy canes, bowl"),
 ("Doctor Elf", "The elf has a bandage on its arm and gives a 'checkup' to stuffed animals.", "Bandage, stuffed toys"),
 ("Paper Chain Countdown", "A new paper chain with one link for each day left until Christmas.", "Paper strips, tape"),
 ("Elf Crossing", "Toy cars stop at a crosswalk made of paper strips while the elf crosses.", "Toy cars, white paper"),
 ("Fridge Visit", "The elf sits inside the fridge door with a note: 'It's cold, just like home!'", "Nothing extra"),
 ("Tic-Tac-Toe", "The elf starts a game of tic-tac-toe with a cereal-piece board and waits for your move.", "Paper, cereal"),
 ("Wrapping Paper Jail", "The elf is 'wrapped' on a chair: 'I tried to wrap myself as a present!'", "Wrapping paper, tape"),
 ("Movie Night", "The elf and some toys sit in front of the TV with a tiny bowl of popcorn.", "Popcorn, small bowl"),
 ("Treasure Map", "A hand-drawn map leads to a small treat hidden in the house.", "Paper, small treat"),
 ("Elf Workout", "The elf exercises with tiny 'weights' made of marshmallows and toothpicks.", "Marshmallows, toothpicks"),
 ("Art Gallery", "The elf 'drew' portraits of each family member and hung them on the fridge.", "Paper, crayons"),
 ("Tooth Brushing Buddy", "The elf waits next to the toothbrushes with a note: 'Two minutes, I'm timing!'", "Note card"),
 ("Thank-You Cards", "The elf sets out blank cards and crayons: 'Who will you thank today?'", "Cards, crayons"),
 ("Elf Sleepover", "The elf sleeps in a tiny bed made of a tissue box, next to a favorite toy.", "Tissue box, washcloth"),
 ("Santa Video Call", "The elf sits by a laptop or tablet showing a picture of the North Pole.", "Laptop or tablet"),
 ("Goodbye Hug", "On the last day, the elf hugs each family member's toothbrush with a goodbye note.", "Goodbye note"),
]

PROPS = [("Do Not Disturb", "Elf at work"), ("Elf Crossing", "Slow down, please"), ("Snowball Fight Zone", "Enter at your own risk"),
         ("Out of Office", "Back tonight · North Pole"), ("Count to 20", "and come find me!"), ("Kindness Mission", "Today: ____________")]


def card(n, t, d, need):
    return (f'<div class="id"><div class="t"><span class="n">{n}</span><b>{t}</b></div><p>{d}</p>'
            f'<div class="need">You need: {need}</div></div>')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#c9a227",1.2)}</div><div class="eyebrow">Printable · No mess · 5 minutes</div>'
          f'<h1>Easy Christmas<br>Elf Ideas</h1><div class="tg">30 quick, no-mess setups with things you already have, plus a December planner and cut-out elf-size signs.</div>'
          f'<div class="pill">30 ideas · Planner · Props · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to use your idea cards", "book")}
<p class="subtitle">No more 11 p.m. panic scrolling. Pick your ideas in advance, write them on the December planner, and keep the cards next to your bed. Every setup takes about five minutes and uses things you already have.</p>
<div class="step"><div class="num">1</div><div><b>Plan in one sitting</b><p>Choose 24 ideas and write the numbers on the December planner. Save the easiest ones for busy school nights.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Cut out the props</b><p>The elf-size signs make any setup look finished. Print them on card stock and fold them into little tents.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Set a reminder</b><p>A 9 p.m. phone alarm is the best elf helper ever invented.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Keep it kind</b><p>Pair a setup with a small kindness mission. The kids will remember how it felt, not how fancy it was.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Safety first</h3><div class="mini">Keep scissors, small candies and string out of reach of little children. Adult setup only.</div></div>
<div class="card warm col"><h3>Good to know</h3><div class="mini">"Christmas Elf" is a generic name for this activity. Not affiliated with any elf doll brand: use any toy you have.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    days = "".join(f"<div><b>{d}</b>Idea #<br>______</div>" for d in range(1, 25))
    pg.append(f'<div class="page">{page_head("December planner", "My 24-day elf plan", "calendar")}<div class="cal">{days}</div>{footer(NAME, "Planner")}</div>')
    for i in range(0, 30, 6):
        cs = "".join(card(i + j + 1, *I[i + j]) for j in range(6))
        pg.append(f'<div class="page">{page_head("Cut along the dashed lines", f"Ideas {i+1}–{i+6}", "star")}<div class="grid">{cs}</div>{footer(NAME, f"Ideas {i+1}–{i+6}")}</div>')
    ps = "".join(f'<div class="pr">{icon("star",34,"#c9a227")}<b>{a}</b><span>{b}</span></div>' for a, b in PROPS)
    pg.append(f'<div class="page">{page_head("Cut, fold, done", "Elf-size signs", "check")}<div class="props">{ps}</div>{footer(NAME, "Props")}</div>')
    pg.append(f"""<div class="page">{page_head("For grown-ups", "Elf emergency list", "heart")}
<p class="subtitle">Forgot again? These three take under one minute.</p>
<div class="card" style="margin-bottom:12px"><h3>1. The fridge visit</h3><div class="mini">Pop the elf inside the fridge door. Done.</div></div>
<div class="card warm" style="margin-bottom:12px"><h3>2. Count to 20</h3><div class="mini">Hide the elf anywhere and leave the "Count to 20" sign on the table.</div></div>
<div class="card" style="margin-bottom:12px"><h3>3. The kindness card</h3><div class="mini">Leave the elf where it was with a "Kindness Mission" sign. Kids love a mission more than a move.</div></div>
<div class="row" style="margin-top:auto"><div class="card col"><span class="lbl">Our elf's name</span><div class="wline"></div></div><div class="card col"><span class="lbl">Arrival date</span><div class="wline"></div></div><div class="card warm col"><span class="lbl">Goodbye date</span><div class="wline"></div></div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{XMAS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"{SLUG}.html", len(pg), "page")


if __name__ == "__main__":
    main()
