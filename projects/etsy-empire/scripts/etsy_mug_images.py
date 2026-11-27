#!/usr/bin/env python3
"""Bögre-listing képeinek cseréje saját mockupokra (CLAUDE.md „Bögre-képek”).
   python3 scripts/etsy_mug_images.py pod/<slug>-mug.json pod/mockups/<a>.jpg pod/mockups/<b>.jpg pod/mockups/<c>.jpg
Az Etsy-listing ID a Printify-termék external.id mezőjéből jön (publikálás után pár perc). 1. kép rank=1 overwrite."""
import json, sys
from pathlib import Path
import requests
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from etsy_oauth import get_access_token, CONF, _apikey  # noqa: E402

cfg = Path(sys.argv[1]); d = json.loads(cfg.read_text()); imgs = sys.argv[2:]
p = requests.get(f"https://api.printify.com/v1/shops/28692848/products/{d['printify_product_id']}.json",
                 headers={"Authorization": "Bearer proxy-injected"}, timeout=60).json()
lid = (p.get("external") or {}).get("id")
if not lid:
    sys.exit(f"{cfg.name}: még nincs Etsy-listing (Printify external üres) – később futtasd újra")
shop = (CONF / "shop_id").read_text().strip()
h = {"x-api-key": _apikey(), "Authorization": f"Bearer {get_access_token()}"}
for rank, img in enumerate(imgs, start=1):
    with open(img, "rb") as fh:
        data = {"rank": rank, "overwrite": "true"}
        r = requests.post(f"https://api.etsy.com/v3/application/shops/{shop}/listings/{lid}/images", headers=h,
                          files={"image": (Path(img).name, fh, "image/jpeg")}, data=data, timeout=120)
        print(rank, r.status_code, r.text[:120] if r.status_code >= 300 else "")
d["etsy_listing_id"] = str(lid); d["etsy_custom_images"] = imgs
d["megjegyzes_kepek"] = "Printify csak 1 (üres közepű) mockupot ad a kétoldalas bögréhez -> saját mockupok az Etsy-n. Újrapublikálásnál images:false!"
cfg.write_text(json.dumps(d, ensure_ascii=False, indent=2))
print("kész:", lid)
