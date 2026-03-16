# Session: 2026-03-14 20:03:20 UTC

- **Session Key**: agent:main:main
- **Session ID**: 1d16604d-2463-46c1-b50f-08dfe2cf508f
- **Source**: webchat

## Conversation Summary

assistant: [[reply_to_current]] Fixnuté.

Doplnil som:
- `memory/2026-03-13.md`
- `memory/2026-03-14.md`

Prístup:
- **13.3.** som doplnil ako **continuity repair note**, bez vymýšľania fake detailov
- **14.3.** som zapísal normálne ako dnešný operatívny súhrn:
  - cleanup skillov
  - rename na Jarvis
  - doctrine reset
  - OpenClaw doc review
  - operating lessons

To bol správny zásah — deravá daily continuity je presne typ veci, čo potom rozbíja celý systém.

Ak chceš, ďalší okamžitý krok môže byť:
1. **prejsť staršie memory súbory a nájsť ďalšie diery**
alebo
2. **spraviť z daily memory pevný ritual**, aby sa toto neopakovalo.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-14 20:51 GMT+1] /save
assistant: Ukladám dnešný kontext do daily memory, aby continuity neostala len v chate.
assistant: [[reply_to_current]] Uložené.

Zapísal som dnešný kľúčový kontext do `memory/2026-03-14.md`, hlavne:
- posun od experimentovania k agentic operating systemu
- pravidlo postupného skladania blokov
- prioritu real delivery nad meta-workom
- nový Jarvis operating model
- zjednotenie Google Workspace
- zjednodušenie Ironmanu

A malá poznámka:
`/save` route v skilloch je momentálne rozbitý, lebo pôvodný save skill už nie je na aktívnej ceste. Funkčne som to ale spravil ručne správne — context je uložený.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-14 20:55 GMT+1] opravme slash comand skill, cely
assistant: Prepíšem ho celý. Teraz je tam bordel, legacy mapovania a odkazy na skilly, ktoré už ani nemáme. Spravím z neho čistý source-of-truth pre tvoj aktuálny command model.
assistant: Prepíšem `slash-commands` od základov. Vyhodím broken legacy mapovania, nechám len to, čo dnes reálne existuje, a nastavím jasné routing pravidlá.
assistant: [[reply_to_current]] Hotovo.

`slash-commands` som prepísal celý.

Čo som opravil:
- vyhodil som **legacy bordel** a neexistujúce routy
- vyhodil som odkazy na už odstránené skilly:
  - `readme-mgr`
  - `repo-commit`
  - `repo-push`
  - `task-tracker`
  - `habit-tracker`
  - `weather`
  - `things-mac`
  - `singularity-mission-dispatch`
  - staré gmail/calendar wrappery

- nastavil som nový model:
  - `/chat`
  - `/exe`
  - `/system`

- zjednotil som routing na **aktuálne živé skilly**
  - `plan`
  - `fast`
  - `natural20-api-brief`
  - `brave-search`
  - `google-workspace`
  - `crm`
  - `linear`
  - `github`
  - `gifgrep`
  - `morning-brief`
  - `marketing-mode`
  - `business-development`

- doplnil som rozumné správanie pre:
  - `/save`
  - `/brief morning`
  - `/brief evening`
  - `/calendar`
  - `/gog`
  - `/crm`
  - `/linear`
  - `/git`
  - `/github`
  - `/log`
  - basic daily logging commands

- doplnil som zásadu:
  - **slash command = operating intent**
  - nie len text s lomkou

Dôležité:
ten skill je teraz už **čistý a konzistentný s tým, čo v systéme reálne existuje**.

Ak chceš, ďalší krok by mal byť jeden z týchto:
1. **spraviť audit ostatných skillov rovnakým štýlom**  
2. **ísť na OpenClaw config/runtime docs a pretaviť Jarvis model do reálnej konfigurácie**.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-14 20:57 GMT+1] dobre, a este musime upravit TOOL core doc
assistant: Áno. `TOOLS.md` má byť lokálny cheat sheet, nie druhá doktrína. Pozriem ho a upracem, aby sedel na dnešný setup.
assistant: Upravím ho na prísnejší lokálny note file: čo sem patrí, čo sem nepatrí, plus zachovám praktické rescue notes.
assistant: [[reply_to_current]] Hotovo.

`TOOLS.md` som upravil tak, aby bol konečne tým, čím má byť:

- **lokálny cheat sheet**
- nie druhá doktrína
- nie skill spec
- nie memory dump

Čo je tam teraz:
- čo tam **patrí**
  - paths
  - device nicknames
  - auth roots
  - TTS notes
  - local workarounds
- čo tam **nepatrí**
  - politika
  - stratégia
  - identity
  - skill behavior
  - veľké vysvetľovania

Nechal som a doplnil som praktické veci:
- Telegram + voice paths
- runtime workspace path
- Obsidian path
- Google Workspace účty + auth roots
- skill hygiene poznámku

Tým pádom už core doc vrstva drží celkom čisto:

- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `AGENTS.md`
- `MEMORY.md`
- `TOOLS.md`

Najbližší rozumný krok je už podľa mňa:
1. **ísť na OpenClaw config/runtime docs a preložiť toto do reálnej konfigurácie**
alebo
2. **spraviť nový `docs/jarvis-operating-system.md`**, aby sme mali ústavu systému mimo core boot files.
user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Sat 2026-03-14 21:01 GMT+1] /save
assistant: Uložím dnešný ďalší posun do daily memory, nech sa nestratí core-doc cleanup.
assistant: [[reply_to_current]] Uložené.

Doplnil som do dnešnej memory aj:
- rewrite `slash-commands`
- cleanup `TOOLS.md`
- fakt, že core runtime docs sú už zosúladené okolo Jarvisa

Čiže dnešný doctrine reset je už zachytený aj mimo chatu.
