# Dentist Voice Reception Playbook

## Core goals
- Capture patient intent quickly.
- Book appointment to correct calendar slot.
- Handle FAQs (hours, address, insurance basics).
- Escalate urgent/clinical questions to human.

## Mandatory call flow
1. Greeting + clinic identity
2. Intent detect: booking / reschedule / cancel / info
3. Collect essentials: name, phone, reason, preferred time
4. Offer concrete slots (if available)
5. Confirm appointment summary
6. Send confirmation + fallback contact channel

## Guardrails
- No medical diagnosis.
- For pain/urgent symptoms: recommend immediate human contact / emergency path.
- Never invent unavailable slots.

## QA scenarios (minimum)
- New patient booking
- Existing patient reschedule
- Cancellation
- No slot available
- Urgent pain caller
- Caller with unclear speech
- Caller asks pricing
- Caller asks insurance
- Handoff to receptionist
- Callback failure path
