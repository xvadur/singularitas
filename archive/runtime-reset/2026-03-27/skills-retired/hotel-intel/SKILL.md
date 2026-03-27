---
name: hotel-intel
description: Hotel lead intelligence pipeline for GHL contacts. Use when qualifying hotel/hostel leads from GoHighLevel, scoring pain/value, generating prioritized outreach shortlists, and exporting CSV/JSON reports for sales execution.
---

# Hotel Intel

Production-oriented wrapper around Adam's working pipeline.

## Commands

```bash
python3 ~/.openclaw/skills/hotel-intel/scripts/hotel_intel.py phase1
python3 ~/.openclaw/skills/hotel-intel/scripts/hotel_intel.py phase2
python3 ~/.openclaw/skills/hotel-intel/scripts/hotel_intel.py phase3
python3 ~/.openclaw/skills/hotel-intel/scripts/hotel_intel.py phase4
python3 ~/.openclaw/skills/hotel-intel/scripts/hotel_intel.py run-all
python3 ~/.openclaw/skills/hotel-intel/scripts/hotel_intel.py summary
```

## What each phase does

- `phase1`: pulls GHL contacts, runs hygiene + base scoring, exports clean Top20
- `phase2`: enriches Top20 with interpreted pain/value summaries and offer angle
- `phase3`: builds Top5 outreach pack with first-touch drafts
- `phase4`: builds D1/D3/D5/D8/D12 sequence engine for Top5
- `run-all`: phase1 + phase2 + phase3 + phase4 in sequence
- `summary`: prints latest output paths and top companies

## Output files

- `workspace/systems/research-pipeline/runs/phase1_clean_top20_YYYY-MM-DD.(json|csv)`
- `workspace/systems/research-pipeline/runs/phase2_pain_value_interpreted_YYYY-MM-DD.(json|csv)`
- `workspace/systems/research-pipeline/runs/phase3_top5_outreach_pack_YYYY-MM-DD.(json|csv|md)`
- `workspace/systems/research-pipeline/runs/phase4_sequence_engine_top5_YYYY-MM-DD.(json|md)`

## Requirements

- HighLevel token/location configured in underlying scripts
- Python 3.x

## Notes

- This skill is deterministic and file-driven (no n8n required).
- Extend scoring rules in scripts as needed; keep JSON schema stable for downstream automation.
