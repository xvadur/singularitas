# Xvadur E-commerce Outbound Engine v1 — Ironman Brief + Execution Plan

Status: Draft for approval
Date: 2026-03-15
Owner: Jarvis

---

## Approach options

### Option A — Mega-agent
One agent receives the segment, does research, scoring, outreach, voice qualification, and handoff.

**Pros:** simple to invoke
**Cons:** weak observability, hard to verify, brittle, too much hidden state, high drift risk

### Option B — Contract-first engine + skill entrypoint + agent workers **(recommended)**
One canonical engine contract defines inputs, stages, outputs, tracking, and handoffs. A skill triggers the run. Agents own bounded stages.

**Pros:** repeatable, auditable, easier to improve, aligns with current multi-agent topology, supports both manual and automated execution
**Cons:** requires upfront definition of states and ownership

### Option C — Agent-owned process without formal engine
Jarvis runs the process conversationally and delegates ad hoc.

**Pros:** fastest to start
**Cons:** not reusable enough, too dependent on session context, weak repeatability

**Recommendation:** Option B.

---

# IRONMAN DESIGN BRIEF

## Goal
Turn the already-documented autodiely / pneuservis outbound + support-agent materials into one repeatable **Xvadur E-commerce Outbound Engine v1** that can be invoked for a segment and produce a send-ready batch with optional AI call qualification for flagged leads.

## Scope In
- canonicalization of current autodiely / pneuservis assets
- one engine contract for the repeatable run
- skill-style entrypoint for invoking the engine
- stage flow from segment to founder handoff
- lead research and top-10 selection
- pain analysis / scoring
- personalized email draft generation
- shared demo/preview asset mapping
- AI call qualification only for leads flagged `ready_to_call`
- founder handoff packet
- explicit tracking states and ownership

## Scope Out
- new segments outside support-heavy e-commerce in v1
- full autonomous closing without Adam
- custom microsite/demo per lead in v1
- enterprise CRM integrations in v1
- fully autonomous voice-first outbound for every lead
- broad offer/brand redesign

## Chosen Approach
Build a **contract-first engine** with:
1. a canonical run schema,
2. a skill as the invocation layer,
3. bounded agent roles for stage execution,
4. a separate voice qualification module triggered only for flagged leads.

## Why This Approach
- The content already exists; orchestration is what is missing.
- A contract-first engine avoids the softness and hidden state of a mega-agent.
- A skill gives a clean invocation surface later.
- Agent workers preserve judgment where needed without making the whole system vague.
- Voice qualification stays powerful but does not become a blocking dependency for every lead.

## Risks
1. Source-of-truth confusion across CSVs and assets
2. Overbuilding v1 into a full platform instead of a repeatable batch engine
3. Voice module complexity slows the core outbound loop
4. Tracking remains implicit and breaks the founder handoff
5. Too many segments dilute validation

## Verification Strategy
- one canonical asset map exists
- one engine spec defines stages, inputs, outputs, owners, and states
- one first batch of 10 leads can be produced without redesign
- each lead has pain framing, personalized outreach, and mapped preview/demo
- at least a subset of leads can be flagged `ready_to_call` with a qualification packet
- founder handoff is explicit and readable without extra digging
- the run can be repeated for the next batch with the same structure

## Artifacts to Produce
- canonical asset map
- engine spec v1
- run-state / tracking schema
- skill invocation spec
- lane ownership map
- AI call qualification module spec
- founder handoff contract
- batch packet v1 for first 10 leads

---

# IRONMAN EXECUTION PLAN

## Goal
Design and operationalize the first repeatable run shape for the Xvadur E-commerce Outbound Engine v1.

## Lane
Cross-functional: Jarvis / CSO / CRO / CMO / COO

## Sprint Block
Block 1 — normalize assets and define the engine
Block 2 — shape the first batch
Block 3 — define the voice qualification module
Block 4 — validate repeatability

### Task 1: Canonical asset normalization
- **Action:** Audit the existing CSVs, onepager/demo assets, prompt/tool files, and identify one canonical source per category.
- **Systems:** `agents/cso/*.csv`, `agents/cso/ecommerce-support-agent-onepager.md`, `agents/cmo/ecommerce-support-onepager/`, `business/segments/ecommerce-agent-tools-contracts.md`, `tmp/*.json`, Obsidian engine plan
- **Verification:** We can point to exactly one source-of-truth file for lead data, outreach, demo asset, and runtime/tooling.
- **Output:** `canonical-asset-map.md`
- **Rollback:** Keep prior files untouched; mark non-canonical files as legacy instead of deleting.

