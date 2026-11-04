# Norelia – Startsystem (AI cég agent rendszer)

A **Startsystem** a cégfelépítésünk neve: ez a repó egy "AI cég": a **Főnök** agent irányít, alatta osztály-agentek dolgoznak.
Minden agent ezt a fájlt és a `ceg/` mappát olvassa közös memóriaként.

## Az egyetlen cél
**Havi nettó 1 000 000 Ft vagy több az összes Norelia-projektből, amilyen hamar csak lehet.**
- Hosszú táv: 1,5 M Ft/hó side bevétel 12 hónapon belül (Nóra személyes célja).
- Nóra ideje: max 30 óra/hét. Óraérték-mérce: 8 750–19 000 Ft/óra.

## Projektek (részletek: `ceg/projektek.md`)
1. **AureliaVenn** – digitális termékek: Etsy + Amazon KDP + további csatornák
2. **Reinigungsfirma OS** – digitális csomag német takarítócég-alapítóknak
3. **Reinigungs-Kalkulator** – ajánlatkalkulátor takarítócégeknek (sablon → havidíjas eszköz)

Elv: csak olyan projekt, amihez Nóra fizikailag nem kell.

Ebben a rendszerben **nincs max. 3 projekt szabály**: új projekt bármikor jöhet, ha a Ft/óra számítás igazolja. **De hetente max 3 projekt kap Nóra-időt** (a többi csak automatán fut). KDP: csak másodlagos csatorna meglévő printable-ekhez. (Döntés: 2026-11-04)

## Szervezet
```
                      Nóra (tulajdonos, jóváhagy)
                               │
                         FŐNÖK (fonok)
   ┌─────────┬─────────┬─────────┼─────────┬─────────┬──────────┬──────────┐
marketing  sales  ecommerce tartalom  penzugy  palyazat  operacio
```
Definíciók: `.claude/agents/*.md`. Indítás: `claude --agent fonok`.
Heti ritmus: hétfő reggel automatikus Főnök-futás → `ceg/heti/ÉÉÉÉ-HH-NN.md`.

## Közös szabályok (minden agentre)
1. **Végrehajtás először**: kész anyagot adj (szöveg, táblázat, e-mail piszkozat), ne tanácsot.
2. **Pénz-mérce**: minden javaslatnál: várható Ft, ráfordított óra, Ft/óra. 8 750 Ft/óra alatt → elvetni vagy automatizálni.
3. **Jóváhagyási kapu**: ami kimegy vagy tartósan változtat (e-mail küldés, Etsy/Amazon listing élesítése, Apollo/monday írás, közzététel, fizetés) → csak piszkozat + egysoros terv, Nóra jóváhagyása után mehet.
4. **Előbb teszt**: új ötlet előbb max 1 hét és 30–50 000 Ft piaci teszt; keret max 100 000 Ft és 8 óra/hét.
5. **Napló**: minden döntés és eredmény → `ceg/naplo.md` (dátum, ki, mit, eredmény Ft-ban).
6. Magyarul, tömören. Döntésnél: ÉRTÉKELÉS – DÖNTÉS – MIÉRT – KÖVETKEZŐ LÉPÉS.

## Projektmappák (2026-11-04 óta egy repóban)
| Mappa | Mi | Saját szabályok |
|---|---|---|
| `projects/reinigungsfirma-os/` | DACH landing (src → build → site), Kalkulations-Kit generátor, marketing, jogi doksi | `projects/reinigungsfirma-os/CLAUDE.md` |
| `projects/aureliavenn-etsy/` | Etsy bolt (24 listing, POD + digitális), Emily, heti metrikák | `projects/aureliavenn-etsy/CLAUDE.md` |
| `projects/pet-printables/` | kutyás/macskás printable-gyártósor (HTML → Playwright → PDF), napi ütemezés | `projects/pet-printables/CLAUDE.md` |
| `projects/complystarterkit/`, `law-firm-websites/`, `haccp-app/`, `zanahalisi/` | további side projektek (README) | – |
| `ceg/portfolio/` | portfólió (aktív/parkoló/elvetett), döntések, tanulságok, eszközök, feladatok – a korábbi side-projects repóból | – |

Szabály: egy projektmappán belül **annak a CLAUDE.md-je az irányadó** (nyelv, design, build, jogi szabályok); a Főnök és a cél ez a fájl. Nyitott ellentmondások: `ceg/osszevonas.md`.

## monday (workspace: NóRa HéJja Vibes → mappa: Norelia)
| Tábla | ID |
|---|---|
| Termékek | 5107073512 |
| Tartalomnaptár | 5107073533 |
| Affiliate pipeline | 5107073538 |
| KPI | 5107073541 |

## Eszközök
Lásd `ceg/eszkozok.md` – mi van bekötve, mi hiányzik.
