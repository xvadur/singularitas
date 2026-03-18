# Deployment Packet

- Packet ID: `phone-2026-03-18-deploy-01`
- Owner: `delivery`
- Supporting agents: `voice`, `integration`, `revenue`
- State: `sample live packet`
- Offer wrapper: `phone-first pilot`

## Objective

Define the minimum deployable phone-first pilot path:

`prospect -> short call -> pilot proposal -> deployment -> validation -> expansion`

## Inputs

- `/Users/_xvadur/Xvadur Brand & Business/03 Offer/Pilot Packages and Pricing.md`
- `archive/cutover-2026-03-18/legacy-outputs/xvadur-ecommerce-outbound-engine-v1/`
- `/Users/_xvadur/singularitas/projects/phone-first-engine/spec/pilot-workflow.md`

## Required delivery steps

1. confirm buyer problem and pilot scope
2. confirm telephony path and carrier feasibility
3. shape the assistant behavior and handoff logic
4. define callback / booking / escalation behavior
5. produce validation criteria before go-live

## Blockers

- SIP trunk feasibility with Slovak vendors is still pending
- live Vapi credential visibility has not been confirmed in the runtime
- CRM-backed callback queue is not live

## Validation gate

This packet cannot move to `deployment ready` until:
- carrier feasibility is confirmed
- callback behavior is defined
- validation fields are attached

## Next move

Use tomorrow's vendor calls to clear the carrier blocker, then clone this packet into the first real client deployment home.
