---
name: repo-push
description: Singularitas push protocol for clean, audited pushes aligned with heatmap discipline.
user-invocable: true
metadata:
  {
    "openclaw": {
      "requires": {
        "bins": ["git"]
      },
      "emoji": "🚀"
    }
  }
---

# repo-push

Controlled push gate for the Singularitas repository.

## Usage
`/repo-push [remote] [branch]`

Defaults:
- remote: `origin`
- branch: current branch

## Steps
1. Check clean tree: `git status --short`.
2. Show branch and upstream: `git branch --show-current` and `git rev-parse --abbrev-ref --symbolic-full-name @{u}` (if exists).
3. Show queued commits:
   - `git log --oneline -n 5`
4. If clean and branch has upstream, run `git push <remote> <branch>`.
5. If no upstream: propose exact command:
   - `git push -u <remote> <branch>`
6. Run quick validation after push:
   - `git status --short`
   - `git log --oneline -n 3`
7. Print concise push summary for Memory/operational log:
   - remote, branch, commit, timestamp.

## Safety
- Abort if working tree dirty unless user explicitly approves.
- If pre-push checks fail, offer corrective checklist from `.github/PUSH_TEMPLATE.md`.
