# Marek Specific Implementation Plan

Status: Draft locked after client-specific discovery
Purpose: Translate Jakub-specific operating reality into a concrete implementation plan for the current Marek realtor agent, with a later follow-up patch into `voice-factory` as a client-specific extension pattern.

---

## 1. What this document is

This is a **Marek-specific implementation plan**.
It is not yet the generic skill patch.

Reason:
- first we need a clean client-specific implementation spec,
- then we can decide what belongs in the general `voice-factory` skill,
- and what should remain client-specific configuration.

So the sequence is:
1. client-specific spec
2. Marek/Jakub implementation
3. extract reusable pattern
4. patch `voice-factory`

---

## 2. Core business truth

The system exists to help Jakub:
- catch inbound leads immediately,
- preserve lead momentum,
- qualify fast without sounding robotic,
- create structured records automatically,
- trigger fast callback action,
- reduce notebook/manual-entry chaos.

The single most important rule:
**speed-to-lead matters more than over-qualification.**

Default safe principle:
- better fast structured callback than slow perfect questionnaire.

---

## 3. Marek role definition

Marek is:
- Jakub's front-line voice assistant
- first-contact inbound triage layer
- lead qualification and callback acceleration system

Marek is not:
- Jakub himself
- a legal/financial advisor
- a generic receptionist
- a broad real-estate consultant

---

## 4. Pilot scope

### In scope
- inbound phone handling
- intent detection
- buyer / seller / viewing / callback / general info / referral routing
- minimum useful qualification
- lead priority scoring
- competence scoring
- mood / behavior tagging
- structured CRM / ticket output
- ASAP callback workflow
- callback scheduling when explicitly requested
- safe viewing recommendation logic
- regression test suite baseline

### Out of scope for pilot
- full pricing intelligence
- full map-based travel intelligence
- automatic hard booking of viewings without feasibility checks
- deep web/Telegram ecosystem expansion
- legal, tax, mortgage, or investment advice
- broad market analysis as if guaranteed fact

---

## 5. Core lanes

Primary lanes for current Marek:
1. BUYER
2. SELLER
3. VIEWING REQUEST
4. CALLBACK REQUEST
5. GENERAL INFO
6. REFERRAL
7. COMPETITOR / LOW INTENT EXPLORER

Rule:
- optimize mainly for BUYER and SELLER,
- treat VIEWING and CALLBACK as next-step flows,
- treat REFERRAL as high-priority fast-escalation logic.

---

## 6. Callback operating logic

### Default rule
- callback default = ASAP
- do not postpone unless client explicitly wants later timing

### Agent phrasing
Allowed:
- "Odovzdám to Jakubovi ako prioritu a bude vás kontaktovať čo najskôr."
- "Jakub si to hneď preberie a ozve sa vám v najbližších minútach."

Not allowed:
- exact guaranteed time unless system truly supports it

### Callback output must contain
- name
- phone
- call reason
- short summary
- priority
- preferred callback time
- lead type
- status = ASAP or scheduled callback

---

## 7. Qualification logic

### Global rule
Do not recite the full discovery set.
Discovery depth depends on:
- intent clarity
- heat of lead
- referral status
- willingness to cooperate

### HOT / referral rule
- capture minimum viable data
- escalate quickly
- preserve momentum

### Standard buyer/seller rule
- go deeper where useful
- still keep conversation natural and short

### Buyer minimum
- property type
- location
- purpose (investment / own living)
- budget
- financing
- timeline
- who decides
- whether next step should be viewing or callback

### Seller minimum
- what is being sold
- location
- property type / condition
- sale timeline
- whether another broker is involved
- what the seller expects from Jakub
- whether next step is callback or meeting

Note:
- buyer stereotypes are forbidden
- financing is a qualification variable, not the main sales angle

---

## 8. Lead scoring model

### Priority
- HOT
- WARM
- COLD
- LOW VALUE

### Competence
- DECISION MAKER
- INFLUENCER
- UNKNOWN

### Lead type
- BUYER
- SELLER
- VIEWING REQUEST
- CALLBACK REQUEST
- REFERRAL
- GENERAL INFO
- COMPETITOR
- LOW INTENT EXPLORER

### Behavior / mood
- calm
- urgent
- cautious / privacy-protective
- indecisive
- arrogant
- confused

### Guardrail
Do not label a lead low-value just because they protect privacy or refuse one question.
Use low-value only after repeated weak-intent or manipulative signals.

---

## 9. Viewing logic

### Baseline
- one viewing is around 15 minutes
- scheduling cannot rely only on free calendar slots
- travel / transfer time matters

### Conservative rule
If transfer certainty is missing, be conservative.
A viewing at 14:00-14:15 does not imply another realistic viewing at 14:20.

### Preferred windows
- default viewing window: 08:00-18:00
- later in summer only if still daylight
- night viewings are discouraged
- weekend possible, but secondary

### Safe next-step rule
When feasibility is unknown:
1. offer another sensible term
2. offer callback
3. avoid hard promise

---

## 10. CRM / ticket schema minimum

Every call should create a structured record with at least:
- call date and time
- name
- phone
- lead type
- intent
- referral flag
- location
- property type
- purpose
- budget
- financing
- timeline
- who decides
- priority
- client behavior / mood
- important notes
- proposed next step
- callback or viewing
- note on competition / low intent

---

## 11. n8n architecture for current pilot

### V1 core
1. `lead_capture`
2. `request_callback`
3. `log_call_outcome`

### V1.5 next layer
4. `resolve_listing`
5. `check_viewing_feasibility`
6. `create_viewing_event`
7. `suggest_next_slots`

### V2 later
8. `pricing_lookup`
9. map/travel intelligence
10. smarter calendar logistics intelligence

---

## 12. Test suite baseline

Current minimum regression pack for Marek:
1. happy-path listing-specific inbound
2. seller valuation guardrail
3. vague inquiry / ambiguity fallback

Future tests to add:
- referral lead fast-escalation
- privacy-protective but legitimate buyer
- competitor / low-intent filtering
- viewing feasibility with no safe slot

---

## 13. What must still be finalized

Before production lock:
- final agent name
- exact callback promise wording
- discovery set count and final canonical ordering
- whether rentals are active or secondary in this deployment
- after-hours logic
- exact backoffice system naming / destination
- whether map integration is available in V1.5 or only later

---

## 14. What later belongs in the skill patch

After this implementation is stable, patch `voice-factory` with reusable patterns such as:
- speed-to-lead callback-first logic
- referral as high-priority escalation rule
- configurable discovery-depth by lead heat
- travel-aware viewing feasibility pattern
- test-suite minimum pack requirement
- CRM schema expectations for realtor deployments

Do not patch in client-specific branding, names, or backoffice specifics unless converted into placeholders/config fields.

---

## 15. Recommendation

Build Marek as a **callback-first, qualification-aware realtor inbound system**.
Do not overbuild pricing or logistics intelligence in the pilot.
Win first on:
- response speed
- clean lead capture
- priority clarity
- structured handoff to Jakub

Only after that, expand into deeper calendar and pricing intelligence.
