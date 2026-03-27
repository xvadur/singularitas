---
name: github
description: Operácie na GitHube pre Singularitas. Priorita: zmysluplné, frekventované commity a čistý git health pre silnú heatmapu.
metadata:
  {
    "openclaw": {
      "requires": {
        "bins": ["gh"]
      },
      "emoji": "🐙"
    }
  }
---

# GitHub Skill — Singularitas Operational Edition

**Cieľ:** maximalizovať zmysluplnosť commitov, jednoduchý tracing a „heatmap-ready“ rytmus.

## Predvolené nastavenie
- Default repo: `xvadur/singularitas`
- Repo pre operácie: vždy potvrdiť pred mutujúcim krokom, ak nie je explicitne zadané iné.

## Používanie
- Využívaj pre:
  - kontrolu stavu a čistý workflow (`status`, `log`, `diff`)
  - bezpečné commity (`add`, `commit`, `push`)
  - riadené syncy (`pull`, `rebase`, `fetch`)
  - GitHub operácie (`issue`, `pr`, `workflow`, `repo`)

## Režim pre zmysluplnú heatmapu (systémové pravidlo)
1. **Žiadne prázdne commity.** Vždy commitujeť len keď je obsah veci mení stav.
2. **Jedna myšlienka = jeden commit.** Zoskupit podľa funkcionality, nie podľa súborov.
3. **Krátky, výstižný commit titulok** (imperatív):
   - `feat: ...`
   - `fix: ...`
   - `chore: ...`
   - `docs: ...`
   - `infra: ...`
4. **Before/After hygiene:**
   - pred commitom odstrániť `*.DS_Store` a podobný šum
   - kontrola `git status` a `git diff --stat`
5. **Denný rytmus:** minimálne 1–2 malé, ale zmysluplné commity denne, keď sa mení runtime/operácia.
6. **Audit:** po väčšom zásahu vždy spustiť `git log --oneline -n 8` pre spätnú čitateľnosť histórie.

## Odporúčané workflow (pre automatizovaný rytmus)
- `openclaw --profile rescue status`
- `openclaw --profile rescue skills list --enabled | grep github`
- `git status --short`
- `git add <files>`
- `git commit -m "<type>: <point of change>"`
- `git push`

## Bezpečnostný guardrail
- Ak je `git status` čistý, necommituj.
- Ak commit mení hlavne `memory`/`docs`, explicitne označ ako `chore` alebo `docs` podľa obsahu.
- Pred PR/push kontroluj vetvu a base remote (`git branch --show-current`, `git remote -v`).

## Aliasové „vysokou hodnotou“ príkazy
- `/repo-status` → `git status --short && git branch --show-current && git remote -v`
- `/repo-commit "<message>"` → validácia + commit + `git log -1 --oneline`
- `/repo-heatbeat` → `git log --since="24 hours ago" --oneline --graph`

## Integrácia s Singularitas
- Tento skill drží princíp **Singularitas-first**: každý zásah je určený na dlhodobú kontinuitu, auditovateľnosť a rast histórie.
- Vždy prepájaj operácie do `memory/YYYY-MM-DD.md` cez `/save` po výraznom pracovnom bloku.

## Poznámka
Používaj `gh` pre issue/PR/workflow operácie podľa potreby, ale základný git rytmus nech je lokálne disciplinovaný v tomto skil-e.
