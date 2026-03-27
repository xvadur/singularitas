# Session: 2026-03-22 14:42:52 UTC

- **Session Key**: agent:integration:telegram:direct:1594354152
- **Session ID**: 5ff02238-f635-43b4-b07d-9f9f55b57351
- **Source**: webchat

## Conversation Summary

assistant: [[reply_to_current]] Hotovo — oba sú nainštalované:

- `manychat` → `/Users/_xvadur/singularitas/skills/manychat`
- `content-strategy` → `/Users/_xvadur/singularitas/skills/content-strategy`

Ak chceš, ďalší krok spravím jeden z týchto:
1. **pozriem, čo tie skills reálne vedia**
2. **hneď z nich vytiahnem workflow pre tvoj funnel**
3. **spravím 20-postový plán + ManyChat CTA flow**
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-21 16:40 GMT+1] pozri sa co robia
assistant: [[reply_to_current]] Jasné — pozrel som sa na ne a v skratke:

### `manychat`
Toto je **integračný skill na ManyChat API**, nie stratégia. Vie hlavne:
- pracovať so **subscriberami**
- pridávať/odoberať **tagy**
- čítať/vytvárať **custom fields**
- čítať **flows**
- posielať **správy / flowy** cez ManyChat

Na tvoj use-case je to použiteľné skôr na **technickú vrstvu**:
- označiť ľudí, čo prišli z konkrétneho CTA
- uložiť, ktorý lead magnet pýtali
- spustiť flow
- poslať follow-up správu

Ale dôležité:
- potrebuje **`MATON_API_KEY`**
- funguje cez **Maton gateway**
- z popisu je dosť orientovaný na **Facebook Messenger / ManyChat API**, čiže je to skôr “backend connector” než hotový marketingový playbook

### `content-strategy`
Toto je skôr **playbook / framework**, nie technická integrácia. Pomáha navrhnúť:
- **content goals**
- **audience research**
- **content pillars**
- výber **formátov a kanálov**
- **content calendar**
- **distribution**
- **repurposing**
- **metrics**

Čiže presne na to, čo chceš teraz:
- rozložiť tému AI
- spraviť sériu postov
- zaradiť CTA na komentár
- naviazať to na lead magnet
- postupne prejsť k **voice agentom**

### Môj úprimný záver
- **`content-strategy`** je pre nás užitočný **hneď teraz**
- **`manychat`** bude užitočný až pri **implementácii flowov**
- ani jeden z nich ti sám od seba nespraví hotovú 20-postovú kampaň, ale spolu dávajú dobrý základ:
  - jeden na **stratégiu**
  - druhý na **vykonanie CTA / delivery**

Ak chceš, ďalší krok spravím takto:
1. navrhnem **3–4 content pillars**
2. z nich rozložím **20 postov na 10 dní**
3. ku každému doplním **CTA komentár + čo má ManyChat poslať**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-21 16:48 GMT+1] maton nebudem pouzivat, mozes to odstranit, manychat nam vie dat api ked si zaplatim tier, to nam bude stacit 

podme pouzit ten content strategy skill
assistant: Odstránim ten Maton-based ManyChat skill a hneď potom ti načrtnem stratégiu podľa content-strategy frameworku.
assistant: [[reply_to_current]] Jasné — **ManyChat skill som odstránil**. A áno: ak ti stačí **natívne ManyChat API z plateného tieru**, je to čistejšie než ťahať tam Maton vrstvu.

Začnime teda podľa content-strategy rámca:

## 1. Cieľ kampane
**Primárny cieľ:** získať inbound leady cez komentár + automaticky doručiť PDF/manual  
**Sekundárny cieľ:** vybudovať dôveru a postupne ľudí dostať od „čo je AI“ k „OK, toto chcem vo firme“  
**Tretí cieľ:** prirodzene otvoriť tému **voice agentov**

## 2. Strategická línia
Tvoj obsah by mal ísť v tomto poradí:

1. **Demystifikovať AI**  
   - čo AI je a čo nie je
   - zrušiť strach a chaos

2. **Ukázať praktické používanie**  
   - ako ju používaš ty
   - konkrétne workflowy v ChatGPT

3. **Dať ľuďom rýchle výhry**  
   - PDF manuály
   - ready-to-use prompty
   - mini návody

4. **Posunúť ich k business use-casom**  
   - automatizácia
   - lead handling
   - support
   - booking
   - voice agenti

## 3. Content pillars
Navrhujem 4 piliere:

### Pillar A — AI jednoducho
Obsah pre ľudí, ktorí ešte nemajú pevný mentálny model:
- čo je AI
- čo je ChatGPT
- kde ľudia robia chyby
- prečo to nie je len „hračka“

### Pillar B — Ako AI používam ja
Osobný a dôveryhodný obsah:
- moje workflow
- moje prompty
- čo mi šetrí čas
- kde AI používam denne

