"""Parancssor: python -m szte <parancs>"""
from __future__ import annotations

import argparse
import json
import logging
import traceback

from szte.config import load_settings
from szte.db import connect, log_run, now, upsert_space
from szte.log import redact, setup_logging
from szte.notify.email import alert

log = logging.getLogger("szte")

LATER = {
    "deadlines": 2, "summarize": 3, "draft": 4, "done": 2, "opportunities": 5, "weekly": 6,
}


def cmd_login(s, args) -> int:
    from szte.scraper.login import interactive_login

    return 0 if interactive_login(s) else 1


def write_spaces_md(s, rows) -> None:
    out = s.root / "output"
    out.mkdir(exist_ok=True)
    lines = [f"# Színterek – {s.term}", "", f"Frissítve: {now()}", "",
             "| # | Színtér | Félév | Link |", "|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        link = f"[megnyit]({r['url']})" if r["url"] else "–"
        lines.append(f"| {i} | {r['name']} | {r['semester']} | {link} |")
    (out / "szinterek.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_spaces(s, args) -> int:
    from szte.scraper.browser import open_session
    from szte.scraper.spaces import collect_spaces, matches_term, semester_of

    with open_session(s, headless=args.headless) as sess:
        try:
            spaces, dump = collect_spaces(sess)
        finally:
            sess.save_state()  # a frissített cookie-k megtartása
    s.debug_dir.mkdir(parents=True, exist_ok=True)
    (s.debug_dir / "spaces_dump.json").write_text(
        redact(json.dumps(dump, ensure_ascii=False, indent=1, default=str), s.secrets()), encoding="utf-8"
    )

    con = connect(s.db_file)
    new, in_term = 0, []
    for sp in spaces:
        ok = matches_term(sp, s.term)
        sem = semester_of(sp)
        new += upsert_space(con, sp.to_row(), sem, ok)
        if ok:
            in_term.append({"name": sp.name, "url": sp.url, "semester": sem})
    con.commit()

    in_term.sort(key=lambda r: (r["semester"], r["name"]))
    write_spaces_md(s, in_term)
    print(f"\nÖsszes talált színtér: {len(spaces)} (ebből új: {new})")
    print(f"{s.term} tanév színterei: {len(in_term)}\n")
    for i, r in enumerate(in_term, 1):
        print(f"  {i:>2}. [{r['semester']}. félév] {r['name']}")
    if not in_term:
        print("  (A tanévszűrő egyet sem talált. Az összes színtér: data/szte.sqlite, nyers adat: data/debug/)")
        for sp in spaces[:40]:
            print(f"     – {sp.name}  {sp.term}")
    if sess.blocked:
        print(f"\nBlokkolt (írási) kérések száma: {len(sess.blocked)} – részletek: data/debug/spaces_dump.json")
    print("\nTábla: output/szinterek.md")
    return 0


def cmd_sync(s, args) -> int:
    # 1. fázis: a szinkron egyelőre a színterek listázása. A 2–3. fázis itt bővül.
    return cmd_spaces(s, args)


def cmd_later(s, args) -> int:
    print(f"A(z) '{args.cmd}' parancs a {LATER[args.cmd]}. fejlesztési fázisban készül el.")
    return 2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m szte", description="SZTE tanulmányi agent (CooSpace, csak olvasás)")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("login", help="kézi belépés látható böngészőben, session mentése")
    for name, help_ in (("spaces", "színterek listázása, tanévszűrés"), ("sync", "CooSpace szinkron")):
        sp = sub.add_parser(name, help=help_)
        sp.add_argument("--headless", action="store_true", help="rejtett böngésző (a CooSpace tilthatja)")
    for name in LATER:
        sp = sub.add_parser(name, help=f"{LATER[name]}. fázis")
        if name in ("draft", "done"):
            sp.add_argument("id")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    s = load_settings()
    setup_logging(s.secrets(), log_file=s.data_dir / "agent.log", verbose=args.verbose)
    handler = {"login": cmd_login, "spaces": cmd_spaces, "sync": cmd_sync}.get(args.cmd, cmd_later)
    started = now()
    con = connect(s.db_file)
    try:
        rc = handler(s, args)
        log_run(con, args.cmd, rc == 0, "ok" if rc == 0 else f"rc={rc}", started)
        return rc
    except Exception as e:
        from szte.scraper.browser import LayoutChanged, SessionExpired

        dump = getattr(e, "dump", None)
        if dump:
            s.debug_dir.mkdir(parents=True, exist_ok=True)
            (s.debug_dir / "spaces_dump.json").write_text(
                redact(json.dumps(dump, ensure_ascii=False, indent=1, default=str), s.secrets()), encoding="utf-8"
            )
        msg = redact(f"{type(e).__name__}: {e}", s.secrets())
        log.error(msg)
        log_run(con, args.cmd, False, msg, started)
        if isinstance(e, SessionExpired):
            alert(s, "Lépj be újra a CooSpace-be", f"{e}\n\nParancs: python -m szte login")
        elif isinstance(e, LayoutChanged):
            alert(s, "Megváltozott a CooSpace felülete", msg)
        else:
            alert(s, f"'{args.cmd}' futás hibával leállt", redact(traceback.format_exc(), s.secrets()))
        return 1
