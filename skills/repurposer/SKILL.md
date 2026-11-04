---
name: repurposer
description: Turn one canonical article into platform-native posts for the three or four channels that fit the business. Use for distribution, social, newsletters, and video scripts.
version: 1.0.0
license: MIT
allowed-tools: Read, Write
---

# Repurposer

## When to use

Use after an article, listing, or report is published. Do not use it to cross-post the same paragraph everywhere.

## Inputs

| Variable | Required | What it is |
|---|---|---|
| `{{canonical}}` | yes | The published article or asset |
| `{{platforms}}` | yes | 3–4 platforms chosen by buyer fit |
| `{{cta}}` | yes | The one action per platform |
| `{{proof}}` | yes | The strongest number, quote, or visual |

## Platform fit

| Business | Core | Secondary | Skip |
|---|---|---|---|
| B2B SaaS | LinkedIn, X, Medium, YouTube | Reddit, newsletter | Pinterest, Tumblr |
| Local service | Facebook, Instagram, GBP, YouTube | WhatsApp status, local groups | X, Threads |
| E-commerce / digital goods | Instagram, Pinterest, YouTube, Facebook | X, Threads, Telegram | LinkedIn (unless B2B) |
| Agency / consultant | LinkedIn, YouTube, newsletter, X | Medium, podcast | Pinterest |

## Process

1. Choose 3–4 platforms. Explain why.
2. For each, write a native post: different hook, same facts.
3. Add one image prompt per visual platform, with ALT, title, description, ratio, placement.
4. Add the CTA that fits the platform.
5. Return a publishing calendar for the week.

## Output

```markdown
| Platform | Format | Hook | CTA | Metric | Effort |
|---|---|---|---|---|---|
```

Plus the post copy, image prompts, and a 5-day calendar.

## Rules

- Derivatives may change the hook, format, and length.
- They may not change the facts, price, links, or claim.
- One idea per post.
- No platform is used just because it exists.
- No fake urgency or engagement bait.

## QA

- [ ] Each post has a different hook.
- [ ] Facts, price, and links match the canonical asset.
- [ ] Format is native to the platform.
- [ ] CTA fits the platform’s behaviour.
- [ ] Image has alt text and a reason to exist.
- [ ] Post can stand alone.
- [ ] One metric per platform.

## References

- `prompts/06-repurpose.md`
- `playbooks/content-factory.md`
