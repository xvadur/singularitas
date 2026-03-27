# Session: 2026-03-24 22:24:59 UTC

- **Session Key**: agent:integration:telegram:direct:1594354152
- **Session ID**: 619bb552-f69f-4fd1-8fc2-6796b1e67ed0
- **Source**: telegram

## Conversation Summary

assistant: [[reply_to_current]] Áno — **prakticky nám to prinieslo natívny skill lifecycle v OpenClawe**, nie len externý `clawhub` workaround.

**Čo sme tým získali:**
- **native search/install/update skillov**  
  - `openclaw skills search`
  - `openclaw skills install`
  - `openclaw skills update --all`
- **skills sa inštalujú rovno do workspace** a OpenClaw ich hneď berie do úvahy
- **shared vs per-agent skills model**
  - `~/.openclaw/skills` = shared pre všetkých agentov
  - `<workspace>/skills` = lokálne pre konkrétny agent/workspace
- **precedence/override systém**
  - workspace skill prepíše shared skill
  - shared prepíše bundled
- **pluginy môžu shipovať skills**
- jednoduchší základ pre **skill curation, versioning a rollout**

**Čo to neprinieslo automaticky:**
- nie je to ešte “CRM-style priradenie skillu klientovi” ako prvotriedny objekt typu *client → skills*
- OpenClaw rozmýšľa skôr cez:
  - **agent/workspace**
  - **shared skills**
  - **workspace-specific skills**

**Či vieme spraviť skill overhaul?**
**Áno, úplne.**  
Vedel by som to spraviť takto:

1. **audit current skills**
   - bundled
   - shared `~/.openclaw/skills`
   - workspace `skills/`

2. **rozdeliť ich na 3 vrstvy**
   - **core/shared pack** — veci pre všetkých
   - **lane pack** — revenue / voice / integration / delivery
   - **client-specific pack** — len pre konkrétneho klienta

3. **priradenie klientom riešiť architektúrou**
   - buď **1 klient = 1 workspace / agent**
   - alebo **shared base + client override skills** v konkrétnom workspace

4. **čo chýba, dopísať / prerobiť**
   - pomocou custom skillov
   - alebo stiahnuť z ClawHub a upraviť

**Krátka pravda:**  
- **áno, skill overhaul vieme spraviť**
- **áno, vieme “priradiť skilly klientom”**
- ale technicky to bude skôr cez **workspace/agent-per-client model**, nie cez natívne tlačidlo “assign skills to client”

