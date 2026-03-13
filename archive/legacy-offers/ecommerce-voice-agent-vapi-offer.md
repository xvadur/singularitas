# E-shop Voice Agent — Vapi Pilot Draft

## Cieľ
Navrhnúť hlasového agenta pre e-shop, ktorý odbremení support, zrýchli odpovede zákazníkom a zachytí požiadavky 24/7 cez telefón.

## Čo agent rieši v pilote
- FAQ o doprave, platbe, reklamáciách, vrátení tovaru
- stav objednávky po overení zákazníka
- zachytenie problému a odovzdanie na support
- základná orientácia v nákupe a objednávke
- zber leadu alebo kontaktu pri nevybavenom dopyte
- handoff na človeka pri zložitejších prípadoch

## Čo zatiaľ nerieši
- voľné improvizované zásahy do objednávok bez pravidiel
- refundy bez schváleného workflowu
- zmeny objednávok bez overenia identity
- zložité produktové poradenstvo bez znalostnej bázy
- účtovné alebo právne rozhodnutia

## Hlavné scenáre volania

### 1. Stav objednávky
Agent:
- vypýta číslo objednávky alebo email/telefón
- overí zákazníka
- zavolá workflow na zistenie stavu
- stručne oznámi výsledok
- ak treba, ponúkne spojenie na support

### 2. Doprava / platba / vrátenie
Agent:
- odpovie podľa FAQ a pravidiel e-shopu
- ak si nie je istý, eskaluje na človeka
- nevymýšľa si pravidlá

### 3. Reklamácia alebo problém s objednávkou
Agent:
- zachytí typ problému
- získa identifikáciu objednávky
- získa stručný popis problému
- vytvorí support ticket / odovzdá kontakt
- oznámi ďalší krok

### 4. Predpredajná otázka
Agent:
- zistí, čo zákazník hľadá
- ak existuje znalostná báza, odpovie
- ak nie, zachytí dopyt a odovzdá ho tímu

### 5. Handoff na človeka
Trigger:
- zákazník chce človeka
- problém je mimo scope
- workflow zlyhá
- overenie objednávky zlyhá
- otázka je citlivá alebo konfliktná

## Doporučený pilot scope
Prvý pilot má byť úzky a bezpečný.

### Pilot v1
- inbound calls
- FAQ
- order status
- support intake
- human handoff

### Pilot v2
- follow-up po objednávke
- review request
- outbound reminder / check-in
- jednoduché post-purchase flows

## Vapi architektúra
- **Vapi**: runtime agenta, prompt, call flow, tools
- **ElevenLabs**: voice layer podľa potreby
- **n8n**: lookup objednávky, ticketing, CRM/helpdesk, notifikácie

## Potrebné tools pre Vapi
Minimum:
- `get_order_status`
- `create_support_ticket`
- `handoff_to_human`
- `log_customer_request`

Voliteľné podľa integrácie:
- `lookup_customer`
- `list_return_policy`
- `send_followup_sms_or_email`

## Návrh systémového promptu

```text
Si virtuálny hlasový asistent pre e-shop.
Komunikuj po slovensky a vykaj.
Buď stručný, pokojný a praktický.
Pýtaj sa vždy iba jednu otázku naraz.

Tvoj cieľ:
- odpovedať na bežné support otázky
- pomôcť so zistením stavu objednávky
- zachytiť problém zákazníka
- odovzdať zložité prípady na človeka

Pravidlá:
- nikdy si nevymýšľaj informácie o objednávke, doprave alebo reklamácii
- ak nemáš potvrdené dáta z toolu, povedz to priamo
- pri stave objednávky najprv over zákazníka
- pri citlivom alebo konfliktnom prípade ponúkni spojenie na človeka
- ak tool zlyhá, ospravedlň sa a zachyť kontakt na spätné vybavenie
- nepodávaj právne ani účtovné interpretácie
- nepovoľuj zmenu objednávky bez definovaného workflowu

Hlavné scenáre:
1. FAQ
2. Stav objednávky
3. Reklamácia / problém
4. Predpredajná otázka
5. Handoff na support

Na konci stručne zhrň, čo sa vyriešilo a aký je ďalší krok.
```

## Voice a štýl
Odporúčanie:
- profesionálny, príjemný, rýchly hlas
- krátke vety
- bez AI slopu
- support-first, nie sales-first

## QA checklist
Pred go-live otestovať minimálne:
- objednávka nájdená
- objednávka nenájdená
- zákazník nevie číslo objednávky
- FAQ o doprave
- FAQ o vrátení tovaru
- reklamácia s handoffom
- zákazník chce človeka okamžite
- tool timeout / error
- nerozpoznaný vstup
- ukončenie hovoru po vyriešení

## Output package pre klienta
- stručný opis use case
- čo agent pokrýva a čo nie
- pilot scope
- integračné požiadavky
- ukážka call flow
- očakávaný prínos

## Očakávaný prínos
- menej opakujúcich sa support hovorov
- rýchlejšia prvá odpoveď
- 24/7 zachytenie dopytu
- menej stratených zákazníckych požiadaviek
- lepší handoff na tím

## Čo potrebujeme doplniť od klienta
- typ e-shopu
- najčastejšie typy otázok
- pravidlá dopravy / platieb / vrátenia
- zdroj objednávkových dát
- support email / helpdesk / CRM
- pravidlá eskalácie na človeka
- jazyk a tone of voice
