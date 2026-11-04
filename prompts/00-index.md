# Prompt index

Twelve master prompts. Each has frontmatter with inputs, outputs, and tool requirements. Use `scripts/render_prompt.py` to fill the variables.

| # | Prompt | Use | Requires |
|---|---|---|---|
| 01 | [Intent & fan-out](01-intent-fanout.md) | Classify the query and list the questions around it | — |
| 02 | [Silo](02-silo.md) | Build the five-silo cluster | — |
| 03 | [Brief](03-brief.md) | Turn a silo row into a one-page brief | — |
| 04 | [Draft](04-draft.md) | Write the article from the brief | — |
| 05 | [Edit](05-edit.md) | Remove AI tells, add proof, cut 20% | — |
| 06 | [Repurpose](06-repurpose.md) | Create platform-native derivatives | — |
| 07 | [Listing](07-listing.md) | Build the product listing | — |
| 08 | [Directory](08-directory.md) | Build the submission brief and duplicate check | inbox |
| 09 | [Paid social](09-paid-social.md) | Build the campaign and creative matrix | ad account |
| 10 | [QA](10-qa.md) | Audit any output against the gate | — |
| 11 | [Gamma deck](11-gamma-deck.md) | Generate a teaching deck | Gamma |
| 12 | [Prompt audit](12-prompt-audit.md) | Audit and rewrite an existing prompt | — |

## The rules

- Cite or cut.
- No invented experience.
- No keyword density.
- One product link.
- Two checkpoints.
- No secrets in chat.

## Variables

`{{brand}}` · `{{product}}` · `{{product_url}}` · `{{keyword}}` · `{{buyer}}` · `{{market}}` · `{{proof_assets}}` · `{{internal_links}}` · `{{sources}}` · `{{current_year}}`
