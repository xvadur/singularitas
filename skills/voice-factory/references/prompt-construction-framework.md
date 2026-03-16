# Prompt Construction Framework

## Prompt blocks
Build Vapi prompts in this order:
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

## Identity
State:
- who the assistant represents
- what type of incoming calls it handles
- what its job is

## Communication rules
Constrain tone and spoken behavior:
- language
- formality
- brevity
- one question at a time
- natural spoken phrasing
- no robotic repetition

## Routing logic
Do not assume one default caller intent.
Make the assistant classify the call first.
Typical routing buckets:
- seller
- buyer
- landlord
- tenant
- listing-specific
- general inquiry

## Lane playbooks
For each lane define:
- when a call belongs there
- what to ask
- minimum useful info
- default next step

## Lead scoring
Use simple behavioral buckets first:
- hot
- warm
- cold
Tie them to urgency, specificity, and willingness to take the next step.

## Next-step engine
Define the allowed outcomes explicitly:
- callback
- booking / inspection
- consult
- lead capture only
The assistant should choose among these, not improvise undefined outcomes.

## Tool rules
Define:
- when a tool may be used
- minimum required inputs before tool use
- what to do when a tool fails
- what the assistant must never invent after a failed tool

## Guardrails
Include explicit prohibitions for:
- invented availability
- invented pricing
- legal/financial advice
- unsupported claims
- overpromising outcomes

## Fallbacks
Cover at least:
- unclear speech
- unclear intent
- missing required info
- tool failure
- human handoff

## Closing behavior
Always close with:
- short summary
- next step
- polite end

## Design rules
- Keep prompts operational, not essay-like
- Prefer lane logic over giant generic instructions
- Prefer simple defaults plus placeholders over fake certainty
- Write for spoken conversations, not chat UX
