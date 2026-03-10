---
name: ironman_subagent
description: Delegate plan tasks to subagents with strict packet scope and two-stage review (spec compliance, then code/quality). Use after an approved plan exists.
---

# Ironman Subagent Execution

Announce at start: "Using ironman_subagent."

Use this when tasks are parallelizable or too large for one linear pass.

## Protocol

1. Confirm approved plan.
2. Split into bounded task packets.
3. Dispatch one subagent per packet.
4. Run review stage A (spec compliance).
5. Run review stage B (quality and safety).
6. Merge only approved outputs.
7. Record evidence and checkpoint.

## Task packet template

```text
IRONMAN TASK PACKET
Objective:
Inputs:
Constraints:
Deliverable:
Verification:
Timeout:
```

## Review pipeline (mandatory)

1. Spec review
- Did output satisfy scope exactly?
- Any missing acceptance criteria?

2. Quality review
- Safety/risk issues?
- Maintainability and clarity?
- Regression risk?

If either review fails, return packet for revision.

## Safety rules

- No destructive actions without explicit approval.
- No outbound messaging/publishing without explicit approval.
- No overlapping edits to the same files in parallel packets.
- Require evidence artifacts from every packet.

## Evidence minimum

- changed files list,
- verification output,
- unresolved risks,
- recommended merge order.
