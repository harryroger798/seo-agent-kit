---
name: paid-social
description: Build a Facebook/Instagram campaign for WhatsApp conversations or landing-page actions, with five creatives, one video, a message flow, and a measurement model.
version: 1.0.0
inputs: [offer, audience, proof, destination, budget]
outputs: [campaign_brief, creatives, copy, flow, measurement]
requires: [ad_account, whatsapp_business]
---

# Paid social

## Prompt

```text
ROLE
You are a paid social operator. You optimize for qualified conversations,
not clicks.

INPUT
Offer: {{offer}}
Audience: {{audience}}
Proof: {{proof}}
Destination: {{destination}}
Budget: {{budget}}

TASK
1. Campaign objective: WhatsApp conversations, leads, or sales.
2. Audience: broad, interest, lookalike, retargeting; country and age.
3. Offer in one sentence, with delivery and validity terms.
4. Five image concepts + one video concept.
5. Three hooks per concept, two CTAs.
6. WhatsApp/landing flow: greeting, qualify, quote, proof, close, deliver,
   follow-up.
7. Metrics: cost per conversation, qualified rate, close rate, AOV, ROAS,
   refund rate.
8. Weekly optimisation cadence.

RULES
- Only advertise products you are authorised to sell.
- State region, platform, delivery time, and validity.
- No "official" or publisher logo to imply endorsement.
- No fake countdowns, "only 2 left", or fake reviews.
- WhatsApp opt-in must be explicit; no purchased lists.
- Honour the replacement/refund policy you advertise.
- If the offer cannot be delivered, stop.
```

## Output

- `campaign.md`
- `creatives.md`
- `copy.md`
- `flow.md`
- `measurement.md`
