---
name: goplaces
description: Search for businesses and locations using Google Places API. Use when the user wants to find dentists, hotels, or other business leads, or needs details (website, phone, rating) for a specific place.
---

# GoPlaces

Search for businesses and enrich leads with Google Places data.

## Quick start

Search for businesses:
```bash
python3 /Users/_xvadur/singularitas/skills/goplaces/scripts/places_search.py "zubna klinika bratislava"
```

Get details for a specific place (use `place_id` from search results):
```bash
python3 /Users/_xvadur/singularitas/skills/goplaces/scripts/places_search.py --details "PLACE_ID_HERE"
```

## Workflows

### Lead Enrichment
1. Search for a niche/location.
2. Iterate through results.
3. For promising leads, call `--details` to get website and phone number.
4. Save to CRM (`pcrm.sqlite`).

## Environment Variables
- `GOOGLE_PLACES_API_KEY`: Required for all operations.

## Runtime config
- In this workspace, the key is injected from OpenClaw config via `skills.entries.goplaces.apiKey`.
- That value is exposed to the script as `GOOGLE_PLACES_API_KEY` at runtime.
- Current setup is configured for backend/server-side use, not browser referrer use.
