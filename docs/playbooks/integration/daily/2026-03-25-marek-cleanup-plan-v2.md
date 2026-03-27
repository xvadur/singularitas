# Marek / realitky — Cleanup Plan v2

- Date: `2026-03-25`
- Owner: `integration`
- Support lane: `voice`
- State: `review-ready cleanup plan`

## Executive verdict

Current Marek setup is hard to reason about because decision logic is split across **three layers at once**:
1. ElevenLabs prompt
2. ElevenLabs workflow graph
3. n8n backend

This creates duplication, ambiguity, and review fatigue.

## Main design problem

The system currently mixes:
- lane routing in the prompt
- lane routing in the ElevenLabs workflow graph
- business action routing in n8n

That means the same question is being answered multiple times:
- what kind of caller is this
- what is the next step
- when should booking/handoff/logging happen

For a founder-reviewable agent, this is the wrong shape.

## Cleanup goal

Move Marek to a shape that is:
- readable
- debuggable
- patchable
- safe to review
- easy to evolve

## Recommended target architecture

### Recommended default
**Thin ElevenLabs agent + thick n8n control plane**

### What ElevenLabs should own
Only:
- greeting
- concise qualification
- safe spoken behavior
- deciding when it has enough information to call backend
- one clean handoff between conversation and backend

### What n8n should own
Only n8n should own:
- lead logging
- appointment availability checks
- appointment creation
- urgent handoff logic
- call finalization
- CRM / Sheets / Calendar writes
- business rules
- audit trail

## Strong recommendation

### Remove from live design
- the large ElevenLabs workflow graph as the main orchestration layer
- lane-specific graph routing inside ElevenLabs
- duplicated decision logic between graph and prompt

### Keep in live design
- one good system prompt
- one founder-readable opening line
- one backend control surface
- one clear source of truth for business actions

## Preferred v2 contract

### Best option: single control tool
Expose exactly **one ElevenLabs webhook tool**:
- `a10_control`

This tool accepts an `action` field and a normalized payload.

### Suggested actions
- `log_lead`
- `check_availability`
- `create_appointment`
- `handoff_urgent`
- `finalize_call`

### Why this is better
- the agent UI becomes dramatically cleaner
- no tool sprawl
- no workflow graph required for normal operation
- backend stays modular internally
- founder can reason about one entrypoint
- future changes happen in one contract, not five places

## Suggested request shape for the single tool

```json
{
  "action": "check_availability",
  "call_id": "optional-call-id",
  "lead": {
    "full_name": "Ján Kováč",
    "phone": "+421..."
  },
  "lane": "buyer",
  "context": {
    "listing_reference": null,
    "location": "Bratislava - Ružinov"
  },
  "appointment": {
    "type": "callback",
    "requested_start": "2026-03-26T14:00:00+01:00"
  },
  "summary": "buyer wants callback tomorrow afternoon"
}
```

## Minimal conversational architecture in v2

### In prompt
The prompt should do only this:
1. greet
2. identify intent/lane
3. capture minimum viable info
4. choose safe next step
5. call backend when enough info exists
6. speak clearly about the result
7. close

### In backend
The backend should do only this:
1. validate payload
2. normalize payload
3. dispatch by `action`
4. apply business rules
5. write to systems
6. return compact JSON

## What to delete, keep, move

### Delete
Delete from the design surface:
- big lane-heavy ElevenLabs workflow graph
- subagent-style graph routing for seller/buyer/tenant/etc.
- duplicate action nodes for handoff/check/create/finalize in ElevenLabs

### Keep
Keep:
- current language and opening direction
- current business rules for callback / viewing / buffer windows
- current role framing: Marek is not Jakub, he is first-line assistant
- current n8n business logic intent

### Move
Move to n8n:
- all deterministic business decisions
- all write operations
- all audit logic
- all future complexity

## Review standard after cleanup

After cleanup, the founder should be able to inspect Marek in three simple pieces:
1. **prompt** — how he talks
2. **single tool contract** — what he can ask backend to do
3. **n8n workflow** — what actually happens in systems

If it takes more than that to understand the runtime, it is still too messy.

## Safe migration path

### Phase 1 — freeze current state
Before any mutation:
- export current live agent JSON
- save current tool config
- save current prompt
- save current workflow graph

### Phase 2 — define clean v2 contract
Produce:
- single-tool schema
- cleaned prompt
- expected response contract
- action list

### Phase 3 — prepare backend adapter
In n8n:
- create one public webhook endpoint for `a10_control`
- dispatch internally by `action`
- keep internals modular
- keep JSON response stable

### Phase 4 — patch ElevenLabs
Patch live agent to:
- remove the large workflow graph from active orchestration
- remove 5-tool clutter
- attach one clean control tool
- keep the prompt concise and operational

### Phase 5 — bounded QA
Run exactly these tests:
1. lead capture only
2. callback request
3. viewing request with unavailable slot
4. urgent referral/handoff
5. normal close with finalize

## Risks if we do not clean it now

If current design stays as-is:
- reviews will stay confusing
- runtime failures will be harder to localize
- future edits will keep breaking hidden coupling
- founder trust in the surface will drop
- every change will feel heavier than it should

## Recommended decision now

Lock this as the intended direction:

**Marek v2 = prompt-led conversation + single webhook control contract + n8n-owned business logic.**

That is the cleanest shape for a founder-readable phone-first agent.

## Immediate next deliverables

If approved, next I should prepare:
1. `Marek v2 single-tool contract`
2. `Marek v2 cleaned prompt`
3. `Marek v2 live patch plan`

## Sources

- `/Users/_xvadur/singularitas/studio/integration/daily/2026-03-25-marek-elevenlabs-review-packet.md`
- `/Users/_xvadur/singularitas/outputs/marek-n8n-backend-v1/implementation_notes.md`
- `Source: ../../../singularitas_opus/Operácie/Xvadur - Agent Deploy Studio/Marek Workflow v2/23 - n8n Workflow Inventory.md#L1-L58`
- `Source: ../../../singularitas_opus/Operácie/Xvadur - Agent Deploy Studio/Marek Workflow v2/24 - n8n Gateway Workflow Spec.md#L1-L61`
