# CLAUDE.md — Nori side projektjei (Új bevételi források)

> Ezt a fájlt Claude Code minden munkamenet elején beolvassa. Tömör, döntésközpontú. Részletek: `docs/`.
> Utolsó frissítés: 2026-11-04

## 1. Ki vagyok, mi a cél

- **Tulajdonos:** Pócz-Héjja Nóra (Nori). Magyar, németül és angolul folyékonyan beszél. B2B sales és digitális marketing háttér.
- **Cél:** a PK-Techen kívüli nettó jövedelem **12 hónapon belül 2 M Ft/hó, 24 hónapon belül 3 M Ft/hó**. A side projekteknek önmagukban **1,5 M Ft/hó** kell hozniuk egy éven belül.
- **Időkeret:** max 30 óra/hét az oldalprojektekre. Óraérték-mérce: **8 750–19 000 Ft/óra**. Minden feladatot ehhez mérj.
- **Új ötlet költségkerete:** max 100 000 Ft és 8 óra/hét. Kockázatvállalás: közepes/magas.

## 2. Hatókör — mivel foglalkozik ez a repó

**Benne van:** side projektek és új bevételi források (lásd `docs/PROJECTS.md`).

**NINCS benne (ne javasolj, ne dolgozz rajta):** Pedexan, Bacoban, PK-Tech, faldiagnosztika.hu. Ezek a fő cégek / más projekt ügyei.

## 3. Működési szabályok

1. **Végrehajtás először.** Ha meg tudod csinálni (kód, szöveg, számítás, dokumentum), csináld meg. Ne írd le, hogyan kéne.
2. **Autonómia:**
   - Szabadon: olvasás, kutatás, elemzés, piszkozat, fájl létrehozása a repóban.
   - **Egysoros terv + jóváhagyás kell:** minden, ami kimegy vagy tartósan változtat — deploy, közzététel, e-mail küldés, Apollo/monday.com írás, fizetős szolgáltatás, fájl törlése/mozgatása.
3. **Őszinteség:** ha egy ötlet gyenge, vagy nem visz közelebb a jövedelmi célhoz, mondd ki egy mondatban, és adj jobbat.
4. **Döntésnél rangsorolj**, válassz, és zárd így: `MEGCSINÁLNI / TESZTELNI / MÓDOSÍTANI / ELVETNI`.
5. **Előbb teszt:** max 1 hét és 30–50 000 Ft alatt legyen piaci visszajelzés, mielőtt rendszert építünk.
6. **Fókuszőr: max 3 aktív projekt.** Ha új jön, mondd meg, mi menjen érte parkolópályára.
7. **Proaktivitás:** ha pénzt vagy időt hozó lehetőséget látsz (connector, skill, automatizálás, saját agent), jelezd.
8. **Ship first, expand second.** Nem építünk spekulatívan funkciókat monetizációs teszt nélkül.
9. **Reject before refining.** Ha egy ötlet elbukik az alapteszten, tiszta elvetés és váltás.

## 4. Kommunikáció

- **Magyarul**, tömören, egyszerű szavakkal. Egyszerű kérdésre közvetlen válasz.
- Döntési formátum: **ÉRTÉKELÉS – DÖNTÉS – MIÉRT (2–4 pont) – KÖVETKEZŐ LÉPÉS (max 3)**.
- Számításnál röviden mutasd a levezetést.
- A termékek nyelve a célpiacé: angol (US, Etsy), német (DACH), szuahéli (ZanaHalisi).

## 5. Repó-struktúra

```
.
├── CLAUDE.md                 ← ez a fájl
├── docs/
│   ├── PROJECTS.md           ← portfólió: aktív / parkoló / elvetett
│   ├── DECISIONS.md          ← döntési napló (dátummal)
│   ├── TASKS.md              ← nyitott feladatok projektenként
│   ├── LEARNINGS.md          ← technikai és stratégiai tanulságok
│   └── TOOLING.md            ← eszközök, fiókok, platformok
└── projects/
    ├── haccp-app/            ← AKTÍV (specifikáció hiányzik)
    ├── reinigungsfirma-os/   ← AKTÍV — DACH landing + Stundensatz-Rechner
    ├── law-firm-websites/    ← TESZT — ügyvédi irodai weboldalak
    ├── complystarterkit/     ← élő termék (Gumroad), Python/ReportLab PDF
    ├── aurelia-venn/         ← Etsy digitális + POD
    └── zanahalisi/           ← PARKOL — statikus szuahéli utility oldal
```

Minden `projects/<név>/` mappában legyen egy `README.md` (cél, státusz, következő lépés, kill-kritérium).

## 6. Technikai konvenciók

- **Statikus oldalak:** egyetlen önálló `index.html` (HTML+CSS+JS egy fájlban), mellé `robots.txt`, `sitemap.xml`, `og-image.png`. Hosting: **Cloudflare Pages, direkt feltöltés (nincs Git-összekötés)**.
- **Deploy előtt kötelező ellenőrzés:** a fájlnevek pontosan egyezzenek (`index.html`, nem `index 2.html` — macOS átnevezi a duplikált letöltéseket, ez egyszer már 404-et okozott). Mindig **az összes fájlt egyszerre** töltsd fel, mert a direkt feltöltés lecseréli a teljes deployt.
- **PDF termékek:** Python + ReportLab. Lásd `docs/LEARNINGS.md` (checkbox-trükk, egy `Paragraph` / elem, `onFirstPage`/`onLaterPages`, vektoros piktogramok, QA `pdf2image` 110 DPI-n).
- **Képek/grafika:** saját vektoros rajz vagy saját generálás — idegen képet nem importálunk (licenckockázat).
- **Jogi szövegek:** compliance termékekben tilos "OSHA audit" vagy "certified" ígéret; a felelősség az ügyfélé. Weboldalakhoz ÁSZF + adatkezelési tájékoztató kell.
- **Értékesítés jogalanya:** a digitális termékek (pl. Reinigungsfirma OS) Nori **egyéni vállalkozásán** keresztül mennek, nem a Knowtechen.

## 7. Most a legfontosabb (2026. nov. eleje)

Lásd `docs/TASKS.md`. Röviden:
1. **Reinigungsfirma OS** — német landing + ingyenes Stundensatz-Rechner + Kalkulations-Kit csali termék Digistore24-en → első valódi eladás.
2. **Ügyvédi weboldal-teszt** — 1 demóoldal + Apollo-megkeresés → első fizető ügyfél.
3. **HACCP app** — hiányzik a specifikáció; első lépés: Norival tisztázni a célcsoportot, árazást, MVP-t.

Az aktív projektek száma most több mint 3 → a heti tervezésnél javasolj szűkítést.
