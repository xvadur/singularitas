---
name: voice-factory
description: Create, configure, deploy, and manage AI voice agents across ElevenLabs and Vapi with a repeatable delivery pipeline. Use when Adam wants to build a new voice agent, update agent behavior, prepare prompts, define handoff logic, set intake rules, map tool flows, run QA, or manage the operational lifecycle of a voice assistant. Use n8n as the separate automation skill when workflow implementation or debugging is required.
---

# Voice Factory

Use this skill as the main pipeline for Xvadur voice-agent delivery and agent operations.

This skill owns:
- agent intake and deployment planning
- conversation design and prompt structure
- scope definition and handoff rules
- ElevenLabs voice layer decisions
- Vapi agent configuration decisions
- QA, launch readiness, and change control

This skill does **not** replace `n8n`.
Use `n8n` as the separate skill for workflow creation, execution debugging, and automation implementation.

## Platform split

- **Voice Factory** = design, create, configure, and manage the agent across Vapi + ElevenLabs
- **Vapi inside Voice Factory** = assistant inspection, runtime setup, call behavior, tool routing, phone assistant configuration
- **ElevenLabs inside Voice Factory** = voices, speech assets, cloning, dialogue, audio generation
- **n8n** = automation workflows, webhooks, data writes, downstream orchestration

## Required access

Set:
- `VAPI_API_KEY`
- `ELEVENLABS_API_KEY`

Preferred auth pattern for Vapi:
- `Authorization: Bearer $VAPI_API_KEY`

Base URLs:
- Vapi: `https://api.vapi.ai`
- ElevenLabs: `https://api.elevenlabs.io`

## Vapi core endpoints

### List assistants
```bash
curl -sS https://api.vapi.ai/assistant \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

### Get one assistant
```bash
curl -sS https://api.vapi.ai/assistant/<assistant-id> \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

### Create assistant
```bash
curl -sS https://api.vapi.ai/assistant \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @assistant.json
```

### Update assistant
```bash
curl -sS -X PATCH https://api.vapi.ai/assistant/<assistant-id> \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @assistant-patch.json
```

## Default operating workflow

1. **Capture intake brief**
   - business type
   - location and language
   - call types to handle
   - booking or lead destination
   - business hours
   - escalation and human transfer rules
   - forbidden actions / compliance constraints

2. **Define the agent job clearly**
   - what the agent must do
   - what the agent must never do
   - what counts as success on a call
   - what data must be captured every time

3. **Design the conversation system**
   - greeting
   - qualification logic
   - booking or lead capture flow
   - objection / confusion handling
   - fallback behavior
   - handoff triggers

4. **Choose the voice/runtime setup**
   - ElevenLabs voice strategy
   - Vapi runtime and tool behavior
   - latency / quality tradeoffs
   - language and tone constraints

5. **Map integrations**
   - what Vapi sends
   - what n8n receives
   - what systems are updated
   - what confirmation must return to caller

6. **Run QA before go-live**
   - normal path
   - edge cases
   - unclear caller speech
   - after-hours flow
   - escalation path
   - failed tool / failed webhook behavior

7. **Prepare launch packet**
   - final prompt
   - tool map
   - voice/runtime config
   - QA report
   - known limitations
   - next optimization sprint

## Output contract

Always deliver:
- deployment summary
- final prompt or prompt changes
- tool/workflow map
- handoff logic
- QA results
- open risks / known limitations
- next optimization actions

## References

Use the existing vertical playbooks when relevant:
- Dentist: `references/dentist-playbook.md`
- Realtor: `references/realtor-playbook.md`

If the deployment is outside those verticals, still follow the same factory sequence and adapt the intake + QA logic to the business.

## Deterministic helper

```bash
python3 /Users/_xvadur/singularitas/skills/voice-factory/scripts/new_brief.py --vertical dentist
python3 /Users/_xvadur/singularitas/skills/voice-factory/scripts/new_brief.py --vertical realtor
```

## Rules

- Never claim an agent is live-ready without QA evidence.
- Always define explicit human handoff triggers.
- Keep prompts concise, bounded, and operational.
- Prevent custom chaos: define scope before implementation.
- Separate agent design decisions from n8n workflow implementation.
- Prefer repeatable patterns over one-off bespoke setups.
- Prefer read-first inspection before Vapi mutation.
- Record assistant id, purpose, tools, model, transcriber, and voice provider for each deployment.
- Change one runtime variable at a time when debugging Vapi behavior.
