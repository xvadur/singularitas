# Session: 2026-03-25 23:24:16 UTC

- **Session Key**: agent:main:main
- **Session ID**: d13033a3-112a-453b-ae3a-2489ba5c80cc
- **Source**: webchat

## Conversation Summary

user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Thu 2026-03-26 00:03 GMT+1] a ked ho bindneme na tuto konverzaciu co sa stane?
assistant: [[reply_to_current]] Keď ho **bindneš na túto konverzáciu**, stane sa z toho v praxi **aktívny agent pre tento chat**.

## Prakticky čo sa zmení
Namiesto toho, aby si písal mne/Jarvisovi a ja rozhodoval routing, bude tento thread smerovať na ten ACP session context.

To znamená:
- tvoje ďalšie správy v tomto chate pôjdu **tomu ACP agentovi**
- odpovede bude generovať **on**
- tento chat sa stane jeho pracovným surfaceom

## Inými slovami
Teraz:
- tento chat = Jarvis/main surface

Po bindnutí:
- tento chat = Codex ACP surface  
  alebo minimálne thread naviazaný na tú session

## Čo je na tom dobré
Dobré je to, keď chceš:
- dlhší coding/build session
- súvislú prácu v jednom agent runtime
- menej orchestration, viac priamej práce s jedným agentom

## Čo je na tom zlé pre tvoj current setup
Pre tvoj **multisystem founder OS model** je to často horšie, lebo:
- obchádzaš Jarvisa ako command layer
- strácaš clean routing center
- tento chat sa zmení z founder command surface na specialist surface
- môžeš si rozbiť ten model, ktorý sme práve postavili

## Môj verdict
**Na tento chat by som ho defaultne nebindoval**, ak chceš, aby:
- Jarvis ostal command center
- lanes ostali interné
- multisystem ostal čistý

Bind má zmysel skôr keď chceš:
- “teraz idem 45 min robiť len s Codexom”

Nie keď chceš držať founder-facing operating surface.

## Krátka heuristika
- **Jarvis/main chat** → nechaj unbound
- **specialized coding thread/session** → tam bind dáva zmysel

Ak chceš, poviem ti presne:
**čo je správny bind/unbound model pre tvoj nový multisystem**, aby si si to nepomotal.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Thu 2026-03-26 00:05 GMT+1] okej tak to teraz nepotrebujem. 
podme do voice agenta a podme ho dokoncit, potrebujem aby tam boli vsetky vsetky veci ktore patria k voice businesu
assistant: [[reply_to_current]] Rozumiem tomu tak, že chceš **dotiahnuť `voice` agenta na plný owner lane pre celý voice business**, nie len pre ElevenLabs prompty.  
Teda aby pokrýval **všetko, čo patrí k voice biznisu**: agent design, audit, review, QA, workflowy, handoffy, inventory, readiness, možno aj voice offer/delivery vrstvu — ale bez chaosu.

### ADVANCED SPEC BRIEF

**How I understand it**  
Chceš rozšíriť `voice` z “ElevenLabs operatora” na **úplný owner agent pre voice business lane**, tak aby vedel niesť celý segment konzistentne a bol reusable aj ako model pre iné lanes.

**Confirmed**
- `voice` už existuje ako lane agent.
- Je nastavený na ElevenLabs / voice-agent operations.
- Chceš ho teraz **dokončiť**.
- Chceš, aby tam boli **všetky veci, ktoré patria k voice businessu**.
- Po tomto chceš riešiť aj **workspace polish**.

**Inferred**
- Nechceš len prompt/design vrstvu, ale aj širší operating context voice biznisu.
- Chceš, aby `voice` vedel niesť segment end-to-end na úrovni owner lane.
- Nechceš, aby sa voice lane rozlial do integration/revenue/delivery bez hraníc.
- Chceš z toho spraviť **robustný segment owner contract**, nie len ďalší súbor.

**Critical gaps**
- Čo presne patrí do “voice businessu” a čo už nie.
- Či `voice` má vlastniť aj:
  - offer shaping pre voice lane
  - client-specific deployment packaging
  - vendor/carrier feasibility
  - post-launch performance review
  - sales-support artifacts pre voice ponuku
