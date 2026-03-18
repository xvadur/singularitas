# 2026-03-18 Jarvis Usability Checklist v1

## Goal

Close the first founder interaction loop end-to-end:

1. founder writes to Jarvis in Telegram
2. Jarvis loads the right startup context
3. Jarvis classifies the request as `capture`, `decide`, or `execute`
4. Jarvis creates or updates the right artifact
5. Jarvis promotes business truth into `firma` when needed
6. Jarvis replies with a short verdict and the next move

`usable v1` means one real morning session passes this loop.
Config-only checks do not count.

## Companion artifacts

- Live ingress slice: `/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-live-ingress-check.md`
- Startup contract: `/Users/_xvadur/singularitas/projects/founder-cockpit/spec/startup-contract.md`
- Founder command surface: `/Users/_xvadur/singularitas/projects/founder-cockpit/spec/founder-command-surface.md`
- CRM briefing integration: `/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-crm-briefing-integration.md`
- Promotion rules: `/Users/_xvadur/singularitas/projects/founder-cockpit/spec/promotion-rules.md`
- Founder day runbook: `/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-founder-day-runbook.md`
- Parallel workboard: `/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-parallel-workboard.md`

## Canonical contract

- Live ingress path: `Telegram -> OpenClaw -> Jarvis (main)`
- Startup reads for every direct founder session:
  - `/Users/_xvadur/singularitas/SOUL.md`
  - `/Users/_xvadur/singularitas/IDENTITY.md`
  - `/Users/_xvadur/singularitas/USER.md`
  - `/Users/_xvadur/singularitas/memory/2026-03-18.md`
  - `/Users/_xvadur/singularitas/memory/2026-03-17.md`
  - `/Users/_xvadur/singularitas/MEMORY.md`
- Default founder briefing surface: `/Users/_xvadur/firma/briefings/founder-cockpit.md`
- Default business source of truth: `/Users/_xvadur/firma`
- Runtime trace home: `/Users/_xvadur/singularitas/projects/founder-cockpit`
- Raw capture home: `/Users/_xvadur/singularitas_opus`
- Default output rule:
  - runtime packets, handoffs, watchlists, validation notes, blocked-system traces -> `singularitas`
  - approvals, sales records, roadmap, publishing queue, founder briefings, active execution queue -> `firma`
  - raw notes, loose capture, reflections, knowledge assets -> `singularitas_opus`

## Founder command surface

Use explicit mode prefixes until inference is boringly reliable:

- `capture:` record the signal with minimal transformation
- `decide:` rank, judge, or frame what matters
- `execute:` create or update the packet, task, record, queue, or briefing

If the founder sends an unprefixed message, Jarvis should say which mode it inferred.

## Gate 1: Live ingress

- Status: `ready for live test`
- Existing baseline: `/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-runtime-smoke-test.md`
- Send: `ping jarvis live ingress 2026-03-18`
- Pass if:
  - the message lands in `main` (`Jarvis`)
  - Jarvis replies in the new posture, not legacy C-level framing
  - the reply reflects current runtime facts, not generic filler
- Fail if:
  - no reply arrives
  - the wrong agent answers
  - the answer ignores the active founder-cockpit context

## Gate 2: Startup contract

- Status: `defined, not yet proven in one live founder session`
- Jarvis must know on startup:
  - what to read
  - what the default founder briefing surface is
  - what the default business source of truth is
  - where runtime output vs business output goes
- Pass if:
  - when asked for current context, Jarvis correctly names the startup surfaces above
  - founder briefing answers the required sections from `projects/founder-cockpit/spec/control-surface-contract.md`
  - missing sources are shown as `NO_SIGNAL`, never silently dropped

## Gate 3: Founder command surface

- Status: `partially defined, needs live command proof`
- Test A:
  - Send: `capture: Jakub chce callback v piatok po 14:00. Zajtra mi pripomeň follow-up.`
  - Pass if Jarvis:
    - confirms it treated the message as `capture`
    - names the owner (`revenue` unless another owner is explicit)
    - records the reminder in CRM if live, or explicitly falls back to a runtime note while naming the CRM block
    - replies with where it wrote the result
- Test B:
  - Send: `decide: čo je dnes z founder cockpitu skutočne dôležité?`
  - Pass if Jarvis:
    - returns 1-3 priorities, not a long dump
    - names the main blocker if one dominates
    - gives one best next move
- Test C:
  - Send: `execute: priprav dnešný founder briefing a active execution queue.`
  - Pass if Jarvis:
    - updates the briefing and queue surfaces
    - returns the exact output paths
    - keeps runtime trace in `singularitas` and business truth in `firma`

## Gate 4: Promotion behavior

- Status: `defined in doctrine, needs 2-3 live cases`
- Keep in `singularitas`:
  - route and contract notes
  - runtime packets and handoffs
  - validation logs
  - blocked-system traces
- Promote to `firma`:
  - approvals
  - sales and prospect records
  - roadmap changes
  - founder briefings
  - active execution queue items that affect real business state
  - publishing queue changes
- Keep in `singularitas_opus`:
  - raw founder capture
  - loose ideas
  - reflections and knowledge notes
