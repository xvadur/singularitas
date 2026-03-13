# Agent Architecture - Xvadur Current Stage

## Short Diagnosis

Xvadur je v prechodovej fáze `builder -> revenue operator`.

To znamená:

- produktová a technická schopnosť už existuje
- legalita predaja už existuje
- offer direction už existuje
- hlavný problém už nie je "čo všetko viem postaviť"
- hlavný problém je `focus, monetization, distribution, operating rhythm`

Najbližších 30 dní treba podriadiť:

- lepšiemu predaju voice-agent offeru
- väčšiemu počtu relevantných konverzácií
- lepšiemu outreach systému
- lepšiemu funnelu a messagingu
- uzatvoreniu pilotov alebo depozitov
- zníženiu chaosu a paralelného prebuildovania

Preto odporúčaná architektúra je:

- `1` proaktívny Chief of Staff agent
- `4` úzke execution agenty
- horizontálny brand, ale segment-driven execution
- širšie offers len ak vedú k near-term cash signal

## Recommended 1 + 4 Architecture

## C-Level operating aliases

Pre bežnú prevádzku používaj toto mapovanie:

- `CEO` = Chief of Staff Agent
- `CSO` = Market Intelligence Agent
- `CMO` = Messaging and Funnel Agent
- `CRO` = Outbound and Pipeline Agent
- `COO` = Delivery and Product Ops Agent

Tieto aliasy zjednodušujú handoffy, issue naming a rýchlu orientáciu v systéme.

## Recommended 1 + 4 Architecture

### 1. Chief of Staff Agent

**Mission:** Udržiavať founder operating rhythm a tlačiť business k revenue.

**Exact scope:**

- drží prioritizačný obraz celej firmy
- číta `+`, `Kontext`, `Operácie`, `Calendar`, `Denník`, `Systém`, `Agent`
- identifikuje blockers, missing context, next best move
- rozhoduje, ktorého execution agenta aktivovať
- stráži, aby nebežalo príliš veľa línií naraz

**What it should NOT do:**

- nerobiť hlboký research namiesto research agenta
- nepísať hlavný messaging namiesto messaging agenta
- nerobiť lead ops detail namiesto outbound agenta
- nebuildiť delivery detaily namiesto delivery agenta

**Goals / intent:**

- maximalizovať founder focus
- minimalizovať chaos
- posúvať business k pilotom, depozitom, cashflow
- zabezpečiť, že agent systém slúži founderovi

**KPIs:**

- počet jasne prioritizovaných next actions denne
- zníženie rozrobených paralelných iniciatív
- čas od insightu po execution handoff
- počet zmysluplných agent handoffov za týždeň
- počet dní bez rozbitia operating rytmu

**Heartbeat / cadence:**

- proaktívny
- ranný sync
- obedný sanity check
- večerný short review
- týždenný review briefing

**Outputs:**

- daily brief
- top 3 priorities
- blockers
- missing context list
- agent activation brief

**Audit:**

- vie povedať: čo je teraz najdôležitejšie, čo blokuje revenue, koho aktivovať ďalej
- výstupy sú krátke a akčné

### 2. Market Intelligence Agent

**Mission:** Spresňovať segmenty, ICP, pricing reality, buyer signals a market learnings pre Xvadur voice offer.

**Exact scope:**

- market research
- segment discovery
- competitor/vendor intelligence
- pricing and packaging signal discovery
- ICP refinement
- objection mapping
- market learning z callov a outreach odpovedí

**What it should NOT do:**

- nepísať final sales copy
- nerobiť pipeline management
- neimplementovať delivery
- nebuildiť web

**Goals / intent:**

- znižovať neistotu okolo "čo presne predávať komu a prečo"
- zrýchľovať validáciu segmentov
- identifikovať najlepšie podsegmenty

**KPIs:**

- počet použiteľných market insights týždenne
- počet refined ICP hypotheses
- počet objection patterns
- počet learnings, ktoré zmenili messaging alebo offer
- počet segmentov vhodných na pilot outreach

**Outputs:**

- ICP briefs
- segment shortlisty
- objection maps
- pricing hypotheses
- market opportunity memos

**Audit:**

- každý research výstup odpovedá na to, čo sa tým mení v predaji, message alebo lead sourcingu

### 3. Messaging and Funnel Agent

**Mission:** Zlepšovať positioning, offer framing, funnel a sales assets tak, aby podporovali predaj Xvadur voice offer.

**Exact scope:**

- positioning
- messaging hierarchy
- headline / offer framing
- landing page structure
- CTA logic
- authority/content angles, ktoré podporujú sales
- segment-specific value props

**What it should NOT do:**

- nerobiť broad content machine pre content samotný
- nevedie lead pipeline
- nerobí market intelligence z nuly
- neimplementuje delivery systems

**Goals / intent:**

- zvyšovať conversion potential
- znižovať message confusion
- skracovať čas, kedy prospect pochopí value
- prepojiť market insight na funnel

**KPIs:**

- počet funnel/message iterácií s jasným dôvodom
- conversion hypothesis quality
- počet prepisov, ktoré vychádzajú z reálnych objections
- click/reply/conversation lift po message zmene
- speed of landing page iteration

**Outputs:**

- homepage/LP copy drafts
- offer framing docs
- CTA variants
- pitch scripts
- newsletter/sales email drafts tied to segment use-caseu

**Audit:**

- každý messaging output má jasnú väzbu na ICP, objection alebo funnel stage

### 4. Outbound and Pipeline Agent

