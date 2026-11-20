#!/usr/bin/env python3
"""Kindness Advent Calendar Cards – 24 kedvességkártya + matricás tracker + családi beszélgetőkártyák → termekek/kindness-advent-cards/
Manó nélkül is működik (a „kindness” kulcsszó viszi). Védjegy: nincs."""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "kindness-advent-cards"
NAME = "Kindness Advent Cards"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """:root{ --dark:#2f6b4f; --sage:#b23a3a; --tint:#f6ece6; --line:#e6cfc6; --accent:#c9a227; --warm:#eef3ec; --warmline:#cfe0d3; --cream:#fdf8f3; }
.grid{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:repeat(3,1fr); gap:12px; flex:1; margin-bottom:.1in; }
.kc{ border:2px dashed var(--line); border-radius:16px; padding:14px 16px; display:flex; flex-direction:column; gap:6px; background:#fff; position:relative; }
.kc:nth-child(4n+2), .kc:nth-child(4n+3){ background:var(--warm); border-color:var(--warmline); }
.kc .d{ font-size:30pt; font-weight:800; color:var(--sage); line-height:1; }
.kc:nth-child(4n+2) .d, .kc:nth-child(4n+3) .d{ color:var(--dark); }
.kc b{ font-size:15pt; line-height:1.2; color:var(--ink,#2b2b2b); }
.kc p{ margin:0; font-size:12.8pt; line-height:1.45; }
.kc .tip{ margin-top:auto; font-size:10.5pt; color:var(--dark); }
.kc .ic{ position:absolute; right:12px; top:12px; opacity:.85; }
.track{ display:grid; grid-template-columns:repeat(6,1fr); grid-template-rows:repeat(4,1fr); gap:10px; flex:1; margin-bottom:.1in; align-items:center; justify-items:center; }
.track div{ border:2px solid var(--line); border-radius:50%; width:1.05in; height:1.05in; display:flex; align-items:center; justify-content:center; font-size:20pt; font-weight:800; color:var(--sage); background:#fff; }
.track div:nth-child(even){ color:var(--dark); border-color:var(--warmline); }
.stk{ display:grid; grid-template-columns:repeat(6,1fr); gap:10px; margin-bottom:.1in; }
.stk div{ border:1.5px dashed var(--sage); border-radius:50%; aspect-ratio:1; display:flex; align-items:center; justify-content:center; }
.talk{ display:grid; grid-template-columns:1fr 1fr; gap:12px; flex:1; margin-bottom:.1in; }
.talk div{ border:2px dashed var(--warmline); border-radius:14px; padding:14px; font-size:15pt; justify-content:center; text-align:center; line-height:1.4; display:flex; align-items:center; background:#fff; }
.cv{ background:linear-gradient(180deg,#fdf8f3,#eef3ec); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; }
.cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.cert{ border:6px double var(--accent); border-radius:22px; flex:1; margin-bottom:.15in; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:.4in; background:#fff; }
.cert h2{ font-size:34pt; color:var(--sage); margin:12px 0; } .cert p{ font-size:14pt; line-height:1.5; max-width:5.4in; }
.cert .ln{ width:4.2in; border-bottom:2px solid var(--dark); height:.55in; margin:6px auto 14px; }
"""

K = [  # (cím, feladat, tipp, ikon)
 ("Make a card for someone far away", "Draw or write a card for a grandparent, cousin or friend who lives far away and mail it together.", "Tip: add a family photo.", "heart"),
 ("Hold the door", "Hold the door open for someone today and say a friendly hello.", "Tiny acts count too.", "star"),
 ("Thank a helper", "Draw a thank-you picture for your teacher, bus driver, school nurse or lunch staff.", "Name one thing they do for you.", "heart"),
 ("Donate a toy", "Choose one toy in good condition to give to a child who needs it this Christmas.", "Grown-ups: find a local toy drive.", "star"),
 ("Compliment day", "Give three different people a real compliment today.", "\"I like how you…\" works great.", "heart"),
 ("Help with dinner", "Set the table, wash vegetables or stir the pot without being asked.", "Ask: \"What can I do?\"", "check"),
 ("Feed the birds", "Hang a simple bird feeder or scatter seeds outside for winter birds.", "A pine cone + seeds is enough.", "star"),
 ("Sweet note in a lunchbox", "Hide a kind note in someone's lunchbox, coat pocket or bag.", "Use the mini notes page.", "heart"),
 ("Clean up together", "Spend 10 minutes tidying a room you share, without complaining.", "Put on a Christmas song and race the clock.", "check"),
 ("Bake for a neighbor", "Bake or decorate cookies and bring a few to a neighbor.", "Store-bought cookies count!", "star"),
 ("Call a grandparent", "Make a phone or video call to a grandparent or older relative and ask about their childhood Christmases.", "Ask: \"What was your favorite gift?\"", "heart"),
 ("Share with a sibling", "Let a brother, sister or friend choose first, or share a favorite thing.", "Notice how they smile.", "check"),
 ("Pick up litter", "With a grown-up and gloves, pick up litter on a short walk.", "Count how many pieces you find.", "star"),
 ("Make someone laugh", "Tell a joke, make a funny face or plan a silly surprise.", "Use a joke card from the back.", "heart"),
 ("Thank you for the mail", "Leave a thank-you note or drawing for your mail carrier or delivery driver.", "Tape it to the mailbox.", "check"),
 ("Kindness for animals", "Make a blanket bed for your pet, or collect old towels for an animal shelter.", "Shelters often need towels.", "star"),
 ("Help without being asked", "Find one job at home that needs doing and just do it.", "Then see who notices!", "check"),
 ("Write a kind review of your day", "At bedtime, tell your family one kind thing someone did for you today.", "Say thank you to them, too.", "heart"),
 ("Snowflake surprise", "Cut paper snowflakes and leave them for someone to find.", "Write a kind word in the middle.", "star"),
 ("Teacher or coach gift", "Make a small gift or card for a teacher or coach before the break.", "A drawing is a perfect gift.", "heart"),
 ("Be a good friend", "Ask someone who is alone to play with you or sit with you.", "Everyone wants to be included.", "check"),
 ("Kindness to yourself", "Do something kind for you: rest, read, draw, or say \"I did my best today\".", "You deserve kindness too.", "heart"),
 ("Christmas Eve helper", "Help get the house ready: wrap a gift, set out cookies or light the candles with a grown-up.", "Ask what would help most.", "star"),
 ("Merry Christmas kindness", "Give every person in your family a hug or a kind word today.", "Look back at all 24 missions!", "heart"),
]

