# Landing page felépítése

Forrás: `src/landing.src.html` (egyetlen fájl: `<title>`, Google Fonts linkek, `<style>`, markup, `<script>`).
Build: `scripts/build_site.py` → `site/index.html` (teljes HTML-dokumentum, `lang="de"`, meta description, helyi `@font-face`).

A forrás egy claude.ai artifactként is fut (privát előnézet): https://claude.ai/artifact/NNgHdqbZRDSqNe87mgCY9x. Az artifact a Google Fonts-os változatot használja, ez előnézetre jó, élesre nem.

## Szekciók sorrendben

1. **Hero** (petrol háttér): címsor „Was kostet Ihre Reinigungsstunde wirklich?”, 3 bizonyító pont, mellette a **Stundensatz-Rechner**.
2. **Drei Rechenfehler**: 3 hiba (≈ 20 % kiesés, m²/h pauschal, €/hó rezsi).
3. **`#vorverkauf` sáv**:
   - kiemelt doboz: **Kalkulations-Kit 29 €, „Sofort verfügbar”**,
   - két árkártya: Starter-Kit 49 € és Reinigungsfirma OS 99 € (előrendelés),
   - 3 tény: szállítás dátuma, 30 napos garancia, Excel és Google Sheets.
4. **FAQ** (4 kérdés).
5. **CTA**: várólista.
6. **Footer + Impressum + Datenschutz** (`<details>`, a `#impressum` / `#datenschutz` hash kinyitja).

## Vásárlási linkek

A `<script>` elején:

```js
const LINKS = { kit: "", starter: "", os: "", warteliste: "" };
```

Üres érték esetén a gomb nem visz sehova, csak egy „öffnet in Kürze” üzenetet mutat. Ha a Digistore24-link megvan, ide kell beírni, és a gomb új lapon nyitja.

## Kalkulátor-logika (JS)

Bemenetek (csúszka + számmező szinkronban): Stundenlohn (15 €), Lohnnebenkosten (28 %), Produktive Zeit (80 %), Gemeinkosten/hó (2 500 €), verrechenbare Stunden/hó (800), Wagnis & Gewinn (12 %). Anyag fix: 0,90 €/h.

```
lohn   = Stundenlohn × (1 + LNK) ÷ produktiv
gk     = Gemeinkosten ÷ Stunden
selbst = lohn + gk + 0,90
preis  = selbst × (1 + Gewinn)
```

Példaértékekkel: **31,39 €/h**.

> Eltérés az Excellel: az Excel példái 26 % LNK, 81,6 % produktív idő, 2 000 € rezsi → 29,75 €/h. Mindkettő példa, de érdemes egységesíteni (lásd TODO).

## Design-tokenek

| Token | Világos | Sötét |
|---|---|---|
| `--paper` | #F5F7F7 | #0A131A |
| `--card` | #FFFFFF | #111D26 |
| `--ink` | #0C1B2A | #E4ECEE |
| `--muted` | #5B6975 | #93A4AE |
| `--petrol` | #0F4C5C | #0D3F4C |
| `--petrol-deep` | #0A3642 | #082C35 |
| `--foam` | #9FE3D1 | #8FDCC7 |
| `--foam-soft` | #E6F6F1 | #102B28 |

Betűk: Schibsted Grotesk 400–800, JetBrains Mono 400–600 (OFL licenc, @fontsource csomagokból).

## SEO-alapok

- Title: „Stundensatz-Rechner für Reinigungsfirmen | Reinigungsfirma OS”
- Fő kulcsszavak: Stundensatz Reinigungsfirma, Stundensatz Gebäudereinigung berechnen, Reinigung Kalkulation Excel, Angebot Unterhaltsreinigung.
- Élesítés után: Google Search Console + Bing Webmaster (mint a többi projektnél), sitemap.
