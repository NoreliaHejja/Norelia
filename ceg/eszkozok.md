# Eszközök és bekötések

## Már bekötve (működik)
| Terület | Eszköz | Mire használjuk |
|---|---|---|
| Social média | **Metricool** | posztok ütemezése (IG, FB, TikTok, Pinterest, LinkedIn, YouTube), elemzés, legjobb időpont |
| Kép / videó / design | **Higgsfield** (Canva helyett) | termékképek, mockupok, social grafikák, videók, TikTok közzététel |
| Marketing adatok | **Supermetrics** | hirdetések, GA, IG, YouTube statisztika egy helyen |
| Outreach | **Apollo.io** | leadlisták, e-mail szekvenciák |
| CRM / feladatok | **monday.com** | pipeline, feladatok, heti dashboard |
| Weboldal | **WordPress.com** | landing oldalak, blog |
| Iroda | Gmail, Naptár, Drive, Sheets, Docs, Microsoft 365 | e-mail piszkozat, adatok, riportok |
| Design | Figma | |

## Marketing-skillek (boring-marketing-skills, MIT, telepítve 2026-11-26)
32 skill a `.claude/skills/` alatt (forrás: `.claude/skills/BORING-MARKETING-FORRAS.txt`). Hookok és ütemezett rutinok NINCSENEK telepítve.
Több cég → „agency mód”: márkafájlok `./brands/<slug>/` (pl. `reinigungsfirma-os`, `pk-tech`, `pedexan`, `aureliavenn`). Indítás: `/start-here <cég>`.
| Cég / projekt | Első skillek (sorrendben) | Mit hoz |
|---|---|---|
| Reinigungsfirma OS + Kalkulator (DACH) | positioning-angles → direct-response-copy → landing-page (teardown) → lead-magnet (kalkulátor) → email-sequences | a landing konverziója, e-mail-lista |
| PK-Tech (helyi ipari takarítás) | google-business-profile → reviews → first-screen-check → speed-to-lead → local-seo-plan | több hívás és ajánlatkérés helyi keresésből |
| Pedexan / Knowtech (B2B) | competitive-intel → positioning-angles → email-sequences (cold outbound) → ai-search | munkavédelmi boltok és gyárak megkeresése |
| AureliaVenn / Etsy, Gentle-könyvek | audience-research → keyword-research → content-atomizer → performance-review | vevői szóhasználat, Pinterest/social |
| Minden cég havonta | performance-review, ai-search | mérés, AI-ajánlások figyelése |
Fizetős API csak ha Nóra kéri (Firecrawl, Replicate, Google Places, Meta) – nélkülük is működnek.

## Félig bekötve – Nórának kell befejezni (claude.ai → Beállítások → Connectors)
| Eszköz | Állapot | Miért kell |
|---|---|---|
| **Zapier** | csatlakozás befejezetlen | Etsy és más, connector nélküli rendszerek bekötése |
| ElevenLabs | befejezetlen | hang YouTube/TikTok videókhoz |
| Descript | nincs csatlakoztatva | videóvágás |

## Nincs bekötve – javasolt
| Eszköz | Megoldás | Prioritás |
|---|---|---|
| **Etsy** | nincs hivatalos connector → **Zapier** (új rendelés/listing → Google Sheet), vagy AnythingMCP (van Etsy-modulja), vagy heti CSV export Etsyből a `ceg/adatok/` mappába | MAGAS |
| **Amazon** (Account ID: A1BYNK4N45CETG) | Seller Central → **Amazon Selling Partner** connector (claude.ai → Beállítások → Connectors, OAuth). **KDP-hez nincs API/connector** → feltöltés kézzel (Claude elkészíti a belívet, borítót, leírást) | MAGAS |
| Gumroad / Digistore24 | eladási e-mailek a Gmailben → automatikusan olvasom | MAGAS |
| TikTok Shop | AfterShip Channels for TikTok Shop | KÉSŐBB |
| Meta/TikTok hirdetés | Adspirer Social Ads | ha lesz hirdetési keret |
| YouTube kutatás | vidIQ | ha a YouTube aktív |

## Hogyan látok rá a projektekre
1. **Gmail (már működik)**: Etsy heti riport, eladási e-mailek, Gumroad/Digistore értesítők → a hétfői futás ezekből számol.
2. **Havi Etsy CSV**: Shop Manager → Settings → Options → Download Data (Orders + Listings) → Drive `Norelia/adatok` mappa. 2 perc/hó.
3. **Projektleírás egyszer**: minden projekthez 1 oldal a `ceg/projektek/` mappában (mi a termék, ár, hol árulod, link).
