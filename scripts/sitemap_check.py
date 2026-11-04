#!/usr/bin/env python3
"""Check a sitemap for URL count, status codes, and nested sitemaps.

Usage:
  python scripts/sitemap_check.py https://example.com
  python scripts/sitemap_check.py https://example.com --check --limit 50
"""

import argparse
import re
import ssl
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; SEOAgentKit/1.0)"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except Exception as exc:
        return None, str(exc)[:120], b""


def locs(xml):
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml, re.I)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Site root or sitemap URL")
    parser.add_argument("--check", action="store_true", help="Check status of each URL")
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    base = args.url.rstrip("/")
    sitemap_url = base if base.endswith(".xml") else base + "/sitemap.xml"
    status, ctype, body = fetch(sitemap_url, args.timeout)
    xml = body.decode("utf-8", errors="ignore")
    urls = locs(xml)

    print(f"Sitemap: {sitemap_url}")
    print(f"Status: {status}")
    print(f"Content-Type: {ctype}")
    print(f"Bytes: {len(body)}")
    print(f"URLs: {len(urls)}")

    if not urls:
        print("No <loc> entries found. The file may be an HTML soft 404 or a sitemap index.")
        return 1

    if urls and urls[0].endswith(".xml"):
        print("This looks like a sitemap index. Nested sitemaps:")
        for child in urls[:20]:
            print("  -", child)

    if args.check:
        print(f"\nChecking first {min(args.limit, len(urls))} URLs...")
        counts = {}
        for url in urls[:args.limit]:
            code, _, _ = fetch(url, args.timeout)
            counts[code] = counts.get(code, 0) + 1
            print(f"  {code}  {url}")
        print("\nStatus counts:", counts)

    return 0


if __name__ == "__main__":
    sys.exit(main())
