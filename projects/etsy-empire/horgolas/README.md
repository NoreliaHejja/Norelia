# Horgolásminta-gyártósor (Nóra, 2026-11-23)

Cél: PDF horgolásminták az AureliaVenn Etsy-boltba, **angolul és németül** (két külön PDF, egy listingben; a német listing-szöveg a leírás második felében).
Piaci alap (Alura, 2026-11-23): teknős amigurumi ~254 eladás/hó, virágos maxi ruha ~171/hó, KristinesDayCrafts bolt ~360/hó (7 $ átlagár); „crochet christmas ornament pattern” 34e keresés/hó, közepes verseny.

## Kéthetes teszt (nov. 24 – dec. 7, Nóra döntése)
Naponta 2 minta **tesztelő nélkül is élesíthető**, de az 1. kép saját, a mintához hű séma-rajz (diagram; AI-illusztráció nem, mert díszesebbet mutat, mint ami kijön), + mintaoldal + tartalom; a leírásban: „New pattern. Photos are illustrations; a maker-tested photo will be added.” AI-fotó kész darabról tilos. A tesztelői fotók utólag kerülnek fel.

## Alapszabály (a teszt után): minden mintát ember horgol meg és fotóz le
- AI nem tudja garantálni a szemszámokat, és AI-fotó egy nem létező darabról megtévesztés → **tilos**.
- Claude: ötlet + piackutatás, minta-piszkozat (EN), méret- és szemszám-ellenőrzés számolással, PDF EN + DE, listing, SEO, feltöltés, Pinterest.
- Tesztelő (Nóra anyukás csoportjából vagy FB-horgolós csoportból): megcsinálja a darabot a piszkozat alapján, jelzi a hibákat, és lefotózza (útmutató: `TESZTELO.md`). Díj: 5–10e Ft/minta + fonal, Nóra fizeti.
- Élesítés csak a tesztelő visszajelzése + valódi fotók után (`statusz: kesz`). Addig `tesztre_var`.

## Ábrák (Nóra, 2026-11-24) – kötelező minden mintában
Minden minta PDF-jében kell: (1) kész forma vázlata méretekkel, (2) jelkulcsos horgolásrajz (körös: `circle_chart`, soros: `row_chart`, egyedi: granny/hópehely/szív), (3) jelmagyarázat. A `pattern.json` „figures” + „legend” mezője adja (`scripts/crochet_charts.py`); a meglévő mintákét a `horgolas/abrak.py` írja be. Nyelvek: HU / EN / DE.

## Ritmus
- Naponta 2 új minta-**piszkozat**, de a várólista legfeljebb 6 tesztre váró minta lehet (különben csak a teszten átment minták véglegesítése megy).
- A teszten átment mintákat aznap véglegesítjük és élesítjük (EN + DE PDF, listing, kép a tesztelő fotóiból).
- Kezdő sorrend (egyszerűtől nehezebbig): lapos dísz → kis amigurumi → sapka/sál → kosár → nagyobb amigurumi → ruhadarab méretekkel (csak ha egy tesztelő vállalja a méretezést).

## Fájlok
| Mi | Hol |
|---|---|
| minta forrás (JSON, EN + DE mezők) | `horgolas/mintak/<slug>/pattern.json` |
| generátor (HTML → PDF EN + DE) | `scripts/build_crochet_pattern.py horgolas/mintak/<slug>` |
| tesztelő fotói | `horgolas/mintak/<slug>/fotok/` |
| várólista és állapot | `horgolas/SOR.md` |
| tesztelői útmutató (magyar) | `horgolas/TESZTELO.md` |

## Minőségi kapu (élesítés előtt)
- A szemszámok soronként összeadva stimmelnek (a generátor ellenőrzi, ha a sorban `count` van megadva).
- US-terminológia az angol PDF-ben (UK-átváltó táblázattal), német rövidítések a németben (fM, Lm, Km, Stb., zun, abn).
- Valódi fotó: legalább 3 kép (kész darab tiszta háttéren, közeli, méret kézben/vonalzóval) a tesztelőtől.
- Leírás: „PDF PATTERN ONLY, not the finished item”, nehézségi szint, anyag, horgolótű, kész méret, nyelvek, AI-közlés (a szöveg megírásában AI segített; a mintát kézzel tesztelték).
- Ár: kis minta 3,99 €, amigurumi 5,49 €, ruhadarab 6,99 €.
