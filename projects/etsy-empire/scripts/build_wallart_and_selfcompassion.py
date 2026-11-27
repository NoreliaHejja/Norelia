#!/usr/bin/env python3
"""Két printable (termekotletek A5 + T3), 2026-11-27:
  christmas-wall-art-set: 3 nyomtatható tipográfiai karácsonyi falikép (cozy vintage), oldalanként 1 kép + használati lap (Letter/A4 PDF-ben, 8x10 arány)
  self-compassion-journal: önegyüttérzés-napló – 30 napos, 16 oldal: hogyan használd, check-in, kedves belső hang, 30 napi lap (2/oldal), SOS-lap, összegzés
  python3 scripts/build_wallart_and_selfcompassion.py [art|journal]"""
import sys
from pathlib import Path
from common import page_head, icon, footer

ROOT = Path(__file__).resolve().parent.parent / "termekek"


def html(name, css, pages, lang="en"):
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>{name}</title><link rel="stylesheet" href="../../assets/base.css"><style>{css}</style></head><body>{"".join(pages)}</body></html>'


SPRIG = '<svg viewBox="0 0 200 60" width="2.4in"><g fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round"><path d="M10 30 H190"/>' + "".join(
    f'<path d="M{x} 30 q8 -14 18 -16 M{x} 30 q8 14 18 16"/>' for x in range(20, 180, 26)) + '</g><circle cx="100" cy="30" r="7" fill="{c2}"/></svg>'
STAR = '<svg viewBox="0 0 40 40" width="{w}"><path d="M20 2l5 12 13 1-10 9 3 13-11-7-11 7 3-13-10-9 13-1z" fill="{c}"/></svg>'


def art():
    slug, name = "christmas-wall-art-set", "Christmas Wall Art Set"
    css = """:root{ --dark:#1f3b2d; --sage:#a83228; --tint:#f6efe4; --line:#e5d6c3; --accent:#c9a04a; --warm:#f3ece1; --warmline:#e3d7c6; --cream:#fbf7f0; }
.art{ background:#f6efe4; align-items:center; justify-content:center; text-align:center; padding:.6in; }
.frame{ border:3px double #c9a04a; flex:1; width:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:.18in; padding:.4in; }
.art h1{ font-family:'DejaVu Serif',serif; font-size:58pt; line-height:1.02; margin:0; letter-spacing:.02em; }
.art .s{ font-family:'DejaVu Serif',serif; font-size:17pt; letter-spacing:.32em; text-transform:uppercase; }
.a1 h1{ color:#a83228 } .a1 .s{ color:#1f3b2d } .a2{ background:#1f3b2d } .a2 .frame{ border-color:#c9a04a } .a2 h1{ color:#f6efe4 } .a2 .s{ color:#c9a04a }
.a3 h1{ color:#1f3b2d } .a3 .s{ color:#a83228 }"""
    pg = [f"""<div class="page">{page_head("Before you print", "How to print your wall art", "book")}
<div class="step"><div class="num">1</div><div><b>Choose your size</b><p>Each print fits 8×10 in, A4, 11×14 in and 5×7 in frames: print at 100% for Letter/A4, or let your print shop scale it (the design keeps its margins).</p></div></div>
<div class="step"><div class="num">2</div><div><b>Choose your paper</b><p>Matte cardstock or photo paper (200–300 g/m²) looks best. For a gallery look, ask a print shop for fine art paper.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Frame and style</b><p>Group all three on a shelf, hang them in a row above the sofa, or tuck one into the tree branches with a clip.</p></div></div>
<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>What's inside</h3><div class="mini">3 prints: "Merry & Bright" (cream and red), "Let It Snow" (forest green and gold), "Joy to the World" (cream and green). Personal use only.</div></div>
{footer(name, "How to print")}</div>"""]
    for cls, h, s, c, c2 in (("a1", "Merry<br>&amp; Bright", "Christmas", "#1f3b2d", "#a83228"), ("a2", "Let It<br>Snow", "Winter wonderland", "#c9a04a", "#f6efe4"), ("a3", "Joy to<br>the World", "Christmas", "#a83228", "#c9a04a")):
        pg.append(f'<div class="page art {cls}"><div class="frame">{STAR.format(w=".5in", c=c2 if cls != "a2" else "#c9a04a")}<h1>{h}</h1>{SPRIG.format(c=c, c2=c2)}<div class="s">{s}</div></div></div>')
    return slug, html(name, css, pg)


