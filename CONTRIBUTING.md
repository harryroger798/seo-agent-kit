# Contributing

Read `docs/05-contributing.md` for the full guide.

## Quick version

1. Fork the repo.
2. Add a prompt, skill, checklist, template, or tool adapter.
3. Run `python scripts/validate_kit.py`.
4. Update `kit.json`, `prompts/00-index.md`, and `CHANGELOG.md`.
5. Open a PR with: what it adds, how you tested it, and what you removed.

## Rules

- Cite or cut.
- No invented experience, reviews, or “official” claims.
- No keyword density.
- No “bypass AI detection.”
- No secrets in commits.
- One canonical asset; derivatives change the hook, not the facts.

## Adding a prompt

Use `templates/prompt-spec.md`. Frontmatter must include `name`, `description`, `version`, `inputs`, `outputs`, `requires`.

## Adding a skill

Use an existing `skills/*/SKILL.md` as the model. Folder name must match the `name` in frontmatter.

## Adding a tool

Add a row to `mcp/tool-matrix.md` and `data/tool-matrix.csv`. Include: MCP, API, auth, fallback, and security notes.

## Code of conduct

See `CODE_OF_CONDUCT.md`.
