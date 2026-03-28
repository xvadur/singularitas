# Marek Runtime Validation Result

- Date: `2026-03-25`
- Owner: `voice`
- Support lane: `integration`
- Mode: `safe read-only probe`
- Status: `partial validation only`

## What was safely confirmed

- n8n cloud root is live: `https://xvadur.app.n8n.cloud/`
- n8n health endpoint responds: `https://xvadur.app.n8n.cloud/healthz`
- the configured production webhook URLs are reachable as public URLs

## What the safe probes returned

GET requests to these paths return `404` with explicit n8n registration message:
- `/webhook/log_lead_progress`
- `/webhook/check_availability`
- `/webhook/create_appointment`
- `/webhook/handoff_urgent`
- `/webhook/finalize_call`

Observed message shape:
- `The requested webhook "GET <path>" is not registered.`

## What this means

This proves:
- the n8n surface is reachable
- read-only probe traffic reaches n8n

This does **not** prove:
- that the workflow is inactive
- that the workflow is active for `POST`
- that the end-to-end tool flow works

## Safe verdict

Marek runtime is still only partially validated, but the meaning of the probe changed after founder clarification.
The safest current founder-facing statement is:
- infrastructure endpoint is alive
- implementation exists
- removed webhook paths are expected to fail if they were intentionally deleted from `A10`
- the real open task is documenting and validating the single live `A10` control path

## Next move

The next validation step needs authenticated inspection of the workflow state or a deliberately safe POST test after confirming the mode and write behavior.

## Sources

- `/Users/_xvadur/singularitas/outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`
- `/Users/_xvadur/singularitas/outputs/marek-n8n-backend-v1/implementation_notes.md`
