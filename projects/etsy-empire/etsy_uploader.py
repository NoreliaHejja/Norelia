#!/usr/bin/env python3
"""
Etsy uploader – AureliaVenn / etsy-empire

Egy termékmappát (termekek/<slug>/listing.json + PDF + képek) Etsy-n
**piszkozatként** (draft) tölt fel az Etsy Open API v3-mal; --aktival esetén
utána élesíti is (0,20 $ díj). Nóra döntése (2026-11-10): Etsy-n automatikus élesítés.

Használat
  python3 etsy_uploader.py termekek/ready-for-a-dog-kit            # száraz futás (alapértelmezés)
  python3 etsy_uploader.py termekek/ready-for-a-dog-kit --feltolt  # valódi piszkozat-feltöltés
  python3 etsy_uploader.py termekek/ready-for-a-dog-kit --feltolt --aktival  # feltöltés + élesítés (0,20 $)

Hitelesítés: az x-api-key-t a hálózati proxy adja (környezet → Network secrets,
openapi.etsy.com); az OAuth tokent az etsy_oauth.py kezeli (~/.config/etsy/, repón kívül);
a bolt azonosítója: ~/.config/etsy/shop_id.
"""
import json
import os
import sys
from pathlib import Path

API = "https://api.etsy.com/v3/application"
REQUIRED = ["title", "description", "price", "quantity", "who_made", "when_made", "taxonomy_id"]


def load_listing(folder: Path) -> dict:
    data = json.loads((folder / "listing.json").read_text(encoding="utf-8"))
    return data


def check(folder: Path, data: dict) -> list:
    """Visszaadja a hibák listáját. Üres lista = feltölthető."""
    e = data.get("etsy", {})
    errors = []
    for k in REQUIRED:
        if e.get(k) in (None, "", []):
            errors.append(f"hiányzik: etsy.{k}")
    if len(e.get("title", "")) > 140:
        errors.append("cím > 140 karakter")
    tags = e.get("tags", [])
    if len(tags) > 13:
        errors.append("több mint 13 tag")
    for t in tags:
        if len(t) > 20:
            errors.append(f"tag > 20 karakter: {t}")
    if "AI" not in e.get("description", ""):
        errors.append("hiányzik az AI-közlés a leírásból (Etsy creativity standards)")
    for f in data.get("files", []):
        if not (folder / f).exists():
            errors.append(f"nincs meg a fájl: {f}")
    for img in data.get("images", []):
        if not (folder / img).exists():
            errors.append(f"nincs meg a kép: {img}")
    if data.get("status") not in ("kesz", "jovahagyva"):
        errors.append(f"status = {data.get('status')} – csak 'kesz' vagy 'jovahagyva' állapotú termék tölthető fel")
    return errors


def upload(folder: Path, data: dict) -> str:
    import requests
    from etsy_oauth import get_access_token, CONF, _apikey

    shop = (CONF / "shop_id").read_text().strip()
    h = {"x-api-key": _apikey(), "Authorization": f"Bearer {get_access_token()}"}
    e = data["etsy"]

    listing_id = data.get("etsy_listing_id")  # félbeszakadt feltöltés folytatása
    if not listing_id:
        payload = {
            "quantity": e["quantity"], "title": e["title"], "description": e["description"], "price": e["price"],
            "who_made": e["who_made"], "when_made": e["when_made"], "taxonomy_id": e["taxonomy_id"],
            "is_supply": e.get("is_supply", False), "type": e.get("type", "download"), "tags": ",".join(e.get("tags", [])),
        }
        r = requests.post(f"{API}/shops/{shop}/listings", headers=h, data=payload, timeout=60)
        r.raise_for_status()
        listing_id = str(r.json()["listing_id"])
        data["etsy_listing_id"] = listing_id
        (folder / "listing.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        for rank, img in enumerate(data.get("images", []), start=1):
            with open(folder / img, "rb") as fh:
                r = requests.post(f"{API}/shops/{shop}/listings/{listing_id}/images", headers=h,
                                  files={"image": (Path(img).name, fh, "image/jpeg")}, data={"rank": rank}, timeout=120)
                r.raise_for_status()

        nice = e["title"].split(",")[0].replace("?", "").replace("&", "and").strip().replace(" ", "-")
        for f in data.get("files", []):
            fname = f"{nice}-A4.pdf" if f.endswith("-A4.pdf") else f"{nice}-US-Letter.pdf"
            with open(folder / f, "rb") as fh:
                r = requests.post(f"{API}/shops/{shop}/listings/{listing_id}/files", headers=h,
                                  files={"file": (fname, fh, "application/pdf")}, data={"name": fname}, timeout=120)
                r.raise_for_status()

    return str(listing_id)


def activate(listing_id: str) -> None:
    import requests
    from etsy_oauth import get_access_token, CONF, _apikey
    h = {"x-api-key": _apikey(), "Authorization": f"Bearer {get_access_token()}"}
    shop = (CONF / "shop_id").read_text().strip()
    r = requests.patch(f"{API}/shops/{shop}/listings/{listing_id}", headers=h, data={"state": "active"}, timeout=60)
    r.raise_for_status()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    folder = Path(sys.argv[1]).resolve()
    live = "--feltolt" in sys.argv
    data = load_listing(folder)
    errors = check(folder, data)

    print(f"Termék: {data['slug']}")
    print(f"Cím ({len(data['etsy']['title'])} kar.): {data['etsy']['title']}")
    print(f"Ár: {data['etsy']['price']} {data['etsy'].get('currency', '')} · tagek: {len(data['etsy']['tags'])}")
    if errors:
        print("NEM tölthető fel:")
        for x in errors:
            print("  –", x)
        sys.exit(2 if live else 0)
    if not live:
        print("Száraz futás: minden rendben. Valódi feltöltés: --feltolt")
        return
    listing_id = upload(folder, data)
    data["status"] = "etsy_piszkozat"
    data["etsy_listing_id"] = listing_id
    if "--aktival" in sys.argv:
        activate(listing_id)
        data["status"] = "etsy_aktiv"
        data["etsy_url"] = f"https://www.etsy.com/listing/{listing_id}"
    (folder / "listing.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Kész: Etsy #{listing_id} – {data['status']}")


if __name__ == "__main__":
    main()
