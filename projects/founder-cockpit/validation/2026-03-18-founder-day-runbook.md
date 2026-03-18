# 2026-03-18 Founder Day Runbook

## Purpose

This runbook is the first practical morning loop for Jarvis.
The goal is not to redesign the system. The goal is to execute one founder morning end-to-end without reconstructing context by hand.

If this loop works, the workbench is usable.

## Open Order

Open these surfaces in this order:

1. [Founder Cockpit](/Users/_xvadur/firma/briefings/founder-cockpit.md)
2. [Founder Briefing](/Users/_xvadur/firma/briefings/2026-03-18-founder-briefing.md)
3. [Active Execution Queue](/Users/_xvadur/firma/briefings/2026-03-18-active-execution-queue.md)
4. [Web / Proof Approval Packet](/Users/_xvadur/firma/approvals/2026-03-18-web-proof-approval-packet.md)
5. [Current Roadmap](/Users/_xvadur/firma/roadmap/current.md)
6. [Jarvis Usability Checklist v1](/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-jarvis-usability-checklist-v1.md)

This order matters:
- founder cockpit first
- daily truth second
- execution third
- approvals fourth
- roadmap fifth
- test contract last

## Message Order

Send these messages in sequence.

### 1. Live ingress check

Send:
`ping jarvis live ingress 2026-03-18`

Expected result:
- Jarvis lands in `main`
- reply is short and verdict-first
- reply reflects current founder-cockpit state

Pass if:
- the response names the active control surface or current state
- the response does not sound like a legacy bot

Fail if:
- no reply arrives
- the wrong agent answers
- the reply ignores the current founder cockpit

### 2. Context check

Send:
`what did you read on startup and what is the default founder briefing surface?`

Expected result:
- Jarvis names the startup reads
- Jarvis names `/Users/_xvadur/firma/briefings/founder-cockpit.md`
- Jarvis names `/Users/_xvadur/firma` as the business source of truth
- Jarvis distinguishes runtime trace from business truth

Pass if:
- the answer matches the startup contract and the authority matrix

Fail if:
- it handwaves the read order
- it confuses `singularitas` and `firma`

### 3. Capture pass

Send:
`capture: Jakub chce callback v piatok po 14:00. Zajtra mi pripomeň follow-up.`

Expected result:
- Jarvis classifies this as `capture`
- Jarvis states the owner, usually `revenue`
- Jarvis says where the note or reminder was written

Pass if:
- the input is preserved with minimal transformation
- the output says which system got the capture

Fail if:
- the message is treated as a decision
- the message is over-processed into a strategy memo

### 4. Decide pass

Send:
`decide: čo je dnes z founder cockpitu skutočne dôležité?`

Expected result:
- Jarvis returns 1-3 priorities only
- Jarvis names the main blocker if one dominates
- Jarvis gives one best next move

Pass if:
- the answer is compressed and actionable
- no long dump, no vague recap

Fail if:
- the answer lists everything equally
- the answer hides the conclusion

### 5. Execute pass

Send:
`execute: priprav dnešný founder briefing a active execution queue.`

Expected result:
- Jarvis updates the briefing and queue surfaces
- Jarvis returns exact file paths
- runtime trace stays in `singularitas`
- business truth stays in `firma`

Pass if:
- the morning loop produces visible artifacts
- the response tells you what changed

Fail if:
- the answer stays conversational
- the work is not written anywhere

### 6. Promotion pass

Send:
`execute: z Dentmax callu sprav prospect next-step record a povedz, či to ide do firma.`

Expected result:
- Jarvis decides whether the object belongs in `firma`
- if it does, it promotes the business truth
- if it does not, it leaves a runtime trace and says why

Pass if:
- the promotion rule is explicit
- the decision is legible

Fail if:
- promotion happens by intuition with no explanation
- the object lands in the wrong surface

### 7. Approval pass

Send:
`execute: sprav approval packet na homepage/proof publish.`

Expected result:
- Jarvis updates runtime trace in `singularitas`
- canonical approval remains in `/Users/_xvadur/firma/approvals/`
- Jarvis asks only for the real founder decision

Pass if:
- approval state is visible in `firma`
- runtime packet remains trace only

Fail if:
- approval is treated as a chat promise
- live publish boundaries are crossed silently

## Expected Artifacts

By the end of the morning, there should be evidence in these surfaces:

- [Founder Briefing](/Users/_xvadur/firma/briefings/2026-03-18-founder-briefing.md)
- [Active Execution Queue](/Users/_xvadur/firma/briefings/2026-03-18-active-execution-queue.md)
- [Web / Proof Approval Packet](/Users/_xvadur/firma/approvals/2026-03-18-web-proof-approval-packet.md)
- [Current Roadmap](/Users/_xvadur/firma/roadmap/current.md)
- [Jarvis Usability Checklist v1](/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-jarvis-usability-checklist-v1.md)

At least one of these should change because of a live founder message.

## Missing Source Handling

If one source is missing, do not improvise the missing truth.

Use this rule:
- `NO_SIGNAL` for the missing section
- name the missing system
- continue the loop
- do not silently drop the section

Examples:
- if CRM is missing, `Leads needing action today` stays `NO_SIGNAL`
- if live ingress fails, stop after the ingress check and log the blocker
- if approval state is missing, keep the approval in `NO_SIGNAL` and point to the missing file or system

## Pass / Fail Summary

Pass the morning if all of these are true:
- live ingress works
- startup context is named correctly
- `capture`, `decide`, and `execute` are distinct
- at least one object is created or updated
- promotion behavior is explicit
- missing sources are labeled `NO_SIGNAL`
- the founder can continue without reconstructing context

Fail the morning if any of these happen:
- the wrong agent answers
- the context is vague
- the loop stays in chat
- the result is not written to a real surface
- business truth leaks into the wrong repo

## Stop Condition

Stop after the first morning loop is either:
- successful, with artifacts in the right surfaces, or
- blocked, with the blocker named and the next verification step written down

