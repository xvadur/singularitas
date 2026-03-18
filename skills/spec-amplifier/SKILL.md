---
name: spec-amplifier
description: Clarify and strengthen incomplete task specs before planning or execution. Use when the user has clear intent but the request is underspecified, compressed, or missing important constraints, assumptions, edge cases, or defaults—especially for apps, automations, agents, skills, APIs, workflows, offers, or project plans. Produce a pre-planning brief with confirmed facts, inferred assumptions, critical gaps, safe defaults, and only the minimum blocking questions.
---

# Spec Amplifier

Clarify the user's likely intent before planning.
Turn a compressed request into a planning-grade brief without pretending missing details are facts.

## Default job

Use this skill before `plan`, `ironman-design`, delegation, or major execution when the request is directionally clear but structurally incomplete.

Typical trigger shape:
- strong vision, weak specification
- broad idea, thin constraints
- clear outcome, unclear scope or defaults
- likely hidden assumptions that could distort planning

## Workflow

### 1. Choose amplification mode

Use the lightest mode that still protects execution quality.

- **Quick** — small or low-risk tasks; fill only obvious gaps; ask at most 1 blocking question.
- **Standard** — normal build/planning tasks; surface key assumptions and ask at most 3 blocking questions.
- **Critical** — production, client-facing, security-sensitive, infra, money, external writes, or expensive-to-rework tasks; be stricter about hidden risks and missing constraints.

### 2. Reconstruct intent

Write one sentence that states how you currently understand the task.
Do not embellish. Do not sell. Do not broaden the mission.

Start with language like:
- `Rozumiem tomu tak, že...`
- `Cieľ je pravdepodobne...`

### 3. Separate signal from inference

Split the input into:
- **Confirmed** — directly stated by the user
- **Inferred** — likely implied but not explicitly stated
- **Missing** — important dimensions still absent

Never present inferred items as confirmed facts.
Mark them clearly.

### 4. Expand only relevant dimensions

Use `references/gap-patterns.md` to check the task type and scan for typical missing dimensions.
Only surface dimensions that materially affect planning or execution.
Do not dump a generic checklist.

### 5. Propose safe defaults

When the task can keep moving without asking everything, propose defaults.
Defaults must be:
- practical
- low-drama
- reversible when possible
- clearly labeled as assumptions

Use phrasing like:
- `Ak nepovieš inak, navrhujem default...`
- `Safe default pre túto verziu je...`

### 6. Ask only blocking questions

Ask questions only when the answer changes:
- architecture
- scope
- risk
- delivery sequence
- external behavior

Prefer 1 sharp question over 5 weak ones.
If safe defaults are enough, skip questions entirely.

### 7. Decide planning readiness

End with one of these:
- **Ready for planning**
- **Ready for planning with defaults**
- **Not ready for planning until X is clarified**

## Output contract

Use this shape unless the conversation clearly needs a tighter variant:

### Pre-planning brief
- **How I understand it**
- **Confirmed**
- **Inferred**
- **Critical gaps**
- **Proposed defaults**
- **Blocking questions**
- **Planning readiness**

Keep it compact.
The goal is better planning input, not a second planning pass.

## Guardrails

- Do not invent facts.
- Do not turn simple tasks into discovery theater.
- Do not ask about every possible edge case.
- Do not expand scope beyond the user's likely mission.
- Do not confuse product brainstorming with execution-critical clarification.
- If the task is already well specified, say so and move on.

## Heuristics

Bias toward more amplification when:
- the request affects production systems
- the task touches auth, permissions, money, legal, or security
- the output will be client-facing
- the user describes a large concept in a very compressed way
- multiple valid interpretations could lead to expensive rework

Bias toward less amplification when:
- the task is a small edit
- the cost of correction is low
- the user already provided constraints, scope, and acceptance shape

## Example triggers

- `Chcem appku na správu leadov.`
- `Sprav skill na toto.`
- `Potrebujem AI agenta pre makléra.`
- `Postav workflow na follow-up.`
- `Navrhni nový onboarding flow.`

In these cases, amplify first, then plan.
