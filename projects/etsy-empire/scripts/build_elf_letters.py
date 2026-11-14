#!/usr/bin/env python3
"""Christmas Elf Lifesaver Letters – 30 printable elf letters → termekek/elf-lifesaver-letters/*.html
A Kindness Elf Kit (legjobb listing: 4,7% CTR) rokon terméke. Védjegy: csak „Christmas Elf”, márkanév nélkül."""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "elf-lifesaver-letters"
NAME = "Elf Lifesaver Letters"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

XMAS = """:root{ --dark:#2f6b4f; --sage:#b23a3a; --tint:#f6ece6; --line:#e6cfc6; --accent:#c9a227; --warm:#eef3ec; --warmline:#cfe0d3; --cream:#fdf8f3; }
.lt{ border:2px dashed var(--line); border-radius:16px; padding:14px 18px 10px; margin-bottom:12px; height:2.78in; display:flex; flex-direction:column; background:#fff; position:relative; }
.lt .hd{ display:flex; align-items:center; gap:10px; margin-bottom:6px; }
.lt .hd b{ font-size:14pt; color:var(--sage); }
.lt .hd .tag{ margin-left:auto; font-size:7pt; letter-spacing:.14em; text-transform:uppercase; color:var(--dark); background:var(--warm); border-radius:20px; padding:3px 9px; }
.lt p{ font-size:12.6pt; line-height:1.5; font-family:Georgia,'DejaVu Serif',serif; margin:0 0 4px; color:var(--ink); }
.lt .sig{ margin-top:auto; font-size:11pt; font-family:Georgia,'DejaVu Serif',serif; font-style:italic; display:flex; justify-content:space-between; align-items:flex-end; }
.lt .sig span{ border-bottom:1px solid var(--line); min-width:1.6in; display:inline-block; height:.2in; }
.cv{ background:linear-gradient(180deg,#fdf8f3,#f6ece6); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; }
.cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.idx{ columns:2; column-gap:26px; font-size:9.4pt; } .idx div{ padding:4px 0; border-bottom:1px dotted var(--line); break-inside:avoid; }
"""

