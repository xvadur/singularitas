# Startup Contract

## Purpose

Define what Jarvis must load before answering a direct founder session and where the result of that session should land.

This is the startup contract for `live founder use`, not a generic workspace note.

## Read Order

For every direct founder session, Jarvis must load these in this order:

1. `/Users/_xvadur/singularitas/SOUL.md`
2. `/Users/_xvadur/singularitas/IDENTITY.md`
3. `/Users/_xvadur/singularitas/USER.md`
4. `/Users/_xvadur/singularitas/memory/2026-03-18.md`
5. `/Users/_xvadur/singularitas/memory/2026-03-17.md`
6. `/Users/_xvadur/singularitas/MEMORY.md`
7. `/Users/_xvadur/singularitas/projects/founder-cockpit/brief.md`
8. `/Users/_xvadur/singularitas/projects/founder-cockpit/status.md`
9. `/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-jarvis-usability-checklist-v1.md`

If a file is missing, Jarvis should surface that as `NO_SIGNAL` or `missing file`, not silently continue as if the surface existed.

## Default Surfaces

- Default founder briefing surface: `/Users/_xvadur/firma/briefings/founder-cockpit.md`
- Default business source of truth: `/Users/_xvadur/firma`
- Default runtime mission home: `/Users/_xvadur/singularitas/projects/founder-cockpit`
- Default raw capture home: `/Users/_xvadur/singularitas_opus`

The founder briefing is the first business-facing surface Jarvis should prefer for daily control-surface output.

## Output Routing

Jarvis must route output by object type:

- Runtime traces, packets, handoffs, validation notes, watchlists, and blocked-system state -> `singularitas`
- Approvals, sales records, roadmap items, publishing queues, founder briefings, and execution queues -> `firma`
- Raw notes, loose capture, and knowledge assets -> `singularitas_opus`

If a response changes money, commitments, deadlines, ownership, delivery state, or publish state, it belongs in `firma`.

## Founder Session Behavior

Jarvis should treat direct founder messages as one of three modes:

- `capture` - preserve the signal with minimal transformation
- `decide` - rank, judge, or frame the signal
- `execute` - create or update the relevant artifact

If the message is unprefixed, Jarvis should name the inferred mode in the reply.

## Proof Status

Current repo evidence supports the contract structure, but live ingress is still a separate verification step.

Evidence in the repo:

- `projects/founder-cockpit/brief.md` already defines the founder cockpit objective and source systems.
- `projects/founder-cockpit/status.md` says the workbench is only `partial` and the CRM path still needs contract cleanup.
- `projects/founder-cockpit/validation/2026-03-18-jarvis-usability-checklist-v1.md` already names the live ingress, startup contract, command surface, promotion behavior, CRM, feedback loop, and daily loop gates.
- `projects/founder-cockpit/validation/2026-03-18-runtime-smoke-test.md` confirms the route bridge at config level, but explicitly says live Telegram ingress was not exercised.

## Live Test Condition

This contract is only considered usable when a real founder session confirms:

1. Jarvis loaded the startup surfaces in order.
2. Jarvis named the default briefing surface correctly.
3. Jarvis routed output into the correct home based on object type.
4. Jarvis responded with a short verdict and next move.
5. A live Telegram message reached `Jarvis (main)` through OpenClaw.
