# Összevonás – 2026-11-04

A korábban külön élő munkaterületek bekerültek ebbe a repóba:
side-projects (→ `ceg/portfolio/` + `projects/*/README.md`), reinigungsfirma-os, aureliavenn-etsy, pet-printables (→ `projects/`).
A `.git`-történetük nem jött át (csak a fájlok); jelszó/kulcs nem volt bennük.

## Ellentmondások – DÖNTVE (Nóra, 2026-11-04: „mind OK”)
| # | Téma | Régi szabály | Norelia szabály | Javaslat |
|---|---|---|---|---|
| 1 | **Projektszám** | side-projects: max 3 aktív (most 6+ aktív: Reinigungsfirma, ügyvédi weboldal, HACCP, ComplyStarterKit, AureliaVenn, pet-printables) | nincs korlát (2026-11-02, Nóra) | Korlát nélkül is **hetente max 3 kapjon időt**; a többi csak automatán fut. Parkolóba: HACCP (nincs specifikáció), ügyvédi weboldal (szolgáltatás, nem passzív – ellentmond a „Nóra fizikailag ne kelljen” elvnek). |
| 2 | **Amazon KDP** | side-projects PROJECTS.md: ELVETVE („telített piac”) | aktív második csatorna; Color Your Demon ebook már élő; pet-printables KDP-t céloz | KDP **csak másodlagos csatorna** meglévő printable-ekhez (+10 perc/termék), KDP-only termék nem készül. |
| 3 | **Reinigungsfirma landing – 2 verzió** | `projects/reinigungsfirma-os/` (src → `build_site.py` → site, petrol design, saját scriptek, Nóra előző munkája) | `web/reinigungsfirma-os/` (zöld design a canvasból, 3 termék, Impressum EV-adatokkal) | **A `projects/` verzió legyen a hivatalos** (build-folyamat, ellenőrzés, Nóra korábbi döntései). Belőle hiányzó jó részeket átviszem: EV-adatok az Impressumba, várólista Starter/OS-nél, Preiserhöhungs-Paket. Utána a `web/` mappát archiváljuk. |
| 4 | **Katrin / arc** | Reinigungsfirma CLAUDE: „arctalan termék, nincs videó a tulajdonossal” | Katrin AI influenszer, videókkal | Nem ütközik: Katrin AI, Nóra arca nem jelenik meg. A Reinigungsfirma CLAUDE.md-be beírom. |
| 5 | **Megszólítás** | Reinigungsfirma: ügyfélszöveg mindig **Sie** | Katrin: Du a TikTok/IG-n (javaslat) | Javaslat marad (Du csak rövid videóban); webinár, oldal, LinkedIn: Sie. |
| 6 | **Emily** | aureliavenn-etsy: @crunchyish.emily, kész asset-ID-k (`docs/BRAND-EMILY.md`) | `ceg/projektek/karakterek.md`: Emily vázlat | A `BRAND-EMILY.md` az irányadó; a karakterek.md csak hivatkozik rá. |
| 7 | **Pet printables – 2 gyártósor** | pet-printables: napi ütemezett gyártás, saját design system | Claude ebben a munkamenetben Pet Memorial/Puppy v2 + KDP-csomag | A pet-printables design system az irányadó; az elkészült v2/KDP fájlokat oda soroljuk (`products/`). |

## Valódi számok (a régi repókból) – felülírják a korábbi becsléseket
- AureliaVenn: **24 aktív listing** (19 POD + 5 digitális), első eladás 2026-10-30 (Kindness Elf, €3,99), heti ~8 látogatás, Etsy-keresés 0, Pinterest 0, Etsy Ads ROAS 7,53 (30 nap, $0,62 költés).
- ComplyStarterKit: élő, $49, Gumroad.
- SafetyWing affiliate: passzív.

**Végrehajtva 2026-11-04:** heti fókusz max 3 projekt; HACCP és ügyvédi weboldal → parkoló; KDP = másodlagos csatorna; hivatalos landing = `projects/reinigungsfirma-os/` (EV-adatok, várólista, áthúzott árak törölve, dátumok javítva); `web/` → `archiv/web-2026-11/`; Preiserhöhungs-Paket → `projects/reinigungsfirma-os/products/` + `scripts/build_preiserhoehung.py`; Katrin arca: **D**.
