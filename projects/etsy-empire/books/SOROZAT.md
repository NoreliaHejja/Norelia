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

- **Emberi hang – kötelező szerkesztői kör (Nóra, 2026-11-17):** minden fejezetfájl megírása után, build előtt: angol szövegnél a `humanizer` skill (.claude/skills/humanizer), német szövegnél a `humanizer-de` skill (`python3 .claude/skills/humanizer-de/scripts/humanizer_audit.py --file <fájl> --mode locker`, majd a pass-ok). Mérce: `books/WRITING-RULES-anti-ai.md` (tiltott szavak: delve, tapestry, journey…, gondolatjel-keret, „not X but Y”, összefoglaló zárás, túlmagyarázás). A tartalom, a szkriptek, a segélyvonalak és a tények nem változhatnak (claim-lock); kitalált személyes élmény tilos. Ez minőségi szerkesztés, nem az AI-közlés kikerülése: a KDP-n az AI-használatot továbbra is jelöljük.

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
| 2 | unplugged-winter-break | Give Them Back Their Wonder | KÉSZ (83 old., 10,1e szó, 25 fejezet; papír 12,99 $, Kindle 4,99 $) |
| 3 | calm-mom-handbook | I Didn't Mean to Yell (HOSSZÚ) | KÉSZ (2026-11-18): 139 old., 24,2e szó (a 28e-s célnál rövidebb; töltelék helyett a hiányzó tartalom: Ten Hard Moments), 17 fejezet + Quick Finder + 30 napos terv + hűtőkártya + mondatgyűjtemény + GYIK + Further reading; papír 14,99 $, keménytáblás 22,99 $ (borító becsült 14,077×10,417 in), Kindle 5,99 $; humanizer-kör kész |
| 4 | the-invisible-load | The Invisible Load – a 30-day reset for moms carrying the mental load | TERV: mi a mentális teher, kiégés jelei, „család-CEO” leltár, feladatmegosztás párral/gyerekekkel (életkor szerinti házimunka-lista), beszélgetés-forgatókönyvek, rendszerek (menü, bevásárlás, naptár), határok, pihenés, 30 napos program |
| 5 | brave-little-hearts | Brave Little Hearts – helping anxious kids build resilience (ages 4–10) | TERV: normál félelem vs. szorongás, hogyan beszéljünk róla, testi jelek, légzőgyakorlatok gyerekeknek, „worry time”, bátorság-létra, iskola/alvás/elválás, szülői szorongás, mikor kérjünk szakembert; gyerekeknek szóló színezős/munkalap oldalak |
| 6 | starting-over-mom | Starting Over – a mom's guide to rebuilding life (and helping your kids) after divorce | TERV: első 90 nap, gyász és megkönnyebbülés, gyerekeknek elmondani (korosztályonként), közös szülőség határokkal, pénzügyi újraindulás (általános, nem tanácsadás), új otthon és rutin, magány, önbizalom, randizás később, 12 hónapos terv; jogi/pénzügyi tanács nélkül |

