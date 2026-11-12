"""Színterek listázása és szűrése tanévre.

Az új CooSpace (unics.szte.hu) React-alkalmazás, ami JSON API-ból tölti az adatokat.
Ezért két forrásból dolgozunk: (1) a böngésző által letöltött JSON válaszok,
(2) tartalék: a menü/oldal linkjei. A nyers anyagot a data/debug/ mappába mentjük,
hogy a felület változásakor gyorsan javítható legyen.
"""
from __future__ import annotations

import hashlib
import json
import logging
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Iterable
from urllib.parse import urljoin, urlparse

from szte.scraper.browser import LayoutChanged, Session, SessionExpired

log = logging.getLogger("szte")

NAME_KEYS = ("name", "title", "displayName", "label", "text", "Name", "Title", "DisplayName")
ID_KEYS = ("id", "Id", "ID", "sceneId", "SceneId", "spaceId", "SpaceId", "guid", "uid")
TERM_KEYS = re.compile(r"(?i)(term|semester|period|felev|félév|tanev|tanév|year|season)")
SPACE_HINT = re.compile(r"(?i)(scene|space|szinter|színtér|course|kurzus|subject|targy|tárgy)")


@dataclass
class Space:
    uid: str
    name: str
    url: str = ""
    term: str = ""
    source: str = ""
    raw: dict = field(default_factory=dict, repr=False)

    def to_row(self) -> dict:
        d = asdict(self)
        d["raw"] = json.dumps(self.raw, ensure_ascii=False)[:20000]
        return d


def term_patterns(term: str) -> re.Pattern:
    """'2026/27' -> 2026/27, 2026/2027, 2026-27, 2026-2027, 2026_27, 26/27 stb."""
    m = re.match(r"(\d{4})\D+(\d{2,4})", term)
    if not m:
        return re.compile(re.escape(term))
    y1, y2 = m.group(1), m.group(2)[-2:]
    short1 = y1[-2:]
    return re.compile(rf"(?:{y1}|(?<!\d){short1})\s*[/\-_.]\s*(?:20)?{y2}(?!\d)")


def matches_term(space: Space, term: str) -> bool:
    pat = term_patterns(term)
    hay = " ".join([space.name, space.term, json.dumps(space.raw, ensure_ascii=False)])
    return bool(pat.search(hay))


def semester_of(space: Space) -> str:
    hay = f"{space.term} {space.name}"
    m = re.search(r"\d{2,4}\s*[/\-]\s*\d{2,4}\s*[/\-_ ]\s*([12])(?!\d)", hay)
    if m:
        return m.group(1)
    if re.search(r"(?i)\b(1\.|I\.)\s*f[eé]l[eé]v|ősz|osz|autumn|fall", hay):
        return "1"
    if re.search(r"(?i)\b(2\.|II\.)\s*f[eé]l[eé]v|tavasz|spring", hay):
        return "2"
    return "?"


def _first(d: dict, keys: Iterable[str]) -> Any:
    for k in keys:
        if k in d and d[k] not in (None, ""):
            return d[k]
    return None


def _term_value(d: dict) -> str:
    vals = [str(v) for k, v in d.items() if TERM_KEYS.search(k) and isinstance(v, (str, int))]
    return " ".join(vals)


def extract_from_json(payload: Any, api_path: str = "") -> list[Space]:
    """Végigjárja a JSON-t, és színtérnek látszó objektumokat keres."""
    out: list[Space] = []
    path_hint = bool(SPACE_HINT.search(api_path))

    def walk(node: Any, parent_key: str = "") -> None:
        if isinstance(node, list):
            for x in node:
                walk(x, parent_key)
        elif isinstance(node, dict):
            name, uid = _first(node, NAME_KEYS), _first(node, ID_KEYS)
            type_txt = " ".join(str(node.get(k, "")) for k in ("type", "Type", "kind", "objectType", "entityType"))
            hinted = path_hint or SPACE_HINT.search(parent_key) or SPACE_HINT.search(type_txt)
            if isinstance(name, str) and uid is not None and hinted:
                url = _first(node, ("url", "Url", "link", "href", "path")) or ""
                out.append(
                    Space(uid=str(uid), name=name.strip(), url=str(url), term=_term_value(node),
                          source=f"api:{api_path}", raw=node)
                )
            for k, v in node.items():
                if isinstance(v, (dict, list)):
                    walk(v, k)

    walk(payload)
    return out


