# Push Summary Template (before each push)

Before `git push`, paste this block (or keep as mental checklist):

```text
Push Time: <YYYY-MM-DD HH:MM>
Branch: <branch>
Remote: <remote>/<branch>
Commits pushed this batch:
- <short-hash>: <commit subject>
- <short-hash>: <commit subject>

Reason:
- <why these commits are grouped together>

Checks:
- [ ] `git status --short` is clean
- [ ] commit messages follow conventional format
- [ ] memory snapshot (`/save`) updated if context changed
- [ ] no accidental temp/bin files included

Impact:
- <one-liner on user-visible effect>
```

Post-push validation:
- `git log --oneline -n 5`
- optionally: `openclaw status` to confirm operational state
