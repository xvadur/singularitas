# Marek Baseline Spec

Use this as the current golden-reference output for `voice-factory`.

## Reference assistant
- Name: `Marek`
- Vapi assistant id: `e8bf5c35-173f-4217-bd25-51b34e790888`
- Business: Brex Reality
- Role: inbound real-estate assistant for broker call handling

## Why this matters
This assistant is the current proof that the factory can produce a high-quality segment-specific voice agent.
Future segment builds do not need to copy realtor content, but they should match this level of structure, clarity, boundedness, and deployability.

## Baseline quality standard
A compliant output should be:
- segment-specific, not generic
- phone-first and operational
- lane-based
- concise in speech behavior
- conservative about promises
- clear about next steps
- bounded to V1 scope
- deployable in Vapi without major rewriting

## Live Vapi pattern
### Model layer
- provider: `openai`
- model: `gpt-5-chat-latest`
- temperature: `0.4`
- prompt lives in `model.messages[0].content`
- current tools: none (`toolIds: []`)

### Voice layer
- provider: `11labs`
- voice model: `eleven_v3`
- voiceId: `XbNOzeieIf3pDGjp7UgV`
- speed: `1.1`
- stability: `0.5`
- similarityBoost: `0.75`
- optimizeStreamingLatency: `4`

### Transcriber layer
- provider: `openai`
- model: `gpt-4o-transcribe`
- language: `sk`

### Other active fields
- `firstMessage` is set explicitly
- `analysisPlan.structuredDataPlan.enabled = true`
- structured extraction schema currently includes:
  - `lead_type`
  - `call_outcome`
  - `summary_short`
  - `intent_primary`
  - `lead_temperature`

## Prompt shape to preserve
The prompt follows this pattern:
1. Identity
2. Communication rules
3. Main mission
4. Routing / lane detection first
5. Lane playbooks
6. Lead scoring
7. Next-step engine
8. Calendar / booking placeholder rules
9. Forbidden pricing/estimation behavior
10. Tool rules
11. Guardrails
12. Fallbacks
13. Closing behavior

## Behavioral standard
The agent should:
- speak Slovak naturally
- use formal address
- ask one question at a time
- avoid robotic repetition
- summarize when the caller gives many details
- stop at minimum useful qualification
- choose next step conservatively
- never invent facts

## Scope standard
V1 must stay narrow.
For Marek, the scope is first-contact inbound handling for realtor calls.
For other segments, preserve the same narrow-pilot discipline.

## What future builds must reproduce
Not the realtor wording itself, but the same production qualities:
- clear lane model
- minimum useful qualification
- explicit next-step outcomes
- strong guardrails
- realistic spoken behavior
- clean Vapi-ready field mapping

## What future builds may vary
- segment and buyer type
- lane set
- required fields
- default next-step outcomes
- voice choice
- transcriber choice
- tool layer
- analysis schema

## Factory acceptance rule
A new segment build passes only if it can stand next to Marek and still feel:
- equally structured
- equally bounded
- equally usable in a real phone flow
- equally ready for Vapi deployment