def extract_from_links(links: list[dict], base_url: str) -> list[Space]:
    out = []
    for a in links:
        href, text = a.get("href") or "", (a.get("text") or "").strip()
        if not text or not SPACE_HINT.search(href):
            continue
        full = urljoin(base_url, href)
        if urlparse(full).netloc != urlparse(base_url).netloc:
            continue
        m = re.search(r"(\d{3,}|[0-9a-f]{8}-[0-9a-f-]{27})", href)
        uid = m.group(1) if m else hashlib.sha1(full.encode()).hexdigest()[:12]
        out.append(Space(uid=uid, name=text, url=full, term=a.get("title") or "", source="dom", raw=a))
    return out


def dedupe(spaces: list[Space]) -> list[Space]:
    best: dict[str, Space] = {}
    for sp in spaces:
        key = sp.uid
        cur = best.get(key)
        if cur is None or (not cur.url and sp.url) or (not cur.term and sp.term):
            if cur is not None:
                sp.url = sp.url or cur.url
                sp.term = sp.term or cur.term
            best[key] = sp
    return list(best.values())


def collect_spaces(sess: Session) -> tuple[list[Space], dict]:
    """Bejárja a kezdőoldalt (és ha van, a színterek listáját), visszaadja a színtereket + debug dumpot."""
    captured: list[tuple[str, Any]] = []
    base_host = urlparse(sess.s.base_url).netloc

    def on_response(resp):
        try:
            u = urlparse(resp.url)
            if u.netloc != base_host or "/api/" not in u.path:
                return
            if "json" not in (resp.headers.get("content-type") or ""):
                return
            captured.append((u.path, resp.json()))
        except Exception:
            pass

    sess.page.on("response", on_response)
    sess.goto(sess.s.base_url)
    if sess.is_login_page():
        raise SessionExpired("A CooSpace session lejárt. Futtasd: python -m szte login")

    links = sess.page.eval_on_selector_all(
        "a[href]", "els => els.map(e => ({href: e.getAttribute('href'), text: e.innerText, title: e.title}))"
    )
    # Ha van külön "Színtereim" / "összes színtér" oldal, azt is megnyitjuk.
    for a in links:
        if re.search(r"(?i)(színtere|szinter|scenes|spaces|összes)", (a.get("text") or "") + (a.get("href") or "")):
            target = urljoin(sess.s.base_url, a["href"])
            if urlparse(target).netloc == base_host and target.rstrip("/") != sess.s.base_url.rstrip("/"):
                sess.goto(target)
                links += sess.page.eval_on_selector_all(
                    "a[href]", "els => els.map(e => ({href: e.getAttribute('href'), text: e.innerText, title: e.title}))"
                )
                break

    spaces: list[Space] = []
    for path, payload in captured:
        spaces += extract_from_json(payload, path)
    spaces += extract_from_links(links, sess.s.base_url)
    spaces = dedupe(spaces)

    dump = {
        "url": sess.page.url,
        "api_calls": [p for p, _ in captured],
        "api_payloads": {p: payload for p, payload in captured},
        "links": links,
        "blocked": sess.blocked,
        "menu_text": sess.page.inner_text("body")[:5000],
    }
    if not spaces:
        err = LayoutChanged(
            "Nem találtam egyetlen színteret sem – valószínűleg megváltozott a CooSpace felülete. "
            "A nyers adat: data/debug/spaces_dump.json"
        )
        err.dump = dump
        raise err
    return spaces, dump
