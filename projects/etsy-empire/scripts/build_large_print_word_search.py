#!/usr/bin/env python3
"""Large Print Word Search for Seniors (termekotletek T1): 25 téma, 13×13 rács, 12 szó, csak vízszintes/függőleges/átlós (lefelé) irány,
nagy betűk; a végén megoldások (4 / oldal, kiemelt betűkkel). Letter + A4. KDP-re is alkalmas (24+ oldal)."""
import random
from pathlib import Path
from common import page_head, footer

SLUG = "large-print-word-search-seniors"; NAME = "Large Print Word Search for Seniors"
OUT = Path(__file__).resolve().parent.parent / "termekek" / SLUG
N = 13
THEMES = {
 "In the Garden": "ROSE TULIP DAISY SPADE HOSE SEEDS SOIL BENCH FENCE PATH PANSY LILY",
 "At the Seaside": "WAVES SAND SHELL BOAT GULL PIER SUN TOWEL CRAB TIDE DUNE BREEZE",
 "Kitchen Things": "KETTLE SPOON PLATE BOWL OVEN APRON WHISK TOASTER LADLE FORK TRAY CUP",
 "Birds": "ROBIN SPARROW OWL EAGLE WREN DOVE FINCH HERON CROW SWAN DUCK HAWK",
 "Fruit Basket": "APPLE PEAR PLUM GRAPE MELON LEMON PEACH CHERRY KIWI MANGO LIME FIG",
 "Winter Days": "SNOW FROST SCARF MITTENS FIRE COCOA SLED ICE BOOTS QUILT STORM COAT",
 "Old Time Music": "WALTZ PIANO BANJO SWING JAZZ VIOLIN CHOIR TUNE HARP SONG RADIO DRUM",
 "Baking Day": "FLOUR SUGAR BUTTER EGGS DOUGH YEAST CAKE PIE OVEN BREAD SCONE TART",
 "Trees": "OAK MAPLE BIRCH PINE WILLOW ELM CEDAR ASH BEECH FIR HOLLY POPLAR",
 "On the Farm": "BARN COW HORSE SHEEP GOAT HEN TRACTOR HAY FIELD PIG GATE MILK",
 "Colors": "RED BLUE GREEN YELLOW PURPLE ORANGE PINK BROWN BLACK WHITE GRAY GOLD",
 "Flowers": "IRIS POPPY ASTER VIOLET LILAC DAHLIA ORCHID PEONY LOTUS CROCUS SAGE MUM",
 "Around the House": "SOFA LAMP CLOCK RUG DOOR WINDOW SHELF STAIRS CHAIR TABLE MIRROR BED",
 "Things in Space": "MOON STAR SUN COMET PLANET ORBIT MARS VENUS GALAXY ROCKET EARTH SKY",
 "Weather": "RAIN CLOUD WIND SUNNY FOG HAIL MIST THUNDER STORM BREEZE SLEET HEAT",
 "Breakfast": "TOAST EGGS BACON JAM OATS HONEY COFFEE TEA JUICE MUFFIN CEREAL MILK",
 "Sewing Box": "NEEDLE THREAD BUTTON PIN THIMBLE SCISSORS YARN HEM SEAM LACE ZIPPER PATCH",
 "Pets": "DOG CAT FISH RABBIT PARROT HAMSTER TURTLE PONY MOUSE LEASH BOWL COLLAR",
 "Travel": "TRAIN PLANE MAP TICKET HOTEL SUITCASE BUS CRUISE BEACH CAMERA PASSPORT TOUR",
 "Vegetables": "CARROT PEAS ONION LEEK BEAN CORN KALE POTATO CELERY BEET RADISH TOMATO",
 "Games Night": "CARDS CHESS DICE BINGO PUZZLE DOMINO TEAM SCORE WINNER BOARD TOKEN TURN",
 "Spring": "BLOOM NEST LAMB TULIP BUD RAIN GREEN CHICK MEADOW BREEZE SPROUT DAWN",
 "Summer": "PICNIC SWIM BEACH SUN LEMONADE CAMP HIKE FAN SHADE BERRY GRILL ICE",
 "Autumn": "LEAVES ACORN HARVEST PUMPKIN APPLE CIDER RAKE SCARF FOG CHESTNUT HAY CORN",
 "Happy Memories": "WEDDING PICNIC DANCE LETTER FRIEND SMILE PHOTO HOLIDAY FAMILY GARDEN SONG HOME",
}
DIRS = [(0, 1), (1, 0), (1, 1)]
CSS = """:root{ --dark:#24435c; --sage:#2f6f8f; --tint:#eef5f9; --line:#cfe0ea; --accent:#d9a441; --warm:#f5f8fb; --warmline:#d6e3ec; --cream:#fbfdff; }
.cv{ background:linear-gradient(180deg,#fbfdff,#e8f1f7); align-items:center; justify-content:center; text-align:center; }
.cv h1{ font-size:44pt; color:var(--sage); margin:10px 0 6px; line-height:1.05; } .cv .tg{ font-size:15pt; color:var(--dark); max-width:5.8in; line-height:1.45; }
.cv .pill{ margin-top:20px; background:var(--dark); color:#fff; border-radius:30px; padding:10px 22px; font-weight:600; font-size:13pt; }
.ws{ display:grid; grid-template-columns:repeat(13,1fr); border:2.5px solid var(--dark); border-radius:8px; padding:6px; margin:0 auto 12px; width:6.4in; }
.ws div{ height:.46in; display:flex; align-items:center; justify-content:center; font-size:20pt; font-weight:700; color:#222; font-family:'DejaVu Sans Mono',monospace; }
.words{ columns:3; font-size:15pt; line-height:1.6; font-weight:600; color:var(--dark); margin-bottom:.15in; }
.ans{ display:grid; grid-template-columns:1fr 1fr; gap:12px; flex:1; margin-bottom:.12in; }
.ans .t{ font-size:10pt; font-weight:700; color:var(--sage); margin-bottom:3px; }
.mini-ws{ display:grid; grid-template-columns:repeat(13,1fr); border:1.5px solid var(--line); }
.mini-ws div{ height:.2in; display:flex; align-items:center; justify-content:center; font-size:8pt; color:#bbb; font-family:'DejaVu Sans Mono',monospace; }
.mini-ws div.h{ background:#ffe9a8; color:#222; font-weight:700; }
"""


