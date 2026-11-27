# Tanulságok

## Stratégia
- **Reject before refining:** ha az ötlet elbukik az alapteszten, ne védd tovább — váltás.
- **Ship first, expand second:** bővítés csak piaci jel után.
- Munkamódszer: opciók → kemény stressz-teszt → egy végrehajtható döntés → gyors build és ship.
- Széles digitális tartalomhoz (pl. faceless YouTube) az angol jobb, mint a magyar (közönség, RPM).
- Affiliate infó-forgalomnál alacsony a vásárlási szándék; vékony programmatic oldalak SEO-kockázatot hordoznak.

## Platformok
- **Apollo.io:** az API people+email kereséshez fizetős csomag kell; ingyenesen a böngészős UI működik (app.apollo.io → Search → People, NAICS szűrő).
- **impact.com Marketplace:** új oldalt elutasít; a márka saját affiliate signup URL-je megkerüli.
- **Gumroad:** nemzetközi eladóknak is jó; Stripe/PayPal háttér kezeli a sales taxot.

## Deploy (Cloudflare Pages, direkt feltöltés)
- A direkt feltöltés **lecseréli a teljes deployt** → mindig az összes fájlt töltsd fel együtt.
- macOS a duplikált letöltést átnevezi (`index 2.html`) → 404. Feltöltés előtt ellenőrizd a fájlneveket.
- A Cloudflare analytics "látogatói" 404 esetén is bot/crawler forgalmat mutatnak — nem valódi emberek.
- GSC: Domain property, DNS TXT verifikáció. Bing Webmaster: import GSC-ből.

## PDF (Python + ReportLab)
- A ☐ (U+2610) alap Helvetica fontban teli négyzet lesz → használd: `[&nbsp;&nbsp;]` egy `Paragraph`-on belül.
- Checklistnél **egy `Paragraph` elemenként**, különben összeomlik.
- Fejléc/lábléc: `onFirstPage` / `onLaterPages` callback — a borító tiszta marad.
- Piktogramok: ReportLab primitívekből (`Drawing`, `Polygon`, `Circle`, `Rect`, `Line`), külön `pictograms.py` modulban — nincs licenckockázat.
- Vizuális QA: `pdf2image.convert_from_path` 110 DPI-n (a `renderPM` nem elérhető).
