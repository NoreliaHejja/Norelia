"""E-mail küldés SMTP-n (hibariasztás; később napi/heti összefoglaló)."""
from __future__ import annotations

import logging
import smtplib
from email.message import EmailMessage

from szte.config import Settings
from szte.log import redact

log = logging.getLogger("szte")


def send_email(settings: Settings, subject: str, body: str) -> bool:
    if not (settings.smtp_user and settings.smtp_pass and settings.alert_to):
        log.warning("Nincs beállítva SMTP (SMTP_USER / SMTP_PASS / ALERT_TO) – e-mail nem ment ki: %s", subject)
        return False
    msg = EmailMessage()
    msg["Subject"] = f"[SZTE agent] {subject}"
    msg["From"] = settings.smtp_user
    msg["To"] = settings.alert_to
    msg.set_content(redact(body, settings.secrets()))
    try:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=30) as smtp:
            smtp.starttls()
            smtp.login(settings.smtp_user, settings.smtp_pass)
            smtp.send_message(msg)
        log.info("E-mail elküldve: %s", subject)
        return True
    except Exception as e:  # a riasztás hibája ne takarja el az eredeti hibát
        log.error("E-mail küldés sikertelen: %s", e)
        return False


def alert(settings: Settings, title: str, details: str) -> None:
    send_email(settings, f"HIBA – {title}", details)
