# Symphony + OpenClaw - Operating Runbook

## Purpose

Tento note popisuje, ako sa v aktualnej faze pouziva `Symphony` spolu s `OpenClaw`.

Ciel nie je, aby Symphony samo "riadilo firmu". Ciel je:

- `OpenClaw` zadava a riadi pracu cez `Linear`
- `Symphony` issue prebera, spusta a monitoruje
- `Codex` vykonava konkretny workflow v issue workspace
- ja ako operator davam smer, prioritu a dalsie instrukcie

Toto je operacny model pre realne pouzivanie, nie len demo alebo smoke test.

## Core Model

Zakladny model je:

`Human -> OpenClaw -> Linear issue -> Symphony -> Codex workspace run -> OpenClaw review -> Linear update -> Human instruction loop`

Kazde issue ma vlastny dlhodoby workspace.

To znamena:

- issue ma vlastny pracovny priecinok
- Codex pracuje izolovane v tomto priecinku
- vystupy sa daju kontrolovat aj po case
- retry alebo continuation nemusia zacinat od nuly

## Who Does What

### Human

Human:

- urcuje smer
- rozhoduje priority
- pise parent zadania alebo upravuje strategiu
- dava dalsie instrukcie OpenClaw a agentom

Human nema robit mikromanazment kazdeho kroku, ale ma riadit system.

### OpenClaw

OpenClaw je supervisory layer.

OpenClaw:

- vytvara alebo rozdeluje pracu do `Linear`
- kontroluje vystupy Codexu
- rozhoduje, co sa pouzije dalej
- posuva alebo uzatvara stav issue
- vracia issue na doplnenie, ak packet alebo output nie je dostatocny

OpenClaw nie je len "dalsi agent". Je to operacna kontrolna vrstva.

### Symphony

Symphony je orchestrator.

Symphony:

- sleduje zvoleny `Linear` projekt
- vybera issue v aktivnych stavoch
- vytvori workspace pre issue
- spusti `Codex`
- sleduje stav session
- retryuje pri zlyhani alebo stalle
- ukazuje observability dashboard

Symphony samo od seba nerozhoduje obsah prace. Vykonava workflow kontrakt.

### Codex

Codex je worker.

Codex:

- dostane issue title a description
- bezi vo workspace daného issue
- vykona to, co prikazuje `WORKFLOW.md`
- vytvori artefakty alebo vykona repo task podla aktivneho operating modu

## Current Operating Mode

Aktualny prvy pouzitelny mod je:

`OpenClaw execution prep`

To znamena, ze ked Symphony zoberie issue, Codex zatial:

- neimplementuje automaticky celu pracu
- ale pripravi vykonatelny packet pre dalsi krok

Aktualne artefakty su:

- `execution-prep.md`
- `subtasks.md`
- `status.md`

Tento mod je zamerne konzervativny.

Je vhodny, ked:

- issue ma dost kontextu na pripravu planu
- ale este nechceme, aby agent robil siroke zmeny v kode alebo systemoch
- chceme reviewable handoff pre `OpenClaw`

## Issue Lifecycle

### 1. OpenClaw alebo human zalozi issue v Linear

Issue musi byt:

- konkretne
- ohranicene
- s jasnym outputom

Ak issue nie je konkretne, Codex pripravi len partial packet a vypise open questions.

### 2. Symphony issue preberie

Symphony:

- najde issue v aktivnom stave
- vytvori alebo znovu pouzije workspace
- spusti Codex session

### 3. Codex pripravi packet

V `prep` mode Codex:

- precita issue
- vezme dostupny kontext
- pripravi execution packet vo workspace

Minimalne cakam:

- ciel
- scope
- out of scope
- constraints
- deliverables
- definition of done
- rozsekane subtasky
- pomenovane blockers a open questions

### 4. OpenClaw packet skontroluje

OpenClaw:

- pozrie artefakty
- rozhodne, ci su dost dobre
- pouzije ich dalej
- vytvori alebo rozdistribuuje nasledne execution issues
- upravi stav v Linear

### 5. Human dava dalsi smer

Human:

- schvaluje alebo koriguje smer
- rozhoduje prioritu
- hovori, co sa ide dalej vykonavat

