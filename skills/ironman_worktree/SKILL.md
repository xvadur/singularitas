---
name: ironman_worktree
description: Safe branch/worktree operating protocol for isolated implementation. Use before medium or large build changes.
---

# Ironman Git Worktree Safety

Announce at start: "Using ironman_worktree."

## Protocol

1. Confirm baseline
- Current branch status is clean enough for safe work.

2. Isolate work
- Prefer dedicated branch or worktree for non-trivial changes.

3. Verify before merge
- Required checks pass before merge or handoff.

4. Keep traceability
- Use clear commit messages and checkpoint notes.

## Safety rules

- Never run destructive git commands without explicit approval.
- Never discard unrelated local changes.
- Never merge unverified changes.

## Minimum verification

- diff reviewed,
- relevant tests/checks run,
- rollback path known.
