# Marek / realitky — Build System

## What this file is

This is the operating document for building and modifying the Marek voice agent.
It exists so the `voice` layer can reliably:
- inspect the current agent
- redesign the prompt
- redesign tools
- prepare a modification packet
- produce a deployable ElevenLabs update shape

This is the actual working brief for the voice-layer agent.

## Core rule

We do not build Marek by improvising directly in ElevenLabs.
We build Marek through a repeatable packet:
1. define V1 scope
2. define lane logic
3. define prompt
4. define tool surface
5. define workflow outcomes
6. define QA
7. only then patch the agent

## Current platform reality

Current working platform:
- ElevenLabs agent named `Marek` / historically `realitky`
- voice agent for realtor inbound handling

Current workspace truth:
- live/staged runtime evidence still points to a 5-tool shape
- cleaned target design points to a simpler single-control-tool shape

## Build sequence

### 1. Scope
Always define first:
- what problem surface this version solves
- what is in V1
- what is outside V1

Default Marek V1 surface:
- first-contact inbound handling for real-estate calls
- missed inbound / weak first-contact handling

### 2. Lane model
Canonical realtor lanes:
- SELLER
- LANDLORD
- BUYER
- TENANT
- LISTING_SPECIFIC
- GENERAL_INQUIRY
- CALLBACK_REQUEST
- REFERRAL
- UNKNOWN

### 3. Prompt design
Prompt block order:
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

### 4. Tool design
Tool design always defines:
- tool names
- when each tool is allowed
- minimum required inputs before tool call
- what to do on tool failure
- what Marek must never invent

### 5. Workflow outcomes
Allowed V1 outcomes must stay explicit:
- CALLBACK
- VIEWING
- LEAD_CAPTURE_ONLY
- URGENT_HANDOFF
- FINALIZED_CALL

### 6. QA
Minimum QA pack per meaningful change:
- one happy path
- one guardrail path
- one ambiguous-intent path

### 7. Deployment packet
Before patching ElevenLabs, produce:
- modification summary
- prompt diff or replacement prompt
- tool surface definition
- workflow logic summary
- QA expectations

## Design standards

### Spoken behavior standard
Marek should:
- speak Slovak
- use formal address
- sound like a prepared broker assistant
- ask one question at a time
- keep calls short and useful
- stop once minimum useful qualification is captured

### Safety standard
Marek must never:
- pretend to be the broker
- invent listing facts
- invent availability
- invent pricing facts
- give legal/tax/mortgage advice
- promise a confirmed slot without system confirmation

### V1 discipline standard
Do not let V1 sprawl.
Default safe next step is callback.
Viewing is allowed only when the call is specific enough and runtime support can safely back it.

## Current operator use

When asked to modify Marek, the voice-layer agent should work in this order:
1. read `brief.md`
2. read `current-state.md`
3. read `prompt.md`
4. read `tools.md`
5. read `workflow.md`
6. read `knowledge.md`
7. produce modification packet
8. only then prepare runtime patch/deployment work

## Deliverable types this system should produce

This build system should let us produce, on demand:
- revised prompt
- tool redesign
- lane redesign
- stricter scope version
- broker-specific personalization
- QA scenarios
- deployment summary
- ElevenLabs modification packet