- Aké sú presné hranice voči:
  - `integration`
  - `delivery`
  - `revenue`
  - `proof`

**Constraints to lock**
- `voice` musí zostať **bounded owner lane**, nie universal agent.
- Musí ostať kompatibilný s multiagent modelom.
- Nemá preberať live mutation authority bez approval.
- Nemá si brať cudzie lane ownership len preto, že “to súvisí s voice”.
- Má vedieť držať celý **voice business context**, ale s explicitnými hranicami.

**Proposed defaults**
Ak nepovieš inak, safe default pre `voice` lane je:

### `voice` owns
- voice offer implementation context
- agent design
- prompt architecture
- voice persona / voice selection
- conversation/workflow logic
- qualification / routing / handoff logic
- QA and test scenarios
- review prep
- launch-readiness assessment
- voice project inventory
- voice project standardization
- post-call / post-review iteration recommendations
- voice-specific proof extraction suggestions
- voice-business operating notes relevant to agent quality and deployment readiness

### `voice` supports but does not own
- integration execution
- CRM writes
- booking backend implementation
- client rollout governance
- commercial outreach
- pricing/proposal final ownership

### `voice` escalates to
- `integration` for implementation glue
- `delivery` for rollout / onboarding / deployment governance
- `revenue` for sales motion / pipeline / commercial follow-up
- `proof` for proof asset packaging beyond lane-local extraction

**Output contract**
Final `voice` lane should produce:
- updated operating contract
- explicit ownership / non-ownership map
- expanded routing model
- expanded inventory model
- voice-business artifact categories
- founder usage note for `voice`
- cleanup / polish updates to current `voice` files
- recommended first real tasks after expansion

**Acceptance bar**
Poviem, že `voice` je naozaj dokončený, keď:
- je jasné, čo všetko voice lane vlastní
- je jasné, čo už nie
- vieš mu dať “voice business” task bez nejasnosti
- nekoliduje s `integration`, `delivery`, `revenue`
- jeho README/routing/status/inventory už hovoria jedným jazykom
- vie slúžiť ako skutočný owner lane, nie len prompt helper

**Failure modes**
- voice sa stane príliš široký a zje iné lanes
- voice ostane príliš úzky a nebude niesť reálny segment
- vznikne overlap s integration/delivery/revenue
- doplníme veľa wording-u, ale nie reálnu operating clarity
- workspace sa ešte viac rozleje namiesto upratania

**Blocking questions**
Potrebujem len 3 presné odpovede:

1. Chceš, aby `voice` vlastnil aj **voice offer / segment strategy layer**, alebo len **execution layer voice projektov**?  
   - A = execution only  
   - B = execution + voice-business strategy/support

2. Chceš, aby `voice` vlastnil aj **post-launch / runtime performance review voice agentov**?  
   - áno / nie

3. Chceš, aby `voice` držal aj **vendor/platform layer** (ElevenLabs, Vapi, carrier choices relevant to voice), alebo to má zostať rozdelené s `integration`?  
   - A = voice drží platform decisions pre voice use  
   - B = len agent layer, platform glue patrí integration

### Planning readiness
**Ready for planning with defaults** — ale tieto 3 odpovede zmenia finálny shape.  

Odpíš mi len napríklad:
**1B, 2 áno, 3A**  
a ja potom dorobím plnú finalizáciu `voice` lane bez ďalšieho mlátenia slamy.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Thu 2026-03-26 00:16 GMT+1] ja potrebujem aby voice agent vedel obsluihovat cely voice agent busines v tom zmysle ze ja cez neho budem vytvarat voice agenta cize on musi vediet ako sa voice agent vytvara a ako sa vytvara s pouzitim skillu, chapes, ja chcem mat v ramci toho agenta vsetko co o n potrebuje na to aby vedel produkovat spolahlivo a kvalitne agentov podla potreby, teraz ej to polishing agenta pre maklera. 
nas plvy pilot klient caka na to ze mu poslem link aby mohol spravit review agentovy, ktory pre neho tvorime. 
cize, ked poviem ze jarvis, jakub potrebuje skontrolovat agenta, tak musime byt schopny spravit audit, potom navrh vylepseni, implementacia mojich navrhov, impleentacia, testovanie, editacia, workflows, tools, knowladge, system prompt - toto vsetko musi vedeit agento robit, proste full konzola na elevenlab. 
kazdy element voice agenta ma nastarosti tento agent, a ja by som chcel aby tento agent mal vsetky potreben informacie o tom ako sa tvoria agenti a ako my tvorime agenta. 
teraz konkretne pre maklera. 
chapes o com rozpravam?
assistant: [[reply_to_current]] Áno. Chápem to presne.  
A hlavne: **`voice` nemá byť “voice business strategy agent”**. Má byť **full-stack operator pre tvorbu a správu voice agentov** — tvoja **interná konzola na ElevenLabs / voice-agent production**.