Ak chceš, ďalší krok môžem spraviť hneď:
1. **audit existujúcich skillov**, alebo  
2. navrhnúť **skill architecture pre klientov**.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1665",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Mon 2026-03-23 20:05 GMT+1"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Adam Xvadur (1594354152)",
  "id": "1594354152",
  "name": "Adam Xvadur",
  "username": "xvadur"
}
```

dobre tak sa pozrime na clawhub co by sme mohli získať pre každý agent lane, podľa toho co ktoré skilly chýbajú. 
skilly zatiaľ nejsu koherentne priradené k agentom
assistant: Pozriem current agent lanes, aké skills už lokálne máte, a potom urobím shortlist z ClawHubu podľa medzier.
assistant: Spravím rýchly ClawHub scouting po lane-och a vedľa toho zoberiem do úvahy, čo už v skills máte lokálne.
assistant: [[reply_to_current]] Áno — a hlavný insight je vlastne ešte dôležitejší než samotný ClawHub:

**momentálne nemáte skills koherentne napojené na lane agentov.**

### Čo som zistil
- máš **veľa custom skillov** v:
  - `/Users/_xvadur/singularitas/skills/...`
- ale nemáš:
  - **žiadne shared skills** v `~/.openclaw/skills`
  - **žiadne lane-local skills** v `agents/<lane>/skills`
- lane agenti majú workspace typu:
  - `.../studio/founder-ops/revenue`
  - `.../studio/voice-factory`
  - `.../studio/integration`
  - atď.

To znamená, že tvoje root skills v `/singularitas/skills` **nie sú prirodzene coherentne dostupné všetkým lane agentom**. Pravdepodobne sú najviac “po ruke” main agentovi, ale nie je to čistý shared model.

## Čo by som z toho vyvodil
**Prvý problém nie je nedostatok skillov.**  
Prvý problém je **skill topology**:

1. **shared base pack** chýba  
2. **lane-specific packy** chýbajú  
3. až potom dáva zmysel riešiť **ClawHub imports**

---

# Čo už máte lokálne
V root `skills/` už máš dobrý základ, napríklad:
- `crm`
- `n8n`
- `voice-factory`
- `github`
- `google-workspace`
- `cloudflare-toolkit`
- `lead-researcher`
- `lead-enrichment`
- `business-development`
- `content-strategy`
- `youtube-transcript`
- `linear`
- `supabase`
- `elevenlabs`

Čiže problém nie je „nemáme nič“.  
Skôr: **nemáme to roztriedené podľa lane-ov a shared/common vrstvy.**

---

# Čo by sme vedeli získať z ClawHub podľa lane-u

## research
**Dáva zmysel doplniť:**
- `market-research`
- `reddit-research`
- `academic-deep-research`
- `parallel-ai-research`

**Prečo:** research lane má mať silný external intel pack, a toto ti rozšíri sourcing mimo current local briefs.

## growth
**Kandidáti:**
- `linkedin`
- `linkedin-cli`
- `linkedin-writer`
- `seo`
- `seo-competitor-analysis`
- `airtable` *(ak niektorý pipeline/use case ide cez Airtable)*

**Prečo:** growth dnes potrebuje outreach + positioning + site refresh + lead movement. LinkedIn/SEO skills sú tu celkom prirodzený gap.

## revenue
**Kandidáti:**
- `close-crm`
- `hubspot`
- `airtable`
- `calendar` / `gcalcli-calendar` *(ak chceš tvrdší scheduling flow)*
- `linkedin`

**Prečo:** revenue lane je commercial motion. Najväčšia medzera je často **CRM-specific skill podľa stacku klienta**.

## voice
**Kandidáti:**
- `vapi-calls`
- `vapi`
- `openrouter-transcribe`
- `deepgram-transcribe`
- `super-transcribe`

**Prečo:** lokálne máš `voice-factory` a `elevenlabs`, ale ClawHub ti vie doplniť **Vapi ops + call transcription layer**.

## integration
**Kandidáti:**
- `email-webhook`
- `webhook-send`
- `hubspot`
- `airtable`
- `close-crm`
- prípadne CRM/vendor-specific skills podľa klienta

**Prečo:** integration lane potrebuje explicitné konektory a webhook surfaces. Tu ClawHub vie byť reálne užitočný.

## delivery
**Kandidáti:**
- `calendar-manager`
- `jira`
- `airtable`
- `notion` varianty len ak by bundled nestačil

**Prečo:** delivery je onboarding + rollout + validation. Tu by som išiel skôr po **execution system skills**, nie po generických kreatívnych skilloch.

## proof
**Kandidáti:**
- `transcribe`
- `openrouter-transcribe`
- `podcast-transcribe`
- `deepgram-transcribe`

**Prečo:** proof lane potrebuje ťažiť dôkazy z callov, meetingov, delivery výstupov. Transcription/export layer tu chýba viac než “writing” layer.

## web
**Kandidáti:**
- `wordpress`
- `wordpress-pro`
- `wordpress-publishing-skill-for-claude`
- `seo`
- `website-seo`
- `seo-content-engine`

**Prečo:** web lane má najväčší zmysel pre **CMS + SEO + publishing** skills.

## personal-web
**Kandidáti:**
- podobne ako web:
  - `wordpress`
  - `seo`
  - `wordpress-optimizer`

**Prečo:** osobný web stewardship je v zásade mini web lane.

## personal-ops
Tu by som bol opatrný:
- zmysluplné veci typu reminders/calendar/notion už máš skôr **bundled/native**:
  - `apple-reminders`
  - `things-mac`
  - `gog`
  - `notion`
  - `obsidian`

**Verdikt:** pre personal-ops by som skôr upratal **existujúce bundled skills**, než ťahal veľa z ClawHub.

## ops
**Kandidáti:**
- `jira`
- `system-resource-monitor`
- `security-monitor`
- `openclaw-backup`
- `audit`

**Prečo:** ops lane vie benefitovať z monitoringu, backupov, auditov a execution tooling.

## janitor
**Kandidáti:**
- `audit`
- `openclaw-backup`
- `security-monitor`
- `system-resource-monitor`

**Prečo:** janitor lane je hygiene/drift/audit. Tu sú audit/backup/monitor skills vhodnejšie než business skills.

## build
Pre build lane by som z ClawHub bral menej:
- prípadne `jira`
- prípadne klientsky stack-specific plugin/skill
- inak build je skôr o repo/tooling a nie o marketplace skills

**Verdikt:** build nepotrebuje veľký ClawHub overhaul ako prvý.

---

# Môj reálny záver

## Najväčší win nie je “stiahnuť 20 skillov”
Najväčší win je:

### 1. upratať skill architektúru
Navrhujem:
- **`~/.openclaw/skills`** = shared common pack
- **`agents/<lane>/skills`** = lane-specific pack
- root `/singularitas/skills` buď:
  - presunúť do shared,
  - alebo pridať cez `skills.load.extraDirs`

### 2. až potom doplniť ClawHub len tam, kde je reálny gap
Moja priorita by bola:

**Tier 1**
- voice → `vapi-calls`, `openrouter-transcribe` alebo `deepgram-transcribe`
- web/personal-web → `wordpress`, `seo`
- revenue/integration → `hubspot` / `close-crm` / `airtable` podľa reality stackov
- research → `market-research`, `reddit-research`

**Tier 2**
- ops/janitor → `audit`, `openclaw-backup`, `system-resource-monitor`
- delivery → `jira` / `calendar-manager`

**Tier 3**
- personal-ops → skôr využiť bundled, nie ClawHub shopping

---

# Čo by som spravil hneď teraz
Ak chceš, viem spraviť toto ako ďalší krok:

**A. Skill assignment matrix**
- lane × current skills
- lane × missing skills
- lane × ClawHub candidates
- priority: now / later / skip

alebo

**B. Concrete overhaul plan**
- ktoré skills presunúť do `~/.openclaw/skills`
- ktoré vytvoriť do `agents/<lane>/skills`
- ktoré 5–10 skillov má zmysel reálne stiahnuť z ClawHub ako prvú vlnu

Za mňa by som išiel rovno na **A → potom B**.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1672",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Tue 2026-03-24 16:21 GMT+1"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Adam Xvadur (1594354152)",
  "id": "1594354152",
  "name": "Adam Xvadur",
  "username": "xvadur"
}
```

