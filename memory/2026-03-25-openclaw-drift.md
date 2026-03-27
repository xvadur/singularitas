# Session: 2026-03-25 13:56:43 UTC

- **Session Key**: agent:main:main
- **Session ID**: 14a91db1-739c-496b-8bce-b0b8cf8019f2
- **Source**: webchat

## Conversation Summary

assistant: Našiel som podozrivý bod: CLI je novšia než bežiaci gateway. Idem overiť, odkiaľ launch agent štartuje OpenClaw, lebo to je presne typ driftu, čo vie update zneistiť.
assistant: Našiel som core problém. Ešte si overím, či `openclaw-main` checkout je čistý a na akom commite/tagu sedí — to povie, či update pôjde hladko alebo bude treba najprv upratať repo.
assistant: [[reply_to_current]] Verdikt: **systém nie je “nepripravený” — systém je v drift stave.**  
To je reálny problém. Nie firewall. Nie host. **Install drift.**

### Čo som našiel
Máš naraz **dve OpenClaw reality**:

- **globálna CLI**: `2026.3.23-2`
- **bežiaci gateway service**: `2026.3.9`

A to nie je domnienka. Service plist ukazuje, že gateway štartuje zo **source checkoutu**:

- launch agent spúšťa Node nad `~/openclaw-main/dist/index.js`
- comment/version v service je `v2026.3.9`
- logy hovoria:
  - **“Config was last written by a newer OpenClaw (2026.3.23-2); current version is 2026.3.9.”**

Čiže:
- **CLI už je novšia**
- **gateway stále beží na staršom source builde**
- config už bol medzitým dotknutý novšou verziou

To je presne ten typ stavu, ktorý nechceš nechať visieť.

### Dôležité zistenia
- `~/openclaw-main` je **clean worktree**
- branch: `main`
- HEAD: `f57c0a1...`
- latest tags v repo už obsahujú `v2026.3.23-2`
- security audit: bez kritických problémov
- UI je lokálne, takže reverse-proxy warning nás netrápi

### Reálny problém
Nie “update dostupný / nedostupný”.

**Problém je, že update path je rozštiepený:**
1. globálny npm/pnpm install
2. source checkout gateway service

To znamená, že aj keď `openclaw` v shelli vyzerá aktualizovaný, **runtime nemusí byť**.

### Čo treba spraviť
Potrebujeme systém **zjednotiť na jeden install method**.

Moja odporúčaná voľba:
### 1. zostať na **source checkout** pre gateway
Lebo:
- service už na tom beží
- repo je clean
- rollback je jednoduchší cez git
- kontrola nad runtime je lepšia

### Safe update sequence
1. backup configu a launch agent info
2. update `~/openclaw-main`
3. build
4. `openclaw doctor`
5. restart gateway
6. verify:
   - `openclaw status --deep`
   - `openclaw update status`
   - health + channels
   - či runtime verzia už nie je `2026.3.9`

### Čo ešte bije do očí
V logoch sú aj sekundárne veci, ktoré update môže, ale nemusí vyriešiť:
- stale config warning pre `plugins.entries.brave`
- repeated `skills ... resolves outside configured root`
- `tools.profile (coding) allowlist contains unknown entries`

To nie sú blockers pre update, ale sú to **cleanup kandidáti po update**.

---

## Môj odporúčaný ďalší krok
Vyber:

1. **Sprav mi safe update teraz**  
   - backup → update source checkout → build → doctor → restart → verify

2. **Najprv len backup + runbook**  
   - nič nemením, pripravím presný rollback-ready packet

3. **Najprv zjednoť install na global npm/pnpm**  
   - možné, ale toto teraz nepovažujem za najlepší smer

Moja voľba: **1**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Wed 2026-03-25 13:57 GMT+1] neviem preco, ale do teraz sa update robi hladko, podme prosim upratat system tak aby sa to dalo normalne updatovat
assistant: [[reply_to_current]] Áno. Treba to **upratať na jeden pravdivý update path**. Teraz máš split-brain a preto to pôsobí divne.

### Môj verdict
Najlepší stav je:

- **jeden runtime**
- **jeden update mechanism**
- **jeden service entrypoint**
- žiadne „CLI je novšia než gateway“

