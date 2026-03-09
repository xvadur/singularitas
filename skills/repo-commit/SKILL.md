---
name: repo-commit
description: Singularitas commit orchestrator. Prepare a meaningful commit with disciplined message format and optional scope.
user-invocable: true
metadata:
  {
    "openclaw": {
      "requires": {
        "bins": ["git"]
      },
      "emoji": "🧱"
    }
  }
---

# repo-commit

This is a focused execution command for meaningful commits in `Singularitas`.

## Usage
`/repo-commit <type(scope): summary>`

If no message is provided, ask for clarification.

## Steps
1. Run `git status --short`.
2. If no changes: stop and report: `No changes staged/unstaged. Nothing to commit.`
3. Stage all intentional files (or ask for explicit include list).
4. Show compact diff summary:
   - `git diff --stat --cached`
5. Validate commit message format against this regex:
   - `^(feat|fix|chore|docs|infra|refactor|test|build|ci|revert)(\([a-z0-9._-]+\))?: .{8,72}$`
6. Commit with `git commit -m "<message>"`.
7. Confirm result with:
   - `git log --oneline -n 1`
   - optionally show `git status --short`.

## Hard constraints
- No empty commits.
- One commit = one concrete change set.
- Keep message short, imperative, in EN.
- Prefix types: `feat|fix|chore|docs|infra|refactor|test|build|ci|revert`.

## Safety
- If message violates format, do not commit; ask user for corrected message.
- If diff is obviously temp-noise (`.DS_Store`, `node_modules`, binary noise), refuse and suggest cleanup.
