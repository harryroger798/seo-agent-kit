---
name: product-listing
description: Build a digital product listing that answers what it is, who it is for, what you get, how it arrives, how long it lasts, and why it is safe to buy. Use for software keys, subscriptions, templates, and digital goods.
version: 1.0.0
license: MIT
allowed-tools: Read, Write
---

# Product Listing

## When to use

Use when the user wants a product page, marketplace listing, or listing refresh for a digital product.

## Inputs

| Variable | Required | What it is |
|---|---|---|
| `{{product}}` | yes | Product name and what it does |
| `{{product_url}}` | yes | The canonical listing URL |
| `{{facts}}` | yes | Licence, delivery, validity, region, support |
| `{{competitors}}` | yes | 3–5 real alternatives |
| `{{proof}}` | yes | Screenshots, reviews, delivery proof |
| `{{images}}` | no | Existing assets; otherwise generate prompts |

## Process

1. Write the title: 60–70 characters, product + differentiator + audience.
2. Choose one focus keyphrase and 2–3 secondary.
3. Write the short description: 150–160 characters.
4. Write the long description: 800–1,500 words.
5. Build the comparison table with verified criteria.
6. Write 5–7 FAQs: delivery, validity, compatibility, refund, support.
7. Specify delivery time, validity, region, device limit.
8. Write the meta description, slug, category, and 5–7 tags.
9. Create the five-image set with prompt, ALT, title, description, ratio, placement.
10. Run the QA gate.

## Output

- `listing.md` — title, descriptions, comparison, FAQ, delivery, validity, meta, slug, tags.
- `images.md` — five prompts + metadata.
- `qa.md` — compliance and accuracy checks.

## Trust layer

Every listing must answer:

- What exactly do I get?
- How is it delivered?
- How long does it last?
- Will it work in my region?
- What if it fails?
- Are you authorised to sell it?

## Compliance

- Do not claim “official,” “authorised,” or “genuine” without proof.
- Do not sell accounts or keys in violation of the vendor’s terms.
- Do not use “lifetime” when you mean “until the vendor changes the plan.”
- Do not use fake discounts, reviews, or scarcity.
- Do not imply endorsement with another company’s trademark.

## QA

- [ ] Title 60–70 characters.
- [ ] Focus keyphrase in title, H1, first 100 words, meta.
- [ ] Short description 150–160 characters.
- [ ] Long description answers what/who/how/how long.
- [ ] Comparison table uses verified data.
- [ ] FAQ covers delivery, validity, compatibility, refund, support.
- [ ] Product schema matches visible facts.
- [ ] Five images with alt text.
- [ ] No fake reviews, discounts, or “official” claims.
- [ ] Support and policy pages linked.

## References

- `prompts/07-listing.md`
- `playbooks/listing-engine.md`
- `checklists/listing-qa.md`
- `templates/listing.md`
