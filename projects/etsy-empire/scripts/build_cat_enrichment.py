#!/usr/bin/env python3
"""Indoor Cat Enrichment Planner → termekek/cat-enrichment-planner/*.html"""
from pathlib import Path
from common import page_head, icon, footer, cover

SLUG = "cat-enrichment-planner"
NAME = "Happy Indoor Cat"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

CSS = """
.hab{ table-layout:fixed; } .hab th,.hab td{ text-align:center; } .hab th:first-child,.hab td:first-child{ text-align:left; width:1.9in; }
.hab tbody td{ height:0.46in; }
.dot{ width:0.26in; height:0.26in; border:1.5px dashed var(--sage); border-radius:50%; display:inline-block; }
.ideas{ columns:2; column-gap:20px; }
.idea{ break-inside:avoid; display:flex; gap:9px; align-items:flex-start; padding:15px 0; border-bottom:1px dotted var(--line); font-size:9.3pt; }
.idea b{ color:var(--dark); display:block; } .idea span.d{ color:var(--soft); font-size:8pt; }
.kid{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.kc{ display:flex; gap:12px; align-items:center; background:var(--tint); border:1px solid var(--line); border-radius:14px; padding:20px 14px; font-size:11pt; font-weight:600; color:var(--dark); }
.kc .ic{ width:52px; height:52px; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.kc.w{ background:var(--warm); border-color:var(--warmline); }
.prof .wline{ height:.42in; }
.signs .ck{ font-size:9.8pt; padding:11px 0; }
.big td{ height:0.62in; } .wk7 td{ height:0.9in; border-left:1px solid var(--line); } .wk7 td:first-child{ border-left:0; }
"""
IDEAS = [("Wand toy session", "10 min, end with a 'catch'"), ("Treat puzzle", "egg carton or toilet-roll pyramid"), ("Window perch", "bird TV, safely latched"),
         ("Cardboard box fort", "cut two doorways"), ("Paper bag tunnel", "handles cut off"), ("Hide & seek kibble", "5 pieces around a room"),
         ("Scent day", "a new safe smell: a twig, a sock"), ("Ping-pong ball in the bath", "dry tub, endless chase"), ("Scratching post upgrade", "vertical and horizontal"),
         ("Cat grass pot", "grow it together"), ("Shelf highway", "a path up high"), ("Clicker game", "sit, high-five, come"),
         ("Brushing spa", "slow strokes, short sessions"), ("Rotate the toys", "hide half, swap weekly"), ("Bubble chase", "pet-safe bubbles"),
         ("Food-dispensing ball", "for breakfast"), ("Crinkle blanket", "under a towel"), ("Sunny nap spot", "a soft bed by the window"),
         ("Bird feeder outside", "visible from the window"), ("Quiet hour", "lights low, no chasing")]
KID = [("toy", "Wiggle the wand toy slowly"), ("bowl", "Fill the water bowl"), ("heart", "Gentle strokes, head and back"),
       ("calendar", "Hide 3 treats for the cat"), ("star", "Make a paper-ball toy"), ("leaf", "Water the cat grass")]
