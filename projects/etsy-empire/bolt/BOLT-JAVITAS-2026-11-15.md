# AureliaVenn – karácsonyi boltjavítás (2026-11-15)

## 1. Bolt szövegei (JÓVÁHAGYÁSRA VÁR – élesítéshez shops_w engedély kell, lásd lent)

### Tagline (max. 55 karakter) – válassz egyet
1. **Matching family Christmas tees, mugs & kids printables** (54) ← javaslatom: a két fő kínálatot (családi POD + gyerek-printable) egyszerre mondja ki
2. Cozy Christmas gifts & printables for the whole family (54)
3. Personalized Christmas gifts, family tees & printables (54)

### Announcement (angol)
> 🎄 Christmas 2026 order deadlines
> • Shirts, sweatshirts & mugs shipping to the USA: order by **December 9** for delivery by Christmas Eve (each item is made to order in 3–5 business days, then ships in 2–5 business days).
> • Mugs shipping to Europe and other countries: international delivery takes 10–30 business days, so we can't guarantee arrival before Christmas. For the best chance, please order by **November 19**.
> • Printables & PNG files: instant download, any time – even on Christmas Eve.
> Personalized items are printed exactly as you type them, so please double-check the spelling of every name. Thank you for shopping small! ✨

**A határidő számítása (nem becslés, a bolt saját adataiból):**
| | Gyártás (Etsy feldolgozási idő a listingen) | Szállítás (Printify-szolgáltató, standard) | Összesen | Utolsó rendelési nap dec. 24-i érkezéshez |
|---|---|---|---|---|
| USA – póló/gyerekpóló/pulóver (Printify Choice, Miami) | 3–5 munkanap | 2–5 munkanap | max. 10 munkanap | dec. 10. (0 nap tartalék) → **bejelentésben dec. 9.** (1 nap tartalék a csúcsforgalomra) |
| USA – bögre (SPOKE Custom Products, Georgia) | 2–5 munkanap | 2–5 munkanap | max. 10 munkanap | ugyanaz: dec. 9. |
| EU / egyéb – bögre (SPOKE, USA-ból) | 2–5 munkanap | 10–30 munkanap | 15–35 munkanap | legrosszabb eset: nov. 5. (már elmúlt) · középérték (20 nap szállítás): **nov. 19.** · legjobb eset: dec. 3. → garancia nincs |

Forrás: Printify API `v2/catalog/blueprints/{12,157,49,68}/print_providers/{99,1}/shipping/standard.json` (handlingTime) és a bolt Etsy readiness-state-jei (3–5 / 2–5 nap).

**Fontos lelet:** a pólók és pulóverek szállítási profilja (Printify Choice) **csak USA, Kanada és Ausztrália**. EU-ba most csak a bögre rendelhető. Mivel német printable-jeink is vannak, érdemes lehet EU-s gyártóval (pl. német/lett Printify-partner) egy EU-s póló-változatot csinálni → külön döntés.

### About (angol, frissített)
**Headline:** Cozy Christmas gifts and printables for real families

> Hi, and welcome to AureliaVenn! We're a small online shop making the holidays a little cozier and a little easier for busy families.
>
> In our shop you'll find matching family Christmas shirts and mugs (the Cookie Taster Elf is very popular in our house), personalized name gifts, cheerful designs for dog moms and bird lovers, and screen-free printables that keep kids busy, kind and creative through December – in English and in German.
>
> Our shirts, sweatshirts and mugs are printed on demand by trusted print partners, so nothing is wasted and every order is made just for you. Printables and PNG files are instant downloads you can print at home as many times as you need for your family.
>
> Our designs are created by our small team with the help of AI tools, and every product is checked by hand before it goes live.
>
> Questions about sizes, delivery dates or a personalized order? Send us a message – we usually reply within a day.

