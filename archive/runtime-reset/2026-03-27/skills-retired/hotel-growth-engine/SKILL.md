---
name: hotel-growth-engine
description: Build and run an automated hotel outreach workflow using existing GHL contacts and Google Places enrichment. Use when Adam wants to monetize hotel leads at scale, route offers by lead condition (review-agent vs web refresh vs AI recepcia), generate priority batches, and produce execution-ready outreach plans.
---

# Hotel Growth Engine

Automate hotel monetization from existing assets.

## Command

```bash
python3 ~/.openclaw/skills/hotel-growth-engine/scripts/hotel_growth_engine.py build-plan
```

Useful options:

```bash
python3 ~/.openclaw/skills/hotel-growth-engine/scripts/hotel_growth_engine.py build-plan --limit 60
python3 ~/.openclaw/skills/hotel-growth-engine/scripts/hotel_growth_engine.py build-plan --no-places
python3 ~/.openclaw/skills/hotel-growth-engine/scripts/hotel_growth_engine.py build-plan --city "Bratislava"
```

## Inputs

Default input source is latest:
- `workspace/systems/research-pipeline/runs/phase2_pain_value_interpreted_YYYY-MM-DD.json`

Optional explicit input:

```bash
python3 ~/.openclaw/skills/hotel-growth-engine/scripts/hotel_growth_engine.py build-plan --phase2 /abs/path/to/file.json
```

## Offer routing logic

Use deterministic routing per lead:
- `review-agent`: low rating or low review-count signals (reputation pain)
- `ai-recepcia`: higher ops pain and stronger value fit
- `web-refresh`: weaker ops pain or obvious website/conversion gap

## Output files

Generated to:
- `workspace/systems/research-pipeline/runs/hotel_growth_plan_YYYY-MM-DD.json`
- `workspace/systems/research-pipeline/runs/hotel_growth_plan_YYYY-MM-DD.csv`
- `workspace/systems/research-pipeline/runs/hotel_growth_plan_YYYY-MM-DD.md`

## Execution workflow

1. Run `hotel-intel` phase1→phase2 to refresh clean hotel candidates.
2. Run `hotel-growth-engine build-plan` to route offers and generate queue.
3. Start with batch A only (highest priority).
4. Move contacted leads to GHL pipeline stages:
   - New lead → Audited → Contacted #1 → Replied → Call booked → Proposal sent → Won/Lost
5. Re-run daily; never contact same lead twice in one day.

## Notes

- Google Places enrichment requires `GOOGLE_PLACES_API_KEY`.
- If Places is unavailable, run with `--no-places`; routing still works from phase2 pain/value.
- Keep this skill deterministic and file-first; n8n can consume generated CSV/JSON downstream.