[Audio]
User text:
[Telegram Adam Xvadur (@xvadur) id:1594354152 +20h Tue 2026-03-24 16:21 GMT+1] <media:audio>
Transcript:
No hej, však teraz je to tak, že máme plnú piču skills z priečinku, ktoré ja invokujem, ale nie sú priradené k agentom a agenti sú iba napísaní v markdowne, tuším, že v configu sú pripravení, ale nemajú žiadnu akciu alebo teda nemajú žiadny ritmus. A kebyže, teda tak si to predstavujem, že keby sme tým agentom pri-priradili (odkrášľaní) skilly a prácu k tomu, čo už majú teraz, tak by sme z toho mohli spraviť operačný rámec. Mohli by sme ich zapnúť, dať im cron joby alebo heartbeaty a mohli by sme to celé nejak spojiť. Konečne.
assistant: [[reply_to_current]] [[tts:plain]][[tts:text]]Presne. Dnes máte skilly skôr ako voľný toolbox pre teba, nie ako operačný systém pre agentov. Keď im priradíme shared a lane-specific skilly, rytmus cez heartbeat a pár cron jobov, z markdown agentov sa stanú reálne pracovné role. Ak chceš, ďalší krok je spraviť assignment matrix a z toho rovno návrh prvého zapnutia pre revenue, voice, integration a delivery.[[/tts:text]]

Presne tak — **dnes máte identity agentov, ale nie ich operačný loop**.

Najpresnejšie by som to pomenoval takto:

- **skills existujú**
- **agenti existujú**
- **config ich pozná**
- ale **skills nie sú ownershipovo priradené agentom**
- a **agenti nemajú pravidelný rytmus, trigger ani zodpovednosť**

Čiže áno: teraz je to skôr **ručný toolbox**, nie **živý multi-agent operating system**.

### Čo z toho vieme spraviť
Z toho sa dá spraviť úplne legit **operačný rámec**:

1. **shared skill layer**
   - veci, ktoré majú mať všetci alebo viac lane-ov

