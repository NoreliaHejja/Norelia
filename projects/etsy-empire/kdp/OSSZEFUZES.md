# Etsy → Amazon KDP összefűzés (Nóra, 2026-11-13)

Cél: a kész Etsy digitális termékekből eladható KDP-könyv (papír, 8.5x11, fekete-fehér), angolul ÉS németül.
Szabály: a hosszú könyv „közbenső” napjain (amikor nem készül kész könyv) 1 összefűzés/nap.

## Hogyan
- 3–4 rokon termék vagy 1 termék kibővítve → 60–110 oldal (KDP: ≤108 old. fix nyomdaköltség, ezért 100–108 old. ideális).
- Belső: fekete-fehér, FEHÉR háttér (teljes színes háttér tilos – KDP elutasítja), szél-ellenőrzés; minta: `scripts/build_kdp_bundle.py`, `scripts/kdp_books.py`, `scripts/kdp_books_de.py`; borító: `scripts/kdp_cover.py` (DE-nél meta lang de).
- Ár: 8,99–9,99 $ / €. Jogdíj ≈ 0,6 × ár − 2,84 $.
- Kimenet: `kdp/<slug>/` (interior.pdf, cover.pdf, KDP_FELTOLTES.md: cím, alcím, leírás, 7 kulcsszó, kategória, AI = Yes) → zip Nórának. Nóra tölti fel (KDP-t nem automatizálunk).

## Sor (felülről lefelé; ha elfogy: az új Etsy-termékekből, vagy a termekotletek.md T1–T4 trend-sorából)
| # | Könyv | Forrás | EN | DE |
|---|---|---|---|---|
| 1 | Large Print Word Search for Adults (100 rejtvény, nagy betű) | T1 trend + generátor | – | – |
| 2 | Self-Compassion Journal for Women (90 napos, a Gentle Life Guides mellé) | T3 trend + Still Lit gyakorlatai | – | – |
| 3 | Bold & Easy Coloring Book for Adults (50 kép) | T4 trend + linework | – | – |
| 4 | Cat & Dog Owner Planner (cat-enrichment-planner + ready-for-a-dog-kit bővítve) | Etsy | – | – |
| 5 | Reading Journal / Book Lover's Log | T2 trend | – | – |
| 6 | következő 3–4 új Etsy-termék tematikus csomagja | Etsy | – | – |
