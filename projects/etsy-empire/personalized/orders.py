#!/usr/bin/env python3
"""Névre szóló Etsy-rendelések automatikus teljesítése a Printifyn át (Nóra jóváhagyta: 2026-11-14).

  python3 personalized/orders.py            # száraz futás: mit rendelne (semmit nem küld)
  python3 personalized/orders.py --live     # éles: Printify-rendelés + gyártásba küldés + tracking vissza az Etsy-re

Menet:
 1) Etsy: fizetett, még nem feladott rendelések; csak a "PFY-" kezdetű SKU-jú tételek (personalized/products.json listingjei).
 2) Név a személyre szabás mezőből → render.py ellenőrzi (csak betű, szóköz, kötőjel, aposztróf, pont; max 18 kar.).
    Érvénytelen név → NEM rendel, 'ellenorzes' állapot, Nóra dönt.
 3) Printify: kép feltöltése → rendelés (vevő címével) → send_to_production. Napi max. MAX_PER_DAY rendelés (költségfék).
 4) Később: ha a Printify-rendelésnek van csomagkövetési száma → Etsy receipt tracking (transactions_w jog kell).
Állapot: personalized/state.json (kulcs: receipt:transaction) – ugyanazt a tételt soha nem rendeli kétszer."""
import base64, datetime, json, sys
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from etsy_oauth import get_access_token, CONF, _apikey  # noqa: E402
from render import render, clean_name  # noqa: E402

EA = "https://api.etsy.com/v3/application"
PA = "https://api.printify.com/v1"
PSHOP = 28692848
PH = {"Authorization": "Bearer proxy-injected"}
MAX_PER_DAY = 10
STATE = ROOT / "state.json"
LIVE = "--live" in sys.argv


def eh():
    return {"x-api-key": _apikey(), "Authorization": f"Bearer {get_access_token()}"}


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_state(s):
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=1))


def personalization(tx):
    """A vevő által beírt név. Az Etsy 2026-os személyre szabási rendszere a választ a tranzakcióban adja vissza;
    több lehetséges helyet is megnézünk (variations / personalization mezők)."""
    for v in tx.get("variations", []):
        n = (v.get("formatted_name") or "")
        if "ersonali" in n or "name" in n.lower():
            return v.get("formatted_value") or ""
    for k, v in tx.items():
        if "personaliz" in k and v:
            if isinstance(v, str):
                return v
            if isinstance(v, list) and v and isinstance(v[0], dict):
                return v[0].get("answer") or v[0].get("value") or v[0].get("text") or ""
    return ""


def parse_sku(sku):
    # PFY-<blueprint>-<provider>-<variant>-<design>
    p = (sku or "").split("-", 4)
    if len(p) != 5 or p[0] != "PFY":
        return None
    return {"bp": int(p[1]), "pv": int(p[2]), "vid": int(p[3]), "design": p[4]}


def address(rc):
    first, _, last = (rc.get("name") or "Customer").partition(" ")
    a = {"first_name": first, "last_name": last or ".", "country": rc.get("country_iso"), "region": rc.get("state") or "",
         "address1": rc.get("first_line") or "", "address2": rc.get("second_line") or "", "city": rc.get("city") or "",
         "zip": rc.get("zip") or ""}
    if rc.get("buyer_email"):
        a["email"] = rc["buyer_email"]
    return a


