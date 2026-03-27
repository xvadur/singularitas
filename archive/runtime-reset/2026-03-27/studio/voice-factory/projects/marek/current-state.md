# Marek / realitky — Current State

## Project identity

- project: `marek`
- live agent name: `realitky`
- live agent id: `agent_2101k84bc5ebfbjrn3etm9g3fytb`
- segment: real estate
- purpose: phone-first inbound handling for a narrow V1 pilot
- owner / collaborator: Adam / Jakub
- platform: ElevenLabs + n8n backend artifacts

## Current stage

- overall stage: `partial-validation`
- prompt status: `candidate canonical prompt mirrored locally`
- workflow status: `staged`
- QA status: `partial`
- review status: `active`

## Confirmed signal

Confirmed from current material:
- a live ElevenLabs agent reference exists: `realitky`
- live readback exists for the agent
- the first message is already defined
- the live agent currently still has 5 attached webhook tools
- the current production-compatible backend package is the 5-webhook gateway in `outputs/marek-n8n-backend-v2/`
- a cleaned prompt candidate exists and is now mirrored into `projects/marek/prompt.md`
- key V1 business rules are already defined:
  - callback = `15 min`
  - viewing = `60 min`
  - working window = `08:00–19:00`
  - lunch block = `12:00–13:00`
  - weekends allowed
  - callbacks cannot overlap with viewings
  - logistics buffers exist
  - failed slot should return `3 nearest alternatives`

## Current reality

Marek is a staged real asset with enough material for serious review and prompt editing.
The main remaining confusion is not whether the agent exists.
The main confusion is which runtime contract should now be treated as canonical:
- current live 5-tool runtime
- or cleaned single-control-tool target

## Main blockers

- contract ambiguity between live runtime and cleaned target
- no founder-readable proof yet for live POST execution
- no final Jakub-facing short review summary yet

## What this project needs next

1. lock the review contract
2. prepare the short Jakub-facing review summary
3. if needed, run one bounded validation pass against the chosen runtime contract

## Canonical local project docs

- `prompt.md`
- `review.md`
- `qa.md`

## Primary source trail

- `studio/integration/daily/2026-03-25-marek-v2-cleaned-prompt.md`
- `studio/integration/daily/2026-03-25-marek-elevenlabs-review-packet.md`
- `studio/integration/daily/2026-03-25-marek-v2-single-tool-contract.md`
- `outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`
- `outputs/marek-n8n-backend-v2/README.md`
