# Session: 2026-03-22 14:06:20 UTC

- **Session Key**: agent:research:telegram:direct:1594354152
- **Session ID**: b6d88c01-5b60-4604-bba5-4e2cc5172075
- **Source**: webchat

## Conversation Summary

user: Conversation info (untrusted metadata):
```json
{
  "message_id": "465",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Sat 2026-03-21 15:08 GMT+1"
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

lebo nemoclaw predstavili ako enterprice grafe sedíte agenta, preto tak rozmýšľam. 
lebo môj bottleneck je práve n8n kde neviem robiť komplexne workflows, takto by som mohol konfigurovať priamo nemoclaw, ktorý by bol spojený s telegramom maklera, ale nemoclaw stále ovládam ja, čiže by som mohol nakonfigurovať openclaw ktorý beží u mňa v dockeri a potom to môžeme skalovat niekde na vps alebočo
assistant: [[reply_to_current]] [[tts:calm]] [[tts:text]]Áno, toto uvažovanie je podľa mňa správne. Ak je tvoj bottleneck n8n, tak agentový backend typu OpenClaw plus NemoClaw runtime ti vie odomknúť presne tú vrstvu, ktorá n8n chýba: stavové rozhodovanie, dlhší kontext, human-in-the-loop a flexibilnejšie workflowy.[/tts:text]]

Ja by som to zhrnul takto:

## Prečo ti to dáva zmysel
**n8n** je super na:
- lineárne automácie
- trigger → pár krokov → výsledok
- prepájanie API

Ale slabne pri:
- zložitej konverzačnej logike
- stavových workflowoch
- rozhodovaní podľa kontextu
- dlhšom handoffe medzi AI a človekom
- “čo spraviť ďalej, keď sa veci nevyvíjajú podľa šablóny”

A presne tu vie byť:
- **OpenClaw** = agent orchestration layer
- **NemoClaw** = secure/managed runtime na to, aby to bolo prevádzkovateľné a kontrolované

## Tvoj návrh architektúry je rozumný
### Lokálne / teraz
- ty máš **OpenClaw u seba v Dockeri**
- nad tým vieš definovať logiku, nástroje, routing, session behavior
- **NemoClaw** môže bežať ako izolovaný klient-facing agent runtime
- Telegram makléra je koncové UI
- ElevenLabs obsluhuje hovory
- MCP/webhooks prepájajú všetky eventy

### Neskôr / scale
- rovnaký model vieš presunúť:
  - na **VPS**
  - alebo dedikovaný host
  - prípadne oddeliť klientov po sandboxoch / inštanciách

To je silnejšie než n8n-only setup, lebo:
- nemusíš všetko lámať do node grafu
- logiku držíš bližšie k agentovi
- vieš robiť komplexné branchingy a approvals

## Čo je na tom naozaj silné
### 1. Ty zostávaš operátor
To je kľúčové:
- klient vidí “svojho Telegram agenta”
- ale **control plane ostáva u teba**
- ty vieš meniť:
  - workflow
  - promptovanie
  - povolené akcie
  - routing
  - escalation rules

Čiže klient dostáva service, nie root access.

### 2. Maklér dostane jednoduchý interface
Maklér nechce:
- n8n
- dashboardy
- 40 integrácií

Maklér chce:
- “čo sa stalo?”
- “čo mám potvrdiť?”
- “aký je ďalší krok?”
- “zavolaj tomu klientovi / bookni obhliadku / pošli follow-up”

Telegram je na toto ideálny.

### 3. Ty obchádzaš bottleneck n8n
Namiesto:
- “ako toto naklikám cez 18 nodeov”

sa pýtaš:
- “aký má byť behavior agenta?”

To je úplne iná liga.

## Ale dôležitá korekcia
**NemoClaw by som dnes nebral ako finálny enterprise production backbone len preto, že je od NVIDIE.**

Lebo podľa ich vlastného README:
- je to **alpha**
- **not production-ready**
- skôr reference stack / early preview

Takže:

### ako smer:
**áno**

### ako experiment / interný backend / pilot:
**áno**

### ako “na toto postavím zajtra všetkých klientov”:
**zatiaľ opatrne**

## Najrozumnejší rollout
Ja by som išiel v 3 vrstvách:

### Fáza 1 — bez NemoClaw lock-inu
Postav:
- **OpenClaw backend**
- Telegram-facing workflow
- ElevenLabs call ingestion
- CRM/calendar/webhook tools

A urob to tak, aby agent logika nebola naviazaná len na NemoClaw.

### Fáza 2 — NemoClaw ako secure runtime experiment
Na 1 internom alebo pilotnom klientovi:
- daj agenta do NemoClaw sandboxu
- otestuj policy, approvals, infra, observability

### Fáza 3 — scale
Ak sa osvedčí:
- klient po klientovi
- sandbox po sandboxe
- VPS / infra orchestration
- jasné tenancy rules

Takto si nespáliš roadmapu na alpha stacku.

## Čo by som spravil namiesto n8n
Nie “vyhodiť n8n”, ale zmeniť mu rolu.

### n8n nech robí:
- jednoduché integrácie
- webhook fan-out
- low-level API glue
- notifikácie
- ETL-ish veci

### OpenClaw agent nech robí:
- rozhodovanie
- workflow state
- human-in-the-loop
- exception handling
- konverzačnú vrstvu pre makléra
- prioritizáciu akcií

To je podľa mňa správne rozdelenie.

## Veľmi praktický produktový framing
Toto už nie je:
- “mám hlasového bota”

Ale:
- **telefonický AI agent + Telegram copilot pre makléra**
- backend orchestration si riadiš ty
- klient dostane jednoduchý operačný interface

To je enterprise-ovejšie a predáva sa to lepšie.

## Môj verdict
Áno:
- tvoje uvažovanie je správne
- tento smer vie vyriešiť bottleneck n8n
- OpenClaw ako tvoja riadiaca vrstva + Telegram agent pre makléra je silný model
- NemoClaw je zaujímavý ako runtime/sandbox layer, ale zatiaľ by som ho bral skôr **ako experimentálnu infra vrstvu než jediný produkčný základ**

Ak chceš, ďalší krok ti spravím veľmi konkrétne:
1. **navrhnem architektúru “n8n + OpenClaw + NemoClaw + ElevenLabs + Telegram”**,  
2. alebo ti rovno spíšem **MVP roadmapu na 2 týždne**, čo postaviť ako prvé.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "469",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Sat 2026-03-21 15:17 GMT+1"
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

lebo vieš, keď budeš chcieť aby si vedel handlovát hovorí ktoré budú prichádzať mne cez agenta z mojej landing, tak sa pokúsim spojiť môj openclaw a elevenlab, keď to robím pre maklera tak na spojenie kalendára a elevenlab použijem n8n 
použiť openclaw je podstatne jednoduchšie 

čiže 
vyskúšame spraviť backend k maklérovi 
z toho agenta marek vo vapi spravíme n8n backend 
naposledy keď sme to robili to bolo napicu 

ale možno keď to naplanujeme sa to môže podariť
assistant: [[reply_to_current]] [[tts:calm]] [[tts:text]]Áno, toto už je dobrý smer. Keď to robíš pre seba, OpenClaw plus ElevenLabs ti dáva väčšiu flexibilitu. Keď to robíš pre makléra, môže mať zmysel nechať n8n len ako integračnú vrstvu, ale nenechať na ňom celú inteligenciu workflowu.[/tts:text]]

Presne kde bol problém naposledy:
- snažili ste sa, aby **n8n bol mozog**
- ale n8n je skôr **kábel a lepidlo**, nie dobrý decision engine

Preto by som to teraz rozdelil takto:

## Nový plán
### 1. Vapi / ElevenLabs / voice layer
- vedie hovor
- zbiera structured data
- posiela eventy ďalej

### 2. OpenClaw alebo agent layer
- rozhoduje:
  - čo spraviť s leadom
  - či booknúť termín
  - či pýtať potvrdenie
  - či eskalovať maklérovi
- drží stav konverzácie a workflowu

### 3. n8n
- len vykonáva jednoduché veci:
  - kalendár
  - CRM zápis
  - webhook forwarding
  - SMS/email
- nie je hlavný mozog

Takže:
- **agent thinking v OpenClaw**
- **integrácie v n8n**

To je podľa mňa správne.

---

## Pre makléra backend by som šiel cez MVP
Nie všetko naraz. Len tento flow:

### MVP flow
1. človek zavolá
2. voice agent kvalifikuje lead
3. agent vytvorí summary
4. maklér dostane správu do Telegramu:
   - meno
   - typ nehnuteľnosti
   - lokalita
   - budget
   - záujem
   - navrhnutý ďalší krok
5. maklér odpovie:
   - potvrď
   - navrhni iný termín
   - zavolám osobne
   - zahodiť lead
6. backend vykoná akciu cez n8n / kalendár / CRM

Toto už samo o sebe je predajný produkt.

---

## Čo by som tentoraz neurobil
- nerobiť naraz:
  - full autonomous agent
  - full calendar sync
  - CRM sync
  - retries
  - reminders
  - outbound
  - handoff
  - analytics
- nenechať n8n rozhodovať z textu
- nerobiť “veľký generický workflow”

---

## Čo by som spravil tentoraz
### Jasne definovať inputs/outputs
Po hovore musí prísť jeden čistý objekt, napríklad:
- caller_name
- phone
- intent
- property_type
- location
- budget
- urgency
- wants_viewing
- preferred_time
- confidence
- summary

A hotovo.

### Potom decision layer
Jednoduché pravidlá:
- vysoký intent + chce obhliadku → správa maklérovi s CTA
- nízka confidence → označiť na ručný follow-up
- spam / irrelevant → discard

### Až potom integrácie
- kalendár
- CRM
- follow-up

---

## Najlepší framing
Z “agenta Marek vo Vapi” by som nespravil “veľký n8n backend”.

Spravil by som:
- **Vapi/Marek = call frontend**
- **OpenClaw = workflow brain**
- **n8n = action executor**

To je oveľa zdravšie.

---

## Prečo to tentoraz môže vyjsť
Lebo už vieš, čo bolo napicu:
- príliš veľa vecí v n8n
- nejasná architektúra
- pravdepodobne nejasné handoffy a stavy

Keď to teraz spravíš ako:
- malý flow
- jasný JSON kontrakt
- agent layer oddelene
- n8n len na integrácie

tak to má oveľa väčšiu šancu fungovať.

---

## Môj návrh ďalšieho kroku
Poďme to naplánovať úplne konkrétne v 4 častiach:
1. **event schema po hovore**
2. **Telegram správa pre makléra**
3. **decision rules**
4. **čo ide do n8n a čo nejde do n8n**

Ak chceš, v ďalšej správe ti to rovno rozkreslím ako:
**„backend pre makléra v MVP verzii“** — bez omáčky, len presný plán.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "471",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Sat 2026-03-21 15:19 GMT+1"
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

dobre, pozri si materiály k všetkému co máme k voice agent businesu, pozri si vo vapi agenta marek a poďme zistiť jaky n8n potrebujeme
assistant: Najprv si pozriem, čo už máte lokálne k voice agent biznisu a k agentovi Marek, aby sme nenavrhovali n8n naslepo.
assistant: Našiel som handoff aj baseline k Marekovi. Teraz vytiahnem konkrétne artefakty k Vapi a starému n8n pokusu, nech navrhneme len to minimum, čo naozaj chýba.
assistant: [[reply_to_current]] Pozrel som to. Krátka verzia: **Marek je už promptovo dosť dobrý; chýba mu nie nový mozog, ale malý a presný n8n toolpack**. Naposledy to bolo zlé preto, že sa z n8n robil workflow brain. Teraz ho treba držať len ako **action layer**.

## Čo už máme
Z materiálov vychádza:
- Marek vo Vapi je už postavený ako **inbound realitný qualifier**
- má:
  - routing / lanes
  - lead scoring
  - next-step engine
- **nemá tools**
- handoff note priamo hovorí, že ďalší missing piece je **n8n tool module / handoff layer**

A baseline hovorí:
- current tools: **none**
- V1 scope má byť úzky
- booking má byť konzervatívny
- pricing/valuation mimo scope

## Záver
Pre Mareka **nepotrebujeme veľké n8n**.  
Potrebujeme len také n8n, ktoré pokryje jeho reálne outcomes.

Podľa promptu má Marek tieto outcomes:
- `URGENT_CALLBACK`
- `CALLBACK`
- `VIEWING_NEXT_STEP`
- `CRM_RECORD_ONLY`
- `REJECT_LOW_VALUE`

Z toho by som spravil **4 n8n workflowy**, nie viac.

---

# Aký n8n potrebujeme pre Mareka v1

## 1. `realtor-log-lead`
Najdôležitejší workflow.  
Používa sa skoro po každom hovore.

### Účel
Zapísať výsledok hovoru do jedného čistého záznamu.

### Input
- agent_name
- caller_name
- phone
- email
- intent_primary
- lane
- lead_temperature
- call_outcome
- summary_short
- property_type
- location
- budget_range
- timeline
- listing_reference
- preferred_callback_time
- notes

### Output
- accepted: true
- record_id
- saved_at
- next_step_recommended

### Prečo
Aby po každom hovore vznikol **normálny structured lead record**, nie len transcript chaos.

---

## 2. `realtor-request-callback`
Toto je hlavný workflow pre makléra.

### Účel
Založiť callback request a poslať maklérovi správu.

### Input
- caller_name
- phone
- reason
- urgency
- summary_short
- lead_temperature
- preferred_callback_time
- listing_reference
- source = marek_vapi

### Output
- accepted: true
- callback_id
- broker_notified: true/false
- recommended_window
- telegram_message_id optional

### Čo má spraviť
- uložiť callback request
- poslať Telegram správu maklérovi
- prípadne označiť prioritu

### Toto je jadro systému
Tu sa láme, či je produkt použiteľný.

---

## 3. `realtor-viewing-request`
Nie full booking engine. Len bezpečný next-step workflow.

### Účel
Keď chce klient obhliadku, workflow:
- zachytí dopyt
- overí, či máme dosť údajov
- pošle maklérovi návrh / upozornenie
- alebo pripraví booking request

### Input
- caller_name
- phone
- listing_reference
- preferred_day
- preferred_time_window
- buyer_or_tenant
- summary_short
- urgency
- notes

### Output
- accepted: true
- viewing_request_id
- status: `needs_broker_confirmation` | `needs_more_info` | `queued`
- broker_notified: true/false

### Dôležité
**V1 by som nerobil automatické bookovanie do kalendára.**  
Len:
- capture
- notify
- prepare next step

Lebo prompt aj handoff hovoria, že booking má byť zatiaľ konzervatívny.

---

## 4. `realtor-low-intent-close`
Malý workflow, ale užitočný.

### Účel
Pri low-value / cold / competitor-ish hovore:
- uložiť stručný záznam
- bez ďalšieho rušenia makléra

### Input
- caller_name optional
- phone optional
- reason
- summary_short
- intent_primary
- disposition

### Output
- accepted: true
- disposition_saved: true

### Prečo
Aby maklér nedostával bordel do Telegramu.

---

# Čo by som do v1 NEDÁVAL
Toto bol podľa mňa zdroj predchádzajúceho chaosu:

- automatické slot finding cez kalendár
- komplikované multi-branch flows
- full CRM orchestration
- retry logic na všetko
- dynamic pricing / valuation
- outbound sequences
- “AI decides everything”

To je v2+.

---

# Ako by som rozdelil zodpovednosť

## Vapi / Marek
Robí:
- call handling
- qualification
- next-step choice
- tool calling

## n8n
Robí:
- webhook endpointy
- validáciu payloadov
- uloženie dát
- Telegram notify makléra
- prípadne zápis do CRM / sheets / DB

## Nie n8n
Nemá robiť:
- rozmýšľanie
- interpretáciu celého hovoru
- lead strategy
- complex conversation logic

---

# Minimálny toolpack, ktorý treba dať Marekovi do Vapi
Ja by som mu dal presne tieto tools:

## Tool 1: `log_lead`
Default tool po hovore.

## Tool 2: `request_callback`
Keď outcome = callback / urgent_callback.

## Tool 3: `request_viewing_next_step`
Keď klient chce obhliadku alebo listing-specific follow-up.

## Tool 4: `mark_low_value`
Keď lead netreba posúvať maklérovi.

To je celé.

---

# Odporúčaný JSON kontrakt pre Mareka
Aby to tentoraz nebolo napicu, Marek musí volať tools s fixnými poľami.

## Spoločné povinné polia
- `caller_name`
- `phone`
- `intent_primary`
- `summary_short`
- `call_outcome`

## Podľa lane doplnkové
- `property_type`
- `location`
- `budget_range`
- `timeline`
- `listing_reference`
- `preferred_callback_time`
- `preferred_day`
- `preferred_time_window`

Ak tieto polia fixneme dopredu, n8n bude jednoduchý.

---

# Môj odporúčaný rollout
## Fáza 1
Spraviť len:
- `realtor-log-lead`
- `realtor-request-callback`

A otestovať 10 call scenárov.

## Fáza 2
Pridať:
- `realtor-viewing-request`

## Fáza 3
Až potom:
- kalendár
- CRM sync
- richer Telegram controls

---

# Verdikt
**Aký n8n potrebujeme?**
Nie veľký. Potrebujeme:
- 1 logging workflow
- 1 callback workflow
- 1 viewing request workflow
- 1 low-intent disposal workflow

To je realistické MVP.

Ak chceš, v ďalšej správe ti spravím presne toto:
1. **zoznam webhook endpointov**,  
2. **payload schema pre každý tool**,  
3. a **čo má Marek volať v ktorom prípade**.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "478",
  "sender_id": "1594354152",
  "sender": "Adam Xvadur",
  "timestamp": "Sun 2026-03-22 12:37 GMT+1"
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

pomenuj mi prosím co marek agent vo vapi teraz robí, ja ti poviem aký backend to potrebuje
assistant: [[reply_to_current]] Jasné. **Marek vo Vapi teraz robí hlavne inbound kvalifikáciu hovoru pre makléra**. Nie je to ešte plne operatívny agent s backendom — je to **silný promptový front-desk/qualifier**.

## Čo Marek teraz robí

### 1. Zdvihne inbound hovor ako prvá línia kontaktu
- vystupuje ako **virtuálny asistent makléra Jakuba Valachovského / Brex Reality**
- komunikuje **po slovensky**
- používa **vykanie**
- má pôsobiť prirodzene, stručne a profesionálne

### 2. Najprv zisťuje, o aký typ hovoru ide
Routinguje call do intentov / lanes, najmä:
- **BUYER** — chce kúpiť
- **SELLER** — chce predať
- **VIEWING_REQUEST / LISTING_SPECIFIC** — chce obhliadku alebo volá ku konkrétnej ponuke
- **CALLBACK_REQUEST** — chce hovoriť priamo s maklérom
- **GENERAL_INFO / GENERAL_INQUIRY** — len sa informuje
- **REFERRAL** — prišiel na odporúčanie
- **COMPETITOR_OR_LOW_INTENT** — nízky intent / obkukávač

V staršej lane verzii sú ešte:
- landlord
- tenant

Čiže prakticky: **najprv zaradí, čo človek vlastne rieši**.

### 3. Robí len minimálnu potrebnú kvalifikáciu
Pýta sa len to, čo treba pre ďalší krok.

#### Keď je buyer:
- typ nehnuteľnosti
- lokalita
- rozpočet
- časový horizont
- či ide o bývanie alebo investíciu
- niekedy financovanie / hypotéka

#### Keď je seller:
- čo predáva
- lokalita
- typ a stav nehnuteľnosti
- časovosť
- očakávanie od makléra

#### Keď je listing / obhliadka:
- ku ktorej ponuke volá
- či chce info alebo termín
- kontakt
- preferovaný časový rámec

#### Keď chce callback:
- meno
- telefón
- dôvod
- či chce ASAP alebo neskôr

### 4. Počas hovoru si robí lead scoring
Vyhodnocuje lead ako:
- **HOT**
- **WARM**
- **COLD**
- prípadne **LOW_VALUE**

A sleduje aj:
- či je decision maker
- urgentnosť
- štýl správania
- konkrétnosť záujmu

### 5. Na konci zvolí ďalší krok
Jeho next-step engine teraz pracuje s outcomes typu:
- **URGENT_CALLBACK**
- **CALLBACK**
- **VIEWING_NEXT_STEP**
- **CRM_RECORD_ONLY**
- **REJECT_LOW_VALUE**

Čiže Marek už teraz vie povedať:
- toto treba rýchlo odovzdať maklérovi
- toto je len zachytenie leadu
- toto smeruje na obhliadku
- toto je slabý lead

### 6. Na konci hovoru urobí stručné zhrnutie
Zhrnie:
- čo klient rieši
- čo sa zistilo
- aký je ďalší krok

---

## Čo Marek teraz NEROBÍ

Toto je dôležité — toto ešte nemá:

### 1. Nemá tools
Podľa baseline:
- `toolIds: []`

Čiže:
- nič reálne nezapisuje
- nič neposiela do CRM
- nič neposiela do Telegramu
- nič nespúšťa v n8n
- nič nebookuje

### 2. Nevie reálne potvrdiť termín
Prompt je zámerne konzervatívny:
- **nesmie sľubovať pevný termín bez systémového potvrdenia**
- booking je zatiaľ len placeholder logika

### 3. Nerobí valuation / pricing
Je tam explicitný zákaz:
- nedáva cenové odhady
- nesľubuje nacenenie ako fakt

### 4. Nerobí skutočný handoff
Vie povedať „Jakub sa ozve“, ale:
- bez backendu to nie je skutočná akcia
- je to zatiaľ len konverzačné správanie, nie vykonaný workflow

---

## Čo Marek momentálne v skratke je
**Marek je teraz voice intake + qualifier + next-step classifier.**

Nie je ešte:
- booking agent
- CRM agent
- Telegram agent
- workflow executor

---

## Najpresnejšia jedna veta
**Marek teraz zachytí inbound realitný hovor, zaradí typ dopytu, získa minimum potrebných informácií, ohodnotí lead a rozhodne, či má ísť na callback, obhliadku, záznam alebo odfiltrovanie.**

Ak chceš, ďalšia správa môže byť úplne praktická:
**„na tieto Marek outcomes potrebuješ presne takýto backend“** — a rozdelíme to po jednom endpoint-e.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sun 2026-03-22 15:00 GMT+1] ideme robit n8n alebo potrebujeme vylepsit prompt?
assistant: [[reply_to_current]] Ideme robiť **n8n**, nie prompt.

Prompt je už **dosť dobrý na v1**:
- routuje hovory
- kvalifikuje
- scoreuje lead
- vyberá next step

Bottleneck teraz nie je „čo má Marek povedať“, ale:
- že **nevie nič vykonať**
- nemá tools
- nevie spraviť callback request
- nevie poslať info maklérovi
- nevie uložiť lead

## Čiže poradie:
### teraz
1. **spraviť n8n toolpack v1**
2. napojiť ho do Vapi
3. otestovať 10 scenárov
4. až potom doladiť prompt podľa failov

## Čo by som dnes robil
Len minimum:

- `realtor-log-lead`
- `realtor-request-callback`
- `realtor-viewing-request`
- `realtor-low-intent-close`

## Kedy by sme išli späť do promptu
Až keď pri testoch zistíme, že Marek:
- zle routuje lanes
- pýta sa moc veľa
- nevie sa rozhodnúť medzi callback vs viewing
- zle vypĺňa payloady

Takže:
**dnes n8n.**
**Prompt len ak sa pri tool testoch ukáže konkrétny problém.**

Ak chceš, hneď ti rozpisem:
- presné **4 webhooky**
- input/output payloady
- a ktorý tool má Marek volať v ktorom prípade.
assistant: 🦞 OpenClaw 2026.3.13 (61d171a)
🧠 Model: openai-codex/gpt-5.4 · 🔑 oauth (openai-codex:default)
🧮 Tokens: 135k in / 430 out
🗄️ Cache: 50% hit · 136k cached, 0 new
📚 Context: 136k/272k (50%) · 🧹 Compactions: 0
📊 Usage: 5h 99% left ⏱4h 45m · Week 84% left ⏱3d 8h
🧵 Session: agent:research:telegram:direct:1594354152 • updated just now
⚙️ Runtime: direct · Think: low
🔊 Voice: inbound · provider=elevenlabs · limit=1500 · summary=on
🪢 Queue: collect (depth 0)
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sun 2026-03-22 15:02 GMT+1] /save uloz ze ideme dorobit n8n backend k makler agentovy, v novej konverzacii
assistant: [[reply_to_current]] Uložené: v novej konverzácii ideme dorobiť **n8n backend k maklér agentovi**. Začneme toolpackom v1 pre Mareka, nie prepisovaním promptu.
