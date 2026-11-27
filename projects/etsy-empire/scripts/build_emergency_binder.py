#!/usr/bin/env python3
"""Family Emergency Binder with Pet & Kids Pages – nyomtatható családi vészhelyzeti terv (2026-11-18, P1, Nóra könyvpiaci kutatása).
Tervező, nem orvosi/vészhelyzeti tanács. Készletlista: Ready.gov „Build a Kit” alapján (közkincs), saját szöveggel. → termekek/emergency-binder/"""
from pathlib import Path
from common import page_head, icon, footer

SLUG = "emergency-binder"
NAME = "Family Emergency Binder"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG

CSS = """:root{ --dark:#1f4e5f; --sage:#c8423b; --tint:#eef5f6; --line:#cfdfe3; --accent:#e8a33d; --warm:#fff4e6; --warmline:#f2d3a8; --cream:#fbfaf7; }
.cv{ background:linear-gradient(180deg,#fbfaf7,#eef5f6); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--dark); margin:10px 0 4px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.8in; line-height:1.4; }
.cv .pill{ margin-top:22px; background:var(--sage); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.ln{ border-bottom:1.5px solid var(--line); height:.34in; }
.box{ border:2px solid var(--line); border-radius:14px; padding:10px 14px; background:#fff; margin-bottom:10px; }
.box h3{ margin:0 0 4px; color:var(--sage); font-size:12.5pt; }
.f{ display:grid; grid-template-columns:auto 1fr; gap:4px 10px; align-items:end; font-size:10.5pt; } .f i{ font-style:normal; font-weight:600; color:var(--dark); white-space:nowrap; } .f u{ text-decoration:none; border-bottom:1.5px solid var(--line); height:.3in; }
table.t{ width:100%; border-collapse:collapse; font-size:9.5pt; } table.t th{ background:var(--dark); color:#fff; padding:5px 6px; text-align:left; font-weight:600; } table.t td{ border:1.5px solid var(--line); height:.36in; }
.tick{ display:flex; gap:8px; align-items:center; font-size:10.5pt; margin:4px 0; } .tick em{ font-style:normal; flex:1; min-width:0; } .tick span{ width:15px; height:15px; border:2px solid var(--dark); border-radius:4px; flex:0 0 auto; }
.two{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }
.kit{ display:grid; grid-template-columns:1fr 1fr; gap:0 18px; }
.cards{ display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:10px; }
.wc{ border:2px dashed var(--sage); border-radius:14px; padding:10px 12px; background:#fff; font-size:10pt; }
.wc b{ color:var(--sage); font-size:12pt; display:block; margin-bottom:4px; }
.wc .f u{ height:.26in; }
.note{ font-size:8.5pt; color:#555; margin-top:auto; margin-bottom:.12in; line-height:1.4; }
"""

KIT = ["Water: 1 gallon per person per day, for several days", "Non-perishable food for several days", "Manual can opener",
       "Flashlight + extra batteries", "Battery or hand-crank radio", "First aid kit", "Prescription medicines (7-day supply)",
       "Glasses / contact lens supplies", "Whistle to signal for help", "Dust masks", "Moist towelettes, garbage bags",
       "Wrench or pliers to turn off utilities", "Phone chargers + power bank", "Cash in small bills", "Copies of important documents",
       "Local paper maps", "Change of clothes + sturdy shoes", "Blankets or sleeping bags", "Baby supplies (formula, diapers)",
       "Pet food, water and leash (see pet page)", "Matches in a waterproof container", "Fire extinguisher (know where it is)"]
PETKIT = ["Food and water for several days", "Bowls and can opener", "Leash, harness or carrier", "Medicines + copy of vaccine records",
          "Recent photo of you with your pet", "Litter box / poop bags", "Favorite toy or blanket"]
DOCS = ["ID cards / driver's licenses", "Passports", "Birth certificates", "Insurance policies (home, car, health, pet)",
        "Medical records + prescriptions", "Property deed / lease", "Bank and credit card contacts", "Pet microchip + vet records"]


def f(*labels):
    return '<div class="f">' + "".join(f"<i>{x}</i><u></u>" for x in labels) + "</div>"


def ticks(items):
    return "".join(f'<div class="tick"><span></span><em>{x}</em></div>' for x in items)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div>{icon("check",110,"#c8423b",1.2)}</div><div class="eyebrow">Printable planner · Families with kids and pets</div>'
          f'<h1>Family Emergency<br>Binder</h1><div class="tg">One calm place for everything you need when it matters: contacts, medical info, your family plan, a 72-hour kit checklist, pet pages and wallet cards for kids.</div>'
          f'<div class="pill">8 pages · fillable by hand · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to use your binder", "book")}
