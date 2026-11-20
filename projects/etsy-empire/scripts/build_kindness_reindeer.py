#!/usr/bin/env python3
"""Kindness Reindeer Kit – Kindness Elf minta (W3), elf nélküli családoknak, 3–8 éves.
Érkező levél, útlevél, 24 cetli, tracker, 2 mentőlevél, félidős levél, reindeer food lap, búcsúlevél, oklevél, üres cetlik, 30 ötlet."""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "kindness-reindeer-kit"
NAME = "Kindness Reindeer Kit"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG
ELF = "reindeer.png"   # akvarell rénszarvas (Higgsfield)
ELF2 = "reindeer-bye.png"

CSS = """:root{ --dark:#6b3f22; --sage:#b8322a; --tint:#fdf3ee; --line:#efd2c6; --accent:#e5a823; --warm:#eef6ef; --warmline:#cfe3d2; --cream:#fffaf3; }
.cv{ background:linear-gradient(180deg,#fffaf3,#fdeee6); align-items:center; justify-content:center; text-align:center; }
.cv img{ width:2.6in; } .cv h1{ font-size:38pt; color:var(--sage); margin:6px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:18px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.letter{ border:3px double var(--sage); border-radius:18px; padding:26px 30px; background:#fff; flex:1; margin-bottom:.15in; display:flex; flex-direction:column; align-items:center; text-align:center; }
.letter img{ width:1.9in; } .letter h2{ color:var(--sage); font-size:24pt; margin:6px 0 10px; }
.letter p{ font-size:15pt; line-height:1.55; margin:0 0 10px; color:#333; max-width:5.6in; } .letter .sig{ margin-top:auto; font-size:14pt; color:var(--dark); font-style:italic; }
.notes{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:12px; flex:1; margin-bottom:.12in; }
.note{ border:2px dashed var(--sage); border-radius:16px; padding:12px 14px; background:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:6px; }
.note:nth-child(even){ border-color:var(--dark); } .note .d{ font-size:10pt; color:var(--sage); font-weight:700; letter-spacing:.06em; }
.note .m{ font-size:16pt; font-weight:600; color:#333; line-height:1.3; } .note .f{ font-size:10pt; color:var(--dark); font-style:italic; }
.track{ display:grid; grid-template-columns:repeat(6,1fr); gap:12px; margin:8px 0 14px; }
.track div{ border:2.5px solid var(--dark); border-radius:50%; aspect-ratio:1; display:flex; align-items:center; justify-content:center; font-size:20pt; font-weight:700; color:var(--dark); }
.pp{ border:2px solid var(--line); border-radius:14px; padding:12px 16px; background:#fff; margin-bottom:12px; }
.pp h3{ margin:0 0 6px; color:var(--sage); font-size:13pt; } .ln{ border-bottom:1.5px solid var(--line); height:.4in; }
.draw{ border:2px dashed var(--dark); border-radius:14px; height:3in; display:flex; align-items:flex-end; justify-content:center; padding:8px; color:var(--dark); font-size:11pt; margin-bottom:12px; }
.ideas{ columns:2; column-gap:22px; font-size:11pt; line-height:1.55; } .ideas li{ margin-bottom:4px; }
.cert{ border:6px double var(--accent); border-radius:20px; padding:30px; flex:1; margin-bottom:.15in; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; background:#fff; }
.cert h2{ font-size:30pt; color:var(--sage); margin:8px 0; } .cert .name{ border-bottom:2px solid var(--dark); width:4.6in; height:.55in; margin:14px 0; }
"""

