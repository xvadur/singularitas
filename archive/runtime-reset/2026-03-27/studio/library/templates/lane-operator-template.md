# Lane Operator Template

Use this contract to define a reusable lane surface in `studio/*` or a future specialized worker when Jarvis needs one bounded execution owner.

## Purpose

A lane operator is not founder-facing by default.
It is a specialized internal execution owner.
In the current runtime, its default home is `studio/*`, not a permanent live `agents/*` lane.
Jarvis routes work here when the request fits the lane.

## Required sections

### 1. Identity
State:
- agent or surface name
- lane/domain owned
- type of problems handled
- what the lane optimizes for

### 2. Mission
Define the core transformation the lane performs.
Pattern:
- turn raw founder intent into bounded, reviewable, execution-safe outputs inside one lane

### 3. Ownership
List exactly what the lane owns.
Prefer 5-8 bullet groups.

### 4. Non-ownership
List what is explicitly outside the lane.
This prevents drift.

### 5. Input types
List the request shapes Jarvis may route into this lane.

### 6. Internal routing modes
Define short internal task classes.
The lane should classify first, then execute the matching playbook.

### 7. Output contract
Every serious answer from the lane should use a stable output shape.
Recommended shape:
- Objective
- Interpreted request
- Scope
- What changed / recommendation
- Core artifact or patch
- Risks / placeholders
- Verification state
- Recommended next move

### 8. Verification standard
Define what evidence is required before claiming readiness, health, or completion.

### 9. Escalation rules
Define when the lane must escalate back to Jarvis.

### 10. Proactivity policy
Default for most lanes:
- no autonomy by default
- surface only real blockers, missing verification, stale critical work, or approval needs

## File pattern for each lane surface

Recommended minimal lane files:
- `README.md` → contract
- `status.md`
- `queue.md`
- `routing.md`
- `inventory/`
- `templates/`
- `daily/`

If the lane is only a reusable method surface, keep it under `studio/*`.
Only promote it into a live isolated agent workspace when the runtime truly needs that separate OpenClaw identity.
