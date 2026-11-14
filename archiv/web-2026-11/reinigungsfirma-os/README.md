# Reinigungsfirma OS – Landing oldal

Új design szerinti verzió. A korábbi, teljes ajánlatot (Kit 29 €, Starter 49 €, OS 99 €) és Impressum/Datenschutz részt tartalmazó oldal: `../reinigungsfirma-os-v1/`.

Statikus oldal (HTML + CSS + vanilla JS), nincs build lépés. Bármilyen tárhelyre feltölthető (WordPress: egyedi HTML-oldal vagy fájlfeltöltés).

- `index.html` – az oldal
- `styles.css` – színek és típusok a design szerint (Archivo + Manrope, zöld #0B6E4F, borostyán #F2A93B)
- `rechner.js` – Stundensatz-Rechner: Lohn → +SV → +Ausfall → +Gemeinkosten → +Gewinn; DE 19% / AT 20% MwSt.

## Élesítés előtt kitöltendő
| Helyőrző | Mi kerül ide |
|---|---|
| `[PREIS]` | a Kit ára (pl. 47) |
| `[DIGISTORE24-LINK]` | Digistore24 rendelési link |
| `[NEWSLETTER-LINK]` | feliratkozó űrlap címe (e-mail szolgáltató) |
| `[DATENSCHUTZ-LINK]`, `[IMPRESSUM-LINK]`, `[AGB-LINK]` | kötelező jogi oldalak (DE/AT) |

Helyben megnyitás: `index.html` dupla kattintással.