2. **lane-specific skill packs**
   - revenue, voice, integration, delivery, research, web…

3. **agent work contract**
   - čo agent sleduje
   - čo robí sám
   - čo len eskaluje
   - čo je jeho heartbeat output

4. **heartbeat cadence**
   - natívne v OpenClawe
   - na stav, riziká, next move, blockers

5. **cron jobs**
   - na konkrétne opakované úlohy
   - sync, checks, reports, refreshes, queue scans

6. **handoff graph medzi lane-mi**
   - napr. revenue → voice → integration → delivery → proof

### Inými slovami
To, čo ti chýba, nie je ďalších 50 skillov.  
Chýba ti **mapa: skill → agent → rytmus → trigger → output**.

### Môj návrh poradia
Najprv by som nerobil všetko naraz, ale:

- **fáza 1:** skill assignment matrix
- **fáza 2:** shared vs lane-local skills
- **fáza 3:** heartbeat contract pre každý lane
- **fáza 4:** 1–2 cron joby na lane
- **fáza 5:** pilot na **revenue + voice + integration + delivery**

To je presne to kvarteto, kde z toho môže vzniknúť prvý reálny operating loop.

Ak chceš, ja teraz môžem urobiť hneď **konkrétny návrh operačného rámca**:
- ktorý agent má mať ktoré skilly,
- aký heartbeat,
- aký cron,
- a aký handoff na ďalší lane.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1676",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Tue 2026-03-24 16:26 GMT+1"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Adam Xvadur (1594354152)",
  "id": "1594354152",
  "name": "Adam Xvadur",
  "username": "xvadur"
}
```

yes, napis k tomu checklist
assistant: [[reply_to_current]] Jasné — tu je **checklist na prechod z “máme skills a agent markdowny” na reálny operačný rámec**.

## 0. Cieľ
- [ ] zmeniť agentov z pasívnych identít na **role s rytmom, skillmi a výstupom**
- [ ] zaviesť **shared + lane-specific skills**
- [ ] zapnúť **heartbeat / cron / handoff loop**
- [ ] spraviť prvý funkčný pilot aspoň pre **revenue + voice + integration + delivery**

---

## 1. Audit súčasného stavu
- [ ] spísať všetkých agentov a ich workspace
- [ ] spísať všetky existujúce lokálne skills
- [ ] označiť ktoré skills sú:
  - [ ] shared/common
  - [ ] lane-specific
  - [ ] legacy / duplicitné / nejasné
- [ ] zistiť, ktoré skills sú dnes reálne používané len tebou manuálne
- [ ] overiť current config problémy a drift
  - [ ] opraviť stale config entry `acpx`
- [ ] skontrolovať, či už nie sú niekde heartbeat/cron nastavenia

---

## 2. Navrhnúť skill topológiu
- [ ] rozhodnúť shared vrstvu:
  - [ ] `~/.openclaw/skills` = common/shared pack
- [ ] rozhodnúť lane vrstvu:
  - [ ] `agents/<lane>/skills` = lane-local pack
- [ ] rozhodnúť osud current root `/singularitas/skills`
  - [ ] presunúť
  - [ ] rozdeliť
  - [ ] alebo dočasne nechať a explicitne mapovať
- [ ] zaviesť pravidlo:
  - [ ] shared = všetko, čo používa viac lane-ov
  - [ ] lane-local = to, čo tvorí operačnú výhodu konkrétneho agenta

---

## 3. Skill assignment matrix
Pre každý agent lane:
- [ ] definovať **čo má robiť**
- [ ] definovať **aké skills potrebuje**
- [ ] definovať **aké skills nesmie dostať**
- [ ] definovať **aké externé systémy používa**
- [ ] definovať **aké výstupy produkuje**
- [ ] definovať **kam handoffuje ďalšiu prácu**

### Minimálne spraviť pre:
- [ ] revenue
- [ ] voice
- [ ] integration
- [ ] delivery
- [ ] research
- [ ] web
- [ ] proof
- [ ] ops
- [ ] janitor
- [ ] personal-ops
- [ ] personal-web
- [ ] build

---

## 4. Doplniť skill gaps
- [ ] porovnať current local skills vs reálne potreby lane-ov
- [ ] spraviť shortlist skillov z ClawHub
- [ ] označiť každý kandidát ako:
  - [ ] now
  - [ ] later
  - [ ] skip
- [ ] neinštalovať všetko naraz
- [ ] najprv riešiť len skills, ktoré zavrú konkrétny workflow gap

### Prioritné gaps pravdepodobne:
- [ ] voice: Vapi / transcribe layer
- [ ] integration: webhook / CRM / connector layer
- [ ] revenue: CRM + scheduling + outreach support
- [ ] web: WordPress / SEO / publishing
- [ ] research: market / competitor / sourcing skills
- [ ] ops/janitor: audit / monitor / backup

---

## 5. Upratať ownership a contracts
Pre každý agent:
- [ ] napísať **owner contract**
- [ ] napísať **scope**
- [ ] napísať **allowed autonomous actions**
- [ ] napísať **what needs approval**
- [ ] napísať **heartbeat output format**
- [ ] napísať **escalation conditions**
- [ ] napísať **handoff destinations**

---

## 6. Heartbeat framework
Pre každý lane:
- [ ] určiť, či heartbeat vôbec potrebuje
- [ ] nastaviť cadence
  - [ ] napr. 30m / 1h / 2h / pracovné hodiny
- [ ] definovať heartbeat prompt
- [ ] definovať, čo má heartbeat surfacovať:
  - [ ] blockers
  - [ ] risks
  - [ ] stale queues
  - [ ] next move
  - [ ] escalation-worthy changes
- [ ] definovať, kam heartbeat ide
- [ ] nastaviť, aby heartbeat neprodukoval spam

### Prvé heartbeat kandidáty:
- [ ] revenue
- [ ] voice
- [ ] integration
- [ ] delivery
- [ ] janitor
- [ ] ops

---

## 7. Cron jobs
- [ ] identifikovať opakované úlohy, ktoré nemajú byť heartbeat
- [ ] pre každú takú úlohu definovať:
  - [ ] trigger time
  - [ ] input
  - [ ] expected output
  - [ ] failure path
- [ ] nepoužiť cron na “premýšľanie”, ale na konkrétne rutiny

### Dobré prvé cron joby:
- [ ] queue scan
- [ ] CRM consistency check
- [ ] stale follow-up detection
- [ ] website/proof queue refresh
- [ ] backup / audit / monitor sweep
- [ ] daily founder digest assembly input prep

---

## 8. Handoff graph medzi lane-mi
- [ ] nakresliť explicitný flow:
  - [ ] research → revenue
  - [ ] revenue → voice
  - [ ] voice → integration
  - [ ] integration → delivery
  - [ ] delivery → proof
  - [ ] proof → web / revenue
- [ ] pre každý handoff určiť:
  - [ ] artifact
  - [ ] trigger
  - [ ] acceptance condition
  - [ ] kto potvrdzuje prevzatie

---

## 9. Secrets, tool gating, bezpečnosť
- [ ] spísať ktoré skills potrebujú API keys / config
- [ ] doplniť len tie credentials, ktoré sú naozaj potrebné
- [ ] oddeliť risky write skills od read-only skills
- [ ] všetky produkčné write paths držať za approval gate
- [ ] overiť, že lane nemá viac práv než potrebuje

---

## 10. Pilot rollout
### Pilot 1: revenue + voice + integration + delivery
- [ ] priradiť shared skills
- [ ] priradiť lane skills
- [ ] zapnúť heartbeat
- [ ] pridať 1–2 cron joby na lane
- [ ] definovať handoff artifacts
- [ ] spraviť testovací end-to-end loop
- [ ] logovať čo sa pokazilo
- [ ] upraviť prompty / skills / contracts podľa reality

---

## 11. Observability a reversibility
- [ ] každá zmena musí byť reverzibilná
- [ ] mať zoznam:
  - [ ] čo sa zaplo
  - [ ] čo sa zmenilo
  - [ ] ako to vypnúť
- [ ] logovať heartbeat outcomes
- [ ] logovať cron success/failure
- [ ] mať rollback pre zlé skill assignmenty

---

## 12. Definition of done
Hotové to je, keď:
- [ ] každý dôležitý lane má jasný scope
- [ ] každý lane má priradené skills
- [ ] shared skills sú oddelené od lane-local
- [ ] heartbeat funguje bez spamu
- [ ] cron robí konkrétne rutiny
- [ ] handoff medzi lane-mi je explicitný
- [ ] aspoň jedno kvarteto funguje end-to-end
- [ ] ty už nemusíš väčšinu skillov invokovať manuálne

Ak chceš, ďalší krok spravím za teba ako **konkrétny execution plan pre revenue / voice / integration / delivery**.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1682",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Tue 2026-03-24 16:29 GMT+1"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Adam Xvadur (1594354152)",
  "id": "1594354152",
  "name": "Adam Xvadur",
  "username": "xvadur"
}
```

