# HEARTBEAT.md

On heartbeat:
- inspect explicit automation health, rollout status, and operational watchlists
- detect stale incidents, missing runbooks, and blocked delivery steps
- prepare runbooks, remediation tasks, and rollout packets
- if nothing material changed, reply `HEARTBEAT_OK`

Do not:
- perform risky external changes automatically by default
- rely on chat memory as the only operational record
