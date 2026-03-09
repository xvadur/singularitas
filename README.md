# Singularitas

**Omnia sponte fluant, absit violentia rebus.**

![Rock Lee | Naruto | never give up](https://media.tenor.com/abfF-YQ167UAAAAC/rock-lee-weights.gif)

## O projekte

**Singularitas** je môj digitálny domov a operačné jádro, kde sa spájajú:
- dlhé cykly a stratégia (práca „na celý kĺb“, nie na pár týždňov),
- precízny architektúrny prístup k AI nástrojom,
- disciplína kontinuity medzi sessionmi.

Je to platforma na budovanie výkonnej AI infraštruktúry s dôrazom na dôstojnosť, reputáciu a expanziu.

## Prečo toto repo existuje

Keď sa človek rozhodne, že chce systém, nestačí „experiment“ — treba **trvalý operačný nástroj**.

Singularitas slúži ako:
- **Core runtime base** pre OpenClaw pracovné prostredie,
- zdroj pravdy pre identitu a preferencie (IDENTITY, USER, SOUL, MEMORY),
- základ pre postupný, verzovaný rast AI recepcie a servisných služieb.

## Ako sa to používa

1. OpenClaw je priradený k tomuto workspace-u ako digitálny domov.
2. Konverzácie, rozhodnutia a kontext sa spracúvajú podľa pravidiel tohto repozitára.
3. Kľúčové veci sa udržiavajú vo verziách – históriu nie je treba spomínať, je možné sa k nej **vrátiť presne**.
4. Každá nová session môže kontinuálne naviazať cez nástroj `/save`.

## Kľúčové princípy

- **Dôstojnosť a presnosť** pred chválu.
- **Bez falošných kompromisov** – rozhodnutia sú jasné, rýchle a odôvodnené.
- **Singularitas-first framing** – najprv stabilita a kontinuita v tomto repozitári.
- **Pripravenosť na expanziu** – systém je navrhnutý na rast, nie na improvizáciu na poslednú chvíľu.

## Roadmapa v hrubých ťahoch

- `v1`: stabilizácia core dokumentov a pracovného rytmu.
- `v2`: AI recepcia s merateľnými metrikami.
- `v3`: automatizované workflowy, ktoré zvládnu repetitívny drift.

## Rýchly štart

```bash
# over stav
openclaw status

# aktualizácia workflow
openclaw dashboard

# export kontextu do nasledujúcej session
/save
```

## Commit a push disciplína (Singularitas)

Aby sme budovali **maximálne zmysluplnú GitHub heatmapu**, držíme tieto pravidlá:

- Každý commit má konvenčný formát: `type(scope): summary`
  - typy: `feat`, `fix`, `chore`, `docs`, `infra`, `refactor`, `test`, `build`, `ci`, `revert`
- Jedna vec = jeden commit.
- Žiadne prázdne commity.
- Pred commitom: `git status --short` + odfiltrovaný šum (`.DS_Store`, temp súbory).
- Po väčšom bloku: `/save` pre pokračovanie kontextu.

### Rýchle príkazy

```bash
# konvenčný commit
./scripts/release-flow.sh "feat(ops): add commit discipline"

# push kontrola
cat .github/PUSH_TEMPLATE.md

# lokálna kontrola
./scripts/release-flow.sh "chore(git): verify clean push history"
```

---

Ak toto je váš štart, toto je aj váš štít: **Singularitas je doma, nie sandbox.**
