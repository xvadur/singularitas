# Singularitas Workspace Overview

`singularitas` is the main OpenClaw runtime workspace and the source of truth for the agent system.

## What lives here

- root runtime files: `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `TOOLS.md`, `HEARTBEAT.md`, `MEMORY.md`, `memory/`
- `agents/`: per-agent workspaces plus shared runtime doctrine
- `business/`: durable business source documents
- `data/`: CRM, imports, run artifacts, temporary operational files
- `outputs/`: drafts, briefs, delivery material, and handoffs
- `archive/`: legacy material kept for reference
- `docs/`: workspace guides, maps, and plans
- `skills/`, `systems/`, `scripts/`: runtime support layers

## What does not live here

- OpenClaw config, credentials, and session transcripts from `~/.openclaw/`
- master runtime doctrine stored only in Obsidian
- loose CSVs, SQLite files, one-off offers, and temp artifacts at the root

## Obsidian boundary

`singularitas_opus` is a collaboration surface for inbound notes and delivery outputs.
It is readable and editable by OpenClaw, but it is not the authoritative home of the runtime.

## Navigation rule

If a document defines how the agent should operate, keep it in `singularitas`.
If a document is meant to be consumed, drafted, or handed off to a human, it can live in `outputs/` and optionally be mirrored to Obsidian.
