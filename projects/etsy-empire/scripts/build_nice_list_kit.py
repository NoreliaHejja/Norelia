#!/usr/bin/env python3
"""Santa's Nice List Kit – Nice List oklevél, levél a Mikulástól, szarvas-eledel címke + recept, kedvesség-lista, boríték-címke
→ termekek/santas-nice-list-kit/  (a név kézzel írható; nincs védjegy)."""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "santas-nice-list-kit"
NAME = "Santa's Nice List Kit"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """:root{ --dark:#2f6b4f; --sage:#b23a3a; --tint:#f6ece6; --line:#e6cfc6; --accent:#c9a227; --warm:#eef3ec; --warmline:#cfe0d3; --cream:#fdf8f3; }
.cv{ background:linear-gradient(180deg,#fdf8f3,#f6ece6); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:42pt; color:var(--sage); margin:10px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.cert{ border:8px double var(--accent); border-radius:24px; flex:1; margin-bottom:.15in; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:.45in; background:#fff; }
.cert .k{ font-size:12pt; letter-spacing:.25em; text-transform:uppercase; color:var(--dark); font-weight:700; }
.cert h2{ font-size:40pt; color:var(--sage); margin:10px 0 6px; line-height:1.05; } .cert p{ font-size:14pt; line-height:1.55; max-width:5.4in; margin:6px 0; }
.cert .ln{ width:4.4in; border-bottom:2px solid var(--dark); height:.6in; margin:4px auto 10px; }
.cert .sig{ display:flex; gap:.6in; margin-top:16px; } .cert .sig div{ border-top:2px solid var(--dark); width:2in; padding-top:4px; font-size:10pt; color:var(--dark); }
.cert.green{ border-color:var(--dark); } .cert.green h2{ color:var(--dark); }
.letter{ flex:1; margin-bottom:.15in; background:#fff; border:2px solid var(--line); border-radius:18px; padding:.45in .55in; display:flex; flex-direction:column; }
.letter .hd{ text-align:center; color:var(--sage); font-size:22pt; font-weight:800; margin-bottom:4px; } .letter .sub{ text-align:center; font-size:10pt; letter-spacing:.2em; color:var(--dark); text-transform:uppercase; margin-bottom:18px; }
.letter p{ font-size:13.4pt; line-height:1.65; margin:0 0 12px; } .letter .blank{ display:inline-block; min-width:1.9in; border-bottom:1.5px solid var(--dark); }
.letter .end{ margin-top:auto; font-size:13pt; }
.list{ flex:1; margin-bottom:.15in; background:#fff; border:2px solid var(--line); border-radius:18px; padding:.35in .45in; }
.list .row{ display:flex; align-items:center; gap:12px; font-size:13.5pt; padding:9px 0; border-bottom:1px dashed var(--line); } .list .row span{ width:22px; height:22px; border:2px solid var(--sage); border-radius:6px; flex:0 0 auto; }
.tags{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:repeat(3,1fr); gap:12px; flex:1; margin-bottom:.1in; }
.tags div{ border:2px dashed var(--sage); border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:10px; background:#fff; }
.tags b{ font-size:19pt; color:var(--sage); line-height:1.1; } .tags span{ font-size:10.5pt; color:var(--dark); margin-top:6px; line-height:1.35; }
.tags div:nth-child(even){ border-color:var(--dark); } .tags div:nth-child(even) b{ color:var(--dark); }
.env{ display:grid; grid-template-rows:repeat(3,1fr); gap:14px; flex:1; margin-bottom:.1in; }
.env div{ border:2px dashed var(--line); border-radius:14px; padding:14px 20px; background:#fff; display:flex; flex-direction:column; justify-content:center; }
.env b{ font-size:16pt; color:var(--sage); } .env i{ font-style:normal; font-size:12pt; color:var(--dark); margin-top:8px; border-bottom:1.5px solid var(--line); padding-bottom:6px; }
"""

GOOD = ["Shared toys with a friend or sibling", "Helped at home without being asked", "Said please and thank you", "Was kind to someone who felt sad",
        "Tried something hard and didn't give up", "Told the truth, even when it was tricky", "Helped tidy up after playing",
        "Was gentle with pets and little ones", "Made someone smile", "Listened to grown-ups (most of the time!)"]
TAGS = [("Magic Reindeer Food", "Sprinkle on the lawn on Christmas Eve so the reindeer can find your house."),
        ("Reindeer Snack", "For Dasher, Dancer and all their friends. Sprinkle outside before bed."),
        ("Magic Reindeer Food", "Sprinkle on the lawn on Christmas Eve so the reindeer can find your house."),
        ("Reindeer Snack", "For Dasher, Dancer and all their friends. Sprinkle outside before bed."),
        ("Magic Reindeer Food", "Sprinkle on the lawn on Christmas Eve so the reindeer can find your house."),
        ("Reindeer Snack", "For Dasher, Dancer and all their friends. Sprinkle outside before bed.")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("star",110,"#c9a227",1.2)}</div><div class="eyebrow">Printable · Christmas Eve magic · Ages 2–10</div>'
          f'<h1>Santa\'s<br>Nice List Kit</h1><div class="tg">An official Nice List certificate, a letter from Santa, a "good things I did this year" list, reindeer food tags and a special delivery envelope label. Just write your child\'s name.</div>'
          f'<div class="pill">10 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to use your kit", "book")}