RULES = [("hug", "Let the cat come to you"), ("moon", "Sleeping cats are not for waking"), ("window", "Cats need a quiet hiding place"), ("check", "Tail flicking? Time to stop")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [cover("Happy Indoor Cat", "A printable enrichment planner for busy families: play, puzzles and calm – plus little jobs for little helpers.",
                "A printable cat care planner", "8 pages · Play plan · 20 ideas · Kid jobs", "cat")]
    sg = ["Overgrooming or bald patches", "Night-time zoomies and yowling", "Scratching furniture, not the post", "Chewing plants or cables",
          "Sleeping much more than usual", "Ambushing ankles"]
    pg.append(f"""<div class="page">{page_head("Start here", "Why indoor cats need a plan", "book")}
<p class="subtitle">Indoor cats are safe, but they still have a hunter's brain. Two short play sessions a day, one puzzle and one cozy high place make a calmer, happier cat – and a calmer home.</p>
<div class="row"><div class="card col signs"><h3>Signs of a bored cat</h3>{''.join(f'<div class="ck"><span class="chk"></span>{x}</div>' for x in sg)}</div>
<div class="card warm col"><h3>The simple formula</h3><div class="step"><div class="num">1</div><div><b>Hunt</b><p>Wand toy, stalk, chase, catch.</p></div></div><div class="step"><div class="num">2</div><div><b>Eat</b><p>A treat or meal right after play.</p></div></div><div class="step"><div class="num">3</div><div><b>Groom &amp; sleep</b><p>Leave them to rest in peace.</p></div></div></div></div>
<div class="card" style="margin-top:14px"><h3>Safe-home checklist</h3>{''.join(f'<div class="ck"><span class="chk"></span>{x}</div>' for x in ["Window screens or safe latches","Toxic plants out of reach (lilies!)","Cords and hair ties tidied away","A hiding spot in every main room"])}</div>
<div class="card" style="margin-top:auto"><h3>Good to know</h3><div class="mini">This planner is for everyday care and fun – not veterinary advice. A sudden change in behaviour, appetite or litter habits is a reason to call your vet.</div></div>
{footer(NAME, "Start here")}</div>""")
    pg.append(f"""<div class="page">{page_head("Get to know your cat", "Cat Profile", "cat")}
<div class="row prof"><div class="card col"><span class="lbl">Name</span><div class="wline"></div><span class="lbl" style="margin-top:8px">Birthday / gotcha day</span><div class="wline"></div><span class="lbl" style="margin-top:8px">Vet &amp; phone</span><div class="wline"></div></div>
<div class="card col" style="display:flex;align-items:flex-end;justify-content:center;border-style:dashed;min-height:2.2in"><span class="mini">photo or drawing</span></div></div>
<div class="row prof" style="margin-top:12px"><div class="card col"><h3>Favorite toys</h3><div class="wline"></div><div class="wline"></div><div class="wline"></div></div><div class="card warm col"><h3>Does NOT like</h3><div class="wline"></div><div class="wline"></div><div class="wline"></div></div></div>
<div class="row prof" style="margin-top:12px"><div class="card col"><h3>Favorite treats</h3><div class="wline"></div><div class="wline"></div><div class="wline"></div></div><div class="card col"><h3>Best nap spots</h3><div class="wline"></div><div class="wline"></div><div class="wline"></div></div></div>
<div class="card warm" style="margin-top:12px"><h3>Funny habits &amp; little quirks</h3><div class="wline"></div><div class="wline"></div><div class="wline"></div></div>
{footer(NAME, "Cat profile")}</div>""")
    rows = [("Morning play", "toy"), ("Evening play", "toy"), ("Puzzle / hunt game", "star"), ("Fresh water", "bowl"), ("Litter scooped", "check"), ("Brushing", "heart"), ("New toy or scent", "leaf")]
    tb = "".join(f'<tr><td><span style="display:inline-flex;align-items:center;gap:7px;font-weight:600;color:var(--dark)">{icon(i,16)}{t}</span></td>' + "".join('<td><span class="dot"></span></td>' for _ in DAYS) + "</tr>" for t, i in rows)
    week = lambda n: f'<div class="eyebrow" style="margin:8px 0 6px">Week {n}</div><table class="hab"><thead><tr><th>Daily</th>' + "".join(f"<th>{d}</th>" for d in DAYS) + f"</tr></thead><tbody>{tb}</tbody></table>"
    pg.append(f"""<div class="page">{page_head("Two weeks at a glance", "Play &amp; Care Tracker", "calendar")}{week(1)}{week(2)}{footer(NAME, "Tracker")}</div>""")
    ide = "".join(f'<div class="idea"><span class="chk" style="margin-top:2px"></span><span><b>{t}</b><span class="d">{d}</span></span></div>' for t, d in IDEAS)
    pg.append(f"""<div class="page">{page_head("Try one a day", "20 Enrichment Ideas", "star")}<p class="subtitle">Tick the ones your cat loves. Most cost nothing but a cardboard box and five minutes.</p><div class="ideas">{ide}</div>{footer(NAME, "Ideas")}</div>""")
    kd = "".join(f'<div class="kc"><span class="ic">{icon(i,24)}</span>{t}</div>' for i, t in KID)
    rl = "".join(f'<div class="kc w"><span class="ic">{icon(i,24)}</span>{t}</div>' for i, t in RULES)
    pg.append(f"""<div class="page">{page_head("For little hands, ages 3+", "Little Cat Helper", "child")}
<p class="subtitle">Read together, then let your child pick one job a day. Always with a grown-up nearby.</p>
<div class="eyebrow" style="margin-bottom:8px">My cat jobs</div><div class="kid">{kd}</div>
<div class="eyebrow" style="margin:16px 0 8px">Gentle cat rules</div><div class="kid">{rl}</div>
<div class="card" style="margin-top:auto"><span class="lbl">Today I helped by…</span><div class="wline"></div></div>
{footer(NAME, "Little helper")}</div>""")
    lr = "".join("<tr><td></td><td></td><td></td><td></td></tr>" for _ in range(11))
    pg.append(f"""<div class="page">{page_head("Keep an eye on things", "Weight &amp; Vet Log", "scale")}
<table class="big"><thead><tr><th>Date</th><th>Weight</th><th>Vet / vaccine / treatment</th><th>Notes</th></tr></thead><tbody>{lr}</tbody></table>
<div class="row" style="margin-top:14px"><div class="card col"><span class="lbl">Food brand &amp; daily amount</span><div class="wline"></div></div><div class="card warm col"><span class="lbl">Next vet visit</span><div class="wline"></div></div></div>
{footer(NAME, "Weight & vet log")}</div>""")
    pg.append(f"""<div class="page">{page_head("Make it yours", "Our Cat's Happy Week", "heart")}
<p class="subtitle">Plan the week's enrichment on Sunday. One idea per day is plenty.</p>
<table class="wk7"><thead><tr><th style="width:1.1in">Day</th><th>Play idea</th><th>Puzzle / treat</th><th>Who helps?</th></tr></thead><tbody>{''.join(f'<tr><td>{d}</td><td></td><td></td><td></td></tr>' for d in DAYS)}</tbody></table>
<div class="card warm" style="margin-top:14px"><h3>This week our cat loved…</h3><div class="wline"></div><div class="wline"></div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME} Planner</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"{SLUG}.html")


if __name__ == "__main__":
    main()
