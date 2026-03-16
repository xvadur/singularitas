# Marek #2 — Intake Brief

## Test purpose
Validate that `voice-factory` can produce another deployable realtor V1 assistant at Marek quality, not just describe the existing one.

## Build label
- Working name: `Marek 2`
- Business: Brex Reality
- Vertical: realtor
- Channel: phone
- Language: Slovak

## Primary business pain
- missed inbound
- weak first-contact handling
- inconsistent qualification before broker follow-up

## One problem surface
Handle first-contact inbound real-estate calls and route them to a safe next step.

## Caller types
- seller
- landlord
- buyer
- tenant
- listing-specific caller
- general inquiry

## Required captured fields
### universal minimum
- name
- phone or other usable callback contact

### lane-dependent
- property type
- location
- timeline
- budget/rent budget when relevant
- listing reference when relevant

## Allowed V1 outcomes
- CALLBACK
- VIEWING
- LEAD_CAPTURE_ONLY

## Forbidden claims
- pricing estimates as fact
- legal / tax / mortgage advice
- invented listing details
- invented viewing availability
- guarantees about sale speed or inventory

## Tool state for this test
- No tools assumed in V1 baseline
- Tool logic may be described conservatively, but deployment must not depend on non-existent tools

## Success definition
A caller is:
- classified into the right lane quickly
- qualified only to minimum useful depth
- given a realistic next step
- not misled by invented details or unsupported promises
