---
name: directory-submission
description: Run a directory submission batch with a queue, brief, contact, inbox access, assets, duplicate check, submission, verification, and status tracking. Use for launch distribution and citations.
version: 1.0.0
license: MIT
allowed-tools: Read, Write, Bash
---

# Directory Submission

## When to use

Use when a site is queued for launch or authority building. Do not use it to submit to paid directories, badge-required directories, or spam lists.

## Inputs

| Variable | Required | What it is |
|---|---|---|
| `{{site}}` | yes | Domain and product URL |
| `{{brief}}` | yes | Tagline, short, long, category |
| `{{contact}}` | yes | Founder name and email |
| `{{inbox_access}}` | yes | How the verification email will be read |
| `{{assets}}` | yes | Logo, screenshots, demo video |
| `{{tracker}}` | yes | Directory tracker CSV |

## Process

1. Pick the next site with status `To do`; set `In progress`.
2. Write the brief: tagline ≤60 chars, short ≤160, long 120–200 words, category.
3. Verify the founder/contact. Never guess an email.
4. Test inbox access by reading one message.
5. Collect assets; capture missing screenshots.
6. For each directory, **duplicate-check first**:
   - `site:directory.com "yourdomain.com"`
   - search the product name
   - check the category page
7. If already listed: set `Already listed`, record URL, stop.
8. If not: submit once. Batch of 15, sorted by relevance and DR.
9. Click the confirmation email. Set `Live`. Record the listing URL.
10. Re-check after 90 days.

## Status taxonomy

`To do` · `In progress` · `Submitted` · `Live` · `Skipped` · `Failed` · `Already listed`

## Tiering

| Tier | Criteria | Batch |
|---|---|---|
| A | Relevant, editorial, real traffic, dofollow or strong referral | First 15 |
| B | Niche directories with real curation and a free tier | Next 30 |
| C | Low-cost citations; free, indexed, low traffic | Capped |
| Skip | Paid-only, badge required, dead, spam, irrelevant | Zero |

## Rules

- Free listings only.
- One site fully processed before the next.
- No duplicate submissions.
- No paid listings without explicit approval.
- No badge requirements unless approved.
- Record every status change immediately.

## QA

- [ ] Brief complete.
- [ ] Contact verified.
- [ ] Inbox tested.
- [ ] Assets uploaded.
- [ ] Duplicate check done first.
- [ ] Free tier only.
- [ ] Confirmation email clicked.
- [ ] Listing URL recorded.
- [ ] Status updated.
- [ ] 90-day re-check scheduled.

## References

- `prompts/08-directory.md`
- `playbooks/directory-engine.md`
- `checklists/directory-qa.md`
- `templates/directory-tracker.csv`
- `data/directory-seed.csv`