<p class="subtitle">Nobody likes to think about emergencies. That is exactly why a plan helps: when you already wrote it down, you do not have to think in a stressful moment. Set aside one evening.</p>
<div class="step"><div class="num">1</div><div><b>Fill it in together</b><p>Write in pencil so you can update it. Older kids can help with their own pages.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Keep it where you can grab it</b><p>Put the binder near your front door or with your emergency kit. Take a photo of each page so you also have it on your phone.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Practice once, twice a year</b><p>Walk to your meeting places with the kids. Check the kit, swap old water and batteries, update medicines and phone numbers.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Cut out the kids' cards</b><p>Fill in one wallet card per child and put it in their backpack.</p></div></div>
<div class="row" style="margin-top:auto"><div class="card col"><h3>Planning aid only</h3><div class="mini">This binder helps you organize information. It is not medical, legal or emergency advice. In an emergency call 911 (US) or 112 (EU). For official guidance see Ready.gov or your local emergency management office.</div></div>
<div class="card warm col"><h3>Keep it private</h3><div class="mini">Your binder holds personal data. Store it somewhere safe and shred old pages when you update.</div></div></div>
{footer(NAME, "Start here")}</div>""")
    rows = "".join("<tr><td></td><td></td><td></td><td></td><td></td></tr>" for _ in range(5))
    pg.append(f"""<div class="page">{page_head("Who we are", "Family contacts + medical info", "heart")}
<table class="t"><tr><th>Name</th><th>Birth date</th><th>Allergies</th><th>Medicines</th><th>Doctor / phone</th></tr>{rows}</table>
<div class="two" style="margin-top:12px"><div class="box"><h3>Emergency contacts</h3>{f("Out-of-area contact","Phone","Neighbor","Phone","Relative nearby","Phone")}</div>
<div class="box"><h3>Important numbers</h3>{f("School / daycare","Work (parent 1)","Work (parent 2)","Pediatrician","Vet","Insurance")}</div></div>
<div class="box"><h3>Health notes (conditions, devices, special needs)</h3><div class="ln"></div><div class="ln"></div></div>
{footer(NAME, "Contacts")}</div>""")
    pg.append(f"""<div class="page">{page_head("Our plan", "Family emergency plan", "calendar")}
<div class="two"><div class="box"><h3>Where we meet</h3>{f("Near home (e.g. big tree)","Outside our neighborhood","If we cannot go home")}</div>
<div class="box"><h3>How we reach each other</h3>{f("Out-of-area contact","Group chat / app","If phones are down")}</div></div>
<div class="box"><h3>How we leave the house</h3>{f("Main exit","Second exit","Evacuation route by car","Where the car keys are")}</div>
<div class="box"><h3>Where things are</h3>{f("Water shut-off","Gas shut-off","Electrical panel","Emergency kit","This binder","Spare keys")}</div>
<div class="box"><h3>Who picks up the kids if we can't</h3>{f("Name","Phone","School knows? (yes / no)")}</div>
{footer(NAME, "Plan")}</div>""")
    pg.append(f"""<div class="page">{page_head("Grab and go", "72-hour emergency kit checklist", "check")}
<p class="subtitle">Tick what you have, circle what you still need. Check the kit twice a year and replace water, food and batteries.</p>
<div class="kit">{ticks(KIT)}</div>
<div class="box" style="margin-top:10px"><h3>Our extras</h3><div class="ln"></div><div class="ln"></div></div>
<div class="note">Checklist based on the basic disaster supplies kit recommended at Ready.gov. Adapt it to your family, climate and needs.</div>
{footer(NAME, "Kit")}</div>""")
    pet = '<div class="box"><h3>Pet profile</h3>' + f("Name", "Species / breed", "Microchip number", "Vet + phone", "Medicines", "Food + amount") + "</div>"
    pg.append(f"""<div class="page">{page_head("Furry family members", "Pet emergency page", "cat")}
<div class="two">{pet}{pet}</div>
<div class="box"><h3>Pet go-bag</h3><div class="kit">{ticks(PETKIT)}</div></div>
<div class="box"><h3>Pet-friendly places to stay (hotels, friends, boarding)</h3><div class="ln"></div><div class="ln"></div></div>
<div class="note">Planning aid, not veterinary advice.</div>
{footer(NAME, "Pets")}</div>""")
    card = ('<div class="wc"><b>My emergency card</b>' + f("My name", "My grown-up", "Phone", "Second phone", "Our meeting place") +
            '<div style="margin-top:6px;font-weight:700;color:#c8423b">In an emergency: 911 (US) · 112 (EU)</div></div>')
    pg.append(f"""<div class="page">{page_head("For kids", "My emergency cards", "child")}
<p class="subtitle">Cut out one card per child, fill it in together and keep it in the backpack. Practice saying the phone number out loud.</p>
<div class="cards">{card * 4}</div>
<div class="box"><h3>I know what to do (color a star when you practiced)</h3>
{ticks(["I know our meeting place near home", "I know my grown-up's phone number", "I know how to call for help", "I know where the flashlight is", "We practiced our fire drill"])}</div>
{footer(NAME, "Kids")}</div>""")
    log = "".join("<tr><td></td><td></td><td></td></tr>" for _ in range(4))
    pg.append(f"""<div class="page">{page_head("Keep it current", "Documents + review log", "book")}
<div class="box"><h3>Where our important documents are</h3><div class="kit">{ticks(DOCS)}</div>{f("Originals kept at","Copies kept at")}</div>
<table class="t"><tr><th>Date reviewed</th><th>What we updated</th><th>Next review</th></tr>{log}</table>
<div class="card warm" style="margin-top:12px;margin-bottom:.15in"><h3>You did it</h3><div class="mini">One evening of planning gives your family a calmer response when something unexpected happens. Review it every six months, for example when the clocks change.</div></div>
{footer(NAME, "For personal use only · © AureliaVenn")}</div>""")
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8")
    print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
