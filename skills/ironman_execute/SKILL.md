---
name: ironman_execute
description: Execute approved plans in controlled batches with evidence checkpoints. Use for delivery work across Sales/Build/Ops/Content.
---

# Ironman Executing Plans

Announce at start: "Using ironman_execute."

## Execution protocol

1. Load approved plan and restate goal.
2. Execute first batch (default 2-3 tasks).
3. Verify each task immediately.
4. Publish checkpoint update.
5. Continue next batch.
6. Run final gate via `ironman_verify`.

## Mandatory checkpoint format

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

## Blocker policy

Stop and escalate if:
- missing credentials/access,
- contradictory requirements,
- risky external action requires approval,
- verification fails twice.

When blocked, provide exactly 2 recovery options.

## Non-negotiables

- Never claim success without evidence.
- Never run outbound publishing or external messaging without explicit approval.
- Keep updates concise and stateful.

## Completion

Only mark execution complete when:
- all tasks done or explicitly deferred,
- outputs exist,
- verification evidence exists,
- systems of record are updated as planned.

Then invoke `ironman_verify`.
