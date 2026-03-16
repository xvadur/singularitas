# Vapi Test Suites

Use Vapi Test Suites as the QA and regression layer for serious voice-agent deployments.

## Why this matters
A good prompt is not enough.
For repeatable delivery, every important assistant should have a test suite that can be re-run after prompt, tool, voice, or runtime changes.

## What a test suite contains
Each test has:
- a scripted conversation flow
- a scorer rubric
- a target assistant via the parent test suite

Think of it as:
- script = what happens
- rubric = how success/failure is judged

## Minimum usage rule
For any serious Vapi assistant, create at least:
1. one happy-path test
2. one edge-case / guardrail test
3. one ambiguity / vague-intent test

## Good test design rules
- Test one real scenario at a time.
- Keep the script concrete and phone-like.
- Test real failure modes, not abstract ideas.
- Rubrics should measure behavior, not vague quality adjectives.
- Do not write tests for capabilities the assistant does not have.
- If tools do not exist, the rubric should reward safe fallback behavior instead of tool use.

## Recommended realtor baseline pack
For a Marek-class realtor assistant, start with:
- LISTING_SPECIFIC happy path
- SELLER pricing / valuation guardrail
- GENERAL_INQUIRY vague-intent fallback

## When to run tests
Run or review tests:
- after major prompt updates
- after tool changes
- after scope changes
- before go-live
- after regressions or suspicious call failures

## What to inspect after a run
Review:
- pass/fail result
- transcript
- scorer reasoning
- whether failure is a real behavior problem or a bad rubric

## Pass/fail interpretation
- If the assistant fails because the rubric is stale, update the test.
- If the assistant fails because the behavior drifted, fix the prompt or runtime.
- If the assistant passes but sounds weak, strengthen the rubric.

## API patterns observed in this workspace
List suites:
```bash
curl -sS https://api.vapi.ai/test-suite \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

Get one suite:
```bash
curl -sS https://api.vapi.ai/test-suite/<suite-id> \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

List tests in a suite:
```bash
curl -sS https://api.vapi.ai/test-suite/<suite-id>/test \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

Get one test:
```bash
curl -sS https://api.vapi.ai/test-suite/<suite-id>/test/<test-id> \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

Update one test:
```bash
curl -sS -X PATCH https://api.vapi.ai/test-suite/<suite-id>/test/<test-id> \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @test-patch.json
```

Run a suite:
```bash
curl -sS -X POST https://api.vapi.ai/test-suite/<suite-id>/run \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Get suite runs:
```bash
curl -sS https://api.vapi.ai/test-suite/<suite-id>/run \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

## Operational rule
Treat test suites as part of the deployment artifact.
A production-grade assistant is not just prompt + config.
It is prompt + config + regression tests.