Ütemezés: naponta 1 könyv (nov. 13: #2 bővítés, nov. 14: #3, nov. 15: #4, nov. 16: #5, nov. 17: #6). Minden kész könyv zip-ben Nórának + napló.

## Piaci tanulságok → stratégia (Nóra kutatása, 2026-11-17; részletek: `piackutatas/konyvpiac-2026-11-17.md`)
1. **Papír > Kindle.** Minden Gentle-könyv papír + **keménytáblás** (6x9, 75+ oldaltól; ár: papír +8 $, pl. 15,99 → 23,99 $); Kindle csak belépő ár. Teendő: `build_book.py` keménytáblás borító (wrap) – a Yell 3/3 buildjével együtt.
2. **Quick Finder minden könyvben:** a tartalomjegyzék után 1–2 oldal „When you… → page” (helyzet szerinti mutató). a Yell 3/3-ban kerül be először.
3. **Hit-alapú anyás vonal (TESZT, 1 könyv):** „Faith & Motherhood” alsorozat – témák szerint rendezett igék (csak közkincs fordítás: **World English Bible**) + rövid saját elmélkedés + ima + napló sor; zsebméret 5x8, ~130 oldal, papír 9,99 $, Kindle 2,99 $. Munkacím: *Grace for the Mom Who Yelled Today* (a Yell könyv témája, más polc). Tilos: kitalált teológus, egyházi jóváhagyás, „bestseller”. Mérés: 30 nap; ha ≥ a Gentle átlag, jöhet a 2. (mentális teher, határok).
4. **Arány:** 80% örökzöld, 20% szezonális cím. Új címet csak alkategória-ellenőrzés után (a top 10 BSR-je és értékelésszáma), fej-kulcsszó helyett.
5. **Nem csinálunk:** orvosi/túlélési szakkönyvet, licencelt karaktert, csak-Kindle kiadást.

**Új sorrend:** #3 Yell (HOSSZÚ, 3/3) → **Faith-teszt (rövid)** → #4 Who Takes Care of Mom? (rövid) → #5 Brave Little Hearts (HOSSZÚ) → #6 The Woman Who Started Over.

## Több csatorna: tredition (DACH) + IngramSpark (angol) – Nóra, 2026-11-19
- **Csak a nyomtatott könyvek mennek szélesre.** A Kindle e-könyv KDP Selectben marad (Kindle Unlimited-olvasás + ingyenes akciók, pl. Noch brennt das Licht 7 letöltés). Select alatt az e-könyv máshol nem árulható.
- **Saját ISBN kell.** A KDP ingyenes ISBN-je máshol nem használható. Új könyvnél: saját ISBN (magyar EV kiadóként, OSZK ISBN Iroda – Nóra ellenőrzi a díjat), és ugyanaz az ISBN megy a KDP-re, az IngramSparkra / tredition-re. Már kint lévő könyvnél (KDP ISBN-nel): a szélesebb csatornára új ISBN-nel, új kiadásként megy.
- **Átfedés Amazonnal:** az IngramSpark és a tredition is listázhatja a könyvet az Amazonon. Ugyanazzal a saját ISBN-nel a KDP-papírkönyv mellett: a KDP „Expanded Distribution” KI, az IngramSparkban az Amazon-csatorna marad (ugyanaz az ISBN → egy termékoldal). Feltöltés előtt Nóra ellenőrzi a felületen, hogy a tredition kizárja-e az Amazont.
- **Fájlok:** a belív ugyanaz (6x9, beágyazott fontok). Borító: mindkét platform saját sablont / gerincszámítást ad → a sablon méretét (W×H, gerinc) Nóra küldi, `scripts/hardcover_cover.py`-hoz hasonló generátorral készül.
- **Sorrend:** német könyvek → tredition (Noch brennt das Licht, Gib ihnen ihr Staunen zurück, később Ich wollte nicht schreien); angol könyvek → IngramSpark (Still Lit, Give Them Back Their Wonder, I Didn't Mean to Yell).

## Német változatok (Nóra, 2026-11-12: MINDEN könyv németül is)
- Szabály: minden angol könyvnek legyen német párja (amazon.de, EUR ár). Nem szó szerinti fordítás: természetes, meleg német, du-forma, a német piac szokásai (hétfővel kezdődő hét, cm-méretek, Kita/Schule).
- Német segélyvonalak: Telefonseelsorge 0800 111 0 111 / 0800 111 0 222 (DE), 142 (AT), 143 (CH); Nummer gegen Kummer (Eltern) 0800 111 0 550.
- Mappa: books/<slug>-de/ (book.json "lang":"de", saját érzelmi német cím a képlet szerint). A builder copyright-szövege németül, ha lang=de.
- Sorrend (minden napi futásban: az aznapi angol könyv + 1 német fordítás): 1) Still Lit DE, 2) Give Them Back Their Wonder DE, 3) I Didn't Mean to Yell DE, 4) Who Takes Care of Mom? DE, 5) Brave Little Hearts DE, 6) The Woman Who Started Over DE, 7) Busy Family Planner DE (a termék-generátorok német szövegével).
- Állapot: **Still Lit DE = „Noch brennt das Licht“ KÉSZ** (2026-11-13, `still-lit-de/`, 88 old., 9,1e szó, papír 10,99 €, Kindle 4,99 €). **Give Them Back Their Wonder DE = „Gib ihnen ihr Staunen zurück” KÉSZ** (2026-11-14, `unplugged-winter-break-de/`, 88 old., 9,9e szó, 12,99 € / 4,99 €). **Ich wollte nicht schreien** (Yell DE, `calm-mom-handbook-de/`): FOLYAMATBAN 2/3 – 15,2e szó, 93 old. (2026-11-20): Schnellfinder, Brief, Kapitel 1–12 + Teil 1–2 összefoglaló. 3/3: Teil 3 + mellékletek + build. Ár: 15,99 € / keménytáblás 23,99 € / Kindle 5,99 €.
- Kész (2026-11-12): Weihnachts-Malbuch, Weihnachts-Rätselbuch, Familienplaner 2027, Haustier-Gesundheitsheft (scripts/kdp_books_de.py). Color Your Demons DE: Nóra forrásfájlja kell.

