# Marek / realitky — ElevenLabs Review Packet

- Date: `2026-03-25`
- Owner: `integration`
- Support lane: `voice`
- State: `ready for founder review`

## Objective

Overiť aktuálny live stav ElevenLabs agenta pre Mareka a pripraviť stručný review packet, ktorý oddeľuje:
- čo je naozaj potvrdené live,
- čo je zatiaľ len staged alebo historicky pripravené,
- čo blokuje runtime review.

## Live state verified now

### Agent identity
- agent name: `realitky`
- agent id: `agent_2101k84bc5ebfbjrn3etm9g3fytb`
- live readback z ElevenLabs API funguje
- last known live update on the agent: `2026-03-23 10:50:28 UTC`

### Language / opening
- language: `sk`
- first message is set to:
  - `„Dobrý deň, dovolali ste sa realitnému maklérovi. Ja som virtuálny asistent Marek. S čím vám môžem pomôcť?“`
- current LLM on the live agent: `gpt-5-mini`

### Prompt / orchestration
- live agent still contains the structured Marek prompt for realtor intake
- live workflow is attached
- workflow size on live agent:
  - nodes: `42`
  - edges: `84`
- live workflow still contains the lane/action architecture for:
  - seller
  - landlord
  - buyer
  - tenant
  - listing-specific inquiry
  - callback request
  - general inquiry
  - referral

### Tools currently attached on the live agent
The live agent currently has **5 webhook tools attached**, not one:
1. `log_lead_progress`
2. `check_availability`
3. `create_appointment`
4. `handoff_urgent`
5. `finalize_call`

Current live webhook URLs on the agent:
- `https://xvadur.app.n8n.cloud/webhook/log_lead_progress`
- `https://xvadur.app.n8n.cloud/webhook/check_availability`
- `https://xvadur.app.n8n.cloud/webhook/create_appointment`
- `https://xvadur.app.n8n.cloud/webhook/handoff_urgent`
- `https://xvadur.app.n8n.cloud/webhook/finalize_call`

## Safe runtime probe results

Read-only GET probe against all 5 configured n8n webhook URLs currently returns `404` with the standard n8n message shape:
- `The requested webhook "GET <path>" is not registered.`

This confirms only:
- public n8n surface is reachable
- the configured URLs resolve to n8n

This does **not** confirm:
- that the workflow is active for `POST`
- that the tool call succeeds end-to-end
- that Sheets / Calendar writes are currently live

## Important mismatch discovered

There is a real mismatch between the previously clarified operating assumption and the current live agent state.

### Previously clarified assumption
Founder clarification said:
- on `A10`, all webhooks were removed except one
- current goal is on-demand control, not the old 5-webhook runtime

### Current live reality on `realitky`
The actual live ElevenLabs agent `realitky` still has:
- 5 tools attached
- 5 webhook URLs in prompt config
- 5-tool workflow routing still wired into the live agent

## What this most likely means

One of these is true:
1. `realitky` is **not** the same live surface Adam meant by `A10`
2. the intended single-webhook simplification was discussed but not actually reflected on this live agent
3. the agent prompt/workflow was preserved while the downstream n8n side was partially removed or deactivated

## Review-ready verdict

### Ready for review now
These layers are reviewable immediately:
- opening line / first impression
- language and persona fit
- prompt quality and guardrails
- lane design and next-step logic
- tool naming and tool intent
- workflow architecture

### Not yet review-complete
These layers are **not** yet proven:
- end-to-end tool execution
- real booking creation
- real Sheets logging
- real urgent handoff behavior
- final production runtime correctness

## Concrete review questions

1. Is `realitky` the exact ElevenLabs agent you want reviewed right now?
2. Do you want review against the **current live 5-tool design**, or against the intended **single-control A10 design**?
3. Is phone routing intentionally absent right now?
   - current live readback shows `phone_numbers: 0`
4. For this review, do we care more about:
   - prompt quality,
   - tool/runtime shape,
   - or true end-to-end call readiness?

## Suggested review framing

Use this review in two layers:

### Layer 1 — agent design review
Review now:
- greeting
- prompt quality
- lane routing
- lead handling logic
- callback / viewing framing
- referral / urgent escalation behavior
- overclaim risks

### Layer 2 — runtime review
Only after design review freeze:
- confirm intended tool surface (`5 tools` vs `1 control webhook`)
- confirm n8n activation mode
- run one deliberately safe POST test
- confirm one bounded happy path

## Recommended next move

Before any live mutation, lock one founder decision:

**Which contract is real now?**
- `Contract A`: keep `realitky` as the 5-tool agent and review it as staged production runtime
- `Contract B`: collapse to the A10-style single-control surface and review only that narrower control path

Without that decision, the review can be useful, but it cannot become a clean launch-readiness verdict.

## Sources

- live ElevenLabs API readback for `agent_2101k84bc5ebfbjrn3etm9g3fytb`
- `/Users/_xvadur/singularitas/outputs/marek-n8n-backend-v1/elevenlabs-tools-deploy.json`
- `/Users/_xvadur/singularitas/outputs/marek-n8n-backend-v1/realitky-agent-patch-body-v2.json`
- `/Users/_xvadur/singularitas/studio/integration/daily/2026-03-25-integration-snapshot.md`
- `/Users/_xvadur/singularitas/studio/voice-factory/daily/2026-03-25-marek-runtime-validation-result.md`
