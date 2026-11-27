"""A 6 magyar tesztminta (Nóra, 2026-11-24) pattern.json-jainak előállítása. Futtatás: python3 horgolas/hu6_build.py"""
import json
from pathlib import Path
M = Path(__file__).parent / "mintak"

def R(lhu, len_, hu, en, count=None, prev=None, change=None):
    r = {"label_hu": lhu, "label_en": len_, "hu": hu, "en": en}
    if count is not None: r["count"] = count
    if prev is not None: r["prev"], r["change"] = prev, change
    return r

def inc_rounds(start_round, start, end):
    """Lapos kör szaporítása 6-tal körönként: (k rp, szap) x6."""
    rows = []; n = start; r = start_round
    while n < end:
        k = n // 6 - 1
        hu = "1 lsz. " + ("Minden szembe szaporítás." if k == 0 else f"*{k} rp, 1 szap.* A *-tól *-ig ismételd még 5-ször.") + " Zárd a kört 1 ksz-mel az első rp-ba."
        en = "Ch 1. " + ("Inc in each st around." if k == 0 else f"*Sc in the next {k} sts, inc in the next st.* Repeat from * to * 5 more times.") + " Join with a sl st to the first sc."
        rows.append(R(f"{r}. kör", f"Round {r}", hu, en, n + 6, n, 6)); n += 6; r += 1
    return rows, r, n

def spiral_inc(start_round, start, end):
    rows = []; n = start; r = start_round
    while n < end:
        k = n // 6 - 1
        hu = "Minden szembe szaporítás." if k == 0 else f"*{k} rp, 1 szap.* Ismételd 6-szor."
        en = "Inc in each st around." if k == 0 else f"*Sc in the next {k} sts, inc in the next st.* Repeat 6 times."
        rows.append(R(f"{r}. kör", f"Round {r}", hu, en, n + 6, n, 6)); n += 6; r += 1
    return rows, r, n

def spiral_dec(start_round, start, end):
    rows = []; n = start; r = start_round
    while n > end:
        k = n // 6 - 2
        hu = "Minden 2 szemet fogyassz össze." if k == 0 else f"*{k} rp, 1 fogy.* Ismételd 6-szor."
        en = "Sc2tog around." if k == 0 else f"*Sc in the next {k} sts, sc2tog.* Repeat 6 times."
        rows.append(R(f"{r}. kör", f"Round {r}", hu, en, n - 6, n, -6)); n -= 6; r += 1
    return rows, r, n

def mat(hu, en): return {"text_hu": hu, "text_en": en}
MR6 = R("1. kör", "Round 1", "Varázsgyűrű, 1 lsz, 6 rp a gyűrűbe. Húzd össze.", "Magic ring, ch 1, 6 sc into the ring. Pull tight.", 6)
SPIRAL_NOTE = {"text_hu": "Csigavonalban (spirálban) horgolunk, a köröket nem zárjuk. Jelöld a kör elejét szemjelölővel.", "text_en": "Worked in a continuous spiral; do not join rounds. Use a stitch marker for the first stitch."}
BASE = {"langs": ["hu", "en"], "statusz": "tesztre_var"}

P = []
# 1 – KEZDŐ: poháralátét
rows, r, n = inc_rounds(2, 6, 36)
P.append(dict(BASE, slug="kerek-poharalatet", name_hu="Kerek poháralátét – horgolásminta", name_en="Round Crochet Coaster – Crochet Pattern",
  tagline_hu="Az első kerek darabod: csak rövidpálca és szaporítás. Kb. 30 perc.", tagline_en="Your first circle: only single crochet and increases. About 30 minutes.",
  level_hu="1/6 – Kezdő", level_en="1/6 – Beginner", size_hu="kb. 10 cm átmérő", size_en="approx. 10 cm (4 in) across", hook="4 mm",
  gauge_hu="Nem lényeges, de horgolj szorosan, hogy laposan feküdjön.", gauge_en="Not critical; work tightly so it lies flat.",
  materials=[mat("Közepes vastagságú pamutfonal, kb. 15 g, bármilyen színben", "Worsted cotton yarn, about 15 g, any colour"), mat("4 mm horgolótű, varrótű, olló", "4 mm hook, tapestry needle, scissors")],
  abbr=["ch", "sl st", "sc", "inc", "MR", "st"], notes=[{"text_hu": "A kör végén zárunk, és minden kört 1 lsz-mel kezdünk (nem számít szemnek).", "text_en": "Each round is joined; the ch 1 at the start does not count as a stitch."}],
  sections=[{"title_hu": "Alátét", "title_en": "Coaster", "rows": [R("1. kör", "Round 1", "Varázsgyűrű, 1 lsz, 6 rp a gyűrűbe. Húzd össze, zárd 1 ksz-mel.", "Magic ring, ch 1, 6 sc into the ring. Pull tight, join with a sl st.", 6)] + rows +
   [R(f"{r}. kör", f"Round {r}", "Szegély: minden szembe 1 ksz, lazán. Vágd el a fonalat.", "Edging: sl st loosely in each st around. Fasten off.", 36, 36, 0)]}],
  finishing=[{"text_hu": "Dolgozd el a szálvégeket. Ha hullámos, nedvesítsd meg, és laposan szárítsd.", "text_en": "Weave in ends. If it ruffles, wet it and dry flat."}]))
