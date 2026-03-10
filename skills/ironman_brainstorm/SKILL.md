---
name: ironman_brainstorm
description: Mandatory pre-execution design workflow for non-trivial work. Use before changing systems, launching campaigns, building automations, or creating new processes.
---

# Ironman Brainstorming

Announce at start: "Using ironman_brainstorm."

Use this skill whenever the task is more than a one-liner.

<HARD-GATE>
Do NOT implement, publish, or run risky actions before an approved design brief exists.
</HARD-GATE>

## Required sequence

1. Context snapshot
- What exists now?
- What is broken or missing?
- What does done look like?

2. Clarify (one question at a time)
- Ask only high-leverage questions.
- Prefer constraints, deadline, success metric first.

3. Offer 2-3 approaches
- Each option: speed, risk, complexity, maintenance cost.
- Give one recommended option and why.

4. Produce design brief
- Scope (in/out)
- Workflow or architecture
- Risks and mitigations
- Required artifacts
- Verification plan

5. Explicit approval gate
- Wait for clear user approval.

6. Handoff
- Invoke `ironman_plan`.

## Design brief template

```text
IRONMAN DESIGN BRIEF
Goal:
Scope In:
Scope Out:
Chosen Approach:
Why This Approach:
Risks:
Verification Strategy:
Artifacts to Produce:
```

## Storage path

Save approved brief to:
`/Users/_xvadur/.openclaw/workspace/reports/plans/YYYY-MM-DD-<topic>-design.md`

## Fast-path exception

Skip this skill only when Adam explicitly asks for a tiny direct action with no design impact.
