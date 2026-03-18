# Promotion Rules

## Purpose

Define where founder-facing objects live and when they move from runtime trace to business truth.

This contract follows the authority matrix:

- `singularitas_opus -> singularitas -> firma`
- `singularitas_opus` is capture and knowledge
- `singularitas` is runtime doctrine, routing, packets, and traces
- `firma` is canonical business truth

## Object Classes

### `Capture`

Raw founder input, loose ideas, notes, and first-pass observations.

Destination:

- default home: `singularitas_opus`
- may be copied into `singularitas` as metadata or trace, but not promoted as business truth
- never canonical in `firma`

### `KnowledgeAsset`

Distilled note, insight, reference, or reusable context extracted from capture.

Destination:

- default home: `singularitas_opus`
- may be referenced from `singularitas`
- promote to `firma` only if it becomes action-bearing business truth

### `Packet`

Runtime instruction, handoff, checklist, or mission trace created by Jarvis or a lane owner.

Destination:

- canonical in `singularitas`
- never canonical in `firma`

### `WorkItem`

An actionable business task that affects an owner, deadline, delivery state, or publish state.

Destination:

- canonical in `firma`

### `Decision`

Founder decision, approval, rejection, or prioritized call that changes business state.

Destination:

- canonical in `firma`

### `Opportunity`

Lead, prospect, segment, account, or sale motion.

Destination:

- canonical in `firma`

### `Interaction`

Call, message, follow-up, callback, or relationship-memory entry.

Destination:

- canonical in `firma`

### `Artifact`

Output with business effect, such as approval packets, sales records, roadmap items, publishing queues, proof assets, or execution queues.

Destination:

- if it changes money, commitments, ownership, deadlines, delivery state, or publish state, canonical in `firma`
- otherwise keep the runtime trace in `singularitas`

## Destination Rules

### Keep in `singularitas_opus`

Use `singularitas_opus` for:

- raw capture
- loose founder notes
- early ideas without business commitment
- knowledge assets that are not yet action-bearing

### Keep in `singularitas`

Use `singularitas` for:

- routing and control docs
- packets and handoffs
- validation notes
- blocked-system traces
- mission evidence
- runtime-only contracts

### Promote to `firma`

Use `firma` for:

- approvals
- sales and prospect records
- founder briefings
- active execution queue items
- roadmap changes
- publishing queue changes
- client/account truth
- relationship-memory entries

## Promotion Test Cases

### Example 1: Idea only

Input:

`capture: nápad na Narrative Watchtower SK, ešte to nedávaj do roadmapy`

Expected result:

- stays in `singularitas_opus` or as a runtime trace in `singularitas`
- does not become a roadmap item in `firma`
- remains explicitly uncommitted

### Example 2: Sales truth

Input:

`execute: z Dentmax callu sprav prospect next-step record`

Expected result:

- creates or updates a prospect or interaction record in `firma`
- preserves the runtime trace in `singularitas` if needed
- the canonical business truth lives in `firma`

### Example 3: Approval truth

Input:

`execute: sprav approval packet na homepage/proof publish`

Expected result:

- runtime draft or trace stays in `singularitas`
- the canonical approval lands in `firma`
- if the item changes publish state, it must not stay only as a runtime note

## Decision Rules

Promote to `firma` when the object changes any of these:

- money
- commitments
- ownership
- deadlines
- delivery state
- publish state

Keep in `singularitas` when the object is only:

- routing
- synthesis
- trace
- validation
- packetization

Keep in `singularitas_opus` when the object is only:

- capture
- note-taking
- reflection
- knowledge extraction

## Live Test Criteria

Promotion behavior is good enough for a live founder session when:

1. Jarvis can state the target surface without guessing.
2. A capture stays out of `firma` unless it becomes committed truth.
3. A business action lands in `firma` without losing the runtime trace.
4. A publish- or approval-bearing object does not remain only in `singularitas`.
5. The founder does not need to decide storage location manually.

Fail conditions:

- the same object is stored in multiple canonical homes without one clear owner
- business truth stays only in `singularitas`
- raw capture is promoted into `firma` before it becomes committed
- Jarvis cannot explain why the object moved

## Verdict

If the object changes the business, it ends up in `firma`.
If it only helps the runtime work, it stays in `singularitas`.
If it is still raw input, it stays in `singularitas_opus`.
