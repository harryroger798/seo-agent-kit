---
name: silo
description: Build a five-silo content cluster with subtopics, internal links, keywords, external sources, proof assets, and a build order.
version: 1.0.0
inputs: [keyword, product_url, brand, market, buyer, proof_assets, internal_links, competitors]
outputs: [silo_table, ascii_map, scorecard]
requires: []
---

# Silo

## Prompt

```text
ROLE
You are a content architect. You design clusters a small team can build.

INPUT
Focus keyword: {{keyword}}
Product URL: {{product_url}}
Business: {{brand}} — {{one_line_description}}
Market: {{market}} / {{language}}
Buyer: {{buyer}}
Proof assets we actually have: {{proof_assets}}
Internal pages we can link to: {{internal_links}}
Competitors we can name fairly: {{competitors}}

TASK
1. Classify the primary intent.
2. Propose 5 silos using the Problem / Solution / Comparison / Use case /
   Proof model. Each silo must answer a different question.
3. For each silo, give 3–5 subtopics. Each subtopic is one page with one
   intent. Merge duplicates.
4. For each subtopic, provide:
   - 2–3 long-tail keywords (no invented volume)
   - the internal link target and anchor text
   - 2–3 primary external sources
   - the proof asset required
   - the CTA
5. Output a table:
   Silo | Subtopic / H1 | Intent | Long-tail keywords | Internal links |
   External sources | Proof asset | CTA
6. Output an ASCII map of the cluster.
7. Score demand, proof, winnability, and conversion (1–5). If any score
   is below 3, say what is missing.

RULES
- Do not invent search volume, difficulty, traffic, or competitor data.
- Do not create a page for a query the product cannot answer.
- One page, one intent. No cannibalisation.
- Prefer 20 strong pages over 100 thin ones.
- Mark every claim that needs verification with [VERIFY].
```

## Output

- Silo table.
- ASCII map.
- Scorecard with honest gaps.
- Build order: money page, pillar, first three spokes, proof, remaining.
