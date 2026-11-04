#!/usr/bin/env python3
"""Concatenate the core kit files into llms-full.txt for assistants without repo access."""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = [
    "README.md",
    "AGENTS.md",
    "BOOTSTRAP.md",
    "kit.json",
    "docs/00-start-here.md",
    "docs/01-how-to-use-with-ai.md",
    "docs/02-connect-mcp.md",
    "docs/03-credentials-and-security.md",
    "docs/07-evidence-standard.md",
    "prompts/00-index.md",
    "prompts/01-intent-fanout.md",
    "prompts/02-silo.md",
    "prompts/03-brief.md",
    "prompts/04-draft.md",
    "prompts/05-edit.md",
    "prompts/06-repurpose.md",
    "prompts/07-listing.md",
    "prompts/08-directory.md",
    "prompts/09-paid-social.md",
    "prompts/10-qa.md",
    "prompts/11-gamma-deck.md",
    "prompts/12-prompt-audit.md",
    "playbooks/content-factory.md",
    "playbooks/listing-engine.md",
    "playbooks/directory-engine.md",
    "playbooks/paid-social.md",
    "playbooks/ai-search.md",
    "checklists/content-qa.md",
    "checklists/listing-qa.md",
    "checklists/directory-qa.md",
    "checklists/paid-social-qa.md",
    "checklists/technical-audit-120.md",
    "checklists/local-seo.md",
    "checklists/ai-visibility.md",
    "mcp/tool-matrix.md",
    "data/evidence-rules.md",
    "data/sources.csv",
    "data/tool-matrix.csv",
    "data/directory-seed.csv",
    "data/glossary.csv",
]

for skill in sorted(os.listdir(os.path.join(ROOT, "skills"))):
    path = os.path.join("skills", skill, "SKILL.md")
    if os.path.exists(os.path.join(ROOT, path)):
        FILES.append(path)

out = []
for rel in FILES:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        continue
    out.append(f"\n\n<!-- ===== {rel} ===== -->\n\n")
    out.append(open(path, encoding="utf-8").read().strip())

text = "# SEO Agent Kit — full context\n\nGenerated from the repository. Use this when an assistant cannot read the repo.\n" + "".join(out)
path = os.path.join(ROOT, "llms-full.txt")
open(path, "w", encoding="utf-8").write(text + "\n")
print(f"Wrote {path} ({len(text)} chars)")
