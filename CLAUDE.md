# CLAUDE.md

Claude Code reads this file instead of `AGENTS.md`. The full contract lives in [`AGENTS.md`](AGENTS.md). Read it first, then come back here for Claude-specific notes.

## Quick start

```text
Read AGENTS.md and kit.json. Then read skills/seo-orchestrator/SKILL.md.
Ask me the three intake questions before doing anything.
```

## Claude-specific notes

- Skills live in `skills/<name>/SKILL.md`. Read the one that matches the request; do not load all of them.
- Prompts live in `prompts/`. They use `{{variable}}` placeholders; use `scripts/render_prompt.py` or fill them manually.
- Use the `Read` tool for files, `Bash` for the scripts, and `Write` only when the operator asks you to create or update a deliverable.
- Never ask for an API key in chat. Ask the operator to set it in `.env` or connect the MCP server. See `mcp/README.md`.
- Stop at the two checkpoints: brief approval and publish approval.

## The three intake questions

1. Which site or product URL?
2. What is the one outcome for this sprint?
3. Which tools are connected: Ubersuggest MCP, AnswerThePublic, SpyFu, Mangools, GSC, GA4, or manual/CSV?

## The one rule

**Cite or cut.** If you cannot source it, write `[VERIFY]` and stop.