### Pillar C — Rýchle výsledky cez ChatGPT
Lead magnet pilier:
- PDF manuály
- prompt packy
- mini checklisty
- návody „sprav to dnes“

### Pillar D — AI v biznise a voice agenti
Postupný posun k tvojej ponuke:
- AI ako asistent
- AI na leady / support / follow-up
- hlasoví agenti
- kedy už nestačí len chat

## 4. CTA mechanika
Keďže chceš komentár-based funnel, držal by som to veľmi jednoducho:

- komentár **MANUAL** → pošli základný PDF
- komentár **PROMPTY** → pošli prompt pack
- komentár **AI** → pošli „AI starter guide“
- komentár **VOICE** → pošli pokročilejší materiál / audit / case

Dôležité:  
**1 post = 1 CTA = 1 asset**  
Nechať to čisté, nech ľudia vedia presne čo majú spraviť.

## 5. Lead magnety
Navrhujem 3 PDFčka:

1. **ChatGPT manuál pre bežné používanie**
   - ako sa pýtať
   - čo od toho čakať
   - 10 jednoduchých use-caseov

2. **20 promptov, ktoré používam v praxi**
   - e-maily
   - sumarizácia
   - brainstorming
   - obsah
   - research

3. **Kedy ti stačí ChatGPT a kedy už potrebuješ AI/voice agenta**
   - veľmi dobrý most k tvojej službe

---

# 20 postov / 10 dní

## Deň 1
**Post 1:** Čo si väčšina ľudí myslí, že AI je — a prečo je to zlé pochopenie  
CTA: koment **AI** a pošlem starter PDF

**Post 2:** 5 vecí, na ktoré používam ChatGPT skoro každý deň  
CTA: koment **PROMPTY**

## Deň 2
**Post 3:** Prečo ľuďom ChatGPT „nefunguje“  
CTA: koment **MANUAL**

**Post 4:** Ako sa správne pýtať AI, aby nevracala balast  
CTA: koment **PROMPTY**

## Deň 3
**Post 5:** 7 praktických úloh, ktoré ti AI vie spraviť dnes  
CTA: koment **AI**

**Post 6:** Môj jednoduchý framework: úloha → kontext → formát → obmedzenia  
CTA: koment **MANUAL**

## Deň 4
**Post 7:** Ako používam ChatGPT na písanie obsahu  
CTA: koment **PROMPTY**

**Post 8:** Ako používam AI na sumarizáciu, výskum a rozhodovanie  
CTA: koment **AI**

## Deň 5
**Post 9:** 3 chyby, kvôli ktorým ľudia AI vzdajú príliš skoro  
CTA: koment **MANUAL**

**Post 10:** Čo by som robil, keby som dnes začínal s AI od nuly  
CTA: koment **AI**

## Deň 6
**Post 11:** ChatGPT nie je kúzelník — je to pracovný nástroj  
CTA: koment **MANUAL**

**Post 12:** 10 promptov, ktoré šetria čas podnikateľovi  
CTA: koment **PROMPTY**

## Deň 7
**Post 13:** Kde AI fakt pomáha vo firme a kde je to zatiaľ zbytočné  
CTA: koment **AI**

**Post 14:** Ako si viem s AI pripraviť e-maily, ponuky a follow-upy  
CTA: koment **PROMPTY**

## Deň 8
**Post 15:** Keď už nechceš len chatovať: AI ako pracovný systém  
CTA: koment **MANUAL**

**Post 16:** Rozdiel medzi ChatGPT, automatizáciou a AI agentom  
CTA: koment **AI**

## Deň 9
**Post 17:** Čo je voice agent a prečo to nie je len „AI s hlasom“  
CTA: koment **VOICE**

**Post 18:** Kde voice agent dáva biznisovo najväčší zmysel  
CTA: koment **VOICE**

## Deň 10
**Post 19:** Kedy ti stačí ChatGPT a kedy už potrebuješ voice agenta  
CTA: koment **VOICE**

**Post 20:** Ako by vyzeral voice agent v praxi u teba vo firme  
CTA: koment **VOICE** alebo **AUDIT**

---

## 6. Odporúčaný prechod k ponuke
Aby to nepôsobilo ako náhly predajný skok, prechod nech je:

- najprv **AI vysvetľujem**
- potom **ukazujem, ako ju používam**
- potom **dávam návody**
- potom **ukazujem limity samotného chatu**
- a až potom:
  **„Keď chceš, aby AI nielen odpovedala, ale aj reálne vybavovala hovory, leady alebo support, tam nastupujú voice agenti.“**

## 7. Čo by som spravil ako ďalší krok
Navrhujem toto poradie:
1. vybrať **3 lead magnety**
2. určiť **4 komentárové keywords**
3. dopísať ku každému z 20 postov:
   - hook
   - hlavný message
   - CTA
   - čo ManyChat pošle

