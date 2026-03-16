---
name: ironman
description: Main project execution skill for non-trivial work. Use for projects, multi-step delivery, system changes, launches, automations, or any task that should move from scope to verified completion with clear gates.
---

# Ironman

Use this as the default project skill.

## Mission

Drive work from objective to verified completion without turning every task into ceremony.

## Route

1. Classify the task.
2. Run `ironman-design` for anything non-trivial.
3. Run `ironman-delivery` once design/plan is approved.
4. Do not claim completion without final verification evidence.

## Fast-path

Skip detailed design only for tiny low-risk actions that:
- take under ~10 minutes,
- do not touch external systems,
- do not change architecture or process,
- do not require rollback planning.

For fast-path tasks, still state:
- goal,
- next 2-4 steps,
- proof of completion.

## Package gate

Use full project flow when any of these are true:
- expected effort > 30 min,
- more than one system/tool boundary,
- user asks for a project or rollout,
- code/process changes need verification,
- risk of rework is meaningful.

## Output posture

- Be direct.
- Ask only high-leverage questions.
- Name tradeoffs.
- Prefer evidence over reassurance.
