"""Csak-olvasás őr: a böngészőből a CooSpace felé menő írási kéréseket blokkolja.

Az agent soha nem tölt fel, nem küld be, nem ír fórumba. Ezt nem csak "nem kattintunk"
alapon, hanem hálózati szinten is kikényszerítjük.
"""
from __future__ import annotations

import re
from urllib.parse import urlparse

# Írást jelző szavak az útvonalban: ha bármelyik szerepel, a kérés tiltott.
WRITE_WORDS = re.compile(
    r"(?i)(upload|submit|send|save|delete|remove|create|update|insert|edit|modify|post(?!s\b)|"
    r"reply|comment|answer|vote|rate|accept|reject|enrol|enroll|register|subscribe|"
    r"unsubscribe|move|copy|rename|share|invite|setstate|setstatus|markread|logout|resetpass)"
)
# Olvasást jelző szavak: POST-ot csak ilyen útvonalra engedünk (sok SPA POST-tal listáz).
READ_WORDS = re.compile(r"(?i)(list|get|load|search|query|find|tree|info|count|view|read|fetch|menu|dummy)")


def is_allowed(method: str, url: str, base_url: str, login_mode: bool = False) -> tuple[bool, str]:
    """Visszaadja: (engedett-e, indoklás)."""
    method = method.upper()
    host = urlparse(url).netloc
    base_host = urlparse(base_url).netloc
    if host != base_host:
        # Külső kérések (pl. reCAPTCHA, CDN): csak GET/HEAD/OPTIONS; bejelentkezéskor a
        # reCAPTCHA POST-ot is engedjük, mert azt Nóra maga oldja meg.
        if method in ("GET", "HEAD", "OPTIONS"):
            return True, "külső olvasás"
        if login_mode and "recaptcha" in url:
            return True, "reCAPTCHA (kézi belépés)"
        return False, "külső írás tiltva"
    if method in ("GET", "HEAD", "OPTIONS"):
        return True, "olvasás"
    path = urlparse(url).path
    if login_mode and re.search(r"(?i)api/public/(login|challenge|emailchallenge|dummy)", path):
        return True, "belépés"
    if method in ("PUT", "PATCH", "DELETE"):
        return False, f"{method} tiltva"
    if WRITE_WORDS.search(path):
        return False, "írási útvonal tiltva"
    if READ_WORDS.search(path):
        return True, "olvasó POST"
    return False, "ismeretlen POST tiltva"
