---
name: plan
description: Build a disciplined 4-step execution plan from a request; includes scope, risks, timeline, and validation.
metadata:
  {
    "openclaw": {
      "emoji": "🧭"
    }
  }
---

# Plan Command

Goal: convert user goal into a practical, reviewable plan before execution.

## Behavior
Given a plan request, return:

1. **Objective** (one precise sentence)
2. **Scope** (in/out)
3. **Assumptions** (max 5)
4. **Execution plan (4 steps):**
   - Step 1: discovery/inputs
   - Step 2: design/decision
   - Step 3: execution
   - Step 4: validation/review
5. **Risks + mitigations**
6. **Milestones** (time-boxed)
7. **Acceptance checklist**

## Format
- Prioritize directness.
- Keep to a single coherent plan block.
- Use numbered lists, no fluff.

## Constraint
- If request is too broad, ask 3 clarifying questions first and do not overplan.
