# How to use with AI

## Claude Code

```bash
cd seo-agent-kit
claude
```

Claude Code reads `CLAUDE.md`, which points to `AGENTS.md`. Say:

> Read `AGENTS.md` and `skills/seo-orchestrator/SKILL.md`. Ask me the three intake questions.

## Cursor

1. Open the folder.
2. Add `.cursor/rules/seo-agent-kit.mdc` (or use `AGENTS.md` if your version reads it).
3. In Agent mode, say:

> Read `AGENTS.md`, `kit.json`, and `skills/seo-orchestrator/SKILL.md`. Ask me the three intake questions.

## Codex / OpenAI

Codex reads `AGENTS.md` from the repo root. Start with:

> Follow `AGENTS.md`. Read `kit.json` and `skills/seo-orchestrator/SKILL.md`. Ask me the three intake questions before doing anything.

## ChatGPT / Claude / Gemini (no repo access)

1. Attach the ZIP or paste `llms-full.txt`.
2. Paste the **Version B** prompt from `BOOTSTRAP.md`.
3. If the assistant cannot read files, paste one skill and one prompt at a time.

## OpenClaw / other agents

Use `AGENTS.md` as the root instruction. If the agent supports Agent Skills, point it at `skills/`. If it supports MCP, use `mcp/servers.example.json`.

## The standard session

```text
1. Intake: site, outcome, tools.
2. Route: one skill, one pipeline.
3. Brief: return for approval.
4. Execute: draft, build, or batch.
5. QA: pass/fail + [VERIFY] list.
6. Publish: return for approval.
7. Measure: one metric, one date.
```

## What to do when the agent goes off-contract

Paste:

```text
Stop. Re-read AGENTS.md section 4. Remove every unsourced claim, invented
anecdote, fake review, and unverified competitor statement. Mark what you
cannot verify as [VERIFY] and return the QA list.
```