Verdikt:  
`voice` má vlastniť **celý production lifecycle voice agenta**.

Nie sales lane.  
Nie generic strategy lane.  
Ale **agent factory + agent operations lane**.

# Ako to správne zarámcovať

## Čo `voice` reálne je
`voice` = **Voice Agent Production Operator**

Jeho job:
keď mu cez Jarvisa zadáš čokoľvek okolo voice agenta, má vedieť:
- auditovať
- navrhnúť zlepšenia
- prepísať prompt
- upraviť flow
- navrhnúť tools
- skontrolovať workflows
- pracovať s knowledge
- pripraviť review
- zapracovať feedback
- pripraviť testovanie
- udržiavať poriadok medzi verziami
- vedieť, ako **my** agentov tvoríme

Čiže áno:
**full konzola na ElevenLabs / voice-agent production**  
to je správny frame.

# Preklad tvojho intentu do scope

## `voice` musí vlastniť tieto vrstvy

### 1. Agent architecture
- use case definition
- V1 scope
- caller scenarios
- desired outcomes
- constraints / forbidden actions

### 2. System prompt layer
- canonical prompt drafting
- prompt patching
- prompt audits
- behavior tuning
- conversation design logic

### 3. Workflow layer
- call flow structure
- routing logic
- qualification logic
- next-step logic
- fallback logic
- handoff logic

### 4. Tools layer
- tool need analysis
- tool map návrh
- tool contract expectations
- tool usage rules in prompt
- identification of missing tools

### 5. Knowledge layer
- what context/knowledge the agent needs
- what should be embedded or supplied
- what is missing for reliable behavior
- knowledge hygiene

### 6. Review / audit layer
- internal review
- Jakub review prep
- founder review prep
- gap identification
- keeper-vs-duplicate logic
- quality scoring

### 7. QA / testing layer
- QA scenarios
- edge cases
- ambiguity tests
- guardrail tests
- launch-readiness checks
- post-change verification recommendations

### 8. Iteration layer
- apply founder feedback
- apply collaborator feedback
- compare versions
- recommend patch set
- track what changed and why

### 9. Portfolio / production hygiene
- inventory of agents
- duplicate cleanup recommendations
- family grouping
- keeper recommendation
- naming/order discipline
- production readiness overview

### 10. Build method memory
A toto je kritické:
`voice` musí niesť aj:
- **ako my agentov tvoríme**
- aký je náš quality bar
- aký je náš review flow
- aký je náš V1 discipline
- aké sú naše defaults
- aký je náš acceptance bar

Čiže nielen “agent work”, ale aj:
**our agent-building method**

To je presne to, čo si povedal.

# Čo `voice` nemá vlastniť
Aby sa nerozlial:

Nemá defaultne vlastniť:
- CRM implementation
- n8n implementation
- SIP/carrier glue
- outreach
- proposal/sales closing
- onboarding governance
- live destructive mutation without approval

Ale má vedieť povedať:
- čo chýba v integration
- čo treba od delivery
- čo treba na review
- čo blokuje launch

# Najpresnejší identity statement
Takto by som ho prepísal:

> `voice` is Adam’s internal production operator for voice agents.  
> It owns the full lifecycle of designing, auditing, improving, testing, organizing, and preparing voice agents for review and deployment, especially in ElevenLabs-based workflows.  
> It also preserves the internal Xvadur method for how voice agents are built, reviewed, and improved.

To je ono.

# Čo sa teraz mení oproti dnešnému setupu
Doteraz bol `voice` postavený hlavne ako:
- ElevenLabs lane
- prompt/workflow/review/QA owner

