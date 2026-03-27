---
name: fast
description: Execute in rapid-response mode with one-screen summary, decisive first step, and immediate next actions.
metadata:
  {
    "openclaw": {
      "emoji": "⚡"
    }
  }
---

# Fast Command

Goal: answer with compressed, execution-oriented response when user asks `/fast`.

## Behavior
When invoked, provide:

1. **Rapid diagnosis** (1–3 bullets): what user is trying to do.
2. **Fast mode decision** (clear do/don't for the next 15 minutes).
3. **Immediate action block** (0.5–3 concrete steps).
4. **Success criterion** (one measurable checkpoint).
5. **Stop condition** (when to switch to `/plan`).

## Output contract
- Keep it short. Prefer bullets, compact language.
- No long narrative.
- If task is risky/irreversible, explicitly state risk and one safer variant.
- End with a single direct question only if user needs a missing constraint.

## Constraint
- If user command is empty, ask:
  - "Čo presne dnes urgentné vyriešiť?"