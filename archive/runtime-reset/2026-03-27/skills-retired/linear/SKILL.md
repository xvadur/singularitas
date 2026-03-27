---
name: linear
description: Work with Linear issues, projects, teams, cycles, and comments via the Linear GraphQL API. Use for execution tracking, issue creation, status updates, and project alignment in Singularity workflow.
metadata:
  {"openclaw":{"requires":{"bins":["curl","jq"],"env":["LINEAR_API_KEY"]},"primaryEnv":"LINEAR_API_KEY"}}
---

# Linear

Use Linear via the GraphQL API at `https://api.linear.app/graphql`.

## Default usage

- create/triage issues
- update execution status
- map work to deliverables
- inspect projects, teams, cycles, and comments

## Rules

- avoid duplicate tickets; update existing first
- prefer a single larger query over many tiny requests
- when mutating data, confirm target item details from user context first
- when possible, fetch ids first, then perform the mutation
- summarize what changed after write operations

## Read operations

Use `curl` with `Authorization: $LINEAR_API_KEY` and GraphQL JSON payloads.

Example team lookup:

```bash
curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $LINEAR_API_KEY" \
  --data '{"query":"query { teams { nodes { id key name } } }"}' | jq
```

Example issue search:

```bash
curl -s https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $LINEAR_API_KEY" \
  --data '{"query":"query { issues(first: 10) { nodes { id identifier title state { name } priority assignee { name } } } }"}' | jq
```

## Write operations

Typical flow:
1. Resolve ids (team / issue / project / state).
2. Run one mutation.
3. Return the changed item identifier/title/state.

## Helper scripts

- `scripts/linear.sh` — richer wrapper for common Linear operations
- `scripts/linear-gql.sh` — thin GraphQL helper for custom queries

## Common objects to fetch

- teams: `id key name`
- issues: `id identifier title description priority`
- issue state: `state { id name type }`
- assignee: `assignee { id name email }`
- project: `project { id name }`
- cycle: `cycle { id number name }`

## Notes

- This skill becomes eligible only when `LINEAR_API_KEY` is available.
- Workspace skills are picked up on the next new OpenClaw session.
