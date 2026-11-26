"""Ábrák (kész forma + horgolásrajz) beírása a pattern.json-okba. Futtasd a hu6_build.py után: python3 horgolas/abrak.py"""
import json
from pathlib import Path
M = Path(__file__).parent / "mintak"
L = lambda hu, en, de=None: {"hu": hu, "en": en, "de": de or en}
def cap(hu, en, de=None): return {"cap_hu": hu, "cap_en": en, "cap_de": de or en}
def shp(kind, c, **a): return dict(fn="shape", args=dict(kind=kind, **a), **c)
def ch(fn, c, **a): return dict(fn=fn, args=a, **c)
F = {
 "kerek-poharalatet": ([shp("circle", cap("Kész forma", "Finished shape"), d=L("≈ 10 cm", "≈ 10 cm (4 in)")),
                        ch("circle_chart", cap("Horgolásrajz körönként (a 7. kör ksz-szegély)", "Chart by round (round 7 = sl st edging)"), counts=[6, 12, 18, 24, 30, 36])], ["ch", "sl", "sc", "inc", "mr"]),
 "felpalcas-mosogatorongy": ([shp("square", cap("Kész forma (szegéllyel)", "Finished shape (with border)"), w=L("≈ 20 cm", "≈ 20 cm (8 in)"), h=L("≈ 20 cm", "≈ 20 cm")),
                              ch("row_chart", cap("Az első 6 sor; a 22. sorig ugyanígy (30 fp soronként)", "First 6 rows; repeat up to row 22 (30 hdc per row)"), widths=[30] * 6, stitch="hdc", found_ch=32)], ["ch", "hdc", "sc"]),
 "nagymama-negyzet": ([shp("square", cap("Kész forma (4 kör)", "Finished shape (4 rounds)"), w=L("≈ 12 cm", "≈ 12 cm"), h=L("≈ 12 cm", "≈ 12 cm")),
                       ch("granny_chart", cap("Horgolásrajz: sarkokban 3 ep, 2 lsz, 3 ep; a csoportok között 1 lsz", "Chart: corners 3 dc, ch 2, 3 dc; ch 1 between groups"), rounds=4)], ["ch", "sl", "dc", "mr"]),
 "amigurumi-labda": ([shp("ball", cap("Kész forma", "Finished shape"), d=L("≈ 8 cm", "≈ 8 cm (3 in)"), label=L("36 szem a közepén", "36 sts at the widest")),
                      ch("circle_chart", cap("1–6. kör felülről nézve (szaporítás). A 13–17. kör ugyanez visszafelé, kék fogyasztással.", "Rounds 1–6 seen from above (increases). Rounds 13–17 mirror this with decreases."), counts=[6, 12, 18, 24, 30, 36])], ["sc", "inc", "dec", "mr"]),
 "amigurumi-csibe": ([shp("chick", cap("Kész forma és összeállítás", "Finished shape and assembly"), eyes=L("szemek: 4–5. kör, 5 szem távol", "eyes: rounds 4–5, 5 sts apart"), wings=L("szárny: 7. kör", "wings: round 7"), h=L("≈ 7 cm", "≈ 7 cm")),
                      ch("circle_chart", cap("Test 1–4. kör felülről (szaporítás)", "Body rounds 1–4 from above (increases)"), counts=[6, 12, 18, 24])], ["sc", "inc", "dec", "mr"]),
 "kerek-kosar-fulekkel": ([shp("basket", cap("Kész forma oldalnézetből", "Finished shape, side view"), d=L("≈ 18 cm", "≈ 18 cm (7 in)"), h=L("≈ 12 cm", "≈ 12 cm"), base=L("alj: 10 kör, 60 szem", "base: 10 rounds, 60 sts")),
                           ch("circle_chart", cap("Az alj 1–10. köre (szaporítás körönként 6 szemmel)", "Base rounds 1–10 (6 increases per round)"), counts=[6, 12, 18, 24, 30, 36, 42, 48, 54, 60])], ["ch", "sl", "sc", "inc", "mr"]),
 "flat-christmas-tree-ornament": ([shp("tree", cap("Kész forma", "Finished shape", "Fertige Form"), w=L("≈ 7 cm", "≈ 7 cm (2.75 in)"), h=L("≈ 9 cm", "≈ 9 cm (3.5 in)")),
                                   ch("row_chart", cap("Fa: 14 sor alulról felfelé, a kék szemek a fogyasztások", "Tree: 14 rows bottom to top, blue = decreases", "Baum: 14 Reihen von unten nach oben, blau = Abnahmen"), widths=[15, 13, 13, 11, 11, 9, 9, 7, 7, 5, 5, 3, 3, 1], found_ch=16)], ["ch", "sc", "dec"]),
 "mini-door-wreath": ([shp("wreath", cap("Kész forma", "Finished shape", "Fertige Form"), d=L("≈ 12 cm", "≈ 12 cm (4.75 in)")),
                       ch("circle_chart", cap("Koszorú: 30 lsz-es gyűrű, majd 5 kör", "Wreath: ring of 30 ch, then 5 rounds", "Kranz: Ring aus 30 Lm, dann 5 Runden"), counts=[30, 36, 42, 48, 48], ring_ch=30)], ["ch", "sl", "sc", "inc"]),
 "crochet-snowflake-ornament": ([shp("circle", cap("Kész méret", "Finished size", "Fertige Größe"), d=L("≈ 9 cm", "≈ 9 cm (3.5 in)")),
                                 ch("snowflake_chart", cap("Horgolásrajz (3 kör)", "Stitch chart (3 rounds)", "Häkelschrift (3 Runden)"))], ["ch", "sl", "sc", "mr"]),
 "crochet-heart-applique": ([ch("heart_chart", cap("Horgolásrajz: minden szem a varázsgyűrűbe", "Chart: every stitch goes into the magic ring", "Häkelschrift: alle Maschen in den Fadenring"))], ["ch", "sl", "hdc", "dc", "mr"]),
}
for slug, (figs, leg) in F.items():
    p = M / slug / "pattern.json"; d = json.loads(p.read_text()); d["figures"] = figs; d["legend"] = leg
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1)); print("ok", slug)
