# Singularity Eco Authority Matrix

Canonical architecture:

`singularitas_opus -> singularitas -> firma`

## Workspace authority

| Surface | Canonical for | Never canonical for |
| --- | --- | --- |
| `singularitas_opus` | `Capture`, `KnowledgeAsset` | runtime state, live business state |
| `singularitas` | runtime doctrine, agents, bindings, routing, skills, scripts, system docs, packets, mission traces, heartbeats | sales state, delivery state, approvals, roadmap, publishing queue, business outputs |
| `firma` | pipeline, opportunities, decisions, approvals, roadmap, delivery state, content queue, proof assets, publishing queue, reports, sales records, client/account truth | runtime topology, bindings, skills, low-level system contracts |

## Object authority

| Object | Born in | Durable truth | Write owner |
| --- | --- | --- | --- |
| `Capture` | Obsidian | Obsidian | founder + human contributors; agents may append metadata only |
| `KnowledgeAsset` | Obsidian or extracted from work | Obsidian | founder, Jarvis, proof |
| `Packet` | singularitas | singularitas trace only | Jarvis or lane owner |
| `Party` | runtime packetization or business operations | firma | revenue |
| `Interaction` | runtime packetization or business operations | firma | revenue or delivery depending on context |
| `Opportunity` | runtime packetization or business operations | firma | revenue |
| `WorkItem` | runtime or business operations | firma | owning business function |
| `Decision` | approval process or founder action | firma | founder or explicit approver |
| `Engagement` | approved opportunity or strategic decision | firma | delivery |
| `Artifact` | runtime production or business request | firma if action-bearing | producing function until approved; then owning business function |

## Hard rule

If an object changes money, commitments, ownership, deadlines, delivery state, or publish state, it must end up in `firma`.
