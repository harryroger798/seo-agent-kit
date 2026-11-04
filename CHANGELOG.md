# Changelog

## 1.1.0 - 2026-11-04

### Added
- `blog-media` skill and prompt 13: featured image for OG/social (not the first body image), 2-4 in-body images, 5-7 FAQs, one video with transcript, 2-3 external citations, 3-5 internal links, key takeaways.
- `ai-interrogation` skill and prompt 14: ask AI "best [category] in [city]", then "why" and "where is [brand]", log the cited sources, fix them, and re-test in 7 days.
- `docs/11-field-notes.md`: 30 operating tips covering blog media, AI interrogation, the India citation stack, links, listings, and paid social.
- India citation stack: Justdial, Sulekha, IndiaMART after Google Business Profile.
- Templates for the blog media plan and the AI interrogation log.

### Changed
- Content QA now requires the media layer.
- Local QA now requires Justdial, Sulekha, and IndiaMART.
- AI visibility QA now requires the interrogation loop.
- `AGENTS.md` now includes content output requirements, local citation priority, and AI interrogation.

## 1.0.0 — 2026-11-04

First public release.

### Added
- 11 Agent Skills: orchestrator, silo, content factory, humanizer, repurposer, product listing, directory submission, paid social, AI visibility, technical audit, local SEO.
- 12 master prompts with frontmatter, variables, output contracts, and QA.
- 4 production playbooks: content, listing, directory, paid social, plus AI search.
- 7 checklists, including a 120-point audit.
- Templates for briefs, listings, trackers, campaigns, reports, prompts, and sources.
- JSON Schemas and a JSON-LD library.
- MCP/API examples and a tool matrix.
- Scripts: validate, render, audit, sitemap, AI panel, dedupe, ZIP.
- Data: sources, tools, directories, glossary, evidence rules.
- 4 worked examples: RocketClips, Byte Shop, Alias Browser, Cini Travels.
- Imported 687 directories from Notion; added a sanitized public list and summary.
- `AGENTS.md`, `BOOTSTRAP.md`, `CLAUDE.md`, `llms.txt`, `llms-full.txt`.

### Changed from the original prompt collection
- Removed hardcoded 2024.
- Removed “invent anecdotes.”
- Removed “bypass AI detection.”
- Removed keyword density targets.
- Reduced eight acknowledgements to two checkpoints.
- Replaced 14-platform cross-posting with a core/secondary/skip matrix.
- Tiered the 687-directory list; duplicate check first.
- Added compliance gates for digital listings and paid social.
