# Voice Lane Context Inventory

- Date: `2026-03-25`
- Owner: `voice`
- Purpose: consolidated workspace context for Adam's current voice-agent needs
- Status: `first consolidated inventory`

## Executive summary

The current voice lane is centered on ElevenLabs-based real-estate voice-agent work, with `voice-factory` as the primary build discipline and one concrete staged reference deployment around the `realitky` / Marek assistant.

What already exists is not just theory:
- a live ElevenLabs agent reference exists
- prompt / tool / backend artifacts exist
- review and QA discipline exists in skill references
- the main gap is not design absence, but fragmented inventory and incomplete end-to-end validation

For the `voice` agent, the current workspace truth is:
- own the ElevenLabs lane
- use `voice-factory` as the primary skill
- treat Marek / realitky as the current baseline reference
- organize future requests as build / audit / patch / workflow / review / QA tasks

## Current owner-lane contract

`voice` now owns:
- ElevenLabs agent design
- prompt architecture and prompt patching
- conversation and workflow logic
- review prep for collaborators like Jakub
- QA scenarios and launch-readiness checks
- consistency and cleanup across voice projects

`voice` does not own by default:
- n8n implementation
- CRM orchestration
- outbound collaborator messaging
- live risky writes without approval

## Core skills and references

### Primary skill
- `skills/voice-factory/SKILL.md`

This is the main build system for:
- capture brief
- define scope
- design conversation system
- build canonical prompt
- prepare deploy/review patch
- run QA logic
- prepare launch packet

### Supporting skill
- `skills/elevenlabs/SKILL.md`

Use for:
- ElevenLabs voices and voice management
- speech generation
- quota and usage
- voice clone operations
- direct ElevenLabs API-oriented work

### High-value references in `voice-factory`
- `references/prompt-construction-framework.md`
- `references/polish-rules.md`
- `references/vapi-build-system.md`
- `references/vapi-test-suites.md`
- `references/realtor-playbook.md`
- `references/marek-baseline-spec.md`

## Current concrete project signal

### 1. Marek / realitky is the main staged proof artifact

From current workspace evidence:
- live ElevenLabs agent name: `realitky`
- recorded live agent id: `agent_2101k84bc5ebfbjrn3etm9g3fytb`
- canonical handoff doc: `outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`

### 2. Current live tool surface attached to the live agent
- `log_lead_progress`
- `check_availability`
- `create_appointment`
- `handoff_urgent`
- `finalize_call`

### 3. Locked v1 operating rules currently present in the workspace
- callback = `15 min`
- viewing = `60 min`
- working window = `08:00–19:00`
- lunch block = `12:00–13:00`
- weekends allowed
- callbacks cannot overlap with viewings
- logistics buffers:
  - same Bratislava zone = `60 min`
  - different Bratislava zone = `90 min`
  - outside Bratislava = `120 min`
- failed slot should return `3 nearest alternatives`

## Current business / design frame

### Wedge
The current wedge is:
- owner-led real-estate businesses
- phone-first inbound handling
- narrow V1 pilots

### Default V1 problem surface
From the realtor playbook:
- missed inbound / weak first-contact handling

### Canonical lane model
The workspace already treats the realtor assistant as lane-based, with these default intent buckets:
- SELLER
- LANDLORD
- BUYER
- TENANT
- LISTING_SPECIFIC
- GENERAL_INQUIRY

### Allowed next-step outcomes in V1
- CALLBACK
- VIEWING
- LEAD_CAPTURE_ONLY

### Main guardrails
- no invented pricing
- no invented inventory availability
- no invented viewing slots
- no legal/financial/mortgage advice
- no pretending the assistant is the broker
- no broad advisory monologues

## Prompt standard already established

The preferred prompt shape is already defined in workspace references:
1. Identity
2. Communication rules
3. Mission
4. Routing logic
5. Lane playbooks
6. Lead scoring
7. Next-step engine
8. Tool rules
9. Guardrails
10. Fallbacks
11. Closing behavior

Prompt quality rules already established:
- write as runtime instructions, not documentation
- prefer short spoken phrasing
- ask one question at a time
- callback should sound like a normal safe path, not failure
- avoid duplicated caution language
- preserve bounded V1 scope

