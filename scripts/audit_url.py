#!/usr/bin/env python3
"""Surface SEO audit for a URL.

Usage:
  python scripts/audit_url.py https://example.com
  python scripts/audit_url.py https://example.com --json audit.json
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.meta = {}
        self.links = []
        self.h1 = []
        self.h2 = []
        self.in_h1 = False
        self.in_h2 = False
        self.current = []
        self.images = 0
        self.images_no_alt = 0
        self.jsonld = []
        self.in_jsonld = False
        self.jsonld_buf = []
        self.lang = ""
        self.text = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "title":
            self.in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag == "link":
            self.links.append(a)
        elif tag == "h1":
            self.in_h1 = True
            self.current = []
        elif tag == "h2":
            self.in_h2 = True
            self.current = []
        elif tag == "img":
            self.images += 1
            if not (a.get("alt") or "").strip():
                self.images_no_alt += 1
        elif tag == "script":
            if (a.get("type") or "").lower() == "application/ld+json":
                self.in_jsonld = True
                self.jsonld_buf = []
            else:
                self.skip += 1
        elif tag == "style":
            self.skip += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
            self.h1.append(re.sub(r"\s+", " ", "".join(self.current)).strip())
        elif tag == "h2":
            self.in_h2 = False
            self.h2.append(re.sub(r"\s+", " ", "".join(self.current)).strip())
        elif tag == "script":
            if self.in_jsonld:
                self.jsonld.append("".join(self.jsonld_buf))
                self.in_jsonld = False
            elif self.skip:
                self.skip -= 1
        elif tag == "style" and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_h1 or self.in_h2:
            self.current.append(data)
        elif self.in_jsonld:
            self.jsonld_buf.append(data)
        elif not self.skip:
            self.text.append(data)


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            body = r.read()
            return {
                "ok": True,
                "status": r.status,
                "final_url": r.geturl(),
                "content_type": r.headers.get("Content-Type", ""),
                "bytes": len(body),
                "ttfb": round(time.time() - t0, 2),
                "body": body,
                "error": None,
            }
    except Exception as exc:
        return {"ok": False, "status": None, "final_url": url, "content_type": "", "bytes": 0, "ttfb": round(time.time() - t0, 2), "body": b"", "error": str(exc)[:200]}


def schema_types(blocks):
    types = set()
    def walk(obj):
        if isinstance(obj, dict):
            t = obj.get("@type")
            if isinstance(t, list):
                types.update(str(x) for x in t)
            elif t:
                types.add(str(t))
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)
    for block in blocks:
        try:
            walk(json.loads(block))
        except Exception:
            types.add("PARSE_ERROR")
    return sorted(types)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--json", help="Write JSON report")
    parser.add_argument("--timeout", type=int, default=25)
    args = parser.parse_args()

    r = fetch(args.url, args.timeout)
    report = {
        "url": args.url,
        "status": r["status"],
        "final_url": r["final_url"],
        "content_type": r["content_type"],
        "ttfb_s": r["ttfb"],
        "bytes": r["bytes"],
        "error": r["error"],
    }

    if r["ok"] and r["body"]:
        html = r["body"].decode("utf-8", errors="ignore")
        p = Parser()
        p.feed(html)
        words = len(re.sub(r"\s+", " ", " ".join(p.text)).split())
        host = urllib.parse.urlparse(r["final_url"]).netloc
        internal = external = 0
        for link in p.links:
            href = (link.get("href") or "").strip()
            if href.startswith(("#", "mailto:", "tel:", "javascript:")):
                continue
            parsed = urllib.parse.urlparse(href)
            if parsed.netloc and parsed.netloc != host:
                external += 1
            else:
                internal += 1
        report.update({
            "title": re.sub(r"\s+", " ", p.title).strip(),
            "title_len": len(re.sub(r"\s+", " ", p.title).strip()),
            "description": p.meta.get("description", ""),
            "description_len": len(p.meta.get("description", "")),
            "h1_count": len(p.h1),
            "h1": p.h1[:3],
            "h2_count": len(p.h2),
            "canonical": next((l.get("href", "") for l in p.links if "canonical" in (l.get("rel") or [])), ""),
            "meta_robots": p.meta.get("robots", ""),
            "lang": p.lang,
            "viewport": "viewport" in p.meta,
            "schema_types": schema_types(p.jsonld),
            "images": p.images,
            "images_no_alt": p.images_no_alt,
            "internal_links": internal,
            "external_links": external,
            "words": words,
        })

        base = "{0.scheme}://{0.netloc}".format(urllib.parse.urlparse(r["final_url"]))
        secondary = {}
        for label, path in (("robots", "/robots.txt"), ("sitemap", "/sitemap.xml"), ("llms", "/llms.txt")):
            f = fetch(base + path, 15)
            secondary[label] = {
                "status": f["status"],
                "content_type": f["content_type"],
                "bytes": f["bytes"],
                "ok": f["ok"],
            }
        report["secondary"] = secondary

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
        print(f"Wrote {args.json}")
    else:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