MISSIONS = [
    ("hug", "Give someone you love a big hug."), ("toy", "Help tidy up the toys without being asked."),
    ("heart", "Say “thank you” to the person who made dinner."), ("star", "Draw a picture for a grandparent."),
    ("leaf", "Put out some seeds for the birds."), ("child", "Let a friend or sibling go first today."),
    ("cart", "Help carry the groceries in."), ("cat", "Be extra gentle with a pet or a teddy."),
    ("sun", "Wave and smile at a neighbor."), ("leaf", "Water a plant in your home."),
    ("book", "Read a story to someone younger (or to a teddy)."), ("spoon", "Help set the table."),
    ("heart", "Make a card for someone who needs cheering up."), ("hug", "Tell three people why you love them."),
    ("bowl", "Help clean up after a meal."), ("shoe", "Line up everyone’s shoes by the door."),
    ("star", "Give a compliment to everyone at breakfast."), ("sun", "Sing a holiday song for your family."),
    ("toy", "Pick a toy to donate to a child who needs it."), ("shirt", "Help fold or sort the laundry."),
    ("window", "Make a thank-you note for the mail carrier."), ("star", "Make a paper snowflake for a friend."),
    ("bowl", "Bake or decorate cookies to share."), ("heart", "Give everyone a thank-you hug tonight."),
]
IDEAS = ["Hold the door for someone", "Pick up one piece of litter (with a grown-up)", "Give your sibling the first turn",
         "Say “please” at every meal today", "Bring a grown-up a glass of water", "Help feed the pet",
         "Tidy up the bookshelf", "Make a get-well drawing", "Leave a sticker on someone’s pillow", "Call a grandparent and sing",
         "Give a compliment: “I like your hat!”", "Help fold the towels", "Put a toy back for someone else",
         "Make a “thank you” picture for the mail carrier", "Comfort a sad friend with a teddy", "Help carry the laundry basket",
         "Wash plastic cups in the sink", "Share your snack", "Draw a heart for the bus driver", "Help make breakfast toast",
         "Give the plants a drink", "Clean up crayons without being asked", "Say “sorry” and hug", "Wave at a neighbor’s window",
         "Make a necklace for a friend", "Help match the socks", "Let someone else choose the song", "Brush the dog or the teddy",
         "Help water the flowers outside", "Give a good-night hug to everyone"]


def img(name, w):
    return f'<img src="{name}" style="width:{w}" alt="">'


def letter(title, paras, sig="Love, your Kindness Reindeer", pic=ELF):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f'<div class="letter">{img(pic, "1.9in")}<h2>{title}</h2>{ps}<div class="sig">{sig}</div></div>'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv">{img(ELF, "2.6in")}<div class="eyebrow">Printable kit · Ages 3 to 8</div>'
          f'<h1>Kindness<br>Reindeer Kit</h1><div class="tg">A cozy December tradition for families without an elf: a little reindeer brings one kind mission a day. No mess, no special toy, five minutes a morning.</div>'
          f'<div class="pill">20 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("For grown-ups", "How the Kindness Reindeer works", "book")}
<p class="subtitle">Kids love little rituals. Each morning your child finds a note from the Kindness Reindeer with one small, kind thing to do. Read it together, do it together, and color one circle on the tracker.</p>
<div class="step"><div class="num">1</div><div><b>Meet your reindeer</b><p>Any soft toy can be the Kindness Reindeer, or simply leave the notes by the window with a hoofprint. Fill in the reindeer passport together.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Print and cut</b><p>Print the notes on paper or cardstock and cut them apart (4 per page). Keep them in an envelope, ready for each morning.</p></div></div>
<div class="step"><div class="num">3</div><div><b>One note a day</b><p>Leave a note out in the evening. In the morning, read it together. Most missions take five minutes and cost nothing.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Celebrate</b><p>Color a circle on the tracker. On Christmas Eve, read the goodbye letter and give the "I was kind" certificate.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Forgot a note?</h3><div class="mini">Use the lifesaver letters: "I was running late" and "Snowstorm delay."</div></div>
<div class="card warm col"><h3>Make it yours</h3><div class="mini">Skip any mission that doesn't fit your family. Use the blank notes and the 30 extra ideas.</div></div></div>
{footer(NAME, "For grown-ups")}</div>""")
    pg.append(f'<div class="page">{letter("Hello from the North Pole!", ["Hi, friend! I’m a young reindeer, and Santa sent me to help you get ready for Christmas.", "Every morning I will leave you one kind mission. Kindness is what makes reindeer fly, so every kind thing you do gives me a little more sparkle.", "I can’t wait to see all the kind things you do!"])}{footer(NAME, "Arrival letter")}</div>')
    pg.append(f"""<div class="page">{page_head("Meet your reindeer", "My reindeer passport", "star")}
<div class="draw">Draw your reindeer here</div>
<div class="pp"><h3>My reindeer's name</h3><div class="ln"></div></div>
<div class="pp"><h3>My reindeer's favorite snack</h3><div class="ln"></div></div>
<div class="pp"><h3>My name</h3><div class="ln"></div></div>
<div class="pp"><h3>Day my reindeer arrived</h3><div class="ln"></div></div>
{footer(NAME, "Passport")}</div>""")
    for i in range(0, 24, 4):
        ns = "".join(f'<div class="note"><div class="d">DAY {d + 1}</div>{icon(ic, 46, "#b8322a", 1.6)}<div class="m">{m}</div><div class="f">♥ your Kindness Reindeer</div></div>'
                     for d, (ic, m) in list(enumerate(MISSIONS))[i:i + 4])
        pg.append(f'<div class="page">{page_head("Cut and use one a day", f"Kindness notes · days {i + 1}–{i + 4}", "heart")}<div class="notes">{ns}</div>{footer(NAME, "Notes")}</div>')
    circles = "".join(f"<div>{n}</div>" for n in range(1, 25))
    pg.append(f"""<div class="page">{page_head("Color one circle a day", "My kindness tracker", "check")}
