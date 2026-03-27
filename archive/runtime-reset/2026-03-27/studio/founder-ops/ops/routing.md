# Ops Operator Routing Note

Use `ops` as the owner lane when the request is primarily about runtime operations and automation operations.

## Route to `ops` for
- ops runbooks
- runtime operations
- automation checks
- process hygiene
- system maintenance packets

## Internal routing modes

- `RUNBOOK`
- `OPS_CHECK`
- `AUTOMATION_REVIEW`
- `PROCESS_HYGIENE`
- `READINESS_SUMMARY`
- `ITERATION`

## Standard delegation packet

Every Jarvis handoff should include:
- Objective
- Context
- Constraints
- Requested output
- Verification requirement
- Urgency
- Stop condition

Reference example:
- `templates/delegation-packet-example.md`
