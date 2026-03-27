# Marek / realitky — Changelog

## 2026-03-26
- consolidated key canonical project material into `agents/voice/projects/marek/`
- rewrote `prompt.md` with the cleaned Marek v2 prompt as the current canonical edit surface
- rewrote `review.md` into a real review packet
- rewrote `current-state.md` into a current truth document
- rewrote `qa.md` into a usable validation-status document
- added missing project docs:
  - `brief.md`
  - `tools.md`
  - `workflow.md`
  - `knowledge.md`
  - `changelog.md`
- made explicit the central contract mismatch:
  - live/staged evidence still points to the 5-tool runtime
  - cleaned target direction points to `a10_control`
- replaced the prior prompt shape with one canonical patch-ready Slovak system prompt meant to be the main iteration surface
- strengthened callback framing so it reads as the normal safe broker path, not as a weak fallback
- tightened tool phrasing so the prompt stays compatible with both the current 5-tool reality and the cleaner single-control target
- updated review framing to reflect that prompt quality is now ahead of contract certainty

## 2026-03-25 and earlier
Historical supporting material still exists across:
- `agents/integration/daily/`
- `agents/voice/daily/`
- `outputs/`
- `outputs/runtime-handoffs/`
- `skills/voice-factory/references/`

These remain source/support artifacts, but `projects/marek/` should now be treated as the primary working surface for this project.
