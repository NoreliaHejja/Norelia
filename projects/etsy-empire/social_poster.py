#!/usr/bin/env python3
"""
Social poster – etsy-empire

A termék listing.json-jából platformonkénti posztcsomagot készít
(Pinterest, Instagram, Facebook, TikTok) Emily hangján, és a
marketing_szovegek/<slug>_social.json fájlba írja „jovahagyasra_var” státusszal.

Ütemezés: Claude a Metricool-kapcsolaton keresztül, CSAK Nóra jóváhagyása után
(és amikor a közösségi fiókok be vannak kötve a Metricoolba). A script maga nem posztol.

Használat
  python3 social_poster.py termekek/<slug> [--etsy-link https://...]
"""
import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AI_LABEL = "AI-generated character"  # Emily AI-karakter → kötelező jelölés


def build(data: dict, link: str) -> dict:
    e = data["etsy"]
    name = e["title"].split(",")[0]
    tags = [t.replace(" ", "") for t in e["tags"][:6]]
    start = date.today() + timedelta(days=1)
    return {
        "slug": data["slug"],
        "status": "jovahagyasra_var",
        "link": link,
        "posts": [
            {
                "platform": "pinterest",
                "date": str(start),
                "title": f"{name} – printable family planner",
                "text": (f"{name}: checklist, dog budget, kids chore chart and a cat & dog intro plan. "
                         "Instant download, print at home."),
                "image": data["images"][0] if data.get("images") else None,
                "isAiGenerated": True,
            },
            {
                "platform": "instagram",
                "date": str(start + timedelta(days=1)),
                "text": ("My son asks for a dog every single morning. So we made it a family project: "
                         "4 weeks, one page at a time, and our cat gets a say too. "
                         f"Link in bio. · {AI_LABEL}\n" + " ".join("#" + t for t in tags)),
                "image": data["images"][1] if len(data.get("images", [])) > 1 else None,
                "isAiGenerated": True,
            },
            {
                "platform": "facebook",
                "date": str(start + timedelta(days=2)),
                "text": (f"Thinking about a dog, but you already have a cat and a busy preschooler? "
                         f"This is the planner I wish I had. {link} · {AI_LABEL}"),
                "isAiGenerated": True,
            },
            {
                "platform": "tiktok",
                "date": str(start + timedelta(days=3)),
                "hook": "POV: your 4-year-old wants a dog and you have a cat 🙃",
                "script": ("1) Show the readiness checklist. 2) The dog budget surprise line. "
                           "3) Kid adds a sticker to the helper chart. 4) The Dog Promise on the fridge. CTA: link in bio."),
                "caption": f"Family dog planner, printable · {AI_LABEL} " + " ".join("#" + t for t in tags[:4]),
                "isAiGenerated": True,
            },
        ],
    }


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    folder = Path(sys.argv[1]).resolve()
    link = ""
    if "--etsy-link" in sys.argv:
        link = sys.argv[sys.argv.index("--etsy-link") + 1]
    data = json.loads((folder / "listing.json").read_text(encoding="utf-8"))
    pack = build(data, link or "[Etsy-link az élesítés után]")
    out = ROOT / "marketing_szovegek" / f"{data['slug']}_social.json"
    out.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Kész:", out.relative_to(ROOT), f"({len(pack['posts'])} poszt, jóváhagyásra vár)")


if __name__ == "__main__":
    main()
