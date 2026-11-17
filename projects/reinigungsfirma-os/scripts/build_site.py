#!/usr/bin/env python3
"""Build the deployable multi-page site (2026-11-17).

Reads  src/landing.src.html  (CSS-Basis, Rechner-Formular und Rechner-Skript)
Writes site/index.html, site/<seite>/index.html, site/404.html, site/assets/site.css,
       site/sitemap.xml

Regeln (CLAUDE.md): keine externen Fonts/CDNs, keine Cookies/Tracker, Sie-Form,
Kauf-Buttons zeigen nur auf das Digistore24-Bestellformular.

Usage:  python3 scripts/build_site.py
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "landing.src.html"
SITE = ROOT / "site"
FONTS = SITE / "fonts"
DOMAIN = "https://reinigung-kalkulieren.de"
MAIL = "info@reinigung-kalkulieren.de"

# Digistore24-Bestellformular-Link des Kalkulations-Kits hier eintragen (leer = "Shop öffnet in Kürze")
LINKS = {"kit": ""}

FACES = [("Schibsted Grotesk", "schibsted-grotesk", w) for w in (400, 500, 600, 700, 800)] + [
    ("JetBrains Mono", "jetbrains-mono", w) for w in (400, 500, 600)
]

CHECK = ('<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3 3 7-7" '
         'fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
LOGO = ('<svg width="26" height="26" viewBox="0 0 26 26" aria-hidden="true"><rect x="1" y="1" width="24" height="24" rx="7" '
        'fill="none" stroke="#9FE3D1" stroke-width="2"/><path d="M7 14.5l4 4 8-10" fill="none" stroke="#9FE3D1" '
        'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def mailto(subject, body=""):
    from urllib.parse import quote
    return f"mailto:{MAIL}?subject={quote(subject)}" + (f"&body={quote(body)}" if body else "")


def ul(items):
    return "<ul class='checks'>" + "".join(f"<li>{CHECK}<span>{i}</span></li>" for i in items) + "</ul>"


EXTRA_CSS = """
/* ===== Mehrseitige Erweiterung (2026-11-17) ===== */
html{scroll-behavior:smooth}
body{margin:0}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;z-index:99;background:var(--card);padding:8px 12px;border-radius:8px}
.nav-links{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.nav-links a{border:0;padding:8px 12px;border-radius:999px;font-weight:600;font-size:.95rem;text-decoration:none;color:var(--on-petrol)}
.nav-links a:hover,.nav-links a[aria-current="page"]{background:rgba(255,255,255,.1)}
.nav-links a.nav-cta{background:var(--foam);color:#0A3642}
.nav-links a.nav-cta:hover{filter:brightness(1.05);background:var(--foam)}
.nav a.logo{border:0;padding:0;font-size:1.1rem;color:#fff;text-decoration:none}
.nav a.logo:hover{background:none}
.menu-btn{display:none;background:transparent;border:1px solid rgba(255,255,255,.25);color:#fff;border-radius:10px;padding:8px 12px;font:600 .95rem var(--sans);cursor:pointer}
@media (max-width:820px){
  .menu-btn{display:inline-flex}
  .nav{flex-wrap:wrap}
  .nav-links{display:none;width:100%;flex-direction:column;align-items:stretch;padding:8px 0 4px}
  .nav-links.open{display:flex}
  .nav-links a{padding:12px 14px}
}
.subhero{background:radial-gradient(120% 120% at 85% 0%,#14606F 0%,var(--petrol) 45%,var(--petrol-deep) 100%);color:var(--on-petrol);padding-bottom:56px}
.subhero h1{color:#fff;font-size:clamp(2rem,4.4vw,3.1rem);max-width:22ch}
.subhero .lead{margin-top:16px;max-width:58ch}
.subhero .eyebrow{color:var(--foam);margin-bottom:14px;display:block;padding-top:24px}
.crumbs{font-size:.85rem;color:var(--on-petrol-muted);padding-top:8px}
.crumbs a{color:var(--on-petrol-muted)}
.checks{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.checks li{display:flex;gap:10px;align-items:flex-start}
.checks li svg{flex:none;margin-top:6px;color:var(--petrol)}
:root[data-theme="dark"] .checks li svg{color:var(--foam)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .checks li svg{color:var(--foam)}}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;counter-reset:s}
.step{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:28px;display:grid;gap:10px;align-content:start}
.step::before{counter-increment:s;content:counter(s,decimal-leading-zero);font-family:var(--mono);font-weight:600;color:var(--petrol);font-size:.95rem;letter-spacing:.06em}
:root[data-theme="dark"] .step::before{color:var(--foam)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .step::before{color:var(--foam)}}
.step p{color:var(--muted)}
.shots{display:grid;grid-template-columns:260px 1fr;gap:28px;align-items:start}
.tabs{display:grid;gap:8px}
.tabs button{all:unset;cursor:pointer;padding:16px 18px;border-radius:14px;border:1px solid var(--line);background:var(--card);display:grid;gap:4px}
.tabs button b{font-size:1rem}
.tabs button span{font-size:.86rem;color:var(--muted)}
.tabs button[aria-selected="true"]{border-color:var(--petrol);box-shadow:inset 3px 0 0 var(--petrol)}
.tabs button:focus-visible{outline:3px solid var(--foam)}
.frame{background:var(--card);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);overflow:hidden}
.frame-bar{display:flex;gap:6px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line);font-family:var(--mono);font-size:.75rem;color:var(--muted)}
.frame-bar i{width:9px;height:9px;border-radius:50%;background:var(--line);display:inline-block}
.frame img{display:block;width:100%;height:auto;max-height:620px;object-fit:contain;object-position:top;background:#fff}
.feature{display:grid;grid-template-columns:1fr 1.15fr;gap:48px;align-items:center;padding-block:44px;border-top:1px solid var(--line)}
.feature:first-of-type{border-top:0;padding-top:0}
.feature.rev{grid-template-columns:1.15fr 1fr}
.feature.rev .feature-text{order:2}
.feature-text{display:grid;gap:14px;align-content:start}
.feature-text p{color:var(--muted)}
.buybox{position:sticky;top:20px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px;box-shadow:var(--shadow);display:grid;gap:14px}
.buybox small{color:var(--muted);font-size:.85rem}
.product-top{display:grid;grid-template-columns:1fr 360px;gap:40px;align-items:start;margin-top:-40px;position:relative}
.prose{display:grid;gap:14px;max-width:72ch}
.prose h2{font-size:1.5rem;margin-top:18px}
.prose p,.prose li{color:var(--muted)}
.prose b{color:var(--ink)}
.prose a{color:var(--petrol)}
:root[data-theme="dark"] .prose a{color:var(--foam)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .prose a{color:var(--foam)}}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:28px;display:grid;gap:12px;align-content:start}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.site-foot{border-top:1px solid var(--line);margin-top:72px}
.foot-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:28px;padding-block:44px}
.foot-grid h4{margin:0 0 10px;font-size:.78rem;font-family:var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.foot-grid ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.foot-grid a{text-decoration:none;color:var(--ink)}
.foot-grid a:hover{text-decoration:underline}
.foot-grid p{color:var(--muted);font-size:.92rem;margin-top:8px;max-width:34ch}
.foot-base{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-bottom:36px;color:var(--muted);font-size:.85rem}
.logo-ink{display:flex;align-items:center;gap:10px;font-weight:800;color:var(--ink)}
.logo-ink svg rect,.logo-ink svg path{stroke:var(--petrol)}
:root[data-theme="dark"] .logo-ink svg rect,:root[data-theme="dark"] .logo-ink svg path{stroke:var(--foam)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .logo-ink svg rect,:root:not([data-theme="light"]) .logo-ink svg path{stroke:var(--foam)}}
.notice{background:var(--foam-soft);border-radius:12px;padding:12px 14px;font-size:.92rem}
@media (max-width:900px){
  .steps,.grid2{grid-template-columns:1fr}
  .shots{grid-template-columns:1fr}
  .tabs{grid-template-columns:1fr 1fr}
  .feature,.feature.rev{grid-template-columns:1fr;gap:24px}
  .feature.rev .feature-text{order:0}
  .product-top{grid-template-columns:1fr;margin-top:24px}
  .buybox{position:static}
  .foot-grid{grid-template-columns:1fr 1fr}
}
@media (max-width:460px){.tabs{grid-template-columns:1fr}.foot-grid{grid-template-columns:1fr}}
"""

NAV_ITEMS = [("/#rechner", "Rechner"), ("/kalkulations-kit/", "Kalkulations-Kit"), ("/#vorlagen", "Vorlagen"),
             ("/#fragen", "Fragen"), ("/kontakt/", "Kontakt")]


def nav(current):
    links = "".join(
        f'<a href="{h}"' + (' aria-current="page"' if h == current else "") + f">{t}</a>" for h, t in NAV_ITEMS
    )
    return (f'<nav class="nav" aria-label="Hauptnavigation"><a class="logo" href="/">{LOGO}Reinigungsfirma OS</a>'
            '<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">Menü</button>'
            f'<div class="nav-links" id="nav-links">{links}<a class="nav-cta" href="/kalkulations-kit/#kaufen">Kit kaufen · 29 €</a></div></nav>')


def footer():
    return f"""<footer class="site-foot"><div class="wrap">
<div class="foot-grid">
  <div><a class="logo-ink" href="/" style="text-decoration:none">{LOGO}Reinigungsfirma OS</a>
  <p>Kalkulationsvorlagen für Reinigungsfirmen in Deutschland, Österreich und der Schweiz.</p></div>
  <div><h4>Produkte</h4><ul><li><a href="/#rechner">Stundensatz-Rechner</a></li><li><a href="/kalkulations-kit/">Kalkulations-Kit</a></li><li><a href="/warteliste/">Starter-Kit &amp; OS</a></li></ul></div>
  <div><h4>Hilfe</h4><ul><li><a href="/#fragen">Häufige Fragen</a></li><li><a href="/kontakt/">Kontakt</a></li><li><a href="/garantie/">Lieferung &amp; Garantie</a></li></ul></div>
  <div><h4>Rechtliches</h4><ul><li><a href="/impressum/">Impressum</a></li><li><a href="/datenschutz/">Datenschutz</a></li></ul></div>
</div>
<div class="foot-base"><span>© {date.today().year} Reinigungsfirma OS</span><span>Verkauf und Zahlung über Digistore24 · Keine Cookies, kein Tracking</span></div>
</div></footer>"""


COMMON_JS = """<script>
const LINKS = __LINKS__;
document.querySelectorAll("[data-link]").forEach(a => {
  const url = LINKS[a.dataset.link];
  if (url) { a.href = url; a.rel = "noopener"; return; }
  a.addEventListener("click", e => {
    const n = document.querySelector('[data-note="' + a.dataset.link + '"]');
    if (n) { e.preventDefault(); n.hidden = false; n.scrollIntoView({block:"nearest"}); }
  });
});
const mb = document.querySelector(".menu-btn"), nl = document.getElementById("nav-links");
if (mb) mb.addEventListener("click", () => { const o = nl.classList.toggle("open"); mb.setAttribute("aria-expanded", o); });
document.querySelectorAll(".tabs button").forEach(b => b.addEventListener("click", () => {
  document.querySelectorAll(".tabs button").forEach(x => x.setAttribute("aria-selected", x === b));
  const img = document.getElementById("shot"); img.src = b.dataset.src; img.alt = b.dataset.alt;
  document.getElementById("shot-name").textContent = b.dataset.name;
}));
</script>"""


def page(path, title, desc, body, current="", hero=None, extra_js=""):
    head = (
        '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{title}</title>\n<meta name=\"description\" content=\"{desc}\">\n"
        f'<link rel="canonical" href="{DOMAIN}{path}">\n'
        '<link rel="stylesheet" href="/assets/site.css">\n'
        '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 26 26%22%3E%3Crect width=%2226%22 height=%2226%22 rx=%227%22 fill=%22%230F4C5C%22/%3E%3Cpath d=%22M7 14.5l4 4 8-10%22 fill=%22none%22 stroke=%22%239FE3D1%22 stroke-width=%222.6%22 stroke-linecap=%22round%22/%3E%3C/svg%3E">\n'
        "</head>\n<body>\n<a class=\"skip\" href=\"#inhalt\">Zum Inhalt</a>\n"
    )
    if hero is None:
        eyebrow, h1, lead = title.split(" | ")[0], title.split(" | ")[0], ""
        hero = ("", h1, "")
    eyebrow, h1, lead = hero
    top = (f'<header class="subhero"><div class="wrap">{nav(current)}'
           + (f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else '<span class="eyebrow">&nbsp;</span>')
           + f"<h1>{h1}</h1>" + (f'<p class="lead">{lead}</p>' if lead else "") + "</div></header>")
    js = COMMON_JS.replace("__LINKS__", repr(LINKS).replace("'", '"'))
    return head + top + f'\n<main id="inhalt">\n{body}\n</main>\n' + footer() + js + extra_js + "\n</body>\n</html>\n"


def write(rel, html):
    out = SITE / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    assert "googleapis" not in html and "gstatic" not in html, f"externe Fonts in {rel}"
    assert not re.search(r'<script[^>]+src="https?://|<link[^>]+rel="(stylesheet|preconnect|preload)"[^>]+href="https?://|<img[^>]+src="https?://', html), f"externe Ressource in {rel}"
    out.write_text(html, encoding="utf-8")
    print(f"OK  site/{rel}  ({len(html):,} bytes)")


def main() -> int:
    s = SRC.read_text(encoding="utf-8")
    css = s[s.index("<style>") + 7:s.index("</style>")]
    form = s[s.index('<form class="calc"'):s.index("</form>") + 7]
    calc_js = s[s.index("const CUR"):s.rindex("</script>")]

    missing, ff = [], ""
    for family, slug, w in FACES:
        fname = f"{slug}-latin-{w}-normal.woff2"
        if not (FONTS / fname).exists():
            missing.append(fname)
        ff += (f'@font-face{{font-family:"{family}";font-weight:{w};font-style:normal;'
               f'font-display:swap;src:url(/fonts/{fname}) format("woff2")}}\n')
    if missing:
        print("Missing font files in site/fonts/ — run scripts/fetch_fonts.sh first:", *missing, sep="\n  ")
        return 1
    (SITE / "assets").mkdir(exist_ok=True)
    (SITE / "assets" / "site.css").write_text(ff + css + EXTRA_CSS, encoding="utf-8")
    print("OK  site/assets/site.css")

    kit_url = "/kalkulations-kit/#kaufen"
    shots = [("stundensatz", "Stundensatz", "Lohn, Ausfall, Gemeinkosten"),
             ("objektkalkulation", "Objektkalkulation", "Fläche, Raumart, Intervall"),
             ("angebot", "Angebot", "Füllt sich automatisch aus"),
             ("leistungswerte", "Leistungswerte", "15 Raumarten in m²/h")]
    tabs = "".join(
        f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-src="/img/kit-{k}.webp" '
        f'data-alt="Blatt {n} des Kalkulations-Kits" data-name="{n}.xlsx"><b>{n}</b><span>{d}</span></button>'
        for i, (k, n, d) in enumerate(shots))

    # ---------- Startseite ----------
    index_body = f"""
<section class="wrap" id="so-gehts">
  <div class="head"><p class="eyebrow">So funktioniert's</p><h2>In drei Schritten zum Preis, der sich rechnet</h2></div>
  <div class="steps">
    <div class="step"><h3>Stundensatz kennen</h3><p>Mit dem kostenlosen Rechner oben sehen Sie in einer Minute, was eine Stunde Reinigung Sie wirklich kostet.</p></div>
    <div class="step"><h3>Objekt kalkulieren</h3><p>Im Kalkulations-Kit tragen Sie Flächen, Raumarten und Intervalle ein. Stunden und Monatspreis rechnen sich selbst.</p></div>
    <div class="step"><h3>Angebot verschicken</h3><p>Das Angebot füllt sich automatisch aus. Drucken, als PDF speichern, an den Kunden senden.</p></div>
  </div>
</section>

<div class="band"><section class="wrap" id="einblick">
  <div class="head"><p class="eyebrow">Ein Blick in die Vorlage</p><h2>So sieht das Kalkulations-Kit aus</h2><p>Echte Ansichten aus der Excel-Datei, mit Beispielwerten gefüllt.</p></div>
  <div class="shots">
    <div class="tabs" role="tablist" aria-label="Blätter des Kalkulations-Kits">{tabs}</div>
    <div class="frame"><div class="frame-bar"><i></i><i></i><i></i><span id="shot-name" style="margin-left:8px">Stundensatz.xlsx</span></div>
      <img id="shot" src="/img/kit-stundensatz.webp" alt="Blatt Stundensatz des Kalkulations-Kits" width="1051" height="1159" loading="lazy"></div>
  </div>
</section></div>

<section class="wrap" id="probleme">
  <div class="head"><p class="eyebrow">Wo das Geld verschwindet</p><h2>Drei Rechenfehler, die gute Aufträge unrentabel machen</h2></div>
  <div class="mistakes">
    <div class="mistake"><span class="fig">≈ 20 %</span><h3>Bezahlte Stunden ohne Leistung</h3><p>Urlaub, Krankheit und Feiertage zahlen Sie trotzdem. Fehlen sie im Preis, arbeitet Ihr Team jeden fünften Tag ohne Deckung.</p></div>
    <div class="mistake"><span class="fig">m²/h</span><h3>Pauschale Leistungswerte</h3><p>Ein Büro mit Teppich braucht mehr Zeit als ein leerer Flur. Wer pauschal kalkuliert, verschenkt bei jedem Objekt Stunden.</p></div>
    <div class="mistake"><span class="fig">€/Monat</span><h3>Vergessene Gemeinkosten</h3><p>Fahrzeug, Versicherung und Buchhaltung laufen jeden Monat weiter. Sie gehören in jede verkaufte Stunde.</p></div>
  </div>
</section>

<div class="band" id="vorlagen"><section class="wrap">
  <div class="head"><p class="eyebrow">Sofort starten oder auf die Warteliste</p><h2>Fertige Vorlagen statt Bauchgefühl</h2>
  <p>Excel- und Google-Sheets-Vorlagen für Reinigungsfirmen in Deutschland, Österreich und der Schweiz. Einmal zahlen, dauerhaft nutzen. Kein Abo, kein Kurs.</p></div>
  <div class="instant">
    <div style="display:grid;gap:14px"><span class="live">Sofort verfügbar · Download</span>
      <h3 style="font-size:1.6rem">Kalkulations-Kit für Reinigungsfirmen</h3>
      {ul(["Stundensatz mit Urlaub, Krankheit und Gemeinkosten", "Objektkalkulation: Fläche, Raumart und Intervall ergeben Stunden und Monatspreis", "15 Leistungswerte in m²/h, von Büro bis Sanitär, frei anpassbar", "Angebot, das sich automatisch ausfüllt, fertig zum Drucken"])}
      <a href="/kalkulations-kit/" style="font-weight:600">Alle Details ansehen →</a></div>
    <div class="instant-buy"><div class="price"><strong>29 €</strong><span>einmalig, inkl. MwSt.</span></div>
      <a class="btn btn-dark" href="{kit_url}" data-link="kit">Jetzt kaufen und sofort herunterladen</a>
      <p class="note notice" hidden data-note="kit">Der Shop öffnet in Kürze. Schreiben Sie uns an <a href="{mailto('Kalkulations-Kit vormerken')}">{MAIL}</a>, dann melden wir uns zum Start.</p>
      <p style="font-size:.88rem;color:var(--muted)">Excel und Google Sheets. Download direkt nach dem Kauf. 30 Tage Geld-zurück-Garantie.</p></div>
  </div>
  <div class="plans">
    <div class="plan"><div class="plan-top"><div><p class="eyebrow">Für Gründer</p><h3>Starter-Kit</h3></div></div>
      {ul(["Stundensatz- und Objektkalkulation", "Angebotsvorlage nach m² und Reinigungsintervall", "Leistungsverzeichnis für Büro, Praxis, Treppenhaus", "Checkliste Gewerbeanmeldung und Versicherungen"])}
      <div class="grow"></div><div class="price"><strong>49 €</strong><span>einmalig, inkl. MwSt. · erscheint in Kürze</span></div>
      <a class="btn btn-dark" href="/warteliste/#starter">Starter-Kit: auf die Warteliste</a></div>
    <div class="plan pro"><div class="plan-top"><div><p class="eyebrow">Für laufende Betriebe</p><h3>Reinigungsfirma OS</h3></div><span class="tag">In Arbeit</span></div>
      {ul(["Alles aus dem Starter-Kit", "Einsatz- und Revierplanung für bis zu 50 Mitarbeiter", "Nachkalkulation: Soll- gegen Ist-Stunden je Objekt", "Qualitätskontrolle mit Prüfprotokoll für Kunden", "Einarbeitungs-Checklisten auf Deutsch, Türkisch und Serbisch"])}
      <div class="grow"></div><div class="price"><strong>99 €</strong><span>einmalig, inkl. MwSt. · erscheint in Kürze</span></div>
      <a class="btn btn-foam" href="/warteliste/#os">Reinigungsfirma OS: auf die Warteliste</a></div>
  </div>
  <div class="facts">
    <div class="fact"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><p><b>Digitaler Download</b>Kalkulations-Kit sofort nach dem Kauf. Starter-Kit und OS: Die Warteliste erfährt es zuerst.</p></div>
    <div class="fact"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8.5 12l2.5 2.5 4.5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><p><b>30 Tage Geld-zurück-Garantie</b>Voller Kaufpreis zurück, ohne Angabe von Gründen. <a href="/garantie/">Details</a></p></div>
    <div class="fact"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 10h18M9 10v10" stroke="currentColor" stroke-width="1.8"/></svg><p><b>Excel &amp; Google Sheets</b>Läuft auf PC, Mac und Tablet, ohne Installation.</p></div>
  </div>
</section></div>

<section class="wrap" id="fragen">
  <div class="faq-grid"><div class="head"><p class="eyebrow">Häufige Fragen</p><h2>Vor dem Kauf</h2><p>Ihre Frage ist nicht dabei? <a href="/kontakt/">Schreiben Sie uns.</a></p></div>
  <div class="faq">
    <details><summary>Gilt das für Deutschland, Österreich und die Schweiz?</summary><p>Ja. Lohn, Nebenkosten und Mehrwertsteuer tragen Sie selbst ein. Die Vorlagen rechnen mit Ihren Werten, nicht mit festen Sätzen.</p></details>
    <details><summary>Brauche ich Excel-Kenntnisse?</summary><p>Nein. Sie füllen die gelb markierten Felder aus, alles andere rechnet automatisch.</p></details>
    <details><summary>Funktioniert es mit Google Sheets?</summary><p>Ja. Laden Sie die Datei in Google Drive hoch und öffnen Sie sie mit Google Sheets. Die Vorlage nutzt nur Funktionen, die dort ebenfalls laufen.</p></details>
    <details><summary>Wie bekomme ich die Datei?</summary><p>Direkt nach der Zahlung erhalten Sie einen Download-Link auf der Bestätigungsseite und per E-Mail von Digistore24.</p></details>
    <details><summary>Bekomme ich eine Rechnung?</summary><p>Ja. Digistore24 ist Verkäufer und stellt die Rechnung aus, auf Wunsch mit Ihren Firmendaten und Ihrer USt-IdNr.</p></details>
    <details><summary>Bleibt der Rechner kostenlos?</summary><p>Ja, dauerhaft und ohne Anmeldung.</p></details>
    <details><summary>Gibt es Support?</summary><p>Ja, per E-Mail an {MAIL}. Sie erhalten in der Regel innerhalb von zwei Werktagen eine Antwort.</p></details>
  </div></div>
</section>

<div class="wrap"><div class="cta"><div><h2>Mit dem richtigen Preis ins nächste Angebot</h2><p>Kalkulations-Kit für 29 €, sofort als Download. 30 Tage Geld-zurück-Garantie.</p></div>
<a class="btn btn-foam" href="/kalkulations-kit/">Zum Kalkulations-Kit</a></div></div>
"""
    # Startseite: eigener Hero mit Rechner
    hero_idx = f"""<header class="hero" id="rechner"><div class="wrap">{nav('/#rechner')}
<div class="hero-grid"><div class="hero-copy"><p class="eyebrow">Kostenloser Rechner für Gebäudereiniger</p>
<h1>Was kostet Ihre Reinigungs&shy;stunde <em>wirklich?</em></h1>
<p class="lead">Lohn plus Gefühl reicht nicht. Rechnen Sie in einer Minute nach, welcher Stundensatz alle Kosten deckt und Gewinn übrig lässt.</p>
<ul class="proof"><li>{CHECK}Für DE, AT und CH</li><li>{CHECK}Ohne Anmeldung</li><li>{CHECK}Ausfallzeiten eingerechnet</li></ul>
<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:8px"><a class="btn btn-foam" href="/kalkulations-kit/">Kalkulations-Kit ansehen</a><a class="btn btn-line" style="color:#fff" href="#so-gehts">So funktioniert's</a></div>
</div>{form}</div></div></header>"""
    idx = page("/", "Stundensatz-Rechner für Reinigungsfirmen | Reinigungsfirma OS",
               "Kostenloser Stundensatz-Rechner für Gebäudereiniger in Deutschland, Österreich und der Schweiz. Lohn, Nebenkosten, Ausfallzeit und Gemeinkosten in einer Minute kalkulieren.",
               index_body, extra_js=f"<script>{calc_js}</script>")
    idx = re.sub(r'<header class="subhero">.*?</header>', lambda m: hero_idx, idx, count=1, flags=re.S)
    write("index.html", idx)

    # ---------- Produktseite ----------
    feats = [
        ("stundensatz", "Blatt 1 · Stundensatz", "Ihr Mindest-Stundensatz, ehrlich gerechnet",
         "Bruttolohn, Arbeitgeberanteile, Urlaub, Krankheit, Feiertage und alle Gemeinkosten von Büro bis Fahrzeug. Am Ende steht der Stundensatz netto, der alles deckt, plus Ihr Aufschlag für Wagnis und Gewinn.",
         ["Ausfallzeiten automatisch eingerechnet", "Gemeinkosten je verrechenbarer Stunde", "Netto und brutto, MwSt.-Satz frei wählbar (DE 19 %, AT 20 %, CH 8,1 %)"]),
        ("objektkalkulation", "Blatt 2 · Objektkalkulation", "Vom Grundriss zum Monatspreis",
         "Bis zu 20 Bereiche je Objekt: Fläche, Raumart und Reinigungen pro Woche. Die Vorlage rechnet Stunden je Reinigung, Stunden pro Monat und den monatlichen Pauschalpreis, auf Wunsch mit Anfahrt sowie Nacht- und Wochenendzuschlag.",
         ["Preis pro m² zur Plausibilitätsprüfung", "Zuschläge und Anfahrt optional", "Beispiel: 360 m² Büro ergibt 1.046,71 € netto im Monat (Beispielwerte)"]),
        ("leistungswerte", "Blatt 3 · Leistungswerte", "15 Raumarten, Ihre eigenen Werte",
         "Von Büro mit Teppich bis Sanitär: Richtwerte in m² pro Stunde, die Sie an Ihre Erfahrung anpassen. Zwei freie Zeilen für eigene Raumarten.",
         ["Alle Werte editierbar", "Gilt automatisch in jeder Objektkalkulation"]),
        ("angebot", "Blatt 4 · Angebot", "Ein Angebot, das sich selbst schreibt",
         "Ihre Firmendaten, die Bereiche aus der Objektkalkulation, Monatspreis netto und brutto sowie Ihre Konditionen. Fertig zum Drucken oder als PDF.",
         ["A4-Layout, druckfertig", "Konditionen frei formulierbar"]),
    ]
    fh = ""
    for i, (k, eb, h, p, pts) in enumerate(feats):
        fh += (f'<div class="feature{" rev" if i % 2 else ""}"><div class="feature-text"><p class="eyebrow">{eb}</p><h2>{h}</h2><p>{p}</p>{ul(pts)}</div>'
               f'<div class="frame"><div class="frame-bar"><i></i><i></i><i></i></div><img src="/img/kit-{k}.webp" alt="{eb} des Kalkulations-Kits" loading="lazy"></div></div>')
    kit_body = f"""
<section class="wrap" style="padding-top:0">
  <div class="product-top">
    <div class="card" style="margin-top:0">
      <p class="eyebrow">Was Sie bekommen</p>
      <h2 style="font-size:1.6rem">Eine Excel-Datei, vier Arbeitsblätter, ein fertiges Angebot</h2>
      <p style="color:var(--muted)">Das Kalkulations-Kit ist eine Vorlage für Excel (ab 2007) und Google Sheets. Gelbe Felder mit blauer Schrift sind Ihre Eingaben, alles andere rechnet. Mit einer Anleitung auf dem Start-Blatt und einer kurzen PDF-Anleitung.</p>
      {ul(["Sofort-Download nach dem Kauf (.xlsx + Anleitung als PDF)", "Für Deutschland, Österreich und die Schweiz", "Alle Zahlen sind Beispielwerte zum Überschreiben", "Nutzung für Ihren eigenen Betrieb, ohne Abo"])}
    </div>
    <aside class="buybox" id="kaufen" aria-label="Kaufen">
      <p class="eyebrow">Kalkulations-Kit</p>
      <div class="price" style="border:0;padding:0"><strong>29 €</strong><span>einmalig, inkl. MwSt.</span></div>
      <a class="btn btn-dark" href="#kaufen" data-link="kit">Jetzt kaufen und sofort herunterladen</a>
      <p class="note notice" hidden data-note="kit">Der Shop öffnet in Kürze. Schreiben Sie uns an <a href="{mailto('Kalkulations-Kit vormerken')}">{MAIL}</a>, dann melden wir uns zum Start.</p>
      {ul(["Download direkt nach der Zahlung", "30 Tage Geld-zurück-Garantie", "Rechnung von Digistore24, auch mit USt-IdNr."])}
      <small>Zahlung per PayPal, Kreditkarte, SEPA und weiteren Verfahren über Digistore24. Im Bestellformular können Sie optional das Preiserhöhungs-Paket (19 €) hinzufügen.</small>
    </aside>
  </div>
</section>
<section class="wrap">{fh}</section>
<div class="band"><section class="wrap">
  <div class="grid2">
    <div class="card"><p class="eyebrow">Für wen</p><h3>Passt zu Ihnen, wenn …</h3>{ul(["Sie Unterhaltsreinigung für Büros, Praxen oder Treppenhäuser anbieten", "Sie Angebote bisher nach Gefühl oder Erfahrungswert schreiben", "Sie gerade gründen oder Ihre Preise neu aufstellen"])}</div>
    <div class="card"><p class="eyebrow">Nicht das Richtige</p><h3>Eher nicht, wenn …</h3>{ul(["Sie eine komplette Branchensoftware mit Zeiterfassung suchen", "Sie Sonderreinigungen wie Bau- oder Glasreinigung kalkulieren wollen (folgt später)"])}</div>
  </div>
</section></div>
<section class="wrap">
  <div class="faq-grid"><div class="head"><p class="eyebrow">Kauf und Lieferung</p><h2>So läuft der Kauf</h2></div>
  <div class="faq">
    <details open><summary>Wer verkauft das Kit?</summary><p>Digistore24 ist Verkäufer, wickelt die Zahlung ab und stellt die Rechnung aus. Die Vorlage stammt von uns, <a href="/impressum/">Reinigungsfirma OS</a>.</p></details>
    <details><summary>Wann bekomme ich die Datei?</summary><p>Sofort nach der Zahlung: auf der Bestätigungsseite und per E-Mail.</p></details>
    <details><summary>Was, wenn es nicht passt?</summary><p>Innerhalb von 30 Tagen erhalten Sie den vollen Kaufpreis zurück, ohne Angabe von Gründen. <a href="/garantie/">Mehr zur Garantie</a></p></details>
    <details><summary>Ersetzt das Kit meinen Steuerberater?</summary><p>Nein. Lohnnebenkosten und Steuersätze sind Richtwerte. Bitte prüfen Sie Ihre Zahlen mit Ihrem Steuerberater.</p></details>
  </div></div>
</section>
<div class="wrap"><div class="cta"><div><h2>Ihr nächstes Angebot, sauber kalkuliert</h2><p>29 € einmalig, sofort als Download.</p></div><a class="btn btn-foam" href="#kaufen" data-link="kit">Jetzt kaufen</a></div></div>
"""
    write("kalkulations-kit/index.html", page("/kalkulations-kit/", "Kalkulations-Kit für Reinigungsfirmen | Reinigungsfirma OS",
          "Excel- und Google-Sheets-Vorlage für Reinigungsfirmen: Stundensatz, Objektkalkulation nach m² und automatisches Angebot. 29 €, Sofort-Download, 30 Tage Geld-zurück-Garantie.",
          kit_body, "/kalkulations-kit/",
          ("Excel &amp; Google Sheets · 29 €", "Kalkulations-Kit für Reinigungsfirmen",
           "Stundensatz, Objektkalkulation und ein Angebot, das sich automatisch ausfüllt. Damit jeder Auftrag seine Kosten trägt und Gewinn übrig bleibt.")))

    # ---------- Warteliste ----------
    wl = f"""<section class="wrap"><div class="grid2">
  <div class="card" id="starter"><p class="eyebrow">Für Gründer · 49 €</p><h2 style="font-size:1.5rem">Starter-Kit</h2>
  {ul(["Stundensatz- und Objektkalkulation", "Angebotsvorlage nach m² und Intervall", "Leistungsverzeichnis für Büro, Praxis, Treppenhaus", "Checkliste Gewerbeanmeldung und Versicherungen"])}
  <a class="btn btn-dark" href="{mailto('Warteliste Starter-Kit', 'Bitte informieren Sie mich, sobald das Starter-Kit erhältlich ist.')}">Per E-Mail eintragen</a></div>
  <div class="card" id="os"><p class="eyebrow">Für laufende Betriebe · 99 €</p><h2 style="font-size:1.5rem">Reinigungsfirma OS</h2>
  {ul(["Alles aus dem Starter-Kit", "Einsatz- und Revierplanung bis 50 Mitarbeiter", "Nachkalkulation Soll gegen Ist", "Prüfprotokoll und Einarbeitungs-Checklisten (DE/TR/SR)"])}
  <a class="btn btn-foam" href="{mailto('Warteliste Reinigungsfirma OS', 'Bitte informieren Sie mich, sobald Reinigungsfirma OS erhältlich ist.')}">Per E-Mail eintragen</a></div>
</div>
<div class="prose" style="margin-top:32px"><p>So funktioniert die Warteliste: Ihr E-Mail-Programm öffnet eine vorbereitete Nachricht an {MAIL}. Wir speichern Ihre Adresse nur für diese eine Benachrichtigung und löschen sie danach. Sie können sich jederzeit mit einer kurzen Antwort wieder austragen. Mehr in der <a href="/datenschutz/">Datenschutzerklärung</a>.</p>
<p>Schon jetzt erhältlich: das <a href="/kalkulations-kit/">Kalkulations-Kit für 29 €</a>.</p></div></section>"""
    write("warteliste/index.html", page("/warteliste/", "Warteliste Starter-Kit und Reinigungsfirma OS | Reinigungsfirma OS",
          "Tragen Sie sich ein und erfahren Sie zuerst, wann Starter-Kit und Reinigungsfirma OS erhältlich sind.", wl, "",
          ("Erscheint in Kürze", "Starter-Kit und Reinigungsfirma OS", "Beide Vorlagen sind in Arbeit. Tragen Sie sich ein, dann erfahren Sie es zuerst. Kein Newsletter, nur diese eine Nachricht.")))

    # ---------- Kontakt ----------
    ko = f"""<section class="wrap"><div class="grid2">
  <div class="card"><p class="eyebrow">E-Mail</p><h2 style="font-size:1.5rem">{MAIL}</h2><p style="color:var(--muted)">Wir antworten in der Regel innerhalb von zwei Werktagen. Support gibt es ausschließlich per E-Mail.</p>
  <a class="btn btn-dark" href="{mailto('Frage zu Reinigungsfirma OS')}">E-Mail schreiben</a></div>
  <div class="card"><p class="eyebrow">Schneller zum Ziel</p><h3>Häufige Anliegen</h3>
  {ul(['Download-Link verloren: Suchen Sie im Postfach nach „Digistore24“, dort steht der Link.', 'Rechnung oder Erstattung: direkt bei Digistore24 über den Link in Ihrer Kaufbestätigung, oder schreiben Sie uns.', 'Fragen zur Vorlage: Bitte nennen Sie das Blatt und die Zeile.'])}
  <p style="color:var(--muted)">Vorab lesen: <a href="/#fragen">Häufige Fragen</a> · <a href="/garantie/">Lieferung &amp; Garantie</a></p></div>
</div></section>"""
    write("kontakt/index.html", page("/kontakt/", "Kontakt | Reinigungsfirma OS", "Kontakt und Support zu den Vorlagen von Reinigungsfirma OS.", ko, "/kontakt/",
          ("Kontakt", "Fragen? Schreiben Sie uns.", "")))

    # ---------- Garantie & Lieferung ----------
    ga = f"""<section class="wrap"><div class="prose">
<h2>Lieferung</h2><p>Alle Produkte sind digitale Downloads. Es wird nichts verschickt. Nach erfolgreicher Zahlung erhalten Sie den Download-Link sofort auf der Bestätigungsseite und per E-Mail von Digistore24. Starter-Kit und Reinigungsfirma OS sind noch nicht erhältlich; dafür gibt es die <a href="/warteliste/">Warteliste</a>.</p>
<h2>Zahlung und Rechnung</h2><p>Verkäufer ist Digistore24 MSLW Limited, Dublin, Irland. Digistore24 wickelt die Zahlung ab (u. a. PayPal, Kreditkarte, SEPA-Lastschrift) und stellt die Rechnung aus, auf Wunsch mit Ihren Firmendaten und Ihrer USt-IdNr. Alle Preise sind Endpreise inkl. MwSt.</p>
<h2>30 Tage Geld-zurück-Garantie</h2><p>Wenn die Vorlage nicht zu Ihnen passt, erhalten Sie innerhalb von 30 Tagen nach dem Kauf den vollen Kaufpreis zurück, ohne Angabe von Gründen. Nutzen Sie dafür den Link in Ihrer Kaufbestätigung von Digistore24 oder schreiben Sie uns an <a href="{mailto('Erstattung Kalkulations-Kit')}">{MAIL}</a>.</p>
<h2>Widerrufsrecht</h2><p>Für Verbraucher gelten die Widerrufsbelehrung und die Geschäftsbedingungen von Digistore24, die Sie im Bestellformular vor dem Kauf einsehen. Unsere 30-Tage-Garantie gilt zusätzlich und unabhängig davon.</p>
<h2>Nutzungsrecht</h2><p>Sie dürfen die Vorlagen für Ihren eigenen Betrieb nutzen und anpassen. Weitergabe oder Weiterverkauf der Dateien ist nicht erlaubt.</p>
</div></section>"""
    write("garantie/index.html", page("/garantie/", "Lieferung und Garantie | Reinigungsfirma OS", "Digitale Lieferung, Zahlung über Digistore24 und 30 Tage Geld-zurück-Garantie.", ga, "",
          ("Kauf ohne Risiko", "Lieferung, Zahlung und Garantie", "")))

    # ---------- Impressum / Datenschutz ----------
    imp = s[s.index('<details id="impressum">'):s.index("</details>", s.index('<details id="impressum">'))]
    imp = imp[imp.index('<div class="legal-body">') + len('<div class="legal-body">'):].rsplit("</div>", 1)[0]
    write("impressum/index.html", page("/impressum/", "Impressum | Reinigungsfirma OS", "Impressum von Reinigungsfirma OS.",
          f'<section class="wrap"><div class="prose">{imp}</div></section>', "", ("Rechtliches", "Impressum", "")))
    ds = s[s.index('<details id="datenschutz">'):]
    ds = ds[ds.index('<div class="legal-body">') + len('<div class="legal-body">'):ds.index("</details>")].rsplit("</div>", 1)[0]
    ds = re.sub(r"<p><b>5\. Kauf und Warteliste</b>.*?</p>",
                "<p><b>5. Kauf</b><br>Zum Kauf werden Sie zum Bestellformular von Digistore24 weitergeleitet. Dort gelten die Datenschutzbestimmungen von Digistore24. Wir erhalten von Digistore24 die für die Lieferung und den Support nötigen Daten (Name, E-Mail-Adresse, Bestellung). Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO.</p>"
                "<p><b>6. Warteliste per E-Mail</b><br>Wenn Sie sich per E-Mail auf die Warteliste setzen, speichern wir Ihre E-Mail-Adresse ausschließlich, um Sie einmalig über die Verfügbarkeit des gewählten Produkts zu informieren (Art. 6 Abs. 1 lit. a DSGVO). Danach löschen wir sie. Sie können die Einwilligung jederzeit per E-Mail widerrufen.</p>",
                ds, flags=re.S)
    ds = ds.replace("<p><b>6. E-Mail-Kontakt</b>", "<p><b>7. E-Mail-Kontakt</b>").replace("<p><b>7. Ihre Rechte</b>", "<p><b>8. Ihre Rechte</b>")
    write("datenschutz/index.html", page("/datenschutz/", "Datenschutzerklärung | Reinigungsfirma OS", "Datenschutzerklärung von Reinigungsfirma OS. Keine Cookies, kein Tracking.",
          f'<section class="wrap"><div class="prose">{ds}</div></section>', "", ("Rechtliches", "Datenschutzerklärung", "")))

    # ---------- Danke (nach dem Kauf) ----------
    dk = f"""<section class="wrap"><div class="grid2">
<div class="card"><p class="eyebrow">Nächste Schritte</p><h2 style="font-size:1.5rem">So geht es weiter</h2>
{ul(["Den Download-Link finden Sie auf der Bestätigungsseite und in der E-Mail von Digistore24.", "Öffnen Sie zuerst START-HIER.pdf und danach die Excel-Datei.", "Gelbe Felder ausfüllen, der Rest rechnet automatisch."])}</div>
<div class="card"><p class="eyebrow">Hilfe</p><h3>Kein Link angekommen?</h3><p style="color:var(--muted)">Prüfen Sie den Spam-Ordner und suchen Sie nach „Digistore24“. Hilft das nicht, schreiben Sie uns an <a href="{mailto('Download-Link fehlt')}">{MAIL}</a>.</p></div>
</div>
<p class="notice" style="margin-top:28px">Die Abbuchung erfolgt durch Digistore24.com. · The debit will be performed by Digistore24.com.</p></section>"""
    dh = page("/danke/", "Vielen Dank für Ihren Kauf | Reinigungsfirma OS", "Bestätigung nach dem Kauf.", dk, "",
              ("Bestellung erhalten", "Vielen Dank für Ihren Kauf!", "Ihr Kalkulations-Kit ist bereit."))
    write("danke/index.html", dh.replace("<head>\n", '<head>\n<meta name="robots" content="noindex">\n', 1))

    # ---------- 404 ----------
    nf = page("/404", "Seite nicht gefunden | Reinigungsfirma OS", "Seite nicht gefunden.",
              '<section class="wrap"><div class="prose"><p>Die Seite gibt es nicht (mehr). Weiter zum <a href="/">Stundensatz-Rechner</a> oder zum <a href="/kalkulations-kit/">Kalkulations-Kit</a>.</p></div></section>',
              "", ("Fehler 404", "Seite nicht gefunden", ""))
    write("404.html", nf.replace("<head>\n", '<head>\n<meta name="robots" content="noindex">\n', 1))

    urls = ["/", "/kalkulations-kit/", "/warteliste/", "/kontakt/", "/garantie/", "/impressum/", "/datenschutz/"]
    today = date.today().isoformat()
    (SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    print("OK  site/sitemap.xml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
