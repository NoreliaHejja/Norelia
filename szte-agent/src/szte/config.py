"""Beállítások a .env fájlból. Titok soha nem kerül a kódba."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]  # szte-agent/


@dataclass(frozen=True)
class Settings:
    base_url: str
    user: str
    password: str = field(repr=False)
    term: str
    anthropic_key: str = field(repr=False)
    smtp_host: str
    smtp_port: int
    smtp_user: str
    smtp_pass: str = field(repr=False)
    alert_to: str
    root: Path = ROOT

    @property
    def data_dir(self) -> Path:
        return self.root / "data"

    @property
    def session_file(self) -> Path:
        return self.data_dir / "session.json"

    @property
    def db_file(self) -> Path:
        return self.data_dir / "szte.sqlite"

    @property
    def debug_dir(self) -> Path:
        return self.data_dir / "debug"

    def secrets(self) -> list[str]:
        """Minden érték, aminek nem szabad megjelennie a naplóban."""
        return [s for s in (self.password, self.anthropic_key, self.smtp_pass) if s]


def load_settings(root: Path = ROOT) -> Settings:
    load_dotenv(root / ".env")
    g = os.environ.get
    url = g("COOSPACE_URL", "https://unics.szte.hu/").strip()
    # A régi coosp.etr.u-szeged.hu már csak egy választóoldal – az új felület a unics.
    if "coosp.etr.u-szeged.hu" in url:
        url = "https://unics.szte.hu/"
    if not url.endswith("/"):
        url += "/"
    s = Settings(
        base_url=url,
        user=g("COOSPACE_USER", "").strip(),
        password=g("COOSPACE_PASS", ""),
        term=g("TERM", "2026/27").strip(),
        anthropic_key=g("ANTHROPIC_API_KEY", ""),
        smtp_host=g("SMTP_HOST", "smtp.gmail.com"),
        smtp_port=int(g("SMTP_PORT", "587")),
        smtp_user=g("SMTP_USER", ""),
        smtp_pass=g("SMTP_PASS", ""),
        alert_to=g("ALERT_TO", ""),
        root=root,
    )
    s.data_dir.mkdir(parents=True, exist_ok=True)
    return s
