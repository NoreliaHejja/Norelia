# etsy-empire – napi digitális termékgyár (AureliaVenn bolt)

Cél: **minden munkanap egy prémium, nyomtatható digitális termék** Emilynek (lásd `persona.md`),
Etsy-re (fő csatorna) és Amazon KDP-re (csak 24+ oldalas bundle-ök). Témák: kutya, macska, kisgyermekes családi élet.
Termék nyelve: US English. Riport Nórának: magyarul, tömören.

## Mappák és fájlok
| Mi | Hol |
|---|---|
| termékek (HTML forrás, PDF, képek, listing.json) | `termekek/<slug>/` |
| közösségi szövegek | `marketing_szovegek/<slug>_social.json` |
| ötlet-rotáció | `termekotletek.md` |
| PDF-render + túlcsordulás-ellenőrzés | `scripts/render_pdf.js` |
| listingképek (4:5) a PDF-ből | `scripts/listing_kepek.py` |
| Etsy piszkozat-feltöltés (API v3) | `etsy_uploader.py` |
| KDP csomag (kézi feltöltésre) | `amazon_kdp.py` |
| posztcsomag | `social_poster.py` |

## Napi rutin (ütemezett futás, memória nélkül)
1. Olvasd: ez a fájl, `persona.md`, `termekotletek.md`. Válaszd a legfelső „ötlet” sort (a napi szabály szerint).
2. Írd meg a terméket egyetlen HTML-ben: `termekek/<slug>/<slug>.html` – a `ready-for-a-dog-kit` a minta (design, fontok, komponensek).
   8 oldal: borító, használati útmutató, 5 funkcionális oldal (legalább 1 gyerekoldal), záró oldal.
3. `node scripts/render_pdf.js termekek/<slug>/<slug>.html` → **OVERFLOW: none** kell; `pdfinfo` → Letter, 8 oldal.
4. Kontaktlap (`pdftoppm` + `montage`) → nézd meg; hibát javíts.
5. `listing.json` a minta szerint (cím ≤140, 13 tag ≤20 kar., leírás AI-közléssel, `status: jovahagyasra_var`).
6. `python3 scripts/listing_kepek.py termekek/<slug>` → `python3 etsy_uploader.py termekek/<slug>` (száraz futás) → `python3 amazon_kdp.py termekek/<slug>` → `python3 social_poster.py termekek/<slug>`.
7. `termekotletek.md`: a sor → „kész (dátum)”. Commit + push.
8. Nórának: PDF + 3 kép + cím/ár, egy mondat, és „Jóváhagyod? (igen → piszkozat az Etsy-n)”.

## Szabályok (kötelező)
- **Jóváhagyási kapu**: `etsy_uploader.py --feltolt` csak `status: jovahagyva` mellett fut, és csak **piszkozatot** hoz létre. Élesítés: Nóra.
- **KDP-t nem automatizálunk** (nincs API; a robotos feltöltés fióktiltást kockáztat) → csak csomag, Nóra tölti fel.
- **Posztolás**: csak jóváhagyás után, Metricoolon át, `isAiGenerated: true`; Emily posztjaiban „AI-generated character”.
- **Etsy AI-közlés** minden leírásban; nincs kitalált vélemény, nincs hamis „eredeti ár”/akció.
- Nincs állatorvosi/nevelési „szakértői” állítás; minden ilyen oldalon: „planning aid, not veterinary advice”.
- Nincs másolás: más bolt termékét, nevét, dizájnját nem utánozzuk.
- Mérce: 1 termék ≈ 1 óra Claude-munka, 0 Ft; Nóra ideje terméken ≤ 5 perc (jóváhagyás).
