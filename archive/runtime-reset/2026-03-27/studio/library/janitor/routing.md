# Janitor Operator Routing Note

Use `janitor` as the owner lane when the request is primarily about system hygiene and drift-detection operations.

## Route to `janitor` for
- cleanup
- drift detection
- stale state review
- missing artifact checks
- hygiene audits

## Internal routing modes

- `HYGIENE_AUDIT`
- `CLEANUP_PACKET`
- `DRIFT_ALERT`
- `MISSING_RECORD`
- `STALE_SURFACE`
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
