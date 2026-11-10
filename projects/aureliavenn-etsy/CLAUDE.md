# CLAUDE.md — AureliaVenn Etsy (POD + digitális termékek)

> Állapot: 2026-11-04. Forrás: a claude.ai „Etsy” projekt dokumentumai (utolsó heti státusz: 2026-11-02) és az eddigi döntések.
> Részletek a `docs/` mappában. Ezt a fájlt tartsd rövidnek; a változó adatok a docs-fájlokba menjenek.

## 1. Ki vagyok, mi a cél
- **Tulajdonos:** Nori (Pócz-Héjja Nóra), Magyarország. Magyarul kommunikálunk; a vevői szövegek **angolul** (US-piac), a DACH-termékek **németül**.
- **Bolt:** AureliaVenn (Etsy, shop ID a képekben: `59888443`). Pénznem: **EUR**. Eladó: EU-s (→ Omnibus-szabály érvényes).
- **Üzleti cél:** a side projektekből **1,5 M Ft/hó nettó 12 hónapon belül**. Az Etsy egy a max. 3 aktív oldalprojektből. Mérce: bevétel, megspórolt idő, lezárt feladat. Óraérték-mérce: kb. 8 750–19 000 Ft/óra.
- **Modell:** print-on-demand (Printify gyárt) + digitális letöltések (PDF, XLSX). Cél: a lehető legmagasabb profit, **automatizált eladás**.
- Nori nem akarja elengedni az Etsyt; **egész évben eladható** termék kell a szezonális mellé (budget planner irány).

## 2. Hogyan dolgozz (kötelező)
1. **Végrehajtás először.** Ha el tudod készíteni (listing-szöveg, PDF, táblázat, kép-prompt, script), készítsd el — ne leírd, hogyan kellene.
2. **Jóváhagyás kell** (egysoros terv + „mehet?”) mindenhez, ami kimegy vagy tartósan változtat: listing élesítése/módosítása, ár, Pinterest-pin kiküldése, Etsy Ads, Printify publish, közösségi poszt. Olvasás, elemzés, piszkozat, fájl: szabadon.
3. **Videót és új terméket Nori maga néz át**, mielőtt élesbe megy. **Kivétel (Nóra, 2026-11-10):** az `projects/etsy-empire` napi digitális termékei minőségi kapu után jóváhagyás nélkül élesíthetők.
4. **Őszinteség:** ha egy ötlet gyenge vagy nem visz a bevételi cél felé, mondd ki egy mondatban, és adj jobbat.
5. **Több opciónál:** rangsorolj, válassz, és zárd így: MEGCSINÁLNI / TESZTELNI / MÓDOSÍTANI / ELVETNI.
6. **Előbb teszt:** max. 1 hét és 30–50 000 Ft alatt piaci visszajelzés, mielőtt rendszert építünk.
7. **Fókuszőr:** új ötletnél mondd meg, mi menjen érte parkolópályára. Új ötlet: max 100 000 Ft és 8 óra/hét.
8. **Proaktivitás:** ha automatizálást, connectort, skillt, agentet látsz, ami pénzt/időt hoz, jelezd.
9. **Formátum:** magyarul, tömören, egyszerű szavakkal. Döntésnél: ÉRTÉKELÉS – DÖNTÉS – MIÉRT (2–4 pont) – KÖVETKEZŐ LÉPÉS (max 3). Számításnál rövid levezetés.

## 3. Nem alku tárgya (Etsy- és jogi szabályok)
- **Nincs „Embroidered” nyomtatott terméken.** Minden nyomott termék leírásában: „embroidery-look, printed design, not real embroidery”.
- **AI-jelölés:** minden leírás végén „designed by our small shop, AureliaVenn, with the help of AI tools”. Etsy „How it was made”: I did + AI generator; POD-nál production partner: **Printify** (kötelező).
- **Omnibus (EU):** áthúzott ár = az előző 30 nap legalacsonyabb ára. **Nincs állandó 40–75% „akció”.** Csak valódi, időzített akció (bevezető ár, Black Friday, december).
- **Védjegy:** „Kindness Elf is our own name… not affiliated with any elf doll brand.” Ne használd az „Elf on the Shelf” nevet.
- **Nincs egészségügyi/gyógyító állítás** (Emily-tartalmakban sem).
- **Önrendelés a mutatók felpörgetésére: ELVETVE**, ne javasold.
- **Printify-szinkron:** Printifyban „Publishing settings” → cím/leírás/tag szinkron KIKAPCSOLVA, különben a re-publish felülírja az Etsy-szövegeket.
- Digitális listing: mindig **US Letter + A4** PDF (Etsy max. 5 fájl/listing); „INSTANT DIGITAL DOWNLOAD. No physical item will be shipped.”

## 4. Mi van most (röviden)
- **24 aktív listing** (19 POD + 5 digitális) + 1 nem elérhető (Classroom Elf). Teljes lista: `docs/LISTINGS.md`.
- **Első eladás: 2026-10-30**, Kindness Elf Printable Kit, €3,99 (a dokumentált ár €5,99 → tisztázandó).
- Forgalom nagyon alacsony (heti 8 látogatás). **Etsy keresés 0, Pinterest 0.** Etsy Ads: 30 nap alatt $0,62 költés, ROAS 7,53.
- Számok és trend: `docs/METRICS.md`.

## 5. Márka és karakter
- **AureliaVenn** = semleges esernyőmárka (több influencer is befér). **Emily** (@crunchyish.emily) = közösségimédia-arc, AI-karakter (Higgsfield), US-célpiac. Részletek, asset-ID-k, szabályok: `docs/BRAND-EMILY.md`.

## 6. Repó-struktúra (javasolt — még nincs kód)
```
CLAUDE.md                 ← ez a fájl
docs/
  DECISIONS.md            ← döntésnapló (mit, mikor, miért)
  TODO.md                 ← nyitott feladatok prioritással
  LISTINGS.md             ← listing-leltár: ID, ár, állapot
  BRAND-EMILY.md          ← Emily persona, csatornák, asset-ID-k
  WORKFLOWS.md            ← heti rutin, Pinterest-módszer, listing-szabályok
  METRICS.md              ← heti számok
  MARKET-RESEARCH.md      ← Etsy bestseller tanulságok
products/<slug>/          ← termékenként: forrás, PDF/XLSX, képek, listing.md
  listing.md              ← cím (≤140), 13 tag, leírás, ár, kategória
scripts/                  ← automatizálás (pl. pinterest_schedule.js, etsy_stats_export)
reports/weekly/           ← YYYY-MM-DD-status.md heti jelentések
```
Konvenció: termék-slug kebab-case (`kindness-elf-kit`, `holiday-budget-planner`). Fájlnevek: `<Termek-Nev>-US-Letter.pdf`, `<Termek-Nev>-A4.pdf`, képek `<rövid>-1…N.jpg`.

## 7. Eszközök
- Etsy (Chrome-ból kezelve, Claude in Chrome), Printify (POD gyártás, US szállítás), Higgsfield (Emily képek/videók/hang), Canva, Pinterest (Business fiók: crunchyishemily), Google Drive/Sheets, monday.com (feladatok).
- Termékfájlok helye Nori gépén: `~/Claude/etsy-upload/<termék>/` — a fájlokat Nori húzza be az Etsybe, utána Claude élesít.

## 8. Heti ritmus
Hétfőnként: Etsy Stats + Ads számok → `reports/weekly/`, következő heti 7 Pinterest-pin terv **jóváhagyásra**, top 3 teendő. Részletek: `docs/WORKFLOWS.md`.
