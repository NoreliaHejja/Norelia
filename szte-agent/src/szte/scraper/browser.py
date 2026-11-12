"""Böngésző indítása a mentett sessionnel, csak-olvasás őrrel és kíméletes tempóval."""
from __future__ import annotations

import logging
import os
import time
from contextlib import contextmanager

from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from szte.config import Settings
from szte.scraper.guard import is_allowed

log = logging.getLogger("szte")

MIN_INTERVAL = 1.0  # mp – max. 1 navigáció másodpercenként


class SessionExpired(RuntimeError):
    """A mentett session lejárt: Nórának újra be kell lépnie (`python -m szte login`)."""


class LayoutChanged(RuntimeError):
    """A CooSpace felülete megváltozott – nem találjuk, amit kerestünk."""


def _launch(p: Playwright, headless: bool) -> Browser:
    # Alapból Nóra saját, telepített Chrome-ját használjuk (normál böngésző, látható ablak).
    channel = os.environ.get("BROWSER_CHANNEL", "chrome")
    try:
        return p.chromium.launch(channel=channel or None, headless=headless)
    except Exception:
        log.info("Telepített Chrome nem található, a Playwright Chromiumot használom.")
        return p.chromium.launch(headless=headless)


class Session:
    def __init__(self, settings: Settings, page: Page, context: BrowserContext):
        self.s = settings
        self.page = page
        self.context = context
        self.blocked: list[str] = []
        self._last_nav = 0.0

    def goto(self, url: str, wait: str = "networkidle") -> None:
        dt = time.monotonic() - self._last_nav
        if dt < MIN_INTERVAL:
            time.sleep(MIN_INTERVAL - dt)
        self._last_nav = time.monotonic()
        log.debug("Megnyitás: %s", url)
        self.page.goto(url, wait_until=wait, timeout=60_000)

    def is_login_page(self) -> bool:
        return bool(self.page.query_selector("#loginbox")) or "login" in (
            self.page.evaluate("document.body.className") or ""
        )

    def save_state(self) -> None:
        path = self.s.session_file
        self.context.storage_state(path=str(path))
        try:
            os.chmod(path, 0o600)
        except OSError:
            pass


@contextmanager
def open_session(settings: Settings, headless: bool = False, login_mode: bool = False):
    if not login_mode and not settings.session_file.exists():
        raise SessionExpired("Nincs mentett session. Futtasd: python -m szte login")
    with sync_playwright() as p:
        browser = _launch(p, headless)
        ctx_kwargs = {"locale": "hu-HU", "accept_downloads": True}
        if settings.session_file.exists():
            ctx_kwargs["storage_state"] = str(settings.session_file)
        context = browser.new_context(**ctx_kwargs)
        page = context.new_page()
        sess = Session(settings, page, context)

        def guard(route):
            req = route.request
            ok, why = is_allowed(req.method, req.url, settings.base_url, login_mode)
            if ok:
                route.continue_()
            else:
                sess.blocked.append(f"{req.method} {req.url.split('?')[0]} ({why})")
                log.warning("Blokkolt kérés (csak olvasás): %s %s – %s", req.method, req.url.split("?")[0], why)
                route.abort()

        context.route("**/*", guard)
        try:
            yield sess
        finally:
            context.close()
            browser.close()