# 2 – KEZDŐ+: mosogatórongy félpálcával
P.append(dict(BASE, slug="felpalcas-mosogatorongy", name_hu="Félpálcás mosogatórongy – horgolásminta", name_en="Half Double Crochet Dishcloth – Crochet Pattern",
  tagline_hu="Egyenes sorok félpálcával, szegéllyel. Kb. 1,5 óra.", tagline_en="Straight rows of half double crochet with a border. About 1.5 hours.",
  level_hu="2/6 – Kezdő", level_en="2/6 – Beginner", size_hu="kb. 20 × 20 cm", size_en="approx. 20 × 20 cm (8 × 8 in)", hook="4,5 mm",
  gauge_hu="15 fp = 10 cm", gauge_en="15 hdc = 10 cm (4 in)",
  materials=[mat("Közepes vastagságú 100% pamutfonal, kb. 45 g", "Worsted 100% cotton yarn, about 45 g"), mat("4,5 mm horgolótű, varrótű, olló", "4.5 mm hook, tapestry needle, scissors")],
  abbr=["ch", "sl st", "sc", "hdc", "st"], notes=[{"text_hu": "A sor eleji 2 lsz nem számít szemnek.", "text_en": "The ch 2 at the start of a row does not count as a stitch."}],
  sections=[{"title_hu": "Rongy", "title_en": "Dishcloth", "rows": [
    R("1. sor", "Row 1", "Horgolj 32 lsz-t. A tűtől számított 3. lsz-be 1 fp, majd minden további lsz-be 1 fp. Fordítsd meg.", "Ch 32. Hdc in the 3rd ch from hook and in each ch across. Turn.", 30),
    R("2–22. sor", "Rows 2–22", "2 lsz, minden szembe 1 fp. Fordítsd meg.", "Ch 2, hdc in each st across. Turn.", 30, 30, 0)]},
   {"title_hu": "Szegély", "title_en": "Border", "rows": [
    R("Szegély", "Border", "1 lsz, rövidpálcával horgold körbe: az oldalakon minden sorvégbe 1 rp, minden sarokba 3 rp. Zárd 1 ksz-mel, vágd el a fonalat.", "Ch 1, sc evenly around: 1 sc in each row end on the sides, 3 sc in each corner. Join with a sl st and fasten off.")]}],
  finishing=[{"text_hu": "Dolgozd el a szálvégeket. Mosható 40 °C-on.", "text_en": "Weave in ends. Washable at 40 °C."}]))
# 3 – KÖNNYŰ: nagymama-négyzet
gs = [R("1. kör", "Round 1", "Varázsgyűrű. 3 lsz (1 ep-nak számít), 2 ep, 2 lsz, *3 ep, 2 lsz* – ezt még 2-szer. Zárd 1 ksz-mel a 3. lsz-be.", "Magic ring. Ch 3 (counts as dc), 2 dc, ch 2, *3 dc, ch 2* 2 more times. Join with a sl st to the top of ch 3.", 12)]
for i, n in ((2, 12), (3, 24), (4, 36)):
    side_hu = " A sarokcsoportok közé 1 lsz-t horgolj." if i == 2 else f" A csoportok között mindig 1 lsz; az oldalakon minden 1 lsz-es ívbe 3 ep (oldalanként {i - 2} csoport)."
    side_en = " Ch 1 between the corner groups." if i == 2 else f" Ch 1 between all groups; along each side work 3 dc in every ch-1 space ({i - 2} group(s) per side)."
    gs.append(R(f"{i}. kör", f"Round {i}", f"Ksz-mel menj be az első sarokívbe. 3 lsz, 2 ep, 2 lsz, 3 ep ugyanabba az ívbe (sarok). Minden további sarokívbe: 3 ep, 2 lsz, 3 ep.{side_hu} Zárd 1 ksz-mel.",
                f"Sl st into the first corner space. Ch 3, 2 dc, ch 2, 3 dc in the same space (corner). In every other corner space: 3 dc, ch 2, 3 dc.{side_en} Join with a sl st.", n + 12, n, 12))
