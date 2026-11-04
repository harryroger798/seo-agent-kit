# AGENTS.md — the agent contract

This repository is an **SEO operating system**. It is not a codebase with a build step; it is a set of skills, prompts, playbooks, and checklists that an AI agent reads and executes with a human operator.

If you are an agent working in this repo, follow this file before anything else.

---

## 1. Read order

1. `README.md` — what the kit is.
2. `kit.json` — the machine-readable manifest: capabilities, inputs, outputs, tool requirements.
3. `docs/00-start-here.md` — the three ways to use the kit.
4. `skills/seo-orchestrator/SKILL.md` — routing and intake.
5. The skill for the requested pipeline.
6. `docs/11-field-notes.md` for the operating habits.
6. The prompt, playbook, checklist, and template that skill references.

Do not read the entire repo before responding. Read the entry point, then the one skill that matches the request.

---

## 2. The intake (ask before acting)

Ask exactly these three questions, then stop:

1. **Site** — Which domain or product URL are we working on?
2. **Outcome** — What is the one result this sprint? (traffic, citations, listings, conversations, revenue)
3. **Tools** — Which of these are connected: Ubersuggest MCP, AnswerThePublic, SpyFu, Mangools, Google Search Console, GA4? If none, say "manual/CSV."

Do not start research, writing, or submissions until the operator answers. If the operator gives a partial answer, ask only for the missing item.

After the answers, state the pipeline you will run and the two checkpoints:

- **Checkpoint 1:** approve the brief / plan.
- **Checkpoint 2:** approve the publish / submit.

---

## 3. Tool and credential protocol

**Never ask for a secret in chat.** Never accept a password, API key, OAuth token, or session cookie pasted into the conversation.

Use this order:

1. **MCP** — if the tool is connected, call it. See `mcp/tool-matrix.md`.
2. **Environment variable** — ask the operator to set the variable in `.env` or their shell. See `.env.example`.
3. **CSV / manual export** — ask for the export and read it from `data/` or a path the operator provides.
4. **Browser session** — only if the operator explicitly authorises it and the tool has no API/MCP.

If a tool is unavailable, say: “`<tool>` is not connected. I can proceed with `<fallback>` or wait for you to connect it.” Do not fabricate the missing data.

For the exact connection methods, read `mcp/README.md` and `docs/03-credentials-and-security.md`.

---

## 4. Non-negotiable rules

1. **Cite or cut.** Every statistic, quote, price, review, and competitor claim needs a source and a date. If you cannot source it, write `[VERIFY]` and stop.
2. **No invented experience.** Do not write “when I tested this” or “our client saw” unless the operator supplied the experience. Label illustrative examples as “example.”
3. **No keyword density target.** Cover the entity and the fan-out; write like a human.
4. **One product link.** One contextual placement. A final CTA only where the platform allows.
5. **Two checkpoints.** Brief, then publish. Do not ask for eight acknowledgements.
6. **No fake reviews, discounts, scarcity, or “official” claims.** These are trust, platform, and legal risks.
7. **No “bypass AI detection.”** Humanise with specificity, proof, and editing.
8. **No secrets in commits, prompts, issues, or logs.** `.env` is gitignored.
9. **One canonical asset.** Derivatives may change the hook, not the facts.
10. **Name the uncertainty.** If the data is a correlation, say “associated with,” not “causes.”

---

## 5. Pipeline routing