TALK = ["What was the kindest thing someone did for you this year?", "Who could use a little kindness this week?",
        "How does it feel when someone is kind to you?", "What is something kind you can do in one minute?",
        "Who is a helper in our town we could thank?", "What is one kind thing you did that nobody saw?",
        "How can we be kind to someone we don't know?", "What does a good friend do?"]

JOKES = ["What do snowmen eat for breakfast? Frosted flakes!", "Why did the gingerbread go to the doctor? It was feeling crummy!",
         "What do you call a reindeer with no eyes? No eye-deer!", "What is a snowman's favorite game? Freeze tag!",
         "Why was the Christmas tree bad at knitting? It kept dropping its needles!", "What do elves learn in school? The elf-abet!"]


def card(n, t, d, tip, ic):
    return (f'<div class="kc"><span class="ic">{icon(ic, 26, "#c9a227")}</span><div class="d">{n}</div>'
            f'<b>{t}</b><p>{d}</p><div class="tip">{tip}</div></div>')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("heart",110,"#b23a3a",1.2)}</div><div class="eyebrow">Printable · December 1–24 · Ages 3–12</div>'
          f'<h1>Kindness<br>Advent Calendar</h1><div class="tg">24 simple kindness missions for kids, one for every day of December. Works on its own, with an advent calendar, or with your Christmas elf.</div>'
          f'<div class="pill">24 cards · Tracker · Talk cards · Certificate · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How the kindness calendar works", "book")}
<p class="subtitle">A countdown that grows kind hearts instead of a sugar rush. Each card is one small mission that takes 5–20 minutes and needs little or no shopping.</p>
<div class="step"><div class="num">1</div><div><b>Print and cut</b><p>Print the card pages on card stock, cut along the dashed lines and fold or roll each card.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Choose your calendar</b><p>Put a card in each pocket of an advent calendar, in numbered envelopes, in a jar, or let your Christmas elf deliver one every morning.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Do it together</b><p>Read the mission at breakfast and do it as a family. Little ones need a grown-up partner, older kids can lead.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Track and talk</b><p>Color a circle on the tracker every day. At dinner, pull a talk card and share how it felt.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Swap freely</h3><div class="mini">Busy day? Swap cards around. There is a blank card page for your own family missions.</div></div>
<div class="card warm col"><h3>Grown-ups</h3><div class="mini">Some missions need an adult (baking, litter walk, phone calls). Safety first, kindness second.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    for i in range(0, 24, 6):
        cs = "".join(card(i + j + 1, *K[i + j]) for j in range(6))
        pg.append(f'<div class="page">{page_head("Cut along the dashed lines", f"Kindness missions {i+1}–{i+6}", "star")}<div class="grid">{cs}</div>{footer(NAME, f"Days {i+1}–{i+6}")}</div>')
    blank = "".join(f'<div class="kc"><div class="d">__</div><b>Our own mission</b><p style="border-bottom:1.5px solid var(--line);height:.35in"></p><p style="border-bottom:1.5px solid var(--line);height:.35in"></p><div class="tip">Made by: ____________</div></div>' for _ in range(6))
    pg.append(f'<div class="page">{page_head("Make your own", "Blank kindness cards", "heart")}<div class="grid">{blank}</div>{footer(NAME, "Blank cards")}</div>')
    tr = "".join(f"<div>{d}</div>" for d in range(1, 25))
    pg.append(f'<div class="page">{page_head("Color a circle every day", "My kindness tracker", "calendar")}<p class="subtitle">Name: ______________________ &nbsp; Color, sticker or stamp each day you finish a mission.</p><div class="track">{tr}</div>{footer(NAME, "Tracker")}</div>')
    tk = "".join(f"<div>{t}</div>" for t in TALK)
    pg.append(f'<div class="page">{page_head("Dinner table", "Kindness talk cards", "heart")}<div class="talk">{tk}</div>{footer(NAME, "Talk cards")}</div>')
    jk = "".join(f"<div>{j}</div>" for j in JOKES)
    notes = "".join(f"<div>You make people smile.<br><br>— ________</div>" for _ in range(2))
    pg.append(f'<div class="page">{page_head("For missions 8 and 14", "Mini notes and joke cards", "star")}<div class="talk">{jk}{notes}</div>{footer(NAME, "Notes")}</div>')
    pg.append(f"""<div class="page">{page_head("December 24", "Kindness certificate", "check")}
<div class="cert">{icon("star",70,"#c9a227",1.2)}<h2>Kindness Champion</h2><p>This certificate is proudly given to</p><div class="ln"></div>
<p>for spreading kindness every day of December and making Christmas brighter for everyone around you.</p><div class="ln" style="width:3in;height:.45in"></div><p style="font-size:10pt">Signed by the family · Date</p></div>
{footer(NAME, "For personal and single-classroom use · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"{SLUG}.html", len(pg), "pages")


if __name__ == "__main__":
    main()