P.append(dict(BASE, slug="nagymama-negyzet", name_hu="Klasszikus nagymama-négyzet – horgolásminta", name_en="Classic Granny Square – Crochet Pattern",
  tagline_hu="Pálca-csoportok és sarkok: a takarók és táskák alapja. Kb. 40 perc.", tagline_en="Dc clusters and corners: the base of blankets and bags. About 40 minutes.",
  level_hu="3/6 – Könnyű", level_en="3/6 – Easy", size_hu="kb. 12 × 12 cm (4 kör)", size_en="approx. 12 × 12 cm (4 rounds)", hook="4 mm",
  gauge_hu="Nem lényeges.", gauge_en="Not critical.", materials=[mat("Közepes vastagságú fonal, 2–4 szín, összesen kb. 15 g", "Worsted yarn, 2–4 colours, about 15 g in total"), mat("4 mm horgolótű, varrótű, olló", "4 mm hook, tapestry needle, scissors")],
  abbr=["ch", "sl st", "dc", "MR", "st"], notes=[{"text_hu": "A kör eleji 3 lsz 1 ep-nak számít. A szemszám a pálcák száma (az ívek nélkül). Színt minden kör végén válthatsz.", "text_en": "Ch 3 at the start counts as a dc. Stitch counts are dc only. You may change colour at the end of any round."}],
  sections=[{"title_hu": "Négyzet", "title_en": "Square", "rows": gs}],
  finishing=[{"text_hu": "Dolgozd el a szálvégeket, és gőzöld/nedvesítsd laposra.", "text_en": "Weave in ends and block flat."}]))
# 4 – KÖZEPES: amigurumi labda
a, r, n = spiral_inc(2, 6, 36)
plain = R(f"{r}–{r + 5}. kör", f"Rounds {r}–{r + 5}", "Minden szembe 1 rp (6 kör).", "Sc in each st around (6 rounds).", 36, 36, 0); r += 6
d1, r, n2 = spiral_dec(r, 36, 18)
stuff = R("Tömés", "Stuffing", "Töltsd ki keményre a labdát.", "Stuff the ball firmly.")
d2, r, n3 = spiral_dec(r, 18, 6)
P.append(dict(BASE, slug="amigurumi-labda", name_hu="Amigurumi labda – horgolásminta", name_en="Amigurumi Ball – Crochet Pattern",
  tagline_hu="Spirál, szaporítás, fogyasztás, tömés: az amigurumi alapja. Kb. 1,5 óra.", tagline_en="Spiral, increase, decrease and stuffing: amigurumi basics. About 1.5 hours.",
  level_hu="4/6 – Közepes", level_en="4/6 – Intermediate", size_hu="kb. 8 cm átmérő", size_en="approx. 8 cm (3 in) across", hook="3,5 mm",
  gauge_hu="Horgolj szorosan, hogy ne látsszon át a tömés.", gauge_en="Work tightly so the stuffing doesn't show.",
  materials=[mat("Közepes vastagságú pamut- vagy akrilfonal, kb. 20 g", "Worsted cotton or acrylic yarn, about 20 g"), mat("3,5 mm horgolótű, szemjelölő, tömőanyag (kb. 15 g), varrótű", "3.5 mm hook, stitch marker, fibrefill (about 15 g), tapestry needle")],
  abbr=["sc", "inc", "sc2tog", "MR", "st"], notes=[SPIRAL_NOTE],
  sections=[{"title_hu": "Labda", "title_en": "Ball", "rows": [MR6] + a + [plain] + d1 + [stuff] + d2}],
  finishing=[{"text_hu": "Fűzd át a fonalat a maradék 6 szem elülső szálán, húzd össze, és dolgozd el. 3 év alattiaknak csak biztonságosan bevarrva.", "text_en": "Thread the tail through the front loops of the last 6 sts, pull tight and weave in. For under 3s, make sure everything is sewn securely."}]))
