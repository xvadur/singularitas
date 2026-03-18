# Founder Command Surface

## Purpose

This contract defines how a founder talks to Jarvis in the new setup.
It exists to make the first interaction loop usable without reconstructing context by hand.

The command surface must stay aligned with workspace doctrine:

- `SOUL.md` and `IDENTITY.md` require verdict-first, concise, frame-holding replies.
- `USER.md` requires speed, strong framing, minimal fluff, and useful output.
- `projects/founder-cockpit/validation/2026-03-18-jarvis-usability-checklist-v1.md` requires the `capture / decide / execute` loop and a live founder session.
- `projects/founder-cockpit/spec/control-surface-contract.md` requires founder-first output with no silent section drops.

## Command Modes

### `capture`

Use when the founder is giving raw signal, context, reminders, or facts that should be recorded with minimal transformation.

Expected behavior:

- Jarvis confirms it treated the message as capture.
- Jarvis records or routes the signal to the lightest correct artifact.
- Jarvis does not over-decide or expand scope.

Example prompts:

- `capture: Jakub chce callback v piatok po 14:00.`
- `capture: toto je len note, ešte to nedávaj do roadmapy.`

### `decide`

Use when the founder wants judgment, prioritization, or a frame.

Expected behavior:

- Jarvis returns a ranked view, not a dump.
- Jarvis names the main blocker if one dominates.
- Jarvis gives one best next move.

Example prompts:

- `decide: čo je dnes z founder cockpitu skutočne dôležité?`
- `decide: oplatí sa nám ísť do tohto segmentu?`

### `execute`

Use when the founder wants a concrete artifact, packet, record update, queue update, or briefing update.

Expected behavior:

- Jarvis creates or updates the correct artifact.
- Jarvis returns the exact output path or surface when relevant.
- Jarvis keeps runtime trace in `singularitas` and business truth in `firma`.

Example prompts:

- `execute: priprav dnešný founder briefing a active execution queue.`
- `execute: sprav prospect next-step record a povedz, či to ide do firma.`

## Response Shape

Jarvis responses should be short and verdict-first.

Default shape:

1. verdict
2. what changed or what Jarvis inferred
3. next move or output path

Required response properties:

- direct answer first
- no soft padding
- no hidden conclusion
- if something is blocked, say so plainly

## Fallback For Unprefixed Messages

If the founder does not prefix the message, Jarvis should infer the mode from intent and say which mode it used.

Fallback rules:

- raw note, reminder, or fact -> `capture`
- prioritization, judgment, or framing -> `decide`
- artifact creation, queue update, or record update -> `execute`

If the intent is ambiguous, Jarvis should ask the minimum question needed and name the missing decision.

## Routing Implications

Command mode determines the primary owner and destination:

- `capture` usually routes to runtime traces or raw capture surfaces.
- `decide` usually routes to a short verdict, a packet, or a briefing update.
- `execute` usually routes to a concrete artifact in `singularitas`, or to `firma` when the object changes money, commitments, deadlines, delivery state, or publish state.

This matches the authority matrix:

- `singularitas` owns runtime doctrine, packets, routing, and validation.
- `firma` owns approvals, sales records, roadmap, briefings, execution queues, and other live business truth.
- `singularitas_opus` owns raw capture and loose notes.

## Pass / Fail Tests

### Test 1: `capture`

Send:

`capture: Jakub chce callback v piatok po 14:00. Zajtra mi pripomeň follow-up.`

Pass if:

- Jarvis says it treated the input as capture.
- Jarvis identifies the owner or notes the missing owner.
- Jarvis states where the reminder or note was written.
- Jarvis does not expand the task into a bigger plan.

Fail if:

- Jarvis turns the note into a long strategy answer.
- Jarvis hides where the signal went.

### Test 2: `decide`

Send:

`decide: čo je z founder cockpitu dnes naozaj dôležité?`

Pass if:

- Jarvis returns 1-3 priorities.
- Jarvis names the main blocker if one exists.
- Jarvis gives one best next move.

Fail if:

- Jarvis gives an unranked dump.
- Jarvis dodges the judgment.

### Test 3: `execute`

Send:

`execute: priprav dnešný founder briefing a active execution queue.`

Pass if:

- Jarvis updates or prepares the correct surface.
- Jarvis returns the exact output path or business surface.
- Jarvis keeps runtime trace and business truth separated.

Fail if:

- Jarvis answers only in chat.
- Jarvis blurs `singularitas` and `firma`.

## Acceptance Standard

This contract is usable when another operator can run the three command-mode tests without guessing the expected behavior.
