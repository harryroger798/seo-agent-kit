#!/usr/bin/env python3
"""Check a directory tracker for duplicate site+directory pairs, duplicate URLs,
invalid statuses, and paid/badge flags.

Usage:
  python scripts/directory_dedupe.py templates/directory-tracker.csv
"""

import argparse
import csv
import os
import sys

VALID = {"To do", "In progress", "Submitted", "Live", "Skipped", "Failed", "Already listed"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tracker")
    args = parser.parse_args()

    path = args.tracker
    if not os.path.isabs(path):
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), path)
    if not os.path.exists(path):
        print(f"Not found: {path}", file=sys.stderr)
        return 2

    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    seen = {}
    urls = {}
    problems = 0
    for i, row in enumerate(rows, 2):
        key = (row.get("site", "").strip().lower(), row.get("directory", "").strip().lower())
        if key in seen:
            print(f"DUPLICATE site+directory: {key} (rows {seen[key]} and {i})")
            problems += 1
        seen[key] = i

        url = row.get("listing_url", "").strip()
        if url:
            if url in urls:
                print(f"DUPLICATE listing_url: {url} (rows {urls[url]} and {i})")
                problems += 1
            urls[url] = i

        status = row.get("status", "").strip()
        if status and status not in VALID:
            print(f"INVALID status at row {i}: {status}")
            problems += 1

        if row.get("free", "").strip().lower() == "no" and status not in ("Skipped", "Failed"):
            print(f"PAID directory not skipped at row {i}: {row.get('directory')}")
            problems += 1

    print(f"\nRows: {len(rows)}")
    print(f"Problems: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
