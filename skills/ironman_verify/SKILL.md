---
name: ironman_verify
description: Final evidence gate before saying work is done. Use to validate outputs, acceptance criteria, and system-of-record updates.
---

# Ironman Verification Before Completion

Run this before saying "done", "fixed", "ready", or "complete".

## Core law

No completion claim without fresh verification evidence.

## Verification checklist

1. Requirement match
- Goal and scope match approved plan.

2. Artifact existence
- Files/records/messages exist in the expected locations.

3. Functional proof
- Core flow tested with command/check output.

4. Ops sync
- CRM/Linear/Obsidian/memory updated if required by plan.

5. Risk note
- Remaining risk or follow-up explicitly listed.

## Claim-to-proof mapping

- "Tests pass" -> test command output with zero failing tests.
- "Build passes" -> build command output with exit 0.
- "Bug fixed" -> reproduction gone + regression check passed.
- "Campaign ready" -> draft artifacts + approval gate status.

## Output format

```text
IRONMAN FINAL VERIFY
Goal Match: PASS/FAIL
Artifacts: PASS/FAIL
Functional Proof: PASS/FAIL
Ops Sync: PASS/FAIL
Residual Risks:
Final Status: DONE / PARTIAL / BLOCKED
```

If any line is FAIL, return to execution with exact remediation tasks.
