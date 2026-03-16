# Vapi Build System

## Goal
Turn one-off prompt work into a repeatable build pipeline for Vapi agents.

## Canonical build flow
1. Capture brief
2. Define scope
3. Design conversation architecture
4. Build canonical prompt
5. Prepare Vapi patch payload
6. Deploy to Vapi
7. Run QA scenarios
8. Record changelog and next iteration

## Required input packet
- business / vertical
- language
- target caller types
- desired next steps
- booking/callback rules
- tool destinations
- hard guardrails
- success definition

## Agent architecture
Every Vapi agent should be treated as a composed system:
- brief
- lane map
- routing logic
- qualification rules
- lead scoring
- next-step engine
- tool layer
- voice config
- transcriber config
- QA pack
- deployment patch
- changelog

## Minimum artifacts to create
For every serious agent change, create or update:
- canonical prompt file
- deploy patch file
- lane / logic spec
- QA scenario list
- deployment summary

## Deploy rules
- Inspect current assistant before mutation
- Patch only what you intend to change
- Preserve voice/transcriber/tool config unless intentionally changing them
- Verify the write by reading the assistant back
- Record assistant id, prompt version, and changed fields

## Placeholder policy
Use placeholders when business rules are missing, but label them clearly.
Typical placeholder categories:
- hot/warm/cold scoring thresholds
- booking preferences
- callback windows
- qualification depth
- escalation triggers

## V1 vs V2 rule
Do not force advanced intelligence into V1.
Use V1 for:
- routing
- qualification
- next-step handling
- safe booking/callback behavior
Use V2+ for:
- pricing engines
- route/travel intelligence
- complex recommendation logic
- dynamic market reasoning

## QA baseline
Always test at least:
- clear seller call
- clear buyer call
- tenant/prenájom call
- listing-specific call
- vague inquiry
- caller with no contact yet
- caller asking for something outside scope
- failed-tool fallback

## Output contract
Return:
- what changed
- what stayed untouched
- assistant id/name
- risks / placeholders still present
- next iteration actions
