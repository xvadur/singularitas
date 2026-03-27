# Delegation Packet Example — Jarvis -> `integration`

## Example 1 — inspect workflow health

### Objective
Inspect the current integration surface for a workflow and state the main risk before any live changes are made.

### Context
- The goal is runtime clarity, not immediate mutation.
- Use existing integration artifacts and lane status as the starting point.
- Founder needs a clean answer on what is confirmed vs unconfirmed.

### Constraints
- Prefer read-first inspection.
- Do not run risky writes without approval.
- Keep the answer founder-readable.

### Requested output
Return:
- current state
- what is confirmed
- what is unverified
- highest-risk gap
- safest next validation or repair step

### Verification requirement
Separate observed evidence from assumptions.

### Urgency
Normal

### Stop condition
Stop when Jarvis can summarize the runtime truth confidently.

---

## Example 2 — prepare an integration repair packet

### Objective
Prepare a bounded repair packet for a broken or unclear integration path.

### Context
- The path may involve webhook logic, booking glue, or CRM writes.
- The repair should preserve runtime legibility.
- Avoid unnecessary broad redesign.

### Constraints
- Patch only the failing or unclear layer.
- Keep external writes gated behind approval.
- Note dependencies owned by other lanes.

### Requested output
Return:
- interpreted problem
- scope of repair
- contract or workflow issue
- proposed patch / runbook
- risks
- validation steps
- recommended next move

### Verification requirement
Name what evidence would count as repaired.

### Urgency
High

### Stop condition
Stop when the repair packet is ready for execution approval.
