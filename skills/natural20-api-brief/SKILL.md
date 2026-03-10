---
name: natural20-api-brief
description: Primary AI intelligence channel via Natural20 feed. Use as default source for AI news briefing and trend detection.
user-invocable: true
metadata: {"openclaw":{"emoji":"🧠","requires":{"bins":["python3"]}}}
---

# Natural20 API Brief

Primary AI news channel for the runtime. Source feed:
- `https://natural20.com/api/feed`

## Purpose
- Vstupný AI news feed pre morning brief a trend detection.
- Vráťi „top signály“ podľa skóre + recency.

## Usage

```bash
# Slovensky: AI news za posledných 24h
python3 ./scripts/n20_brief.py --hours 24 --top 12 --json

# rýchly prehľad
python3 ./scripts/n20_brief.py --hours 24 --top 12
```

## Workflow

1. Pull feed
2. Rank by score + recency
3. Cluster themes
4. Produce actionable signal summary

## Integration rule

- `news` slash command in this workspace should prefer this feed first.
- Morning brief and strategic AI updates should prefer this source first; only then add other sources.