- Promotion test set:
  - Note-only idea:
    - Send: `capture: nápad na Narrative Watchtower SK, ešte to nedávaj do roadmapy`
    - Correct behavior: stays as capture, not promoted into `firma`
  - Sales truth:
    - Send: `execute: z Dentmax callu sprav prospect next-step record`
    - Correct behavior: creates or updates `/Users/_xvadur/firma/sales/prospects/...`
  - Approval truth:
    - Send: `execute: sprav approval packet na homepage/proof publish`
    - Correct behavior: runtime trace stays in `singularitas`, canonical approval lands in `/Users/_xvadur/firma/approvals/...`

## Gate 5: First real records

- Status: `minimum baseline already exists`
- Existing business truth surfaces:
  - founder cockpit record: `/Users/_xvadur/firma/briefings/founder-cockpit.md`
  - daily founder briefing: `/Users/_xvadur/firma/briefings/2026-03-18-founder-briefing.md`
  - active execution queue: `/Users/_xvadur/firma/briefings/2026-03-18-active-execution-queue.md`
  - approval packet: `/Users/_xvadur/firma/approvals/2026-03-18-web-proof-approval-packet.md`
  - sales prospect record: `/Users/_xvadur/firma/sales/prospects/2026-03-12-dentmax-bohus-call.md`
  - roadmap surface: `/Users/_xvadur/firma/roadmap/current.md`
- Pass condition:
  - Jarvis can read these as real objects, not placeholders
  - at least one of them gets updated from a live founder session

## Gate 6: CRM / relationship memory

- Status: `data exists, path contract still needs live briefing proof`
- Current local source:
  - `/Users/_xvadur/singularitas/data/crm/pcrm.sqlite`
  - `contacts=2`
  - `interactions=2`
  - `reminders=2`
- Pass if:
  - Jarvis uses this exact DB path as the relationship-memory source
  - the founder briefing section `Leads needing action today` stops being `NO_SIGNAL`
  - at least one follow-up or reminder appears in the briefing with source attribution
- Fails if:
  - the DB exists but the briefing still behaves as if CRM is missing
  - path drift remains hidden

## Gate 7: Feedback loop

- Status: `needs one practical tuning cycle`
- Jarvis must be adjustable through files plus real usage, not redesign work
- Write location rules:
  - same-day tuning -> `/Users/_xvadur/singularitas/memory/2026-03-18.md`
  - durable behavior and preference changes -> `/Users/_xvadur/singularitas/MEMORY.md`
  - founder briefing format changes -> `/Users/_xvadur/singularitas/projects/founder-cockpit/spec/control-surface-contract.md`
  - routing or promotion rule changes -> `/Users/_xvadur/singularitas/projects/founder-cockpit/spec/*.md`
- Feedback test messages:
  - `feedback: briefuj ma tvrdšie a max 5 riadkov`
  - `feedback: approvals chcem pred active execution queue`
- Pass if Jarvis:
  - applies the change to the correct file or cites the correct file to update
  - does not force a bigger redesign than necessary

## Gate 8: Canonical daily loop

- Status: `defined, not yet closed end-to-end`
- Morning open order:
  1. `/Users/_xvadur/firma/briefings/founder-cockpit.md`
  2. latest founder briefing in `/Users/_xvadur/firma/briefings/`
  3. latest active execution queue in `/Users/_xvadur/firma/briefings/`
  4. pending approval records in `/Users/_xvadur/firma/approvals/`
  5. `/Users/_xvadur/firma/roadmap/current.md`
- Founder gives 1-3 priorities
- Jarvis returns:
  - ranked order
  - the main front
  - packets or records created
  - approvals needed
  - one best next move
- Daily loop test:
  - Send: `decide: dnes priority 1) CRM restore 2) SIP vendor calls 3) web proof approval. Zoraď to.`
  - Then send: `execute: z prvých dvoch sprav packets a update active execution queue.`
- Pass if:
  - Jarvis updates the queue and any needed runtime packet surfaces
  - Jarvis does not lose the founder briefing as the default control surface

## First live session script

Use this exact sequence for the first real founder morning:

1. `ping jarvis live ingress 2026-03-18`
   - Correct answer: short reply proving Jarvis is live in the new posture and aware of current founder-cockpit state
2. `capture: Jakub chce callback v piatok po 14:00. Zajtra mi pripomeň follow-up.`
   - Correct answer: confirms capture, owner, due date, and where it was written
3. `decide: čo je z founder cockpitu dnes naozaj dôležité?`
   - Correct answer: 1-3 priorities and one best next move
4. `execute: priprav dnešný founder briefing a active execution queue.`
   - Correct answer: updates the files and returns the paths
5. `execute: z Dentmax callu sprav prospect next-step record a povedz, či to ide do firma.`
   - Correct answer: promotes the business truth into `firma` and explains why
6. `execute: sprav approval packet na homepage/proof publish.`
   - Correct answer: updates runtime trace plus canonical approval record, then asks only for the real founder decision

## Current baseline score

- [x] Route bridge exists at config level
- [x] Founder briefing surface exists in `firma`
- [x] Active execution queue exists in `firma`
- [x] At least one approval record exists
- [x] At least one sales record exists
- [x] Roadmap surface exists
- [x] CRM database exists locally
- [ ] Live Telegram ingress is proven
- [ ] CRM-fed briefing section is proven live
- [ ] Promotion behavior is proven on 2-3 real cases
- [ ] One full founder morning loop is recorded as passed

## Verdict

This is no longer an architecture problem.
The main remaining gap is one practical founder day that proves ingress, CRM-fed briefing, promotion behavior, and command surface in a real Telegram loop.