Po tvojom spresnení ho treba posunúť na:
- **full voice-agent production operator**
- with **method memory**
- with **complete build surface ownership**
- with **agent console mentality**

To je upgrade, nie pivot.

# Konkrétne pre Makléra / Jakuba
Tvoj aktuálny real use case to krásne potvrdzuje.

`voice` musí vedieť:
- pozrieť current maklér agent
- spraviť audit
- pripraviť Jakub review
- navrhnúť zmeny
- zapracovať tvoje pripomienky
- upraviť prompt
- upraviť tools/workflow/knowledge
- pripraviť testing
- vydať review-ready alebo deploy-ready verdict

Presne toto je jeho job.

# Verdikt
**Áno, úplne chápem, o čom rozprávaš.**  
A áno, `voice` má byť nastavený ako:
**full-stack voice agent production operator pre ElevenLabs / voice-agent builds**,  
nie len ako prompt helper alebo audit lane.

# Ďalší správny krok
Tu už netreba ďalšie filozofovanie.  
Treba spraviť 2 veci:

1. **rozšíriť contract `voice` agenta** na full production operator scope  
2. **nahádzať mu do workspace všetky build-method references a operating truth**, ktoré potrebuje pre spoľahlivú tvorbu agentov

To znamená update:
- README
- routing
- inventory model
- templates
- status
- memory
- možno aj dedicated `method/` alebo `references/` note v jeho workspace

Ak chceš, spravím to rovno teraz ako ďalší batch:
**prekopem `voice` z current ElevenLabs owner lane na full Voice Agent Production Operator.**
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Thu 2026-03-26 00:18 GMT+1] dalsia vec, zda sa mi ze to extremne komplikujeme, cez vsetky tie handoff markdown srandy, jakoze chapes, openclaw ma nejaky designe, nejaku dokumentaciu ktoru potrebujeme vzdy dodrziavat, aby sme zarucili ze system bude fungovat. 
teraz co som videl dokumenty vo vnutry napr voice, su v hroznom stave, nie su uplne, a maly by byt rozvinutejsie, a hlavne by tam mali byt iba tie dokuemnty ktore tam musia byt, ostatne docs musia byt vo folderoch
assistant: [[reply_to_current]] Áno. **Máš pravdu. Prekomplikovali sme to.**  
A to je teraz hlavný problém — nie chýbajúci ďalší markdown, ale **zlý shape workspaceu**.

Verdikt:  
treba spraviť **workspace cleanup + contract hardening**, nie ďalej vrstviť dokumenty.

## Čo je zle
Momentálne sme spravili správnu vec na úrovni architektúry, ale príliš ťažkopádne na úrovni súborov:
- veľa ad-hoc docs
- nie všetko má správnu váhu
- lane rooty sa začínajú plniť bordelom
- niektoré dokumenty sú slabé
- niektoré sú duplicity
- niektoré patria do podfolderov, nie do rootu agenta

A to je presne ten typ driftu, ktorý neskôr zlomí systém.

## Správny frame teraz
Nepotrebujeme ďalší “vymýšľací” design.  
Potrebujeme:
1. **vrátiť sa k OpenClaw shape**
2. **nechať v root agenta len minimum required files**
3. **všetko ostatné presunúť do priečinkov**
4. **zosilniť tie core docs, ktoré musia existovať**
5. **vyhodiť / zlúčiť zbytočnosti**

## Môj odporúčaný shape pre každý agent
V root by mali zostať len tieto core súbory:

- `AGENTS.md`
- `README.md`
- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `TOOLS.md` *(ak je relevantné)*
- `status.md`
- `queue.md`

A potom len priečinky typu:
- `daily/`
- `templates/`
- `inventory/`
- prípadne `references/`
- prípadne `runs/` / `config/` ak ten lane fakt potrebuje

To je čisté.

## Čo určite nechcem ďalej robiť
Nechcem pokračovať v:
- random new docs v root-e
- další “manuals” v každom agente
- duplication medzi README / routing / status / queue
- packet theater bez reálneho runtime prínosu

## Čo treba spraviť teraz pre `voice`
Presne 3 veci:

### 1. Zadefinovať minimalistický agent root
Čo musí byť v `agents/voice/` root  
a čo musí ísť do subfolderov

### 2. Prepísať core docs poriadne
Najmä:
- `README.md`
- `AGENTS.md`
- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `status.md`
- `queue.md`
- `MEMORY.md`

Tieto majú byť:
- silnejšie
- čistejšie
- menej šumu
- lepšie aligned s OpenClaw runtime

### 3. Urobiť presun / cleanup
- nech root ostane čistý
- templates do `templates/`
- inventory do `inventory/`
- context notes do `daily/` alebo `references/`
- staré slabé docs preč alebo zlúčiť

## Dôležitá vec
To, čo si práve povedal, mení poradie práce.

Predtým:
- configure voice
- potom polish

Teraz:
- **voice cleanup + contract hardening je súčasť konfigurácie**
- až potom ďalšie použitie

A to je správne.

## Môj verdict
**Áno, stop ďalšiemu vrstveniu markdownov.**  
Teraz treba:
- zredukovať
- upratať
- zosilniť core files
- vrátiť shape do čistého OpenClaw-compatible stavu

## Najlepší ďalší krok
Ja by som teraz spravil presne toto:

### Phase 1 — voice workspace audit
- čo tam je
- čo musí zostať v root
- čo treba presunúť
- čo je slabé
- čo je duplicita
- čo chýba

### Phase 2 — voice root hardening
- prepísať core docs do silnej podoby
- zredukovať root noise
- usporiadať supporting files do folders

### Phase 3 — až potom ostrý use
- ElevenLabs cleanup audit
- review support
- build operations

To je správne poradie.

Ak chceš, idem teraz presne týmto smerom:
**urobím audit `agents/voice/`, navrhnem clean target shape a potom ho rovno upracem.**
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Thu 2026-03-26 00:19 GMT+1] musim euvazovat systemovo, proste kazdy agent ma svoj workspace ktory mozeme nadizajnovat tak zacine odtialto, co aky foldertree potrebuje voice agent? 
co vsetko potrebuje vedeit, aky ma mat kontext voice agent, co potrebuje vedeit na to aby robil spolahlivo plnohodnoteho voice agenta?
assistant: [[reply_to_current]] Áno. Toto je správna otázka.  
Nie „aké ďalšie markdowny dopíšeme“, ale:

**aký workspace tree potrebuje `voice`, aký kontext má niesť, a čo musí vedieť, aby spoľahlivo vyrábal plnohodnotných voice agentov.**

To je systémové myslenie. Správne.

# Verdikt
`voice` potrebuje byť navrhnutý ako **production workspace pre voice-agent factory**, nie ako poznámkový folder.

Teda musí mať:
1. **core runtime root**
2. **method / operating knowledge**
3. **active project surfaces**
4. **templates**
5. **inventory**
6. **review / QA artifacts**
7. **durable memory**
8. **minimal root noise**

---

# 1. Čo musí `voice` vedieť, aby robil spoľahlivo voice agentov

Toto je jadro.

## A. Build method
Musí vedieť:
- ako **my** navrhujeme voice agentov
- aký je náš **build sequence**
- čo je V1 scope discipline
- čo musí mať každý agent
- čo je acceptance bar
- čo je review-ready vs deploy-ready
- čo je safe fallback
- ako vyzerá kvalitný output

Inými slovami:
**our factory method**

---

## B. Segment / use-case modeling
Musí vedieť:
- aký biznis/use case agent rieši
- aký je caller typ
- aké sú hlavné scenáre
- aké sú cieľové outcomes
- čo je in-scope / out-of-scope
- aké sú constraints a guardrails

Bez toho nevie robiť spoľahlivé agent design rozhodnutia.

---

## C. Voice agent components
Musí vedieť, z čoho sa agent skladá:

- system prompt
- first message
- workflow / routing
- tools
- knowledge
- handoff logic
- QA/test layer
- review layer
- readiness layer
- version/iteration layer

A musí vedieť, ako tieto komponenty spolu súvisia.

---

## D. Platform knowledge
Musí vedieť:
- ako funguje ElevenLabs agent layer
- čo sú limity a možnosti platformy
- čo je voice-specific vs backend-specific
- čo patrí do promptu
- čo patrí do tools
- čo patrí do workflow contractu
- čo patrí do external implementation

