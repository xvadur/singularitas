# Marek / realitky — Tool Design

## Purpose

This file explains how tools for Marek should be designed.
It is not implementation code.
It is the contract-design layer between prompt and backend.

## Tool design rule

Tools exist to let Marek do real actions safely.
They are not there to make the prompt look advanced.
If a tool does not support a real next step, it should not exist.

## What a tool spec must define

Every tool spec must define:
1. tool name
2. business purpose
3. when Marek may use it
4. minimum required inputs
5. expected success response shape
6. expected failure response shape
7. fallback spoken behavior

## Current known 5-tool surface

### `log_lead_progress`
Purpose:
- store/update lead data after qualification

Minimum useful inputs:
- caller identity/contact
- lane
- short summary

### `check_availability`
Purpose:
- verify whether callback/viewing slot is actually available

Minimum useful inputs:
- appointment type
- requested time
- enough contact/context

### `create_appointment`
Purpose:
- create confirmed callback or viewing after slot agreement

Minimum useful inputs:
- caller identity
- confirmed slot
- appointment type
- enough event context

### `handoff_urgent`
Purpose:
- escalate urgent or referral-based high-priority lead

Minimum useful inputs:
- caller identity/contact
- reason for urgency
- short summary

### `finalize_call`
Purpose:
- cleanly close the call trace in backend systems

Minimum useful inputs:
- outcome
- summary

## Cleaner target shape

Preferred future public shape:
- one public tool = `a10_control`
- one required top-level selector = `action`

Allowed actions:
- `log_lead`
- `check_availability`
- `create_appointment`
- `handoff_urgent`
- `finalize_call`

## Tool response rules

Tool responses should be:
- compact
- structured
- safe for spoken follow-up
- explicit about whether the requested next step is confirmed or not

Never rely on the model to infer confirmation from vague backend wording.

## Tool failure rule

If a tool fails or cannot confirm:
- Marek must not invent success
- Marek must not promise the slot/action anyway
- Marek should fall back to callback or safe follow-up

## Design principle

The cleaner the tool surface, the easier the agent is to patch, review, and scale.
But documentation must always reflect actual live reality, not aspirational architecture.
