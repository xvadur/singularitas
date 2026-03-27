# Marek v2 — Single-Tool Contract

- Date: `2026-03-25`
- Owner: `integration`
- Support lane: `voice`
- State: `draft ready for review`

## Goal

Replace the current cluttered multi-tool / multi-graph setup with one founder-readable control surface.

## Public tool surface

Expose exactly one ElevenLabs webhook tool:
- `a10_control`

Suggested public description:

> Použi tento nástroj vždy, keď už máš dosť údajov na vykonanie ďalšieho kroku. Tento nástroj slúži na lead logging, overenie dostupnosti, vytvorenie callbacku alebo obhliadky, urgent handoff a finálne uzavretie hovoru. Nepoužívaj ho bez minima potrebných údajov pre konkrétnu akciu.

## Contract principle

The agent should not think in terms of many tools.
It should think in terms of one backend capability with one required field:
- `action`

Everything else is structured payload.

## Allowed actions

### 1. `log_lead`
Use when:
- the caller is qualified enough to store/update lead
- no booking is needed yet
- the call should still leave a clean CRM trace

### 2. `check_availability`
Use when:
- caller wants callback or viewing
- requested date/time is known enough to check
- the agent must not promise a slot before verification

### 3. `create_appointment`
Use when:
- a specific slot was confirmed by caller
- slot was either returned as available or selected from alternatives

### 4. `handoff_urgent`
Use when:
- referral or clearly urgent high-value lead
- immediate transfer/escalation path should be attempted
- the lead should be marked as priority

### 5. `finalize_call`
Use when:
- the call is ending
- outcome is known
- the backend should close the trace cleanly

## Minimal request schema

```json
{
  "action": "check_availability",
  "call_id": "optional-call-id",
  "lead": {
    "full_name": "Ján Kováč",
    "phone": "+421900000000",
    "email": null
  },
  "lane": "buyer",
  "priority": "warm",
  "context": {
    "listing_reference": null,
    "location": "Bratislava - Ružinov",
    "source": "inbound_call",
    "referral": false
  },
  "qualification": {
    "intent_primary": "callback_request",
    "intent_secondary": null,
    "lead_temperature": "warm",
    "decision_role": "unknown",
    "summary_short": "buyer wants callback tomorrow afternoon"
  },
  "appointment": {
    "type": "callback",
    "requested_start": "2026-03-26T14:00:00+01:00",
    "requested_end": null,
    "confirmed_start": null,
    "confirmed_end": null
  },
  "handoff": {
    "reason": null,
    "target": null
  },
  "call": {
    "outcome": null,
    "notes": "caller prefers afternoon"
  }
}
```

## Action-specific required fields

### `log_lead`
Required:
- `action`
- at least one contact field:
  - `lead.phone` preferred
  - `lead.full_name` strongly preferred
- `lane`
- `qualification.summary_short`

### `check_availability`
Required:
- `action`
- `lead.full_name` or `lead.phone`
- `appointment.type`
- `appointment.requested_start`
- `lane`

### `create_appointment`
Required:
- `action`
- `lead.full_name`
- `lead.phone`
- `appointment.type`
- `appointment.confirmed_start`
- enough context for event labeling

### `handoff_urgent`
Required:
- `action`
- `lead.full_name` or `lead.phone`
- `handoff.reason`
- `qualification.summary_short`

### `finalize_call`
Required:
- `action`
- `call.outcome`
- `qualification.summary_short` or `call.notes`

## Allowed lane values

- `buyer`
- `seller`
- `landlord`
- `tenant`
- `listing_specific`
- `callback_request`
- `general_inquiry`
- `referral`
- `unknown`

## Allowed appointment types

- `callback`
- `viewing`

## Response contract

The backend should always return compact JSON.
Never HTML. Never raw stack traces.

## Common response envelope

```json
{
  "ok": true,
  "action": "check_availability",
  "status": "available",
  "message_for_agent": "Termín vyzerá voľný. Môžeš si ho s klientom potvrdiť.",
  "data": {}
}
```

## Action-specific response examples

### `log_lead`
```json
{
  "ok": true,
  "action": "log_lead",
  "status": "stored",
  "message_for_agent": "Lead je uložený.",
  "data": {
    "lead_id": "lead_123"
  }
}
```

### `check_availability` — available
```json
{
  "ok": true,
  "action": "check_availability",
  "status": "available",
  "message_for_agent": "Termín je dostupný.",
  "data": {
    "requested_start": "2026-03-26T14:00:00+01:00",
    "requested_end": "2026-03-26T14:15:00+01:00"
  }
}
```

### `check_availability` — unavailable
```json
{
  "ok": true,
  "action": "check_availability",
  "status": "unavailable",
  "message_for_agent": "Požadovaný termín nie je voľný. Ponúkni tri najbližšie alternatívy.",
  "data": {
    "requested_start": "2026-03-26T14:00:00+01:00",
    "alternatives": [
      "2026-03-26T15:00:00+01:00",
      "2026-03-26T16:30:00+01:00",
      "2026-03-27T09:00:00+01:00"
    ]
  }
}
```

### `create_appointment`
```json
{
  "ok": true,
  "action": "create_appointment",
  "status": "created",
  "message_for_agent": "Termín je zapísaný.",
  "data": {
    "calendar_event_id": "evt_123",
    "calendar_event_link": "https://calendar.google.com/..."
  }
}
```

### `handoff_urgent`
```json
{
  "ok": true,
  "action": "handoff_urgent",
  "status": "escalated",
  "message_for_agent": "Urgentný handoff bol zaznamenaný ako priorita.",
  "data": {
    "handoff_status": "logged"
  }
}
```

### `finalize_call`
```json
{
  "ok": true,
  "action": "finalize_call",
  "status": "closed",
  "message_for_agent": "Hovor je uzavretý.",
  "data": {
    "call_outcome": "callback_requested"
  }
}
```

## Error contract

```json
{
  "ok": false,
  "action": "create_appointment",
  "status": "validation_error",
  "message_for_agent": "Chýba potvrdený termín. Najprv si ho s klientom potvrď.",
  "data": {
    "missing_fields": ["appointment.confirmed_start"]
  }
}
```

## Business rules that remain in backend

These should stay in n8n, not in the ElevenLabs workflow graph:
- callback duration = 15 min
- viewing duration = 60 min
- working hours = 08:00–19:00
- lunch block = 12:00–13:00
- weekends allowed
- callbacks blocked during viewings
- BA same-zone / diff-zone / outside buffers
- 3 alternatives on unavailable slot

## Founder-readable rule

If the agent needs to do something real, it calls `a10_control` with an `action`.
That is the whole public runtime mental model.

## Sources

- `/Users/_xvadur/singularitas/studio/integration/daily/2026-03-25-marek-cleanup-plan-v2.md`
- `/Users/_xvadur/singularitas/outputs/marek-n8n-backend-v1/implementation_notes.md`
