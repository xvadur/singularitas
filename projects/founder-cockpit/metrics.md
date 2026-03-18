# Metrics

## Daily briefing sources

- Approvals queue
  - source: `projects/*/approvals/`
  - current state: `partial`
- Leads needing action
  - preferred source: local CRM inbox / reminders
  - current state: `blocked` because CRM DB is missing
- Callbacks at risk
  - preferred source: `projects/phone-first-engine/status.md` + CRM
  - current state: `manual`
- Deployment blocked
  - source: `projects/phone-first-engine/status.md`
  - current state: `live`
- Proof/content ready
  - source: `projects/web-proof-engine/content/` and `projects/web-proof-engine/status.md`
  - current state: `partial`
- Web maintenance
  - source: `projects/web-proof-engine/watchlist.md`
  - current state: `live`
- Single best next move
  - source: Jarvis synthesis across all of the above
  - current state: `manual`

## Operability KPIs

- one full briefing produced daily
- zero required briefing sections left implicit
- every blocker has owner + next move
- at least one approval packet available when work is pending