<p class="subtitle">A little Christmas Eve magic that takes ten minutes to set up and gets talked about all year.</p>
<div class="step"><div class="num">1</div><div><b>Print on card stock</b><p>Certificates look best on thick white or cream paper. Write the names with a gold or red pen.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Fill in the good-things list together</b><p>A few days before Christmas, sit down with your child and tick the kind things they did this year. Add their own ideas on the blank lines.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Deliver the letter</b><p>Fill in the blanks of Santa's letter, fold it into the envelope with the special delivery label and leave it by the tree or the stockings.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Feed the reindeer</b><p>Mix oats with a pinch of colored sugar, fill small bags and tie on a reindeer food tag. Sprinkle outside on Christmas Eve.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Two certificate styles</h3><div class="mini">A red and gold version and a green version – one per child, or keep one for next year.</div></div>
<div class="card warm col"><h3>Reindeer food tip</h3><div class="mini">Use oats and colored sugar only – no glitter, so it is safe for birds and animals outside.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    for cls in ("", "green"):
        pg.append(f"""<div class="page" style="padding-top:.5in"><div class="cert {cls}"><div class="k">Official Certificate</div>{icon("star",64,"#c9a227",1.2)}<h2>Santa's Nice List</h2>
<p>This certifies that</p><div class="ln"></div><p>has been checked twice and found to be <b>NICE</b> this year,<br>for kindness, helping and a very big heart.</p>
<p style="font-size:12pt;color:#2f6b4f">Year: __________ &nbsp;&nbsp; North Pole Approval No. ______</p>
<div class="sig"><div>Santa Claus</div><div>Head Elf</div></div></div>{footer(NAME, "Certificate")}</div>""")
    pg.append(f"""<div class="page" style="padding-top:.5in"><div class="letter"><div class="hd">A Letter from Santa</div><div class="sub">Special delivery · North Pole</div>
<p>Dear <span class="blank"></span>,</p>
<p>The elves and I have been watching all year, and I have wonderful news: your name is on my Nice List! I heard about the time you <span class="blank" style="min-width:3.4in"></span>, and it made my whole workshop smile.</p>
<p>I know this year was not always easy. You kept trying, you were kind to others, and you helped your family. That is exactly what makes Christmas magic.</p>
<p>My reindeer are practicing their landings, and Mrs. Claus is baking cookies for the long ride. Please remember to keep being kind, even after Christmas is over.</p>
<p>See you very soon (but only when you are fast asleep!),</p>
<div class="end">Love,<br><b style="font-size:20pt;color:#b23a3a">Santa</b><br><span style="font-size:10.5pt">P.S. Rudolph says hello to <span class="blank" style="min-width:1.6in"></span>.</span></div></div>{footer(NAME, "Letter from Santa")}</div>""")
    rows = "".join(f'<div class="row"><span></span>{g}</div>' for g in GOOD) + "".join('<div class="row"><span></span><i style="flex:1;border-bottom:1.5px solid #e6cfc6;height:20px"></i></div>' for _ in range(3))
    pg.append(f'<div class="page">{page_head("For the Nice List", "Good things I did this year", "check")}<p class="subtitle">Name: ____________________ &nbsp; Tick everything you did, then add your own!</p><div class="list">{rows}</div>{footer(NAME, "Nice list checklist")}</div>')
    tg = "".join(f'<div>{icon("star",30,"#c9a227")}<b>{a}</b><span>{b}</span></div>' for a, b in TAGS)
    pg.append(f'<div class="page">{page_head("Cut, punch a hole, tie on a bag", "Reindeer food tags", "star")}<div class="tags">{tg}</div>{footer(NAME, "Reindeer food tags")}</div>')
    pg.append(f"""<div class="page">{page_head("Christmas Eve", "Magic reindeer food recipe", "heart")}
<div class="card" style="margin-bottom:14px"><h3>You need</h3><div class="mini">1 cup rolled oats · 2 tablespoons colored sugar (red or green) · small bags or jars · the tags from the previous page</div></div>
<div class="step"><div class="num">1</div><div><b>Mix</b><p>Stir the oats and sugar together in a big bowl. Let your child do the stirring and the "magic words".</p></div></div>
<div class="step"><div class="num">2</div><div><b>Fill and tag</b><p>Spoon the mix into small bags, tie with ribbon and add a tag. Great for siblings, cousins and classmates too.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Sprinkle</b><p>Right before bed on Christmas Eve, sprinkle a handful on the lawn or balcony. The moonlight makes it sparkle for the reindeer.</p></div></div>
<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>Please note</h3><div class="mini">No glitter, please – it is not safe for birds and animals. Oats and sugar only.</div></div>
{footer(NAME, "Recipe")}</div>""")
    env = "".join(f'<div><b>Special Delivery from the North Pole</b><i>To: </i><i>Delivered by: Santa\'s Reindeer Post · Priority Sleigh Mail</i></div>' for _ in range(3))
    pg.append(f'<div class="page">{page_head("Cut and glue on an envelope", "Special delivery labels", "book")}<div class="env">{env}</div>{footer(NAME, "Envelope labels")}</div>')
    pg.append(f"""<div class="page" style="padding-top:.5in"><div class="cert green"><div class="k">Santa's Elf Report</div>{icon("heart",60,"#b23a3a",1.2)}<h2>Kindness Award</h2>
<p>Presented to</p><div class="ln"></div><p>for the kindest thing the elves saw this year:</p><div class="ln" style="width:5in;height:.5in"></div><div class="ln" style="width:5in;height:.5in"></div>
<div class="sig"><div>Elf on duty</div><div>Date</div></div></div>{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