Ak chceš, v ďalšej správe ti to rovno rozpracujem do **presného 20-postového kalendára s caption outline ku každému postu**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-21 16:52 GMT+1] podme sa zamysliet nad strategiou pred draftmi prispevkov, 
ako mozeme pouzit skill?
assistant: [[reply_to_current]] Áno — presne takto by som k tomu pristúpil: **skill nepoužiť na písanie postov, ale na navrhnutie rozhodnutí predtým**, než začneme písať.

### Ako ten `content-strategy` skill reálne použiť
On je v zásade **strategický framework**, nie „generator captionov“. Čiže ho vieme použiť ako pracovnú osnovu v tomto poradí:

1. **Goal**
   - čo má obsah spraviť:
   - awareness?
   - komentáre?
   - DM/conversion do ManyChatu?
   - call booking?
   - predaj voice agentov?

2. **Audience needs**
   - čo si tvoje publikum dnes myslí o AI
   - čoho sa bojí
   - čo chce prakticky dosiahnuť
   - aké otázky sa opakujú

3. **Content pillars**
   - 3–5 stabilných tematických okruhov
   - aby sme nepostovali random veci

4. **Formats + channels**
   - aký typ postov ideme robiť
   - či to je skôr edukačný text, osobná skúsenosť, mini case, myth-busting, checklist

5. **Calendar**
   - až potom rozložiť 20 postov / 10 dní

6. **Distribution**
   - čo sa stane po poste
   - komentár → ManyChat → asset → follow-up → ďalší krok

7. **Metrics**
   - čo budeme považovať za úspech:
   - počet komentov?
   - opt-in rate do flowu?
   - otvorenie PDF?
   - reply rate?
   - záujem o voice audit?

---

## Ako by som to použil konkrétne na tvoj prípad

Namiesto otázky **„aké posty ideme písať?“** si najprv zodpovieme:

### 1. Aký je skutočný biznisový cieľ?
Možnosti:
- **A:** vybudovať publiku dôveru okolo AI
- **B:** nazbierať leady cez komentáre a ManyChat
- **C:** dostať ľudí do pipeline na voice agentov

Môj odhad:  
**hlavný cieľ = leads + trust**,  
nie čistý reach.

---

### 2. Aká je transformácia publika?
Toto je podľa mňa kľúčové.

Dnes sú ľudia asi niekde tu:
- „AI je hype“
- „ChatGPT som skúsil, ale nič moc“
- „Neviem, na čo by mi to bolo“
- „Voice agent znie sci-fi“

A ty ich chceš dostať sem:
- „Aha, AI viem použiť hneď“
- „Toto mi šetrí čas“
- „Chcem tie návody/prompty“
- „OK, toto už má biznisový dopad“
- „Voice agenti sú reálny nástroj, nie gimmick“

Čiže stratégia nemá byť len obsahová — má byť aj **posun vo vnímaní**.

---

### 3. Aké content piliere zodpovedajú tejto transformácii?
Skill by nás viedol k pillarom. Pre teba by som ich skúsil definovať nie len tematicky, ale aj psychologicky:

#### Pillar 1 — AI bez chaosu
Cieľ: odstrániť zmätok a odpor  
Obsah:
- čo AI je / nie je
- najčastejšie mýty
- čo od nej čakať realisticky

#### Pillar 2 — Ako ju používam ja
Cieľ: dôvera + konkrétnosť  
Obsah:
- tvoje workflow
- tvoje use-cases
- osobné „takto to robím“

#### Pillar 3 — Rýchle výhry pre človeka/firmu
Cieľ: akcia  
Obsah:
- prompty
- mini návody
- PDFká
- checklisty

#### Pillar 4 — AI systémy a voice agenti
Cieľ: posun k ponuke  
Obsah:
- rozdiel medzi chatbotom, automatizáciou a agentom
- kde voice agent dáva ROI
- praktické business use-cases

---

### 4. Ako skill použiť na funnel, nie len na content
Toto je dôležité: my ten skill môžeme použiť ako **funnel design tool**.

Každý content pillar musí mať:
- **dominantný uhol**
- **CTA**
- **asset**
- **ďalší krok**

Príklad:

| Pillar | Čo má človek cítiť | CTA | Asset | Next step |
|---|---|---|---|---|
| AI bez chaosu | „už tomu rozumiem“ | koment AI | starter guide | follow-up s ďalším tipom |
| Ako ju používam ja | „chcem tvoje workflow“ | koment PROMPTY | prompt pack | otázka na use-case |
| Rýchle výhry | „idem to skúsiť dnes“ | koment MANUAL | PDF návod | segmentácia podľa záujmu |
| Voice agenti | „toto už je pre biznis vážne“ | koment VOICE | explainer/case | audit / call |

