# Termékek és árak

| Termék | Ár (bruttó) | Állapot | Kinek |
|---|---|---|---|
| Stundensatz-Rechner (web) | ingyenes | kész, a landing page-en | mindenki (forgalomszerzés) |
| **Kalkulations-Kit** | **29 €** | **kész** (`products/`), Digistore24-be feltöltendő | belépő vásárlás |
| Starter-Kit | 49 € (áthúzva 79 €) | még nincs elkészítve | induló cégek |
| Reinigungsfirma OS | 99 € (áthúzva 149 €) | még nincs elkészítve | működő cégek |
| Komplettpaket (terv) | ~249 € | ötlet, 3. hónaptól | nagyobb cégek |

Digistore24-díj: 7,9 % + 1 € eladásonként. Garancia: 30 nap.

## Egységnyi számítás (a célhoz)

- 1,5 M Ft nettó ≈ 4 500 €/hó bruttó bevétel.
- Csak OS-ből (99 €): ~45 eladás/hó.
- Csak Kitből (29 €): ~155 eladás/hó → önmagában nem elég, ezért a Kit csak belépő.
- Cél-mix: Kit-vevők 20–30%-a később OS-t vesz; 249 €-s csomag + affiliate → ~25–30 eladás/hó is elég lehet.

## Kalkulations-Kit (29 €) – tartalom

Fájl: `products/Kalkulations-Kit_Reinigungsfirma_v1.0.xlsx`, generálja: `scripts/build_kit.py`. 211 képlet, 0 hiba.

| Lap | Mit csinál |
|---|---|
| **Start** | Használati útmutató, színjelmagyarázat, figyelmeztetések (példaértékek, Lohnnebenkosten-irányértékek, DE/AT/CH áfa, Google Sheets) |
| **Stundensatz** | Bér + munkáltatói járulék (21 %) + egyéb (5 %); kiesés: 261 munkanap − 26 szabadság − 10 ünnep − 12 betegség → 81,6 % produktív; rezsi (8 tétel, 2 000 €/hó) ÷ 800 óra; anyag 0,90 €/h; kockázat és nyereség 12 %; áfa 19 %. **Eredmény: 29,75 €/h nettó** (35,40 € bruttó) |
| **Leistungswerte** | 15 helyiségtípus m²/óra irányértékkel (pl. iroda kárpit 180, folyosó 300, WC 60, teakonyha 110), mind szerkeszthető, 2 saját sor |
| **Objektkalkulation** | Max 20 sor: terület, helyiségtípus (legördülő), heti gyakoriság → óra/takarítás, óra/hó (×4,33), költség/hó. Kiszállás, éjszakai/hétvégi felár. **Példa:** 360 m² iroda → 29,4 óra/hó → **1 046,71 €/hó nettó, 2,91 €/m²** |
| **Angebot** | Automatikusan kitöltődő, A4-es árajánlat; cégadatok, feltételek szerkeszthetők |

Formázási szabályok: Arial; bemenet sárga háttér + kék betű; képlet fekete; másik lapról jövő érték zöld; csak Excel-2007-es függvények.

## Starter-Kit (49 €) – tervezett tartalom

- Stundensatz- és Objektkalkulation (a Kit alapján)
- Angebotsvorlage m² és takarítási gyakoriság szerint
- Leistungsverzeichnis (iroda, rendelő, lépcsőház)
- Checkliste: Gewerbeanmeldung és biztosítások

## Reinigungsfirma OS (99 €) – tervezett tartalom

- Minden a Starter-Kitből
- Einsatz- und Revierplanung max 50 dolgozóig
- Nachkalkulation: Soll- vs. Ist-Stunden objektumonként
- Qualitätskontrolle: Prüfprotokoll ügyfeleknek
- Einarbeitungs-Checklisten németül, törökül és szerbül

## Tervezett további ingyenes kalkulátorok (SEO, 2027 febr.–márc.)

- Glasreinigung-Rechner
- Unterhaltsreinigung m²-Preis-Rechner
- (Ötlet) Angebotsrechner Treppenhausreinigung
