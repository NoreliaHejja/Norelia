#!/usr/bin/env python3
"""
Etsy OAuth2 (PKCE) – egyszeri bolt-összekötés + automatikus token-frissítés.

1) python3 etsy_oauth.py link      → kiír egy Etsy-linket; Nóra megnyitja, engedélyezi,
                                      a böngésző átirányít a REDIRECT címre (?code=...).
2) python3 etsy_oauth.py code <teljes átirányított URL vagy code>
                                    → beváltja a kódot; a tokeneket a TOKEN_FILE-ba menti
                                      (a repón KÍVÜL, soha nem kerül gitbe).
3) A többi script a get_access_token()-t hívja: lejárt token esetén magától frissít.

Az x-api-key fejlécet (keystring:shared_secret) a hálózati proxy teszi hozzá – a kódban
csak helyőrző szerepel. A keystring kell a kérésekben client_id-ként; ezt a KEYSTRING
fájlból olvassuk (nem titok, de a repón kívül tartjuk).
"""
import base64, hashlib, json, os, secrets, sys, time, urllib.parse
from pathlib import Path

CONF = Path.home() / ".config" / "etsy"
TOKEN_FILE = CONF / "token.json"
PKCE_FILE = CONF / "pkce.json"
KEYSTRING_FILE = CONF / "keystring"
REDIRECT = "https://reinigung-kalkulieren.de/etsy-callback"
SCOPES = "listings_w listings_r listings_d shops_r transactions_r"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"
HDR = {"x-api-key": "proxy-injected"}


def _keystring():
    return KEYSTRING_FILE.read_text().strip()


def link():
    CONF.mkdir(parents=True, exist_ok=True)
    verifier = secrets.token_urlsafe(64)[:96]
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
    state = secrets.token_urlsafe(16)
    PKCE_FILE.write_text(json.dumps({"verifier": verifier, "state": state}))
    os.chmod(PKCE_FILE, 0o600)
    q = urllib.parse.urlencode({"response_type": "code", "redirect_uri": REDIRECT, "scope": SCOPES,
                                "client_id": _keystring(), "state": state, "code_challenge": challenge,
                                "code_challenge_method": "S256"})
    print("https://www.etsy.com/oauth/connect?" + q)


def _save(tok):
    tok["expires_at"] = int(time.time()) + int(tok.get("expires_in", 3600)) - 60
    TOKEN_FILE.write_text(json.dumps(tok))
    os.chmod(TOKEN_FILE, 0o600)


def code(arg):
    import requests
    p = json.loads(PKCE_FILE.read_text())
    if arg.startswith("http"):
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(arg).query)
        if qs.get("state", [""])[0] != p["state"]:
            sys.exit("Hibás state – kezdd újra a link lépéssel.")
        arg = qs["code"][0]
    r = requests.post(TOKEN_URL, headers=HDR, data={"grant_type": "authorization_code", "client_id": _keystring(),
                      "redirect_uri": REDIRECT, "code": arg, "code_verifier": p["verifier"]}, timeout=30)
    r.raise_for_status()
    _save(r.json())
    PKCE_FILE.unlink(missing_ok=True)
    print("Kész: bolt összekötve, token elmentve.")


def get_access_token():
    import requests
    tok = json.loads(TOKEN_FILE.read_text())
    if time.time() < tok.get("expires_at", 0):
        return tok["access_token"]
    r = requests.post(TOKEN_URL, headers=HDR, data={"grant_type": "refresh_token", "client_id": _keystring(),
                      "refresh_token": tok["refresh_token"]}, timeout=30)
    r.raise_for_status()
    _save(r.json())
    return json.loads(TOKEN_FILE.read_text())["access_token"]


def user_shop():
    """A token első része a user_id; ebből lekérjük a bolt azonosítóját."""
    import requests
    t = get_access_token()
    uid = t.split(".")[0]
    r = requests.get(f"https://openapi.etsy.com/v3/application/users/{uid}/shops",
                     headers={**HDR, "Authorization": f"Bearer {t}"}, timeout=30)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "link":
        link()
    elif cmd == "code":
        code(sys.argv[2])
    elif cmd == "shop":
        print(json.dumps(user_shop(), indent=2)[:800])
    else:
        print(__doc__)
