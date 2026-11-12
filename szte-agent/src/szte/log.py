"""Naplózás, ami kitakarja a jelszót, a session cookie-t és a tokeneket."""
from __future__ import annotations

import logging
import re
from typing import Iterable

MASK = "***"

_PATTERNS = [
    # kulcs=érték / "kulcs": "érték" párok érzékeny kulcsokkal
    re.compile(
        r'(?i)("?(?:pass(?:word)?|jelszo|pwd|token|secret|api[_-]?key|session(?:id)?|'
        r'cookie|authorization|auth|x-csrf-token|\.aspnetcore\.[\w.]+)"?\s*[:=]\s*)'
        r'("[^"]*"|[^\s,;&}]+)'
    ),
    # Cookie / Set-Cookie fejléc teljes tartalma
    re.compile(r"(?i)((?:set-)?cookie:\s*)(.+)"),
    # Bearer tokenek
    re.compile(r"(?i)(bearer\s+)([\w\-.~+/]+=*)"),
    # Anthropic kulcs formátum
    re.compile(r"()(sk-ant-[\w-]+)"),
]


def redact(text: str, secrets: Iterable[str] = ()) -> str:
    for s in secrets:
        if s and len(s) >= 4:
            text = text.replace(s, MASK)
    for p in _PATTERNS:
        text = p.sub(lambda m: m.group(1) + MASK, text)
    return text


class RedactingFilter(logging.Filter):
    def __init__(self, secrets: Iterable[str] = ()):
        super().__init__()
        self.secrets = [s for s in secrets if s]

    def filter(self, record: logging.LogRecord) -> bool:
        msg = record.getMessage()
        record.msg = redact(msg, self.secrets)
        record.args = ()
        return True


def setup_logging(secrets: Iterable[str] = (), log_file=None, verbose: bool = False) -> logging.Logger:
    logger = logging.getLogger("szte")
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
    flt = RedactingFilter(secrets)
    handlers = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))
    for h in handlers:
        h.setFormatter(fmt)
        h.addFilter(flt)
        logger.addHandler(h)
    return logger
