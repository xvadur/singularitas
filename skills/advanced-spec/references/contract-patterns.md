# Contract Patterns

Use these patterns to turn a vague idea into an execution-grade brief.

## Core dimensions

For most non-trivial requests, try to lock these:
- Goal
- Why now
- Scope in
- Scope out
- User / audience
- Output
- Constraints
- Dependencies
- Risks
- Acceptance bar
- Failure bar
- Stop condition

Do not force every dimension if some are irrelevant.

## Fast reconstruction pattern

Use this when the user has strong intent but weak structure:

- **How I understand it**
- **What is already clear**
- **What is being assumed**
- **What would break planning if left fuzzy**
- **Safe defaults**
- **1–3 blocking questions**
- **Ready / not ready**

## Output contract pattern

Every planning-grade task should end up with:
- **Deliverable:** what will exist
- **Format:** how it will be packaged
- **Quality bar:** what makes it good enough
- **Failure bar:** what makes it a miss
- **Stop condition:** where to stop instead of hallucinating extra system

## Useful blocking-question categories

Ask only when the answer changes the build:
1. **Scope question** — what is in vs out?
2. **Output question** — what exact artifact is needed?
3. **Risk question** — what mistake is expensive here?
4. **Externality question** — does this touch clients, money, public systems, or publishing?
5. **Cadence question** — one-shot, recurring, or ongoing?

## Safe default patterns

Use defaults like:
- v1 over full system
- internal over public
- brief-first over dashboard-first
- narrow ICP over generic audience
- one primary output over many parallel outputs
- weekly review over constant churn
- reversible architecture over clever architecture

## Failure patterns to catch early

### 1. Vision blob
The request mixes product, workflow, branding, automation, and content into one sentence.
Fix: split layers and choose the dominant one.

### 2. Output fog
The user wants progress but has not defined what should be delivered.
Fix: force an output contract.

### 3. Scope romance
The request sounds exciting but is too broad for v1.
Fix: cut geography, channels, actors, or features.

### 4. Proof gap
The user wants authority or deployment claims without evidence.
Fix: define current proof and frame the claim honestly.

### 5. Planning too early
The problem is not yet specified enough for a real plan.
Fix: amplify first, then plan.

## Adam-specific note

Adam often provides:
- strong strategic direction
- strong intuitive pattern recognition
- useful emotional signal about what matters

But may under-specify:
- constraints
- sequence
- what counts as done
- what should be left out

Compensate by building a tighter contract, not by asking endless questions.