def make(words, seed):
    rnd = random.Random(seed)
    for _ in range(500):
        g = [[None] * N for _ in range(N)]; pos = set(); ok = True
        for w in sorted(words, key=len, reverse=True):
            placed = False
            for _ in range(300):
                dr, dc = rnd.choice(DIRS); r = rnd.randrange(N - dr * (len(w) - 1)); c = rnd.randrange(N - dc * (len(w) - 1))
                cells = [(r + dr * i, c + dc * i) for i in range(len(w))]
                if all(g[a][b] in (None, w[i]) for i, (a, b) in enumerate(cells)):
                    for i, (a, b) in enumerate(cells): g[a][b] = w[i]; pos.add((a, b))
                    placed = True; break
            if not placed: ok = False; break
        if ok:
            for a in range(N):
                for b in range(N):
                    if g[a][b] is None: g[a][b] = rnd.choice("ABCDEFGHIJKLMNOPRSTUVWY")
            return g, pos
    raise SystemExit("nem fér el: " + " ".join(words))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pg = [f'<div class="page cv"><div class="eyebrow">Printable puzzle book · Extra large print</div><h1>Large Print<br>Word Search</h1>'
          f'<div class="tg">25 cheerful puzzles with big, easy-to-read letters. Words go across, down and diagonally, never backwards. Answers included.</div><div class="pill">{len(THEMES)} puzzles · answers · US Letter + A4</div></div>']
    pg.append(f"""<div class="page">{page_head("Before you start", "How to play", "book")}
<p class="subtitle" style="font-size:15pt;line-height:1.6">Find each word from the list in the grid. Words run <b>left to right</b>, <b>top to bottom</b> or <b>diagonally down</b>. They never run backwards. Circle each word you find and tick it off the list.</p>
<div class="card warm" style="font-size:14pt"><h3>Tips</h3><div>Start with the longest words. Look for unusual letters like K, Y or Z. Take a break and come back: fresh eyes find words faster.</div></div>
<div class="card" style="margin-top:auto;margin-bottom:.15in"><h3>Print tip</h3><div class="mini">Print one puzzle at a time, or print the whole book and keep it in a folder. A clipboard makes it easy to solve in an armchair.</div></div>
{footer(NAME, "How to play")}</div>""")
    sol = []
    for i, (theme, ws) in enumerate(THEMES.items(), start=1):
        words = ws.split(); assert len(words) == 12 and all(len(w) <= N for w in words), theme
        g, pos = make(words, i * 7); sol.append((i, theme, g, pos))
        grid = "".join(f"<div>{ch}</div>" for row in g for ch in row)
        wl = "".join(f"<div>☐ {w.title()}</div>" for w in words)
        pg.append(f'<div class="page">{page_head(f"Puzzle {i}", theme, "star")}<div class="ws">{grid}</div><div class="words">{wl}</div>{footer(NAME, f"Puzzle {i}")}</div>')
    for k in range(0, len(sol), 4):
        cells = ""
        for i, theme, g, pos in sol[k:k + 4]:
            mg = "".join(f'<div class="{"h" if (a, b) in pos else ""}">{g[a][b]}</div>' for a in range(N) for b in range(N))
            cells += f'<div><div class="t">{i}. {theme}</div><div class="mini-ws">{mg}</div></div>'
        pg.append(f'<div class="page">{page_head("Answers", f"Solutions {k + 1}–{min(k + 4, len(sol))}", "check")}<div class="ans">{cells}</div>{footer(NAME, "Answers")}</div>')
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME}</title><link rel="stylesheet" href="../../assets/base.css"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
    (OUT / f"{SLUG}.html").write_text(html, encoding="utf-8"); print("wrote", len(pg), "pages")


if __name__ == "__main__":
    main()
