# Norelia – teljes rendszer (2026-11-02)

## 1. Cégfelépítés
```
                        NÓRA – tulajdonos (jóváhagy, ~2-4 óra/hét a rendszerre)
                                         │
                                  FŐNÖK (fonok)
               cél: ≥ 1 M Ft/hó · rangsorol · delegál · hétfői jelentés
   ┌──────────┬──────────┬──────────┼──────────┬──────────┬──────────┬───────────┐
marketing   sales    ecommerce   penzugy   palyazat   operacio   tartalom
social,     affiliate, Etsy, KDP,  Ft/hó,     KKV/kut.   automati-  influenszer
hirdetés,   megkere-   Digistore,  Ft/óra,    pályázat   zálás      videók
SEO         sések      listingek   nullpont                         (Emily, Katrin)
```
A `tartalom` agent 2026-11-02 óta él.

## 2. Projektek és arcaik
| Projekt | Arc (AI, jelölve) | Csatornák | Állapot |
|---|---|---|---|
| AureliaVenn | **Emily** (38, anya, férj, macska, kisfiú) | Etsy, Amazon KDP, POD; IG, TikTok, Pinterest | él, 1 eladás |
| Reinigungsfirma Startsystem | **Katrin** (46, virtuális mentor) | Digistore24 + affiliate-ek; TikTok, IG, FB, LinkedIn, YT Shorts, Pinterest | tartalom keresése / újraépítés |
| Reinigungs-Kalkulator | Katrin (ugyanaz a márka) | Startsystem része + Etsy/Gumroad, később havidíj | terv |

## 3. Táblák és fájlok (ami MOST megvan)
| Hol | Mi | Ki írja |
|---|---|---|
| `CLAUDE.md` | közös szabályok, cél | Claude (Nóra jóváhagyásával) |
| `.claude/agents/*.md` | 7 agent: fonok, marketing, sales, ecommerce, penzugy, palyazat, operacio | – |
| `ceg/celok.md` | célszámok 3/6/12 hónapra | penzugy |
| `ceg/projektek.md` | portfólió + számítás | fonok |
| `ceg/projektek/*.md` | projektlapok: aureliavenn, startsystem, startsystem-affiliate | ecommerce, sales |
| `ceg/naplo.md` | döntési napló | minden agent |
| `ceg/eszkozok.md` | connectorok, hiányok | operacio |
| `ceg/heti/` | hétfői jelentések | fonok (automatikus, hétfő 6:47) |
| `ceg/adatok/` | Etsy CSV-k stb. | Nóra (havi 2 perc) |

## 4. Mi hiányzik még a teljes működéshez
### A) Nórától (fiókok, anyagok)
| # | Mi | Miért | Prioritás |
|---|---|---|---|
| 1 | AureliaVenn meglévő anyagai → Drive „Norelia/AureliaVenn” | feltöltés Etsyre/KDP-re | MAGAS |
| 2 | Startsystem anyag (ha előkerül) → Drive „Norelia/Startsystem” | különben újraépítem | MAGAS |
| 3 | **Digistore24** vendor fiók | Startsystem eladás | MAGAS |
| 4 | **Amazon KDP** fiók (adó- és bankadatokkal) | printable-ek | MAGAS |
| 5 | Social fiókok: Emily (IG, TikTok, Pinterest), Katrin (TikTok, IG, FB oldal, LinkedIn, YouTube, Pinterest) → mind a **Metricoolba** | ütemezett posztolás | MAGAS |
| 6 | Domain + landing a Startsystemhez (WordPress.com van) + **Impressum, Datenschutz** (német előírás) | Digistore és hirdetés feltétele | MAGAS |
| 7 | Gumroad: felfüggesztett kifizetés rendezése (vagy Gumroad elhagyása) | pénz beragad | KÖZEPES |
| 8 | Zapier befejezése | Etsy-adatok automatikusan | KÖZEPES |
| 9 | POD partner (Printify vagy Printful) összekötése Etsyvel | póló, pulcsi, bögre | KÖZEPES |

### B) Rendszer (Claude építi, jóváhagyás után)
| # | Mi | Hol |
|---|---|---|
| 1 | ✅ **monday táblák kész** (NóRa HéJja Vibes → Norelia mappa): Termékek 5107073512, Tartalomnaptár 5107073533, Affiliate 5107073538, KPI 5107073541 | monday.com |
| 2 | ✅ **tartalom agent kész** | `.claude/agents/tartalom.md` |
| 3 | **ügyfélszolgálat**: vevői kérdések (Etsy, Digistore) → válasz-piszkozat Gmailben | sales vagy operacio bővítése |
| 4 | ✅ Karakterlapok vázlata kész – Katrin arcát Nóra választja ki | `ceg/projektek/karakterek.md` + Higgsfield |
| 5 | Heti KPI-sor automatikusan a hétfői futásból | monday KPI tábla |
| 6 | Jogi checklist: AI-jelölés, Impressum, DSGVO, KDP és Etsy szabályok | `ceg/jogi.md` |

## 5. Heti működés (célállapot)
| Nap | Mi történik | Nóra ideje |
|---|---|---|
| Hétfő 6:47 | Főnök: jelentés, a hét 3 lépése, jóváhagyási lista | 20 perc átnézés |
| Hétfő–kedd | tartalom: heti Emily- és Katrin-csomag → Metricool (jóváhagyás után) | 15 perc |
| Szerda | ecommerce: 2–3 új listing (Etsy + KDP) | feltöltés 30 perc (amíg nincs connector) |
| Csütörtök | sales: affiliate-megkeresések, válaszok | 10 perc jóváhagyás |
| Folyamatos | ügyfélszolgálati piszkozatok | 5 perc/nap |
**Összesen: kb. 2–4 óra/hét Nórától.**