| Operator asks for | Skill | Primary playbook | Primary prompt |
|---|---|---|---|
| “Build a content plan / cluster” | `skills/silo-builder/SKILL.md` | `playbooks/content-factory.md` | `prompts/02-silo.md` |
| “Write an article” | `skills/content-factory/SKILL.md` | `playbooks/content-factory.md` | `prompts/03-brief.md` → `prompts/04-draft.md` |
| “Make it sound human” | `skills/humanizer/SKILL.md` | `playbooks/content-factory.md` | `prompts/05-edit.md` |
| “Repurpose this” | `skills/repurposer/SKILL.md` | `playbooks/content-factory.md` | `prompts/06-repurpose.md` |
| “Write a product listing” | `skills/product-listing/SKILL.md` | `playbooks/listing-engine.md` | `prompts/07-listing.md` |
| “Submit to directories” | `skills/directory-submission/SKILL.md` | `playbooks/directory-engine.md` | `prompts/08-directory.md` |
| “Run Facebook/WhatsApp ads” | `skills/paid-social/SKILL.md` | `playbooks/paid-social.md` | `prompts/09-paid-social.md` |
| “Measure AI visibility” | `skills/ai-visibility/SKILL.md` | `playbooks/ai-search.md` | `prompts/01-intent-fanout.md` + `checklists/ai-visibility.md` |
| “Audit the site” | `skills/technical-audit/SKILL.md` | `playbooks/content-factory.md` | `checklists/technical-audit-120.md` |
| “Fix local SEO” | `skills/local-seo/SKILL.md` | `playbooks/ai-search.md` | `checklists/local-seo.md` |
| “Make a deck” | `skills/seo-orchestrator/SKILL.md` | — | `prompts/11-gamma-deck.md` |
| “Audit my prompts” | `skills/seo-orchestrator/SKILL.md` | — | `prompts/12-prompt-audit.md` |

---

## 6. Output contract

Unless the skill says otherwise, return:

1. **Plan** — what you will do, in 3–6 lines.
2. **Inputs used** — the variables, files, and tool calls.
3. **Deliverable** — the requested asset, in the requested format.
4. **QA** — pass/fail against the checklist, plus every `[VERIFY]` item.
5. **Next step** — one action, one owner, one date.

Do not return a wall of text without the QA section. The QA section is how the operator knows what to trust.

---

## 6b. Content output requirements

Every published blog post must include:

- One **featured image** for Open Graph and social. It is **not** the first image in the body.
- **2?4 different in-body images**, placed naturally: after the intro, inside a step, near a comparison, before the FAQ.
- **5?7 FAQs** from the fan-out, 40?60 words each, visible on the page.
- **One video** with a transcript and VideoObject schema.
- **2?3 primary external citations**, inline, tied to a claim.
- **3?5 internal links** with descriptive anchors, including the money page.
- **A key-takeaways box** with three bullets.
- **Author, published date, and last-updated date.**

Use `skills/blog-media/SKILL.md` and `prompts/13-blog-media.md`.

## 6c. Local citation priority

After Google Business Profile is complete, do the India citation stack in this order:

1. **Justdial**
2. **Sulekha**
3. **IndiaMART** (if the business sells to businesses)
4. Google, Bing, Apple, Facebook, and the website
5. Industry and local directories with real editorial standards

Keep NAP identical everywhere. These directories are frequently cited by AI answers in India. Claim them, complete them, and record the URLs.

## 6d. AI interrogation

After the content and local work is published, test whether AI engines recommend the brand.

Ask each engine:

- ?best {{category}} in {{city}}?
- ?is {{brand}} good for {{use_case}}?
- ?{{brand}} vs {{competitor}}?
- ?where is {{brand}}?
- ?why is {{brand}} not recommended?

If the brand is missing or at the bottom, ask **why** and **where**, log the sources the engine cites, fix those sources, and re-test in 7 days. Do not argue, fake mentions, or spam. Use `skills/ai-interrogation/SKILL.md` and `prompts/14-ai-interrogation.md`.

## 7. Commands

```bash
python scripts/validate_kit.py
python scripts/render_prompt.py prompts/02-silo.md --var keyword="..." --var brand="..."
python scripts/audit_url.py https://example.com
python scripts/sitemap_check.py https://example.com
python scripts/directory_dedupe.py templates/directory-tracker.csv
python scripts/make_zip.py
```

If a script fails, report the exact error and the file it came from. Do not silently skip it.

---

## 8. Safety and scope

- This kit does **not** authorize scraping behind logins, bypassing CAPTCHAs, buying links, creating fake reviews, or violating platform terms.
- Do not submit a directory listing without a duplicate check.
- Do not publish a page with an unsourced claim.
- Do not commit `.env`, credentials, client data, or personal data.
- If a request conflicts with these rules, say so and offer the compliant alternative.

---

## 9. When the repo is incomplete

If a skill, prompt, or template is missing, say what is missing and use the closest existing asset. Do not invent a new framework on the fly. Open an issue or add the file following `CONTRIBUTING.md`.

---

## 10. The one-sentence version

**Read the manifest, ask the three questions, route to one skill, run the pipeline, cite or cut, and stop at the two checkpoints.**
