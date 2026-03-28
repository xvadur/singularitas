# Voice Queue

- Date: `2026-03-26`
- Owner: `voice`
- State: `lean-active`

## Active items

1. `marek-review-pass`
   - State: `active`
   - Objective: turn Marek into the first complete edit / review / send-ready loop
   - Current reality: lean workspace is ready, but key Marek docs still need rewriting into operator-usable form
   - Next move: rewrite `business/voice/clients/marek/current-state.md`, `review.md`, `qa.md`, and `prompt.md`
   - Source: `business/voice/clients/marek/`

2. `marek-runtime-validation`
   - State: `partial`
   - Objective: verify end-to-end runtime behavior for the staged Marek assistant
   - Current reality: safe read-only probe result exists, but activation and POST path behavior are still not founder-readably proven
   - Next move: inspect workflow state directly, then run one deliberately safe POST validation
   - Source: `business/voice/clients/marek/qa.md`

3. `voice-workflow-proof`
   - State: `next`
   - Objective: prove that the reduced workspace supports real edit and review work without drift
   - Current reality: the lean structure exists, but the delivery loop still needs to be completed once end-to-end
   - Next move: complete the Marek review pass and extract only the patterns that actually helped
   - Source: `method/`
