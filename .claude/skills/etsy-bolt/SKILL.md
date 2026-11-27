---
name: etsy-bolt
description: Az AureliaVenn Etsy-bolt kezelése és diagnosztikája – forgalom- és listing-elemzés (megtekintés, kedvelés, kor), SEO (cím, tag, long-tail), képek (négyzetes első kép, életkép), árak/akciók (Omnibus), Etsy Ads, értékelések, Etsy API v3 receptek és a bolt szabályai. Használd, ha Etsy-forgalomról, láthatóságról, listingek javításáról, új Etsy-termékről, akcióról, hirdetésről vagy a bolt beállításairól van szó.
---

# Etsy-bolt skill (AureliaVenn, shop 59888443)

Projekt: `projects/etsy-empire/` (szabálykönyv: `projects/etsy-empire/CLAUDE.md`). Riport Nórának magyarul, tömören, ÉRTÉKELÉS–DÖNTÉS–MIÉRT–KÖVETKEZŐ LÉPÉS formában.

## 1. Mindig adatból indulj
```bash
cd projects/etsy-empire && python3 scripts/etsy_stats.py
```
- Pillanatkép: `bolt/stats/ÉÉÉÉ-HH-NN.json`; a következő futás kiírja az azóta jött megtekintéseket (napi delta).
- Az API listingenként ad `views` és `num_favorers` mezőt. **Bolt-szintű látogatót, keresési megjelenést (impression), kattintási arányt (CTR) és Ads-statisztikát az API NEM ad** – ezt Nórától kérd képernyőképen (Shop Manager → Stats; Marketing → Etsy Ads).
- Rendelések: `GET /shops/{shop}/receipts` (transactions_r).

### Diagnosztikai küszöbök (új bolt, 0 értékelés)
| Jel | Mit jelent | Teendő |
|---|---|---|
| Új listing 7 nap után 0–1 megtekintés | nem rangsorol a keresésben (fej-kulcsszó, erős verseny) | cím/tag long-tailre, nem új termék |
| Sok megtekintés, 0 kedvelés | első kép/ár/cím nem győz meg | első kép, ár, leírás eleje |
| Kedvelés van, vásárlás nincs | bizalomhiány (0 értékelés) vagy ár | értékelésgyűjtés, akció, bundle |
| Régi listing visz forgalmat | ott van a kereslet | rokon termék ugyanabba a résbe |

**Nincs „túl sok listing” büntetés az Etsyn** – a rangsor listingenként számol (relevancia, listing-minőség: kattintás/kedvelés/eladás, bolt-élmény: értékelések, szabályzatok, teljes profil; új listing rövid újdonság-előnyt kap). A sok új listing nem árt, de ha nem kap megtekintést, csak listázási díj (0,20 $) és munka. Ilyenkor a megoldás: kevesebb új termék, több optimalizálás és külső forgalom (Pinterest).

## 2. SEO (cím, tag)
- Cím ≤140 kar., az első 40 karakterben a fő keresőkifejezés **úgy, ahogy a vevő beírja**. Fej-kulcsszó helyett **long-tail** (3–5 szó, konkrét helyzet/vevő): „kindness advent calendar for preschool”, nem „christmas printable”.
- 13 tag, mind ≤20 kar., ne ismételd szó szerint a kategóriát; vegyes: termék + vevő + alkalom + stílus.
- Attribútumok (alkalom, ünnep, kinek) kitöltése = ingyen extra kulcsszó.
- Ellenőrzés: Etsy-keresés autocomplete (Nóra böngészőjében) és a versenytárs-találatszám; ha >50 000 találat és az első oldal csupa 1000+ értékelésű bolt, akkor szűkíts.
- Szabály: nincs védjegy (Elf on the Shelf, Grinch, Disney, Stanley stb.); „Christmas Elf” általános.

## 3. Képek
- **1. kép négyzet-biztos**: `python3 scripts/square_cover.py termekek/<slug>/kepek/01-cover.jpg` → 2000x2000 (a shop-rács és a mobil négyzetesre vág; 4:5-ön a cím és az alsó sáv levágódik).
- POD: az 1. kép közeli életkép (ember viseli / kézben a bögre), a fehér hátterű Printify-mockup hátrébb. Bögre: `scripts/etsy_mug_images.py`. Póló: Etsy kép-feltöltés `rank=1` (overwrite nélkül), utána ellenőrizd, hogy nincs-e két rank-1 (ha van: `listing_image_id`+`rank` újrasorrendezés).
- Kép generálás: Higgsfield nano_banana_2 a valódi dizájnnal referenciaként; márkanév/logó a képen tilos (ellenőrizd: befőttesüveg-felirat, társasjáték-doboz).

## 4. Ár, akció, kupon (EU Omnibus)
- Akciót **Etsy Shop Managerben** Nóra állít (Marketing → Sales and discounts) – az API-nak nincs akció-végpontja. A listing árát API-val át lehet írni, de akkor nincs „% off” címke.
- Hamis áthúzott ár tilos; az EU-ban a 30 napos legalacsonyabb árat az Etsy kezeli. Két akció között tarts azonos %-ot (pl. 25%), hogy ne legyen megtévesztő.
- Értékelésért kedvezmény/ajándék felajánlása **tilos** (Etsy-szabály). Csak udvarias kérés a vásárlás után.

## 5. Etsy Ads
- Napi keret Nóra döntése (jelenleg 10 $). Leállítási szabály: 5 nap után ha költés >40 $ és hirdetési bevétel < 2× költés → vissza 5 $-ra.
- Hirdetésből zárd ki: 2,49 €-s PNG-k, szezonon kívüli termékek, 0 értékű régi tesztek.

## 6. API-receptek (api.etsy.com/v3/application, tokenek: `etsy_oauth.py`, ~/.config/etsy)
- Listingek: `GET /shops/{shop}/listings?state=active&limit=100&offset=` · képek: `GET /listings/{id}/images` · kép fel: `POST /shops/{shop}/listings/{id}/images` (files=image, data rank, overwrite) · sorrend: ugyanez `listing_image_id`+`rank`.
- Listing-módosítás (cím, tag, ár, rovat): `PATCH /shops/{shop}/listings/{id}` (listings_w) · készlet/variáció: `PUT /listings/{id}/inventory`.
- Személyre szabás: `POST /shops/{shop}/listings/{id}/personalization` (a régi is_personalizable mezőt figyelmen kívül hagyja).
- Bolt-szöveg, rovatok (`POST /shops/{shop}/sections`), bejelentés: **shops_w** jog kell (2026-11-15 óta kérve; ha 403: `python3 etsy_oauth.py link` → link Nórának).
- Tiltott hostok a konténerből: i.etsystatic.com, images.printify.com (képet nem tudsz letölteni; a repó helyi fájljaival dolgozz).

## 7. Döntési keret (Nóra mércéje)
- Minden javaslat: várható Ft, ráfordított óra, Ft/óra (mérce 8 750–19 000 Ft/óra). Új ötlet: max 1 hét és 30–50 ezer Ft teszt.
- Kifelé menő vagy tartós változás (élesítés kivételével – az etsy-empire termékek minőségi kapu után automatikusan élesíthetők) → egysoros terv + Nóra jóváhagyása.
- Napló: `ceg/naplo.md`; pillanatképek: `projects/etsy-empire/bolt/stats/`.
