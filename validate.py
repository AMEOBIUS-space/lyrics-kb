#!/usr/bin/env python3
"""Validate index.json integrity: every entry has a file that exists, JSON is valid, count matches."""
import json, sys, os

KB_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(KB_DIR, "index.json")

def main():
    if not os.path.exists(INDEX):
        print("FAIL: index.json not found")
        sys.exit(1)

    with open(INDEX) as f:
        idx = json.load(f)

    entries = idx.get("entries", [])
    declared = idx.get("count", 0)

    errors = []

    if len(entries) != declared:
        errors.append(f"count mismatch: declared={declared}, actual={len(entries)}")

    seen_ids = set()
    for i, e in enumerate(entries):
        eid = e.get("id") or e.get("file") or f"entry-{i}"

        if eid in seen_ids:
            errors.append(f"[{eid}] duplicate id")
        seen_ids.add(eid)

        fp = e.get("file") or e.get("path")
        if not fp:
            errors.append(f"[{eid}] no file/path field")
            continue

        full = os.path.join(KB_DIR, fp)
        if not os.path.exists(full):
            errors.append(f"[{eid}] missing file: {fp}")

        if not e.get("title"):
            errors.append(f"[{eid}] missing title")
        if not e.get("category"):
            errors.append(f"[{eid}] missing category")

    if errors:
        print(f"FAIL: {len(errors)} errors")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"OK: {len(entries)} entries, {declared} declared, all files present")
        cats = {}
        for e in entries:
            c = e.get("category", "?")
            cats[c] = cats.get(c, 0) + 1
        for c, n in sorted(cats.items()):
            print(f"  {c}: {n}")
        sys.exit(0)

if __name__ == "__main__":
    main()
