# Runtime Mission Homes

`projects/` holds runtime mission homes.

Use it when a workflow, deployment, or agent task needs packetized execution truth inside the runtime.
Do not use it as the canonical home of business state.

## What belongs here

Each runtime mission should get one folder:

- `brief.md` for the current objective
- `status.md` for runtime state, owner, blockers, next move
- `metrics.md` for explicit KPI inputs and source locations
- `watchlist.md` for recurring checks, risks, and signals
- `approvals/` for review-gated decisions and approval packets
- `spec/` for working specs
- `artifacts/` for intermediate non-final working outputs
- `validation/` for outcome checks and acceptance evidence
- `content/` for proof extraction and content-ready shards
- `staging/` for active payloads, patches, and machine-facing scratch
- `handoffs/` for founder-ready or agent-ready packets
- `approved-for-firma/` for artifacts that have been promoted into business truth

## Rules

- Every mission home must declare:
  - `canonical_owner: singularitas`
  - `firma_record:` absolute path to the matching business record in `firma`
  - `status_scope: runtime only`
  - `do_not_store_business_truth_here: true`
- If a lane heartbeat needs to reason about a live mission, it should be able to do so from this folder.
- Do not hide runtime mission truth only in chat, `tmp/`, or agent-local `memory/`.
- `outputs/` is runtime evidence and handoff space, not the business output layer.
- Canonical pipeline stage, account state, roadmap state, founder approvals, and publish-ready business state do not belong here.
- Old material can stay where it is during transition, but new runtime work should prefer `projects/`.

## Shared objects

Mission homes should resolve work into explicit objects when possible:

- `Lead`
- `Account`
- `Call`
- `Follow-up`
- `Proposal`
- `Deployment`
- `Client`
- `Validation`
- `Proof Asset`
- `Web Asset`
- `Approval`
- `Partner Opportunity`

These objects may be traced here, but business truth for action-bearing objects lives in `firma`.
