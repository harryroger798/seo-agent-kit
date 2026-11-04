# Start here

## What this kit is

A public, agent-readable SEO operating system. It contains skills, prompts, playbooks, checklists, templates, schemas, and MCP/API adapters. It is designed to be read by an AI agent and executed with a human operator.

## The three ways to use it

### 1. Agent + repo

Open the repo in Claude Code, Cursor, Codex, Gemini CLI, Windsurf, or any agent that reads `AGENTS.md`.

Say:

> Read `AGENTS.md` and `kit.json`. Then read `skills/seo-orchestrator/SKILL.md` and ask me the three intake questions.

### 2. Agent + bootstrap

No repo access? Copy `BOOTSTRAP.md` into ChatGPT, Claude, Gemini, or any assistant. Attach the ZIP or paste `llms-full.txt`.

### 3. Manual

Every prompt is standalone. Use `scripts/render_prompt.py` to fill the variables, or copy the prompt and replace `{{...}}` manually.

## The three intake questions

1. **Site** — domain or product URL.
2. **Outcome** — traffic, citations, listings, conversations, or revenue.
3. **Tools** — Ubersuggest MCP, AnswerThePublic, SpyFu, Mangools, GSC, GA4, or manual/CSV.

## The two checkpoints

1. Approve the brief or plan.
2. Approve the publish or submit.

## The one rule

**Cite or cut.** If you cannot source it, write `[VERIFY]` and stop.

## What to read next

- `docs/01-how-to-use-with-ai.md` — tool-specific setup.
- `docs/02-connect-mcp.md` — MCP and API connections.
- `docs/03-credentials-and-security.md` — secret handling.
- `skills/seo-orchestrator/SKILL.md` — routing.
- `prompts/00-index.md` — the 12 prompts.
