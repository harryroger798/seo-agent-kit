#!/usr/bin/env python3
"""Validate the SEO Agent Kit.

Checks:
- required files
- kit.json parses and references existing paths
- every SKILL.md has name + description
- every prompt has name + description + inputs + outputs + requires
- every JSON file parses
- no obvious secrets
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []
WARNINGS = []


def fail(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def rel(path):
    return os.path.relpath(path, ROOT)


def check_required():
    required = [
        "README.md", "AGENTS.md", "BOOTSTRAP.md", "CLAUDE.md", "kit.json",
        "LICENSE", "LICENSE-CONTENT", "CONTRIBUTING.md", "SECURITY.md",
        ".gitignore", ".env.example",
        "docs/00-start-here.md", "docs/02-connect-mcp.md",
        "skills/seo-orchestrator/SKILL.md",
        "prompts/00-index.md",
        "checklists/technical-audit-120.md",
        "schemas/kit.schema.json",
        "mcp/tool-matrix.md",
    ]
    for name in required:
        if not os.path.exists(os.path.join(ROOT, name)):
            fail(f"missing required file: {name}")


def check_manifest():
    path = os.path.join(ROOT, "kit.json")
    try:
        data = json.loads(read(path))
    except Exception as exc:
        fail(f"kit.json does not parse: {exc}")
        return
    for key in ("name", "version", "description", "entrypoints", "capabilities", "tools", "paths"):
        if key not in data:
            fail(f"kit.json missing key: {key}")
    for cap in data.get("capabilities", []):
        for key in ("id", "name", "inputs", "outputs"):
            if key not in cap:
                fail(f"capability missing {key}: {cap.get('id', '?')}")
        for field in ("skill", "prompt", "playbook", "checklist"):
            if field in cap and not os.path.exists(os.path.join(ROOT, cap[field])):
                fail(f"capability {cap['id']} references missing {field}: {cap[field]}")
        for prompt in cap.get("prompts", []):
            if not os.path.exists(os.path.join(ROOT, prompt)):
                fail(f"capability {cap['id']} references missing prompt: {prompt}")


def parse_frontmatter(path):
    text = read(path)
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    data = {}
    for line in block.splitlines():
        if ":" in line and not line.strip().startswith("#"):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def check_skills():
    skills_dir = os.path.join(ROOT, "skills")
    if not os.path.isdir(skills_dir):
        fail("missing skills/ directory")
        return
    count = 0
    for name in sorted(os.listdir(skills_dir)):
        skill = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.exists(skill):
            continue
        count += 1
        fm = parse_frontmatter(skill)
        if not fm:
            fail(f"{rel(skill)}: missing YAML frontmatter")
            continue
        for key in ("name", "description"):
            if not fm.get(key):
                fail(f"{rel(skill)}: missing {key}")
        if fm.get("name") and fm["name"] != name:
            warn(f"{rel(skill)}: name '{fm['name']}' does not match folder '{name}'")
    if count == 0:
        fail("no skills found")


def check_prompts():
    prompts_dir = os.path.join(ROOT, "prompts")
    if not os.path.isdir(prompts_dir):
        fail("missing prompts/ directory")
        return
    count = 0
    for name in sorted(os.listdir(prompts_dir)):
        if not name.endswith(".md") or name == "00-index.md":
            continue
        path = os.path.join(prompts_dir, name)
        count += 1
        fm = parse_frontmatter(path)
        if not fm:
            fail(f"{rel(path)}: missing YAML frontmatter")
            continue
        for key in ("name", "description", "inputs", "outputs", "requires"):
            if key not in fm:
                fail(f"{rel(path)}: missing {key}")
        body = read(path)
        if "```text" not in body:
            fail(f"{rel(path)}: missing ```text prompt block")
        if "{{" not in body:
            warn(f"{rel(path)}: no {{variables}} found")
        for bad in ("bypass AI detection", "keyword density"):
            if bad.lower() in body.lower():
                warn(f"{rel(path)}: contains '{bad}'")
    if count == 0:
        fail("no prompts found")


def check_json():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "dist", "__pycache__")]
        for name in filenames:
            if not name.endswith(".json"):
                continue
            path = os.path.join(dirpath, name)
            try:
                json.loads(read(path))
            except Exception as exc:
                fail(f"{rel(path)}: invalid JSON: {exc}")


SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{20,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"AIza[0-9A-Za-z\-_]{20,}",
    r"xox[baprs]-[A-Za-z0-9-]{10,}",
    r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----",
]


def check_secrets():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "dist", "__pycache__")]
        for name in filenames:
            if name in (".env",) or name.endswith((".zip", ".pdf", ".png", ".jpg", ".webp")):
                continue
            path = os.path.join(dirpath, name)
            try:
                text = read(path)
            except Exception:
                continue
            for pattern in SECRET_PATTERNS:
                if re.search(pattern, text):
                    fail(f"possible secret in {rel(path)} (pattern {pattern})")


def main():
    check_required()
    check_manifest()
    check_skills()
    check_prompts()
    check_json()
    check_secrets()

    print(f"Checked: {rel(ROOT)}")
    print(f"Errors: {len(ERRORS)}")
    print(f"Warnings: {len(WARNINGS)}")
    for msg in ERRORS:
        print(f"  ERROR: {msg}")
    for msg in WARNINGS:
        print(f"  WARN:  {msg}")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
