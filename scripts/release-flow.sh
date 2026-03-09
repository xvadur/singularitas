#!/usr/bin/env bash
set -euo pipefail

set -a

# Usage: ./scripts/release-flow.sh "<commit message>"
# Example: ./scripts/release-flow.sh "feat(ops): add commit conventions"

msg="${1:-}"
if [ -z "$msg" ]; then
  echo "Usage: $0 \"<commit-message>\""
  echo "Message must follow conventional format: type(scope): summary"
  exit 1
fi

branch="$(git rev-parse --abbrev-ref HEAD)"
remote="${2:-origin}"

# Preflight
if [ -z "$(git status --porcelain)" ]; then
  echo "⚠️  No staged/unstaged changes. Nothing to commit."
  exit 0
fi

git status --short

git commit -m "$msg"

git log --oneline -n 3

echo "\nPush this commit? [y/N]"
read -r ans
if [[ "$ans" == "y" || "$ans" == "Y" ]]; then
  git push "$remote" "$branch"
  echo "\nPushed. Append summary to .github/PUSH_TEMPLATE.md checklist manually if needed."
else
  echo "Commit created locally, not pushed."
fi
