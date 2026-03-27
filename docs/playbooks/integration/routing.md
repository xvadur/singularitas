# Integration Routing Note

Use `integration` as the owner lane when the request is primarily about system glue, workflow execution, or runtime contracts between AI and external systems.

## Route to `integration` for

- n8n workflow design or repair
- webhook contract checks
- CRM write-path design or diagnosis
- booking / scheduling glue
- calendar integration behavior
- SIP / carrier / telephony connector questions
- external connector mapping and runtime contract clarity
- safe runtime-health inspection of integration surfaces

## Internal routing modes

- `WORKFLOW_BUILD`
- `WORKFLOW_AUDIT`
- `WEBHOOK_DIAGNOSIS`
- `CRM_GLUE`
- `BOOKING_GLUE`
- `CONNECTOR_MAPPING`
- `RUNTIME_HEALTH`
- `RUNBOOK_PREP`
- `ITERATION`
- `PORTFOLIO_HYGIENE`

## Route elsewhere when

- the real task is prompt behavior or voice-agent design → `voice`
- the real task is founder prioritization, scope arbitration, or cross-lane sequencing → `main`
- the real task is client rollout, deployment governance, or onboarding readiness → `delivery`
- the real task is sales follow-up, lead state, or outreach logic → `revenue`

## Standard delegation packet

Every Jarvis → `integration` handoff should include:
- Objective
- Context
- Constraints
- Requested output
- Verification requirement
- Urgency
- Stop condition

Reference example:
- `templates/delegation-packet-example.md`
