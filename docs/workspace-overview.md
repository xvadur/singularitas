# Singularitas Workspace Overview

`singularitas` is the main OpenClaw runtime workspace and the source of truth for runtime behavior.
The canonical operating model is `Obsidian -> singularitas -> firma`.

## What lives here

- root runtime files: `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `TOOLS.md`, `HEARTBEAT.md`, `MEMORY.md`, `memory/`
- `agents/`: personal-layer workspaces, business-layer workspaces, and support execution lanes
- `projects/`: runtime mission homes with packets, traces, validation, staging, and handoffs
- `outputs/`: runtime evidence and runtime handoffs
- `data/`: operational support storage for local databases, imports, and run artifacts
- `archive/`: archived legacy material that is no longer part of the active runtime
- `docs/`: workspace guides, maps, and plans
- `skills/`, `systems/`, `scripts/`: runtime support layers

`projects/` contains runtime mission truth.
`data/` is support storage, not business truth.
Anything archived under `archive/` is reference-only.

## What does not live here

- OpenClaw config, credentials, and session transcripts from `~/.openclaw/`
- master runtime doctrine stored only in Obsidian
- canonical sales, delivery, publishing, roadmap, or approval truth that belongs in `firma`
- loose temp artifacts at the workspace root

## Obsidian boundary

`singularitas_opus` is a collaboration surface for inbound notes and delivery outputs.
It is readable and editable by OpenClaw, but it is not the authoritative home of the runtime.
Only `Capture` and `KnowledgeAsset` are durably true there.

## Layer model

### Personal Layer

- `personal-ops` owns commitments, inbox/capture triage, reminders, and personal queue hygiene
- `personal-web` owns personal website maintenance, drift detection, and upgrade packets

### Business Layer

- `revenue`
- `voice`
- `integration`
- `delivery`
- `proof`
- `web`

### Support Execution Lanes

- `research`
- `growth`
- `build`
- `ops`
- `janitor`

## Revenue logic

For the next 18 months, default operating bias is:

1. primary revenue engine = phone-first deployments
2. parallel revenue engine = web/content/proof systems
3. vendor/MCP/connectors = opportunistic strategic lane only

## Navigation rule

If a document defines how the runtime should operate, keep it in `singularitas`.
If a document traces a live runtime mission, keep it in `projects/`.
If a document changes sales, delivery, approvals, roadmap, publishing, or other business state, keep canonical truth in `firma`.
If a document is meant to be consumed, verified, or handed off inside the runtime, keep it in `outputs/`.

Action-bearing business objects belong in `firma`.
