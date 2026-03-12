#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 '<graphql-query>' [variables-json]" >&2
  exit 1
fi

: "${LINEAR_API_KEY:?LINEAR_API_KEY is not set}"
QUERY="$1"
VARS="${2:-{}}"

curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: ${LINEAR_API_KEY}" \
  --data "$(jq -cn --arg q "$QUERY" --argjson v "$VARS" '{query:$q,variables:$v}')"
