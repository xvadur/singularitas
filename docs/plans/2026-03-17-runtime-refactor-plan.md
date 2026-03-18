# Singularitas Runtime Refactor Plan

> Historical plan note: this document predates the `Obsidian -> singularitas -> firma` authority split. Treat it as superseded where it claims canonical business/project truth inside `singularitas`.

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refactor `singularitas` into a cleaner OpenClaw-aligned runtime with one main orchestrator, functional specialist workspaces, and explicit project homes for auditability.

**Architecture:** Keep `singularitas` as the main Jarvis runtime workspace and add functional specialist workspaces under `agents/`. Move runtime-local traceability into root `projects/` so mission truth is not split across chat, `tmp/`, `outputs/`, and agent-local memory. Preserve existing C-level workspaces as legacy during transition to avoid breaking current context and `.openclaw` state.

**Tech Stack:** Markdown doctrine files, OpenClaw workspace conventions, shell filesystem layout

---

### Task 1: Re-anchor root doctrine

**Files:**
- Modify: `AGENTS.md`
- Modify: `docs/workspace-overview.md`
- Modify: `docs/workspace-map.md`

**Step 1: Update the runtime topology**

Replace the C-level runtime model with:
- root workspace = `Jarvis`
- functional specialist workspaces = `research`, `growth`, `build`, `ops`, `janitor`
- legacy workspaces = `cso`, `cro`, `cmo`, `coo` retained temporarily

**Step 2: Update system-of-record rules**

Set the durable truth model to:
- `memory/` for daily continuity
- `projects/` for runtime mission truth
- `outputs/` for reviewable runtime deliverables
- `MEMORY.md` for long-term carry-forward

**Step 3: Rewrite workspace maps**

Make the docs describe the new runtime-first structure and explicitly demote `business/`, `data/`, `tmp/`, and old agent folders to migration/reference surfaces.

### Task 2: Add founder-auditable runtime surfaces

**Files:**
- Create: `agents/REGISTRY.md`
- Create: `projects/README.md`
- Create: `projects/_template/README.md`
- Create: `projects/_template/brief.md`
- Create: `projects/_template/status.md`
- Create: `projects/_template/metrics.md`
- Create: `projects/_template/watchlist.md`

**Step 1: Create runtime registry**

Add one founder-readable index that lists:
- every active agent workspace
- mission
- KPI source
- heartbeat behavior
- allowed outputs

**Step 2: Create project-home contract**

Define one runtime mission home with:
- `brief.md`
- `status.md`
- `metrics.md`
- `watchlist.md`
- `spec/`
- `artifacts/`
- `staging/`
- `handoffs/`

### Task 3: Add functional specialist workspaces

**Files:**
- Create: `agents/research/*`
- Create: `agents/growth/*`
- Create: `agents/build/*`
- Create: `agents/ops/*`
- Create: `agents/janitor/*`

**Step 1: Create minimal OpenClaw workspace skeleton**

For each workspace create:
- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`
- `TOOLS.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `memory/`

**Step 2: Make roles functional, not theatrical**

Use these missions:
- `research`: market, prospect, and knowledge discovery
- `growth`: offer, outreach, CRM, and website improvement queue
- `build`: frontend, backend, product implementation, design polish subagents
- `ops`: integrations, delivery systems, automations, client runtime
- `janitor`: health checks, drift detection, stale loops, cleanup oversight

**Step 3: Set heartbeat guardrails**

Heartbeats should:
- read explicit KPI sources and watchlists
- prepare drafts, tasks, diffs, and handoffs
- avoid external side effects without approval

### Task 4: Verify coherence

**Files:**
- Test: workspace docs and structure only

**Step 1: Verify filesystem shape**

Run:
```bash
find agents/research agents/growth agents/build agents/ops agents/janitor -maxdepth 2 -print | sort
find projects -maxdepth 2 -print | sort
```

Expected:
- all new workspaces exist
- all project-home template files exist

**Step 2: Verify doctrine references**

Run:
```bash
rg -n "cso|cro|cmo|coo|business/|data/tmp|tmp/" AGENTS.md docs/workspace-overview.md docs/workspace-map.md agents/REGISTRY.md
```

Expected:
- only intentional mentions remain, clearly labeled as legacy or migration surfaces

**Step 3: Review git diff**

Run:
```bash
git diff -- AGENTS.md docs/workspace-overview.md docs/workspace-map.md agents/REGISTRY.md projects agents/research agents/growth agents/build agents/ops agents/janitor
```

Expected:
- the refactor is additive and documentation-led
- no destructive move or risky deletion is included

**Step 4: Commit**

```bash
git add AGENTS.md docs/workspace-overview.md docs/workspace-map.md docs/plans/2026-03-17-runtime-refactor-plan.md agents/REGISTRY.md projects agents/research agents/growth agents/build agents/ops agents/janitor
git commit -m "feat(runtime): add functional lane workspace scaffold"
```
