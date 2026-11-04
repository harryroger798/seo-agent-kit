---
name: silo-builder
description: Build a five-silo content cluster from a money page and the questions a buyer asks before converting. Use for content plans, topical maps, cluster architecture, and internal-link planning.
version: 1.0.0
license: MIT
allowed-tools: Read, Write
---

# Silo Builder

## When to use

Use when the user asks for a content plan, topic cluster, silo, content map, or “what should we write?” Do not use it to write the pages; use `content-factory` for that.

## Inputs

| Variable | Required | What it is |
|---|---|---|
| `{{keyword}}` | yes | The primary query, not a keyword list |
| `{{product_url}}` | yes | The one page that converts |
| `{{brand}}` | yes | Business name and one-line description |
| `{{market}}` | yes | Country, language, currency |
| `{{buyer}}` | yes | Role, objection, what they already tried |
| `{{proof_assets}}` | yes | Data, cases, reviews, screenshots |
| `{{internal_links}}` | yes | Pages that already exist and can be linked |
| `{{competitors}}` | no | Competitors you can name fairly |

## Process

1. Classify the primary intent: informational, commercial, transactional, navigational, local.
2. Propose **five silos**: Problem, Solution, Comparison, Use case, Proof.
3. For each silo, give **3–5 subtopics**. One page, one intent. Merge duplicates.
4. For each subtopic, specify:
   - 2–3 long-tail keywords (no invented volume)
   - the internal link target and anchor
   - 2–3 primary external sources
   - the proof asset required
   - the CTA
5. Output the table, then an ASCII map, then a scorecard.
6. Score demand, proof, winnability, conversion (1–5). If any is below 3, say what is missing.

## Output

```markdown
| Silo | Subtopic / H1 | Intent | Long-tail keywords | Internal links | External sources | Proof asset | CTA |
|---|---|---|---|---|---|---|---|

```text
<ASCII map>
```

| Dimension | Score | Why |
|---|---|---|
| Demand | /5 | |
| Proof | /5 | |
| Winnability | /5 | |
| Conversion | /5 | |
```

## Rules

- Do not invent search volume, difficulty, traffic, or competitor data.
- Do not create a page for a query the product cannot answer.
- One page, one intent. No cannibalisation.
- Prefer 20 strong pages over 100 thin ones.
- Mark every claim that needs verification with `[VERIFY]`.

## QA

- [ ] Five silos, each a different question.
- [ ] Every subtopic has one intent and one proof asset.
- [ ] Every money page is reachable in three clicks.
- [ ] No two subtopics target the same query.
- [ ] The scorecard is honest; anything below 3 is called out.
- [ ] No invented numbers or competitor claims.

## References

- `prompts/02-silo.md`
- `playbooks/content-factory.md`
- `examples/01-rocketclips-silo.md`
