# TODO

Utolsó ismert állapot: 2026. szept. 27. (a részletes munkamenet vége), kiegészítve nov. 4-én.
A „?” jelű pontok állapotát a tulajdonostól kell megkérdezni, mert azóta változhatott.

## P0 – élesítés előtt kötelező

- [ ] **Domain** kiválasztása és megvétele (.de; ötletek: `stundensatz-rechner.de`, `reinigung-kalkulieren.de`). ?
- [ ] **EV-adatok** az Impressumba: cím, e-mail, nyilvántartási szám, adószám, közösségi adószám. ?
- [ ] **Közösségi adószám** az EV-re (Digistore24-kifizetéshez kell). ?
- [ ] **Elavult dátumok javítása** a `src/landing.src.html`-ben:
  - 282. sor „Frühbucherpreis sichern” + a 79/149 €-s áthúzott árak: a korai ár eredetileg okt. 31-ig szólt → új határidő, vagy az áthúzott ár törlése (német jog: kitalált „eredeti ár” nem lehet),
  - 334. sor „Auslieferung am 15. November 2026” → reális új dátum az OS/Starter elkészülte szerint,
  - 390. sor Datenschutz „Stand: Oktober 2026” → élesítés hónapja.
- [ ] **Digistore24:** Kalkulations-Kit termék létrehozása (adatok: `marketing/digistore24-termekek.md`), xlsx feltöltése, beküldés jóváhagyásra (élő oldal kell hozzá!). ?
- [ ] Digistore24 vásárlási link(ek) beírása a `LINKS` objektumba → `build_site.py` → deploy.
- [ ] **Deploy** a `site/` mappából Cloudflare Pagesre, domain hozzákötése (jóváhagyással).
- [ ] Digistore24-supportlevél elküldése az előrendelésről (`marketing/digistore24-support-level.md`). ?

## P1 – teszthét

- [ ] Várólista eszköze: Brevo-fiók → űrlap beépítése a `warteliste` gombhoz + Datenschutz 5. pont átírása.
- [ ] Facebook-oldal létrehozása (hirdetéshez kell).
- [ ] 3 Facebook-poszt a csoportokba (hétfő/szerda/péntek), előtte csoportszabályok és 1–2 nap kommentelés.
- [ ] Meta-hirdetés: 7 nap × ~7 €, DE + AT.
- [ ] Cloudflare Web Analytics bekapcsolása (cookie nélküli).
- [ ] Google Search Console + Bing Webmaster + sitemap.
- [ ] Termékkép a Digistore24-hez (Excel-képernyőképekből összeállítva).
- [ ] Teszthét kiértékelése a `docs/06-utemterv.md` kritériumai szerint.

## P2 – teszt után (ha MEGCSINÁLNI)

- [ ] Starter-Kit elkészítése (`build_kit.py` mintájára új generátor vagy bővítés).
- [ ] Reinigungsfirma OS elkészítése (Revierplanung, Nachkalkulation, Prüfprotokoll, DE/TR/SR betanító listák).
- [ ] Kit-vevőknek e-mail sorozat az OS-ről (upsell).
- [ ] Digistore24 affiliate-program beállítása.
- [ ] 249 €-s Komplettpaket koncepció.
- [ ] További ingyenes kalkulátor-oldalak SEO-ra.

## Technikai adósság / kisebb javítások

- [ ] A web-rechner és az Excel példaértékeinek egységesítése (web: 28 % LNK, 80 %, 2 500 € → 31,39 €/h; Excel: 26 %, 81,6 %, 2 000 € → 29,75 €/h).
- [ ] A web-rechner anyagköltsége fix 0,90 €/h → opcionálisan bemenet.
- [ ] Digistore24 címének ellenőrzése az Impressumban.
- [ ] `site/` mappához `_headers` fájl (Cloudflare Pages) biztonsági fejlécekkel (opcionális).
