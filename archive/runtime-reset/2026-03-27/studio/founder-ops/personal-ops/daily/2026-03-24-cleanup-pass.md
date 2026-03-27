# Cleanup Pass Packet

- Date: `2026-03-24`
- Owner: `personal-ops`
- Mode: partial execution applied, no outbound send
- Purpose: convert the current personal backlog into reply-ready and cleanup-ready artifacts

## 1. OpenAI billing

### Verified signal
- mail subject: `Please update your Plus payment method`
- state: last payment failed, access is still temporarily active
- action path in the mail: `https://chatgpt.com`

### Recommended move
- update the payment method first before it turns into avoidable tooling friction

## 2. Expandeco

### Decision
- do not proceed with Expandeco collaboration
- remove this thread from the active personal layer queue

### Current handling
- no outbound send prepared anymore
- keep only as historical context unless explicitly reopened later

## 3. Legalia trademark reply draft

### What they need
- closer description of your activity
- optionally official links / website / platforms
- logo if used
- later also billing details for the preliminary search invoice

### Draft

```text
Dobrý deň,

ďakujem za správu.

Moja činnosť je aktuálne zameraná na AI telefónne a agentové služby, najmä návrh a nasadenie AI voice workflowov, inbound call handlingu a súvisiacich automatizácií pre firmy.

Značku `xvadur` plánujem používať ako pracovnú a obchodnú značku pre tieto AI služby a súvisiace digitálne produkty.

Aktuálne oficiálne webové podklady ešte finalizujem, ale viem doplniť aj odkazy a logo, ak je to potrebné pre predbežný prieskum.

Prosím, dajte mi vedieť, či vám na začatie rešerše stačí tento základný popis, prípadne aké doplňujúce informácie odo mňa ešte potrebujete.

Ďakujem,
Adam Rudavský
```

### Decision still needed
- whether this framing is accurate enough
- whether to include live links now
- whether to proceed with the 19 EUR preliminary search

## 4. Reminder cleanup result

### Duplicate follow-up pairs visible now
- `Call Bohuš Dentmax`
  - keep `E05C6159-4D32-458F-9DBC-8A37F8B3CB81` in list `XVADUR`, due `2026-03-09`
  - retire `E1CBA8FC-BCA7-4103-9B29-B71C1250AC08` from legacy list `xvadur`, due `2026-03-10`
- `Call Semafor Dent - Ondrej Užovič`
  - keep `5E995FBE-5B90-4508-95F6-09A06FC3342F` in list `XVADUR`, due `2026-03-11`
  - retire `E00A0062-4634-479C-AB2D-40961DF7F1A0` from legacy list `xvadur`, due `2026-03-12`

### Applied cleanup shape
- `Spraviť demo na AI recepciu` was moved from legacy `xvadur` into `XVADUR`
- legacy duplicate `Call Bohuš Dentmax` in `xvadur` was deleted
- legacy duplicate `Call Semafor Dent - Ondrej Užovič` in `xvadur` was deleted

### Current normalized set
- `Spraviť demo na AI recepciu` in `XVADUR`
- `Call Bohuš Dentmax` in `XVADUR`
- `Call Semafor Dent - Ondrej Užovič` in `XVADUR`

## 5. Best next execution order

1. resolve OpenAI billing manually
2. approve or adjust the Legalia draft
3. reschedule or kill the remaining overdue `XVADUR` reminders based on real priority