Toto je praktická produkčná znalosť, nie len všeobecný voice theory.

---

## E. Quality control
Musí vedieť:
- ako robiť audit
- ako robiť review prep
- ako robiť QA scenáre
- ako vyhodnotiť, či agent pôsobí silno/slabo
- ako pomenovať gaps
- ako navrhnúť patch set

---

## F. Portfolio hygiene
Musí vedieť:
- čo už existuje
- ktoré agenty sú duplicitné
- čo je keeper
- čo je stale
- čo je reusable pattern
- čo je len experiment

Toto je kritické, ak nechceš chaos v ElevenLabs.

---

# 2. Aký folder tree potrebuje `voice`

Tu je môj odporúčaný **clean target shape**:

```text
agents/voice/
├── AGENTS.md
├── README.md
├── IDENTITY.md
├── SOUL.md
├── USER.md
├── MEMORY.md
├── HEARTBEAT.md
├── TOOLS.md
├── status.md
├── queue.md
│
├── method/
│   ├── build-system.md
│   ├── prompt-standard.md
│   ├── qa-standard.md
│   ├── review-standard.md
│   ├── readiness-standard.md
│   └── platform-boundaries.md
│
├── inventory/
│   ├── agents.md
│   ├── projects.md
│   ├── voices.md
│   ├── tools.md
│   └── knowledge-assets.md
│
├── templates/
│   ├── delegation-packet.md
│   ├── review-template.md
│   ├── audit-template.md
│   ├── prompt-patch-template.md
│   ├── agent-spec-template.md
│   ├── qa-pack-template.md
│   └── cleanup-template.md
│
├── references/
│   ├── elevenlabs/
│   ├── examples/
│   ├── baselines/
│   └── segment-playbooks/
│
├── projects/
│   ├── marek/
│   │   ├── brief.md
│   │   ├── current-state.md
│   │   ├── prompt.md
│   │   ├── tools.md
│   │   ├── workflow.md
│   │   ├── knowledge.md
│   │   ├── review.md
│   │   ├── qa.md
│   │   └── changelog.md
│   └── ...
│
├── daily/
│   └── YYYY-MM-DD-*.md
│
└── archive/
    └── ...
```

Toto je už usable production tree.

---

# 3. Čo patrí do root a čo nie

## Root = len runtime core
V root majú byť len:
- identity
- role
- rules
- current status
- queue
- memory

To je všetko.

## Mimo root
### `method/`
Ako agenti tvoríme

### `inventory/`
Čo máme a v akom stave

### `templates/`
Ako opakovane pracujeme

### `references/`
Externé alebo baseline referencie

### `projects/`
Každý reálny voice projekt oddelene

### `daily/`
Priebežné snapshoty, nie canonical truth

---

# 4. Čo presne má byť v `method/`

Toto je možno najdôležitejší priečinok.

## `method/build-system.md`
- canonical build sequence
- od intake po review/deploy
- čo sa robí v akom poradí

## `method/prompt-standard.md`
- ako skladáme system prompts
- required sections
- style law
- what good looks like

## `method/qa-standard.md`
- minimálny QA pack
- edge cases
- regression mindset
- pass/fail rules

## `method/review-standard.md`
- ako robíme interný review
- ako robíme Jakub review
- čo je review-ready

## `method/readiness-standard.md`
- draft-ready vs review-ready vs deploy-ready
- aké dôkazy treba na každú úroveň

## `method/platform-boundaries.md`
- čo patrí `voice`
- čo patrí `integration`
- čo patrí `delivery`
- čo patrí `revenue`

Toto zabráni chaosu.

---

# 5. Čo presne má byť v `inventory/`

## `inventory/agents.md`
Zoznam agentov:
- názov
- typ
- platforma
- stage
- owner
- current keeper?
- duplicate?
- last reviewed
- next move

## `inventory/projects.md`
Zoznam projektov:
- klient/use case
- current agent
- review state
- QA state
- deployment state

## `inventory/voices.md`
Používané voices:
- voice id
- provider
- use
- quality notes
- current preference

## `inventory/tools.md`
Tool surfaces:
- tool name
- purpose
- where used
- current status
- missing docs?

