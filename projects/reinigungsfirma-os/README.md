# Reinigungsfirma OS

Német nyelvű kalkulációs sablonok takarítócégeknek (DACH), ingyenes Stundensatz-Rechnerrel a landing page-en. Értékesítés Digistore24-en.

## Gyors indítás

```bash
# 1. Betűtípusok letöltése (egyszer; npm kell)
bash scripts/fetch_fonts.sh

# 2. Landing page build
python3 scripts/build_site.py          # → site/index.html

# 3. Excel termék build (openpyxl kell)
python3 scripts/build_kit.py           # → products/Kalkulations-Kit_Reinigungsfirma_v1.0.xlsx
```

Az Excel képleteit LibreOffice-szal érdemes újraszámolni és hibára ellenőrizni (0 hiba az elvárt).

## Deploy

A `site/` mappa tartalmát kell feltölteni a Cloudflare Pagesre (direct upload). A forrás a `src/landing.src.html`. A `site/index.html` generált fájl, kézzel ne szerkeszd.

## Dokumentáció

| Fájl | Tartalom |
|---|---|
| `CLAUDE.md` | Szabályok és kontextus Claude Code-nak |
| `docs/01-kontextus-es-celok.md` | Üzleti háttér, célok, célcsoport |
| `docs/02-dontesnaplo.md` | Minden eddigi döntés dátummal és indoklással |
| `docs/03-termekek-es-arak.md` | Termékek, árak, tartalom, Excel-felépítés |
| `docs/04-jogi-es-platform.md` | Impressum, Datenschutz, DSGVO, Digistore24, adózás |
| `docs/05-weboldal-felepites.md` | Landing page szekciók, kalkulátor-logika, build |
| `docs/06-utemterv.md` | 12 hónapos mérföldkövek és tesztkritériumok |
| `docs/TODO.md` | Nyitott feladatok prioritás szerint |
| `marketing/` | Posztok, hirdetés, Digistore24-termékadatok, supportlevél |
