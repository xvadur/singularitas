# Singularity Eco Promotion Contract

Only one allowed movement path:

`Obsidian Capture -> singularitas Packet/Mission -> firma Business Record`

## Allowed actions

- `harvest`
  - Obsidian -> singularitas for operational extraction
- `promote`
  - singularitas -> firma for action-bearing business truth
- `mirror`
  - firma -> Obsidian for human-readable summaries or knowledge reuse
- `reference`
  - firma -> singularitas for runtime contracts, skills, docs, and traces without duplication

## Disallowed actions

- direct `Obsidian -> firma` for action-bearing truth
- full bidirectional sync
- background mirroring of live state
- duplicated live status in both `singularitas` and `firma`

## Lineage header for promoted artifacts

Every promoted artifact in `firma` must include:

- `canonical_owner`
- `source_path`
- `promoted_from`
- `last_promoted`
- `status`
- `edit_rule`

## Runtime mission rule

Every runtime mission that maps to a business object must link to its canonical `firma` record via the `firma_record` field.