## 2. Rovatok
- 6 rovat létrehozása: **nem sikerült még** – az Etsy-kapcsolatnak nincs `shops_w` joga (403). Engedélyezési link Nórának (lásd lent). Utána 2 perc alatt létrehozom és mind a 72 terméket besorolom (`bolt/rovatok.json` kész).
- Hozzárendelés: `bolt/rovatok.md` (72 sor). 59 termék illik a 6 rovat valamelyikébe; **13 nem illik sehova** (nem karácsonyi macskás termékek, családi tervezők) – ezekre 2 új rovat javasolt: „Cat Lover Gifts” és „Family Planners & Printables”.

## 3. Termékképek (fizikai POD) – KÉSZ, élesben
| Termék | Változás |
|---|---|
| Cookie Taster / Sleepy / Bossy Elf póló (3) | új 1. kép: felnőtt viseli, közeli életkép |
| Cookie Taster / Sleepy / Bossy Elf gyerekpóló (3) | új 1. kép: gyerek viseli, közeli életkép |
| Cookie Dough and Chaos Club póló + gyerekpóló (2) | új 1. kép: sütés közben viselt póló |
| Cookie Taster / Sleepy / Bossy Elf bögre + Cookie Dough bögre (4) | a meglévő „kézben tartott” közeli kép került előre (a fehér stúdiókép / két bögre a 2. helyre) |
| Névre szóló bögre (2) + családi póló (1) | nem kellett: az 1. kép már életkép (bögre karácsonyi környezetben, család a pólókban) |
Összesen 15 termék átnézve, 12 módosítva, egy kép sem törölve (a régi fehér Printify-mockupok hátrébb kerültek).

**Eltérés a kéréstől:** a Printify mockup-könyvtárából nem tudtam lifestyle képet választani: az API csak a Printifyban kijelölt mockupokat adja (ezeknél: „front-2” fehér háttér + mérettáblázat), a teljes könyvtár csak a Printify webes felületén érhető el, és a Printify képszervere (images.printify.com) ebből a környezetből tiltott. Helyette Higgsfield-del készült életképek, a valódi dizájnnal (helyesírás ellenőrizve). Ha a Printify saját „person” mockupjait szeretnéd: Printify → termék → Mockups → jelöld ki a lifestyle képeket, és én áttolom őket első helyre.

## 4. Digitális nézőképek – KÉSZ (20/27), 7 nem ellenőrizhető
- A 20 saját termék 1. képe 4:5-ös (2000x2500) volt: négyzetes kivágásban **mind a 20-nál levágódott a felső cím-sáv és az alsó „INSTANT DOWNLOAD” sáv**.
- Javítás: új 2000x2000-es, kivágás-biztos 1. kép (a teljes borító középen, oldalt elmosott háttér) – feltöltve a régi helyére. Szkript: `scripts/square_cover.py` (új szabály: minden új termékhez ez megy első képnek).
- 7 régebbi listing (Kindness Elf Kit, Classroom Kindness Elf, Christmas Countdown, Countdown + Kindness Elf Bundle, Christmas Budget Planner, Thanksgiving Gratitude, River Coloring Pages): az eredeti kép nincs a repóban, az Etsy képszervere (i.etsystatic.com) innen tiltott → nem tudtam megnézni. 6 közülük 4:3 fekvő (2000x1500): négyzetes kivágásban oldalt 12,5–12,5% esik le – ha a cím a szélekig ér, levágódik. Kérlek, nézd meg a boltoldalon; ha engeded az i.etsystatic.com elérését, ezt is megcsinálom.

## 5. Köszönő üzenet az egyetlen vevőnek (PISZKOZAT – nem küldtem el)
Vevő: Marydith · termék: Kindness Elf Printable Kit
> Hi Marydith,
>
> Thank you so much for choosing our Kindness Elf Printable Kit – you were our very first customer, and it truly made our day! 🎄
>
> I hope your little ones are enjoying the elf's kindness notes. If you have a moment, we'd be so grateful if you could leave a short review on Etsy. As a tiny shop, every review helps other families find us.
>
> If anything didn't print the way you hoped, just reply here and I'll be happy to help.
>
> Wishing you a cozy and kind December,
> The AureliaVenn team

(Etsy-szabály: értékelésért jutalmat/kedvezményt felajánlani tilos – a piszkozat ilyet nem tartalmaz.)
