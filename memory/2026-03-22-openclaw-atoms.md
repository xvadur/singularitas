# Session: 2026-03-22 23:51:16 UTC

- **Session Key**: agent:main:main
- **Session ID**: b139d3f2-570b-4aa1-9138-3e7627a57e2a
- **Source**: webchat

## Conversation Summary

assistant: [[reply_to_current]] Hotovo.

Zapísal som to do Obsidianu sem:
`/Users/_xvadur/singularitas_opus/Xvadur OS Unification Blueprint v1.md`

Ďalší logický krok je podľa mňa:
1. z toho spraviť **canonical spec v singularitas/projects/**
2. potom z neho vyrobiť:
   - **agent registry**
   - **morning/evening brief templates**
   - **routing matrix**
   - **14-day rollout checklist**

Ak chceš, idem hneď na ten ďalší krok.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sun 2026-03-22 23:21 GMT+1] dobre a teraz to mozeme dekomponovat na drobne atomy aby sme zistili ake mame moznosti v openclaw a aby sme zistili ako by to cele mohlo vyzerat a bolo to v sulade s dokumentaciou
assistant: Najprv si rýchlo overím relevantné OpenClaw surfaces v lokálnej dokumentácii, aby sme to rozsekali podľa reality frameworku, nie podľa wishful thinking.
assistant: [[reply_to_current]] Áno. Toto je presne správny ďalší krok.

**Verdikt:**
teraz to nemáme ďalej rozvíjať ako víziu, ale **rozobrať na OpenClaw primitíva** a oddeliť:

1. **čo OpenClaw už vie natívne**
2. **čo vie cez správny lane/skill**
3. **čo vyžaduje glue v n8n / web / externých tooloch**
4. **čo je governance, nie technický problém**

A popri tom sa držať authority splitu, ktorý už máme v docs:

- `singularitas_opus` = capture / knowledge
- `singularitas` = runtime doctrine, agents, routing, packets, heartbeats
- `firma` = business truth, approvals, delivery state, publishing queue, content queue, pipeline  
Source: `docs/singularity-eco-authority-matrix.md`

A zároveň je v staršom runtime pláne už jasný smer:
- founder-readable registry
- explicit agent workspaces
- heartbeat guardrails
- project-home contract  
Source: `docs/plans/2026-03-17-runtime-refactor-plan.md`

Čiže: **smer je správny, len to musíme preložiť do atomov.**

---

# Xvadur OS dekompozícia na atómy

Nižšie to rozsekám tak, aby bolo jasné:
- capability
- OpenClaw primitive
- owner lane
- system of record
- approval model
- poznámka k realite

---

# 1. Founder command layer

## Atom 1.1 — jedno vstupné rozhranie
**Potrebujeme:** aby si komunikoval primárne s Jarvisom, nie s každým agentom zvlášť.

- **OpenClaw primitive:** main agent + `sessions_send` / `sessions_spawn` / routing
- **Owner:** Jarvis
- **Record:** `singularitas`
- **Approval:** n/a
- **Reality:** toto je natívne možné už teraz

### Čo to znamená prakticky
Ty dáš:
- dump
- otázku
- task
- approval
- korekciu

Jarvis rozhodne:
- či to rieši priamo
- či to deleguje
- komu
- v akom formáte
- čo ti má prísť späť

---

## Atom 1.2 — founder review loop
**Potrebujeme:** aby agenti vracali návrhy, nie chaos.

- **Primitive:** packets v súboroch + subagent/session outputs
- **Owner:** Jarvis + owner lane
- **Record:** `singularitas` pre packet trace, `firma` ak to mení business state
- **Approval:** draft-first
- **Reality:** governance problem, nie tooling problem

### Required output shape
Každý návrat má mať:
- verdict
- evidence
- recommendation
- risks
- needs approval?

Toto je kritické.

---

# 2. Agent layer

## Atom 2.1 — agent registry
**Potrebujeme:** founder-readable mapu agentov, ich scope a outputov.

- **Primitive:** markdown docs
- **Owner:** Jarvis / ops
- **Record:** `singularitas`
- **Approval:** internal only
- **Reality:** toto by malo byť canonical a v súlade s runtime refactor planom

### Minimálne polia
- agent id
- mission
- owns
- does not own
- input types
- output contract
- escalation rules
- heartbeat behavior

---

## Atom 2.2 — routing matrix
**Potrebujeme:** otázka → owner lane → support lane → output.

- **Primitive:** markdown spec
- **Owner:** Jarvis
- **Record:** `singularitas`
- **Approval:** internal only

Bez tohto bude swarm chaos.

---

## Atom 2.3 — lane packets
**Potrebujeme:** jednotný task packet, ktorý Jarvis pošle agentovi.

- **Primitive:** `sessions_send` / `sessions_spawn` + markdown packet pattern
- **Owner:** Jarvis
- **Record:** `singularitas`
- **Approval:** n/a

### Packet contract
- Objective
- Context
- Constraints
- Output format
- Verification
- Stop condition

---

# 3. Daily operating rhythm

## Atom 3.1 — morning brief
**Potrebujeme:** 08:00 founder brief.

- **Primitive:** `cron` + agentTurn/systemEvent
- **Owner:** Jarvis
- **Sources:** research lane, calendar, active work fronts, watchlists
- **Record:** brief môže byť transient + prípadne trace v `singularitas`
- **Approval:** not needed for delivery of the brief itself

### OpenClaw fit
Toto je presne to, na čo je `cron` dobrý.

---

## Atom 3.2 — evening brief
**Potrebujeme:** 20:00 diff briefing.

- **Primitive:** `cron`
- **Owner:** Jarvis
- **Sources:** morning commitments, packets, completions, blockers
- **Record:** transient + optional summary artifact
- **Approval:** no

---

## Atom 3.3 — heartbeat interrupt layer
**Potrebujeme:** iba action-forcing nudges.

- **Primitive:** normal agent response + heartbeat rules
- **Owner:** Jarvis
- **Record:** `singularitas` doctrine
- **Approval:** n/a

### Dôležité
Heartbeat nemá byť status report.
Len:
- blocker
- approval needed
- dominant next move
- urgent opportunity
- deadline risk

---

# 4. Research engine

## Atom 4.1 — world scan
**Potrebujeme:** priebežný AI/world signal scan.

- **Primitive:** research lane + web search/fetch + prípadne external skill/source
- **Owner:** `research`
- **Record:** `singularitas` packet trace, extrakty do `firma` alebo `opus` podľa použitia
- **Approval:** no, read-only

### Reality
OpenClaw vie:
- web search
- web fetch
- memory
- cron-triggered agent turns

To znamená, že **briefing intelligence layer** je realistická.

---

## Atom 4.2 — source shaping for content
**Potrebujeme:** aby research neostal len zhrnutie správ.

- **Primitive:** delegated packet
- **Owner:** `research`
- **Support:** `growth`
- **Record:** content-supporting artifacts podľa potreby

### Output
- top signals
- why it matters
- angle for founder audience
- possible CTA/use in newsletter/post

---

# 5. Content engine

## Atom 5.1 — founder dump ingestion
**Potrebujeme:** aby si dal raw myšlienky a systém ich rozložil.

- **Primitive:** chat input to Jarvis
- **Owner:** Jarvis
- **Record:** transient, prípadne concept note v `singularitas_opus`
- **Approval:** n/a

---

## Atom 5.2 — content packet generation
**Potrebujeme:** z dumpu spraviť viac formátov.

- **Primitive:** routing na `growth` + support lanes
- **Owner:** `growth`
- **Support:** `research`, `proof`, `web`
- **Record:** draft artifacts ideálne do `firma` ak sú už publishing queue, inak staging v `singularitas`

### Output
- reel script
- carousel structure
- newsletter abstract
- blog outline
- lead magnet angle
- CTA recommendation

---

## Atom 5.3 — content queue
**Potrebujeme:** publishing queue a approval state.

- **Primitive:** file-based queue alebo business repo structure
- **Owner:** `web` / `growth`
- **Record:** **`firma`**
- **Approval:** yes

### Prečo `firma`
Lebo publish state a content queue sú business truth, nie runtime doctrine.  
To sedí s authority matrix.

---

## Atom 5.4 — lead magnet / PDF pipeline
**Potrebujeme:** pravidelný downloadable asset.

- **Primitive:** content generation + export path
- **Owner:** `growth` / `proof` / `web`
- **Record:** `firma`
- **Approval:** yes before release

### Reality
OpenClaw vie pomôcť s draftingom a orchestration.
Samotný polished PDF pipeline môže vyžadovať:
- templates
- scripts
- build/export tooling

To je skôr `build` + `web`.

---

## Atom 5.5 — video scripting lane
**Potrebujeme:** samostatný script engine pre short videos.

- **Primitive:** skill/workspace instructions + packetization
- **Owner:** `growth`
- **Support:** `proof`, `research`
- **Record:** `firma` ak ide do queue, inak staging

---

# 6. Web / funnel / metrics

## Atom 6.1 — landing page drafting
**Potrebujeme:** drafty úprav landing page a funnel page.

- **Primitive:** `web` lane
- **Owner:** `web`
- **Support:** `growth`
- **Record:** `firma`
- **Approval:** yes

---

## Atom 6.2 — web implementation
**Potrebujeme:** reálne zmeny na Astro surface.

- **Primitive:** `build` lane / ACP coding sessions / file edits
- **Owner:** `build`
- **Support:** `web`
- **Record:** repo v `firma` ak to je canonical web

### Dôležité
Toto je presne miesto, kde musíme rozhodnúť repo boundary:
- runtime/docs → `singularitas`
- business web/funnel → pravdepodobne `firma`

---

## Atom 6.3 — analytics digestion
**Potrebujeme:** digest metrik, nie ručné pozeranie dashboardov.

- **Primitive:** externé integrations + cron + summary packet
- **Owner:** `web` / `growth` / `ops`
- **Record:** `firma`
- **Approval:** no na reporting, yes na changes

### Reality
OpenClaw vie scheduling + reporting.
Ale metriky musia prísť z:
- analytics stacku
- scripts
- APIs
- n8n glue

Čiže to je kombinácia OpenClaw + externá infra.

---

## Atom 6.4 — optimization proposals
**Potrebujeme:** návrhy, nie autonómne live zásahy.

- **Primitive:** heuristics packet + approval loop
- **Owner:** `growth`
- **Support:** `web`
- **Record:** `firma`
- **Approval:** yes

---

# 7. Client delivery / voice pilot

## Atom 7.1 — meeting prep
**Potrebujeme:** Jakub packet na stretnutie.

- **Primitive:** Jarvis routes to `revenue` + `delivery` + `voice`
- **Record:** `firma` ak z toho vzniká commercial/delivery truth
- **Approval:** founder review

---

## Atom 7.2 — pilot spec
**Potrebujeme:** success criteria, scope, collaboration options.

- **Primitive:** packet + doc artifacts
- **Owner:** `delivery`
- **Support:** `revenue`, `voice`, `integration`
- **Record:** `firma`

---

## Atom 7.3 — voice implementation lane
**Potrebujeme:** Vapi/ElevenLabs prompt, tool flow, QA.

- **Primitive:** `voice` + `integration`
- **Record:** runtime artifacts in `singularitas`, engagement/client truth in `firma`

---

# 8. Personal ops / founder support

## Atom 8.1 — calendar accountability
**Potrebujeme:** brief + reminders + next commitments.

- **Primitive:** calendar skill/integration + cron + personal-ops lane
- **Owner:** `personal-ops`
- **Record:** personal context skôr `singularitas_opus`, commitments ak business-relevant aj `firma`

---

## Atom 8.2 — meals / movement / rhythm
**Potrebujeme:** light accountability, nie gimmick engine.

- **Primitive:** reminders/check-ins
- **Owner:** `personal-ops`
- **Record:** `singularitas_opus`
- **Approval:** no

### Reality
Toto je možné.
Ale nesmie to zjesť business priority.

---

## Atom 8.3 — weekly planning / time blocking
**Potrebujeme:** structured planning support.

- **Primitive:** briefing + planning packets
- **Owner:** `personal-ops` + Jarvis
- **Record:** personal in `opus`, business-relevant commitments in `firma`

---

# 9. CRM / roadmap / business truth

## Atom 9.1 — decisions
- **Record:** `firma`

## Atom 9.2 — opportunities / leads
- **Record:** `firma`

## Atom 9.3 — delivery state
- **Record:** `firma`

## Atom 9.4 — publish queue
- **Record:** `firma`

## Atom 9.5 — runtime packets / doctrine
- **Record:** `singularitas`

## Atom 9.6 — founder thought dumps / raw notes
- **Record:** `singularitas_opus`

Toto je možno najdôležitejší alignment s docs.

---

# 10. Čo OpenClaw už vie natívne vs čo treba dostavať

## Natívne vie veľmi dobre
- main orchestrator model
- delegáciu do ďalších sessions/subagents
- cron jobs
- heartbeat-style interrupting
- browser control
- nodes / device integrations
- messaging
- memory recall
- file-based system of record
- session-based orchestration

## Vie dobre, ale potrebuje správny contract
- multi-agent governance
- routing discipline
- daily briefings
- draft approval loops
- content packet orchestration
- founder operating cadence

## Potrebuje externý glue / infra
- ManyChat execution
- analytics ingestion
- polished content publishing pipeline
- n8n backend specifics
- Astro/Vercel deployment flow
- production web optimization loop
- PDF export system
- CRM truth sync, ak nebude čisto file-based/local

Čiže pointa:
**OpenClaw je orchestra framework, nie magická náhrada celej business infra.**
Ale na command layer je presne vhodný.

---

# 11. Ako by to celé mohlo vyzerať v súlade s docs

## Reálny compliant shape

### `singularitas`
- agent registry
- routing matrix
- packet contracts
- briefing contracts
- cron architecture
- heartbeat rules
- runtime docs
- internal lane specs

### `singularitas_opus`
- tvoje raw notes
- founder dumpy
- osobné kontexty
- briefing inputs
- long-form myšlienky
- knowledge capture

### `firma`
- klienti
- piloty
- rozhodnutia
- approvals
- web/funnel docs
- content queue
- offers
- roadmap
- delivery truth
- publishing truth

Toto sedí aj na authority matrix, aj na to čo chceš.

---

# 12. Dekompozícia do prvých pracovných balíkov

Ak to chceme robiť disciplinovane, ďalšie work packets sú:

## Packet A — Runtime governance
- agent registry
- routing matrix
- output contracts
- escalation rules

## Packet B — Briefing system
- morning brief schema
- evening brief schema
- heartbeat rules
- cron plan

## Packet C — Workspace authority cleanup
- singularitas vs opus vs firma
- čo kam patrí
- čo presunúť
- čo nechať

## Packet D — Revenue/delivery pilot layer
- Jakub meeting packet
- pilot spec
- collaboration option map

## Packet E — Content engine v1
- founder dump → content packet
- queue shape
- approval flow
- lead magnet pipeline

## Packet F — Web/funnel architecture
- repo decision
- Astro/Vercel decision shape
- analytics and optimization shape

---

# Môj tvrdý odporúčaný next move

Nesnažil by som sa teraz rozobrať každý OpenClaw feature ad hoc v chate.

Správny ďalší krok je:
## spraviť **Capability Map + Compliance Spec**
kde bude pri každom subsystéme:

- objective
- OpenClaw primitive
- lane owner
- source of truth
- approval class
- blockers
- phase

To je ten most medzi víziou a implementáciou.

Ak chceš, idem hneď na to a napíšem ti do Obsidianu druhý dokument:

## **Xvadur OS Capability Map (OpenClaw-aligned)**

s tabuľkami a presnými sekciami:
- Founder OS
- Agent OS
- Briefing OS
- Content OS
- Delivery OS
- Web/Funnel OS
- Personal Ops OS
- Systems of Record
- What OpenClaw natively covers / what needs glue

To by bol teraz najsprávnejší artifact.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sun 2026-03-22 23:35 GMT+1] nice, podme teda naplanovat ako to cele impleremtujeme v priebehu nasledujucich 7 dni
assistant: Správne. Teraz už nie vízia, ale 7-dňová implementácia.
assistant: [[reply_to_current]] Áno. Poďme to stiahnuť na **7-dňový implementation sprint**.

Nebudeme sa tváriť, že za 7 dní postavíme celý Xvadur OS.
Za 7 dní postavíme:

**fungujúci V1 operating core**, na ktorom sa dá ďalej vrstviť.

---

# 7-day implementation plan

## 1. Objective
Za 7 dní zaviesť **Xvadur OS V1**: zjednotenú agent vrstvu, founder briefing rytmus, workspace authority split, pilot-ready delivery support pre Jakuba a základ content pipeline, všetko v súlade s OpenClaw dokumentáciou.

---

## 2. Scope

### In scope
- agent registry + routing matrix
- founder operating model
- morning/evening brief contracts
- heartbeat/cron design
- workspace authority split:
  - `singularitas`
  - `singularitas_opus`
  - `firma`
- Jakub / realitný pilot support packet
- content pipeline V1:
  - founder dump → content packet
- implementation sequence a ownership

### Out of scope
- full ManyChat production deployment
- full analytics infra
- complete n8n backend ecosystem
- complete habit tracker system
- fully autonomous publishing
- full Astro/Vercel migration

---

## 3. Assumptions
1. **Telegram** ostáva primary runtime surface.
2. Default approval model je **draft-first, publish/send/change-live po schválení**.
3. `firma` bude business truth repo.
4. `singularitas` bude runtime/governance/system layer.
5. Tento sprint je o **governance + operating core**, nie o complete business automation.

---

## 4. Execution plan

## Step 1: Discovery + freeze architecture
**Cieľ:** uzamknúť systémové hranice a nevymýšľať ich každý deň znova.

### Deliverables
- `Xvadur OS Capability Map`
- finálny authority split
- V1 lane list
- approval classes
- implementation sequence

### Tasks
1. spraviť capability map po subsystémoch:
   - founder OS
   - agent OS
   - briefing OS
   - delivery OS
   - content OS
   - web/funnel OS
   - personal ops OS
2. pre každý subsystem určiť:
   - objective
   - OpenClaw primitive
   - owner lane
   - source of truth
   - approval requirement
   - blocker
3. rozhodnúť repo hranice:
   - čo ostáva v `singularitas`
   - čo ide do `singularitas_opus`
   - čo ide do `firma`

### Output
1 canonical planning doc + clear boundaries

---

## Step 2: Design the operating core
**Cieľ:** definovať, ako sa systém správa cez deň.

### Deliverables
- agent registry
- routing matrix
- packet contract
- review contract
- morning brief template
- evening brief template
- heartbeat rules
- cron plan

### Tasks
1. spraviť founder-readable agent registry
2. dopísať routing matrix:
   - otázka → owner lane → support → output
3. dopísať packet contract:
   - Objective
   - Context
   - Constraints
   - Output
   - Verification
   - Stop condition
4. dopísať review contract:
   - Verdict
   - Evidence
   - Recommendation
   - Risks
   - Approval needed
5. navrhnúť ranný brief a večerný brief
6. navrhnúť cron jobs V1
7. zafixovať heartbeat trigger rules

### Output
Runtime governance layer ready for implementation

---

## Step 3: Execute the V1 system in files + first live operating surfaces
**Cieľ:** premeniť blueprint na skutočné pracovné artefakty.

### Deliverables
- canonical docs v `singularitas/projects/`
- agent-facing docs / registry updates
- briefing docs
- Jakub pilot packet
- content packet template
- workspace cleanup plan

### Tasks
1. vytvoriť project home pre Xvadur OS v `projects/`
2. zapísať:
   - brief
   - status
   - watchlist
   - metrics
   - spec docs
3. pridať/aktualizovať:
   - agent registry
   - operating contracts
   - routing matrix
4. pripraviť Jakub / Monday packet:
   - pilot scope
   - questions
   - collaboration options
   - success criteria
5. pripraviť content packet template:
   - founder dump input
   - reel script
   - carousel
   - newsletter abstract
   - blog angle
   - lead magnet angle
6. pripraviť workspace cleanup map:
   - čo presunúť
   - čo nechať
   - čo je stale unclear

### Output
System exists as files, not just chat intent

---

## Step 4: Validate + start controlled use
**Cieľ:** overiť, že systém funguje bez chaosu.

### Deliverables
- first daily brief cycle
- first routing test
- first content packet test
- first delivery packet test
- backlog of phase-2 implementation

### Tasks
1. odsimulovať 1 ranný brief
2. odsimulovať 1 večerný brief
3. spraviť 1 real routing run:
   - napr. content dump → content packet
4. spraviť 1 real delivery run:
   - Jakub packet
5. zhodnotiť:
   - kde vzniká friction
   - kde sú duplicity
   - čo treba automizovať až neskôr
6. pripraviť phase-2 backlog:
   - cron implementation
   - analytics ingestion
   - web/funnel ops
   - content queue
   - personal ops reminders

### Output
V1 operating core je overený na reálnom use-case, nie len teoreticky

---

## 5. Risks + mitigations

### Risk 1: too much scope in 7 days
**Mitigation:** sústrediť sa len na governance + operating core + pilot support

### Risk 2: architecture spiral
**Mitigation:** každé rozhodnutie musí skončiť v súbore alebo template

### Risk 3: mixing business truth with runtime truth
**Mitigation:** striktne držať authority split podľa docs

### Risk 4: agent registry without execution value
**Mitigation:** registry musí mať routing + outputs + approvals, nie len identity flavor

### Risk 5: content lane steals focus from revenue lane
**Mitigation:** Jakub/pilot je dominantný real-world validation front

### Risk 6: too much automation too early
**Mitigation:** najprv templates + docs + routing, až potom cron/autonomy

---

## 6. Milestones

## Day 1
- finalize capability map
- finalize authority split
- finalize V1 scope
- create implementation project home

## Day 2
- write agent registry
- write routing matrix
- write packet + review contracts

## Day 3
- write morning/evening brief specs
- write heartbeat rules
- write cron architecture V1

## Day 4
- prepare Jakub pilot packet
- prepare delivery/revenue operating artifacts
- define founder review flow

## Day 5
- build content packet template
- define founder dump → content pipeline
- define queue/approval shape

## Day 6
- workspace cleanup plan
- decide `firma` role more concretely
- define web/funnel implementation boundary

## Day 7
- run first full review:
  - morning brief mock
  - one routed task
  - one content packet
  - one pilot packet
- produce phase-2 backlog

---

## 7. Acceptance checklist

Po 7 dňoch to musí znamenať, že máme:

- [ ] jasne definovaný authority split medzi `singularitas`, `singularitas_opus`, `firma`
- [ ] founder-readable agent registry
- [ ] routing matrix
- [ ] packet contract
- [ ] review contract
- [ ] morning brief contract
- [ ] evening brief contract
- [ ] heartbeat rules
- [ ] cron architecture V1
- [ ] Jakub pilot packet
- [ ] content packet template
- [ ] workspace cleanup map
- [ ] phase-2 backlog

A hlavne:
- [ ] systém už existuje ako **operating artifact**
- [ ] nie si odkázaný na improvizované prepínanie medzi agentmi
- [ ] Jarvis môže fungovať ako command layer

---

# Môj odporúčaný sequencing verdict

Ak to chceme urobiť správne, poradie je:

1. **capability map**
2. **governance docs**
3. **briefing system**
4. **pilot support**
5. **content pipeline**
6. **workspace cleanup**
7. **first live validation**

---

Ak chceš, môžem teraz spraviť hneď ďalší konkrétny krok:

## zapíšem tento 7-day sprint do Obsidianu
a/alebo
## vytvorím z neho canonical project skeleton v `singularitas/projects/xvadur-os/`

Ja by som odporúčal spraviť **oboje**, ale prvý správny pohyb je:
**project skeleton v singularitas/projects/**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sun 2026-03-22 23:39 GMT+1] mozes z toho spravit canon project 
zapis master brief a k tomu samostatny check list na 7 dni, aby sme to mohli postupne vykonavat
assistant: Spravím z toho canonical project v `singularitas/projects/` a rozdelím to na master brief + 7-day checklist.
assistant: Idem to uložiť ako nový project home `projects/xvadur-os-v1/` s briefom, statusom, metrics, watchlistom a samostatným 7-day checklistom.
assistant: Project home je hotový, ešte dorobím prázdne required subfolders podľa template contractu.
assistant: [[reply_to_current]] Hotovo.

Spravil som canonical project home tu:

`/Users/_xvadur/singularitas/projects/xvadur-os-v1/`

## Vytvorené súbory
- `brief.md` — master brief
- `checklist-7-days.md` — samostatný 7-day execution checklist
- `status.md`
- `metrics.md`
- `watchlist.md`
- `README.md`

## Vytvorené subfolders
- `approvals/`
- `approved-for-firma/`
- `artifacts/`
- `content/`
- `handoffs/`
- `spec/`
- `staging/`
- `validation/`

Toto je už dobrý canonical base.

## Môj odporúčaný next move
Teraz by som nešiel ďalej široko.
Išiel by som presne podľa Day 1:

1. `spec/capability-map.md`
2. `spec/authority-split.md`
3. `spec/agent-registry.md`
4. `spec/routing-matrix.md`

To je správny ďalší balík.

Ak chceš, idem hneď vyplniť **Day 1 artifacts**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sun 2026-03-22 23:43 GMT+1] /save zapis to do pamate ako aktivnu otvorenu ulohu ktrora je teraz primarna, zapis to do pamate aby som mohol dat novu konverzaciu a pokracovat aj cez telegram
assistant: Zapíšem to ako primárny otvorený front do dlhodobej aj dennej pamäte, aby sa na to dalo plynulo nadviazať aj z Telegramu.
assistant: [[reply_to_current]] Hotovo.

Zapísal som to na dve úrovne:

### Dlhodobá pamäť
Do `MEMORY.md` som pridal, že:
- **primárna otvorená úloha je `xvadur-os-v1`**
- ide o zjednotenie agent vrstvy do founder command systemu
- **Telegram je primary runtime**
- canonical project home je:
  `/Users/_xvadur/singularitas/projects/xvadur-os-v1/`

### Denná kontinuita
Vytvoril som:
- `/Users/_xvadur/singularitas/memory/2026-03-22.md`

Je tam:
- current primary front
- locked operating direction
- approval model
- created artifacts
- immediate next move

Takže áno — keď otvoríš novú konverzáciu, aj cez Telegram, toto by malo byť normálne nadviazateľné.

Ďalší správny krok nabudúce je:
**Day 1 artifacts**
- capability map
- authority split spec
- agent registry
- routing matrix
