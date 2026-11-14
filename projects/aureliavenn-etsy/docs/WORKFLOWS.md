# Munkafolyamatok

## 1. Heti rutin (hétfő)
1. Etsy Stats (előző hét, napi grafikon): látogatás, listing-megtekintés, kosár, eladás, bevétel, kedvenc, követő, forgalmi források.
2. Etsy Ads (30 nap — 7 napos szűrő nincs): megjelenés, kattintás, rendelés, költés, ROAS, listingenként.
3. Pinterest: Created lap — kimentek-e a múlt heti pinek? Megjelenítések.
4. Jelentés: `reports/weekly/YYYY-MM-DD-status.md` (sablon: lent) + sor a `docs/METRICS.md`-be.
5. Következő heti 7 pin terve → **Nori jóváhagyása után** ütemezés.
6. Top 3 teendő → `docs/TODO.md`.

### Jelentés-sablon
```
# AureliaVenn — állapot (YYYY-MM-DD)
## Heti számok
## Ads
## Húzó termék
## Pinterest (kiment? megjelenítés)
## Pin-terv (jóváhagyásra vár)
## Teendő (max 3)
```

## 2. Pinterest-pin kiküldés (jelenlegi módszer, Chrome)
- Chrome-ban bejelentkezve pinterest.com, JS `fetch` POST `/resource/PinResource/create/`
- Fejléc: `X-CSRFToken` = a `csrftoken` süti értéke.
- options: `board_id`, `image_url` (a listing og:image-e), `link` (Etsy listing URL), `title`, `description`, `method: 'uploaded'`, `scheduled_ts` (Unix, 00:30 UTC = US esti idősáv).
- **Ismert hiba:** az okt. 13–25 pinek nem jelentek meg; a `_scheduled` oldal hibára dob. Kiküldés után MINDIG ellenőrizni a Created/Scheduled lapon. Ha a módszer nem megbízható → Pinterest hivatalos ütemező vagy Metricool (connector elérhető) — eldöntendő.
- Napi 1 pin, 7/hét. Az életkép-stílus működik, a sima termékfotó nem.

### Aktuális pin-terv (nov. 5–11, 00:30 UTC) — JÓVÁHAGYVA (Nóra, 2026-11-04); kiküldés: Metricool, ha a Pinterest be van kötve
| Nap | Tábla | Termék | Listing | Kép (hash/id_suffix) |
|---|---|---|---|---|
| 11.05 | Christmas Printables for Kids | Kindness Elf Kit | 4586400098 | 4db7b6/8631460688_oj1f |
| 11.06 | Thanksgiving Ideas for Kids | Thanksgiving Gratitude Countdown | 4586893950 | 5ae7f0/8631477930_db2s |
| 11.07 | Christmas Family Traditions | Christmas Countdown | 4586397852 | 542a33/8679548651_kuj8 |
| 11.08 | Gift Ideas for Families | Budget Planner | 4589530944 | 6c0954/8679253753_q3ra |
| 11.09 | Christmas Printables for Kids | Countdown + Elf Bundle | 4586897813 | 0e5f5c/8679542389_4v56 |
| 11.10 | Thanksgiving Ideas for Kids | Pumpkin Cat Youth Sweatshirt | 4562150299 | 642157/8476160171_tqv8 |
| 11.11 | Cat Mom Life | Santa Hat Cat Mug | 4584553523 | 887e27/8593097366_gkzn |
Minden pinnél: Pinterest AI-jelölés (isAiGenerated) bekapcsolva, link = Etsy listing.

## 3. Új digitális termék → élő listing
1. Tartalom + PDF (US Letter + A4) / XLSX elkészítése → `products/<slug>/`. XLSX-nél: képletek ellenőrzése (LibreOffice recalculation, 0 hiba).
2. Képsor (cél: 10 kép): hero, feature-képek (1 kép = 1 funkció + haszon), kompatibilitás/nyomtatás, kitöltött oldal/eredmény, „Is this right for you?” GYIK, How it works, „You might also like”.
3. `listing.md`: cím ≤140 karakter (keresési kifejezés elöl), 13 tag (≤20 karakter/tag), leírás (horog → WHAT'S INSIDE → WORKS WITH / HOW IT WORKS → A NOTE AI-jelöléssel), ár, kategória.
4. Etsy piszkozat (Claude, Chrome) → Nori feltölti a fájlokat a `~/Claude/etsy-upload/<termék>/` mappából → Nori átnézi → **jóváhagyás után** Claude élesít.
5. Bevezető ár az első 5 értékelésig; később valódi időzített akció.

## 4. Új POD-termék
1. Minta (Higgsfield, átlátszó PNG 2048×2048) → Printify, színek, amik minden méretvariánsban megvannak.
2. Printify „Publishing settings”: cím/leírás/tag szinkron KI.
3. Etsyben: cím a terméktípussal (mug, sweatshirt, tee), 13 tag, „printed design” jelölés, méret-táblázat kép, production partner: Printify.
4. Képsor: mockup → flat lay/életkép → méret-táblázat → közeli.

## 5. Listing-szöveg minta (angol, Emily-hang)
- Horog 1 mondatban, emoji 1 db.
- Konkrét haszon („Most cost $0 and take under 30 minutes”).
- Kor/célcsoport („Best for families with kids ages 3 to 10”).
- Záró „💛 A NOTE”: AI-jelölés, védjegy-mondat, „Personal use only” / „Licensed for one classroom”.
