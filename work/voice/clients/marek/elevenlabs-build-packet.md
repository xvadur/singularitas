# Marek / realitky — ElevenLabs Build Packet

## Purpose

This file defines what we need in hand before making or updating the Marek agent in ElevenLabs.

## Build packet contents

A proper ElevenLabs update/build packet for Marek should contain:

1. **Deployment summary**
   - what this version is for
   - what changed
   - what stayed stable

2. **V1 scope**
   - one problem surface only
   - what Marek does
   - what Marek does not do

3. **Canonical prompt**
   - deployable prompt text

4. **First message**
   - opening line

5. **Tool map**
   - actual tool surface used by the agent
   - minimum assumptions for tool use

6. **Workflow logic summary**
   - lanes
   - next-step outcomes
   - callback / viewing policy
   - handoff policy

7. **Guardrails**
   - unsupported claims
   - forbidden promises
   - unsupported advisory surfaces

8. **QA pack**
   - minimum 3 scenarios
   - ideally more for serious revisions

9. **Known limitations**
   - what still is not deployed or proven

10. **Patch note / modification summary**
   - what exactly changed since previous version

## Minimum Marek packet for modification work

For most modifications, we need at least:
- updated prompt
- first message
- tool surface summary
- change summary
- QA notes

## Current live-truth warning

When producing an ElevenLabs packet, do not hide the current contract mismatch.
If the live agent still uses 5 tools, the packet must say so.
If we are preparing a cleaned target packet, the packet must say it is a target design unless already deployed.

## Working first message baseline

`Dobrý deň, dovolali ste sa realitnému maklérovi. Ja som virtuálny asistent Marek. S čím vám môžem pomôcť?`

## Build-quality rule

If the packet cannot answer these questions, it is not ready:
- what problem surface does Marek solve?
- what lanes does he route?
- what next steps is he allowed to choose?
- when does he use tools?
- what must he never claim?
- what exactly changed in this revision?
