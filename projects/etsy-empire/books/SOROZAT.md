# Gentle Life Guides – tartalmas (high-content) könyvsorozat

Nóra döntése (2026-11-12): angol (német fordítás jan.-tól), 6x9 papírkönyv ff belívvel + Kindle EPUB színes képekkel, írói álnév: **Clara Whitfield**, sorozat: **Gentle Life Guides**. Cél 90–120 oldal / könyv.

## Minőségi szabályok
- Célterjedelem: **12 000–16 000 szó** könyvenként (+ munkalapok, napló). 10 000 szó alatt NEM kész.
- Hang: meleg, gyakorlatias, tegező („you”), rövid bekezdések, minden fejezet végén gyakorlat ([[box]], [[lines:N]]).
- Tilos: kitalált kutatás, statisztika, idézet, szakértő, vélemény/„olvasói visszajelzés”; kitalált végzettség az álnévhez. Esettanulmány csak egyértelműen jelölt „composite” példa.
- Lelki/szülői témánál: „not a substitute for professional help” (a builder automatikusan beteszi) + segélyvonalak, ahol releváns (US 988, UK Samaritans 116 123).
- Illusztráció: 1 színes borító (2:3, felső harmad üres a címnek) + 4 fejezetkép (4:3 akvarell), Higgsfield nano_banana_2, borító 2k/4k upscale.
- Build: `python3 scripts/build_book.py books/<slug>` → out/interior.pdf, cover.pdf, book.epub, front.jpg, KDP_FELTOLTES.md.
- Árazás: 70–90 oldal 10,99 $; 90+ oldal 12,99 $; Kindle 4,99 $ (KDP Select).


## Érzelmi szövegírás és meggyőzés (Nóra, 2026-11-12: Robert Greene + Újszászi Bogár László befolyásolástechnika)
Cím, alcím, hátsó borító, Amazon-leírás képlete:
1. **Tükör (Greene: az olvasó rejtett belső hangja).** Az első mondat az olvasó saját, ki nem mondott gondolata: „You love them more than anything. So why do you keep yelling?” → az olvasó érzi: „ez rólam szól”.
2. **Feszültség, majd felmentés.** Megnevezzük a fájdalmat (szégyen, magány, kimerültség), aztán azonnal felmentjük: „There is nothing wrong with you.” (Greene: az ember vágyik arra, hogy lássák és megértsék.)
3. **Indoklás – „mert” (Bogár: a meggyőzés kulcsa a jó „miért”).** Minden ígéret mellett ott a miért: „…because the problem isn't your love, it's your exhausted nervous system.”
4. **Konkrét átalakulás-kép.** Egy jelenet a „holnap utáni” életből (érzékszervi részletekkel): „Imagine a bedtime where you're the calm one.”
5. **Kis elköteleződés (Bogár/Cialdini: következetesség).** Kis, könnyű első lépés: „Start with one page tonight.”
6. **Bizalom (tekintély/rokonszenv) – csak igaz elemekkel.** Konkrétum (oldalszám, gyakorlatok, forgatókönyvek), meleg hang. TILOS: kitalált vélemény, „bestseller”, hamis szűkösség, kitalált szakértő vagy végzettség, ijesztgetés.
- Cím: 2–5 szó, érzelmi kép vagy belső mondat (pl. „I Didn't Mean to Yell”). Alcím: kinek + mit érez + mit kap (≤ 200 karakter).
- Borító „cover_sub”: egy érzelmi mondat, ≤ 70 karakter.

## Tartalom: valóban segítő pszichológia (bizonyítékalapú irányzatok, általánosan megnevezve, kitalált kutatás nélkül)
- Önegyüttérzés (észrevenni – közös emberség – kedvesség), kognitív átkeretezés (CBT), elfogadás és értékek (ACT), viselkedéses aktiválás (horgonyok), érzelmi coaching gyerekeknél, kötődés és „rupture & repair”, idegrendszer-szabályozás (légzés, „window of tolerance”), szorongásnál fokozatos expozíció (bátorság-létra) és a túlzott alkalmazkodás csökkentése.
- Minden fejezet: 1) felismerés („miért érzem ezt”), 2) egy eszköz, 3) gyakorlat/forgatókönyv, 4) kedves zárómondat.
- Biztonság: krízisjelek + segélyvonalak; gyerek-szorongásnál és válásnál: mikor kell szakember; jogi/pénzügyi tanács nélkül.

