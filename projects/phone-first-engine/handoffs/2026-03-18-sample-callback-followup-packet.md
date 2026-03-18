# Callback / Follow-up Packet

- Packet ID: `phone-2026-03-18-callback-01`
- Owner: `revenue`
- Supporting agents: `voice`, `integration`
- State: `sample live packet`
- Account: `realtor pilot lane`

## Trigger

Inbound phone-first pilot interest exists, but the callback and follow-up flow is not yet attached to a live CRM queue.

## Objective

Prepare the first callback/follow-up packet shape so tomorrow's vendor and pilot work can be captured without inventing a workflow.

## Inputs

- current wedge and engine status from `/Users/_xvadur/singularitas/projects/phone-first-engine/status.md`
- callback workflow contract from `/Users/_xvadur/singularitas/projects/phone-first-engine/spec/pilot-workflow.md`
- missing CRM signal from `/Users/_xvadur/singularitas/projects/founder-cockpit/spec/current-system-contracts.md`

## Proposed handling

1. use manual callback tracking until the CRM source is restored
2. log callback owner, promised next move, and follow-up due date in the deployment packet or founder queue
3. after SIP/vendor feasibility is confirmed, promote the callback path into n8n + CRM integration work

## Required fields

- lead/account name
- contact number
- source
- callback owner
- callback due time
- promised next move
- booking path
- blocker

## Current blocker

The expected local CRM SQLite database is missing, so no live callback queue can yet be derived from the CRM skill.

## Next move

Use this packet format for tomorrow's first real callback event if one occurs, then convert it into the canonical CRM object once the relationship memory layer is restored.
