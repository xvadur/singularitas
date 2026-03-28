# Marek / realitky — Brief

## Project verdict

Marek is the current baseline real-estate voice-agent project inside the `voice` lane.
It is the first concrete staged proof that the lane can produce a narrow, phone-first, segment-specific assistant with real runtime artifacts behind it.

## What Marek is

Marek is a Slovak-speaking inbound real-estate assistant for broker call handling.
He is not the broker himself.
He is the first-line intake surface that:
- answers inbound calls
- quickly identifies what the caller needs
- captures the minimum useful information
- routes the caller toward the correct next step
- avoids overpromising
- hands real actions to the backend layer

## Who it is for

Primary working context:
- broker-side inbound handling
- real-estate use case
- Jakub / Brex-Reality-style operator context

## V1 scope

Marek V1 is for first-contact inbound handling only.
Main outcomes:
- lead capture
- callback request handling
- viewing request handling
- referral / urgent escalation handling
- clean call closure

## Not in V1 scope

Do not pretend V1 is broader than it is.
Marek V1 is not:
- a full sales closer
- a legal / tax / mortgage advisor
- a pricing authority
- a full CRM operating system
- a broad real-estate knowledge bot
- a freeform concierge for every backoffice task

## What makes this project important

This project matters because it is the current practical baseline for the whole `voice` lane.
It is not just a single client experiment.
It is the reference pack for:
- prompt quality
- lane-based call logic
- runtime boundaries
- handoff discipline
- booking / callback logic
- future segment expansion quality bar

## Current project shape

The project currently spans three realities:
1. live/staged ElevenLabs agent surface
2. backend/tooling packages in `outputs/`
3. cleaned project docs in `business/voice/clients/marek/`

This folder exists to make `business/voice/clients/marek/` the canonical working surface for review, editing, QA, and eventual send-ready packaging.

## Current bottleneck

The main bottleneck is no longer idea quality.
The main bottleneck is operational clarity:
- which runtime contract is canonical right now
- what is live vs staged
- what is actually proven vs only prepared

## Success condition

This project is in a good state when:
- one canonical prompt exists
- one canonical tool/runtime explanation exists
- current-state truth is easy to read
- QA truth is explicit
- a short Jakub-facing review summary can be produced quickly
- the project can be updated without digging through old handoffs and scattered notes
