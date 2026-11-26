#!/usr/bin/env python3
"""Két printable (termekotletek A3 + T2):
  christmas-gift-tags-printable: 60 karácsonyi ajándékcímke, 5 stílus × 12, To/From mezővel + vágási útmutató (7 oldal)
  reading-journal-printable: olvasónapló – célok, 52 könyves tracker, havi napló, 8 könyvértékelő oldal, TBR, idézetek, év végi összegzés (16 oldal)
  python3 scripts/build_gift_tags_and_reading_journal.py [tags|journal]"""
import sys
from pathlib import Path
from common import page_head, icon, footer

ROOT = Path(__file__).resolve().parent.parent / "termekek"


def html(name, css, pages, lang="en"):
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>{name}</title><link rel="stylesheet" href="../../assets/base.css"><style>{css}</style></head><body>{"".join(pages)}</body></html>'


def tags():
    slug, name = "christmas-gift-tags-printable", "Christmas Gift Tags Printable"
    css = """:root{ --dark:#1f4d3a; --sage:#b8322a; --tint:#fdf1ee; --line:#efd2c6; --accent:#d9a441; --warm:#eef6ef; --warmline:#cfe3d2; --cream:#fffaf3; }
.cv{ background:linear-gradient(180deg,#fffaf3,#fdeee6); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:40pt; color:var(--sage); margin:10px 0 6px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; }
.cv .pill{ margin-top:18px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.tags{ display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(4,1fr); gap:10px; flex:1; margin-bottom:.12in; }
.tag{ border:1.5px dashed #999; border-radius:14px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px; position:relative; padding:8px; }
.tag .hole{ position:absolute; top:8px; width:12px; height:12px; border-radius:50%; border:1.5px solid #999; }
.tag .t{ font-size:15pt; font-weight:700; } .tag .ln{ width:85%; border-bottom:1.2px solid currentColor; height:.24in; font-size:9pt; text-align:left; opacity:.85; }
.s1{ background:#b8322a; color:#fff; } .s2{ background:#fff; color:#1f4d3a; border-color:#1f4d3a; } .s3{ background:#1f4d3a; color:#fff; }
.s4{ background:#fbecd0; color:#8a5a12; } .s5{ background:#eaf1f8; color:#2c4a6e; }"""
    styles = [("s1", "Merry Christmas", "#ffffff", "star"), ("s2", "Ho Ho Ho", "#b8322a", "heart"), ("s3", "Season's Greetings", "#d9a441", "star"),
              ("s4", "Joy & Love", "#b8322a", "heart"), ("s5", "Let It Snow", "#2c4a6e", "star")]
    pg = [f'<div class="page cv"><div>{icon("star",110,"#d9a441",1.2)}</div><div class="eyebrow">Printable gift tags · Instant download</div><h1>Christmas<br>Gift Tags</h1>'
          f'<div class="tg">60 ready-to-print tags in 5 cheerful styles, each with a To / From line. Print, cut, punch and tie.</div><div class="pill">60 tags · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Before you print", "How to use your tags", "book")}
<div class="step"><div class="num">1</div><div><b>Print</b><p>Use cardstock (160–250 g/m²) for sturdy tags, or plain paper for a quick fix. Print at 100% scale.</p></div></div>
<div class="step"><div class="num">2</div><div><b>Cut</b><p>Cut along the dashed lines with scissors or a paper trimmer. Rounded corners are optional.</p></div></div>
<div class="step"><div class="num">3</div><div><b>Punch and tie</b><p>Punch the small circle with a hole punch and tie with ribbon, twine or yarn.</p></div></div>
<div class="step"><div class="num">4</div><div><b>Write</b><p>Fill in the To / From lines with a felt-tip pen. On dark tags, a white gel pen looks lovely.</p></div></div>
<div class="card warm" style="margin-top:auto;margin-bottom:.15in"><h3>Ink saver</h3><div class="mini">The light styles (Ho Ho Ho, Joy & Love, Let It Snow) use far less ink than the full-colour red and green ones.</div></div>
{footer(name, "How to use")}</div>""")
    for cls, title, ic_col, ic in styles:
        t = "".join(f'<div class="tag {cls}"><div class="hole"></div>{icon(ic, 26, ic_col, 1.6)}<div class="t">{title}</div><div class="ln">To:</div><div class="ln">From:</div></div>' for _ in range(12))
        pg.append(f'<div class="page">{page_head("Cut along the dashed lines", f"{title} · 12 tags", "star")}<div class="tags">{t}</div>{footer(name, title)}</div>')
    return slug, html(name, css, pg)


def journal():
    slug, name = "reading-journal-printable", "Reading Journal Printable"
    css = """:root{ --dark:#3b3a5c; --sage:#7a5c9e; --tint:#f4effa; --line:#dfd3ec; --accent:#d9a441; --warm:#f7f4fb; --warmline:#e3daee; --cream:#fcfaff; }
.cv{ background:linear-gradient(180deg,#fcfaff,#efe6f7); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:42pt; color:var(--sage); margin:10px 0 6px; line-height:1.05; } .cv .tg{ font-size:13pt; color:var(--dark); max-width:5.6in; }
.cv .pill{ margin-top:18px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:11pt; }
.ln{ border-bottom:1.5px solid var(--line); height:.34in; } .box{ border:2px solid var(--line); border-radius:12px; padding:10px 12px; background:#fff; margin-bottom:10px; }
.box h3{ margin:0 0 4px; color:var(--sage); font-size:12pt; } .two{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.books{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; flex:1; margin-bottom:.1in; }
.books div{ border:1.5px solid var(--line); border-radius:8px; font-size:8.5pt; color:#999; padding:4px 6px; display:flex; flex-direction:column; justify-content:space-between; }
.stars{ font-size:16pt; color:var(--accent); letter-spacing:4px; } table.log{ width:100%; border-collapse:collapse; font-size:9.5pt; } table.log th{ background:var(--tint); color:var(--dark); }
table.log td, table.log th{ border:1.2px solid var(--line); height:.36in; padding:2px 5px; text-align:left; }"""
    L = lambda n: "".join('<div class="ln"></div>' for _ in range(n))
    pg = [f'<div class="page cv"><div>{icon("book",110,"#7a5c9e",1.2)}</div><div class="eyebrow">Printable book journal · 2027 or any year</div><h1>My Reading<br>Journal</h1>'
          f'<div class="tg">Track every book, remember what you loved and see your reading year at a glance: goals, a 52-book tracker, monthly logs, review pages and a year in books.</div><div class="pill">15 pages · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Start here", "My reading goals", "star")}
<div class="two"><div class="box"><h3>Books I want to read this year</h3><div class="stars" style="font-size:30pt">____</div></div><div class="box"><h3>Genres I want to try</h3>{L(2)}</div></div>
<div class="box"><h3>Why I want to read more</h3>{L(3)}</div><div class="box"><h3>Authors on my list</h3>{L(3)}</div>
<div class="box"><h3>My reading habit (when, where, how long)</h3>{L(3)}</div>{footer(name, "Goals")}</div>""")
    cells = "".join(f'<div><span>{i}</span><span>______________</span></div>' for i in range(1, 53))
    pg.append(f'<div class="page">{page_head("Colour one in for every book", "52 books tracker", "check")}<div class="books">{cells}</div>{footer(name, "Tracker")}</div>')
    rows = "".join("<tr><td></td><td></td><td></td><td></td><td></td></tr>" for _ in range(14))
    for half in ("January – June", "July – December"):
        pg.append(f'<div class="page">{page_head("Monthly reading log", half, "calendar")}<table class="log"><tr><th>Month</th><th>Title</th><th>Author</th><th>Pages</th><th>★</th></tr>{rows}{rows[:len(rows)//2]}</table>{footer(name, "Log")}</div>')
    for k in range(8):
        pg.append(f"""<div class="page">{page_head(f"Book review {k + 1}", "What I read", "book")}
<div class="two"><div class="box"><h3>Title</h3>{L(1)}<h3>Author</h3>{L(1)}</div><div class="box"><h3>Started · Finished</h3>{L(1)}<h3>Rating</h3><div class="stars">☆ ☆ ☆ ☆ ☆</div></div></div>
<div class="box"><h3>In one sentence, this book is about…</h3>{L(2)}</div><div class="box"><h3>What I loved</h3>{L(3)}</div>
<div class="box"><h3>Favourite quote or moment</h3>{L(2)}</div><div class="box"><h3>Would I recommend it? To whom?</h3>{L(2)}</div>{footer(name, "Review")}</div>""")
    pg.append(f'<div class="page">{page_head("Want to read", "To-be-read list", "heart")}<div class="two"><div class="box">{L(14)}</div><div class="box">{L(14)}</div></div>{footer(name, "TBR")}</div>')
    pg.append(f"""<div class="page">{page_head("Looking back", "My year in books", "star")}
<div class="two"><div class="box"><h3>Books read</h3>{L(1)}</div><div class="box"><h3>Pages read</h3>{L(1)}</div></div>
<div class="box"><h3>My top 3 books</h3>{L(3)}</div><div class="box"><h3>Most surprising read</h3>{L(1)}</div><div class="box"><h3>Favourite quotes of the year</h3>{L(4)}</div>
<div class="box"><h3>Next year I want to…</h3>{L(2)}</div>{footer(name, "For personal use only · © AureliaVenn")}</div>""")
    return slug, html(name, css, pg)


if __name__ == "__main__":
    for which in (sys.argv[1:] or ["tags", "journal"]):
        slug, h = {"tags": tags, "journal": journal}[which]()
        (ROOT / slug).mkdir(parents=True, exist_ok=True); (ROOT / slug / f"{slug}.html").write_text(h, encoding="utf-8"); print("wrote", slug)
