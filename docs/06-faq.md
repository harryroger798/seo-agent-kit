# FAQ

## Is this a prompt pack?

No. It is a repo with skills, prompts, playbooks, checklists, templates, schemas, and tool adapters. The prompts are one layer.

## Do I need an MCP server?

No. The kit works with manual inputs and CSV exports. MCP makes it faster.

## Which tools are supported?

Ubersuggest, AnswerThePublic, SpyFu, Mangools, Google Search Console, and GA4. See `mcp/tool-matrix.md`.

## Do I need to pay for the tools?

The kit does not include tool subscriptions. Ubersuggest has a free tier; SpyFu and Mangools are paid; GSC and GA4 are free. Use the CSV fallback if you do not have a paid plan.

## Can I use this with ChatGPT?

Yes. Attach the ZIP or paste `llms-full.txt`, then use `BOOTSTRAP.md` Version B.

## Can I use this with Claude Code?

Yes. `CLAUDE.md` points to `AGENTS.md`; skills are in `skills/`.

## Can I use this with Cursor?

Yes. Open the folder, point Cursor at `AGENTS.md`, and optionally add `.cursor/mcp.json`.

## Does it work for local businesses?

Yes. Use `skills/local-seo/SKILL.md` and `checklists/local-seo.md`.

## Does it work for SaaS?

Yes. Use the content factory, AI visibility, and listing skills.

## Does it work for e-commerce?

Yes. Use the listing engine and the programmatic checklist in the technical audit.

## Is it safe to share?

Yes, if you remove `.env`, client data, and private exports. The validator scans for common secrets.

## Can I contribute?

Yes. Read `CONTRIBUTING.md`.

## Why no “bypass AI detection”?

Because it is an arms race, not a quality strategy. The kit humanises with specificity, proof, and editing. See `skills/humanizer/SKILL.md`.

## Why no keyword density?

Because it encourages stuffing. The kit uses entity and fan-out coverage.

## Why two checkpoints?

Because eight acknowledgements break the workflow. Approve the brief and the publish; let the agent run the middle.

## Where are the citations?

`data/sources.csv` and `templates/source-register.csv`. Every material claim in the playbooks has a source and a date.
