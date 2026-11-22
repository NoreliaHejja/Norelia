# SaaS-résvizsgálat (2026-11-22) – top 4 ötlet

Módszer: webes keresés a versenytársakra, árakra, funkciókra. A számok csak a talált forrásokból vannak; ahol nincs adat, azt jelölöm.

| # | Ötlet | Mit találtunk | Rés | Döntés |
|---|---|---|---|---|
| 1 | **Printable Listing Image Studio** (PDF → 8–10 Etsy-listingkép) | Nincs olyan eszköz, ami közvetlenül PDF-ből készít Etsy-listingképeket. A versenytársak: Canva-sablonbundle-ök (1500+ sablon, kézi munka), általános mockup-generátorok (Dynamic Mockups, Mediamodifier, Picsart), és egy ListifyAI, ami főleg fizikai termékfotóra van hangolva. | **Nyitott.** A meglévők kézi szerkesztést kérnek, vagy nem a printable-ekre szólnak. | **TESZTELNI (1.)** |
| 2 | **Pin Factory** (listingből Pinterest-pin) | Sok szereplő: Pinsevo 9 $/hó, Pin Generator (Shopify) 16,99 $/hó-tól, Alura, PinMaster AI, Pintzy, plus IFTTT/MESA. | Zsúfolt, árverseny. | **ELVETNI** |
| 3 | **Etsy Personalization → POD** | A Printify-nak már van natív „Personalization Hub for Etsy”-je: a vevő mezőit automatikusan nyomdai rétegre viszi, beállítható automatikus gyártásba küldéssel. A Customily is létezik. | Lezárva, a platform maga oldja meg. | **ELVETNI** |
| 4 | **Low-Content Book Builder** (belív + papír-/keménytáblás-/Kindle-borító) | BookBolt, Tangent Templates, Canva, Book Bird, KDPBuilder, bookow.com sablongenerátor. A KDP saját Cover Creatora **nem támogatja a keménytáblás borítót**. | Részleges: a teljes csomag (keménytáblás pontos méretre) gyenge pont, de erős a verseny. | **TESZTELNI (2.)**, csak ha az 1. elbukik |

## Ajánlás
**1. Printable Listing Image Studio.**
- A rés nyitott.
- A vevőkör (Etsy digitális eladók) nagy, és már fizet eszközökért.
- Az MVP-hez a technika nagyrészt kész nálunk: `projects/etsy-empire/scripts/clean_cover.py`, `listing_kepek.py` és `pin_image.py`.

Ár-hipotézis: 9–19 $/hó vagy 39 $ életre szóló kezdő ajánlat. Teszt: angol nyitóoldal várólistával, 1 hét, max. 30 e Ft.

## Források
- Mockup/printable: https://www.etsy.com/listing/1878418023/1500-etsy-listing-mockup-templates · https://dynamicmockups.com/knowledge/how-to-create-etsy-mockups-no-photoshop/ · https://mediamodifier.com/blog/etsy-mockup-generator · https://www.listifyai.net/for/digital-printables
- Pinterest: https://apps.shopify.com/pin-generator · https://www.producthunt.com/products/pinmaster-ai · https://alura.io/features/pinterest · https://delzonic.com/blogs/best-pinterest-scheduler-for-etsy-2026/
- Personalization: https://help.printify.com/hc/en-us/articles/47145436478609-What-is-Personalization-Hub-for-Etsy-and-how-does-it-work · https://www.customily.com/etsy-product-personalizer
- KDP: https://kindlepreneur.com/best-book-bolt-alternatives/ · https://kdp.amazon.com/help?topicId=G201113520 · https://kdpbuilder.com/blog/kdpbuilder-vs-bookbolt-best-kdp-workflow
