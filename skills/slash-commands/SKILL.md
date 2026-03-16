---
name: slash-commands
description: Interpret and execute Adam's slash command protocol. Use when the user sends a slash command, asks what commands exist, or asks how command routing should work across chat, execution, system updates, search, briefs, CRM, Google Workspace, Linear, GitHub, GIF lookup, and related operating actions.
---

# Slash Commands

Use this skill as the source of truth for slash command behavior in this workspace.

## Core rule

A slash command is not just text formatting.
It is an operating intent.

When a slash command appears:
1. identify the mode
2. identify the target workflow
3. route to the most specific active skill or tool
4. do not invent commands or legacy routes that no longer exist

## Mode contracts

### `/chat`
Use for:
- reflection
- framing
- brainstorming
- interpretation
- strategic discussion

Behavior:
- conversation-first
- do not force execution unless Adam asks
- clarify the real question if the prompt is fuzzy

### `/exe`
Use for:
- execution
- concrete next steps
- file changes
- system actions
- task movement

Behavior:
- execution-first
- prefer action over discussion
- return proof, outputs, or exact next steps

### `/system`
Use for:
- core doctrine changes
- operating model changes
- workspace policy changes
- config/architecture updates

Behavior:
- update the relevant source-of-truth files
- confirm exactly what changed
- prefer docs and files over chat-only conclusions

## High-value direct commands

### `/save`
Purpose:
- persist current conversation context into memory

Behavior:
- update `memory/YYYY-MM-DD.md`
- if something is durable across days, also update `MEMORY.md`
- keep saved context distilled, not transcript-like

### `/brief morning`
Purpose:
- generate the morning brief

Route:
- use `morning-brief`
- prefer `natural20-api-brief` as AI source

### `/brief evening`
Purpose:
- produce a short end-of-day synthesis

Behavior:
- summarize what moved
- identify unfinished loops
- name the most important next move for tomorrow
- save to daily memory if useful

### `/gif <query>`
Purpose:
- find a relevant GIF for chat/content

Route:
- use `gifgrep`

## Business / operating commands

### `/plan <goal>`
Route:
- `plan`

Use for:
- creating a structured execution plan

### `/fast <task>`
Route:
- `fast`

Use for:
- rapid-response framing and immediate next action

### `/news <topic>`
Route:
- `natural20-api-brief` first for AI topics
- otherwise `brave-search`

### `/search <query>`
Route:
- `brave-search`

### `/calendar ...`
### `/gog ...`
Purpose:
- Google mail/calendar operations

Route:
- `google-workspace`

Rule:
- choose account by intent:
  - business → `adam@xvadur.com`
  - personal → `yksvadur.ja@gmail.com`

### `/crm ...`
Route:
- `crm`

Use for:
- contacts
- interactions
- reminders
- follow-up state

### `/linear ...`
Route:
- `linear`

Use for:
- issue/project/status operations

### `/github ...`
### `/git ...`
Route:
- `github` for GitHub-side PR/issues/CI work
- use direct repo actions only when the task is local git work rather than GitHub workflow

### `/cloudflare ...`
Route:
- `cloudflare-toolkit`

### `/obsidian ...`
Route:
- prefer direct file work in the Obsidian vault when enough
- use `obsidian` skill only if it exists and is active

### `/downloads <query>`
Route:
- `business-development` only if the real task is lead/business discovery
- otherwise ask what output is actually wanted

## Daily logging commands

These should update `memory/YYYY-MM-DD.md` when used.

### `/log <text>`
- add concise daily log entry

### `/sleep in <time>`
### `/sleep out <time>`
### `/jedlo <what>`
### `/cvicenie <type> [duration]`
### `/expense <merchant> <amount> [category] [note]`
Behavior:
- log the event in the daily note
- if a system-of-record exists for the event, update it too when appropriate
- do not create a giant framework around simple logging

## Command routing principles

### Prefer active skills only
Do not route commands into removed or retired skills.

### Current active mappings in this workspace
- planning → `plan`
- rapid framing → `fast`
- AI/news brief → `natural20-api-brief`
- web search → `brave-search`
- Google Workspace → `google-workspace`
- CRM → `crm`
- Linear → `linear`
- GitHub → `github`
- GIF lookup → `gifgrep`
- morning brief → `morning-brief`
- content/messaging framing → `marketing-mode`
- business pipeline/outreach → `business-development`

### Do not route to retired skills
Do not reference these as active command targets:
- `readme-mgr`
- `repo-commit`
- `repo-push`
- `task-tracker`
- `habit-tracker`
- `weather`
- `things-mac`
- `singularity-mission-dispatch`
- legacy Gmail/calendar wrapper skills

## If a command is ambiguous

Do not fake certainty.
Ask one short clarifying question if needed.

Examples:
- `/git` → ask whether Adam means local git work or GitHub workflow
- `/news` → ask whether this is AI-only, business, or general
- `/calendar` → ask whether it is personal or business if the intent is unclear

## Output standard

For command handling:
- be concise
- confirm the interpreted intent when ambiguity matters
- show the result or the next action
- prefer execution over ceremony

This skill should stay lean and reflect the real command system, not historical leftovers.
