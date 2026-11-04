#!/usr/bin/env python3
"""Import a Notion directory database into data/directories.csv.

Setup:
  1. Create a Notion integration: https://www.notion.so/my-integrations
  2. Share the directory database with the integration.
  3. Set NOTION_TOKEN and NOTION_DATABASE_ID in .env (never commit).
  4. Run:
       python scripts/import_notion_directories.py --site aliasbrowser.com

The script auto-detects common property names (Directory, Category, URL, DR,
Free, Dofollow, API, Status, Listing URL, Notes). If your database uses
different names, edit the ALIASES map below.
"""

import argparse
import csv
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.notion.com/v1/databases/{db}/query"
VERSION = "2022-06-28"

ALIASES = {
    "directory": ["directory", "directory name", "name", "site name", "tool"],
    "category": ["category", "type", "niche"],
    "url": ["url", "website", "submission url", "link"],
    "dr": ["dr", "domain rating", "authority", "da"],
    "free": ["free", "free tier", "pricing"],
    "dofollow": ["dofollow", "do follow", "follow"],
    "api": ["api", "api status", "api available"],
    "status": ["status"],
    "listing_url": ["listing url", "live url", "published url"],
    "notes": ["notes", "note", "comment"],
}

COLUMNS = ["site", "directory", "category", "tier", "dr", "free", "dofollow", "api",
           "status", "listing_url", "submitted_date", "verified_date", "notes"]


def env(name):
    value = os.environ.get(name, "").strip()
    if value:
        return value
    env_path = os.path.join(ROOT, ".env")
    if os.path.exists(env_path):
        for line in open(env_path, encoding="utf-8"):
            if line.strip().startswith(name + "="):
                return line.split("=", 1)[1].strip()
    return ""


def text_of(prop):
    if not prop:
        return ""
    t = prop.get("type")
    if t == "title":
        return "".join(x.get("plain_text", "") for x in prop.get("title", []))
    if t == "rich_text":
        return "".join(x.get("plain_text", "") for x in prop.get("rich_text", []))
    if t == "select":
        return (prop.get("select") or {}).get("name", "")
    if t == "status":
        return (prop.get("status") or {}).get("name", "")
    if t == "multi_select":
        return ", ".join(x.get("name", "") for x in prop.get("multi_select", []))
    if t == "number":
        return "" if prop.get("number") is None else str(prop.get("number"))
    if t == "checkbox":
        return "yes" if prop.get("checkbox") else "no"
    if t == "url":
        return prop.get("url") or ""
    if t == "email":
        return prop.get("email") or ""
    if t == "formula":
        return text_of(prop.get("formula", {}))
    return ""


def pick(props, key):
    aliases = ALIASES[key]
    lower = {k.lower().strip(): v for k, v in props.items()}
    for alias in aliases:
        if alias in lower:
            return text_of(lower[alias])
    return ""



def search_databases(token):
    req = urllib.request.Request(
        "https://api.notion.com/v1/search",
        data=json.dumps({
            "filter": {"property": "object", "value": "database"},
            "page_size": 100,
        }).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + token,
            "Notion-Version": VERSION,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    results = data.get("results", [])
    print(f"Databases visible to this integration: {len(results)}")
    for db in results:
        title = "".join(x.get("plain_text", "") for x in db.get("title", [])) or "(untitled)"
        print(f"  {db.get('id')}  {title}")
        print(f"    {db.get('url', '')}")
    return results


def query(db, token):
    results = []
    cursor = None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        req = urllib.request.Request(
            API.format(db=db),
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Authorization": "Bearer " + token,
                "Notion-Version": VERSION,
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode("utf-8"))
        results.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="", help="Domain to fill in the site column")
    parser.add_argument("--out", default="data/directories.csv")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--search", action="store_true", help="List databases the integration can see")
    args = parser.parse_args()

    token = env("NOTION_TOKEN")
    db = env("NOTION_DATABASE_ID")
    if not token:
        print("NOTION_TOKEN is not set.")
        print("Add it to .env (see .env.example) or export it in your shell.")
        print("Do not paste the token into chat.")
        return 1
    if args.search:
        search_databases(token)
        return 0
    if not db:
        print("NOTION_DATABASE_ID is not set.")
        print("Add it to .env (see .env.example) or export it in your shell.")
        return 1

    try:
        pages = query(db, token)
    except urllib.error.HTTPError as exc:
        print(f"Notion returned HTTP {exc.code}.")
        if exc.code == 404:
            print("The integration cannot see this database, or the ID is wrong.")
            print("Open the database in Notion -> ... -> Connections -> add your integration.")
            print("Then copy the 32-character database ID from the URL (before ?v=).")
            print("Run with --search to list the databases this integration can see.")
        elif exc.code == 401:
            print("The token is invalid or expired. Re-copy the Internal Integration Secret.")
        else:
            print(exc.read().decode("utf-8", errors="ignore")[:500])
        return 1
    print(f"Fetched {len(pages)} pages from Notion.")
    if args.dry_run:
        return 0

    rows = []
    for page in pages:
        props = page.get("properties", {})
        rows.append({
            "site": args.site,
            "directory": pick(props, "directory"),
            "category": pick(props, "category"),
            "tier": "",
            "dr": pick(props, "dr"),
            "free": pick(props, "free"),
            "dofollow": pick(props, "dofollow"),
            "api": pick(props, "api"),
            "status": pick(props, "status") or "To do",
            "listing_url": pick(props, "listing_url"),
            "submitted_date": "",
            "verified_date": "",
            "notes": pick(props, "notes"),
        })

    path = args.out if os.path.isabs(args.out) else os.path.join(ROOT, args.out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {path} ({len(rows)} rows)")
    print("Next: run scripts/directory_dedupe.py data/directories.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
