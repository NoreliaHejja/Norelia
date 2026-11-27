# Szabásminta-gyártósor (Nóra, 2026-11-23)

Kétheti teszt (nov. 26 – dec. 9, eltolva): naponta **1 szabásminta + 2 horgolásminta + 2 printable**. Dec. 10-én kiértékelés (megtekintés, kedvelés, eladás termékcsaládonként).

## Menet
1. `szabas/mintak/<slug>/pattern.json` (type, sizes, labels EN/DE, img, guide EN/DE) – minta: `womens-skirt-block`.
2. `python3 scripts/build_sloper.py szabas/mintak/<slug>` → A4/Letter (csempézett, tesztnégyzet) + A0, EN és DE, méret-ellenőrzés.
3. `python3 scripts/build_sloper_guide.py szabas/mintak/<slug>` → útmutató PDF EN + DE, listingképek (kepek/).
4. Zip: `<slug>-English.zip` (A4, Letter, A0, Guide EN) + `<slug>-Deutsch.zip` → listing.json (taxonomy 6343 Patterns & Blueprints, is_supply true) → `etsy_uploader.py --feltolt --aktival` → API-val ellenőrizd a 2 fájlt.
5. Új típushoz `draft_<type>()` a build_sloper.py-ban; a darabok cm-ben, a varrásráhagyás jelölve (blokkoknál nincs).

## Szabályok
- Csak saját, szabványos szerkesztési lépések és saját mérettáblázat; más bolt mintáját, nevét, képét nem másoljuk.
- Képek: a szabásminta-rajz, mérettáblázat, tartalom, útmutató – fotó nem kell. AI-fotó varrott ruháról TILOS.
- Leírásban: „drafted with the help of software from a standard size chart, please sew a test version first”, varrásráhagyás igen/nem, bőség, AI-közlés.
- Ár: egyszerű tárgy (táska, párnahuzat, kötény) 3,99 €; blokk/szoknya 7,99 €; csomag 14,99–19,99 €.
- Ellenőrzés: a generátor kiírja a kész méreteket (csípő = test + bőség); ha eltér, nem töltjük fel.
