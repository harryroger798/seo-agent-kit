#!/usr/bin/env python3
"""Build a distributable ZIP of the kit, excluding secrets and build artifacts.

Usage:
  python scripts/make_zip.py
"""

import json
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = json.load(open(os.path.join(ROOT, "kit.json"), encoding="utf-8"))["version"]
OUT = os.path.join(ROOT, "dist", f"seo-agent-kit-v{VERSION}.zip")

EXCLUDE_DIRS = {".git", "node_modules", "dist", "__pycache__", ".venv", "venv", "data/private"}
EXCLUDE_FILES = {".env", ".DS_Store"}
EXCLUDE_EXT = {".pyc", ".pyo", ".zip"}


def should_skip(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    name = parts[-1]
    if name in EXCLUDE_FILES:
        return True
    if os.path.splitext(name)[1].lower() in EXCLUDE_EXT:
        return True
    if rel_path.replace("\\", "/").startswith("site/preview-"):
        return True
    if rel_path.replace("\\", "/").startswith("site/.audit"):
        return True
    return False


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    count = 0
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
            for name in filenames:
                full = os.path.join(dirpath, name)
                rel = os.path.relpath(full, ROOT)
                if should_skip(rel):
                    continue
                zf.write(full, os.path.join("seo-agent-kit", rel))
                count += 1
    size = os.path.getsize(OUT)
    print(f"Wrote {OUT}")
    print(f"Files: {count}")
    print(f"Size: {size/1024:.1f} KB")


if __name__ == "__main__":
    main()
