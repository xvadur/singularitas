# Runtime Route Bridge

## Canonical owner model

- `default` Telegram account -> `main` (`Jarvis`)
- `cso` Telegram account -> `research`
- `cro` Telegram account -> `revenue`
- `cmo` Telegram account -> `web`
- `coo` Telegram account -> `integration`

## Why this bridge exists

- keep the existing Telegram bot fleet alive for tomorrow
- stop the runtime from being C-level-only in practice
- avoid creating a dozen new bots before the workbench is operational

## Temporary rule

Legacy bot names are transport labels only.
They are not the canonical operating model anymore.

For tomorrow's cutover:
- only `default`, `cso`, `cro`, `cmo`, and `coo` have direct Telegram ingress
- `voice`, `delivery`, `proof`, `personal-ops`, and `personal-web` are canonical owners in doctrine but are reached through Jarvis dispatch, not direct bot ingress
- support lanes remain callable, but they are execution helpers, not the primary ownership model
