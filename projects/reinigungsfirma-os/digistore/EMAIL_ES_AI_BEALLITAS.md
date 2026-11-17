# info@reinigung-kalkulieren.de + AI-láthatóság – beállítás (2026-11-17)

## 1. E-mail fogadása (Cloudflare Email Routing, ingyenes, ~5 perc)
1. Cloudflare → reinigung-kalkulieren.de → **Email** → **Email Routing** → Get started / Enable.
2. **Destination address:** a saját Gmail-címed → Cloudflare küld egy megerősítő e-mailt → kattints rá.
3. **Custom address:** `info` → Action: Send to an email → a Gmail-címed → Save.
4. Cloudflare felajánlja a DNS-rekordokat (MX + SPF TXT) → **Add records automatically**.
5. Teszt: írj egy levelet bármelyik címedről az info@reinigung-kalkulieren.de-re → megérkezik a Gmailbe.

## 2. Válaszolás info@-ról (Gmail „Send mail as” + Brevo SMTP, ingyenes 300 levél/nap)
1. brevo.com → ingyenes fiók → Senders, Domains → **Add domain**: reinigung-kalkulieren.de → a megadott DKIM/DMARC rekordokat add hozzá Cloudflare DNS-ben (Brevo „Authenticate” gomb).
2. Az SPF-rekord **egy** legyen, mindkét szolgáltatóval: `v=spf1 include:_spf.mx.cloudflare.net include:spf.brevo.com ~all` (a Cloudflare által létrehozottat írd át erre).
3. Brevo → SMTP & API → SMTP key generálása.
4. Gmail → Beállítások → Fiókok → **E-mail küldése más címről** → `info@reinigung-kalkulieren.de`, SMTP: `smtp-relay.brevo.com`, port 587, TLS, felhasználó: a Brevo SMTP-login, jelszó: az SMTP key.
5. Gmail megerősítő kódot küld az info@-ra → a routing miatt a Gmailedbe érkezik → beírod.
(A Brevo később a várólista-levélhez is jó.)

## 3. AI-láthatóság a Cloudflare-ben (FONTOS – a Cloudflare alapból tilthatja az AI-robotokat)
- Security → Bots (vagy **AI Crawl Control**): az AI-robotok (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) legyenek **Allow**; a „Block AI bots / AI Scrapers and Crawlers” kapcsoló **ki**.
- **Managed robots.txt / Content Signals**: kikapcsolni, különben a Cloudflare felülírja a mi robots.txt-nket.
- Bot Fight Mode: ki (Digistore-ellenőrzés miatt is).

## 4. Keresők (egyszeri, ~10 perc)
- Google Search Console → Domain property (DNS TXT a Cloudflare-ben) → Sitemaps: `https://reinigung-kalkulieren.de/sitemap.xml`.
- Bing Webmaster Tools → „Import from Google Search Console” (a ChatGPT és a Copilot keresése a Bing-indexre épül).

## Mi van már az oldalon (AI-SEO)
- `llms.txt` (az AI-asszisztenseknek szóló összefoglaló), `robots.txt` (az AI-robotok név szerint engedélyezve), `sitemap.xml`.
- Strukturált adatok (JSON-LD): Organization, WebSite, WebApplication (Rechner), FAQPage, Product (Kit, 29 €, 30 nap), Article (3 ratgeber).
- 3 ratgeber „válasz először” formában, képlettel, táblázattal, számolt példával: Stundensatz berechnen · Büroreinigung pro m² · Leistungswerte.
