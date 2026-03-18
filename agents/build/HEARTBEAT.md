# HEARTBEAT.md

On heartbeat:
- read active build queues, watchlists, and project status
- detect stale patches, blocked implementation, or outdated product surfaces
- prepare diffs, implementation plans, or polish proposals
- if nothing material changed, reply `HEARTBEAT_OK`

Do not:
- deploy or perform risky production changes automatically by default
- hide build state only inside local memory
