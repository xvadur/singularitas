---
canonical_owner: singularitas
firma_record: /Users/_xvadur/firma/briefings/founder-cockpit.md
status_scope: runtime only
do_not_store_business_truth_here: true
---

# Founder Cockpit

## Objective

Make Jarvis usable as the daily founder control surface without requiring chat reconstruction.

The cockpit exists to answer, every day:
- what needs approval
- what leads need action today
- which callbacks are at risk
- what deployment is blocked
- what proof/content is ready to ship
- what web surface needs maintenance
- what the single best next move is

## Current definition of operable

The runtime mission is operable when:
- routing lands founder traffic in Jarvis
- runtime mission homes carry current traceable state
- one daily briefing can be assembled from current sources
- one approval packet can be generated
- missing signal is shown explicitly instead of being silently ignored

## Source systems

- local CRM SQLite, when present
- `projects/phone-first-engine/`
- `projects/web-proof-engine/`
- OpenClaw runtime and Telegram routing
- n8n workflow state if accessible
- manual founder queue for anything not yet system-wired