L = [  # (cím, címke, szöveg)
 ("Hello, I'm Here!", "Arrival", "I flew all the way from the North Pole to spend December with you! Every morning I'll be somewhere new, so look carefully. I can't wait to see all the kind and helpful things you do. One rule: please don't touch me, so my Christmas magic stays strong."),
 ("I'm Back Again!", "Arrival · returning", "Guess who remembered the way to your house? Me! I missed you all year. You have grown so much. This December I have a special job: to notice every kind thing you do. Let's make it our best Christmas season yet!"),
 ("Sorry, I Was Running Late!", "Lifesaver", "Oops! Last night I was so busy helping Santa sort the wish lists that I didn't have time to find a new spot. Please forgive me. I'll fly extra fast tonight. Thank you for being so patient with a very tired elf!"),
 ("Don't Worry, My Magic Is Fine", "Lifesaver · touched", "Someone touched me by accident, but please don't be sad! Santa says accidents happen and my magic is still strong. A little sprinkle of cinnamon (or a kind word to each other) helps me recharge. I'm okay!"),
 ("I'm Staying Put Today", "Lifesaver · no move", "Today I'm staying right here because I like this spot so much! I can see everything from up here. Tomorrow I'll be back to my hiding adventures. Keep looking for me in the morning!"),
 ("A Snowy Day at the North Pole", "Lifesaver · no move", "There was a big snowstorm at the North Pole last night, so I couldn't fly home to report to Santa. That's why I'm in the same place. The reindeer are digging out the runway. I'll be back on schedule tonight!"),
 ("Elf Rest Day", "Lifesaver", "Even elves need a cozy rest day! Today I'm taking a nap to save my magic for Christmas Eve. Can you be extra quiet and kind to each other so I can recharge? Thank you, sweet friends."),
 ("Someone Is Sick", "Lifesaver · family", "I heard someone in this house isn't feeling well. Today my only job is to send healing hugs and cozy wishes. No hiding games today. Please rest, drink water and get lots of cuddles. Feel better soon!"),
 ("We're Going on a Trip!", "Lifesaver · travel", "I heard you're traveling! Don't worry, elves always know where their families are. I'll keep an eye on you from the North Pole while you're away and I'll be waiting for you when you come home."),
 ("I Brought a Friend", "Fun", "Look who came with me! This is my friend from the North Pole workshop. They wanted to see the kindest family I always talk about. Can you give my friend a name? We'll only stay together for one day."),
 ("Santa's Mid-December Report", "From Santa", "Ho ho ho! Your elf has been sending me wonderful reports. I've heard about your helping hands, your kind words and your patience. Keep going: the most important part of Christmas is being kind to each other."),
 ("A Little Reminder", "Gentle nudge", "I've noticed things have been a bit bumpy lately: some grumpy words and a few squabbles. That's okay, everyone has hard days! Tomorrow, let's try a fresh start. I believe in you. Can you do one kind thing for each person in this house?"),
 ("Sorry About the Mess!", "Lifesaver · oops", "Oh no! I got a little too excited last night and made a mess. Elves aren't always the best at cleaning up. Would you help me tidy up? Teamwork makes the North Pole work!"),
 ("The Kindness Challenge", "Kindness", "Today's mission: do 3 kind things before bedtime. Hold a door, share a toy, say thank you, draw a picture for someone. Draw a star on this note for every kind thing, and I'll tell Santa all about it."),
 ("Thank You for Being Brave", "Feelings", "I saw that today was a little hard, but you were so brave. Being brave doesn't mean you're never scared. It means you keep going. I'm very proud of you, and I told Santa too."),
 ("Welcome, Baby!", "Family", "There is a brand new little person in your family this year! Babies love Christmas lights and gentle voices. Big brothers and sisters are the best helpers in the whole world. Thank you for being so loving."),
 ("I Lost My Hat!", "Fun", "I think I lost my hat somewhere in this house! Can you help me look for it today? If you find it, put it next to me tonight and I'll wear it tomorrow. Elves get cold ears, you know!"),
 ("Bedtime Helper", "Routine", "I heard bedtime has been tricky. Here's an elf secret: the sooner you sleep, the faster Christmas comes! Tonight, try pajamas, teeth, story and lights out without any fuss. I'll be watching and cheering!"),
 ("Try Something New", "Routine", "Elves love trying new things, like new cookie recipes and new ways to wrap presents. Today, can you be brave and try something new? A new food, a new game or a new friend. Tell me how it went!"),
 ("My Favorite Thing About You", "Feelings", "My favorite thing about you is ______________. I noticed it this week and it made my elf heart so happy. Never forget how special you are, especially at Christmas."),
 ("A Letter for Santa", "Fun", "Santa asked me to collect your letters this year! Write or draw what you're wishing for, and also one thing you're thankful for. Leave it next to me tonight and I'll fly it straight to the North Pole."),
 ("Giving Day", "Kindness", "Today is Giving Day! Can you pick one toy you don't play with anymore and give it to a child who needs it? Giving is the best kind of Christmas magic. Santa will be so proud."),
 ("Only One Week Left!", "Countdown", "Can you believe it? Only seven more sleeps until Christmas! The North Pole is so busy: the reindeer are practicing and the cookies are baking. Let's make this the kindest week of all."),
 ("Christmas Eve Goodbye", "Goodbye", "Tonight I fly home with Santa. Thank you for the best December ever: for every kind word, every hug and every helping hand. I'll tell Santa everything. Keep the Christmas magic in your heart all year. See you next year!"),
 ("See You Next Year", "Goodbye", "Merry Christmas! I'm back at the North Pole now, resting my wings. I left a little bit of my magic here with you. Use it to be kind every day until I return next December. Love, your elf"),
 ("Our Elf's Early Goodbye", "Lifesaver · early", "Santa needs extra help at the workshop, so I have to fly home a little early this year. I'm sad to leave, but I'll be watching over you from the North Pole. Thank you for being so wonderful!"),
 ("When You Ask If It's Real", "Big kid letter", "You're growing up, and you have big questions. Here's the truth: the elf was a game we played because we love you. The magic was real, though. It was the kindness, the giving and the joy. Now you can help make the magic for others."),
 ("You're Part of the Magic Now", "Big kid letter", "Now that you know the secret, you have an important job. You can help keep Christmas magic alive for the younger kids in our family. Every kind surprise you give is real Christmas magic. Welcome to the team!"),
 ("Two Elves, One Family", "Siblings", "Your family is so full of kindness that Santa sent me a helper this year! We'll take turns watching and hiding. Please be extra kind to each other, because we'll compare notes every night."),
 ("Blank Letter", "Write your own", "____________________________________________________________ ____________________________________________________________ ____________________________________________________________ ____________________________________________________________"),
]


