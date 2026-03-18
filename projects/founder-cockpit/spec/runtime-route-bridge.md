# Runtime Route Bridge

## Canonical owner model

- `default` Telegram account -> `main` (`Jarvis`)
- canonical owners are dispatched through `Jarvis` unless a legacy alias is explicitly configured.

## Compatibility bridge (legacy)

- `cso` Telegram account -> `research`
- `cro` Telegram account -> `revenue`
- `cmo` Telegram account -> `web`
- `coo` Telegram account -> `integration`

## Why this bridge exists

- keep the existing Telegram fleet continuity during migration
- avoid creating a fresh bot surface before the workbench is operational

## Rule

Legacy bot names are transport labels only.
They are not the canonical operating model anymore.

### Migration expectation

- after the migration cutover is complete, remove/disable the legacy alias bindings and keep only `default -> main`.
- `voice`, `delivery`, `proof`, `personal-ops`, and `personal-web` are canonical owners in doctrine and must be reached through Jarvis dispatch, not direct alias bindings.
- support lanes remain callable and are execution helpers, not the primary ownership model.
