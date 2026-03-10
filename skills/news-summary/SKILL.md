---
name: news-summary
description: Fallback general-news summarizer. Use only when Natural20 feed is insufficient for requested scope.
---

# News Summary (Fallback)

Use this when broader non-AI news is needed or Natural20 is sparse.

Rule:
- AI-first brief -> use `natural20-api-brief` first
- global/general brief -> this skill as fallback
