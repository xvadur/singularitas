# Marek Runtime Validation Packet

- Date: `2026-03-25`
- Owner: `voice`
- Support lane: `integration`
- State: `ready for execution`

## Objective

Turn the staged Marek voice runtime into a founder-readable validated state.

## Validation scope

### ElevenLabs side
Confirm the live agent still reflects the staged setup:
- agent: `realitky`
- attached tools:
  - `log_lead_progress`
  - `check_availability`
  - `create_appointment`
  - `handoff_urgent`
  - `finalize_call`

### n8n side
Confirm the backend can answer the live webhook contract:
- `log_lead_progress`
- `check_availability`
- `create_appointment`
- `handoff_urgent`
- `finalize_call`

### QA pass
Verify at least one bounded scenario:
- appointment request
- callback request
- failed slot returning alternatives
- urgent handoff path

## Pass condition

A founder-readable note can say:
- tools attached = confirmed
- workflow active = confirmed
- one scenario works end-to-end = confirmed
- main remaining risk = explicitly named

## Failure condition

Any of these:
- webhook path fails
- workflow inactive
- scheduling logic breaks the locked rules
- callback/handoff behavior is unclear after test

## Output

Write results back into:
- `agents/voice/daily/2026-03-25-voice-snapshot.md`
- `agents/voice/queue.md`
- founder-facing active execution queue if the blocker meaningfully changes

## Sources

- `/Users/_xvadur/singularitas/outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`
- `/Users/_xvadur/singularitas/projects/phone-first-engine/status.md`
