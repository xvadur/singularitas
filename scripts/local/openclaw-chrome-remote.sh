#!/usr/bin/env bash
set -euo pipefail

PORT="${OPENCLAW_CHROME_DEBUG_PORT:-60105}"
CHROME_BIN="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
USER_DATA_DIR="${OPENCLAW_CHROME_USER_DATA_DIR:-$HOME/Library/Caches/openclaw-chrome-remote}"

mkdir -p "$USER_DATA_DIR"

exec "$CHROME_BIN" \
  --remote-debugging-port="$PORT" \
  --user-data-dir="$USER_DATA_DIR" \
  --no-first-run \
  --no-default-browser-check \
  about:blank
