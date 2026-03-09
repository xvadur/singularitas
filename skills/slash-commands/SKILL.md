---
name: slash-commands
description: Execute and interpret Adam's slash command protocol (/chat, /exe, /system, daily commands, business/ops commands). Use when user sends a slash command, asks what commands exist, or asks how command routing should work.
---

# Slash Commands

Single source of truth for command behavior and routing.

## Mode contracts (strict)

- `/chat` → conversation-first (reflection, framing, understanding). Do not force execution unless user asks.
- `/exe` → execution-first (concrete next steps, sequence, completion).
- `/system` → update core docs/protocols and confirm exact changes.

## Core daily commands

- `/sleep in <cas>`
- `/sleep out <cas>`
- `/laura out <cas>`
- `/laura in <cas>`
- `/udrzba <co> [kde]`
- `/jedlo <co>`
- `/cvicenie <typ> [trvanie]`
  - pri detailnom tréningu (série/váhy) zapisuj aj do workout DB (`pcrm.sqlite`) cez `workspace/systems/local-scripts/crm.sh` (`workout-new`, `workout-add`, `workout-day`)
- `/karol <udalost>`
- `/log <text>`
- `/expense <merchant> <amount> [category] [note]`
- `/xp add <source> <points> [note]`
- `/xp today|week|total|list|leaderboard`
- `/brief morning`
- `/brief evening`
- `/save`
- `/gif <query>`

## Daily Log Protocol

- Maintain `memory/YYYY-MM-DD.md` continuously through the day.
- Log meaningful day events even from natural chat updates (sleep, food, exercise, Karol, decisions, tasks).
- Use `/log` for explicit entries; still capture relevant implicit status updates.
- Goal: complete day timeline with minimal friction.

## Business / operations commands

- `/linear [akcia]`
- `/plan <co> <kedy>`
- `/calendar [akcia]`
- `/git [akcia]`
- `/repo-commit <conventional message>`
- `/repo-push [remote] [branch]`
- `/readme [refresh|status]`
- `/crm [akcia]`
- `/fin [akcia]`
- `/cloudflare [akcia]`
- `/obsidian [akcia]`
- `/news <tema>`
- `/gog [akcia]`
- `/airtable [akcia]`

## Command → skill routing handshake

- When a command requires a specialized workflow/tool, use the most specific skill.
- Canonical mappings:
  - `/weather` → `weather`
  - YouTube transcript/sumarizácia → `youtube-transcript`
  - GitHub issues/PR/CI → `github`
  - `/repo-commit` → `repo-commit`
  - `/repo-push` → `repo-push`
  - `/readme` → `readme-mgr`
  - Obsidian operácie → `obsidian`
  - Google Workspace operácie (mail + kalendár, business + personal) → `google-workspace`
  - Airtable operácie → `airtable` (ak dostupný), inak API fallback
  - CRM operácie → `crm` (SQLite v `workspace/crm/pcrm.sqlite`)
  - XP operácie → `xp` (`workspace/systems/local-scripts/xp.sh`)
  - Things 3 tasky → `things-mac`
  - Apple Reminders → `apple-reminders`
  - `/gif <query>` → `gifgrep` (vyhľadať GIF, vybrať najrelevantnejší a poslať do chatu)
  - Legacy wrappers (`gmail-*`, `calendar-*`) sú povolené iba kvôli spätnej kompatibilite.

## Rule

Keep this file as source-of-truth for command protocol changes. Keep `TOOLS.md` as quick operational notes only.

## Singularity dispatch commands
- `/mission <objective>` -> use `singularity-mission-dispatch`
- `/dispatch <objective>` -> use `singularity-mission-dispatch`
- `/squad run <objective>` -> use `singularity-mission-dispatch`

Expected behavior:
1. Convert objective to mission payload.
2. Run runtime dispatcher.
3. Return Done/Evidence/Blocked/Next with Linear + Telegram status.
