#!/usr/bin/env bash
set -euo pipefail

# Readme orchestration for Singularitas
# Keeps repo-stable: optional, generated snapshot + manual merge if needed.

echo "🔧 Singularitas README flow"

if ! command -v npx >/dev/null 2>&1; then
  echo "npx not found"
  exit 1
fi

CFG=".readme-md-generator.json"
OUT="README.generated.md"
TS="$(date '+%Y-%m-%d %H:%M:%S')"

echo "{\n  \"name\": \"Singularitas\",\n  \"description\": \"Digital operating home for AI infrastructure and disciplined execution.\",\n  \"github\": {\n    \"username\": \"xvadur\",\n    \"repo\": \"singularitas\"\n  }\n}\n" > "$CFG"

echo "Generating candidate README to $OUT ..."
npx --yes readme-md-generator -y -c "$CFG" -o "$OUT" >/tmp/readme-md-generator.log 2>&1 || {
  echo "Generator failed. Inspect /tmp/readme-md-generator.log";
  exit 1
}

echo "✅ Generated: $OUT"
echo "Timestamp: $TS"
echo "Diff preview (first 80 lines):"
head -n 80 "$OUT"
echo "\nIf this looks good, review and replace README.md manually for style control."