## Címek (érzelmi változat)
| # | Cím | Alcím |
|---|---|---|
| 1 | Still Lit | A Gentle Guide for Single Women Who Feel Alone at Christmas: Quiet the Loneliness, Face the Family Questions and Create a Season That Finally Feels Like Home |
| 2 | Give Them Back Their Wonder | A Parent's Guide to Rescuing Your Kids from Digital Noise This School Break, with 100 Screen-Free Games That Bring the Laughter Back |
| 3 | I Didn't Mean to Yell | A Gentle Guide for Moms Who Love Their Kids Fiercely and Lose Their Temper Anyway: Calmer Days, Kinder Words and the Repair That Heals |
| 4 | Who Takes Care of Mom? | A 30-Day Reset for Women Carrying the Invisible Load: Share the Mental Work, End the Quiet Burnout and Find Yourself Again |
| 5 | Brave Little Hearts | How to Help Your Anxious Child Feel Safe, Name Their Worries and Grow Courage One Small Step at a Time (Ages 4–10) |
| 6 | The Woman Who Started Over | A Mother's Guide to Rebuilding Your Life, Your Confidence and Your Children's Sense of Home After Divorce |

## Könyvek és állapot
| # | Slug | Cím | Állapot |
|---|---|---|---|
| 1 | holidays-on-my-own | Still Lit (régi munkacím: Holidays on My Own) | KÉSZ (79 old., 9,2e szó; papír 10,99 $, Kindle 4,99 $) |
| 2 | unplugged-winter-break | Give Them Back Their Wonder | VÁZLAT (a book.json-ban már az új cím/hátszöveg; az Amazon-leírást a képlet szerint újraírni) (3,8e szó) → bővíteni ~11e szóra: mind a 100 játékhoz 2–3 mondatos „how to”; új fejezetek: korosztályok szerint (2–4, 5–7, 8–12), jó képernyőidő (családi filmest, videóhívás nagyszülőkkel), dolgozó szülők túlélési terve, nagyszülők/rokonok szabályai, utazás és autózás tablet nélkül, nem-képernyős ajándékötletek |
| 3 | calm-mom-handbook | The Calm Mom Handbook – Gentle, practical tips for calmer, less shouty parenting (ages 2–10) | TERV: miért robbanunk, triggerek, 5 mp-es szünet, kapcsolódás előbb, határok kedvesen, hiszti/vita/testvérharc forgatókönyvek, reggel/lefekvés/képernyő, javítás kiabálás után, saját töltődés, 30 napos nyugodt-anya kihívás |
| 4 | the-invisible-load | The Invisible Load – a 30-day reset for moms carrying the mental load | TERV: mi a mentális teher, kiégés jelei, „család-CEO” leltár, feladatmegosztás párral/gyerekekkel (életkor szerinti házimunka-lista), beszélgetés-forgatókönyvek, rendszerek (menü, bevásárlás, naptár), határok, pihenés, 30 napos program |
| 5 | brave-little-hearts | Brave Little Hearts – helping anxious kids build resilience (ages 4–10) | TERV: normál félelem vs. szorongás, hogyan beszéljünk róla, testi jelek, légzőgyakorlatok gyerekeknek, „worry time”, bátorság-létra, iskola/alvás/elválás, szülői szorongás, mikor kérjünk szakembert; gyerekeknek szóló színezős/munkalap oldalak |
| 6 | starting-over-mom | Starting Over – a mom's guide to rebuilding life (and helping your kids) after divorce | TERV: első 90 nap, gyász és megkönnyebbülés, gyerekeknek elmondani (korosztályonként), közös szülőség határokkal, pénzügyi újraindulás (általános, nem tanácsadás), új otthon és rutin, magány, önbizalom, randizás később, 12 hónapos terv; jogi/pénzügyi tanács nélkül |

Ütemezés: naponta 1 könyv (nov. 13: #2 bővítés, nov. 14: #3, nov. 15: #4, nov. 16: #5, nov. 17: #6). Minden kész könyv zip-ben Nórának + napló.
