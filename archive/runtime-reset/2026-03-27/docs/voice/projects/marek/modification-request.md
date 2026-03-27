# Marek / realitky — Modification Request Format

## Purpose

Use this format whenever we want the voice-layer agent to modify Marek.
This is the request packet that should precede prompt/tool changes.

## Rule

Do not ask for "improve Marek" vaguely.
Every modification request should specify:
- objective
- current problem
- what should change
- what must stay unchanged
- output expected
- validation expectation

## Canonical request template

```md
# Marek modification request

## Objective
What exact improvement or change is needed?

## Current problem
What feels wrong in the current Marek behavior/prompt/tooling?

## Scope of change
Choose one or more:
- prompt only
- tool logic / tool contract
- lane logic
- greeting / tone
- next-step policy
- guardrails
- QA scenarios
- ElevenLabs config notes

## What should change
List concrete requested changes.

## What must stay unchanged
List the parts that should remain stable.

## Deployment target
- draft only
- review-ready packet
- patch-ready prompt
- full build packet

## Validation needed
How should we know the change is good?
- style review
- scenario walkthrough
- QA pack update
- patch-ready diff
```

## Example

```md
# Marek modification request

## Objective
Spraviť Mareka prirodzenejšieho a menej skriptového pri buyer calls.

## Current problem
Prompt pôsobí príliš formulárovo, callback framing je OK, ale buyer lane znie sucho.

## Scope of change
- prompt only
- lane logic
- greeting / tone

## What should change
- buyer lane má znieť prirodzenejšie
- menej rigidných formulácií
- viac short spoken phrasing
- zachovať stručnosť

## What must stay unchanged
- Slovak language
- formal address
- callback as safe default
- no invented facts

## Deployment target
- review-ready packet
- patch-ready prompt

## Validation needed
- style review
- 3 buyer scenario walkthroughs
```

## Standard outputs from a good modification request

A good response to a modification request should return:
- change summary
- updated prompt or prompt diff
- updated tool/logic notes if relevant
- risks introduced by the change
- recommended QA checks