### Čo je zle teraz
Momentálne:
- shell `openclaw` ide z **global npm installu**
- gateway service ide zo **source checkoutu** `~/openclaw-main/dist/index.js`

To je hlavný bordel.

---

## Odporúčaný cieľový stav

### Varianta A — **source-first**  ✅ odporúčam
Nechať OpenClaw bežať zo `~/openclaw-main` a dorovnať tomu aj update flow.

Prečo:
- gateway už takto beží
- repo je clean
- rollback cez git je čistý
- vieš mať kontrolu nad channel/tag/build
- je to robustnejšie pre power-user setup

Cieľ:
- service bude stále ukazovať na `~/openclaw-main`
- global `openclaw` buď:
  - bude zosynchronizovaný na ten checkout, **alebo**
  - ho odstránime ako redundantný zdroj zmätku
- update sa potom robí konzistentne cez **source flow**

### Varianta B — global-only
Presunúť gateway na čistý npm/pnpm global install.

To by šlo, ale **teraz to neodporúčam**, lebo už máš reálne funkčný source runtime a skôr treba odstrániť drift než meniť architektúru.

---

## Čo navrhujem spraviť
Upratovanie v 3 krokoch:

### 1. Stabilize
- backup configu
- backup launch agent plist
- snapshot aktuálnej verzie + commit + service entrypoint

### 2. Normalize
- potvrdiť `source-first` ako canonical install
- prepojiť CLI/tooling tak, aby neukazovalo inú realitu než gateway
- odstrániť alebo neutralizovať redundantný global path, ak treba
- spustiť `openclaw doctor`, aby prepísal service entrypoint korektne na current install

### 3. Verify
- `openclaw status --deep`
- `openclaw update status`
- overiť, že:
  - runtime version = CLI version
  - config warning “written by newer OpenClaw” zmizol
  - gateway restartuje čisto
  - Control UI ide normálne

---

## Dôležitá poznámka
Toto už je **state-changing** zásah.  
Nechcem to robiť napoly.

Takže navrhujem tento konkrétny execution mode:

1. **Normalize source-first install teraz**
   - backup
   - doctor / service normalization
   - dorovnanie runtime
   - verify

2. **Len priprav runbook**
   - nič nemením

3. **Najprv detailný diff toho, čo presne zmažeme / prepíšeme**
   - ak chceš ultra opatrný režim

### Moja voľba: **1**

Ak dáš **1**, idem krok po kroku a pri každej citlivej veci poviem:
- čo idem spraviť
- dopad
- rollback shape
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Wed 2026-03-25 13:57 GMT+1] a to preco takto? 
to sa robi vzdy pri update?
assistant: [[reply_to_current]] Nie. **Toto nie je normálny stav po každom update.**

### Krátka odpoveď
Update sa ti doteraz zrejme „robil hladko“, lebo:
- update prebehol pre **jednu vrstvu**
- ale **service entrypoint** zostal na starej vrstve
- a dlho to ešte fungovalo, lebo OpenClaw je dosť tolerantný

Čiže nie:  
**nemá sa to robiť vždy.**  
Toto je skôr **nahromadený drift**.

### Prečo sa to stalo
Najpravdepodobnejší scenár je tento:

1. kedysi gateway bežal zo `~/openclaw-main`
2. neskôr sa spravil global install / update CLI
3. shell `openclaw` sa začal brať z `~/.npm-global/bin/openclaw`
4. ale launch agent ďalej štartoval starý source build z `~/openclaw-main/dist/index.js`

Výsledok:
- v termináli vidíš novú verziu
- v service beží stará
- oboje sa tvári „OK“
- až kým log nezačne hlásiť:
  - config písala novšia verzia než tá, čo práve beží

### Prečo to nebuchlo hneď
Lebo medzi týmito verziami asi nebol okamžitý breaking mismatch.  
Takže systém:
- stále bootol
- stále obsluhoval gateway
- stále prechádzal health checks

Lenže to je falošný pokoj.  
Je to **technický dlh**, nie clean state.

### Robí sa to vždy pri update?
**Nie.** Clean update flow má vyzerať takto:

- buď si **source install**
  - update ide cez repo/build/doctor/restart
