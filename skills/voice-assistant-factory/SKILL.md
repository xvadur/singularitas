---
name: voice-assistant-factory
description: Create voice reception assistants quickly for service businesses (currently dentist and realtor playbooks). Use when Adam wants to deploy a new AI voice assistant fast with repeatable intake, prompt, workflow, and QA steps.
---

# Voice Assistant Factory

Use this skill to spin up a production-ready voice assistant in a repeatable way.

## Supported playbooks

- **Dentist reception**
- **Realtor intake / lead qualification**

Read the right reference before building:
- Dentist: `references/dentist-playbook.md`
- Realtor: `references/realtor-playbook.md`

## Factory workflow (fast path)

1. **Intake brief** (mandatory)
   - business type, location, language, opening hours
   - what calls assistant should handle
   - booking destination (calendar/CRM)
   - escalation rules (when to transfer to human)
2. **Use playbook template**
   - select vertical-specific conversation flow
   - fill scripts, guardrails, and booking logic
3. **Wire automation**
   - telephony/voice layer
   - n8n workflow(s)
   - CRM + calendar writeback
4. **Run QA checklist**
   - 10 test scenarios minimum
   - error/fallback and handoff behavior
5. **Go-live packet**
   - final prompt
   - workflow endpoints
   - test report
   - known limitations

## Output contract (always deliver)

- Deployment summary (what is live)
- Final system prompt (versioned)
- Tool/workflow map (voice -> webhook -> CRM/Calendar)
- QA results (pass/fail list)
- Next optimization sprint (top 3 improvements)

## Deterministic helper

```bash
python3 ~/.openclaw/skills/voice-assistant-factory/scripts/new_brief.py --vertical dentist
python3 ~/.openclaw/skills/voice-assistant-factory/scripts/new_brief.py --vertical realtor
```

## Rules

- Never claim "production ready" without QA run evidence.
- Always define explicit human handoff triggers.
- Keep prompts concise and fail-safe (no hallucinated promises).
- Prioritize booking completion and lead capture over long conversations.
