# Contributing

## What to add

- A new prompt that fills a real gap.
- A new skill that routes a pipeline.
- A checklist that catches a failure.
- A tool adapter (MCP config or API script).
- A worked example with real inputs and outputs.

## Before you open a PR

1. Run `python scripts/validate_kit.py`.
2. Add or update the entry in `kit.json`.
3. Add the prompt to `prompts/00-index.md`.
4. Add the skill to `skills/` with valid YAML frontmatter.
5. Add the checklist or template to the right folder.
6. Update `CHANGELOG.md`.
7. Remove every secret, client name, and personal data.

## Prompt rules

- Frontmatter: `name`, `description`, `version`, `inputs`, `outputs`, `requires`.
- Variables in `{{snake_case}}`.
- A “do not invent” rule.
- An output contract.
- A QA gate or a reference to one.
- No hardcoded year.
- No keyword density target.
- No “bypass AI detection.”
- No fake reviews, scarcity, or “official” claims.

## Skill rules

- Folder name matches the `name` in frontmatter.
- Description says when to use it.
- Body: when to use, inputs, process, output, QA, references.
- No skill should require a secret in chat.

## Evidence rules

- Every statistic needs a source and a date.
- Label vendor research.
- Separate correlation from causation.
- Add the source to `data/sources.csv`.

## Review

A maintainer checks:

- Does it work on a real site?
- Does it follow `AGENTS.md`?
- Does it add a new capability, not a duplicate?
- Is it safe to publish?
