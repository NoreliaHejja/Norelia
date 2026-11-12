import logging

from szte.log import RedactingFilter, redact
from szte.scraper.guard import is_allowed
from szte.scraper.spaces import Space, dedupe, extract_from_json, extract_from_links, matches_term, semester_of

BASE = "https://unics.szte.hu/"


def test_redact_known_secret_and_patterns():
    s = redact('login ok pass=Titok123!X cookie: .AspNetCore.Cookies=abc; {"password": "x1"} Bearer abc.def', ["Titok123!X"])
    assert "Titok123!X" not in s and "abc.def" not in s and '"x1"' not in s
    assert "abc;" not in s


def test_filter_on_logger(caplog):
    lg = logging.getLogger("t")
    lg.addFilter(RedactingFilter(["SzuperTitok9"]))
    with caplog.at_level(logging.INFO):
        lg.info("jelszó: %s", "SzuperTitok9")
    assert "SzuperTitok9" not in caplog.text


def test_guard_readonly():
    assert is_allowed("GET", BASE + "api/scene/list", BASE)[0]
    assert is_allowed("POST", BASE + "api/scene/list", BASE)[0]
    assert not is_allowed("POST", BASE + "api/assignment/upload", BASE)[0]
    assert not is_allowed("POST", BASE + "api/forum/createPost", BASE)[0]
    assert not is_allowed("POST", BASE + "api/doc/getAndSave", BASE)[0]  # tiltó szó nyer
    assert not is_allowed("PUT", BASE + "api/scene/get", BASE)[0]
    assert not is_allowed("POST", BASE + "api/public/login", BASE)[0]
    assert is_allowed("POST", BASE + "api/public/login", BASE, login_mode=True)[0]
    assert not is_allowed("POST", "https://evil.example/x", BASE)[0]
    assert is_allowed("POST", "https://www.google.com/recaptcha/api2/reload", BASE, login_mode=True)[0]


def test_term_matching():
    for name in ["Agrárinformatika 2026/27/1", "Marketing (2026/2027 ősz)", "Statisztika 2026-27-2", "X 26/27 tavasz"]:
        assert matches_term(Space("1", name), "2026/27"), name
    for name in ["Agrárinformatika 2025/26/2", "2026/28", "Kurzus 12026/270"]:
        assert not matches_term(Space("1", name), "2026/27"), name


def test_semester():
    assert semester_of(Space("1", "Agrár 2026/27/1")) == "1"
    assert semester_of(Space("1", "Agrár", term="2026/27 2. félév")) == "2"
    assert semester_of(Space("1", "Agrár (tavasz)")) == "2"


def test_extract_from_json_and_links():
    payload = {"data": {"scenes": [{"id": 11, "name": "Digitális agrár 2026/27/1", "semester": "2026/27/1"},
                                   {"id": 12, "name": "Régi 2025/26/2"}]}, "user": {"id": 5, "name": "Nóra"}}
    sp = extract_from_json(payload, "/api/home/menu")
    names = [s.name for s in sp]
    assert "Digitális agrár 2026/27/1" in names and "Nóra" not in names
    assert sp[0].term == "2026/27/1"
    links = [{"href": "/Scene/12345", "text": "Üzleti stat"}, {"href": "https://x.com/scene/1", "text": "Külső"},
             {"href": "/Profile", "text": "Profil"}]
    ls = extract_from_links(links, BASE)
    assert [s.name for s in ls] == ["Üzleti stat"] and ls[0].uid == "12345"
    merged = dedupe([Space("12345", "Üzleti stat"), Space("12345", "Üzleti stat", url=BASE + "Scene/12345")])
    assert len(merged) == 1 and merged[0].url
