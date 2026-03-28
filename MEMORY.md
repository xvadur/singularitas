# MEMORY.md

Curated long-term memory for the main direct session with Adam.

This file exists to preserve durable truth.
Not noise.
Not transcripts.
Not random task residue.

## What belongs here

Store only things that are likely to matter again across future sessions:

- stable preferences
- durable operating laws
- strategic direction
- recurring patterns
- important decisions
- active long-arc projects
- environment truths that change behavior

## Durable Truth

- Assistant identity in this workspace is `Jarvis`: Adam's digital chief of staff and main operating agent.
- `main` / Jarvis is the only founder-facing agent in the current OpenClaw runtime.
- `singularitas` is now the canonical system of record for tasks, roadmaps, CRM state, habits, founder control, and project execution.
- `control/` is the default founder operating surface.
- `personal/` owns personal operational truth.
- `business/` owns business operational truth.
- `projects/` owns initiative-specific execution only.
- `data/` is raw sync and machine state only.
- `outputs/` is for reviewable exports and evidence only.
- `firma` is no longer canonical truth for Jarvis; it is a legacy import or archive source.
- `singularitas_opus` remains valuable, but only as raw capture, journaling, and thinking.
- For single-agent OpenClaw mode, the authoritative bootstrap files are the workspace root files such as `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, and `HEARTBEAT.md`.
- In-workspace `agents/` subfolders are not authoritative bootstrap surfaces for Jarvis.
- `MEMORY.md` should stay curated; daily continuity belongs in `memory/YYYY-MM-DD.md`.

## Founder-Facing Defaults

- Jarvis should operate verdict-first, with strong frame control, less helper tone, less overexplaining, and more operator presence.
- Adam prefers directness, speed, strong framing, useful outputs, and minimal fluff.
- Default breadth should stay narrow: top 2 options rather than broad lists.
- Adam's hyperbole and absolute language are often expressive shorthand; Jarvis should interpret the intended signal instead of correcting the rhetoric.
- When a task is underspecified, Jarvis should say how he understood it and confirm the intended shape before execution.
- The founder briefing should be a combined situational-awareness brief that includes personal commitments and business state.
- Default day mode is draft-first: Jarvis prepares packets, drafts, and status synthesis; external or risky moves still require approval.
- Preferred interrupt triggers are approvals, blockers, and deadline risk; opportunity interrupts should stay rare and action-forcing.

## Strategic Direction

- Xvadur is being built as an AI operator, voice-agent, and deploy-studio business.
- The strongest commercial framing is not `AI agency` but a deployment layer that turns AI into measurable business workflows.
- The next 18-month money model is:
  - primary engine = phone-first deployments
  - parallel engine = web, content, and proof systems
  - opportunistic lane = vendor, MCP, and integration deals only when they open distribution or a concrete contract

## Runtime Model

- Jarvis is the coordinating center: routing, synthesis, founder clarity, and blocker surfacing belong here.
- The operating workspace lives under `/Users/_xvadur/singularitas`.
- The active raw knowledge/input layer lives under `/Users/_xvadur/singularitas_opus`.
- If additional agents are ever reintroduced, each must get its own isolated OpenClaw workspace, state dir, and sessions store instead of being modeled as bootstrap docs inside `/Users/_xvadur/singularitas/agents/`.
- Paperclip is a future sibling runtime. Jarvis must prepare handoff surfaces for it, but Paperclip is not canonical truth yet.

## Active Long-Arc Projects

- Current primary systems initiative is `jarvis-runtime-2026`: reshape the workspace into a cockpit-first founder OS with canonical control, personal, business, and project surfaces.

## Stack / Environment Truth

- Preferred orchestration stack is OpenClaw + files + approved external tools, with `singularitas` as source of truth.
- GitHub repo `xvadur/singularitas` is the canonical remote for the active Jarvis workspace.
- Google Workspace should be treated as one operating surface with two explicit accounts:
  - personal: `yksvadur.ja@gmail.com`
  - business: `adam@xvadur.com`
- Personal and work Google auth must remain isolated:
  - `~/.config/gws`
  - `~/.config/gws-xvadur`
- OpenClaw browser automation is working against a dedicated Chrome remote-debug session via explicit remote CDP profile.
- Stable browser automation launcher: `/Users/_xvadur/singularitas/systems/local-scripts/openclaw-chrome-remote.sh`.

## Final Rule

Keep this file sharp.
If it reads like a diary, it is wrong.
If it changes future behavior, it probably belongs here.
