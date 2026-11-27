#!/usr/bin/env python3
"""Christmas Family Games Bundle (termekotletek A1): bingo (8 különböző kártya + hívókártyák), házi kincskeresés,
Would You Rather (24), Charades (24), Pictionary (24 szó), Christmas trivia (20 + megoldás), pontozólap. 13 oldal."""
import random
from pathlib import Path
from common import page_head, icon, footer

SLUG = "christmas-family-games-bundle"; NAME = "Christmas Family Games Bundle"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG
CSS = """:root{ --dark:#1f4d3a; --sage:#b8322a; --tint:#fdf1ee; --line:#efd2c6; --accent:#d9a441; --warm:#eef6ef; --warmline:#cfe3d2; --cream:#fffaf3; }
.cv{ background:linear-gradient(180deg,#fffaf3,#fdeee6); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 6px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.8in; line-height:1.45; }
.cv .pill{ margin-top:20px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.bingo{ display:grid; grid-template-columns:repeat(5,1fr); border:3px solid var(--sage); border-radius:10px; overflow:hidden; margin:4px 0 12px; }
.bingo div{ border:1px solid var(--line); height:.78in; display:flex; align-items:center; justify-content:center; text-align:center; font-size:10.5pt; font-weight:600; padding:3px; color:#333; }
.bingo .h{ background:var(--sage); color:#fff; font-size:20pt; height:.5in; } .bingo .free{ background:var(--accent); color:#fff; }
.two{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.card2{ border:2px dashed var(--sage); border-radius:12px; padding:10px 12px; min-height:.95in; display:flex; align-items:center; justify-content:center; text-align:center; font-size:12pt; font-weight:600; color:#333; }
.grid4{ display:grid; grid-template-columns:repeat(3,1fr); gap:10px; flex:1; margin-bottom:.12in; }
.tick{ display:flex; gap:10px; align-items:center; font-size:12.5pt; margin:7px 0; } .tick span{ width:17px; height:17px; border:2px solid var(--dark); border-radius:4px; flex:0 0 auto; }
.q{ font-size:11.5pt; margin:6px 0; line-height:1.35; } .q b{ color:var(--sage); }
table.score{ width:100%; border-collapse:collapse; } table.score td, table.score th{ border:1.5px solid var(--line); height:.42in; text-align:center; font-size:11pt; } table.score th{ background:var(--tint); color:var(--dark); }
"""
WORDS = ["Snowman", "Reindeer", "Candy cane", "Stocking", "Gingerbread", "Star", "Sleigh", "Mittens", "Ornament", "Wreath", "Bell", "Present",
         "Hot cocoa", "Snowflake", "Elf", "Christmas tree", "Cookies", "Candle", "Scarf", "Lights", "Angel", "Penguin", "Holly", "Santa hat", "Teddy bear",
         "Gift bag", "Chimney", "Sled", "Pine cone", "Nutcracker"]
WYR = ["build a snowman or have a snowball fight?", "open one gift on Christmas Eve or all on Christmas Day?", "be an elf or a reindeer for a day?",
       "eat only cookies or only candy canes all day?", "have a white Christmas or a beach Christmas?", "decorate the tree or bake cookies?",
       "ride in Santa's sleigh or drive the snow plow?", "wear pajamas all day or a fancy outfit?", "sing a carol alone or dance in front of everyone?",
       "have a talking snowman or a flying reindeer?", "get one big present or ten small ones?", "go sledding or ice skating?",
       "live in a gingerbread house or an igloo?", "have hot cocoa or eggnog?", "be the star on top of the tree or a present under it?",
       "find a puppy or a kitten under the tree?", "wrap 100 presents or bake 100 cookies?", "have elf ears or a red reindeer nose?",
       "spend Christmas at the North Pole or on the moon?", "make a snow angel or a snow fort?", "watch a Christmas movie or play a board game?",
       "have Christmas twice a year or a birthday every month?", "be able to fly like Santa or be invisible like the elves?", "eat Christmas dinner for breakfast or breakfast for Christmas dinner?"]
CHAR = ["Building a snowman", "Wrapping a present", "Decorating the tree", "Ice skating", "Opening a gift", "Sledding down a hill", "Baking cookies",
        "Hanging a stocking", "A reindeer flying", "Santa going down the chimney", "Throwing a snowball", "Making a snow angel", "Singing carols",
        "Drinking hot cocoa", "Shivering in the cold", "Putting on mittens", "An elf making toys", "Ringing a bell", "Lighting a candle",
        "A penguin waddling", "Catching snowflakes", "Hugging a teddy bear", "Shoveling snow", "Sleeping on Christmas Eve"]
PICT = ["Snowman", "Candy cane", "Mitten", "Igloo", "Star", "Gift", "Stocking", "Reindeer", "Bell", "Sled", "Christmas tree", "Elf hat", "Cookie",
        "Penguin", "Snowflake", "Wreath", "Chimney", "Ornament", "Candle", "Scarf", "Gingerbread house", "Santa's boot", "Polar bear", "Hot cocoa"]
