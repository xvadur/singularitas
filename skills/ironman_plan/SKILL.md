---
name: ironman_plan
description: Convert an approved design into an executable step-by-step plan with verification and rollback. Use after brainstorming approval and before execution.
---

# Ironman Writing Plans

Announce at start: "Using ironman_plan."

## Inputs required

- Approved design brief
- Lane: Sales, Build, Ops, or Content
- Time budget (sprint block)

## Plan rules

- Max 7 tasks per sprint plan.
- Each task must be 2-15 minutes.
- Each task must produce a visible output.
- No vague tasks ("improve", "optimize", "clean up").

## Mandatory plan format

```text
IRONMAN EXECUTION PLAN
Goal:
Lane:
Sprint Block:

Task N: <name>
- Action:
- Systems:
- Verification:
- Output:
- Rollback:

Dependencies:
Stop Conditions:
Final Deliverables:
```

## Quality bar

- Verification must be concrete command/check/result.
- Rollback must be explicit for any external/state-changing step.
- Include approval gates before outbound messages, production writes, or destructive actions.

## Storage path

Save plan to:
`/Users/_xvadur/singularitas/reports/plans/YYYY-MM-DD-<topic>-plan.md`

## Handoff

After plan approval, choose one execution path:

1. `ironman_execute` (sequential batches)
2. `ironman_subagent` (parallelizable or long tasks)
