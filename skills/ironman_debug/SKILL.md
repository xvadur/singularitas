---
name: ironman_debug
description: Root-cause debugging protocol for repeatable fixes. Use when issues are unclear, intermittent, or recurring.
---

# Ironman Systematic Debugging

Announce at start: "Using ironman_debug."

## Protocol

1. Reproduce reliably
- Define exact reproduction steps.
- Capture expected vs actual behavior.

2. Instrument before fixing
- Add logs/metrics/checkpoints to isolate failure boundary.

3. Trace to source
- Follow data/control flow upstream until root cause is found.
- Do not patch symptoms first.

4. Smallest safe fix
- Apply minimal change at root cause.

5. Regression proof
- Verify original issue is gone.
- Add one regression test/check where possible.

## Stop conditions

Escalate when:
- issue cannot be reproduced,
- multiple root-cause candidates remain,
- fix impacts production-risk paths.

## Output format

```text
IRONMAN DEBUG REPORT
Issue:
Repro Steps:
Root Cause:
Fix Applied:
Verification Evidence:
Regression Guard:
Residual Risk:
```
