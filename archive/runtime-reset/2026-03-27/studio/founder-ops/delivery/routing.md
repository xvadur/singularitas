# Delivery Operator Routing Note

Use `delivery` as the owner lane when the request is primarily about delivery and rollout operations.

## Route to `delivery` for
- onboarding
- rollout status
- validation criteria
- deployment readiness
- scope drift
- handoff prep

## Internal routing modes

- `ONBOARDING`
- `ROLLOUT_PLAN`
- `VALIDATION`
- `READINESS_REVIEW`
- `SCOPE_CONTROL`
- `HANDOFF_PREP`
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
