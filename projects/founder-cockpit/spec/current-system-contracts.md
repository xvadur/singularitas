# Current System Contracts

## CRM

- Purpose: relationship memory, reminders, follow-up queue
- Owner: `revenue`
- Input: contacts, interactions, reminders
- Output: leads needing action, overdue follow-ups
- State: `partial`
- Canonical DB path: `/Users/_xvadur/singularitas/data/crm/pcrm.sqlite`
- Canonical tables: `contacts`, `interactions`, `reminders`
- Required briefing projection:
  - `Leads needing action` must list open prospect contacts with next follow-up context from `reminders`
  - each item should include `contact name`, `company`, `relationship_tier`, `openclaw_status`, `next due date or due now`, and `source_ref` or contact provenance
  - `Callbacks at risk` must include open reminders with a due date, sorted by nearest due date first
  - if `due_at` is missing, the item stays visible but is marked `manual due date needed`
  - if the DB path cannot be read, print `NO_SIGNAL` and name the missing path explicitly
- Evidence: live DB exists at `/Users/_xvadur/singularitas/data/crm/pcrm.sqlite` with 2 contacts, 2 interactions, and 2 reminders; current mismatch is briefing path wiring, not missing CRM data

## Calendar / Booking

- Purpose: meeting scheduling and time commitments
- Owner: `personal-ops` and `revenue`
- Input: founder availability, qualified leads
- Output: booked meetings, scheduling commitments
- State: `partial`
- Evidence: Cal.com is part of the intended stack, but no local contract artifact exists yet

## Google Workspace

- Purpose: business and personal inbox/calendar execution
- Owner: `personal-ops` for personal, `revenue` for business communication support
- Input: emails, calendar state
- Output: drafts, scheduling context, inbox triage
- State: `partial`
- Evidence: skill exists and accounts are documented; no live pull was verified in this pass

## n8n

- Purpose: workflow glue, webhooks, downstream automation
- Owner: `integration`
- Input: trigger payloads from forms, voice, CRM, booking
- Output: writes, alerts, workflow execution state
- State: `partial`
- Evidence: strong local skill/tooling exists, but no live execution state was surfaced in this session

## Vapi

- Purpose: voice runtime and assistant behavior
- Owner: `voice`
- Input: assistant config, prompts, tools
- Output: voice assistant runtime
- State: `partial`
- Evidence: strong local references and payload artifacts exist; no visible live credential was confirmed from the current runtime config

## ElevenLabs

- Purpose: voice layer, TTS, STT, asset generation
- Owner: `voice`
- Input: voice assets, speech requests
- Output: voice synthesis / STT
- State: `partial`
- Evidence: runtime config includes an ElevenLabs API key and local STT/TTS tooling exists

## Web / Public Surface

- Purpose: Xvadur homepage, proof pages, pilot CTA, trust surface
- Owner: `web`
- Input: proof assets, copy, publish packets
- Output: public pages and CTA surfaces
- State: `partial`
- Evidence: historical site artifacts and `jozef.xvadur.com` references exist, but the new engine is not yet fully populated

## OpenClaw Runtime

- Purpose: routing, orchestration, Telegram access, agent dispatch
- Owner: `jarvis`
- Input: channel events, bindings, workspace doctrine
- Output: routed conversations and delegated execution
- State: `live`
- Evidence: `~/.openclaw/openclaw.json` exists and now carries the compatibility routing bridge
