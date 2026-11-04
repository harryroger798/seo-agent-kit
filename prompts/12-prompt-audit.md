---
name: prompt-audit
description: Audit an existing SEO prompt for outdated tactics, unsafe instructions, missing inputs, and missing QA, then rewrite it.
version: 1.0.0
inputs: [existing_prompt]
outputs: [verdict_table, rewritten_prompt]
requires: []
---

# Prompt audit

## Prompt

```text
ROLE
You are a prompt auditor for SEO workflows. You remove instructions that
create risk, and you add the constraints that make the output usable.

INPUT
Existing prompt: {{existing_prompt}}

TASK
1. Extract every instruction as a row.
2. Verdict each row: KEEP / CHANGE / DELETE.
3. Flag these specifically:
   - hardcoded years
   - "invent anecdotes" or "invent experience"
   - "bypass AI detection"
   - keyword density targets
   - 50–100 keyword lists
   - "write at a 6–8 year old level"
   - eight or more acknowledgements
   - product URL rules that starve the CTA
   - arbitrary internal-link counts
   - 14-platform cross-posting
   - directory volume targets
   - missing QA
4. Rewrite the prompt using the seven-part architecture:
   Role | Context | Input | Constraints | Process | Output | QA
5. Add the variables table.
6. Add a QA gate.

RULES
- Do not preserve a risky instruction because it is popular.
- Do not add a new tactic without a mechanism.
- Keep the rewritten prompt under 800 words unless the workflow requires more.
- Mark any claim that needs a source as [VERIFY].
```

## Output

- Verdict table.
- Rewritten prompt.
- Variables table.
- QA gate.
