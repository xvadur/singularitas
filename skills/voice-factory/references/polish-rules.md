# Polish Rules for Voice Factory Outputs

Use these rules when turning a valid agent design into a polished Vapi-ready prompt.

## Goal
Produce prompts that feel deployable immediately, with spoken behavior close to a good live assistant rather than a careful draft.

## Primary polish targets
- sharper spoken phrasing
- fewer over-explanations
- less bureaucratic wording
- stronger callback framing
- clearer distinction between recommendation and confirmation

## Spoken style rules
- Prefer short spoken sentences over explanatory prose.
- Prefer direct operational wording over abstract wording.
- Prefer calm confidence over excessive politeness.
- Avoid phrases that sound like documentation inside the prompt.
- Avoid repeating the same caution in multiple sections unless it protects a real failure mode.
- Do not write as if explaining the system to another operator; write for runtime behavior.

## Good prompt phrasing patterns
Prefer:
- "Zisti" over long explanatory sentences
- "Navrhni callback" over "preferovaný next step je callback", unless the structured format is needed
- "Ak si neistá, povedz to priamo" over softer vague hedging
- "Nikdy nepotvrdzuj termín bez systému" over longer variants of the same rule

## Callback framing
For V1 pilots, callback is often the safest outcome.
Write callback logic clearly and confidently.
Do not make callback sound like a failure.
Make it sound like the normal broker handoff path.

## Tool phrasing
If tools are missing or not yet deployed:
- say so briefly in the prompt logic
- do not over-discuss tools
- do not let missing tools dominate the prompt

Bad:
- long explanations about hypothetical tools

Good:
- "Ak systém nevie potvrdiť termín, navrhni callback."

## Formality control
Aim for professional, not stiff.
If a prompt line sounds like a policy memo, tighten it.
If a prompt line sounds like a spoken operator rule, keep it.

## Anti-bloat checks
Cut or compress when you see:
- duplicated guardrails
- duplicated callback logic
- duplicated uncertainty handling
- over-detailed rationale that will not change runtime behavior

## Realtor-specific polish cues
For Marek-class realtor outputs:
- sound like a capable broker assistant
- keep listing/viewing logic practical
- treat callback as the main safe next step
- keep pricing/valuation prohibitions short and firm
- keep listing-specific lane crisp

## Final pass checklist
Before finalizing a prompt, check:
1. Does it sound like runtime instructions, not documentation?
2. Is callback framed as a normal next step?
3. Are tool limitations short and cleanly phrased?
4. Are there any lines that feel too formal or over-explained?
5. Could this go into Vapi without a human doing a style cleanup?
