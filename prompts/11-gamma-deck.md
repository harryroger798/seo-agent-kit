---
name: gamma-deck
description: Generate a 20-slide teaching deck or a 10-slide workshop deck in Gamma from the playbook library.
version: 1.0.0
inputs: [audience, goal, outline]
outputs: [gamma_prompt, slide_outline, speaker_notes]
requires: [gamma]
---

# Gamma deck

## Prompt

```text
You are a presentation designer and SEO operator. Create a 20-slide deck
titled "The Operator's SEO Playbook 2026 — The Playbook Library".

AUDIENCE
{{audience}}

GOAL
{{goal}}

TONE
Direct, practical, slightly contrarian. No hype. No "in today's
fast-paced world." Plain English.

VISUAL STYLE
Editorial field manual: cream background, ink black, one burnt-orange
accent, serif headlines, sans-serif body. Clean diagrams, no stock
photos of people shaking hands. One idea per slide. Maximum 5 bullets
per slide. Maximum 12 words per bullet.

DECK OUTLINE
1. Title: The Playbook Library 2026
2. The problem: prompt collections are not systems
3. The operating map: four pipelines, one source of truth
4. The one rule: one canonical asset, many derivatives
5. The content factory: keyword to seven assets
6. The eight stages and the two checkpoints
7. The silo generator: five silos, one intent per page
8. The silo scorecard: demand, proof, winnability, conversion
9. The article brief: promise, proof, links, metric
10. The draft: answer-first, sourced, one product link
11. Humanise without lying: seven moves, no invented anecdotes
12. The repurposing matrix: core, secondary, skip
13. The digital product listing: anatomy and trust layer
14. The comparison table and the five-image set
15. The directory engine: seven steps, duplicate check first
16. Directory tiers: A, B, C, skip
17. Paid social: one campaign, five creatives, one WhatsApp flow
18. The prompt OS: role, context, input, constraints, process, output, QA
19. The fixes: what to delete from the old prompts
20. The 90-day rollout and the four KPIs

FOR EACH SLIDE
- A headline that makes the point, not a label.
- 3–5 short bullets, or one diagram.
- Speaker notes: 60–90 words, with one example from Byte Shop,
  TextShift, Alias Browser, ShipChamber, Cini Travels, Emily's Pet
  Heaven, GEOwallah, or ByteSherlock.
- A source line where a number appears.

CONSTRAINTS
- Do not invent statistics.
- Do not use emoji as icons.
- Do not use a wall of text.
- One idea per slide.
- End with one next step.

OUTPUT
Generate the deck in Gamma. Use the "presentation" format, 16:9,
professional theme. After generating, list the slides that need a
manual diagram and the slides that need a source check.
```

## 10-slide workshop version

Replace the outline with:

1. The four pipelines
2. The one source of truth
3. The silo: five questions
4. The brief: six fields
5. The draft: answer-first + three sources
6. The edit: seven humanisation moves
7. The repurpose: three platforms, three hooks
8. The QA gate: ten checks
9. The publish checklist
10. The next 7 days

Each slide: one exercise, one pass/fail criterion.
