# Conventional Commit Template

Use this template for every commit in Singularitas:

```text
<type>(optional scope): <short imperative summary>

- what changed
- why changed
- impact
```

Allowed `<type>`:
- feat
- fix
- chore
- docs
- infra
- refactor
- test
- build
- ci
- revert

Example:

```text
feat(ops): enforce repo context in github skill

- set default repo to xvadur/singularitas
- tightened commit hygiene rules
- improved audit visibility in memory log
```

Rules:
- Subject line max 72 chars.
- One clear behavioral change per commit.
- No empty commits.
