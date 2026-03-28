#!/usr/bin/env bash
set -euo pipefail

BASE="/Users/_xvadur/Singularitas_vault/singularitas"
INBOX="$BASE/00_Inbox"

for f in "$INBOX"/*.md; do
  [ -e "$f" ] || continue
  [ "$(basename "$f")" = "README.md" ] && [ "$(basename "$f")" = "INBOX.md" ] && continue

  # Skip if still draft or in inbox marker
  if grep -q "^category:\s*10_Projects\|^category:\s*20_Areas\|^category:\s*30_Resources\|^category:\s*40_System\|^category:\s*90_Archive" "$f"; then
    if grep -q "^category:\s*10_Projects" "$f"; then mv "$f" "$BASE/10_Projects/"
    elif grep -q "^category:\s*20_Areas" "$f"; then mv "$f" "$BASE/20_Areas/"
    elif grep -q "^category:\s*30_Resources" "$f"; then mv "$f" "$BASE/30_Resources/"
    elif grep -q "^category:\s*40_System" "$f"; then mv "$f" "$BASE/40_System/"
    elif grep -q "^category:\s*90_Archive" "$f"; then mv "$f" "$BASE/90_Archive/"
    fi
  fi

done

echo "Inbox routing done."
