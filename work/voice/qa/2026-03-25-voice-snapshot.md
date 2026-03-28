# Voice Snapshot

- Date: `2026-03-25`
- Owner: `voice`
- Scope: runtime only
- Status: `first real owner-lane snapshot`

## Verified signal

- the realtor voice-agent work is staged around a live ElevenLabs agent: `realitky`
- live agent id recorded in runtime handoff: `agent_2101k84bc5ebfbjrn3etm9g3fytb`
- five webhook tools are already attached to the live ElevenLabs agent:
  - `log_lead_progress`
  - `check_availability`
  - `create_appointment`
  - `handoff_urgent`
  - `finalize_call`
- v1 operating rules are already locked:
  - callback = `15 min`
  - viewing = `60 min`
  - working window = `08:00–19:00`
  - lunch block = `12:00–13:00`
  - weekends allowed
  - logistics buffers defined
  - failed slots should return 3 alternatives
- backend artifacts for the n8n side already exist and validate locally

## Current reality

Voice is no longer only conceptual.
The product layer is materially staged, but runtime confidence is still limited because end-to-end live validation is not yet proven at the founder-facing layer.

## Main risk

The biggest voice risk is not prompt absence.
It is the gap between staged assistant/tool configuration and verified live runtime behavior.

## Known unknowns

- current end-to-end webhook behavior = `NO_SIGNAL`
- current QA outcome from a live call path = `NO_SIGNAL`
- current callback handoff behavior under real traffic = `NO_SIGNAL`
- visible Vapi credential / deployment state in the current runtime = `NO_SIGNAL`

## Next safe move

Run one bounded runtime validation pass:
1. confirm workflow import/activation on the n8n side
2. verify the five live webhook paths end-to-end
3. record one founder-readable QA result
4. only then propose live runtime changes

## Sources

- `/Users/_xvadur/singularitas/projects/phone-first-engine/status.md`
- `/Users/_xvadur/singularitas/outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`