def journal():
    slug, name = "self-compassion-journal", "Self-Compassion Journal"
    css = """:root{ --dark:#3d4a5c; --sage:#6a8caf; --tint:#eef3f8; --line:#d6e1ec; --accent:#e0a96d; --warm:#f6f1ea; --warmline:#e6dccf; --cream:#fbfaf7; }
.cv{ background:linear-gradient(180deg,#fbfaf7,#eaf0f6); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--dark); margin:10px 0 6px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; line-height:1.4; }
.cv .pill{ margin-top:18px; background:var(--sage); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.ln{ border-bottom:1.5px solid var(--line); height:.32in; } .box{ border:2px solid var(--line); border-radius:12px; padding:9px 12px; background:#fff; margin-bottom:9px; }
.box h3{ margin:0 0 3px; color:var(--sage); font-size:11.5pt; } .two{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.day{ border:2px solid var(--line); border-radius:14px; padding:10px 12px; margin-bottom:10px; flex:1; } .day b{ color:var(--sage); }
.scale{ display:flex; gap:10px; font-size:10pt; color:#777; margin:4px 0; } .scale span{ width:22px; height:22px; border:1.5px solid var(--sage); border-radius:50%; display:inline-flex; align-items:center; justify-content:center; }"""
    L = lambda n: "".join('<div class="ln"></div>' for _ in range(n))
    pg = [f'<div class="page cv"><div>{icon("heart",100,"#6a8caf",1.2)}</div><div class="eyebrow">Printable journal · 30 days · Undated</div><h1>Be Kind<br>to Yourself</h1>'
          f'<div class="tg">A gentle 30-day self-compassion journal: notice how you feel, talk to yourself like a good friend would, and end each day with one small kindness for you.</div><div class="pill">21 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "How to use this journal", "book")}
<div class="step"><div class="num">1</div><div><b>Five minutes a day</b><p>Pick a time that already exists: with your morning coffee or before you sleep. One page holds two days.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Notice, don't judge</b><p>Write down how you feel and what happened. There are no wrong answers and no grades.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Talk like a friend</b><p>Ask: "What would I say to a good friend in this situation?" Then write that to yourself.</p></div></div>
<div class="step"><div class="num">4</div><div><b>One small kindness</b><p>End the day with one small thing for you: a walk, a glass of water, going to bed on time.</p></div></div>
<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>Please note</h3><div class="mini">This journal is a self-care tool, not therapy or medical advice. If you feel unsafe or overwhelmed, please contact a doctor or a local crisis line (US: call or text 988 · UK: Samaritans 116 123 · EU: 112).</div></div>
{footer(name, "Start here")}</div>""")
    pg.append(f"""<div class="page">{page_head("Day 0", "Where I am right now", "star")}
<div class="box"><h3>Lately I have been feeling…</h3>{L(3)}</div><div class="box"><h3>The things I am hardest on myself about</h3>{L(3)}</div>
<div class="box"><h3>What I would like to feel in 30 days</h3>{L(2)}</div><div class="box"><h3>People and places that make me feel safe</h3>{L(2)}</div>{footer(name, "Day 0")}</div>""")
    pg.append(f"""<div class="page">{page_head("My kind inner voice", "Words I can say to myself", "heart")}
<div class="two"><div class="box"><h3>When I make a mistake</h3><div class="mini">"Everyone makes mistakes. What can I learn, and what do I need now?"</div>{L(2)}</div>
<div class="box"><h3>When I feel not enough</h3><div class="mini">"I am doing my best with what I have today."</div>{L(2)}</div>
<div class="box"><h3>When I feel overwhelmed</h3><div class="mini">"One thing at a time. I don't have to do it all today."</div>{L(2)}</div>
<div class="box"><h3>When I compare myself</h3><div class="mini">"Their path is not my path."</div>{L(2)}</div></div>
<div class="box"><h3>My own kind sentences</h3>{L(5)}</div>{footer(name, "Kind voice")}</div>""")
    for d in range(1, 31, 2):
        days = "".join(f"""<div class="day"><b>Day {k}</b> &nbsp;<span style="color:#999">date ________</span>
<div class="scale">How I feel: <span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></div>
<div class="mini">Something that was hard today</div>{L(1)}<div class="mini">What a good friend would say to me</div>{L(2)}<div class="mini">One small kindness for me</div>{L(1)}</div>""" for k in (d, d + 1))
        pg.append(f'<div class="page">{page_head("Daily page", f"Days {d}–{d + 1}", "calendar")}{days}{footer(name, "Daily")}</div>')
    pg.append(f"""<div class="page">{page_head("For hard days", "My SOS page", "check")}
<div class="box"><h3>Three things that calm me down</h3>{L(3)}</div><div class="box"><h3>People I can call or text</h3>{L(3)}</div>
<div class="box"><h3>A sentence I need to hear</h3>{L(2)}</div><div class="box"><h3>Crisis lines</h3><div class="mini">US: 988 · UK & Ireland: Samaritans 116 123 · Germany: 0800 111 0 111 · Emergency: 911 / 999 / 112</div></div>{footer(name, "SOS")}</div>""")
    pg.append(f"""<div class="page">{page_head("Day 30", "Looking back", "star")}
<div class="box"><h3>What changed in how I talk to myself?</h3>{L(3)}</div><div class="box"><h3>Kind habits I want to keep</h3>{L(3)}</div>
<div class="box"><h3>A letter to myself, from a good friend</h3>{L(7)}</div>{footer(name, "For personal use only · © AureliaVenn")}</div>""")
    return slug, html(name, css, pg)


if __name__ == "__main__":
    for which in (sys.argv[1:] or ["art", "journal"]):
        slug, h = {"art": art, "journal": journal}[which]()
        (ROOT / slug).mkdir(parents=True, exist_ok=True); (ROOT / slug / f"{slug}.html").write_text(h, encoding="utf-8"); print("wrote", slug)
