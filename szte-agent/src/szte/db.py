"""SQLite adattár (data/szte.sqlite). Minden tételnek stabil egyedi azonosítója van."""
from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS spaces (
    uid TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT,
    term TEXT,
    semester TEXT,
    in_term INTEGER NOT NULL DEFAULT 0,
    source TEXT,
    raw TEXT,
    first_seen TEXT NOT NULL,
    last_seen TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS items (
    uid TEXT PRIMARY KEY,            -- színtér + típus + forrás-azonosító hash
    space_uid TEXT REFERENCES spaces(uid),
    kind TEXT NOT NULL,              -- beadando / vizsga / teszt / hirdetmeny / dokumentum / egyeb
    title TEXT NOT NULL,
    due TEXT,
    where_to_submit TEXT,
    status TEXT NOT NULL DEFAULT 'új',
    source_url TEXT,
    content_hash TEXT,
    raw TEXT,
    first_seen TEXT NOT NULL,
    last_seen TEXT NOT NULL,
    changed_at TEXT
);
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started TEXT NOT NULL,
    finished TEXT,
    command TEXT,
    ok INTEGER,
    message TEXT
);
"""


def now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def connect(path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def upsert_space(con: sqlite3.Connection, row: dict, semester: str, in_term: bool) -> bool:
    """True, ha új színtér."""
    t = now()
    cur = con.execute("SELECT uid FROM spaces WHERE uid=?", (row["uid"],)).fetchone()
    if cur:
        con.execute(
            "UPDATE spaces SET name=?, url=COALESCE(NULLIF(?, ''), url), term=?, semester=?, in_term=?,"
            " source=?, raw=?, last_seen=? WHERE uid=?",
            (row["name"], row["url"], row["term"], semester, int(in_term), row["source"], row["raw"], t, row["uid"]),
        )
        return False
    con.execute(
        "INSERT INTO spaces(uid,name,url,term,semester,in_term,source,raw,first_seen,last_seen)"
        " VALUES(?,?,?,?,?,?,?,?,?,?)",
        (row["uid"], row["name"], row["url"], row["term"], semester, int(in_term), row["source"], row["raw"], t, t),
    )
    return True


def log_run(con: sqlite3.Connection, command: str, ok: bool, message: str, started: str) -> None:
    con.execute(
        "INSERT INTO runs(started, finished, command, ok, message) VALUES(?,?,?,?,?)",
        (started, now(), command, int(ok), message[:2000]),
    )
    con.commit()
