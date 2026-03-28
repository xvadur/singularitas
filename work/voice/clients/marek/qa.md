# Marek / realitky — QA

## Current QA objective

Describe what is actually verified for Marek today and what still remains unproven before stronger runtime confidence is justified.

## Confirmed behavior

Confirmed from current material:
- live ElevenLabs agent identity is known
- live readback exists
- current first message is set
- public n8n webhook URLs resolve to n8n
- n8n cloud root is live
- health endpoint responds
- local backend artifacts exist
- production-compatible 5-webhook gateway package exists

## Unverified behavior

Still not confirmed founder-readably:
- end-to-end POST tool behavior
- live workflow activation state for production traffic
- Sheets writes under real traffic
- Calendar writes under real traffic
- whether the cleaned single-tool contract is actually the intended next runtime or only a proposal

## Known risks

- the project looks more runtime-ready than it is because packaging depth is high
- live 5-tool reality and cleaned single-tool target can be confused if not stated explicitly
- review confidence can outrun QA evidence if design review and runtime review are mixed together

## Recommended next validation pass

Run one bounded validation pass that:
1. confirms which runtime contract is active
2. verifies workflow activation state
3. tests one safe POST path end-to-end
4. records the result in founder-readable language

## Current QA verdict

Marek is `partially validated`.
It is a real staged agent with real backend material.
It is not blank and not purely conceptual.
But it is also not yet live-proven.
