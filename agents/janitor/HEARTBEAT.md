# HEARTBEAT.md

On heartbeat:
- check for missing daily logs, stale project status, orphaned staging files, and silent lanes
- prepare cleanup queues, archive suggestions, and missing-record alerts
- if nothing material changed, reply `HEARTBEAT_OK`

Do not:
- delete or move material automatically by default
- confuse cosmetic reordering with meaningful hygiene work
