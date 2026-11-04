#!/usr/bin/env python3
"""Render a prompt by replacing {{variables}}.

Usage:
  python scripts/render_prompt.py prompts/02-silo.md \
    --var keyword="AI video clipper" \
    --var brand="Byte Shop" \
    --out rendered.md
"""

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def extract_prompt(text):
    match = re.search(r"```text\n(.*?)```", text, re.S)
    if not match:
        raise ValueError("No ```text prompt block found")
    return match.group(1).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Path to a prompt markdown file")
    parser.add_argument("--var", action="append", default=[], help="key=value")
    parser.add_argument("--out", help="Write to a file instead of stdout")
    parser.add_argument("--list", action="store_true", help="List variables and exit")
    args = parser.parse_args()

    path = args.prompt
    if not os.path.isabs(path):
        path = os.path.join(ROOT, path)
    if not os.path.exists(path):
        print(f"Not found: {path}", file=sys.stderr)
        return 2

    text = open(path, encoding="utf-8").read()
    prompt = extract_prompt(text)
    variables = sorted(set(re.findall(r"\{\{(\w+)\}\}", prompt)))

    if args.list:
        print("\n".join(variables))
        return 0

    values = {}
    for item in args.var:
        if "=" not in item:
            print(f"Bad --var (expected key=value): {item}", file=sys.stderr)
            return 2
        key, value = item.split("=", 1)
        values[key.strip()] = value

    missing = [v for v in variables if v not in values]
    if missing:
        print("Missing variables:", ", ".join(missing), file=sys.stderr)
        print("Pass them with --var key=value", file=sys.stderr)
        return 2

    rendered = prompt
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(rendered + "\n")
        print(f"Wrote {args.out}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
