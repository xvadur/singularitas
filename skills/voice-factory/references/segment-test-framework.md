# Segment Test Framework

Use this framework to test whether `voice-factory` can produce Marek-level outputs for other segments before adding backend complexity.

## Goal
Validate that the skill can reliably generate a deployable segment-specific V1 agent, not just a good realtor agent.

## Test order
1. Select one segment
2. Define one narrow problem surface
3. Produce full factory artifacts
4. Score output against the baseline
5. Only then add backend / n8n complexity

## Choose test segments
Prefer segments with these traits:
- inbound matters
- first contact has business value
- owner-led or simple buyer path
- easy to explain pilot outcome

Good candidates:
- clinic / dental
- ecommerce support
- automotive service booking
- home services

## Test input packet
For each segment, define:
- segment name
- business type
- target caller types
- primary pain surface
- language
- required captured fields
- allowed next-step outcomes
- forbidden claims
- whether tools exist yet

## Mandatory artifacts
A valid test run must produce:
- intake brief
- V1 scope definition
- deployment-pack summary
- lane / logic spec
- canonical prompt
- firstMessage
- Vapi field map
- QA scenario list
- deployment summary

## Pass criteria
### 1. Scope discipline
- one problem surface only
- no fake expansion into adjacent workflows
- no vague "AI can do everything" language

### 2. Segment specificity
- lanes match the segment
- qualification questions feel native to the segment
- next steps fit the buyer journey
- guardrails fit real failure modes

### 3. Spoken usability
- short natural phone phrasing
- one question at a time
- no essay prompt leakage into speech
- no repetitive filler

### 4. Deployment readiness
- prompt can go straight into Vapi with minor or no edits
- firstMessage is explicit
- model/transcriber/voice choices are declared
- tool assumptions are bounded and explicit

### 5. Marek parity
Compare to `marek-baseline-spec.md`.
The build does not need the same content, but should match:
- structural rigor
- V1 boundedness
- lane clarity
- next-step discipline
- production realism

## Fail signals
A build fails if:
- it sounds generic
- it asks for too much data
- it lacks clear lanes
- it invents undefined capabilities
- it mixes multiple surfaces into one pilot
- it cannot be patched into Vapi cleanly
- it needs major rewriting before deployment

## Test scoring rubric
Score each category from 1 to 5:
- scope discipline
- segment specificity
- spoken usability
- deployment readiness
- Marek parity

Interpretation:
- 22-25 = strong pass
- 18-21 = usable but needs tightening
- 14-17 = weak, revise before backend work
- below 14 = fail

## Recommended test sequence
1. Realtor baseline check against Marek
2. One adjacent segment test
3. One structurally different segment test
4. Review recurring failure patterns
5. Update skill before n8n backend layer

## Review questions
After each test ask:
- Did the skill protect scope?
- Did the output feel native to the segment?
- Did it define clear next steps?
- Did it avoid fake certainty?
- Could this go into Vapi today?

## Backend gate
Do not add n8n/backend complexity for a new segment until the segment passes the framework above.
Backend should amplify a good agent design, not compensate for a weak one.
