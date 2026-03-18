# Watchlist

## Immediate blockers

- SIP vendor compatibility call pending
  - Owner: `integration`
  - Next move: call Slovak SIP vendors and record trunk/auth/TLS answers in this project home
- Vapi credential visibility not confirmed
  - Owner: `voice`
  - Next move: confirm whether Vapi is the primary voice path or whether ElevenLabs remains the default until Vapi is provisioned
- CRM DB missing
  - Owner: `revenue`
  - Next move: restore the local CRM source or replace it with a temporary manual callback ledger
- n8n health not yet connected to the engine
  - Owner: `integration`
  - Next move: attach a local automation-state note or explicitly keep callback work in manual mode

## Deployment risks

- callback flow can still drift into theory if not packetized
- follow-up promises can get ahead of actual implementation
- expansion layers can cannibalize the narrow pilot if not gated

## Tomorrow checks

- confirm SIP capabilities with vendor
- confirm which voice stack path is primary: `Vapi first` or `ElevenLabs first`
- confirm whether callback destination is CRM, calendar, or manual handoff first