Tym sa uzatvara operacna slucka.

## Parent Issue vs Execution Issues

Pouzivaj dva levely prace.

### Parent issue

Parent issue je strategicke alebo koordinacne zadanie.

Typicky:

- vacsia tema
- viac rol alebo lane
- potreba rozkladu na casti

Parent issue je vhodne pre:

- `prep`
- rozsek taskov
- urcenie workerov
- definovanie contractov

### Execution issue

Execution issue je jednotka konkretnej prace.

Ma byt:

- samostatne vykonatelne
- s jasnym outputom
- s minimalnym ambiguity

Execution issues maju vznikat z parent issue alebo z OpenClaw review.

## How To Write A Good Issue

Dobre issue by malo mat:

- `Goal`
- `Scope`
- `Out of scope`
- `Expected output`
- `Definition of done`
- `Relevant context`
- `Constraints`

Ak tam toto chyba, agent sice nieco pripravi, ale packet nebude naozaj execution-ready.

### Bad examples

- `sprav outreach`
- `rozbehni sales`
- `vymysli agentov`

### Good examples

- `Priprav execution packet pre CRO outbound lane. Vystup: definicia skillov, read context, output contract a 5 execution issues.`
- `Navrhni 4 outreach angles pre CFO segment. Vystup daj do outreach-angles.md. Nepis emaily, len strategy draft.`
- `Rozsekaj CEO lane na implementacne slices pre Symphony/OpenClaw workflow.`

## What Codex Should Do In This Mode

V tomto mode ma Codex:

- pripravit packet
- nepredstierat, ze praca je hotova, ak chyba kontext
- jasne napisat blockers
- vytvorit subtask decomposition

Codex v tomto mode nema:

- robit siroke mutacie mimo workspace
- vymyslat skryty kontext, ktory nedostal
- oznacovat issue za hotove len preto, ze vytvoril nejaky subor

## What OpenClaw Should Do After Packet Creation

Po vytvoreni packetu ma OpenClaw:

1. pozriet `execution-prep.md`
2. pozriet `subtasks.md`
3. rozhodnut, ci packet:
   - je dost dobry na pouzitie
   - potrebuje doplnenie
   - treba vratit na nove issue s dalsim kontextom
4. vytvorit alebo aktivovat dalsie konkretne execution issues
5. aktualizovat `Linear`

OpenClaw je teda reviewer, router a operator nad packetom.

## Practical Daily Loop

Kazdodenny loop ma vyzerat takto:

1. Ja urcim prioritu alebo ciel.
2. OpenClaw z toho vytvori alebo upravi `Linear` issue.
3. Symphony issue preberie.
4. Codex spravi packet vo workspace.
5. OpenClaw packet skontroluje a pouzije.
6. OpenClaw oznaci alebo posunie issue v `Linear`.
7. Ja dam dalsi smer alebo zmenu priority.

Toto je momentalne najstabilnejsi sposob pouzivania systemu.

## What "Done" Means Right Now

V aktualnej faze nie je `done` to iste ako "full execution complete".

Aktualne rozlisujeme:

- `packet done`
  - workspace obsahuje kvalitny prep packet
- `execution done`
  - nasledny worker alebo lane vykonal konkretnu pracu
- `operator accepted`
  - OpenClaw alebo human potvrdil, ze vystup je pouzitelny

Netreba tieto tri stavy miesat.

## Current Limitation

Aktualny operating mode je vhodny hlavne na:

- decompoziciu
- planning
- packet creation
- handoff preparation

Nie je to este finalny mod pre:

- plne autonomne repo execution vo velkom
- volne agentic riadenie viacerych externych systemov
- "zadaj firmovy ciel a nech sa to cele same vykona"

Na to bude treba dalsie workflow modu a lepsie definovane role/permissions/context surfaces.

## Recommended Next Step

Najblizsi prakticky krok je:

- pouzivat parent issue na strategicke zadania
- z packetu robit mensie execution issues
- nechat `OpenClaw` rozhodovat, ktore z nich idu dalej

Tymto sposobom sa system da realne pouzivat uz teraz bez toho, aby predstieral vacsiu autonomiu, nez aku skutocne ma.
