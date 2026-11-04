# Repo map

```
seo-agent-kit/
├── README.md                 # human front door
├── AGENTS.md                 # agent contract
├── BOOTSTRAP.md              # copy-paste prompt for any AI
├── CLAUDE.md                 # Claude Code entry
├── kit.json                  # machine-readable manifest
├── llms.txt                  # agent index
├── llms-full.txt             # full agent context
├── LICENSE                   # MIT (code)
├── LICENSE-CONTENT           # CC BY 4.0 (content)
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── .env.example
├── .gitignore
├── .github/
│   ├── workflows/validate.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── 00-start-here.md
│   ├── 01-how-to-use-with-ai.md
│   ├── 02-connect-mcp.md
│   ├── 03-credentials-and-security.md
│   ├── 04-repo-map.md
│   ├── 05-contributing.md
│   ├── 06-faq.md
│   └── 07-evidence-standard.md
├── skills/
│   ├── seo-orchestrator/SKILL.md
│   ├── silo-builder/SKILL.md
│   ├── content-factory/SKILL.md
│   ├── humanizer/SKILL.md
│   ├── repurposer/SKILL.md
│   ├── product-listing/SKILL.md
│   ├── directory-submission/SKILL.md
│   ├── paid-social/SKILL.md
│   ├── ai-visibility/SKILL.md
│   ├── technical-audit/SKILL.md
│   └── local-seo/SKILL.md
├── prompts/
│   ├── 00-index.md
│   ├── 01-intent-fanout.md
│   ├── 02-silo.md
│   ├── 03-brief.md
│   ├── 04-draft.md
│   ├── 05-edit.md
│   ├── 06-repurpose.md
│   ├── 07-listing.md
│   ├── 08-directory.md
│   ├── 09-paid-social.md
│   ├── 10-qa.md
│   ├── 11-gamma-deck.md
│   └── 12-prompt-audit.md
├── playbooks/
│   ├── content-factory.md
│   ├── listing-engine.md
│   ├── directory-engine.md
│   ├── paid-social.md
│   └── ai-search.md
├── checklists/
│   ├── content-qa.md
│   ├── listing-qa.md
│   ├── directory-qa.md
│   ├── paid-social-qa.md
│   ├── technical-audit-120.md
│   ├── local-seo.md
│   └── ai-visibility.md
├── templates/
│   ├── content-brief.md
│   ├── listing.md
│   ├── directory-tracker.csv
│   ├── campaign-brief.md
│   ├── monthly-report.md
│   ├── prompt-spec.md
│   └── source-register.csv
├── schemas/
│   ├── kit.schema.json
│   ├── content-brief.schema.json
│   ├── listing.schema.json
│   ├── directory-row.schema.json
│   └── jsonld/
│       ├── organization.json
│       ├── website.json
│       ├── breadcrumb.json
│       ├── article.json
│       ├── localbusiness.json
│       ├── softwareapplication.json
│       ├── product.json
│       └── person.json
├── mcp/
│   ├── README.md
│   ├── servers.example.json
│   ├── claude-desktop.example.json
│   ├── cursor.example.json
│   └── tool-matrix.md
├── scripts/
│   ├── validate_kit.py
│   ├── render_prompt.py
│   ├── audit_url.py
│   ├── sitemap_check.py
│   ├── ai_visibility_panel.py
│   ├── directory_dedupe.py
│   └── make_zip.py
├── data/
│   ├── sources.csv
│   ├── tool-matrix.csv
│   ├── directory-seed.csv
│   ├── glossary.csv
│   └── evidence-rules.md
└── examples/
    ├── 01-rocketclips-silo.md
    ├── 02-byte-shop-listing.md
    ├── 03-alias-browser-directory.md
    └── 04-cini-travels-local.md
```

## Reading order

1. `README.md`
2. `AGENTS.md`
3. `kit.json`
4. `skills/seo-orchestrator/SKILL.md`
5. The skill for your task.
6. The prompt, playbook, checklist, and template that skill references.
