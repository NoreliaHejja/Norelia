#!/usr/bin/env python3
"""Etsy bolt-pillanatkép: listingenkénti megtekintés + kedvelés, kor szerinti bontás, napi mentés.
   python3 scripts/etsy_stats.py            → kiírás + bolt/stats/ÉÉÉÉ-HH-NN.json (napi delta számolható)"""
import sys, json, datetime, html, statistics
from pathlib import Path
import requests
ROOT = Path(__file__).resolve().parent.parent; sys.path.insert(0, str(ROOT))
from etsy_oauth import get_access_token, CONF, _apikey  # noqa: E402
shop = (CONF / "shop_id").read_text().strip(); h = {"x-api-key": _apikey(), "Authorization": f"Bearer {get_access_token()}"}
rows, off = [], 0
while True:
    r = requests.get(f"https://api.etsy.com/v3/application/shops/{shop}/listings", headers=h, params={"state": "active", "limit": 100, "offset": off}).json()["results"]
    rows += r
    if len(r) < 100: break
    off += 100
now = datetime.datetime.now().timestamp()
data = [{"id": x["listing_id"], "title": html.unescape(x["title"])[:80], "views": x.get("views", 0), "favs": x.get("num_favorers", 0),
         "age_days": round((now - x["original_creation_timestamp"]) / 86400, 1), "type": x["listing_type"], "price": x["price"]["amount"] / x["price"]["divisor"]} for x in rows]
out = ROOT / "bolt" / "stats"; out.mkdir(parents=True, exist_ok=True)
today = datetime.date.today().isoformat(); (out / f"{today}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
prev = sorted(p for p in out.glob("*.json") if p.stem < today)
pv = {d["id"]: d["views"] for d in json.loads(prev[-1].read_text())} if prev else {}
print(f"aktív listing: {len(data)} · össz megtekintés: {sum(d['views'] for d in data)} · kedvelés: {sum(d['favs'] for d in data)}")
if pv: print(f"új megtekintés az előző pillanatkép óta ({prev[-1].stem}): {sum(d['views'] - pv.get(d['id'], 0) for d in data)}")
for lo, hi in [(0, 3), (3, 7), (7, 30), (30, 9999)]:
    g = [d for d in data if lo <= d["age_days"] < hi]
    if g: print(f"  kor {lo}-{hi} nap: {len(g)} db · átlag megtekintés {statistics.mean(d['views'] for d in g):.1f} · 0 megtekintés: {sum(1 for d in g if d['views'] == 0)}")
print("TOP 10:"); [print(f"  {d['views']:>3} 👁 {d['favs']} ♥ {d['title'][:60]}") for d in sorted(data, key=lambda d: -d["views"])[:10]]