## Runtime / backend artifact inventory

### Voice lane runtime docs
- `agents/voice/status.md`
- `agents/voice/daily/2026-03-25-voice-snapshot.md`
- `agents/voice/daily/2026-03-25-marek-runtime-validation-packet.md`
- `agents/voice/daily/2026-03-25-marek-runtime-validation-result.md`

### Phone-first engine docs
- `projects/phone-first-engine/status.md`
- `projects/phone-first-engine/brief.md`
- `projects/phone-first-engine/spec/pilot-workflow.md`
- `projects/phone-first-engine/validation/first-deployment-path-checks.md`

### Runtime handoff + backend packages
- `outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`
- `outputs/marek-n8n-backend-v1/`
- `outputs/marek-n8n-backend-v2/README.md`
- `outputs/marek-n8n-backend-v3-phased/`

### Notable backend package truths
The v2 package says the current production-compatible gateway is built around the exact public webhook endpoints already attached in ElevenLabs.

It already covers:
- Google Sheets lead/call/appointment logging
- Google Calendar availability and event creation
- urgent handoff storage / webhook path
- call finalization
- the current business scheduling constraints

## Current validation truth

What is confirmed:
- n8n cloud root is live
- health endpoint responds
- public webhook paths are reachable
- local backend artifacts exist
- read-only probes reached n8n

What is not yet confirmed founder-readably:
- end-to-end POST tool behavior
- live workflow activation state beyond safe partial validation
- live callback/handoff behavior under actual runtime traffic
- full current deploy/readiness inventory across all ElevenLabs work

This means the main gap is validation and consolidation, not blank-slate design.

## Existing baseline standard for future work

The current golden-reference build standard is the Marek baseline.

Key baseline expectations:
- segment-specific, not generic
- phone-first and operational
- lane-based
- bounded to V1
- conservative about promises
- deployable structure
- explicit prompt shape
- realistic spoken behavior

The baseline spec also records one prior runtime pattern with:
- model provider: `openai`
- model: `gpt-5-chat-latest`
- voice provider: `11labs`
- voice model: `eleven_v3`
- transcriber provider: `openai`
- transcriber model: `gpt-4o-transcribe`
- language: `sk`

Treat this as a reference pattern, not an immutable requirement.

## What the `voice` agent should now be able to do with this context

Given current workspace state, `voice` should be ready to handle:
- audit an existing ElevenLabs agent
- rewrite or patch a system prompt
- prepare a review pack for Jakub
- compare staged voice artifacts
- generate QA scenarios for a voice agent
- identify missing pieces before review or launch
- frame a new voice-agent build request using the existing factory pattern
- summarize current readiness and biggest risk

## Known gaps in the workspace right now

- no single consolidated inventory of all existing ElevenLabs agents / projects yet
- no reusable review template stored in the lane yet
- no reusable prompt-patch template stored in the lane yet
- live validation is still partial, not end-to-end
- some canonical planning docs for Marek still live in `singularitas_opus`, not mirrored into the lane workspace

## Recommended immediate next artifacts

1. `agents/voice/templates/review-template.md`
2. `agents/voice/templates/prompt-patch-template.md`
3. `agents/voice/inventory/elevenlabs-projects.md`
4. one concise "how to route voice requests" note for Jarvis → voice delegation

## Sources used for this inventory

- `agents/voice/README.md`
- `agents/voice/status.md`
- `agents/voice/daily/2026-03-25-voice-snapshot.md`
- `agents/voice/daily/2026-03-25-marek-runtime-validation-packet.md`
- `agents/voice/daily/2026-03-25-marek-runtime-validation-result.md`
- `projects/phone-first-engine/status.md`
- `outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`
- `outputs/marek-n8n-backend-v2/README.md`
- `skills/elevenlabs/SKILL.md`
- `skills/voice-factory/SKILL.md`
- `skills/voice-factory/references/realtor-playbook.md`
- `skills/voice-factory/references/marek-baseline-spec.md`
- `skills/voice-factory/references/prompt-construction-framework.md`
- `skills/voice-factory/references/polish-rules.md`
- `skills/voice-factory/references/vapi-build-system.md`
- `skills/voice-factory/references/vapi-test-suites.md`
