# Xvadur E-commerce Outbound Engine v1 - Engine Spec

Status: Active  
Version: v1  
Scope: autodiely / pneuservis / support-heavy e-commerce only

## Purpose

Define the minimum repeatable engine that turns existing segment assets into:
- one selected lead batch
- one send-ready outbound packet
- one file-based tracking loop
- one founder-ready handoff when a lead is ready

The engine is a batch workflow, not a platform. Founder closing stays manual.

## Scope

### In
- support-heavy e-commerce leads already inside the autodiely / pneuservis wedge
- existing CSV-based shortlist and enrichment assets
- one shared or segment-level demo/preview asset
- personalized outbound draft creation
- file-only tracking
- founder handoff after reply or qualified call
- optional AI call qualification only for leads marked `ready_to_call`

### Out
- any new segment expansion
- CRM sync or CRM-as-source-of-truth
- automatic sending infrastructure
- custom microsite generation per lead
- AI calling for all leads
- autonomous closing without Adam

## Run Inputs

### Required run inputs

| Field | Type | Notes |
| --- | --- | --- |
| `run_id` | string | Unique batch identifier |
| `segment` | enum | `autodiely` or `pneuservis` |
| `geo_scope` | string | Default `SK` |
| `batch_size` | integer | Default `10` |
| `source_lead_file` | path | Canonical source CSV |
| `demo_asset_reference` | path | Canonical onepager/demo asset |
| `operator` | string | Usually `Jarvis` |

### Optional run inputs

| Field | Type | Notes |
| --- | --- | --- |
| `preferred_angle` | enum | `compatibility_load`, `returns_friction`, `support_chaos`, `mixed` |
| `source_outreach_reference` | path | Existing outreach reference file |
| `qualify_calls` | boolean | Default `false`; still gated by `ready_to_call` |

### Minimum lead input shape

| Field | Required | Notes |
| --- | --- | --- |
| `lead_id` | yes | Stable row key |
| `company_name` | yes | Account name |
| `website` | yes | Main domain |
| `segment` | yes | Must match v1 scope |
| `contact_email` | yes | Needed for send-ready state |
| `personalization_hook` | yes | One concrete observation |
| `pain_hypothesis` | yes | One likely problem |
| `demo_mapping` | yes | Shared or specific demo pointer |

## Stage-by-Stage Flow

| Stage | What happens | Owner | Output artifact | Exit state |
| --- | --- | --- | --- | --- |
| `run_init` | Create run shell and bind canonical sources | Jarvis | `run-manifest.json` | `initialized` |
| `batch_select` | Pick the batch from canonical lead source | CSO | `selected-leads.csv` | `batch_selected` |
| `score_and_angle` | Assign one primary pain angle and priority | CSO | updated `lead-tracker.csv` | `scored` |
| `draft_outreach` | Write subject, body, CTA, demo reference | CRO | `outreach-packet.md` | `ready_to_send` |
| `founder_send_review` | Review and decide send / revise / hold | Jarvis -> Adam | notes in tracker + packet status | `sent`, `revise_copy`, or `hold` |
| `reply_route` | Route replies into nurture, call queue, or founder handoff | Jarvis | tracker update + handoff prep | `replied`, `ready_to_call`, or `founder_handoff` |
| `ai_call_qualification` | Optional screening call for flagged leads only | CRO / CallAgent | `ai-call-queue.csv` + call summary | `qualified_for_founder`, `nurture`, `disqualified`, or `call_failed` |
| `founder_handoff` | Assemble final packet for Adam | Jarvis | `founder-handoff.md` | `founder_handoff` |

## Stage Owners

| Lane | Responsibility |
| --- | --- |
| Jarvis | run setup, routing, tracking discipline, founder packet assembly |
| CSO | lead selection, enrichment interpretation, scoring, angle assignment |
| CRO | outbound drafting, follow-up shaping, call qualification execution |
| CMO | demo asset maintenance, supporting copy maintenance |
| Adam | send judgment, real replies, founder calls, close/no-close decision |

## Handoff Rules

### CSO -> CRO
- Allowed only when each lead has `lead_id`, `contact_email`, `personalization_hook`, `pain_hypothesis`, and one `primary_pain_angle`.
- If one of these is missing, lead stays with CSO.

### CRO -> Jarvis
- Allowed only when each lead has subject, body, CTA, demo mapping, and `ready_to_send`.
- If copy is generic or the CTA is unclear, route back to CRO as `revise_copy`.

### Jarvis -> Adam
- Allowed only when the lead is either:
- `ready_to_send` and needs founder send approval
- `founder_handoff` after a meaningful reply
- `qualified_for_founder` after AI call qualification
- Adam should never receive a lead without the exact packet required by the founder handoff contract.

### Jarvis -> CallAgent
- Allowed only when `ready_to_call = true` and the call qualification packet is complete.
- Missing phone or missing reply context blocks the call.

## Success Criteria

The engine is successful when:
- one run can produce a coherent batch without redesign
- every selected lead has one owner, one state, and one next action
- every send-ready lead has personalisation plus a demo reference
- Adam can act on a handoff packet without searching across files
- the same structure can be reused for the next batch

The engine is not successful if it creates more docs but no send-ready batch or no founder-ready packet.