<p class="subtitle">After each kind mission, color one circle. Watch your kindness grow all the way to Christmas!</p>
<div class="track">{circles}</div>
<div class="row" style="margin-top:auto;margin-bottom:.15in"><div class="card col"><h3>My favorite kind thing</h3><div class="ln"></div><div class="ln"></div></div>{img(ELF, "1.6in")}</div>
{footer(NAME, "Tracker")}</div>""")
    pg.append(f'<div class="page">{letter("Sorry, I was running late!", ["Good morning! Flight practice with the big reindeer went very late last night.", "Today’s kind mission: give someone a big smile. I’ll be back on time tomorrow!"])}{footer(NAME, "Lifesaver letter")}</div>')
    pg.append(f'<div class="page">{letter("Snowstorm delay!", ["A big snowstorm kept me in the stable last night.", "Today’s kind mission: help someone who is having a hard day. I’ll be back tomorrow!"])}{footer(NAME, "Lifesaver letter")}</div>')
    pg.append(f'<div class="page">{letter("You’re doing great!", ["Santa heard about all your kind missions. He was so happy he did a little dance!", "Keep going, little friend. Christmas is getting closer and your kindness is shining bright."], "Love, your Kindness Reindeer")}{footer(NAME, "Mid-December letter")}</div>')
    pg.append(f"""<div class="page">{page_head("Christmas Eve", "Magic reindeer food", "star")}
<p class="subtitle">On Christmas Eve, sprinkle a little reindeer food outside so Santa’s team can find your home. Use only bird-safe ingredients.</p>
<div class="notes">""" + "".join(f'<div class="note"><div class="d">MAGIC REINDEER FOOD</div>{img(ELF, "1.1in")}<div class="m">Oats + bird seed + a pinch of love</div><div class="f">Sprinkle on the lawn on Christmas Eve</div></div>' for _ in range(4)) + f"""</div>
<div class="mini" style="margin-bottom:.12in">Cut out the labels and glue them on small paper bags. Please skip glitter: it can hurt birds and wildlife.</div>
{footer(NAME, "Reindeer food labels")}</div>""")
    pg.append(f'<div class="page">{letter("Goodbye for now!", ["Tonight I fly with Santa’s team, all thanks to your kindness sparkle.", "Thank you for every hug, every smile and every kind thing you did. Keep being kind all year long.", "See you next Christmas!"], "Love forever, your Kindness Reindeer", ELF2)}{footer(NAME, "Goodbye letter")}</div>')
    pg.append(f'<div class="page"><div class="cert">{img(ELF, "1.8in")}<div class="eyebrow">Official North Pole award</div><h2>I Was Kind!</h2><div style="font-size:14pt">This certificate goes to</div><div class="name"></div><div style="font-size:14pt">for 24 days of kindness. Every reindeer at the North Pole is proud of you!</div><div style="margin-top:22px;font-size:12pt;color:#2f5a3c">Date ____________ &nbsp;&nbsp; Signed: Your Kindness Reindeer</div></div>{footer(NAME, "Certificate")}</div>')
    for k in range(2):
        ns = "".join('<div class="note"><div class="d">DAY ___</div><div style="height:.9in;width:100%;border-bottom:1.5px solid #efd2c6"></div><div class="f">♥ your Kindness Reindeer</div></div>' for _ in range(4))
        pg.append(f'<div class="page">{page_head("Your own ideas", "Blank kindness notes", "heart")}<div class="notes">{ns}</div>{footer(NAME, "Blank notes")}</div>')
    ideas = "".join(f"<li>{x}</li>" for x in IDEAS)
    pg.append(f"""<div class="page">{page_head("For grown-ups", "30 more tiny kindness ideas", "star")}
<p class="subtitle">Swap in any of these when a note doesn't fit your day. Keep missions short, concrete and done together.</p>
<ul class="ideas">{ideas}</ul>
<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>Pair it with</h3><div class="mini">Love an elf instead? Our Kindness Elf Kit and Toddler Kindness Elf Kit follow the same 5-minute idea. Find them in our shop.</div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
