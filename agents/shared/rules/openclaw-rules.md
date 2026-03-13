# Pravidlá pre OpenClaw

Tento vault je pracovný kontext pre OpenClaw.

## Vždy čítaj

- `+`
- `Kontext`
- `Operácie`
- `Calendar`
- `Denník`
- `Systém`
- `Agent/00 Bootstrap - Xvadur Agent System` (core startup)
- `Operácie/Agent Architecture - Xvadur Current Stage` (agent architecture)
- `Systém/Pravidlá pre OpenClaw` (governance)

## Môžeš robiť

- navrhovať missing context
- dopĺňať rozumné backlinky
- navrhovať nové tematické väzby v `Kontext`
- skladať briefy a plány v `Operácie`
- zakladať nové operačné iniciatívy z potvrdeného kontextu
- čítať `Calendar` ako zdroj časového kontextu a denného priebehu

## Nemáš robiť potichu

- meniť význam pôvodných používateľových poznámok
- mazať surové capture notes bez zachovania stopy
- reorganizovať veľké časti `Kontext` bez vysvetlenia

## Označovanie medzier

Ak chýba dôležitý kontext, vytvor explicitný návrh typu:

- missing audience detail
- missing offer definition
- missing outreach criteria
- missing landing page input
- missing CRM structure

## Pracovný tok

1. Prečítaj určené priečinky.
2. Zhrň, čo už je jasné.
3. Povedz, čo chýba.
4. Navrhni, čo má ísť do `Kontext` a čo do `Operácie`.
5. Po potvrdení priprav execution materiály.

## Calendar pravidlo

Calendar notes vznikajú cez plugin v priečinku `Calendar`.
Nemigruj ich automaticky do `Denník`, pokiaľ na to nie je explicitný dôvod.

## Agent setup docs

Praktické setup dokumenty pre jednotlivých agentov sú v priečinku `Agent`.
Použi ich ako source of truth pri konfigurácii agent identities, goals, scope, heartbeat a first-message initialization.

## Operating aliases

V bežnej prevádzke používaj C-level aliasy:

- `CEO` = Chief of Staff Agent
- `CSO` = Market Intelligence Agent
- `CMO` = Messaging and Funnel Agent
- `CRO` = Outbound and Pipeline Agent
- `COO` = Delivery and Product Ops Agent

Ak founder použije tieto názvy, ber ich ako preferovaný shorthand pre handoffy, issue naming a operating komunikáciu.
