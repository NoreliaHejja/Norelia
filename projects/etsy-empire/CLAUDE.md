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

## ÚJ RITMUS (Nóra, 2026-11-17) – ez felülírja a lenti napi 2+1-et
Az Etsy Stats szerint (nov. 11–17: 19 látogató; Etsy-keresés 2, Ads 6, közösségi média 0) és az API szerint (az 52 új listing átlag 0,2–0,5 megtekintés) az új termék most nem hoz forgalmat. Ezért: **naponta 5 listing optimalizálása** (long-tail cím + 13 tag, `bolt/optimalizalas.json`), **új digitális termék csak H/Sze/P 1 db**, **POD szünet nov. 24-ig**, mérés `scripts/etsy_stats.py`. Etsy-tudás: `.claude/skills/etsy-bolt/SKILL.md`. Felülvizsgálat: nov. 24.

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
- **Négyzetes első kép (2026-11-15):** az Etsy shop-rács és a mobil négyzetesre vágja a 4:5-ös borítót (levágja a címsávot és az INSTANT DOWNLOAD sávot). Ezért az `images[0]` mindig `python3 scripts/square_cover.py termekek/<slug>/kepek/01-cover.jpg` → `01-cover-square.jpg` (2000x2000).
- Trend-szabály: a `termekotletek.md` keresletalapú; ha a lista fogy, előbb trendkutatás (Etsy/Pinterest szezon), csak utána új ötlet.

## Szabályok (kötelező)
- **Etsy: automatikus élesítés** (Nóra döntése, 2026-11-10): jóváhagyás nélkül megy ki, ha a minőségi kapu átment (OVERFLOW: none, kontaktlap rendben, uploader-ellenőrzés hibátlan). Kétes minőség → `status: javitando`, nem tölt fel. Költség: 0,20 $/listing (+ 4 havonta megújítás).
- **Minden más kifelé menő dolog** (social poszt, e-mail, KDP) továbbra is Nóra jóváhagyásával.
- **KDP-kapu (Nóra, 2026-11-14):** borító és belív mérete pontosan a KDP-ben választott trim szerint, semmi nem lóg ki a keretből (0,25 in biztonsági sáv), feltöltési lap normál betűs (11 pt), tágabb sorközű PDF-ben (`scripts/kdp_lap.py`). Részletek: `books/SOROZAT.md` „KDP-kapu”.
- **KDP-t nem automatizálunk** (nincs API; a robotos feltöltés fióktiltást kockáztat) → csak csomag, Nóra tölti fel.
- **Posztolás**: csak jóváhagyás után, Metricoolon át, `isAiGenerated: true`; Emily posztjaiban „AI-generated character”.
- **Etsy AI-közlés** minden leírásban; nincs kitalált vélemény, nincs hamis „eredeti ár”/akció.
- Nincs állatorvosi/nevelési „szakértői” állítás; minden ilyen oldalon: „planning aid, not veterinary advice”.
- Nincs másolás: más bolt termékét, nevét, dizájnját nem utánozzuk.
- Mérce: 1 termék ≈ 1 óra Claude-munka, 0 Ft; Nóra ideje terméken ≤ 5 perc (jóváhagyás).

## Printify POD (2026-11-12)
- **Napi max. 2 POD-termék (Nóra, 2026-11-15)**: a rendelések Printify-költségét Nóra előre fizeti, ezért kevesebb, jobban kiválasztott termék. Alap: 1 dizájn → felnőtt póló + bögre.
- Bolt: Printify „Aurelia Venn” (28692848), Etsy-hez kötve. Feltöltő: `printify_uploader.py pod/<slug>.json [--publish]`; token a proxyban (api.printify.com network secret).
- Dizájn-szabálykönyv: `pod/DESIGN.md` (fantáziadús, trendi, ötlet-alapú; védjegy tilos). Minden új POD-dizájn ez alapján.
- TikTok Shop: a Printify-integráció csak US eladónak megy, magyar eladó nem regisztrálhat → most nem (lásd ceg/naplo.md).
- **Bögre-képek (Nóra, 2026-11-13):** a kétoldalas bögrénél (blueprint 68, minta x=0.25/0.75) a Printify csak 1 mockupot ad, és az a bögre üres közepét mutatja. Ezért minden bögre publikálása után kötelező: 3 saját Higgsfield-mockup (nano_banana_2, a Printify-feltöltés preview_url-je → `media_import_url`): (1) stúdió-közeli, fül jobbra, (2) jobb kézben tartva, minta szembe, (3) két bögre egymás mellett = mindkét oldal → 2000x2500 JPG `pod/mockups/` → Etsy képfeltöltés rank 1 (overwrite=true), 2, 3. Ellenőrizd a kontaktlapon, hogy a minta látszik. Utólagos Printify-újrapublikálásnál `images: false`, különben felülírja.
- **Mug wrap PNG (Nóra, 2026-11-14, bestseller-minta: 12e megtekintés, 2,33 €):** minden új POD-bögre dizájnja digitális termékként is megy: 11oz (2550x1050) + 15oz (2625x1140) PNG, 300 DPI, átlátszó, minta mindkét oldalon; listing 2,49 €, `is_supply: true`, licenc: személyes + kisvállalkozói max. 200 bögre. Minta: `termekek/mug-wrap-<slug>/`. Borító: `cover_overlay.py ... "PNG · 300 DPI · Sublimation ready" "PNG|FILE"`.
- **Névre szóló termékek (Nóra, 2026-11-14):** `personalized/` – dizájnok `designs.json` + `art/`, renderelő `render.py` (név-ellenőrzés), listingek `create_listings.py` (Etsy API közvetlenül, NEM Printify-publikálás; SKU `PFY-<bp>-<provider>-<variant>-<kód>`, max 32 kar.; névmező az új `/shops/{shop}/listings/{id}/personalization` végponttal), teljesítés `orders.py --live` (ütemezett: 8:23 és 20:23). Árak: bögre 16,99 €, póló felnőtt 22,99–26,99 €, gyerek 16,99 €.
