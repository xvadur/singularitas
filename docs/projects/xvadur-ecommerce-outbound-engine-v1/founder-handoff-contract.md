# Xvadur E-commerce Outbound Engine v1 - Founder Handoff Contract

Status: Active  
Owner before handoff: Jarvis  
Owner after handoff: Adam

## When Founder Receives A Packet

Adam receives a handoff only when at least one of these is true:
1. The lead replied and now needs founder judgment or founder response.
2. The lead completed AI call qualification and the outcome is `qualified_for_founder`.
3. Jarvis marks the lead commercially sensitive enough for founder action now.

Adam should not receive:
- leads still missing core context
- weak replies that belong in nurture
- speculative leads with no clear next move

## Exact Packet Contents

Every founder packet must contain these sections:

### 1. Lead snapshot
- `lead_id`
- company name
- website
- segment
- contact name if known
- contact email
- contact phone if relevant
- current lead state
- founder priority

### 2. Why this matters now
- strongest visible pain signal
- why the account is worth attention now
- what changed that triggered founder involvement

### 3. Outbound history
- original subject line
- original outbound summary or direct body reference
- send date if already sent
- any follow-up already done

### 4. Reply or qualification summary
- what the lead said or what the call confirmed
- real interest signal
- open uncertainty

### 5. Recommended next move
- exactly one action: `reply by email`, `founder call`, `nurture follow-up`, or `disqualify`
- recommended timing
- recommended CTA

### 6. References
- tracking row reference
- outreach packet reference
- demo/preview asset reference
- AI call packet reference if applicable

## What Must Never Be Missing

The packet is invalid if any of these are missing:
- company identity
- current state
- reason founder is seeing it now
- outbound history
- clear next move
- source references

If one is missing, the lead stays with Jarvis and does not get handed off yet.

## Ownership Rules

### Before handoff
- Jarvis owns packet assembly and delivery readiness.
- Upstream owners must fill missing context before Jarvis can hand off.

### After handoff
- Adam owns the commercial action.
- Tracking should switch owner to `Adam`.
- `handoff_status` may become `delivered` only after the packet exists and owner changed.

## Delivery Format

Recommended file:

`founder-handoff.md`

Recommended section order:

```md
## Lead snapshot
## Why this matters now
## Outbound history
## Reply or qualification summary
## Recommended next move
## References
```

## Minimal Quality Bar

Adam should be able to answer these immediately from the packet:
- Who is this?
- Why now?
- What happened already?
- What do I do next?

If the packet does not answer all four, it is not handoff-ready.