def place(rc, tx, info, name, st, key):
    out = ROOT / "out" / f"{rc['receipt_id']}-{tx['transaction_id']}.png"
    out.parent.mkdir(exist_ok=True)
    render(info["design"], name, out)
    if not LIVE:
        print(f"  [SZÁRAZ] rendelne: {info} név={name!r} → {out}")
        return
    up = requests.post(f"{PA}/uploads/images.json", headers=PH, timeout=120,
                       json={"file_name": out.name, "contents": base64.b64encode(out.read_bytes()).decode()})
    up.raise_for_status()
    src = up.json()["preview_url"]
    mug = info["bp"] == 68
    body = {"external_id": key.replace(":", "-"), "label": f"Etsy {rc['receipt_id']}",
            "line_items": [{"blueprint_id": info["bp"], "print_provider_id": info["pv"], "variant_id": info["vid"],
                            "quantity": tx.get("quantity", 1),
                            "print_areas": {"front": [{"src": src, "scale": 1 if mug else 0.9, "x": 0.5,
                                                       "y": 0.5 if mug else 0.45, "angle": 0}]}}],
            "shipping_method": 1, "send_shipping_notification": False, "address_to": address(rc)}
    r = requests.post(f"{PA}/shops/{PSHOP}/orders.json", headers=PH, json=body, timeout=120)
    if r.status_code >= 300:
        st[key] = {"allapot": "hiba", "uzenet": r.text[:300]}
        print("  HIBA Printify-rendelés:", r.status_code, r.text[:300])
        return
    oid = r.json()["id"]
    s2 = requests.post(f"{PA}/shops/{PSHOP}/orders/{oid}/send_to_production.json", headers=PH, timeout=60)
    st[key] = {"allapot": "gyartasban" if s2.status_code < 300 else "rendelve_nem_gyartasban", "printify_order": oid,
               "nev": name, "datum": datetime.date.today().isoformat(), "receipt": rc["receipt_id"]}
    print(f"  Printify-rendelés #{oid} → {st[key]['allapot']}")


def sync_tracking(st):
    shop = (CONF / "shop_id").read_text().strip()
    for key, v in st.items():
        if v.get("allapot") != "gyartasban":
            continue
        o = requests.get(f"{PA}/shops/{PSHOP}/orders/{v['printify_order']}.json", headers=PH).json()
        sh = (o.get("shipments") or [])
        if not sh:
            continue
        t = sh[0]
        if not LIVE:
            print(f"  [SZÁRAZ] tracking: {key} {t.get('carrier')} {t.get('number')}")
            continue
        r = requests.post(f"{EA}/shops/{shop}/receipts/{v['receipt']}/tracking", headers=eh(), timeout=60,
                          data={"tracking_code": t.get("number"), "carrier_name": t.get("carrier") or "other"})
        if r.status_code < 300:
            v["allapot"] = "feladva"
            print(f"  Etsy tracking OK: {key}")
        else:
            print(f"  Etsy tracking HIBA {r.status_code}: {r.text[:200]} (transactions_w jog kell?)")


def main():
    st = load_state()
    shop = (CONF / "shop_id").read_text().strip()
    rs = requests.get(f"{EA}/shops/{shop}/receipts", headers=eh(), timeout=60,
                      params={"was_paid": "true", "was_shipped": "false", "limit": 50}).json().get("results", [])
    today = datetime.date.today().isoformat()
    done_today = sum(1 for v in st.values() if v.get("datum") == today and v.get("printify_order"))
    for rc in rs:
        for tx in rc.get("transactions", []):
            info = parse_sku(tx.get("sku"))
            if not info:
                continue
            key = f"{rc['receipt_id']}:{tx['transaction_id']}"
            if key in st:
                continue
            raw = personalization(tx)
            print(f"Rendelés {key}: {tx.get('title','')[:50]} | név: {raw!r}")
            try:
                name = clean_name(raw)
            except ValueError as e:
                st[key] = {"allapot": "ellenorzes", "uzenet": str(e), "datum": today, "receipt": rc["receipt_id"]}
                print("  ELLENŐRZÉS KELL (Nóra):", e)
                continue
            if done_today >= MAX_PER_DAY:
                print("  napi keret elfogyott – holnap")
                break
            place(rc, tx, info, name, st, key)
            done_today += 1
    sync_tracking(st)
    if LIVE:
        save_state(st)
    nyitott = {k: v for k, v in st.items() if v.get("allapot") in ("ellenorzes", "hiba", "rendelve_nem_gyartasban")}
    print("Kész.", "Nóra figyelmét kéri:" if nyitott else "", json.dumps(nyitott, ensure_ascii=False) if nyitott else "")


if __name__ == "__main__":
    main()
