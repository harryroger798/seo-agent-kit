---
name: paid-social
description: Build a Facebook/Instagram campaign that drives qualified WhatsApp conversations or landing-page actions, with five creatives, one video, a message flow, and a measurement model. Use for digital products and local offers.
version: 1.0.0
license: MIT
allowed-tools: Read, Write
---

# Paid Social

## When to use

Use when the user has a clear offer, a real audience, and a destination (WhatsApp or landing page). Do not use it to “boost” a post with no offer.

## Inputs

| Variable | Required | What it is |
|---|---|---|
| `{{offer}}` | yes | What is sold, price, discount, guarantee |
| `{{audience}}` | yes | Country, age, interests, exclusions |
| `{{proof}}` | yes | Reviews, delivery proof, customer video |
| `{{destination}}` | yes | WhatsApp number or landing page |
| `{{budget}}` | yes | Daily budget and test window |

## Process

1. Choose the objective: WhatsApp conversations, leads, or sales.
2. Define the audience: broad, interest, lookalike, retargeting.
3. Write the offer in one sentence, with the delivery and validity terms.
4. Create five image concepts + one video concept.
5. Write three hooks per concept, two CTAs.
6. Build the WhatsApp/landing flow: greeting, qualify, quote, proof, close, deliver, follow-up.
7. Define the metrics: cost per conversation, qualified rate, close rate, AOV, ROAS, refund rate.
8. Set the weekly optimisation cadence.

## Output

- `campaign.md` — objective, audience, budget, placements, bidding.
- `creatives.md` — five image prompts + one video brief.
- `copy.md` — headlines, primary text, descriptions, CTAs.
- `flow.md` — WhatsApp/landing script.
- `measurement.md` — KPIs and review cadence.

## Compliance

- Only advertise products you are authorised to sell.
- State region, platform, delivery time, and validity.
- Do not use “official” or a publisher’s logo to imply endorsement.
- No fake countdowns, fake “only 2 left,” or fake reviews.
- WhatsApp opt-in must be explicit; no purchased lists.
- Honour the replacement/refund policy you advertise.

## QA

- [ ] Offer is true and deliverable.
- [ ] Audience and region defined.
- [ ] Five creatives + one video.
- [ ] No fake scarcity or discounts.
- [ ] WhatsApp opt-in explicit.
- [ ] Flow matches the ad.
- [ ] Delivery time and validity stated.
- [ ] Cost per conversation tracked.
- [ ] Weekly optimisation scheduled.

## References

- `prompts/09-paid-social.md`
- `playbooks/paid-social.md`
- `checklists/paid-social-qa.md`
- `templates/campaign-brief.md`