## Váltakozó ritmus (Nóra döntése, 2026-11-13)
- **1 hosszú + 1 rövid könyv váltja egymást.** Hosszú: 28–32e szó, ~200 old., papír 15,99 $ / 15,99 €, Kindle 5,99; 3 napi futás alatt készül (1. nap: vázlat + 1/3, 2. nap: 2/3, 3. nap: kész + build). Rövid: 10–12e szó, 85–110 old., 10,99–12,99 $; 1 nap.
- A plusz terjedelem csak valódi tartalom lehet: esettanulmány (összetett figura, jelölve), korosztály/élethelyzet szerinti részek, munkalapok, 30 napos program, „mit mondj” szkriptek, GYIK. Töltelék, ismétlés tilos.
- Sorrend: #3 I Didn't Mean to Yell = HOSSZÚ → #4 Who Takes Care of Mom? = rövid → #5 Brave Little Hearts = HOSSZÚ → #6 The Woman Who Started Over = rövid → utána új címek trendelemzés alapján, ugyanígy váltakozva.
- Teszt: a feltöltés után 30 nappal összevetjük a könyvenkénti jogdíjat; ha a hosszú nem hoz ≥30%-kal többet, vissza a rövidre.

## Alapanyag és olvasói lánc (Nóra, 2026-11-13)
Cél: a könyv valóban segítsen, és vigye tovább az olvasót a sorozat következő kötetéhez.

### 1. Alapanyag-gyűjtés írás ELŐTT → `books/<slug>/ALAPANYAG.md` (kötelező, kb. 1 óra Claude-munka)
1. **Olvasói fájdalompontok** (WebSearch): a téma 3–5 legkelendőbb Amazon-könyvének 1–3 csillagos véleményei („mi hiányzott”), Reddit/fórum-szálak (r/Parenting, r/Mommit, r/divorce, r/Anxiety stb.). Csak összefoglalva, saját szavakkal; idézni, másolni tilos. Kimenet: 10–15 konkrét helyzet, amiben az olvasó elakad, és az olvasó saját szóhasználata.
2. **Bizonyítékalap**: a témában elismert, ellenőrizhető megközelítések és források (pl. szakmai szervezetek ajánlásai – AAP, NHS, CDC, APA; ismert, nevesített módszerek – CBT, ACT, önegyüttérzés, érzelmi coaching, expozíciós „bátorság-létra”). Csak olyat írj be, aminek a létezése ellenőrizhető; kitalált tanulmány, szám, idézet tilos. A könyvben a módszer neve + egyszerű magyarázat; a végén „Further reading” lista valódi, létező címekkel.
3. **Rés a piacon**: mit nem ad meg a versenytárs (pl. túl elméleti, nincs „mit mondj” szöveg, nincs kisgyerekes változat) → ez lesz a könyv ígérete.
4. **Fejezetterv a fájdalompontokra**: minden fejezet egy valós elakadásra válaszol.

### 2. Hasznossági kapu (minden fejezet)
- Miért történik (egyszerű mechanizmus) → mit tegyél (lépések) → mit mondj (szó szerinti mondatok) → gyakorlat → „ha nem működik” (hibaelhárítás).
- Gyors siker az elején: az 1. fejezetben egy módszer, ami még aznap este kipróbálható.
- A végén: 1 oldalas összefoglaló/„hűtőre tehető” kártya + 30 napos (rövid könyvnél 7 napos) terv.

### 3. Olvasói lánc
- A könyv végét a `build_book.py` automatikusan írja a `books/series.json`-ból: „Where to Go From Here” (a következő kötet, miért ez a következő lépés) + a többi kötet + őszinte értékelés-kérés (ösztönző, ajándék nélkül – Amazon-szabály).
- Szövegközben max. 2 természetes utalás a sorozat másik kötetére ott, ahol a téma valóban oda vezet (pl. a kiabálós fejezetben a „Brave Little Hearts” szorongásos részére). Reklámszöveg tilos.
- Lánc-térkép: Give Them Back Their Wonder → I Didn't Mean to Yell → Brave Little Hearts / Who Takes Care of Mom? ↔ I Didn't Mean to Yell; Still Lit ↔ The Woman Who Started Over.
- Ha egy kötet elkészül: `series.json` → `status`/`status_de: ready`, és a korábbi kötetek újraépíthetők (a „coming soon” felirat eltűnik). Nóra feltöltéskor a KDP-ben „series” mezőt állít: Gentle Life Guides.