zapis ho do obsidianu, a rozdeľ to na action batch runs, ktoré vykonaš, a ku každému napis potrebné otázky pre clean exec
assistant: Zapíšem to do Obsidianu ako execution note a rozsekám checklist na batch runs s otázkami pre clean exec.
assistant: [[reply_to_current]] [[tts:plain]][[tts:text]]Hotovo. Zapísal som to do Obsidianu ako execution note a rozdelil som to na batch runs s otázkami pre clean exec. Note je v Operácie, v Xvadur Agent Deploy Studio, pod názvom Agent skill overhaul a operačný rámec. Keď chceš, ďalší krok je ísť rovno na Batch 1 a spraviť audit reality plus skill inventory.[[/tts:text]]

Hotovo — zapísal som to do Obsidianu sem:

`/Users/_xvadur/singularitas_opus/Operácie/Xvadur - Agent Deploy Studio/2026-03-24 - Agent skill overhaul a operačný rámec.md`

Obsah som rozdelil na:
- **8 action batch runs**
- ku každému:
  - čo sa vykoná
  - aké sú outputy
  - **clean exec questions**
  - definition of done

Najdôležitejšie je, že to už nie je len checklist, ale **vykonávací plán v poradí**:
1. audit reality
2. skill topology
3. lane assignment matrix
4. ClawHub gap fill
5. heartbeat + cron design
6. handoff graph
7. controlled rollout
8. validation + tuning

