---
name: ironman-design
description: Project design and planning layer for Ironman. Use before executing non-trivial work to produce the approved brief, execution plan, risks, verification strategy, and rollback shape.
---

# Ironman Design

Use this before execution for any real project.

## Mandatory flow

1. Snapshot context
- what exists now
- what is broken/missing
- what done looks like

2. Clarify
- ask one high-leverage question at a time
- prefer scope, deadline, success metric, constraints

3. Offer approaches
- give 2-3 options when tradeoffs matter
- recommend one option clearly

4. Produce design brief

```text
IRONMAN DESIGN BRIEF
Goal:
Scope In:
Scope Out:
Chosen Approach:
Why This Approach:
Risks:
Verification Strategy:
Artifacts to Produce:
```

5. Get explicit approval
- do not execute before approval if the task is non-trivial or risky

6. Convert brief into plan

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

## Built-in modules

### Debug mode
Use root-cause debugging when issue is unclear, intermittent, or recurring:
- reproduce reliably
- instrument before fixing
- trace to source
- apply smallest safe fix
- prove regression protection

### Work isolation
Use branch/worktree discipline for medium or large build changes:
- confirm safe baseline
- isolate work
- verify before merge
- preserve rollback path

## Non-negotiables

- No implementation before approved design when risk is meaningful.
- No vague tasks in the plan.
- Every task needs verification and output.
