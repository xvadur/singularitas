---
name: singularity-mission-dispatch
description: Dispatch Singularity missions from natural-language objectives into runtime packet graphs. Use when Adam asks to run a mission, split work across lanes, sync to Linear, and send Telegram recap.
---

# Singularity Mission Dispatch

Use this skill to run orchestration v1 in the Singularity runtime.

## When to use
- User says: "execute mission", "spusti misiu", "rozdel to agentom", "run squad", "dispatch this".
- Need to transform vague objective into structured mission payload.
- Need live Linear + Telegram orchestration evidence.

## Runtime paths
- Runtime root: `/Users/_xvadur/singularitas/projects/singularity/runtime`
- Example payloads: `/Users/_xvadur/singularitas/projects/singularity/runtime/examples`
- Project ops docs: `/Users/_xvadur/singularitas/projects/singularity/ops`

## Workflow
1. Build mission payload from user objective.
2. Save payload to `examples/mission.<slug>.json`.
3. Run dispatcher.
4. Report output as: `Done / Evidence / Blocked / Next`.

## Required payload fields
- `mission_id`
- `objective`
- `priority` (`P0|P1|P2`)
- `deadline` (ISO timestamp)
- `mission_type` (`voice_delivery|sales_batch|delivery_readiness|runtime_health|generic`)
- `success_criteria` (non-empty array)

Optional:
- `constraints`
- `requested_by`
- `approval_class`

## Commands
```bash
cd /Users/_xvadur/singularitas/projects/singularity/runtime
npm run dispatch -- ./examples/mission.<slug>.json
```

Live mode env (if missing):
- `LINEAR_API_KEY`
- `LINEAR_TEAM_ID`
- `SINGULARITY_TELEGRAM_TARGET` (for recap)

## Safety and gates
- High-risk packet types stay in `approval_pending` until valid approval token.
- Approval token regex:
`^APR-[0-9]{8}-[a-z0-9\\-]+-[a-f0-9]{6,12}$`
- Respect routing, approval, and handoff rules from this skill's references first.
- Use runtime ops docs only as execution companions, not as the primary contract source.

## Output contract
Always return:
- Done
- Evidence
- Blocked
- Next

## Reference
Read:
`references/mission-dispatch-reference.md`
`references/routing-v1.md`
`references/approval-schema-v1.md`
