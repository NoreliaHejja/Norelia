# SZTE egyetemi agent

Személyes tanulmányi asszisztens a CooSpace-hez. **Csak olvas**: nem tölt fel, nem küld be, nem ír fórumba.
Ezt a kód hálózati szinten is kikényszeríti (`src/szte/scraper/guard.py`).

## Állapot

| Fázis | Tartalom | Állapot |
|---|---|---|
| 1 | Biztonság + belépés + színterek listázása | **kész, éles tesztre vár** |
| 2 | Feladatok, vizsgák, határidő-tábla, naptár | következik |
| 3 | Tananyag letöltése + kivonatolás | – |
| 4 | Beadandó-asszisztens | – |
| 5 | Lehetőségkereső | – |
| 6 | Ütemezés + napi/heti értesítés | – |

## Fontos: az új CooSpace

- A régi `coosp.etr.u-szeged.hu` már csak egy választóoldal. A felsőoktatási CooSpace új címe **https://unics.szte.hu**.
- A belépésnél **reCAPTCHA** van, és a szerver tiltja a rejtett (headless) böngészőt. Ezért:
  - a belépést **te** csinálod egy látható böngészőablakban (a program kitölti a nevet és a jelszót, te kipipálod a CAPTCHA-t),
  - a program elmenti a sessiont (`data/session.json`), és a további futások ezt használják, amíg érvényes,
  - ha lejár, e-mailt kapsz: „Lépj be újra”.
- Emiatt az agent **a saját gépeden fut**, nem felhőben.

## Telepítés (egyszer, kb. 10 perc)

1. Telepítsd a Pythont (3.11 vagy újabb): https://www.python.org/downloads/ – Windowson pipáld be: „Add Python to PATH”.
2. Töltsd le ezt a repót, és nyiss parancssort a `szte-agent` mappában.
3. Futtasd:
   ```
   python -m venv .venv
   .venv\Scripts\activate        (Windows)
   source .venv/bin/activate     (Mac)
   pip install -e .
   python -m playwright install chromium
   ```
4. Másold le a `.env.example` fájlt `.env` néven, és írd bele a Neptun-kódodat és a jelszavadat.
   A `.env` soha nem kerül gitbe.

## Használat – 1. fázis

```
python -m szte login     # megnyílik a böngésző → CAPTCHA → Belépés
python -m szte spaces    # színterek listája, szűrés a 2026/27-es tanévre
```

Eredmény:
- a képernyőn a 2026/27-es színterek listája,
- `output/szinterek.md` – ugyanez táblázatban,
- `data/debug/spaces_dump.json` – nyers adat a finomhangoláshoz (csak a gépeden marad).

**Ha a lista üres vagy hibás:** küldd el a `data/debug/spaces_dump.json` fájlt, és ebből pontosan beállítom a felismerést.

## Hibariasztás e-mailben

A `.env`-ben töltsd ki: `SMTP_USER`, `SMTP_PASS`, `ALERT_TO`. Gmailnél a `SMTP_PASS` egy
**alkalmazásjelszó** (Google-fiók → Biztonság → Alkalmazásjelszavak), nem a rendes jelszavad.

## Biztonság

- Jelszó, API-kulcs és cookie csak a `.env`-ben és a `data/` mappában van; mindkettő `.gitignore`-ban.
- A napló (`data/agent.log`) kitakarja a jelszót, a session cookie-t és a tokeneket.
- Kíméletes tempó: max. 1 oldalbetöltés másodpercenként.
- Minden írási kérést (feltöltés, beküldés, mentés, törlés, fórum) a böngésző szintjén blokkol.

## Tesztek

```
pip install -e ".[dev]" && python -m pytest
```
