#!/usr/bin/env python3
"""Névre szóló Etsy-listingek létrehozása (közvetlenül az Etsy API-val, NEM Printify-publikálással,
hogy a rendelést a personalized/orders.py a beírt névvel adja le).  python3 personalized/create_listings.py"""
import json, sys
from pathlib import Path
import requests
from PIL import Image

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from etsy_oauth import get_access_token, CONF, _apikey  # noqa: E402

A = "https://api.etsy.com/v3/application"
PARTNER = 5765857          # ugyanaz a Printify-gyártópartner, amit a Printify-listingek használnak
RETURN_POLICY = 1509455453498
PROD = json.loads((ROOT / "products.json").read_text())


def h():
    return {"x-api-key": _apikey(), "Authorization": f"Bearer {get_access_token()}"}


def main():
    shop = (CONF / "shop_id").read_text().strip()
    for key, p in PROD.items():
        if p.get("etsy_listing_id"):
            print(key, "már létezik:", p["etsy_listing_id"]); continue
        prices = [v["price"] for v in p["variants"]]
        data = {"quantity": 999, "title": p["title"], "description": p["description"], "price": min(prices),
                "who_made": "someone_else", "when_made": "made_to_order", "taxonomy_id": p["taxonomy_id"],
                "shipping_profile_id": p["shipping_profile_id"], "return_policy_id": RETURN_POLICY,
                "production_partner_ids": [PARTNER], "type": "physical", "tags": ",".join(p["tags"]),
                "is_personalizable": "true", "personalization_is_required": "true",
                "personalization_char_count_max": 18, "personalization_instructions": p["personalization_instructions"],
                "readiness_state_id": p["readiness_state_id"]}
        r = requests.post(f"{A}/shops/{shop}/listings", headers=h(), data=data, timeout=60)
        if r.status_code >= 300:
            sys.exit(f"{key} HIBA {r.status_code}: {r.text[:500]}")
        lid = r.json()["listing_id"]; print(key, "draft:", lid)
        # változatok + SKU (PFY-<bp>-<pv>-<variant>-<design>) → orders.py ebből tudja, mit rendeljen
        products = []
        for v in p["variants"]:
            pr = {"sku": f"PFY-{v['bp']}-{v['pv']}-{v['vid']}-{p.get('sku_code', p['design'])}",
                  "offerings": [{"price": v["price"], "quantity": 999, "is_enabled": True, "readiness_state_id": p["readiness_state_id"]}],
                  "property_values": []}
            if len(p["variants"]) > 1:
                pr["property_values"] = [{"property_id": 513, "property_name": "Size", "values": [v["label"]], "value_ids": []}]
            products.append(pr)
        inv = {"products": products, "price_on_property": [513] if len(products) > 1 else [],
               "quantity_on_property": [], "sku_on_property": [513] if len(products) > 1 else [], "readiness_state_on_property": []}
        r = requests.put(f"{A}/listings/{lid}/inventory", headers={**h(), "Content-Type": "application/json"}, data=json.dumps(inv), timeout=60)
        if r.status_code >= 300:
            sys.exit(f"{key} inventory HIBA {r.status_code}: {r.text[:500]}")
        # személyre szabás: az új (2026-os) végponttal – a régi is_personalizable mezőt az Etsy figyelmen kívül hagyja
        r = requests.post(f"{A}/shops/{shop}/listings/{lid}/personalization", headers={**h(), "Content-Type": "application/json"},
                          data=json.dumps({"personalization_questions": [{"question_type": "text_input", "question_text": p.get("question", "Name to print"),
                                           "instructions": p["personalization_instructions"], "required": True, "max_allowed_characters": 18}]}), timeout=60)
        print(key, "névmező:", r.status_code)
        for rank, img in enumerate(p["images"], start=1):
            jpg = ROOT / "mockups" / (Path(img).stem + ".jpg")
            Image.open(ROOT / img).convert("RGB").save(jpg, quality=90)
            with open(jpg, "rb") as fh:
                r = requests.post(f"{A}/shops/{shop}/listings/{lid}/images", headers=h(),
                                  files={"image": (jpg.name, fh, "image/jpeg")}, data={"rank": rank}, timeout=120)
                r.raise_for_status()
        r = requests.patch(f"{A}/shops/{shop}/listings/{lid}", headers=h(), data={"state": "active"}, timeout=60)
        print(key, "aktiválás:", r.status_code, r.text[:200] if r.status_code >= 300 else "")
        p["etsy_listing_id"] = lid; p["etsy_url"] = f"https://www.etsy.com/listing/{lid}"
        (ROOT / "products.json").write_text(json.dumps(PROD, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
