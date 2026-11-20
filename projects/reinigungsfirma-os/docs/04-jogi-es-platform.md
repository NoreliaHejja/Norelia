# Jogi, adózási és platform-tudnivalók

> Nem jogi vagy adótanács. A pontokat könyvelővel és szükség esetén ügyvéddel kell megerősíteni.

## Eladó és adózás (magyar EV)

- Eladó: a tulajdonos magyar egyéni vállalkozása.
- **Közösségi adószám (HU…) kell.** A Digistore24 viszonteladóként megveszi és továbbadja a terméket, az EV a Digistore24-nek számláz (német cég, fordított adózás). Enélkül nincs kifizetés. A NAV-nál ingyenes.
- **TEÁOR:** ellenőrizni, van-e digitális termék eladására alkalmas tevékenység (pl. 58.19 „Egyéb kiadói tevékenység”). Ha nincs, az Ügyfélkapun felvehető.
- **Adózási mód** (pl. átalányadó): egyeztetni a könyvelővel az első eladás előtt.
- A Digistore24 kifizetése az EV külön bankszámlájára menjen.

## Digistore24

- Díj: 7,9 % + 1 € eladásonként, havidíj nincs.
- Merchant of Record: intézi az EU-s áfát, a német számlát és az elállási jogot (Widerruf) a pénztárban.
- Fizetési módok: PayPal, SEPA, Klarna, kártya stb.
- **Jóváhagyás:** munkanapokon kb. 48 óra. Ha egy évig nincs eladás, a jóváhagyás lejár.
- **Eladási oldal feltételei:**
  - élő és nyilvános (nincs jelszó),
  - pontos termékleírás,
  - ár jól látható, egyezik a Digistore24-ben megadottal,
  - szállítási mód leírva,
  - visszatérítési idő írásban (német termékeknél 14/30/60/90/180 nap; nálunk **30 nap**),
  - vásárlás gomb csak Digistore24-rendelőlapra mutathat.
- **Előrendelés:** a szabályzat nem említi → a supporttól megkérdezni (levél: `marketing/digistore24-support-level.md`). Ezért indul a Kit azonnal letölthető termékként.

Források:
- https://help.digistore24.com/hc/en-us/articles/23612799859345-Criteria-for-product-sales-pages
- https://help.digistore24.com/hc/en-us/articles/23612121975441-Approval-process

## Impressum (§ 5 DDG)

A szöveg a `src/landing.src.html` végén van, `<details id="impressum">`. **Kitöltendő placeholderek:**
- `[Straße Hausnummer]`, `[PLZ] [Ort]` – az EV székhelye
- `[kontakt@ihre-domain.de]` – a domainre szóló cím
- `[Nyilvántartási szám]`
- `[Adószám]`
- `[HU12345678]` – közösségi adószám

Tartalmazza még: felelős a tartalomért (§ 18 Abs. 2 MStV), fogyasztói vitarendezés, eladó = Digistore24 GmbH (St.-Godehard-Straße 32, 31139 Hildesheim). A címet élesítés előtt ellenőrizni kell.

## Datenschutz (DSGVO)

A `src/landing.src.html`-ben, `<details id="datenschutz">`. Jelenleg ezt állítja, és ennek igaznak kell maradnia:
1. Felelős: a tulajdonos (lásd Impressum).
2. **Nincs cookie, nincs tracking**; a betűk saját szerverről jönnek.
3. A kalkulátor csak a böngészőben számol, adat nem megy sehova.
4. Tárhely: Cloudflare (EU-US Data Privacy Framework).
5. Vásárlás és várólista a Digistore24-en keresztül. **Ha a várólista Brevóra kerül, ezt a pontot át kell írni** (Brevo mint adatfeldolgozó).
6. E-mail-kapcsolat.
7. Érintetti jogok, felügyeleti hatóság (NAIH).
- „Stand: Oktober 2026” → élesítéskor frissíteni.

## DSGVO-csapdák (ne kövesd el)

- **Google Fonts külső betöltése** → Abmahnung-kockázat (LG München, 2022. jan.). A build ezt kiszűri.
- **Meta Pixel / Google Analytics** cookie-hozzájárulás nélkül → tilos. A teszthez nem kell; mérés: Digistore24-statisztika + Cloudflare Web Analytics (cookie nélküli).
- Külső CDN-ek (scriptek, képek) → kerülni.
- Beágyazott YouTube/Maps → csak kétlépcsős hozzájárulással.

## Áthúzott árak (UWG / PAngV)

- Az oldalon most 79 € → 49 € és 149 € → 99 € áthúzott ár szerepel.
- Németországban az áthúzott „eredeti ár” csak akkor szabályos, ha a termék valóban kapható volt azon az áron (különben „Mondpreis”, félrevezető, Abmahnung-kockázat).
- Ezek a termékek még sosem voltak 79/149 €-ért kaphatók → **élesítés előtt az áthúzott árat törölni**, vagy átírni egyértelmű jövőbeli árra: „Frühbucherpreis bis [DATUM], danach 79 €”.

## Facebook-csoportok és hirdetés

- Sok német csoport tiltja a reklámot: előbb a szabályokat kell elolvasni, és 1–2 napig hasznosan kommentelni.
- A linket gyakran az első kommentbe kell tenni („Link im ersten Kommentar”).
- Meta-hirdetéshez Facebook-oldal kell (pl. „Reinigungsfirma OS”), személyes profilról nem lehet hirdetni.
