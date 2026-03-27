# Founder Ops Snapshot

- Date: `2026-03-24`
- Owner: `personal-ops`
- Scope: runtime only
- Status: `verified live refresh + cleanup applied`
- Refreshed at: `2026-03-25 01:04 Europe/Bratislava`

## Sources checked

- Google Calendar via `gog` on `adam@xvadur.com`
- Gmail via `gog` on `adam@xvadur.com`
- Apple Reminders via `remindctl`

## Current state

The founder control surface now has its first real live `personal-ops` read.

- calendar is verified, not `NO_SIGNAL`
- inbox is verified, not `NO_SIGNAL`
- tasks / commitments now have a provisional trusted source in Apple Reminders
- the main founder risk is not schedule collision but commitment drift from overdue follow-ups and unresolved operational inbox items

## Calendar

### Verified signal
- no events were found for today across the visible `adam@xvadur.com` calendars
- no events were found for the next 48 hours across the visible `adam@xvadur.com` calendars
- visible calendars:
  - `adam@xvadur.com`
  - `Sviatky na Slovensku`

### Interpretation
- there is no live calendar conflict visible in the verified source
- if meetings exist elsewhere, they are outside the currently trusted calendar surface

## Inbox

### Verified signal
Unread inbox is real, but most visible unread items are social or newsletter noise rather than founder-critical blockers.

Actionable items surfaced in the live scan:
- `OpenAI` — `Please update your Plus payment method`
  - payment failed but access is still temporarily active
- `Denisa Novotná / Legalia` — `Ochranná známka - xvadur`
  - waiting for more detail about your activity so trademark help can proceed
- `Finančná správa` — `Oznámenie o zmene stavu overenia podania`
  - the filing status changed to valid

Founder decision already applied:
- `Expandeco` is now treated as cancelled / no-go and removed from the active personal queue

### Noise visible but not urgent
- LinkedIn notifications
- Facebook comment notifications
- Instagram feed mail
- newsletters such as Claw and OpenClaw digests

### Interpretation
- inbox is not empty, but there is no same-day crisis visible from the verified scan
- the real founder-facing inbox pressure is a small backlog of unresolved operational items, not fresh emergency mail

## Tasks and commitments

### Trusted source for v1
Apple Reminders is now the provisional trusted task surface for `personal-ops`, specifically list:
- `XVADUR`

### Verified open overdue reminders
- `Spraviť demo na AI recepciu`
- `Call Bohuš Dentmax`
- `Call Semafor Dent - Ondrej Užovič`

### Interpretation
- commitment drift is visible and real
- reminder duplication has been reduced by retiring the legacy `xvadur` duplicates and consolidating into `XVADUR`
- this remains the strongest current founder-ops risk in the live refresh

## Reminder and time risk

### Verified signal
- no same-day calendar conflict is visible
- no next-48h meeting load is visible
- overdue reminders and unresolved operational inbox items are still open

### Risk
The current risk is under-rotation on follow-up commitments, not schedule overload.

## Current limitations

- this refresh verifies only the currently visible Google account: `adam@xvadur.com`
- the task-source contract is now usable in v1, but still provisional rather than final
- Obsidian remains context, not the primary live task source for this pass
- no automation has been attached to this refresh yet

## Single best next move

Do one founder cleanup pass on the live backlog:
1. resolve the OpenAI payment method issue
2. decide whether to reply to Legalia on the trademark thread
3. reschedule or kill the remaining overdue `XVADUR` reminders based on real priority
