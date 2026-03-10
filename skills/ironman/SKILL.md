---
name: ironman
description: Unified execution layer with 3 packages: low (quick tasks), default (standard delivery), high (large strategic projects like Singularity).
---

# Ironman

Single orchestrator over Ironman modules.

## Packages

- `ironman low` -> quick tasks (minimal planning)
- `ironman default` -> standard chain
- `ironman high` -> large project governance

## Package routing

### LOW
Use when task < 30 min and low risk.
Flow:
1. objective
2. 3-5 steps
3. execute
4. verify

Uses: `ironman_mode`, `ironman_execute`, `ironman_verify`.

### DEFAULT
Use for normal delivery.
Flow:
1. `ironman_brainstorm`
2. `ironman_plan`
3. `ironman_execute` or `ironman_subagent`
4. `ironman_verify`

### HIGH
Use for multi-day/strategic work (e.g. Singularity).
Flow:
1. design gate
2. phased plan
3. worktree safety
4. subagent packets with reviews
5. checkpoint governance
6. final verification + residual risk report

Uses: all Ironman modules including `ironman_worktree` and `ironman_debug`.

## Default behavior

If package not specified, use `default`.


## Automatic package gate

- If estimated effort > 2h -> do not use `low`; use at least `default`.
- If task touches more than 1 integration/tool boundary -> use `default` or `high`.
- If task is multi-day, cross-team, or architectural -> force `high`.
- If uncertain, escalate one level up (prefer safety over speed).
