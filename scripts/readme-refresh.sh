#!/usr/bin/env bash
set -euo pipefail

# Readme orchestration for Singularitas
# Keeps repo-stable: temporary generated candidate + manual merge if needed.

echo "🔧 Singularitas README flow"

if ! command -v npx >/dev/null 2>&1; then
  echo "npx not found"
  exit 1
fi

CFG=".readme-md-generator.json"
OUT="README.generated.md"
TMP_README=".README.md.singularitas.tmp"
TS="$(date '+%Y-%m-%d %H:%M:%S')"

cat > "$CFG" <<'JSON'
{
  "name": "Singularitas",
  "description": "Digital operating home for AI infrastructure and disciplined execution.",
  "github": {
    "username": "xvadur",
    "repo": "singularitas"
  }
}
JSON

echo "Preparing non-interactive generation..."

# Generator always writes README.md and asks overwrite in non-tty mode, so we use a temp swap.
if [ -f README.md ]; then
  mv README.md "$TMP_README"
  RESTORED=1
else
  RESTORED=0
fi

# Ensure tmp file restored even on failure
cleanup() {
  local code=$?
  if [ "$RESTORED" -eq 1 ] && [ -f "$TMP_README" ]; then
    mv -f "$TMP_README" README.md
  fi
  if [ -f "$TMP_README" ] && [ "$RESTORED" -eq 0 ]; then
    rm -f "$TMP_README"
  fi
  exit $code
}
trap cleanup EXIT

# Feed a default answer to skip inquirer selection reliably.
printf "\n" | npx --yes readme-md-generator -y -c "$CFG" >/tmp/readme-md-generator.log 2>&1 || {
  echo "Generator failed. Inspect /tmp/readme-md-generator.log"
  exit 1
}

if [ -f README.md ]; then
  cp README.md "$OUT"
  echo "✅ Generated candidate: $OUT"
else
  echo "Generator did not emit README.md"
  exit 1
fi

echo "Timestamp: $TS"
echo "Diff preview (first 80 lines):"
head -n 80 "$OUT"

echo "\nIf this looks good, review and merge manually with README.md to preserve branding."