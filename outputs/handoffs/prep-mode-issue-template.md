# Symphony - Issue Template for Prep Mode

## Purpose

Toto je sablona pre `Linear` issue, ktore maju byt spracovane cez `Symphony` v aktualnom `prep` mode.

Tato sablona je vhodna, ked chcem:

- rozsekat vacsiu temu
- pripravit execution packet
- definovat scope a output
- dat `OpenClaw` reviewable handoff

Nie je to sablona pre plne autonomne vykonanie celej prace.

## Copy Paste Template

```md
## Goal

<Co je ciel tohto issue v jednej jasnej vete?>

## Why This Matters

<Preco je to dolezite teraz? Na aku prioritu alebo operacny ciel to nadvazuje?>

## Scope

- <Co ma byt zahrnute>
- <Co ma byt zahrnute>
- <Co ma byt zahrnute>

## Out Of Scope

- <Co agent nema riesit>
- <Co agent nema riesit>

## Expected Output

- <Aký konkretny artefakt alebo packet ma vzniknut>
- <Co ma mat hotove na konci>

## Definition Of Done

- <Ako vieme, ze je task dost dobre pripraveny?>
- <Co musi byt explicitne pomenovane?>
- <Co musi byt rozsekane alebo zdokumentovane?>

## Available Context

- <Linky, docs, notes, issue references, folders, repo paths>
- <Co uz existuje a ma sa pouzit>

## Constraints

- <Na co si ma agent davat pozor>
- <Co nemoze menit alebo vykonavat>

## Open Questions

- <Ak existuju nezname, daj ich sem radsej hned>
```

## What A Good Prep Issue Produces

Dobry `prep` issue by mal viest k tomu, ze Codex pripravi:

- `execution-prep.md`
- `subtasks.md`
- `status.md`

Z tychto vystupov ma byt jasne:

- co sa ide robit
- co sa robit nema
- co chyba
- ako sa to ma rozdelit na dalsie execution issues

## Fast Rules

Pouzi tuto sablonu, ked:

- tema je vacsia ako jeden task
- treba rozdelit pracu
- chyba presny execution shape
- chces reviewable packet pre `OpenClaw`

Nepouzivaj ju, ked:

- uz vies presne, aky konkretny single execution task treba spravit
- task je maly a ma jednoznacny output
- ide len o jednoduchu operacnu akciu bez potreby decomposition

## Example 1: Agent Lane Setup

```md
## Goal

Priprav execution packet pre CRO lane v Symphony/OpenClaw operating modeli.

## Why This Matters

CRO lane je jedna z prvych prioritnych operacnych liniek a potrebujeme ju dostat z abstraktnej idey do vykonatelnej podoby.

## Scope

- definovat rolu CRO
- urcit skills
- urcit read context
- urcit output contract
- navrhnut execution slices

## Out Of Scope

- implementacia runtime
- zmeny v produkcnom kode
- vytvaranie Linear child issues

## Expected Output

- execution packet pre CRO lane
- rozsekane subtasky pre dalsi execution krok

## Definition Of Done

- CRO lane ma explicitny contract
- su pomenovane blockers
- su navrhnute dalsie execution issues

## Available Context

- parent issue pre agent setup
- aktualny Symphony workflow
- existujuce agent notes v Obsidiane

## Constraints

- bez mutacii mimo workspace
- bez repo implementacie

## Open Questions

- kde bude finalne ulozena definicia lane
- aky format bude canonical pre skill contract
```

## Example 2: Outreach Strategy Prep

```md
## Goal

Priprav execution packet pre outbound angles pre CFO segment.

## Why This Matters

Potrebujeme rychlo pripravit kvalitny outbound smer bez toho, aby sa hned pisali finalne kampane.

## Scope

- navrhnut 4 outbound angles
- pomenovat ICP pains
- urcit hooks a CTA smer
- rozdelit pracu na dalsie execution slices

## Out Of Scope

- pisanie finalnych mailov
- odosielanie outreachu
- CRM mutacie

## Expected Output

- packet s decomposition pre outreach execution

## Definition Of Done

- angles su jasne oddelene
- su pomenovane vstupy a blockers
- OpenClaw z toho vie vytvorit dalsie tasky

## Available Context

- messaging docs
- offers docs
- audience notes

## Constraints

- bez external execution
- bez publikovania

## Open Questions

- ktory audience segment ma prioritu
- ci sa ma pouzit existujuci offer alebo novy angle
```

## Operator Recommendation

Ak si nie si isty, ci mas vytvorit parent issue alebo execution issue:

- parent issue pouzi, ked treba decomposition
- execution issue pouzi, ked uz vies presny output

Ked vahas, zacni parent `prep` issue a nechaj Codex rozsekat pracu.