## KDP-kapu: méret és keret (Nóra, 2026-11-14) – KÖTELEZŐ
- **A trim méretet a book.json `trim` mezője adja** (alap 6x9; a Noch brennt das Licht 6.14x9.21). A KDP-ben PONTOSAN ugyanazt kell választani – a KDP_FELTOLTES első soraiban kiemelve.
- **Borító = 2 × szélesség + 0,25 + oldalszám × 0,002252 (gerinc) × magasság + 0,25** (in). A `build_book.py` `kdp_check` ezt ellenőrzi, és hiba esetén leáll.
- **Semmi nem lóghat ki a keretből:** a belívben a lap szélétől 0,25 in-en belül nincs tinta (a kapu oldalanként ellenőrzi); a borítón minden szöveg/logó ≥0,375 in-re a vágóéltől és a gerinc hajtásától, a hátsó szöveg nem érhet a vonalkód-dobozba (assert).
- Sorrend a KDP-ben: **előbb az új belív, utána a borító** (a KDP az oldalszámból számolja a gerincet).
- **Feltöltési lap: `KDP_FELTOLTES.pdf`** – normál betű (11 pt), tágabb sorköz (1,55), A4 (`scripts/kdp_lap.py`); a zip-be ez megy a .md mellé.
- **Gerinc:** gerincszöveg csak 100+ oldaltól, és a szöveg mindkét oldalán ≥0,0625 in szabad hely (KDP). 100 oldal alatt a gerinc csak színes, felirat nélkül.
- **Kindle e-könyv borító (Nóra, 2026-11-17):** minden KDP-csomagba kerül `ebook-cover.jpg` / `front.jpg`: JPG, RGB, **min. 625 px széles × 1000 px magas, max. 10 000 px mindkét irányban**, ajánlott magasság 2560 px, a trim arányában (8.5x11 → ~1978 × 2560; 6x9 → 1600 × 2415). Papírkönyv-csomagnál: `python3 scripts/kdp_ebook_cover.py kdp/<csomag>/` (a cover.pdf elülső paneljéből, kifutó nélkül); Gentle-könyveknél a `build_book.py` `front.jpg`-je. A KDP_FELTOLTES-ben külön „Kindle e-könyv” szakasz.
- **Képoldalas belív e-könyvként (2026-11-17):** a képekből álló PDF-et (munkafüzet, tervező, kifestő) a KDP e-könyv-konvertere fekvőbe forgatja/újratördeli → e-könyvhöz mindig fix elrendezésű EPUB3: `python3 scripts/kdp_fixed_epub.py <interior.pdf> <ebook-fixed.epub> "Cím" "Szerző" ebook-cover.jpg en` (pre-paginated, orientation portrait, epubcheck-valid). Kitöltős tartalmat a KDP e-könyvként elutasíthat.
- **Borító-keret (Nóra, 2026-11-17):** minden szöveg/doboz ≥0,5 in-re a vágóéltől (KDP minimum 0,125 in); vonalkód-doboz pontosan a KDP helyén: 2 × 1,2 in, 0,25 in-re a gerinctől és az alsó vágóéltől; gerincfelirat csak 100+ oldaltól (a kdp_cover.py korábban 80-tól tett ki – javítva). Meglévő borító javítása: `python3 scripts/kdp_cover_fix.py kdp/<csomag> 8.5 11`. Feltöltés előtt: a KDP Print Previewerben nincs piros jelzés, és a belív minden oldala álló (rot 0).
- **Keménytáblás borító (2026-11-17):** a 6x9-es keménytáblás tábla-mérete a KDP-nél 6.14x9.21 (80 oldal: 13,944 × 10,417 in); a generátor ezt automatikusan kezeli. `python3 scripts/hardcover_cover.py books/<slug> <W> <H>` – W×H a KDP-től (hibaüzenet vagy Cover Calculator); ráhajtás = (H − trim_h)/2, gerinc a maradék; szöveg ≥ ráhajtás + 0,5 in a széltől és ≥ 0,65 in a gerinctől. Noch brennt das Licht (81 old.): 13,946 × 10,417 in.
- **Oldalszám/lábléc (2026-11-17):** min. 0,5 in-re a lap aljától (0,25 in-nél a keménytáblás Print Previewer „text outside the margins” hibát ad); a kdp_check 0,45 in-es szélső sávot ellenőriz.
- **Előlap:** cím- és szerzőmező ≥0,5 in-re a vágóéltől (a szerzőmező alja is).
