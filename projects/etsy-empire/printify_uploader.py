#!/usr/bin/env python3
"""
Printify POD-termékek – AureliaVenn (Printify bolt id: 28692848).

  python3 printify_uploader.py pod/<slug>.json            # létrehozás Printify-ban (piszkozat)
  python3 printify_uploader.py pod/<slug>.json --publish  # + élesítés az összekötött Etsy-boltba

Hitelesítés: az API-tokent a hálózati proxy teszi a kérésbe (api.printify.com network secret);
a kódban csak helyőrző van. A pod/<slug>.json-ba kerül vissza a printify_product_id.
Szabályok: nincs „Embroidered” (csak „embroidery-look”), AI-közlés a leírásban, nincs hamis akció.
"""
import base64, json, sys
from pathlib import Path
import requests

API = "https://api.printify.com/v1"
SHOP = 28692848
H = {"Authorization": "Bearer proxy-injected", "Content-Type": "application/json"}


def upload_image(path: Path) -> str:
    r = requests.post(f"{API}/uploads/images.json", headers=H, timeout=180,
                      json={"file_name": path.name, "contents": base64.b64encode(path.read_bytes()).decode()})
    r.raise_for_status()
    return r.json()["id"]


def check(d):
    err = []
    txt = (d["title"] + d["description"] + " ".join(d["tags"])).lower()
    if "embroidered" in txt:
        err.append("'embroidered' tilos")
    if "AI" not in d["description"]:
        err.append("hiányzik az AI-közlés")
    if len(d["tags"]) > 13 or any(len(t) > 20 for t in d["tags"]):
        err.append("tag-hiba (max 13, max 20 kar.)")
    if len(d["title"]) > 140:
        err.append("cím > 140")
    return err


def create(cfg_path: Path, publish=False):
    d = json.loads(cfg_path.read_text())
    e = check(d)
    if e:
        sys.exit("HIBA: " + "; ".join(e))
    if not d.get("printify_product_id"):
        img_id = d.get("printify_image_id") or upload_image(cfg_path.parent / d["design"])
        d["printify_image_id"] = img_id
        variants = [{"id": v, "price": d["price_cents"].get(str(v), d["price_cents"]["default"]), "is_enabled": True} for v in d["variant_ids"]]
        body = {
            "title": d["title"], "description": d["description"], "tags": d["tags"],
            "blueprint_id": d["blueprint_id"], "print_provider_id": d["print_provider_id"], "variants": variants,
            "print_areas": [{"variant_ids": d["variant_ids"], "placeholders": [
                {"position": d.get("position", "front"), "images": (
                    # bögre (blueprint 68): a minta MINDKÉT oldalra kerül – jobb- és balkezesnek is szembe néz (Nóra, 2026-11-12)
                    [{"id": img_id, "x": x, "y": d.get("y", 0.5), "scale": d.get("scale", 0.33), "angle": 0} for x in (0.25, 0.75)]
                    if d["blueprint_id"] == 68 else
                    [{"id": img_id, "x": d.get("x", 0.5), "y": d.get("y", 0.45), "scale": d.get("scale", 0.85), "angle": 0}])}]}],
        }
        r = requests.post(f"{API}/shops/{SHOP}/products.json", headers=H, json=body, timeout=120)
        if r.status_code >= 300:
            sys.exit(f"Printify hiba {r.status_code}: {r.text[:600]}")
        d["printify_product_id"] = r.json()["id"]
        d["mockups"] = [i["src"] for i in r.json().get("images", [])[:6]]
        cfg_path.write_text(json.dumps(d, ensure_ascii=False, indent=2))
        print("Létrehozva:", d["printify_product_id"])
    if publish:
        r = requests.post(f"{API}/shops/{SHOP}/products/{d['printify_product_id']}/publish.json", headers=H, timeout=60,
                          json={"title": True, "description": True, "images": True, "variants": True, "tags": True,
                                "keyFeatures": True, "shipping_template": True})
        print("Publish:", r.status_code, r.text[:300])
        if r.status_code < 300:
            d["status"] = "publikalas_elinditva"
            cfg_path.write_text(json.dumps(d, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    create(Path(sys.argv[1]), "--publish" in sys.argv)
