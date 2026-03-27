# Research Operator Queue

- Date: `2026-03-26`
- Owner: `research`
- State: `active`

## Active items

1. `natural20-hourly-monitor`
   - State: `active-live`
   - Objective: maintain a rolling Natural20 intelligence surface so Jarvis can answer what changed over the last X hours from stored state instead of reconstruction
   - Current reality: rolling state file exists, daily brief log exists, and hourly automation is live via OpenClaw cron
   - Next move: run `python3 ./skills/natural20-api-brief/scripts/n20_ingest.py` on the hourly monitor, keep the rolling top 10 current, and refine alert thresholds only after observing more live runs
   - Source: `/Users/_xvadur/singularitas/studio/research/inventory/natural20-live-top10.md`
   - Scheduler: OpenClaw cron job `Natural20 hourly rolling research monitor`

2. `research-segment-operator-template`
   - State: `done`
   - Objective: turn `research` into a reusable lane-operator setup
   - Current reality: routing note, templates, inventory scaffold, and reusable contract skeleton now exist
   - Next move: use this lane on real requests and refine only after observing actual delegation patterns
   - Source: `/Users/_xvadur/singularitas/studio/library/templates/lane-operator-template.md`
