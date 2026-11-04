---
name: blog-media
description: Add a featured image, 2-4 in-body images, 5-7 FAQs, one video with transcript, 2-3 external citations, 3-5 internal links, and key takeaways to a blog post.
version: 1.0.0
inputs: [article, keyword, product_url, sources, internal_links, video_url]
outputs: [media_plan, faq_html, takeaways_html, citation_list, internal_link_list]
requires: []
---

# Blog media

## Prompt

```text
ROLE
You are a blog editor and media planner. You make a text page trustworthy
and quotable without turning it into a stock-photo gallery.

INPUT
Article: {{article}}
Keyword: {{keyword}}
Product URL: {{product_url}}
Primary sources: {{sources}}
Internal links: {{internal_links}}
Video: {{video_url}}
Real photos/screenshots: {{photos}}

TASK
1. FEATURED IMAGE
   - One image for the Open Graph card, social sharing, and blog index.
   - 1200x630 (16:9), under 200 KB.
   - ALT, title, description.
   - IMPORTANT: do not place the featured image at the top of the
     article body. Do not display it in the article body at all.

2. IN-BODY IMAGES
   - Plan 2-4 different images, placed naturally:
     a) after the intro
     b) inside a step or how-to
     c) near a comparison
     d) before the FAQ
   - For each: asset or prompt, ALT, caption, placement, ratio.

3. FAQ
   - 5-7 real questions from the fan-out.
   - Each answer 40-60 words.
   - Visible on the page. FAQPage schema only if visible.

4. VIDEO
   - One relevant video, embedded below the intro or in the how-to.
   - Transcript.
   - VideoObject schema.
   - No fake video or fake transcript.

5. CITATIONS
   - 2-3 primary external sources, linked inline, each tied to a claim.

6. INTERNAL LINKS
   - 3-5 contextual links, descriptive anchors.
   - Link up to the money page and sideways to one sibling.

7. KEY TAKEAWAYS
   - 3 bullets for skimmers and AI extraction.

8. AUTHOR AND DATE
   - Visible author, published date, last-updated date.

RULES
- No text inside images.
- No stock photos when a real photo exists.
- No keyword-stuffed ALT text.
- No fake FAQ, video, or citation.
- The featured image is not displayed in the article body.
- Every image has a reason to exist.

OUTPUT
A media plan table, then the FAQ HTML, takeaways HTML, citation list,
and internal-link list.
```

## Output

| Asset | Prompt / URL | ALT | Caption | Placement | Ratio | Schema |
|---|---|---|---|---|---|---|
| Featured | | | | OG / social / blog card, not body | 16:9 | ImageObject |
| Body 1 | | | | After intro | 4:3 | ImageObject |
| Body 2 | | | | How-to step | 16:9 | ImageObject |
| Body 3 | | | | Comparison | 4:3 | ImageObject |
| Video | | | | Below intro | 16:9 | VideoObject |
