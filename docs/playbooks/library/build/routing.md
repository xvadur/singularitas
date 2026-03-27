# Build Operator Routing Note

Use `build` as the owner lane when the request is primarily about implementation and product build operations.

## Route to `build` for
- feature builds
- implementation planning
- technical patches
- code review packets
- build verification

## Internal routing modes

- `BUILD_PACKET`
- `PATCH`
- `IMPLEMENTATION_PLAN`
- `CODE_REVIEW`
- `VERIFY`
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
