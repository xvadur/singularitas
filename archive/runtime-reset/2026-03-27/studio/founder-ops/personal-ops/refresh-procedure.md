# Personal Ops Refresh Procedure

Purpose: run one founder-ops live refresh for `main` without improvisation.

## V1 trusted sources

### Calendar
- source: Google Calendar via `gog`
- account: `adam@xvadur.com`
- default scope:
  - today
  - next 48 hours

### Inbox
- source: Gmail via `gog`
- account: `adam@xvadur.com`
- default scope:
  - unread inbox
  - important or starred inbox items
  - exclude obvious social/promo noise from the final founder-facing summary unless risk is present

### Tasks and commitments
- source: Apple Reminders via `remindctl`
- trusted list for v1:
  - `XVADUR`
- use as the primary reminder / follow-up surface until a stronger unified contract replaces it

### Context only
- Obsidian vault at `/Users/_xvadur/singularitas_opus`
- use only for context or capture lookup, not as the primary live task source in this refresh

## Refresh order

1. calendar
2. inbox
3. reminders / tasks / commitments
4. time risk synthesis
5. write current-day snapshot
6. update founder brief if the result changes founder-facing truth

## Commands

### Calendar
```bash
gog calendar calendars --account adam@xvadur.com --plain --no-input
gog calendar events --account adam@xvadur.com --from '<ISO_FROM>' --to '<ISO_TO>' --plain --no-input
```

Use two windows:
- today: local midnight to next local midnight
- next 48h: now to now + 48h

### Inbox
```bash
gog gmail search 'in:inbox is:unread' --account adam@xvadur.com --max 20 --plain --no-input
gog gmail search 'in:inbox is:important newer_than:14d' --account adam@xvadur.com --max 20 --plain --no-input
gog gmail search 'in:inbox is:starred' --account adam@xvadur.com --max 20 --plain --no-input
```

If a message looks actionable, inspect it:
```bash
gog gmail get '<MESSAGE_ID>' --account adam@xvadur.com --json --results-only --no-input
```

### Tasks and reminders
```bash
remindctl status
remindctl overdue --plain
remindctl list XVADUR --plain
remindctl list xvadur --plain
```

## Output contract for the daily snapshot

Always surface:
- current state
- urgent conflict or approval need
- blocker or risk
- single best next founder move

Always separate:
- verified signal
- unresolved / blind spots
- inferred risk

Use `NO_SIGNAL` only when the source was actually checked and still does not yield usable truth.

## Current v1 interpretation rules

### Calendar
- if there are no events today and no events in the next 48h, say that explicitly
- do not invent hidden meetings from inbox noise

### Inbox
- newsletters and social notifications do not become founder-critical by default
- payment failures, legal/admin asks, client/prospect replies, and founder-blocking operational requests do
- if the inbox has noise but no urgent blocker, say so plainly

### Tasks and commitments
- overdue reminders count as commitment drift even if no calendar event exists
- duplicate reminders should be surfaced as cleanup debt if they affect clarity

## Review threshold

Escalate to `main` immediately if the refresh finds:
- a same-day meeting conflict
- a payment / account risk blocking core tools
- a legal / tax / compliance deadline risk
- a client or lead reply that is clearly waiting on the founder

Otherwise, write the snapshot and keep the next move concrete.
