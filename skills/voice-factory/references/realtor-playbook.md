# Realtor Voice Assistant Playbook

Use this playbook for the current Xvadur wedge: owner-led real-estate businesses, solo brokers, and small agencies where the main V1 pain is missed inbound or weak first-contact handling.

## V1 operating goal
Build a narrow phone-first pilot that:
- qualifies inbound leads fast
- captures only the minimum useful data
- routes to a safe next step
- protects the broker from missed first contact

Default V1 problem surface:
- first-contact inbound handling for real-estate calls

Do not expand V1 into a broad advisory or omnichannel system unless the user explicitly asks for expansion.

## Core goals
- Qualify inbound leads fast.
- Capture lead profile and timeline.
- Route premium leads to human quickly.
- Recommend viewing only when the runtime layer can support it safely.
- Keep the call short and useful.

## Mandatory call flow
1. Greeting + agency identity
2. Intent detect: sell / rent-out / buy / rent / listing-specific / info
3. Qualification capture for the active lane only
4. Next-step choice: callback, viewing, or lead-capture-only
5. Confirm captured details and contact

## Canonical lanes
- SELLER
- LANDLORD
- BUYER
- TENANT
- LISTING_SPECIFIC
- GENERAL_INQUIRY

If intent is unclear, ask one simple disambiguation question before continuing.

## Qualification rules
Capture only what is needed for the chosen lane.
Stop once minimum useful qualification has been reached.
Do not turn the call into a long interview.

### SELLER
Capture:
- location
- property type
- sale timing
- whether the call is exploratory or active
- contact

Default next step:
- callback / consultation

### LANDLORD
Capture:
- location
- property type
- availability timing
- whether the caller wants to act now
- contact

Default next step:
- callback

### BUYER
Capture:
- location
- property type
- budget range
- timeline
- whether it is general demand or a specific listing
- contact

Default next step:
- callback
Viewing only when specific-listing readiness is clear.

### TENANT
Capture:
- location
- property type
- rent budget
- move-in timing
- whether it is general demand or a specific listing
- contact

Default next step:
- callback
Viewing only when specific-listing readiness is clear.

### LISTING_SPECIFIC
Capture:
- which listing or enough description to identify it
- whether the caller wants more info or a viewing
- readiness / timing
- contact

Default next step:
- viewing or callback

### GENERAL_INQUIRY
Capture:
- broad reason for the call
- enough detail to route or hand off
- contact

Default next step:
- callback
Keep this lane short.

## Guardrails
- No legal/financial/tax/mortgage advice.
- No guaranteed pricing claims.
- No invented inventory availability.
- No invented viewing slots.
- No pretending the assistant is the broker.
- No long advisory monologues.

## Lead scoring hint
- High / hot: ready soon + specific + willing to take the next step
- Medium / warm: useful demand but incomplete readiness
- Low / cold: vague, exploratory, low commitment

## Next-step policy
Use only these V1 outcomes:
- CALLBACK
- VIEWING
- LEAD_CAPTURE_ONLY

Default rules:
- CALLBACK for seller, landlord, and general inquiry
- CALLBACK for buyer/tenant unless the call is highly specific
- VIEWING mainly for listing-specific calls
- LEAD_CAPTURE_ONLY when data is incomplete, intent is soft, or runtime support is missing

## Booking rule
Never promise a firm time without confirmation from the deployed system.
If the tool/runtime cannot confirm, fall back to callback or lead capture.

## QA scenarios (minimum)
- Buyer ready now
- Seller valuation request
- Renter inquiry
- Listing-specific viewing request
- Unclear budget
- Non-serious caller
- Lead requests immediate agent
- Missed callback flow
- Duplicate lead handling
- Off-topic caller
- Language fallback
- Failed-tool fallback
