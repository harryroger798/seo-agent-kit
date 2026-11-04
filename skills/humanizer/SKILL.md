---
name: humanizer
description: Edit AI-assisted copy for specificity, proof, rhythm, and point of view without inventing experience or promising to bypass detectors. Use on drafts that sound generic.
version: 1.0.0
license: MIT
allowed-tools: Read, Write
---

# Humanizer

## When to use

Use when a draft sounds generic, repetitive, or “AI-written.” Do not use it to fabricate anecdotes or to evade detection.

## The principle

Humanisation is not disguise. It is the addition of things a model cannot supply: real experience, specific numbers, named people, a decision, and a trade-off.

## The seven moves

1. **Specificity** — replace the category with a named thing.
2. **Constraint** — name the budget, time, or condition.
3. **Evidence** — add a number with a source and date.
4. **Point of view** — say what you would do, and why.
5. **Rhythm** — mix short and long sentences.
6. **Admission** — name a trade-off or a failure.
7. **Cut** — remove 20% without losing a fact.

## Process

1. Read the draft and mark every generic sentence.
2. Replace each with a specific fact, example, or decision.
3. Add one sourced statistic and one named quotation if missing.
4. Cut the warm-up, the summary, and the hedging.
5. Read aloud. Rewrite anything that sounds like a brochure.
6. Return the edited draft and a change log.

## Output

- `edited.md` — the cleaned copy.
- `changes.md` — what changed and why.

## AI tells to cut

- “In today's fast-paced world…”
- “It's important to note that…”
- “Delve into,” “unlock,” “seamless,” “robust”
- “Not only… but also…”
- “Moreover,” “furthermore,” “additionally” at every paragraph
- “The landscape of…”
- “Whether you're a… or a…”
- “In conclusion,” followed by a summary
- False balance: “However, it's essential to consider…”
- Empty superlatives: “revolutionary,” “game-changing”

## Do not

- Invent a personal anecdote.
- Add slang that does not fit the brand.
- Insert “I think” or “in my opinion” as filler.
- Claim first-hand testing you did not do.
- Promise to “bypass AI detection.”

## QA

- [ ] First 60 words answer the query.
- [ ] Every generic claim replaced with a specific one.
- [ ] At least three facts have a source and date.
- [ ] At least one trade-off or failure is named.
- [ ] No paragraph longer than four sentences.
- [ ] 20% of the words are gone.
- [ ] Nothing would embarrass the brand if a customer read it.

## References

- `prompts/05-edit.md`
- `playbooks/content-factory.md`