TRIVIA = [("What color is Santa's suit?", "Red and white"), ("How many reindeer pull Santa's sleigh in the classic poem?", "Eight (nine with Rudolph)"),
          ("What do people traditionally leave out for Santa?", "Milk and cookies"), ("What is the name of the snowman in the famous song?", "Frosty"),
          ("Which reindeer has a red nose?", "Rudolph"), ("What do you call a person who makes toys at the North Pole?", "An elf"),
          ("What shape is a candy cane?", "A hook / the letter J"), ("Where does Santa live?", "The North Pole"),
          ("What do you hang over the fireplace?", "Stockings"), ("What is a baby reindeer called?", "A calf"),
          ("What sweet house is made from cookies?", "A gingerbread house"), ("What goes on top of a Christmas tree?", "A star or an angel"),
          ("What do snowmen often have as a nose?", "A carrot"), ("How many points does a snowflake usually have?", "Six"),
          ("What do you call the plant people kiss under?", "Mistletoe"), ("Which month is Christmas in?", "December"),
          ("What do reindeer like to eat?", "Lichen, moss and grass"), ("What is frozen water called?", "Ice"),
          ("What do you write to Santa?", "A letter or a wish list"), ("What is the day before Christmas called?", "Christmas Eve")]
HUNT = ["Something red", "Something that sparkles", "A sock", "Something soft", "A star shape", "Something that smells nice", "A ribbon or string",
        "Something round", "A spoon", "Something green", "A book with a winter picture", "A button", "Something that makes a sound", "A blanket",
        "Something smaller than your thumb", "A picture of a family member"]


def bingo(seed):
    random.seed(seed); w = random.sample(WORDS, 24); w.insert(12, "FREE")
    cells = "".join(f'<div class="h">{c}</div>' for c in "JOLLY") + "".join(f'<div class="{"free" if x == "FREE" else ""}">{x}</div>' for x in w)
    return f'<div class="bingo">{cells}</div>'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#d9a441",1.2)}</div><div class="eyebrow">Printable family game night · All ages</div><h1>Christmas<br>Family Games</h1>'
          f'<div class="tg">Seven easy games for Christmas Eve, family gatherings and school parties: bingo, a scavenger hunt, Would You Rather, charades, drawing, trivia and a score sheet. Print, cut and play.</div><div class="pill">13 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("For grown-ups", "How to play", "book")}
<div class="step"><div class="num">1</div><div><b>Christmas Bingo</b><p>Give everyone a different card (8 included). Cut out the caller cards, shuffle and read them out. First to get five in a row shouts “JOLLY!”.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Scavenger Hunt</b><p>Set a timer for 10 minutes. Players find the items around the house and tick them off.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Would You Rather</b><p>Read a card, everyone picks a side of the room. Explaining why is half the fun.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Charades and Pictionary</b><p>Draw a card, act it out or draw it in one minute. No words, no letters.</p></div></div>
<div class="step"><div class="num">5</div><div><b>Trivia</b><p>Read the questions; answers are on the last page. Play in teams of mixed ages.</p></div></div>
<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>Tip</h3><div class="mini">Print the bingo cards on cardstock and use buttons, cereal or chocolate chips as markers.</div></div>
{footer(NAME, "How to play")}</div>""")
    for k in range(0, 8, 2):
        pg.append(f'<div class="page">{page_head("Christmas Bingo", f"Bingo cards {k + 1}–{k + 2}", "star")}{bingo(k + 1)}{bingo(k + 2)}{footer(NAME, "Bingo")}</div>')
    calls = "".join(f'<div class="card2">{w}</div>' for w in WORDS)
    pg.append(f'<div class="page">{page_head("Cut out and shuffle", "Bingo caller cards", "heart")}<div class="grid4" style="grid-template-columns:repeat(5,1fr)">{calls}</div>{footer(NAME, "Caller cards")}</div>')
    tk = lambda xs: "".join(f'<div class="tick"><span></span>{x}</div>' for x in xs)
    pg.append(f'<div class="page">{page_head("10 minutes · ready, set, go", "Christmas Scavenger Hunt", "check")}<div class="two"><div>{tk(HUNT[:8])}</div><div>{tk(HUNT[8:])}</div></div>'
              f'<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>Found everything?</h3><div class="mini">Name: ______________________ Time: ________</div></div>{footer(NAME, "Scavenger hunt")}</div>')
    w = "".join(f'<div class="card2">Would you rather {x}</div>' for x in WYR)
    pg.append(f'<div class="page">{page_head("Cut out and take turns", "Would You Rather", "heart")}<div class="grid4">{w}</div>{footer(NAME, "Would you rather")}</div>')
    c = "".join(f'<div class="card2">{x}</div>' for x in CHAR)
    pg.append(f'<div class="page">{page_head("Act it out, no words", "Christmas Charades", "star")}<div class="grid4">{c}</div>{footer(NAME, "Charades")}</div>')
    p_ = "".join(f'<div class="card2">{x}</div>' for x in PICT)
    pg.append(f'<div class="page">{page_head("Draw it in one minute", "Christmas Pictionary", "star")}<div class="grid4">{p_}</div>{footer(NAME, "Pictionary")}</div>')
    tq = "".join(f'<div class="q"><b>{i + 1}.</b> {q}</div>' for i, (q, a) in enumerate(TRIVIA))
    pg.append(f'<div class="page">{page_head("Play in teams", "Christmas Trivia", "book")}{tq}{footer(NAME, "Trivia")}</div>')
    ta = "".join(f'<div class="q"><b>{i + 1}.</b> {a}</div>' for i, (q, a) in enumerate(TRIVIA))
    rows = "".join("<tr>" + "".join("<td></td>" for _ in range(8)) + "</tr>" for _ in range(6))
    pg.append(f"""<div class="page">{page_head("Answers and scores", "Trivia answers + score sheet", "check")}<div class="two"><div>{ta}</div><div>
<table class="score"><tr><th>Name</th><th>Bingo</th><th>Hunt</th><th>WYR</th><th>Char.</th><th>Draw</th><th>Trivia</th><th>Total</th></tr>{rows}</table></div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8"); print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