# 5 – KÖZEPES+: amigurumi csibe
b, r, n = spiral_inc(2, 6, 24)
P.append(dict(BASE, slug="amigurumi-csibe", name_hu="Amigurumi csibe – horgolásminta", name_en="Amigurumi Chick – Crochet Pattern",
  tagline_hu="Egytestes figura csőrrel, szárnnyal, bóbitával; az összevarrás gyakorlása. Kb. 2 óra.", tagline_en="One-piece figure with beak, wings and tuft; practise assembly. About 2 hours.",
  level_hu="5/6 – Közepes", level_en="5/6 – Intermediate", size_hu="kb. 7 cm magas", size_en="approx. 7 cm (2.75 in) tall", hook="3,5 mm",
  gauge_hu="Szorosan horgolj.", gauge_en="Work tightly.",
  materials=[mat("Közepes vastagságú fonal: sárga (15 g), narancs (2 g)", "Worsted yarn: yellow (15 g), orange (2 g)"), mat("2 db 6 mm-es biztonsági szem (vagy fekete fonal hímzéshez), tömőanyag, 3,5 mm tű, szemjelölő, varrótű", "Two 6 mm safety eyes (or black yarn to embroider), fibrefill, 3.5 mm hook, marker, tapestry needle")],
  abbr=["sc", "inc", "sc2tog", "MR", "st", "sl st", "ch"], notes=[SPIRAL_NOTE, {"text_hu": "3 év alatti gyereknek biztonsági szem helyett hímezd a szemeket.", "text_en": "For children under 3, embroider the eyes instead of using safety eyes."}],
  sections=[
   {"title_hu": "Test (sárga)", "title_en": "Body (yellow)", "rows": [MR6] + b + [
     R(f"{r}–{r + 5}. kör", f"Rounds {r}–{r + 5}", "Minden szembe 1 rp (6 kör). A 4. és 5. kör között tedd be a szemeket, 5 szem távolságra egymástól (a varázsgyűrű a fej teteje).", "Sc in each st around (6 rounds). Insert the eyes between rounds 4 and 5, 5 sts apart (the magic ring is the top of the head).", 24, 24, 0),
     R(f"{r + 6}. kör", f"Round {r + 6}", "*2 rp, 1 fogy.* Ismételd 6-szor.", "*Sc in the next 2 sts, sc2tog.* Repeat 6 times.", 18, 24, -6),
     R(f"{r + 7}. kör", f"Round {r + 7}", "*1 rp, 1 fogy.* Ismételd 6-szor. Töltsd ki a testet.", "*Sc in the next st, sc2tog.* Repeat 6 times. Stuff the body.", 12, 18, -6),
     R(f"{r + 8}. kör", f"Round {r + 8}", "Minden 2 szemet fogyassz össze. Húzd össze a nyílást.", "Sc2tog around. Close the opening.", 6, 12, -6)]},
   {"title_hu": "Csőr (narancs)", "title_en": "Beak (orange)", "rows": [
     R("1. kör", "Round 1", "Varázsgyűrű, 4 rp.", "Magic ring, 4 sc.", 4),
     R("2. kör", "Round 2", "*1 rp, 1 szap.* Ismételd 2-szer. Vágd el hosszú szállal, ne töltsd ki.", "*Sc in the next st, inc.* Repeat twice. Fasten off with a long tail; do not stuff.", 6, 4, 2)]},
   {"title_hu": "Szárny (sárga, 2 db)", "title_en": "Wing (yellow, make 2)", "rows": [
     R("1. kör", "Round 1", "Varázsgyűrű, 6 rp.", "Magic ring, 6 sc.", 6),
     R("2. kör", "Round 2", "*1 rp, 1 szap.* Ismételd 3-szor. Hajtsd félbe laposra, vágd el hosszú szállal.", "*Sc in the next st, inc.* Repeat 3 times. Fold flat, fasten off with a long tail.", 9, 6, 3)]}],
  finishing=[{"text_hu": "Varrd a csőrt a 6. körbe, középre a két szem alá.", "text_en": "Sew the beak onto round 6, centred below the eyes."},
             {"text_hu": "Varrd a szárnyakat a test két oldalára, a 7. kör magasságában.", "text_en": "Sew the wings to the sides at round 7."},
             {"text_hu": "Bóbita: a fej tetején (a varázsgyűrűnél) húzz át 3 sárga szálat, csomózd meg, és vágd 1,5 cm-esre.", "text_en": "Tuft: pull 3 strands of yellow through the top of the head (the magic ring), knot and trim to 1.5 cm."}]))