Čiže skill nám pomáha nielen s témami, ale aj s **obsahovou architektúrou funnelu**.

---

## Čo by sme mali rozhodnúť ešte pred draftmi
Ak chceme skill použiť dobre, pred písaním by sme mali uzavrieť týchto 6 vecí:

1. **Primárne publikum**
   - podnikatelia?
   - SMB firmy?
   - marketéri?
   - realitáci?
   - lokálne služby?

2. **Primárny promise**
   - AI ti šetrí čas?
   - AI ti zarába peniaze?
   - AI ti zjednoduší prácu?
   - AI ti vybaví komunikáciu?

3. **Entry point**
   - začíname cez ChatGPT basics
   - alebo cez „ako to používam ja“
   - alebo cez „3 veci, kde AI reálne funguje“

4. **Lead magnet stack**
   - aké presne 2–3 assety budeme rozdávať

5. **ManyChat logic**
   - jeden keyword pre všetko?
   - alebo viac keywordov podľa intentu?
   - budeme segmentovať ľudí na:
     - začiatočník
     - praktické použitie
     - biznis/voice?

6. **Offer bridge**
   - čo je prvý komerčný krok po obsahu:
   - audit?
   - konzultácia?
   - demo voice agenta?
   - „napíš mi a ukážem ti use-case“?

---

## Môj návrh: takto skill použime v 3 fázach

### Fáza 1 — Strategy decisions
Najprv spolu určíme:
- audience
- promise
- pillars
- funnel
- KPI

### Fáza 2 — Asset architecture
Potom navrhneme:
- PDF 1
- PDF 2
- PDF 3
- ManyChat keywords
- follow-up sekvencie

### Fáza 3 — Content calendar
Až potom:
- 20 postov
- poradie tém
- CTA mapovanie
- postupný prechod k voice agentom

---

## Za mňa je teraz správna otázka
Nie:
- „aké posty ideme písať?“

Ale:
- **„akú zmenu v hlave človeka chceme za tých 10 dní urobiť — a aký funnel to má podporiť?“**

Ak chceš, poďme teraz spraviť **strategický worksheet podľa skillu** a uzavrieme iba tieto body:
1. audience  
2. promise  
3. pillars  
4. CTA/lead magnets  
5. bridge k voice agentom.  

Môžem ti to hneď viesť otázka-po-otázke.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-21 21:50 GMT+1] ked ti poslem instagram video vedel by si ho spracovat?
assistant: [[reply_to_current]] Áno — ak mi pošleš **IG video link** alebo ešte lepšie **stiahnutý súbor**, viem ho spracovať.  

Viem z toho spraviť napríklad:
- **prepis / zhrnutie**
- vytiahnuť **hlavnú pointu, hooky a CTA**
- prerobiť to na **post, carousel, script, PDF osnovu**
- povedať, **kam to patrí v content stratégii**

Ak je video **private / ťažko dostupné cez link**, pošli radšej súbor. A napíš aj, čo presne chceš: **sumár, transcript, analýzu, alebo prerobiť na obsah**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-21 21:52 GMT+1] https://www.instagram.com/reel/DUN2CkWjwbw/?igsh=emk3YzVicjZuOG50
assistant: Skúsim z toho vytiahnuť aspoň zhrnutie a použiteľný obsah. Ak Instagram nepustí text/video metadata, poviem ti presne čo ďalej.
assistant: [[reply_to_current]] Áno, ale **z tohto IG linku som vytiahol len veľmi obmedzené metadata** — prakticky len to, že je to reel od **Callum Carver** s captionom **“An absolute fu*king masterclass for you 🙂↕️”**. Instagram mi z linku nevrátil použiteľný **obsah videa ani transcript**, takže na poriadne spracovanie to nestačí.

Najlepšie bude, ak mi pošleš jedno z tohto:
- **MP4 súbor videa**
- alebo **screen recording / stiahnuté video**
- prípadne aspoň **caption + screenshoty hlavných scén**

Potom ti z toho viem spraviť:
- **presný sumár / transcript**
- **rozbor hooku, štruktúry a CTA**
- **prepis do vlastného postu/reelu**
- a zaradiť to do tvojej **content stratégie**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-21 21:54 GMT+1] okej tak nic, idem ti prepisat co sa tam hovori
assistant: [[reply_to_current]] Super, to bude úplne stačiť. Pošli mi pokojne:
- **presný prepis**, ak sa ti chce
- alebo len **body / približný obsah**
- ideálne aj:
  - **ako začína hook**
  - **hlavnú pointu**
  - **CTA na konci**

A ja z toho potom spravím buď:
- **analýzu videa**
- **zaradenie do stratégie**
- alebo to prerobím na **vlastný content angle**.
