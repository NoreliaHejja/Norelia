# Márka: AureliaVenn + Emily

## Szerepek
- **AureliaVenn** — az Etsy-bolt, semleges esernyőmárka. Több karakter is befér.
- **Emily** — AI-generált közösségimédia-arc (Higgsfield), US-célpiac. Nem új persona — mindig ezt a meglévő karaktert jelenti.

## Persona
- ~30-as, „crunchy-ish (not preachy)” boy mom, egészségtudatos, házi snackek, sár, hangulatos családi hagyományok. „Progress, not perfection.”
- Család: fiú **Theo** (4, dinoszaurusz-szakértő), férj **Jake** (decemberben is grillezik), macska **Biscuit** (barna-narancs cirmos, „judgy”).
- Hang (videó): **Gracie**.

## Fiókok
- Fióknév mindenhol: **@crunchyish.emily** (Pinterest: crunchyishemily). Megjelenő név: „Emily | crunchy-ish boy mom”.
- Csatornák: TikTok (fő) · **Pinterest (fő Etsy-forgalom)** · Instagram (Reels újrahasznosítás) · YouTube Shorts.
- Instagram: kész, AI-címkével (2026-10-01). TikTok régió: Hungary — csak 60 nap után váltható.
- Belépési e-mail: belső, a jelszókezelőben (szándékosan nincs a repóban).
- Bio-link: AureliaVenn Etsy, „Emily's Family Collection” szekció.

## Pinterest táblák (board ID-k)
| Tábla | ID |
|---|---|
| Matching Family Shirts | 1095289640567036555 |
| Christmas Family Traditions | 1095289640567036556 |
| Gift Ideas for Families | 1095289640567036558 |
| Cozy Fall Outfits | 1095289640567036559 |
| Cat Mom Life | 1095289640567036560 |
| Family Fall Traditions | 1095289640567036561 |
| Kids in the Kitchen | 1095289640567036562 |
| Healthy Kids Snacks | 1095289640567036563 |
| Christmas Printables for Kids | 1095289640567036564 |
| Thanksgiving Ideas for Kids | 1095289640567036565 |
| Classroom Christmas Ideas | 1095289640567036566 |
(A rövidített „…556” formából visszaírt ID-k — első használat előtt ellenőrizni.)

Pinterest-profil (nov. 2): 438 havi megtekintés, 0 követő. Legjobb pinek életképek (Dye-Free Snack Board 158, Sourdough 108, Pumpkin Patch 87 megjelenítés); az Etsy-linkes pinek 0 megjelenítéssel.
→ Tanulság: az életkép-pinek mennek, a termékpinek nem. Termékpint életkép-stílusban kell csinálni.

## Higgsfield asset-ID-k
- Profilkép: `0d60efc5-9041-4829-b181-a0ef82207986`
- Borító: `73a94fdd-0030-4aed-a1b4-347cbf0f3dd8`
- Bemutatkozó hang (Gracie, Biscuittal): `83c11065-f748-435b-a9fa-efffc650014a`
- Bemutatkozó videó (23 mp): `190ee00b-6425-4ec3-9265-0381556cc5d5`
- **KÖTELEZŐ arc-referencia (Nóra, 2026-11-19): `58eb1f42-9851-475c-a07c-73bf4c4a9439`** = `docs/emily-reference.jpg` (göndör vörösesbarna haj, szeplők, krémszínű pulóver, cirmos macska). Minden Emily-kép `medias: [{value: "58eb1f42-…", role: "image_references"}]` + prompt: „the exact same woman as in the reference image: same face, curly auburn hair, freckles”. Videónál a start_image is ezzel készült kép legyen.
- NE használd arc-referenciának: a régi sütőtökös `1ed6fe40-…` és a korábbi generált Emily-képek (ezektől csúszott el az arc).
- Saurus minták: Mama `88bb4fa5-9738-405b-8380-bd1bc36ca68f` · Papa v2 `7f3b59ed-88aa-4413-9682-0e3110020b59` · Little `c94f83c6-1334-411a-9d33-fd4be086367d`
- Saurus mockupok: család flat lay `05e4e4ac-dba2-4df9-9077-4d10874b662a` · család életkép `649afbe0-7b25-496d-8da2-65632790c595` · Mama+Little `82e21fab-cf45-4d07-ac13-07477911534b`
- NE használd: régi Maple/Milo hang-videók, Papa Saurus v1 (szakállas) `8d34f9a4-…`, `806f55f9-…`

## Pin-szabályok (Nóra, 2026-11-19 – a régi pinekre 0 kattintás)
Ok: négyzetes/4:5 életkép felirat nélkül → a hírfolyamban nem derül ki, mit kap a néző; terméknév-cím előny helyett; generikus leírás; kevés, rendszertelen pin (az ütemezés napokig elakadt).
1. **Formátum 2:3 (1000×1500)**, `python3 projects/etsy-empire/scripts/pin_image.py termekek/<slug> "Előny-cím|2. sor" "konkrét ígéret"`.
2. **Cím = keresett kifejezés + előny**, nem terméknév („Easy Elf Ideas for Toddlers”, „Kindness Elf Arrival Letter”). Max 6–7 szó, nagy betű.
3. **Látszódjon a termék közelről** (2 oldal), alul PRINTABLE · INSTANT DOWNLOAD + „Tap to see all pages”.
4. Pin-cím (≤100 kar.) és leírás (≤500) a listing long-tail kulcsszavaival, 1 CTA-mondat; link = listing URL.
5. Termékenként 3 pin-változat (más cím/kép), 3–5 naponta új változat – a Pinterest az új képet „friss pin”-ként kezeli.
6. Emily-életképes pin csak az arc-referenciával, és ugyanúgy előny-címmel.
7. Elsőbbség: Kindness-mintás termékek (Kindness Elf, Toddler Kindness Elf, következő szereplők).

## Tartalomszabályok
- Minden poszton AI-címke (TikTok „AI-generated content”, Instagram „AI info”).
- Theo főleg hátulról / kéz / csizma / messziről; szemből ritkán.
- Nincs egészségügyi vagy gyógyító állítás.
- Videót Nori néz át élesítés előtt.

Részletes poszttervek a claude.ai projektben: `emily-2-week-post-plan.md`, `emily-post-plan-weeks-3-4.md`, `emily-persona-story.md`, `emily-channel-starter-kit.md`.
