# Prompt spec

Use this template when adding a prompt to `prompts/`.

```markdown
---
name: <kebab-case>
description: <one sentence: when to use, what it returns>
version: 1.0.0
inputs: [<variable>, <variable>]
outputs: [<artifact>, <artifact>]
requires: [<tool>, <tool>]
---

# <Title>

## When to use

## Inputs

| Variable | Required | What it is |
|---|---|---|

## Prompt

```text
ROLE
...
INPUT
...
TASK
...
RULES
...
OUTPUT
...
```

## Output

## QA

- [ ] ...

## References
```

## Rules

- Every variable in the prompt must be listed in `inputs`.
- Every output must be listed in `outputs`.
- Every tool dependency must be listed in `requires`.
- The prompt must include a "do not invent" rule.
- The prompt must include an output contract.
- The prompt must include a QA gate or reference one.
- No hardcoded year.
- No keyword density target.
- No "bypass AI detection."
