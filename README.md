# SEO Agent Kit

**A public, agent-readable SEO operating system. Not a PDF. A repo your AI can actually run.**

**Built by [GEOwallah](https://geowallah.com)** ? AI Search & Local SEO Agency.

**Live site:** https://harryroger798.github.io/seo-agent-kit/

[![License: MIT](https://img.shields.io/badge/code-MIT-17130f.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-c9430a.svg)](LICENSE-CONTENT)
[![Agent-ready](https://img.shields.io/badge/agent--ready-AGENTS.md-1e4b39.svg)](AGENTS.md)
[![Skills](https://img.shields.io/badge/skills-Agent%20Skills-1e4b39.svg)](skills/)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-c9430a.svg)](CONTRIBUTING.md)

Most SEO prompt packs are screenshots, PDFs, or a 4,000-word chat log. They are written for a human to copy and paste. This kit is written for an **agent** to read, route, and execute: structured skills, versioned prompts, explicit inputs, QA gates, MCP/API adapters, and a machine-readable manifest.

It is the operating layer behind [The Operator's SEO Playbook 2026](https://github.com/) — the curriculum teaches the thinking; this repo runs the work.

---

## What it does

Give it a site, a goal, and a tool connection. It can:

- Build a **silo and cluster** from a money page, not a keyword list.
- Turn a brief into a **sourced article** with internal links, external citations, schema, and a product link used once.
- **Humanise** the draft without inventing experience or "bypassing detectors."
- **Repurpose** one article into platform-native posts, not the same paragraph on 14 networks.
- Build a **digital product listing** with comparison table, FAQ, delivery, validity, and image metadata.
- Run a **directory submission batch** with duplicate checks, status tracking, and verification.
- Build a **Facebook/WhatsApp campaign** with five creatives, one video, and a measurement model.
- Audit **AI visibility** with a prompt panel, GSC AI impressions, and GA4's AI Assistant channel.
- Run a **120-point technical/local/content audit**.
- Generate a **Gamma deck** from the playbooks.

---

## Quickstart

### 1. Clone and open in your agent

```bash
git clone https://github.com/harryroger798/seo-agent-kit.git
cd seo-agent-kit
```

Open the folder in **Claude Code**, **Cursor**, **Codex**, **Gemini CLI**, **Windsurf**, or any agent that reads `AGENTS.md`.

Then say:

> Read `AGENTS.md`, `kit.json`, and `skills/seo-orchestrator/SKILL.md`. Ask me the three intake questions before doing anything.

### 2. No repo access? Paste the bootstrap

Open [`BOOTSTRAP.md`](BOOTSTRAP.md), copy the prompt, and paste it into ChatGPT, Claude, Gemini, or any assistant that can read files or a repo URL. Attach the ZIP if the assistant cannot browse.

### 3. Use it manually

Every prompt is a standalone Markdown file with variables at the top:

```bash
python scripts/render_prompt.py prompts/02-silo.md \
  --var keyword="AI video clipper for podcasters" \
  --var product_url="https://example.com/product" \
  --var brand="Byte Shop" \
  --var market="India"
```

---

## The four pipelines

```
DEMAND
  |
  +--> CONTENT: keyword -> SERP delta -> brief -> article -> edit -> 7 derivatives
  |
  +--> LISTING: product -> facts -> comparison -> FAQ -> images -> listing -> QA
  |
  +--> DIRECTORY: site -> brief -> contact -> assets -> submit -> verify -> live
  |
  +--> PAID: offer -> audience -> 5 creatives -> WhatsApp/landing -> measure
```

Every pipeline has one canonical output and one QA gate. Derivatives may change the hook; they may not change the facts.

---

## What's inside

| Folder | What it is | Start with |
|---|---|---|
| `skills/` | 11 Agent Skills (`SKILL.md`) that route and execute the work | `skills/seo-orchestrator/SKILL.md` |
| `prompts/` | 12 versioned master prompts with variables and output contracts | `prompts/00-index.md` |
| `playbooks/` | The four production pipelines, end to end | `playbooks/content-factory.md` |
| `checklists/` | QA gates, 120-point audit, local, AI visibility | `checklists/content-qa.md` |
| `templates/` | Briefs, listings, trackers, reports, prompt specs | `templates/content-brief.md` |
| `schemas/` | JSON Schemas + JSON-LD library | `schemas/kit.schema.json` |
| `mcp/` | MCP configs, tool matrix, credential protocol | `mcp/README.md` |
| `scripts/` | Validation, prompt rendering, URL audit, sitemap check, dedupe | `scripts/validate_kit.py` |
| `data/` | Sources, tool matrix, 687-directory list, glossary | `data/directories.summary.md` |
| `examples/` | Filled examples for RocketClips, Byte Shop, Alias Browser, Cini Travels | `examples/01-rocketclips-silo.md` |
| `docs/` | How to use with AI, connect MCP, handle credentials | `docs/00-start-here.md` |

---

## Connect your tools

The kit never asks you to paste secrets into chat. It asks you to set environment variables or connect an MCP server. See [`mcp/README.md`](mcp/README.md) and [`docs/03-credentials-and-security.md`](docs/03-credentials-and-security.md).

| Tool | Best connection | Auth | Fallback |
|---|---|---|---|
| **Ubersuggest** | Official MCP connector | OAuth via MCP | CSV export |
| **AnswerThePublic** | MCP (where available) or public API | OAuth / API key | CSV export |
| **SpyFu** | Official REST API or community MCP | API key (Pro/Team) | CSV export |
| **Mangools** | Official REST API or MCP (where available) | `x-access-token` | CSV export |
| **Google Search Console** | API / MCP | OAuth | CSV export |
| **GA4** | API / MCP | OAuth | CSV export |

If a tool is not connected, the agent must say so and ask for a CSV or a manual export. It must never invent the missing data.

---

## Why this is different

- **Evidence rules, not vibes.** Every claim needs a source and a date, or it is cut. See [`data/evidence-rules.md`](data/evidence-rules.md).
- **Two checkpoints, not eight.** Approve the brief; approve the publish. Everything else runs.
- **No invented experience.** The kit forbids fabricated anecdotes, reviews, quotes, and "official" claims.
- **No "bypass AI detection."** Humanisation means specificity, proof, and editing — not evasion.
- **Credential safety.** Secrets live in `.env`, never in prompts, issues, or commits.
- **Machine-readable.** `kit.json` lists every capability, input, output, and tool requirement.
- **Agent-native.** `AGENTS.md`, `llms.txt`, `llms-full.txt`, and `SKILL.md` files.

---

## Repo map

```
.
├── AGENTS.md                 # the agent contract
├── BOOTSTRAP.md              # copy-paste prompt for any AI
├── CLAUDE.md                 # Claude Code entry point
├── kit.json                  # machine-readable manifest
├── llms.txt                  # agent index
├── llms-full.txt             # full agent context
├── skills/                   # 11 Agent Skills
├── prompts/                  # 12 master prompts
├── playbooks/                # 4 pipelines
├── checklists/               # QA gates and audits
├── templates/                # briefs, listings, trackers
├── schemas/                  # JSON Schema + JSON-LD
├── mcp/                      # MCP configs and tool matrix
├── scripts/                  # validation and utilities
├── data/                     # sources, tools, directories, glossary
├── examples/                 # filled examples
└── docs/                     # start here, AI usage, MCP, security
```

---

## 5-minute demo

```bash
# 1. Validate the kit
python scripts/validate_kit.py

# 2. Render the silo prompt
python scripts/render_prompt.py prompts/02-silo.md \
  --var keyword="AI video clipper for podcasters" \
  --var product_url="https://shop.bytevault.co.in/product/rocketclips-pro-ai-video-editor/" \
  --var brand="Byte Shop" \
  --var market="India"

# 3. Audit a URL
python scripts/audit_url.py https://aliasbrowser.com

# 4. Check a sitemap
python scripts/sitemap_check.py https://bytesherlock.com
```

---

## Share

Ready-to-post X and LinkedIn copy: [`docs/08-share-on-x.md`](docs/08-share-on-x.md).

## Contributing

Add a prompt, a skill, a checklist, or a tool adapter. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first. Every prompt needs frontmatter, variables, an output contract, and a QA gate. Every skill needs a `SKILL.md` with valid YAML.

---

## Credits

Built by **GEOwallah** ? AI Search & Local SEO Agency, Barrackpore, India.  
https://geowallah.com

Maintained by **harryroger798**. See [`CREDITS.md`](CREDITS.md) for the full list.

## License

- **Code** (scripts, schemas, configs): MIT — see [`LICENSE`](LICENSE).
- **Content** (playbooks, prompts, checklists, docs): CC BY 4.0 — see [`LICENSE-CONTENT`](LICENSE-CONTENT).

Use it, fork it, teach with it, ship it. Attribution is appreciated.

---

**Built on live audits of eight working sites** — Byte Shop, TextShift, Alias Browser, ShipChamber, Cini Travels, Emily's Pet Heaven, GEOwallah, ByteSherlock — and 25 dated sources. The mechanisms are durable; the numbers are dated. Re-verify before you quote.
