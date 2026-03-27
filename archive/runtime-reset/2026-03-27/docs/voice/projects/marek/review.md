# Marek / realitky — Review

## Objective

Prepare Marek / realitky as a reviewable voice-agent baseline that can be shown to Jakub without pretending the runtime is more proven than it is.

## Asset under review

- project: `marek`
- agent name: `realitky`
- agent id: `agent_2101k84bc5ebfbjrn3etm9g3fytb`
- platform: `ElevenLabs`
- current stage: `partial-validation`

## Current scope

Narrow V1 voice agent for phone-first real-estate inbound handling.
Current scope is first contact, lead handling, scheduling logic, and controlled handoff behavior.

## Confirmed signal

Confirmed from current material:
- live ElevenLabs agent identity is known and readable
- live readback exists for `realitky`
- current first message is:
  - `Dobrý deň, dovolali ste sa k realitnému maklérovi Jakubovi Valachovskému. Ja som jeho virtuálny asistent Marek. S čím vám môžem pomôcť?`
- live agent currently still contains structured Marek prompt and workflow shape
- live workflow shape still reflects lane/action logic across seller, landlord, buyer, tenant, listing-specific inquiry, callback request, general inquiry, and referral
- live agent currently has 5 webhook tools attached:
  - `log_lead_progress`
  - `check_availability`
  - `create_appointment`
  - `handoff_urgent`
  - `finalize_call`
- backend package v2 exists as the current production-compatible 5-webhook gateway
- the local canonical prompt surface is now intentionally written tool-agnostically enough to survive either the live 5-tool contract or a later `a10_control` cleanup

## Unverified areas

Still not confirmed founder-readably:
- end-to-end POST tool execution
- live workflow activation for production traffic
- Sheets / Calendar writes under real traffic
- whether the actual intended contract is still the live 5-tool design or the newer single-control-tool design

## What looks strong

- Marek is already a real staged asset, not just a concept
- the agent has a strong bounded V1 shape
- the new canonical prompt is more natural, less form-like, and more phone-native
- callback is framed as the normal safe broker path, not as an apologetic fallback
- the prompt keeps Marek clearly separate from Jakub
- scheduling, handoff, and guardrail logic remain conservative

## What looks weak

- contract ambiguity exists between the live 5-tool runtime and the newer `a10_control` simplification proposal
- runtime evidence is weaker than the packaging depth might suggest
- prompt quality is now ahead of runtime-contract clarity

## Missing before review-ready

- one clean send-ready summary for Jakub
- one explicit statement of which contract is being reviewed:
  - current live 5-tool runtime
  - or next cleaned single-tool target

## Missing before deploy-ready

- bounded founder-readable proof of live POST execution
- clearer evidence around workflow activation mode
- confirmation that current prompt and current tool contract actually match the intended deployment model

## Recommended review framing

Use two layers:

### Layer 1 — design review now
Review now:
- greeting
- tone and persona fit
- prompt quality
- qualification logic
- callback / viewing framing
- referral / urgent handling
- guardrails and overclaim risk

### Layer 2 — runtime review after contract lock
Then verify:
- intended tool surface
- workflow activation mode
- one safe end-to-end POST path
- one bounded happy path

## Recommended patch set

1. keep `projects/marek/prompt.md` as the canonical main iteration surface
2. keep the prompt’s tool phrasing lean so it stays compatible with both runtime shapes
3. preserve explicit mention that the current live agent still uses 5 tools until revalidated otherwise
4. run one bounded validation pass and update `qa.md`
5. produce a short send-ready summary for Jakub from this review

## Recommended next move

Use the new prompt as the main review surface with Jakub, but keep the runtime contract question explicit until one contract is locked.
