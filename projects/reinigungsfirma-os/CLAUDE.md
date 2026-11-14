# CLAUDE.md – Reinigungsfirma OS

Ez a fájl a Claude Code projektmemóriája. Minden munkamenet elején olvasd el, utána a `docs/TODO.md`-t.

## Mi ez a projekt

**Reinigungsfirma OS**: német nyelvű digitális termékek (Excel/Google Sheets sablonok) takarítócég-tulajdonosoknak Németországban, Ausztriában és Svájcban (DACH).
- **Belépő:** ingyenes Stundensatz-Rechner a landing page-en (organikus forgalom, SEO).
- **Csali termék (azonnal eladható):** Kalkulations-Kit, 29 €.
- **Fő termékek (később, előrendelés/várólista):** Starter-Kit 49 € és Reinigungsfirma OS 99 €.
- **Értékesítés:** Digistore24 (Merchant of Record, kezeli az áfát és az elállási jogot).
- **Jogi eladó:** a tulajdonos magyar egyéni vállalkozása (EV). NEM a Knowtech Kft., NEM a PK-Tech.

**Üzleti cél:** 12 hónapon belül **1,5 M Ft/hó nettó** (≈ 4 500 €/hó bruttó bevétel) csak oldalprojektekből. Minden javaslatot ehhez mérj. Részletek: `docs/01-kontextus-es-celok.md`, ütemterv: `docs/06-utemterv.md`.

## Hogyan dolgozz a tulajdonossal (Nori)

- **Magyarul, tömören, egyszerű szavakkal.** Az ügyfeleknek szóló szöveg mindig **németül** van (Sie-forma).
- **Végrehajtás először:** készítsd el a munkát, ne leírd, hogyan kellene.
- **Proaktív pontosítás kötelező:** ha jogi, platform- vagy piaci buktatót látsz (pl. DSGVO, Impressum, Digistore24-szabály), magadtól szólj. Ne neki kelljen kitalálnia.
- **Döntésnél ez a formátum:** ÉRTÉKELÉS – DÖNTÉS – MIÉRT (2–4 pont) – KÖVETKEZŐ LÉPÉS (max 3). Több opciónál rangsorolj, és zárd így: MEGCSINÁLNI / TESZTELNI / MÓDOSÍTANI / ELVETNI.
- **Jóváhagyás kell** mindenhez, ami kimegy vagy tartósan változtat (deploy, e-mail küldés, közzététel, Digistore24 vagy más fiók módosítása). Előtte egysoros terv.
- **Előbb teszt:** legfeljebb 1 hét és 30 000 Ft alatt kapjunk piaci visszajelzést, mielőtt rendszert építünk.
- **Arctalan termék:** nincs videó a tulajdonossal, nincs ügyfélhívás, support csak e-mailben. A márka arca **Katrin, AI-karakter** (mindig jelölve: „KI-generierte Figur”), lásd `../../ceg/projektek/karakterek.md`; Nóra arca soha nem jelenik meg.
- Számításnál röviden mutasd a levezetést.

## Repó felépítése

```
CLAUDE.md                 ← ez a fájl
README.md                 ← gyors indítás, parancsok
src/landing.src.html      ← a landing page FORRÁSA (ezt szerkeszd)
site/                     ← GENERÁLT, ezt kell a Cloudflare Pagesre feltölteni
  index.html              ← build_site.py állítja elő, kézzel ne szerkeszd
  fonts/*.woff2           ← saját tárhelyről betöltött betűk (fetch_fonts.sh)
scripts/
  build_site.py           ← src → site/index.html (Google Fonts → helyi @font-face)
  fetch_fonts.sh          ← @fontsource csomagokból letölti a betűket
  build_kit.py            ← legenerálja a Kalkulations-Kit .xlsx-et
products/                 ← generált, eladható termékfájlok (.xlsx)
docs/                     ← kontextus, döntésnapló, jogi tudnivalók, ütemterv, TODO
marketing/                ← Facebook-posztok, hirdetésszöveg, Digistore24-adatok, supportlevél
```

## Parancsok

```bash
bash scripts/fetch_fonts.sh                 # egyszer, klónozás után (npm kell)
python3 scripts/build_site.py               # landing page build → site/index.html
python3 scripts/build_kit.py                # Excel termék → products/
# Excel ellenőrzés: LibreOffice-szal újraszámolni, 0 képlethiba kell
# Elvárt példaértékek: Stundensatz netto 29,75 €/h; 360 m² iroda → 1 046,71 €/hó, 2,91 €/m²
```

Deploy: a `site/` mappa tartalma kerül a Cloudflare Pagesre (direct upload, mint a többi projektnél). **Deploy csak jóváhagyással.**

## Kötelező szabályok (jogi és technikai)

1. **Google Fonts tilos külső szerverről** a deployolt oldalon (LG München 2022 → Abmahnung-hullám). A `build_site.py` ellenőrzi; ne kerüljön vissza `fonts.googleapis.com`.
2. **Nincs cookie és tracker** (Meta Pixel, GA stb.) cookie-banner nélkül. Jelenleg a Datenschutz azt állítja: „keine Cookies, kein Tracking”. Ha ez változik, a Datenschutzot is frissíteni kell.
3. **Külső CDN-t ne használj** a site-on; minden inline vagy saját fájl.
4. **Impressum kötelező** (§ 5 DDG). A placeholderek `[...]` között vannak; élesítés előtt ki kell tölteni (EV-adatok).
5. **Digistore24-jóváhagyás feltételei:** élő, nyilvános eladási oldal; ár jól látható (brutto, „inkl. MwSt.”); szállítási mód leírva; visszatérítési idő írásban (nálunk 30 nap); vásárlás gomb csak Digistore24-rendelőlapra mutathat. Lásd `docs/04-jogi-es-platform.md`.
6. **Excel-termék:** csak Excel-2007-es függvények (Google Sheets-kompatibilis). Nincs XLOOKUP, FILTER, SORT stb. Bemenet = sárga háttér + kék betű, képlet = fekete, másik lapról jövő érték = zöld. Arial betű.
7. Az ügyfélnek szóló számok mind **példaértékek**, és jelölve kell legyenek („Beispielwerte”, „Richtwert, bitte prüfen”).

## Design-rendszer (landing page)

- Koncepció: „műszerfal-pontosság” – a kalkulátor eredménye nyugtaként jelenik meg.
- Színek: petrol `#0F4C5C`, mély petrol `#0A3642`, hab `#9FE3D1`, halvány hab `#E6F6F1`, papír `#F5F7F7`, tinta `#0C1B2A`.
- Betűk: Schibsted Grotesk (szöveg, címek), JetBrains Mono (számok, címkék).
- Világos és sötét téma tokenekkel (`:root`, `prefers-color-scheme`, `[data-theme]`).
- Mobilon is működnie kell (min. 16 px oldalsó margó, nincs vízszintes görgetés).
- A tulajdonos a korábbi egyszerű dizájnt „rondának” találta: a mostani szintet tartsd vagy emeld.

## Aktuális állapot röviden

Lásd `docs/TODO.md`. Legfontosabb: az oldal **még nincs élesítve**, a domain és az EV-adatok hiányoznak, és **az oldalon lévő dátumok elavultak** (Frühbucher okt. 31., szállítás nov. 15.), ezeket élesítés előtt javítani kell.
