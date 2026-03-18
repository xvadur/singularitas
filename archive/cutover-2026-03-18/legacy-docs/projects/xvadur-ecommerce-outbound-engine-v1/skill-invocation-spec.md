# Xvadur E-commerce Outbound Engine v1 - Skill Invocation Spec

Status: Future OpenClaw skill contract  
Intent: one minimal invocation shape for one engine run

## Invocation Shape

```json
{
  "segment": "autodiely",
  "geo_scope": "SK",
  "batch_size": 10,
  "run_mode": "new_run",
  "preferred_angle": "mixed",
  "qualify_calls": false,
  "run_id": null,
  "source_lead_file": null,
  "demo_asset_reference": null
}
```

## Parameters

| Parameter | Type | Default | Rule |
| --- | --- | --- | --- |
| `segment` | string | none | Must be `autodiely` or `pneuservis` |
| `geo_scope` | string | `SK` | Keep inside v1 target geography |
| `batch_size` | integer | `10` | Must be `> 0` |
| `run_mode` | enum | `new_run` | `new_run` or `continue_run` |
| `preferred_angle` | enum | `mixed` | `compatibility_load`, `returns_friction`, `support_chaos`, `mixed` |
| `qualify_calls` | boolean | `false` | Enables optional call branch only |
| `run_id` | string/null | `null` | Required only for `continue_run` |
| `source_lead_file` | string/null | canonical file | Override only inside approved source family |
| `demo_asset_reference` | string/null | canonical demo file | Override only inside approved demo family |

## Default Binding Rules

- If `source_lead_file` is omitted, bind to the canonical support-heavy e-commerce lead source.
- If `demo_asset_reference` is omitted, bind to the canonical e-commerce support onepager/demo.
- If `run_mode = new_run`, generate a fresh `run_id`.
- If `run_mode = continue_run`, load the existing tracker and resume from the next valid stage.
- `qualify_calls = true` does not mean all leads get called; it only allows the `ready_to_call` branch.

## Files Created Or Updated By A Run

Inside:

`outputs/xvadur-ecommerce-outbound-engine-v1/<run_id>/`

The run should create or update:
- `run-manifest.json`
- `lead-tracker.csv`
- `selected-leads.csv`
- `outreach-packet.md`
- `founder-handoff.md` only when at least one lead is handoff-ready
- `ai-call-queue.csv` only when at least one lead is `ready_to_call`

## Minimal Return Shape

```json
{
  "run_id": "2026-03-15-sk-batch-01",
  "accepted_scope": {
    "segment": "autodiely",
    "geo_scope": "SK",
    "batch_size": 10
  },
  "next_stage": "batch_select",
  "artifacts": [
    "run-manifest.json",
    "lead-tracker.csv",
    "selected-leads.csv"
  ],
  "warnings": []
}
```

## Guardrails

- Reject any segment outside autodiely / pneuservis / support-heavy e-commerce v1.
- Reject any invocation that implies CRM sync or non-file tracking.
- Reject `continue_run` when `run_id` is missing.
- Reject source-file overrides outside the approved source family.
- Do not silently expand the state vocabulary.
- Do not auto-call replied leads without `ready_to_call = true`.
- Do not create platform-level objects beyond the run folder and its files.

## Human Operator Equivalent

`Run Xvadur E-commerce Outbound Engine v1 for <segment> in <geo_scope> with batch <batch_size> and angle <preferred_angle>.`
