# Trading – prop firm (futures)

**Státusz:** SZÜNETEL → TESZT-jelölt (Nóra döntésére vár). Áthozva a Kft. rendszerből 2026-11-10-én.
**Felelős agent:** `fonok` (prioritás), a szabályőr skill elkészülte után külön trading-skill.

## Kiinduló helyzet
- Eddig: **Apex Trader Funding**, **Tradovate** platformon.
- Gép: **Mac**. A NinjaTrader csak Windowson megy rendesen, ezért nem opció.
- Nóra kérdése: van-e olyan prop firm, ahol **bot / automatizált kereskedés** engedélyezett.

## Prop firmok összevetése (2026-11-07, másodlagos forrásokból: élesítés előtt a cég saját súgójában ellenőrizni kell)
| Cég | Bot / automatizálás | Mac | Megjegyzés |
|---|---|---|---|
| **Lucid Trading** | engedélyezett vizsgán és funded számlán is (automata rendszer + trade copier) | Tradovate + TradingView | **legkisebb váltás**, ugyanaz a platform |
| Topstep | saját bot a TopstepX / ProjectX API-n keresztül | böngészős platform | API 29 $/hó; élő funded számlán nincs API; csak saját gépről (VPS/VPN tilos); HFT tilos |
| Tradeify | csak saját fejlesztésű, saját tulajdonú stratégia | Tradovate | vett vagy bérelt bot tilos |
| Apex (jelenlegi) | vizsgán és felügyelettel igen; funded számlán a teljesen automata tilos | Tradovate | a források ellentmondanak, botnak kockázatos |
| Take Profit Trader | tiltja | – | kerülendő |

**Bot bekötése Macről:** TradingView riasztás (webhook) → felhős összekötő (PickMyTrade / CrossTrade / TradersPost) → Tradovate. A TradingView webhookhoz fizetős csomag kell.

## Döntés (javaslat, 2026-11-07)
**TESZTELNI: Lucid, egy vizsgaszámla.**
- Ugyanaz a Tradovate, nincs betanulási idő.
- Kifejezetten engedi az automatizálást, így nem zárnak ki a funded számlán.
- Kockázat: magas. Sokan elbuknak a challenge-en, és a díj elveszik. **Nem lehet a havi 1,5 M Ft fő pillére.**
- Megvett, „kész” botot nem használunk. Csak olyan stratégiát automatizálunk, amit Nóra kézzel már nyereségesen kereskedett.

## Teszt-keret
- 1 vizsgaszámla, **legfeljebb 30–50 000 Ft összesen** (vizsgadíj + TradingView + összekötő), 30 nap.
- Siker: a vizsga szabályszegés nélkül sikerül. Kudarc: szabályszegés vagy a keret elfogy → ELVETNI vagy MÓDOSÍTANI.
- Fókusz: ez Nóra-időt visz. Ha indul, egy másik projekt a heti 3 Nóra-idős projekt közül parkolóba megy.

## Megvizsgált eszköz: day-trader-skill (github.com/Jakeschincariol/day-trader-skill)
- **Biztonság:** rendben. MIT licenc, csak a Python beépített könyvtárait használja, csak nyilvános adatot olvas (Yahoo, SEC, Nasdaq). Megbízást csak dupla jóváhagyással ad, alapból paper számlán.
- **Prop firmhöz:** gyenge. Csak amerikai részvény és Alpaca bróker; futures, Tradovate és prop-szabályok nincsenek benne (equity-alapú napi limit, trailing drawdown, konzisztencia, hírek körüli tilalom).
- **Döntés: ELVETNI** így. Átvenni a két jó ötletét: a kötelező kockázati kaput (minden trade előtt ENGEDÉLY/TILTÁS), és hogy belépés előtt visszateszteljük a setupot.

## Következő lépések
1. Nóra: a Lucid súgójából bemásolja az automatizálási és a drawdown-szabályokat, és megadja a számlatípust (pl. LucidFlex 50K).
2. Claude: **prop-szabályőr skill** a Lucid szabályaira: equity-alapú napi limit, trailing drawdown, konzisztencia, hírek körüli tiltott idősávok, minden trade előtt ENGEDÉLY/TILTÁS, napi napló. Kb. 1 óra.
3. Nóra: dönt, melyik projekt megy parkolóba a teszt idejére.

## Kapcsolódó
- `ceg/portfolio/PROJECTS.md` → PARKOLÓPÁLYA: „Trading (prop firm)”
- Várólista: szerb / román prop firm összehasonlító oldal (affiliate-ötlet, külön projekt)