## `inventory/knowledge-assets.md`
Knowledge/context assets:
- docs
- briefs
- KB inputs
- structured context
- what is stale / missing

---

# 6. Čo presne má byť v `business/voice/clients/marek/`

Keďže Maklér je teraz aktívny, mal by mať vlastný projektový priečinok.  
To je presne to, čo teraz chýba.

## `business/voice/clients/marek/brief.md`
- čo agent rieši
- pre koho
- V1 scope
- target outcomes

## `business/voice/clients/marek/current-state.md`
- čo aktuálne existuje
- čo je live/staged
- čo je blocker

## `business/voice/clients/marek/prompt.md`
- current system prompt
- maybe current first message
- patch notes

## `business/voice/clients/marek/tools.md`
- attached tools
- tool purpose
- expected behavior
- missing tools

## `business/voice/clients/marek/workflow.md`
- routing
- lane logic
- next-step engine
- handoff logic

## `business/voice/clients/marek/knowledge.md`
- aké knowledge inputs agent má / potrebuje

## `business/voice/clients/marek/review.md`
- review findings
- Jakub review prep
- founder comments

## `business/voice/clients/marek/qa.md`
- QA pack
- tested / not tested
- failures / next tests

## `business/voice/clients/marek/changelog.md`
- čo sa zmenilo a prečo

Toto je oveľa lepšie než rozhodené artefakty.

---

# 7. Minimal context, ktorý musí `voice` vždy mať
Ak má byť spoľahlivý, musí mať vždy dostupné:

- current build method
- prompt standard
- QA standard
- active project inventory
- active project state
- review criteria
- readiness criteria
- platform boundary rules
- reusable templates
- current baseline examples

Bez týchto vrstiev bude vždy len improvizovať.

---

# 8. Čo by som vyradil alebo obmedzil
Aby sa to nerozpadlo:

- žiadne random docs v root
- žiadne nekonečné packet docs, ak nemajú reuse
- daily notes nie sú canonical truth
- references nemajú žiť v root
- jeden projekt = jeden project folder
- inventory sú durable tables/lists, nie denné poznámky
- status/queue len krátke executive surfaces

---

# 9. Najlepší operating model pre `voice`
Keď mu povieš:
- auditni agenta
- priprav review
- oprav prompt
- navrhni tools
- dotiahni workflow
- sprav QA
- vyber keeper verziu

mal by robiť toto:

1. nájde projekt / založí projekt surface
2. načíta method standards
3. pozrie inventory
4. spraví task
5. update-ne project files
6. update-ne status/queue len ak sa mení lane truth
7. vráti Jarvisovi founder summary

To je čistý operating loop.

---

# 10. Môj verdict
**`voice` nepotrebuje viac náhodných docs. Potrebuje správny filesystem design.**  
A ten design je:

- **root = runtime core**
- **method = how we build**
- **inventory = what exists**
- **templates = reusable execution shapes**
- **projects = actual client/use-case work**
- **daily = continuity only**
- **references = supporting material**

To je systémový základ.

# Najlepší ďalší krok
Ak chceš, ja teraz nespravím len opis.  
Ja spravím rovno:

1. **target tree pre `agents/voice/`**
2. **presun/cleanup existujúcich vecí**
3. **vytvorenie `method/`, `business/voice/clients/marek/`, `inventory/`, `templates/` v správnom tvare**
4. **prepísanie core docs tak, aby sedeli tomuto modelu**

To je podľa mňa presne to, čo teraz treba.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Thu 2026-03-26 00:23 GMT+1] vyborne, podme to prosim spravit postupne. sprav check list a podme na to
assistant: [[reply_to_current]] Jasné. Ideme systematicky, nie hurá štýlom.

# Checklist — prestavba `voice` workspace na plnohodnotný voice-agent production lane

## Phase 1 — audit a target shape
- [ ] spísať **target folder tree** pre `agents/voice/`
- [ ] určiť, čo musí zostať v root
- [ ] určiť, čo sa má presunúť do `method/`
- [ ] určiť, čo sa má presunúť do `inventory/`
- [ ] určiť, čo sa má presunúť do `templates/`
- [ ] určiť, čo sa má presunúť do `projects/`
- [ ] určiť, čo ostáva len v `daily/`
- [ ] označiť duplicity / slabé docs / dočasné docs

