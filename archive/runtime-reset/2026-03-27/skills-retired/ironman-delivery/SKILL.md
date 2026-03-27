---
name: ironman-delivery
description: Execution, delegation, checkpoints, and final verification layer for Ironman. Use after an approved design/plan exists to run work in batches, delegate packets when useful, and close only with evidence.
---

# Ironman Delivery

Use this after the plan is approved.

## Execution protocol

1. Restate goal and batch.
2. Execute 2-3 tasks.
3. Verify immediately.
4. Publish concise checkpoint.
5. Continue or escalate blockers.
6. Run final verification before claiming done.

## Checkpoint format

```text
IRONMAN CHECKPOINT
Completed:
- ...
Verification Evidence:
- ...
Blocked:
- ...
Next Batch:
- ...
```

## Delegation rule

If work is parallelizable or too large for one pass, split into packets and delegate.

```text
IRONMAN TASK PACKET
Objective:
Inputs:
Constraints:
Deliverable:
Verification:
Timeout:
```

For delegated work, require two reviews:
1. spec compliance
2. quality/safety

Do not merge outputs that fail either review.

## Final verification law

No completion claim without fresh evidence.

```text
IRONMAN FINAL VERIFY
Goal Match: PASS/FAIL
Artifacts: PASS/FAIL
Functional Proof: PASS/FAIL
Ops Sync: PASS/FAIL
Residual Risks:
Final Status: DONE / PARTIAL / BLOCKED
```

## Blocker policy

Stop and escalate when:
- access is missing,
- requirements conflict,
- risky external action needs approval,
- verification fails twice.

When blocked, give exactly 2 recovery options.
