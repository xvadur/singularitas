---
name: rag-jarvis
description: Query Jarvis memory from Supabase vector store. Use for identity/history/project context retrieval before answering strategic or personal-context prompts.
---

# RAG Jarvis

Use this skill when context about Adam, projects, chronology, or prior notes is needed.

## Command

```bash
python ~/.openclaw/skills/rag-jarvis/scripts/rag_query.py "<query>" --json
```

Optional filter:

```bash
python ~/.openclaw/skills/rag-jarvis/scripts/rag_query.py "<query>" --type jarvis --json
```

## Result handling

- `used_rag=true` -> ground response in returned chunks/sources
- `used_rag=false` -> state low confidence and continue without hallucination