## Phase 2 — core runtime hardening
- [ ] prepísať `README.md`
- [ ] prepísať `AGENTS.md`
- [ ] prepísať `IDENTITY.md`
- [ ] prepísať `SOUL.md`
- [ ] prepísať `USER.md`
- [ ] prepísať `MEMORY.md`
- [ ] upratať `status.md`
- [ ] upratať `queue.md`
- [ ] skontrolovať `TOOLS.md`

## Phase 3 — method layer
- [ ] vytvoriť `method/build-system.md`
- [ ] vytvoriť `method/prompt-standard.md`
- [ ] vytvoriť `method/qa-standard.md`
- [ ] vytvoriť `method/review-standard.md`
- [ ] vytvoriť `method/readiness-standard.md`
- [ ] vytvoriť `method/platform-boundaries.md`

## Phase 4 — inventory layer
- [ ] vytvoriť / upratať `inventory/agents.md`
- [ ] vytvoriť / upratať `inventory/projects.md`
- [ ] vytvoriť / upratať `inventory/voices.md`
- [ ] vytvoriť / upratať `inventory/tools.md`
- [ ] vytvoriť / upratať `inventory/knowledge-assets.md`

## Phase 5 — templates layer
- [ ] zjednotiť `templates/delegation-packet.md`
- [ ] zjednotiť `templates/review-template.md`
- [ ] vytvoriť `templates/audit-template.md`
- [ ] upratať `templates/prompt-patch-template.md`
- [ ] vytvoriť `templates/agent-spec-template.md`
- [ ] vytvoriť `templates/qa-pack-template.md`
- [ ] vytvoriť `templates/cleanup-template.md`

## Phase 6 — active project layer
- [ ] vytvoriť `business/voice/clients/marek/`
- [ ] založiť `business/voice/clients/marek/brief.md`
- [ ] založiť `business/voice/clients/marek/current-state.md`
- [ ] založiť `business/voice/clients/marek/prompt.md`
- [ ] založiť `business/voice/clients/marek/tools.md`
- [ ] založiť `business/voice/clients/marek/workflow.md`
- [ ] založiť `business/voice/clients/marek/knowledge.md`
- [ ] založiť `business/voice/clients/marek/review.md`
- [ ] založiť `business/voice/clients/marek/qa.md`
- [ ] založiť `business/voice/clients/marek/changelog.md`

## Phase 7 — cleanup
- [ ] presunúť supporting docs z root do správnych folderov
- [ ] zmazať / zlúčiť duplicity
- [ ] nechať v root len runtime core
- [ ] skontrolovať, že `daily/` nehrá rolu canonical truth
- [ ] skontrolovať, že `inventory/` a `projects/` nesú durable truth

## Phase 8 — validation
- [ ] skontrolovať, že `voice` vie niesť celý voice-agent production lifecycle
- [ ] skontrolovať, že hranice voči `integration`, `delivery`, `revenue` sú jasné
- [ ] skontrolovať, že workspace je čitateľný aj bez vysvetľovania
- [ ] pripraviť prvý ostrý use case cez nový shape

# Odporúčané poradie práce
Ja by som to robil takto:
1. **Phase 1**
2. **Phase 2**
3. **Phase 3**
4. **Phase 4**
5. **Phase 5**
6. **Phase 6**
7. **Phase 7**
8. **Phase 8**

# Môj návrh na teraz
Začnime hneď správne:
**spravím Phase 1 — target folder tree + audit čo patrí kam**  
a potom to budeme fyzicky prestavovať.

Ak chceš, idem rovno na Phase 1.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Thu 2026-03-26 00:23 GMT+1] zapis to do systemu, pojdeme z novej konverzacie
assistant: Zapíšem checklist do workspace, aby sme na to nadviazali v novej konverzácii.
assistant: [[reply_to_current]] Zapísané.

Nadviažeme na toto:
- `docs/plans/2026-03-26-voice-workspace-rebuild-checklist.md`

V novej konverzácii môžeme ísť rovno na **Phase 1 — target folder tree pre `agents/voice/`**.
