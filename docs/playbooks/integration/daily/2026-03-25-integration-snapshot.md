# Integration Snapshot

- Date: `2026-03-25`
- Owner: `integration`
- Scope: runtime only
- Status: `first real owner-lane snapshot`

## Verified signal

- the n8n cloud surface is live at `https://xvadur.app.n8n.cloud/`
- health endpoint responds successfully at `https://xvadur.app.n8n.cloud/healthz`
- Marek backend implementation artifacts exist locally and define a 5-webhook contract:
  - `log_lead_progress`
  - `check_availability`
  - `create_appointment`
  - `handoff_urgent`
  - `finalize_call`
- safe GET probes against the production webhook URLs currently return `404` with n8n message:
  - `The requested webhook "GET <path>" is not registered.`
- mail-triage worker exists locally and is intentionally reversible:
  - plain Node.js
  - `gog`-based Gmail access
  - additive labels only
  - no sending
  - apply mode separated from dry-run

## Current reality

Integration is not blank.
There is real runtime infrastructure and real implementation work.
The main problem is not absence of tooling, but missing founder-readable confirmation of which flows are actually live versus only staged.

Founder clarification applied:
- on `A10`, all webhooks were removed except one
- current goal is control of `A10` on demand, not full 5-webhook production behavior right now
- this means the current 404 results on removed webhook paths are expected, not automatically a failure

## Highest-risk blocker

The most important integration blocker is no longer “why are all 5 Marek webhooks not live”.
The clarified blocker is control clarity:
- n8n is up
- implementation artifacts exist
- but the currently intended `A10` control contract is not yet written as a concise founder-readable runtime contract

## Known unknowns

- whether the Marek workflow is active for `POST` production traffic = `NO_SIGNAL`
- current `MAREK_N8N_MODE` in live n8n = `NO_SIGNAL`
- current live Sheets write behavior = `NO_SIGNAL`
- current live Calendar write behavior = `NO_SIGNAL`
- current mail-triage runtime schedule / cadence = `NO_SIGNAL`

## Next safe move

Write the current `A10` control contract explicitly:
1. what the single remaining webhook does
2. what inputs it accepts
3. what it is allowed to control on demand
4. what has been intentionally removed for now

Only after that should we validate the remaining live path.

## Sources

- `/Users/_xvadur/singularitas/studio/integration/README.md`
- `/Users/_xvadur/singularitas/studio/integration/MAIL_TRIAGE_IMPLEMENTATION_NOTE.md`
- `/Users/_xvadur/singularitas/outputs/marek-n8n-backend-v1/implementation_notes.md`
- `/Users/_xvadur/singularitas/outputs/marek-n8n-backend-v1/canvas_design.md`
