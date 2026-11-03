import argparse
import json
import sqlite3
import sys
from pathlib import Path
from .store import Store

def main(argv=None):
    parser = argparse.ArgumentParser(description="Local holiday-home draft and approval desk; never publishes")
    parser.add_argument("--db", default="zuna.sqlite3")
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create"); create.add_argument("input", type=Path)
    for name in ("show", "approve", "reject", "events"):
        cmd = sub.add_parser(name); cmd.add_argument("id", type=int)
    args = parser.parse_args(argv)
    store = None
    try:
        store = Store(args.db)
        if args.command == "create": result = store.create(json.loads(args.input.read_text()))
        elif args.command == "show": result = store.get(args.id)
        elif args.command == "events": result = store.events(args.id)
        else: result = store.decide(args.id, "approved" if args.command == "approve" else "rejected")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    finally:
        if store: store.close()

if __name__ == "__main__":
    raise SystemExit(main())