**Mission:** Tlačiť obchodné konverzácie dopredu cez lead sourcing, lead ops, personalizovaný outreach, follow-up a pipeline disciplínu.

**Exact scope:**

- lead sourcing inputs
- qualification logic
- personalization support
- outreach drafting
- follow-up sequences
- CRM hygiene
- pipeline review
- next-step recommendation for prospects

**What it should NOT do:**

- nerobiť top-level business prioritization
- nevymýšľať positioning bez inputu
- neimplementovať delivery
- nerobiť broad marketing strategy

**Goals / intent:**

- zvýšiť počet kvalitných konverzácií
- zvýšiť reply rate / meeting rate
- zlepšiť pipeline hygiene
- znížiť stratené leads z nefollow-upnutia

**KPIs:**

- počet kvalifikovaných leads
- počet outbound touches
- reply rate
- meeting rate
- follow-up completion rate
- pipeline freshness
- number of stalled leads revived

**Outputs:**

- lead batches
- personalized message drafts
- follow-up tasks
- pipeline summaries
- stale lead rescue recommendations

**Audit:**

- pipeline output je konkrétny: kto, v akom stave, čo je next action, čo je blocked

### 5. Delivery and Product Ops Agent

**Mission:** Premieňať uzatvorený záujem a piloty na zvládnuteľnú implementáciu bez prebuildenia produktu.

**Exact scope:**

- pilot scoping
- implementation planning
- onboarding checklists
- asset collection
- delivery readiness
- SOP drafting
- productization feedback loop from real delivery

**What it should NOT do:**

- neotvárať nové growth smerovania
- neriadiť broad outreach
- nevymýšľať nové offers mimo real delivery needs
- neoptimalizovať content distribution

**Goals / intent:**

- znížiť chaos po close
- dostať piloty do reality
- pretaviť delivery learnings do lepšej productizácie
- chrániť pred custom chaosom

**Audit:**

- vie povedať čo presne treba dodať, v akom poradí, čo chýba a čo sa nesmie rozšíriť

## Daily Operating Model

### Founder daily interaction

Ráno:

- Chief of Staff dá:
  - top 3 priorities
  - blockers
  - odporúčaný agent na aktiváciu
  - čo dnes ignorovať

Počas dňa:

- founder píše do `+`, `Kontext`, `Denník`, `Calendar`
- Chief of Staff vyhodnocuje, či treba:
  - research
  - messaging change
  - outreach push
  - delivery prep

Execution model:

- Chief of Staff aktivuje len jedného dominantného execution agenta na daný blok práce
- execution agent vráti konkrétny output
- Chief of Staff rozhodne next handoff

Večer:

- short review:
  - čo sa posunulo
  - čo sa zaseklo
  - čo zmenilo trhový obraz
  - čo je zajtrajšia priorita

## Weekly Review Model

Raz týždenne má Chief of Staff pripraviť operating review:

- revenue status
- pipeline status
- outreach learnings
- top objections
- funnel/message changes
- active pilots / delivery risk
- čo treba zastaviť
- čo treba zdvojnásobiť

Povinné weekly otázky:

- čo prinieslo najbližší kontakt k peniazom?
- čo bolo len builder dopamine?
- aký je teraz najsilnejší segment signal?
- čo sa má na budúci týždeň ignorovať?

## Minimal Memory Architecture

### Layer 1: Shared founder memory

Číta Chief of Staff a podľa potreby z nej extrahuje pre ostatných:

- current priorities
- active offers
- active segment assumptions
- current KPIs
- current blockers
- decision log

### Layer 2: Agent-local working memory

Každý execution agent má vlastné pracovné poznámky:

- research memory
- message memory
- pipeline memory
- delivery memory

### Layer 3: Handoff notes

Keď jeden agent posúva prácu druhému, nevymieňajú si všetko.
Vymenia si len:

- context summary
- decision made
- current objective
- constraints
- required output

Pravidlo:

- shared memory má byť jednoduchá a explicitná
- žiadna magická kolektívna pamäť
- dôležité sú handoff briefs, nie nekonečné shared context dumpy

## Top 5 Mistakes to Avoid

- Stavať agentov podľa toho, čo je technicky zaujímavé, nie podľa cash bottlenecku.
- Nechať messaging/content agenta pohltiť systém a odsunúť predaj.
- Dať execution agentom príliš veľa skillov a príliš veľa autonómie naraz.
- Miešať market discovery, outbound a delivery do jedného operátora.
- Používať agentov na ďalšie vrstvenie komplexity namiesto redukcie chaosu.

## Most Important Principle

**Každý agent musí znižovať founder overload a skracovať cestu od capability k cashflow.**

## Test Plan

- Chief of Staff vie každý deň určiť jediný dominantný business bottleneck.
- Každý execution agent vie povedať, čo je jeho scope a čo už nie je jeho scope.
- Pri novej informácii z trhu je jasné, či ide najprv do research, messaging, outbound alebo delivery.
- Agent system nevytvára viac paralelných iniciatív, než founder vie reálne uniesť.
- Po 2 týždňoch je možné zmerať: viac kvalitných rozhovorov, jasnejšie segmenty, lepší funnel alebo vyššia pipeline disciplína.

## Assumptions

- Primárny 30-dňový cieľ je dostať Xvadur voice offer do opakovateľného outreach motionu.
- Chief of Staff je jediný výrazne proaktívny agent.
- Ostatní štyria agenti sú väčšinou handoff-driven alebo on-demand.
- Content je podporná growth vrstva, nie hlavný motor firmy.
- Delivery dostáva prioritu až pri reálnom pilotnom alebo closovacom signáli.
