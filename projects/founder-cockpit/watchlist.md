# Watchlist

## Missing signals

- CRM DB missing from the expected local path
  - Owner: `revenue`
  - Next move: recover or replace the local relationship-memory source used by the CRM skill
- n8n health not yet wired into the briefing
  - Owner: `integration`
  - Next move: capture a local n8n state artifact or explicitly mark the automation lane `NO_SIGNAL` in the morning briefing
- Vapi credential visibility is unclear from current runtime config
  - Owner: `voice` + `integration`
  - Next move: confirm whether Vapi is intentionally absent from current config or present elsewhere in runtime secrets
- Cal.com exists by founder confirmation but is not yet represented as a local contract artifact
  - Owner: `personal-ops`
  - Next move: add a local booking contract note if Cal.com remains part of tomorrow's daily loop

## Drift risks

- old Telegram bot names can hide the fact that routing logic changed
  - Owner: `jarvis`
  - Next move: keep using the runtime route bridge doc in all founder-facing runtime references
- founder queue can fall back into chat if packets are not used
  - Owner: `jarvis`
  - Next move: force approvals and execution changes into `projects/*/approvals` or handoff packets
- web/content/proof work can drift into notes if not packetized
  - Owner: `web` + `proof`
  - Next move: promote the publishing queue and publish approval packet into the default workflow

## Immediate checks

- verify default Telegram account still lands in Jarvis
- verify legacy account routing now points to the new canonical owners
- verify the briefing can be generated even with partial source coverage
