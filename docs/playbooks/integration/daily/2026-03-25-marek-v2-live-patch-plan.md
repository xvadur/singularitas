# Marek v2 — Live Patch Plan

- Date: `2026-03-25`
- Owner: `integration`
- Support lane: `voice`
- State: `approval-ready plan`

## Objective

Patch the live ElevenLabs agent from the current cluttered multi-tool + workflow-graph setup to a cleaner v2 shape:
- one cleaned prompt
- one control tool
- minimal or no active workflow graph orchestration
- n8n owns business logic

## Current live state to replace

Confirmed on current live `realitky` agent:
- 5 webhook tools attached
- 42 workflow nodes
- 84 workflow edges
- prompt still contains duplicated lane/action logic

## Desired live state after patch

### ElevenLabs side
Keep:
- agent identity
- language = `sk`
- first message
- voice / ASR / turn settings unless intentionally changed

Change:
- replace 5 tools with 1 tool: `a10_control`
- replace current long prompt with `Marek v2 — Cleaned Prompt`
- remove the large workflow graph from active orchestration
- keep the agent as a thin conversational front-end

### n8n side
Create or expose one public webhook endpoint, for example:
- `/webhook/a10_control`

Inside n8n:
- validate payload
- dispatch by `action`
- reuse current internal modules for:
  - lead log
  - availability check
  - appointment creation
  - urgent handoff
  - finalize

## Non-goals for this patch

This patch should **not** try to redesign the whole product.
It should only:
- simplify control surface
- eliminate duplication
- improve legibility
- preserve current business intent

## Patch sequence

### Phase 0 — backup
Before any change:
1. export current live agent JSON
2. save current prompt
3. save current tool definitions
4. save current workflow JSON
5. note current update timestamp

### Phase 1 — backend first
Do this before touching the live agent:
1. create `a10_control` webhook in n8n
2. implement `action` dispatch
3. return stable JSON responses
4. verify one safe mock response per action

### Phase 2 — tool definition
Prepare one ElevenLabs webhook tool:
- name: `a10_control`
- method: `POST`
- URL: `https://xvadur.app.n8n.cloud/webhook/a10_control`
- body schema aligned with `Marek v2 — Single-Tool Contract`

### Phase 3 — prompt patch
Replace the current prompt with the cleaned v2 prompt.
Do not mix the old lane-heavy prompt with the new single-tool contract.

### Phase 4 — workflow simplification
Preferred:
- remove the large workflow graph from active decision-making
- leave either:
  - minimal/default start flow only, or
  - no meaningful orchestration graph at all if platform allows prompt-led behavior cleanly

Important:
Do not keep the old graph half-alive.
Half-cleanups create the worst confusion.

### Phase 5 — live verification
Run a bounded QA pass:
1. lead capture only
2. callback request
3. viewing request with unavailable slot
4. urgent referral
5. normal call close

## Exact fields to preserve during patch

Unless intentionally changed, preserve:
- voice settings
- ASR settings
- turn settings
- language
- first message
- any platform safety / privacy settings

The patch should target only:
- prompt
- tool list
- workflow orchestration shape

## Rollback plan

If anything becomes unclear or unstable:
1. restore previous live agent JSON from backup
2. restore original 5 tools
3. restore original workflow graph
4. verify readback from ElevenLabs API

No cleanup should happen without a clear rollback artifact.

## Approval gates

Before patching live, lock these approvals:

### Gate 1 — architecture
Approve:
- one-tool contract
- thin ElevenLabs / thick n8n split

### Gate 2 — prompt
Approve:
- cleaned v2 prompt
- first message

### Gate 3 — backend contract
Approve:
- request schema
- response schema
- action list

### Gate 4 — live mutation
Approve:
- replacing the live agent tool surface
- removing the old workflow graph from active orchestration

## Expected outcome

After patch, founder should be able to explain Marek in one sentence:

> Marek vedie hovor, zistí minimum potrebných údajov a cez jeden control webhook spúšťa backend akcie v n8n.

If the runtime cannot be explained that simply, the patch is not finished.

## Immediate implementation packet to prepare next

After approval, the actual mutation packet should include:
1. backup file path
2. final prompt text
3. final tool JSON
4. final endpoint URL
5. test payloads for all 5 actions
6. rollback command / rollback payload

## Sources

- `/Users/_xvadur/singularitas/studio/integration/daily/2026-03-25-marek-cleanup-plan-v2.md`
- `/Users/_xvadur/singularitas/studio/integration/daily/2026-03-25-marek-v2-single-tool-contract.md`
- `/Users/_xvadur/singularitas/studio/integration/daily/2026-03-25-marek-v2-cleaned-prompt.md`
- `/Users/_xvadur/singularitas/studio/integration/daily/2026-03-25-marek-elevenlabs-review-packet.md`
