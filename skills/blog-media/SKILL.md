---
name: blog-media
description: Add the media and conversion layer to a blog post: one featured image for social/OG, different in-body images, an FAQ, a video with transcript, external citations, internal links, and key takeaways. Use after the draft, before publishing.
version: 1.0.0
license: MIT
allowed-tools: Read, Write
---

# Blog Media

## When to use

Use after `content-factory` has produced a draft and before the QA gate. This skill turns a text page into a page a human trusts and an AI can quote.

## Inputs

| Variable | Required | What it is |
|---|---|---|
| `{{article}}` | yes | The draft or published article |
| `{{keyword}}` | yes | The primary query |
| `{{product_url}}` | yes | The one product link |
| `{{sources}}` | yes | 2–3 primary external sources |
| `{{internal_links}}` | yes | 3–5 validated URLs |
| `{{video_url}}` | no | A relevant video; otherwise propose one |
| `{{photos}}` | no | Real photos or screenshots; otherwise prompt for them |

## The media rule

**The featured image is not the first image in the body.**

The featured image is for the Open Graph card, social sharing, and the blog index. It should be 1200×630 (16:9), under 200 KB, with alt text. It should **not** be placed at the top of the article body.

Use different images inside the article, placed naturally:

1. After the intro: a real photo, screenshot, or diagram.
2. Inside a step or how-to section: a close-up of the action.
3. Near the comparison: a table, annotated screenshot, or before/after.
4. Before the FAQ: a simple visual that resolves the last objection.

## Process

1. Define the featured image: prompt or asset, ALT, title, description, 1200×630.
2. Plan 2–4 in-body images: asset, ALT, caption, placement, ratio.
3. Add 5–7 FAQs from the fan-out. Each answer is 40–60 words.
4. Add one video: embed URL, transcript, VideoObject schema, placement below the intro or in the how-to.
5. Add 2–3 primary external citations, inline, with the claim they support.
6. Add 3–5 internal links with descriptive anchors; link up to the money page.
7. Add a key-takeaways box with 3 bullets.
8. Confirm the author, published date, and last-updated date are visible.
9. Return the media plan table and the HTML snippets.

## Output

```markdown
| Asset | Prompt / URL | ALT | Caption | Placement | Ratio | Schema |
|---|---|---|---|---|---|---|
| Featured | | | | OG / social / blog card, not body | 16:9 | ImageObject |
| Body 1 | | | | After intro | 4:3 | ImageObject |
| Body 2 | | | | How-to step | 16:9 | ImageObject |
| Body 3 | | | | Comparison | 4:3 | ImageObject |
| Video | | | | Below intro | 16:9 | VideoObject |
```

Plus:

- FAQ HTML block.
- Key-takeaways HTML block.
- Citation list.
- Internal-link list.

## Rules

- No text inside images. Models garble it and buyers do not read it.
- No stock photos when a real photo exists.
- No fake video, fake transcript, or fake FAQ.
- Alt text describes the image, not a keyword dump.
- The featured image is not the first body image.
- Every image has a reason to exist.
- Compress to WebP or AVIF; set width and height.
- Lazy-load below the fold; do not lazy-load the LCP image.

## QA

- [ ] Featured image 1200×630, under 200 KB, with ALT.
- [ ] Featured image is not the first body image.
- [ ] 2–4 different in-body images.
- [ ] Every image has ALT, caption, and placement.
- [ ] 5–7 real FAQs, 40–60 word answers.
- [ ] FAQ is visible on the page.
- [ ] One video with transcript and VideoObject schema.
- [ ] 2–3 primary external citations.
- [ ] 3–5 internal links with descriptive anchors.
- [ ] Key takeaways box.
- [ ] Author, published date, last-updated date.
- [ ] No text inside images.

## References

- `prompts/13-blog-media.md`
- `playbooks/content-factory.md`
- `checklists/content-qa.md`
- `templates/blog-media-plan.md`
