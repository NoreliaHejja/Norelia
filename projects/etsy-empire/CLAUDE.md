# etsy-empire – napi digitális termékgyár (AureliaVenn bolt)

Cél: **a hét minden napján 2 új prémium termék + 1 kiegészítés, ha van értelme** (színváltozat, A4-változat vagy 3–4 termékes bundle; bundle 24+ oldallal → KDP) Emilynek (lásd `persona.md`),
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
| Etsy feltöltés + élesítés (API v3, api.etsy.com) | `etsy_uploader.py` (folytatja a félbeszakadt feltöltést) |
| Etsy OAuth (PKCE, token-frissítés) | `etsy_oauth.py` – tokenek és kulcs: `~/.config/etsy/` (repón kívül!). Ha a konténer újraindul és a token elveszett: `python3 etsy_oauth.py link` → Nóra engedélyez → `code <URL>` |
| KDP csomag (kézi feltöltésre) | `amazon_kdp.py`; több termékből 24+ oldalas könyv: `scripts/build_kdp_bundle.py` → `kdp/<könyv>/` |
| Emily reel (9:16 felirat) | `scripts/reel_overlay.sh`; videókönyvtár: `marketing_szovegek/emily_videok.json` |
| posztcsomag | `social_poster.py` |

## Napi rutin (ütemezett futás, memória nélkül)
1. Olvasd: ez a fájl, `persona.md`, `termekotletek.md`. Új termék: a két legfelső „ötlet” sor (ha 5 alá fogy a lista, előbb írj 10 új ötletet a persona alapján, ismétlés nélkül). Kiegészítés: a legrégebbi kész termék színváltozata, vagy ha van 3–4 rokon kész termék, bundle.
2. Írj egy generátort: `scripts/build_<slug>.py` (közös elemek: `scripts/common.py`, stílus: `assets/base.css`) → `termekek/<slug>/<slug>.html`. Minták: `build_cook_with_me.py`, `build_meal_planner.py`. A listing.json-ba kerüljön `kepszoveg` (listingkép-feliratok) és `social` (poszt-szövegek Emily hangján).
   8 oldal: borító, használati útmutató, 5 funkcionális oldal (legalább 1 gyerekoldal), záró oldal.
3. `node scripts/render_pdf.js termekek/<slug>/<slug>.html` → **OVERFLOW: none** kell; `pdfinfo` → Letter, 8 oldal. Utána `node scripts/render_a4.js termekek/<slug>/<slug>.html` → A4 PDF (az AureliaVenn-szabály: mindig Letter + A4).
4. Kontaktlap (`pdftoppm` + `montage`) → nézd meg; hibát javíts.
5. `listing.json` a minta szerint (cím ≤140, 13 tag ≤20 kar., mindkét PDF a files-ban, leírásban „INSTANT DIGITAL DOWNLOAD. No physical item will be shipped.” és a záró mondat: „Designed by our small shop, AureliaVenn, with the help of AI tools.”, `status: kesz`).
6. `python3 scripts/listing_kepek.py termekek/<slug>` → `python3 etsy_uploader.py termekek/<slug> --feltolt --aktival` (ha nincs API-kulcs: száraz futás, és jelezd) → `python3 amazon_kdp.py termekek/<slug>` → `python3 social_poster.py termekek/<slug>`.
7. `termekotletek.md`: a sor → „kész (dátum)”. Commit + push.
8. Nórának: rövid napi riport (mi ment ki, cím, ár, Etsy-link). Jóváhagyás nem kell.

## Borító és képek (Nóra, 2026-11-12)
- Az 1. kép (borító) legyen **színes, életképes mockup**: a nyomtatott oldalak valós környezetben (konyhapult, gyerekasztal, karácsonyi asztal), élénk, szezonális színekkel, vásárlásra csábító szöveg-kiemeléssel (pl. „INSTANT DOWNLOAD”, „Editable”). Higgsfield (nano_banana_pro / gpt_image) a lefotózott PDF-oldal referenciájával, „no extra text” promptrésszel; a feliratot mi tesszük rá. Előbb balance-ellenőrzés.
- Menet: oldal-PNG-k (pdftoppm, 2 db: borító + legszebb belső oldal) → Higgsfield media_upload + PUT + media_confirm → `generate_image_batch` (nano_banana_2, 4:5, image_references) → letöltés (d8j0ntlcm91z4.cloudfront.net) → `python3 scripts/cover_overlay.py <mockup.png> termekek/<slug>/kepek/01-cover.jpg "Cím" "Alcím" "#színkód"` → nézd meg → ez legyen az images[0]. Élő listingen csere: kép-feltöltés `rank=1, overwrite=true` (a régit lecseréli). Ha a Higgsfield nem elérhető: a `listing_kepek.py` borítója marad, és jelezd.
- Trend-szabály: a `termekotletek.md` keresletalapú; ha a lista fogy, előbb trendkutatás (Etsy/Pinterest szezon), csak utána új ötlet.

## Szabályok (kötelező)
- **Etsy: automatikus élesítés** (Nóra döntése, 2026-11-10): jóváhagyás nélkül megy ki, ha a minőségi kapu átment (OVERFLOW: none, kontaktlap rendben, uploader-ellenőrzés hibátlan). Kétes minőség → `status: javitando`, nem tölt fel. Költség: 0,20 $/listing (+ 4 havonta megújítás).
- **Minden más kifelé menő dolog** (social poszt, e-mail, KDP) továbbra is Nóra jóváhagyásával.
- **KDP-t nem automatizálunk** (nincs API; a robotos feltöltés fióktiltást kockáztat) → csak csomag, Nóra tölti fel.
- **Posztolás**: csak jóváhagyás után, Metricoolon át, `isAiGenerated: true`; Emily posztjaiban „AI-generated character”.
- **Etsy AI-közlés** minden leírásban; nincs kitalált vélemény, nincs hamis „eredeti ár”/akció.
- Nincs állatorvosi/nevelési „szakértői” állítás; minden ilyen oldalon: „planning aid, not veterinary advice”.
- Nincs másolás: más bolt termékét, nevét, dizájnját nem utánozzuk.
- Mérce: 1 termék ≈ 1 óra Claude-munka, 0 Ft; Nóra ideje terméken ≤ 5 perc (jóváhagyás).