- alebo si **global npm/pnpm install**
  - update ide cez package-manager flow

Ale nie oboje naraz.

### Čo je pointa
Problém nie je samotný update.  
Problém je, že **nie je jasné, ktorý install je kanonický**.

A keď toto nie je jasné, tak:
- `/status` môže hovoriť jednu vec
- shell druhú
- gateway tretiu

### Dobrý cieľový stav
Po uprataní chceme, aby platilo:

- `openclaw --version`
- bežiaci gateway
- launch agent entrypoint
- `openclaw update status`

…všetko ukazuje na **tú istú realitu**.

### Môj záver
Takže:
- **nie, nemá sa to diať pri každom update**
- **áno, je to opraviteľné**
- **áno, oplatí sa to upratať teraz**, kým to ešte nie je broken

Ak chceš, ďalší krok spravím veľmi prakticky:

1. poviem ti **presne čo upraceme**
2. čo sa prepíše
3. čo sa nechá tak
4. aký bude nový “one true update path”

Až potom dáš go.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Wed 2026-03-25 13:59 GMT+1] podme to upratat ano
assistant: Idem to upratať do source-first stavu. Najprv spravím backupy a snapshot, potom normalizujem service cez doctor/update flow a nakoniec overím, že CLI aj gateway hovoria tú istú verziu.
assistant: Backup je hotový. Teraz si overím najbezpečnejší spôsob, ako spustiť doctor/update **zo source checkoutu**, aby service prepísal na správny entrypoint a nie na global install.
assistant: Source checkout je stále na `2026.3.9`, takže samotné „upratanie“ potrebuje aj dorovnanie checkoutu. Najbezpečnejší ďalší krok je **source-side dry run update**, nech vidíme presný plán bez zápisu.
assistant: Našiel som dôležitý twist: source checkout sa hlási ako **git/dev flow**, nie normálny stable flow. Ak chceš “normálne updatovať”, lepší cieľ je **global stable-only** a service prepísať na ten aktuálny install. Ešte si len overím, ako bezpečne spustiť doctor bez slepého interaktívneho zásahu.
assistant: Mám cieľový path. Source checkout = dev-style flow, global CLI = stable flow. Ak chceme „normálny update“, správny krok je **prepísať gateway service na current global stable install** cez `openclaw doctor --repair --non-interactive`, potom reštart a verifikácia.
assistant: Doctor potvrdil presne náš drift a prepísal config. Ešte musím overiť, či sa service entrypoint reálne prepol na current install; ak nie, spravím kontrolovaný restart, aby sa nový service stav načítal.
assistant: [[reply_to_current]] Máme to presne chytené.

### Stav po prvom uprataní
- backup je hotový
- doctor našiel drift správne
- ale **service entrypoint sa ešte neprepísal**
- stále ukazuje na:
  - `~/openclaw-main/dist/index.js`
  - verzia v plist stále `2026.3.9`

Čiže:
- mäkký repair prešiel
- **hard normalization ešte nie**

### Prečo
`openclaw doctor --repair --non-interactive` bol opatrný.  
Identifikoval mismatch, ale **neprepísal custom service config bez force zásahu**.

To znamená, že na dokončenie upratania treba už spraviť tvrdší, ale stále kontrolovaný krok:

### Ďalší krok
`openclaw doctor --repair --force --yes`

To je presne ten zásah, ktorý má:
- prepísať gateway service entrypoint na **current install**
- odstrániť split medzi:
  - global stable CLI
  - starým source runtime

### Dopad
- gateway sa môže reštartnúť
- krátky výpadok Control UI
- config backup už máme
- plist backup už máme
- rollback je jednoduchý:
  - obnoviť backup plist
  - restart launch agent

### Môj odporúčaný smer
Aby sa to dalo **normálne updatovať**, teraz by som šiel:
- **global stable-only as canonical runtime**
- source checkout necháme bokom ako repo/worktree, nie ako live gateway service

To je v praxi najčistejší stav.

## Potvrď:
1. **Pokračuj hard normalization**
   - spustím `openclaw doctor --repair --force --yes`
   - potom verify

2. stop, chcem najprv len presný rollback plán

Moja voľba: **1**.
