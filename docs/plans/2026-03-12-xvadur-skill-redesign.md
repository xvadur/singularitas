# Xvadur Skill Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rework the OpenClaw marketing and business-development skills around Xvadur's current startup model, then create one Codex skill that supports positioning, GTM, sales docs, and operating materials.

**Architecture:** Keep two narrow execution skills in OpenClaw: one for positioning and messaging, one for outbound and pipeline execution. Create one broader Codex skill that combines both lanes into a founder-facing growth ops package for document work, offer shaping, and sales execution support.

**Tech Stack:** Markdown skill specs, shell helper scripts, Codex skill folder structure.

---

### Task 1: Redesign the marketing skill

**Files:**
- Modify: `/Users/_xvadur/singularitas/skills/marketing-mode/SKILL.md`
- Modify: `/Users/_xvadur/singularitas/skills/marketing-mode/mode-prompt.md`
- Modify: `/Users/_xvadur/singularitas/skills/marketing-mode/skill.json`

**Step 1:** Replace the generic marketing encyclopedia with a focused Xvadur marketing operator workflow.

**Step 2:** Update the mode prompt so the persona is useful for startup positioning, offers, landing pages, objections, and content angles.

**Step 3:** Update machine-readable metadata to match the new scope and trigger words.

### Task 2: Redesign the business-development skill

**Files:**
- Modify: `/Users/_xvadur/singularitas/skills/business-development/SKILL.md`
- Modify: `/Users/_xvadur/singularitas/skills/business-development/scripts/bd-init.sh`
- Modify: `/Users/_xvadur/singularitas/skills/business-development/scripts/partner-research.sh`
- Modify: `/Users/_xvadur/singularitas/skills/business-development/scripts/pipeline-report.sh`

**Step 1:** Rewrite the skill around Xvadur-style segment selection, lead research, outreach, pipeline, and pilot qualification.

**Step 2:** Align helper scripts with client/pilot execution rather than generic partnerships.

**Step 3:** Keep the scripts simple and file-based so they remain usable in OpenClaw sessions.

### Task 3: Create the Codex growth ops skill

**Files:**
- Create: `/Users/_xvadur/.codex/skills/xvadur-growth-ops/SKILL.md`

**Step 1:** Create one Codex skill that triggers on business docs, positioning, offer design, outbound planning, and startup operating materials.

**Step 2:** Keep the skill concise and action-oriented so it can be loaded often without bloating context.

### Task 4: Verify and summarize

**Files:**
- Review all edited files above

**Step 1:** Read back the rewritten skill files and make sure the scopes do not overlap excessively.

**Step 2:** Summarize the new trigger conditions and intended usage.