def letter(t, tag, txt):
    return (f'<div class="lt"><div class="hd">{icon("star",22,"#b23a3a")}<b>{t}</b><span class="tag">{tag}</span></div>'
            f'<p>Dear <span style="border-bottom:1px solid var(--line);display:inline-block;width:1.4in"></span>,</p><p>{txt}</p>'
            f'<div class="sig"><div>{"Love, Santa" if tag == "From Santa" else "Love, your Christmas Elf"}</div><div>Date <span></span></div></div></div>')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#c9a227",1.2)}</div><div class="eyebrow">Printable · No mess · Ages 3–10</div>'
          f'<h1>Elf Lifesaver<br>Letters</h1><div class="tg">30 ready-to-print notes for every December moment: arrivals, goodbyes, the morning you forgot to move it, and the big question "Is it real?"</div>'
          f'<div class="pill">30 letters · US Letter + A4</div></div>']
    idx = "".join(f"<div>{i+1}. {t} <span style='color:var(--soft)'>· {g}</span></div>" for i, (t, g, _) in enumerate(L))
    pg.append(f"""<div class="page">{page_head("Start here", "How to use your elf letters", "book")}
<p class="subtitle">Print the pages, cut along the dashed lines, and keep the stack in a drawer. When a "help!" moment happens, grab the right note, add your child's name and leave it next to your elf. Works with any toy you already have.</p>
<div class="card" style="margin-bottom:12px"><h3>All 30 letters</h3><div class="idx">{idx}</div></div>
<div class="row"><div class="card col"><h3>Printing tips</h3><div class="mini">Print on cream paper or card stock for a "real letter" feel. Write the names with a glitter pen. Fold in half and seal with a sticker.</div></div>
<div class="card warm col"><h3>Good to know</h3><div class="mini">"Christmas Elf" is a generic name for this activity. Not affiliated with any elf doll brand: use any toy you have.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    for i in range(0, len(L), 3):
        pg.append(f'<div class="page" style="padding-top:.55in">{"".join(letter(*x) for x in L[i:i+3])}{footer(NAME, f"Letters {i+1}–{i+3}")}</div>')
    pg.append(f"""<div class="page">{page_head("For grown-ups", "Elf survival plan", "heart")}
<div class="card" style="margin-bottom:12px"><h3>Set a phone alarm</h3><div class="mini">A 9 p.m. "move the elf" reminder saves most mornings. If you still forget, letter #3 or #5 has you covered.</div></div>
<div class="card warm" style="margin-bottom:12px"><h3>Keep it small</h3><div class="mini">Kids remember the letters more than the big setups. A two-line note in a new spot is enough magic.</div></div>
<div class="card" style="margin-bottom:12px"><h3>Plan your "big kid" moment</h3><div class="mini">Letters #27 and #28 turn the end of the elf tradition into a proud promotion: your child becomes a magic-maker for younger siblings.</div></div>
<div class="row" style="margin-top:auto"><div class="card col"><span class="lbl">Our elf's name</span><div class="wline"></div></div><div class="card col"><span class="lbl">Arrival date</span><div class="wline"></div></div><div class="card warm col"><span class="lbl">Goodbye date</span><div class="wline"></div></div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{XMAS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"{SLUG}.html", len(pg), "page")


if __name__ == "__main__":
    main()