Ak chceš, idem hneď na **Batch 1** a pripravím ti:
- agent inventory
- skill inventory
- first-pass classification
- config drift notes
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1685",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Tue 2026-03-24 21:33 GMT+1"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Adam Xvadur (1594354152)",
  "id": "1594354152",
  "name": "Adam Xvadur",
  "username": "xvadur"
}
```

poďme na to
assistant: Idem na Batch 1: spravím audit agentov, skill inventory a drift poznámky, potom ti to zapíšem ako prvý execution batch výsledok.
assistant: [[reply_to_current]] Hotovo — spravil som **Batch 1 audit** a zapísal ho do Obsidianu sem:

`Operácie/Xvadur - Agent Deploy Studio/2026-03-24 - Batch 1 audit reality a skill inventory.md`

### Najdôležitejší záver
Máš **reálnu agent vrstvu** aj **reálnu skill vrstvu**, ale chýba medzi nimi **binding layer**:
- skill placement
- ownership boundaries
- rhythm cez heartbeat / cron / handoff

### Tvrdé findings
- agentov je **14**
- root custom skillov je **34**
- shared skills v `~/.openclaw/skills` sú **0**
- lane-local skills v `agents/<lane>/skills` sú **0**
- heartbeat config je **nulový**
- cron config je **nulový**
- config má stale `acpx` plugin entry

### Praktický verdict
Dnes je to:
- **founder-invoked toolbox**, nie
- **lane-owned operating framework**

### Ďalší krok = Batch 2
Aby som ho spravil clean, potrebujem od teba rozhodnúť tieto veci:

1. Má byť **Jarvis/main** silný orchestrátor, alebo skôr founder interface, čo deleguje?
2. Chceš shared skills fyzicky v **`~/.openclaw/skills`**, alebo radšej repo-managed cez explicit loading?
3. Ktoré current root skilly sú podľa teba **legacy / disposable**?
4. Ktoré lane-y môžu mať v prvej vlne **reálnu write power**?
5. Majú byť `github`, `google-workspace`, `linear`, `rag-jarvis`:
   - shared baseline,
   - alebo niektoré founder-only?
6. Chceš prvý rollout robiť skôr:
   - **strict boundaries first**
   - alebo **immediate utility first**?

Keď mi toto zodpovieš, idem rovno na **Batch 2: skill topology a ownership model**.
