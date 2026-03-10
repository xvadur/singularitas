---
name: morning-brief
description: Build a high-signal morning brief (AI + business + geopolitics) for the previous 24h with clear actions, not generic news dumps.
---

# Morning Brief

## Default source priority

1. `natural20-api-brief` (AI domain)
2. targeted web search for geopolitics/business

## Output format

```text
MORNING BRIEF — YYYY-MM-DD

AI SIGNALS
- ...

BUSINESS / MARKET SIGNALS
- ...

GEOPOLITICS
- ...

WHAT MATTERS FOR XVADUR TODAY
- 3 concrete actions
```

## Rules

- Prioritize signal over volume.
- Max 10 bullets total before actions.
- Always end with actionable next steps.


## Execution flow (required)

1. Pull AI signals from `natural20-api-brief` first.
2. Fill gaps with targeted non-AI sources (business/geopolitics).
3. Produce one concise action layer for today.

If Natural20 is unavailable, state fallback explicitly in the brief.
