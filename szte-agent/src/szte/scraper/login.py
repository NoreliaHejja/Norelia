"""Kézi belépés látható böngészőben. A reCAPTCHA-t és a Belépés gombot Nóra nyomja meg."""
from __future__ import annotations

import logging
import time

from szte.config import Settings
from szte.scraper.browser import open_session

log = logging.getLogger("szte")

TIMEOUT = 300  # mp


def interactive_login(settings: Settings) -> bool:
    with open_session(settings, headless=False, login_mode=True) as sess:
        sess.goto(settings.base_url)
        if not sess.is_login_page():
            log.info("Már be vagy lépve – a sessiont frissítettem.")
            sess.save_state()
            return True
        page = sess.page
        # Előkitöltés, ha a .env-ben megvan. Az értékek sehol nem kerülnek naplóba.
        user_box = page.query_selector("input[name='username'], input#username, input[type='text']")
        pass_box = page.query_selector("input[type='password']")
        if settings.user and user_box:
            user_box.fill(settings.user)
        if settings.password and pass_box:
            pass_box.fill(settings.password)
        print(
            "\n>>> A megnyílt böngészőben pipáld ki a reCAPTCHA-t, és kattints a Belépésre.\n"
            f">>> {TIMEOUT // 60} perced van. Utána ezt az ablakot ne zárd be, magától bezáródik.\n"
        )
        end = time.monotonic() + TIMEOUT
        while time.monotonic() < end:
            page.wait_for_timeout(1500)
            try:
                if not sess.is_login_page():
                    page.wait_for_load_state("networkidle", timeout=30_000)
                    sess.save_state()
                    log.info("Sikeres belépés, session elmentve: data/session.json")
                    return True
            except Exception:
                continue  # átirányítás közben a DOM épp cserélődik
        log.error("Nem történt belépés %s percen belül.", TIMEOUT // 60)
        return False
