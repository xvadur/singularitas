# Xvadur E-commerce Outbound Engine v1 - Tracking Schema

Status: Active  
Storage mode: file-only  
CRM dependency: none

## Purpose

Define the smallest tracking contract that keeps each run and each lead explicit in files.

Tracking must always answer:
- what run this belongs to
- what state the lead is in
- who owns the next move
- whether Adam needs to see it now

## Run-Level Fields

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `run_id` | string | yes | Unique run key |
| `created_at` | datetime | yes | Run creation time |
| `segment` | string | yes | `autodiely` or `pneuservis` |
| `geo_scope` | string | yes | Usually `SK` |
| `batch_size` | integer | yes | Usually `10` |
| `preferred_angle` | string | no | Steering hint |
| `operator` | string | yes | Usually `Jarvis` |
| `source_lead_file` | string | yes | Canonical source path |
| `demo_asset_reference` | string | yes | Canonical demo path |
| `run_state` | enum | yes | See state list below |
| `notes` | string | no | Short ops note only |

## Lead-Level Fields

### Required

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `run_id` | string | yes | Parent run |
| `lead_id` | string | yes | Stable lead key |
| `company_name` | string | yes | Account name |
| `website` | string | yes | Main domain |
| `segment` | string | yes | Scope guard |
| `contact_email` | string | yes | Needed for outbound readiness |
| `priority_score` | integer | yes | Relative priority only |
| `primary_pain_angle` | enum | yes | One angle only |
| `demo_mapping` | string | yes | Shared or specific demo pointer |
| `owner` | enum | yes | Current responsible lane |
| `lead_state` | enum | yes | Current state |
| `next_action` | string | yes | One clear next move |
| `last_updated_at` | datetime | yes | Last state change |

### Recommended

| Field | Type | Notes |
| --- | --- | --- |
| `contact_name` | string | If known |
| `contact_phone` | string | Needed only for call queue |
| `personalization_hook` | string | Concrete observation used in copy |
| `pain_hypothesis` | string | Short problem framing |
| `draft_subject` | string | Current subject line |
| `draft_body_ref` | string | Path or inline ref |
| `send_status` | string | `not_sent`, `sent`, `hold` |
| `reply_summary` | string | One-paragraph reply summary |
| `ready_to_call` | boolean | Default `false` |
| `call_status` | string | Optional call branch result |
| `handoff_status` | string | `not_ready`, `ready`, `delivered` |
| `founder_priority` | string | `high`, `normal`, `low` |

## Allowed States

### Run states
- `initialized`
- `batch_selected`
- `drafted`
- `founder_review`
- `active`
- `completed`
- `blocked`
- `cancelled`

### Lead states
- `selected`
- `scored`
- `ready_for_copy`
- `drafted`
- `ready_to_send`
- `sent`
- `replied`
- `ready_to_call`
- `qualified_for_founder`
- `founder_handoff`
- `nurture`
- `disqualified`
- `call_failed`
- `revise_copy`
- `hold`
- `won`
- `lost`

## Allowed Transitions

### Core path
- `selected -> scored`
- `scored -> ready_for_copy`
- `ready_for_copy -> drafted`
- `drafted -> ready_to_send`
- `ready_to_send -> sent`
- `sent -> replied`

### Review branches
- `ready_to_send -> revise_copy`
- `ready_to_send -> hold`
- `replied -> founder_handoff`
- `replied -> ready_to_call`
- `replied -> nurture`
- `replied -> disqualified`

### Call branch
- `ready_to_call -> qualified_for_founder`
- `ready_to_call -> nurture`
- `ready_to_call -> disqualified`
- `ready_to_call -> call_failed`
- `qualified_for_founder -> founder_handoff`

### Final branches
- `founder_handoff -> won`
- `founder_handoff -> lost`
- `nurture -> won`
- `nurture -> lost`

## Owner Defaults By State

| State | Default owner |
| --- | --- |
| `selected` | CSO |
| `scored` | CSO |
| `ready_for_copy` | CRO |
| `drafted` | CRO |
| `ready_to_send` | Jarvis |
| `sent` | Adam |
| `replied` | Jarvis |
| `ready_to_call` | CRO |
| `qualified_for_founder` | Jarvis |
| `founder_handoff` | Adam |
| `nurture` | CRO |
| `disqualified` | Jarvis |
| `call_failed` | CRO |
| `won` | Adam |
| `lost` | Adam |

## File Layout Recommendation

Recommended run folder:

`outputs/xvadur-ecommerce-outbound-engine-v1/<run_id>/`

Recommended minimum files:
- `run-manifest.json`
- `lead-tracker.csv`
- `outreach-packet.md`
- `founder-handoff.md` when at least one lead is handoff-ready
- `ai-call-queue.csv` only when at least one lead is `ready_to_call`

## Minimal Operational Rules

- One row per `run_id + lead_id`.
- No hidden state in chat.
- Every state change must also update `owner`, `next_action`, and `last_updated_at`.
- `ready_to_call` must stay `false` unless a concrete reason and call packet exist.
- `handoff_status = delivered` only after the founder packet exists and ownership changes to Adam.
- Do not add CRM IDs, delivery analytics, or extra taxonomies in canonical v1.

## Minimal Example Row

```csv
run_id,lead_id,company_name,website,segment,contact_email,priority_score,primary_pain_angle,demo_mapping,owner,lead_state,next_action,last_updated_at,ready_to_call,call_status,handoff_status
2026-03-15-sk-batch-01,AUTODIELYBB,AUTODIELYBB,https://example.sk,autodiely,hello@example.sk,7,returns_friction,shared-ecom-onepager,Jarvis,ready_to_send,Founder review before send,2026-03-15T14:10:00+01:00,false,not_applicable,not_ready
```