# 6 – HALADÓ: kerek kosár fülekkel
k, r, n = inc_rounds(2, 6, 60)
moss_hu = "1 lsz, *1 rp, 1 lsz, ugorj át 1 szemet* körbe; a következő körökben az rp-t mindig az előző kör lsz-ívébe horgold. Zárd 1 ksz-mel."
moss_en = "Ch 1, *sc, ch 1, skip 1* around; on later rounds work each sc into the ch-1 space of the round below. Join with a sl st."
P.append(dict(BASE, slug="kerek-kosar-fulekkel", name_hu="Kerek kosár fülekkel – horgolásminta", name_en="Round Basket with Handles – Crochet Pattern",
  tagline_hu="Lapos alj, hátsó szálas fordulósor, mohaminta-oldal és fülek. Kb. 4 óra.", tagline_en="Flat base, back-loop turning round, moss-stitch sides and handles. About 4 hours.",
  level_hu="6/6 – Haladó", level_en="6/6 – Advanced beginner+", size_hu="kb. 18 cm átmérő, 12 cm magas", size_en="approx. 18 cm (7 in) across, 12 cm (4.75 in) tall", hook="6 mm",
  gauge_hu="12 rp = 10 cm (dupla szállal). Ha a kosár alja hullámos, válts kisebb tűre.", gauge_en="12 sc = 10 cm with yarn held double. If the base ruffles, go down a hook size.",
  materials=[mat("Vastag (chunky) pamut- vagy pólófonal, kb. 250 g, vagy közepes fonal duplán", "Chunky cotton or T-shirt yarn, about 250 g, or worsted yarn held double"), mat("6 mm horgolótű, szemjelölő, varrótű", "6 mm hook, stitch marker, tapestry needle")],
  abbr=["ch", "sl st", "sc", "inc", "MR", "st", "BLO"], notes=[{"text_hu": "Az alj körei zártak. A mohamintás körökben a szemszám: 30 rp + 30 lsz = 60.", "text_en": "Base rounds are joined. In moss-stitch rounds the count is 30 sc + 30 ch = 60."}],
  sections=[{"title_hu": "Alj", "title_en": "Base", "rows": [R("1. kör", "Round 1", "Varázsgyűrű, 1 lsz, 6 rp. Zárd 1 ksz-mel.", "Magic ring, ch 1, 6 sc. Join with a sl st.", 6)] + k},
   {"title_hu": "Oldal", "title_en": "Sides", "rows": [
     R(f"{r}. kör", f"Round {r}", "1 lsz, minden szembe 1 rp csak a hátsó szálba (ettől fordul fel az oldal). Zárd.", "Ch 1, sc in the back loop only of each st (this turns the side up). Join.", 60, 60, 0),
     R(f"{r + 1}–{r + 10}. kör", f"Rounds {r + 1}–{r + 10}", moss_hu, moss_en, 60, 60, 0)]},
   {"title_hu": "Fülek és szegély", "title_en": "Handles and edge", "rows": [
     R(f"{r + 11}. kör", f"Round {r + 11}", "1 lsz, 10 rp, 10 lsz, ugorj át 10 szemet, 20 rp, 10 lsz, ugorj át 10 szemet, 10 rp. Zárd.", "Ch 1, sc 10, ch 10, skip 10, sc 20, ch 10, skip 10, sc 10. Join.", 60, 60, 0),
     R(f"{r + 12}. kör", f"Round {r + 12}", "1 lsz, minden szembe 1 rp, a 10 lsz-es ívekbe 10-10 rp. Zárd.", "Ch 1, sc in each st, 10 sc into each ch-10 space. Join.", 60, 60, 0),
     R(f"{r + 13}. kör", f"Round {r + 13}", "Rákszem (rövidpálca balról jobbra) vagy ksz minden szembe. Vágd el a fonalat.", "Reverse sc (crab stitch) or sl st in each st around. Fasten off.", 60, 60, 0)]}],
  finishing=[{"text_hu": "Dolgozd el a szálvégeket a kosár belsején.", "text_en": "Weave in ends on the inside."}]))

for p in P:
    (M / p["slug"]).mkdir(parents=True, exist_ok=True)
    old = M / p["slug"] / "pattern.json"
    if old.exists() and "de" in json.load(open(old)).get("langs", []):
        print("kihagyva (már van DE szöveg, kézzel szerkeszd):", p["slug"]); continue
    json.dump(p, open(M / p["slug"] / "pattern.json", "w"), ensure_ascii=False, indent=1)
print([p["slug"] for p in P])
