# Voice Build / Edit Flow

Purpose: define the minimum reliable flow for creating, editing, and iterating voice agents inside the `voice` lane.

## When to use this flow

Use this flow when:
- creating a new voice agent
- editing an existing voice agent
- patching prompt behavior
- preparing an agent for review
- tightening current-state clarity after a change

## Standard pass shape

Every meaningful build or edit pass should move through these steps:

1. define the objective
   - what must change
   - why it matters now

2. inspect the current state
   - what is confirmed
   - what is inferred
   - what is still unknown

3. define the scope of change
   - what is in scope
   - what is out of scope
   - what should remain unchanged

4. write or patch the agent
   - update prompt behavior
   - update workflow / handoff logic if needed
   - keep V1 narrow

5. decide the next proof layer
   - review pass
   - QA pass
   - runtime validation pass

6. update project truth
   - refresh `projects/<name>/current-state.md`
   - refresh `projects/<name>/review.md` or `qa.md` if relevant
   - record the next move clearly

## Required outputs

A useful pass should result in one or more of:
- agent spec
- prompt patch
- updated current-state note
- review packet
- QA note

## Build rules

- keep V1 narrow
- patch only the behavior that should change
- separate confirmed state from assumptions
- do not imply runtime confidence without evidence
- optimize for editability and reviewability
- prefer one clean next move over broad idea sprawl

## Minimum done standard

A build or edit pass is done only when the next operator can clearly see:
- what changed
- what the current agent state is
- what still needs validation
- what the next move is
