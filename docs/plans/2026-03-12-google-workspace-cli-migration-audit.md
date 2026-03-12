# Google Workspace CLI Migration Audit — 2026-03-12

## Executive summary

Áno, Xvadur/OpenClaw stack vie adaptovať Google Workspace CLI (`gws`) namiesto súčasného `gog`-based backendu pre Google skilly.

Ale odporúčaná cesta nie je big-bang replacement.
Odporúčaná cesta je:

1. ponechať existujúce skill names a workflow contracty,
2. otestovať `gws` paralelne,
3. až potom prehodiť backend vybraných skillov z `gog` na `gws`.

## Current state

Aktuálne Google skilly v workspace:
- `skills/google-workspace/SKILL.md`
- `skills/gmail-business/SKILL.md`
- `skills/gmail-personal/SKILL.md`
- `skills/calendar-business/SKILL.md`
- `skills/calendar-personal/SKILL.md`

### Current backend

Tieto skilly sú momentálne postavené na `gog` CLI.

Dokázané z auditovaných skillov:
- `google-workspace` používa `gog gmail ...`
- `google-workspace` používa `gog calendar ...`
- wrapper skilly len fixujú account a delegujú na `google-workspace`

### Current backend availability

Lokálne je dostupné:
- `gog` ✅ (`/opt/homebrew/bin/gog`)
- `gws` ❌ (momentálne nie je nainštalované)

### Important nuance

`gog` už dnes pokrýva veľa Google surface area:
- Gmail
- Calendar
- Drive
- Contacts
- Tasks
- Sheets
- Docs
- Slides
- Forms
- App Script
- Chat
- People

Čiže migration nie je motivovaná tým, že `gog` vie málo.
Migration je motivovaná skôr tým, že `gws` môže byť lepší ako jednotný Workspace API wrapper pre agentic workflows.

## What `gws` appears to offer

Podľa README projektu `googleworkspace/cli`:
- one CLI for Google Workspace
- dynamic command surface z Google Discovery docs
- structured JSON output
- agent-friendly orientation
- auth cez OAuth / credentials file / token / service account

Dôležité: README zároveň hovorí:
> This is not an officially supported Google product.

To znamená:
- repo je reálne a použiteľné
- ale nemá status stabilného oficiálne supportovaného Google produktu

## Mapping: current skill contract -> future backend

### 1. Unified mail + calendar skill

Current contract:
- inbox triage
- thread fetch
- draft creation
- calendar listing
- event creation
- draft-first / confirm-before-send policy

Recommendation:
- zachovať skill `google-workspace`
- vnútri prehodiť backend z `gog` na `gws`
- write-safety pravidlá nechať v skill layeri, nie delegovať na CLI

### 2. Account wrapper skills

Current wrappers:
- `gmail-business`
- `gmail-personal`
- `calendar-business`
- `calendar-personal`

Recommendation:
- wrappery ponechať
- len zmeniť interné command examples / operating instructions
- explicit account boundary zachovať aj po migrácii

## What must be validated before migration

## A. Auth model

Treba overiť:
- či `gws` vie pohodlne fungovať s business + personal účtom na jednom stroji
- ako sa prepína medzi účtami
- kde drží credentials
- či vie bezpečne fungovať bez interaktívnych promptov v agent flows

Risk:
- ak multi-account model nebude čistý, wrappers stratia hodnotu alebo budú nebezpečné

## B. Feature parity

Pre migration MVP treba potvrdiť aspoň:
- Gmail search
- thread/message fetch
- draft create
- Calendar list
- Calendar create

Nice-to-have neskôr:
- Drive
- Sheets
- Docs
- Contacts

## C. Stable command contract

`gws` builduje command surface dynamicky z Discovery docs.
To je silné, ale treba otestovať:
- stabilitu syntaxe pre automatizácie
- ergonomiku oproti `gog`
- či sa jednoduché rutiny nezhoršia

## D. Safety contract

OpenClaw skill policy musí ostať rovnaká:
- draft-first by default
- external sends len po explicitnom potvrdení
- event writes s potvrdením pri nejasnom zámere

Toto nesmie zostať iba na používateľovi CLI.
Musí to byť explicitne zachované v `SKILL.md` a v agent behaviour.

## Recommended migration strategy

## Phase 0 — no replacement yet

Nerobiť rewrite current skills naslepo.
Najprv nainštalovať `gws` a overiť auth + základné commandy.

## Phase 1 — experimental backend validation

Cieľ:
- potvrdiť, že `gws` vie robiť to minimum, ktoré dnes používame cez `gog`

Test matrix:
- Gmail read
- Gmail draft create
- Calendar list
- Calendar create
- multi-account switching
- JSON output quality

Výstup:
- short validation note s výsledkom pass/fail

## Phase 2 — backend swap for `google-workspace`

Ak Phase 1 dopadne dobre:
- prepísať `skills/google-workspace/SKILL.md`
- zmeniť command examples z `gog` na `gws`
- zachovať workflow semantics

Wrapper skilly môžu zostať skoro bez zmeny.

## Phase 3 — optional expansion

Po úspešnom swape možno pridať nové skilly:
- `drive-workspace`
- `sheets-workspace`
- `docs-workspace`
- `contacts-workspace`

Ale iba ak na to existuje reálna potreba.

## Decision

### Short answer

Áno, adaptovať to vieme.

### Best answer

- nie ako okamžitý hard replace
- áno ako kontrolovanú migráciu backendu
- `google-workspace` skill nech ostane ako UX vrstva
- `gws` nech sa stane experimentálnym a potom prípadne hlavným backendom

## Concrete next actions

1. Nainštalovať `gws`
2. Nastaviť OAuth
3. Otestovať business + personal account model
4. Overiť 4 základné workflows:
   - inbox read
   - thread fetch
   - draft create
   - calendar read/create
5. Až potom meniť `SKILL.md`

## Recommended call

Môj call je:
- **áno, ísť do pilotnej migrácie na `gws`**
- **nie, ešte neprepisovať existujúce Google skilly napevno**

Najprv validácia. Potom switch.