### Task 2: Define the engine contract
- **Action:** Specify engine inputs, stages, outputs, owners, status transitions, and handoff rules.
- **Systems:** docs + source artifacts
- **Verification:** Every stage has a named owner, file/packet output, and status transition.
- **Output:** `engine-spec-v1.md`
- **Rollback:** Revert to plan-only mode if the contract introduces unnecessary abstractions.

### Task 3: Define the invocation surface
- **Action:** Design the future skill entrypoint and parameters for invoking a run.
- **Systems:** skills/docs/OpenClaw routing model
- **Verification:** A run can be described in one call shape, for example: segment, geo, batch size, angle, channels.
- **Output:** `skill-invocation-spec.md`
- **Rollback:** Keep invocation manual via Jarvis until the skill is implemented.

### Task 4: Define stage outputs and tracking
- **Action:** Design the tracking schema for lead-level and run-level states.
- **Systems:** files now; CRM optional later
- **Verification:** Each lead can move through states without ambiguity.
- **Output:** `tracking-schema-v1.md`
- **Rollback:** Track in flat files if richer tracking becomes a blocker.

### Task 5: Build the first canonical lead batch
- **Action:** Select the canonical top-10 batch, normalize lead rows, and enrich any missing fields needed for downstream use.
- **Systems:** canonical CSV + supporting research files
- **Verification:** Ten leads exist in one consistent shape with contact channel, pain framing, and demo mapping readiness.
- **Output:** `batch-v1-leads.csv` or equivalent canonical batch file
- **Rollback:** Fall back to the existing top-10 outreach CSV if full normalization stalls.

### Task 6: Define pain scoring and personalization rules
- **Action:** Convert existing heuristics into explicit scoring/pain categories and personalization logic.
- **Systems:** current outreach CSV, onepager copy, lead observations
- **Verification:** A new lead can be scored and assigned one outreach angle using rules rather than memory.
- **Output:** `pain-scoring-and-personalization-rules.md`
- **Rollback:** Use manual judgment rules for v1 if numeric scoring becomes overkill.

### Task 7: Produce the email outreach packet
- **Action:** Generate the unified send-ready outreach set for the first 10 leads with CTA and preview/demo reference.
- **Systems:** batch file + onepager/demo asset
- **Verification:** Each lead has a subject, body, reason-for-fit, and mapped demo reference.
- **Output:** `batch-v1-outreach-packet.md` and/or structured CSV
- **Rollback:** Use shared demo asset for all leads if per-lead mapping slows execution.

### Task 8: Design the AI call qualification module
- **Action:** Define when a lead becomes `ready_to_call`, what context is passed into the call agent, what the agent must qualify, and what outcome states are captured.
- **Systems:** Vapi / ElevenLabs direction, current e-shop voice prompt patterns, founder handoff logic
- **Verification:** The call step is optional, explicit, and only triggered for flagged leads.
- **Output:** `ai-call-qualification-spec.md`
- **Rollback:** Keep calls manual until the qualification packet is stable.

### Task 9: Define founder handoff contract
- **Action:** Specify the exact packet Adam receives after reply or qualified call.
- **Systems:** outreach packet + call outcomes + tracking states
- **Verification:** Adam can continue the sales motion without searching across files.
- **Output:** `founder-handoff-contract.md`
- **Rollback:** Use a compact markdown brief per lead if a richer format is unnecessary.

### Task 10: Validate repeatability
- **Action:** Run a dry validation of the full flow from segment input to founder handoff using the first batch.
- **Systems:** all above artifacts
- **Verification:** A second batch could be started without redesigning the process.
- **Output:** `validation-notes-v1.md`
- **Rollback:** Trim the engine back to email-only if the call module is the main blocker.

## Dependencies
- existing autodiely / pneuservis source assets
- confirmation of canonical files
- agreement that voice qualification is only for flagged leads
- agreement that v1 remains inside support-heavy e-commerce

## Stop Conditions
- if canonical files cannot be selected cleanly
- if the call module starts dominating the whole engine
- if new segment expansion enters v1 scope
- if tracking cannot be made explicit

## Final Deliverables
- canonical asset map
- engine spec v1
- invocation spec
- tracking schema
- pain scoring/personalization rules
- outreach packet for first batch
- AI call qualification spec
- founder handoff contract
- validation notes

---

## Recommended immediate next move
Do not implement the whole system yet.
First finish these three artifacts in order:
1. canonical asset map
2. engine spec v1
3. tracking + founder handoff contract

Then build the first batch packet and only after that wire the skill or voice module.
