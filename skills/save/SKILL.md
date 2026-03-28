---
name: save
description: Save the current conversation's relevant context into the workspace memory system. Use when the user says `/save`, "save this", "uloz toto", "zapamataj si toto", or asks to capture the current progress/decisions/state. On trigger, update today's `memory/YYYY-MM-DD.md` with distilled continuity and append today's `memory/logs/YYYY-MM-DD.md` with a higher-detail progress log. Only touch `MEMORY.md` when the information is durable beyond today.
---

# Save

On trigger, treat `/save` as a structured capture command, not a generic reply.

## Goal

Preserve the current relevant context into the workspace in two layers:

1. `memory/YYYY-MM-DD.md` = distilled daily continuity
2. `memory/logs/YYYY-MM-DD.md` = detailed daily progress log

Use `MEMORY.md` only for durable truths that should affect future behavior beyond the day.

## Required behavior

When invoked:

1. Infer today's date from the current runtime date.
2. Ensure these files exist:
   - `memory/YYYY-MM-DD.md`
   - `memory/logs/YYYY-MM-DD.md`
3. Append a concise but useful entry to the daily log.
4. Update the daily memory with distilled continuity from the current context.
5. If and only if the current context contains a durable preference, decision, environment truth, or long-arc project update, also append a short durable-memory candidate to `MEMORY.md`.
6. Reply with a short confirmation of what was saved.

## What goes where

### Daily log (`memory/logs/YYYY-MM-DD.md`)
Append a dated bullet block that captures:
- what was worked on
- what was attempted
- what failed
- what was fixed
- what is currently in motion
- useful operational context that would be too detailed for daily memory

This is the richer trace.

### Daily memory (`memory/YYYY-MM-DD.md`)
Append only distilled continuity:
- important decisions
- state changes that matter tomorrow
- new blockers or resolved blockers
- active fronts
- facts needed to resume work fast

Keep it shorter and more legible than the log.

### Durable memory (`MEMORY.md`)
Only append when the user has revealed or changed something that should persist beyond today, such as:
- stable preferences
- durable operating rules
- meaningful strategic direction changes
- recurring patterns
- environment truths that change behavior

Do not dump day-specific noise into `MEMORY.md`.

## Format guidance

### Log append block
Use this shape:

```md
## HH:MM / save
- Worked on:
- Key actions:
- Failures / friction:
- Fixes / decisions:
- Current state:
- Next likely move:
```

### Daily memory append block
Use this shape:

```md
- Decision / state:
- Active front:
- Blocker / resolution:
- Resume point:
```

Only include the lines that actually matter.

## Quality bar

A good `/save` should:
- preserve resume-relevant context
- distinguish log vs memory cleanly
- avoid dumping the whole chat transcript
- avoid writing fluff
- avoid over-promoting temporary details into `MEMORY.md`

## Final rule

`/save` is for useful continuity, not raw transcript dumping.
