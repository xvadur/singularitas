# Natural20 Event Continuity

- Surface: `natural20-event-continuity`
- Owner: `research`
- State: `durable`
- Last updated: `2026-03-27 17:16 CET / 2026-03-27 16:16 UTC`
- Source of updates: Natural20 feed + script state
- Contract: script-written by `skills/natural20-api-brief/scripts/n20_ingest.py`
- Purpose: preserve major recurring story continuity across the day so Jarvis can answer event-specific questions from stored state.

## Matching contract

1. exact URL match keeps the prior event key
2. else exact normalized title keeps the prior event key
3. else informative-title token overlap ≥ 0.60 with at least 2 shared tokens keeps the prior event key
4. else a new event key is created from the title-token slug

## Tracked events

### 1) `anthropic-quarter-discusses-going-fourth`
- Status: `active`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 01:13 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `11`
- Latest title: Anthropic Discusses Going Public as Soon as the Fourth Quarter
- Latest known position: `#10` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 04:13 CET` — #5 — continuation; holds #5
  - `2026-03-27 05:13 CET` — #5 — continuation; holds #5
  - `2026-03-27 06:19 CET` — #5 — continuation; holds #5
  - `2026-03-27 07:19 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-27 14:16 CET` — #7 — continuation; rank down #6 → #7
  - `2026-03-27 15:16 CET` — #7 — continuation; holds #7
  - `2026-03-27 16:16 CET` — #7 — continuation; holds #7
  - `2026-03-27 17:16 CET` — #10 — continuation; rank down #7 → #10

### 2) `temporarily-anthropic-block-pentagon-sides`
- Status: `active`
- Theme: `data-center-politics`
- First seen: `2026-03-27 02:13 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `10`
- Latest title: Judge sides with Anthropic to temporarily block the Pentagon’s ban
- Latest known position: `#6` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 04:13 CET` — #2 — continuation; holds #2
  - `2026-03-27 05:13 CET` — #2 — continuation; holds #2
  - `2026-03-27 06:19 CET` — #2 — continuation; holds #2
  - `2026-03-27 07:19 CET` — #2 — continuation; holds #2
  - `2026-03-27 14:16 CET` — #3 — continuation; rank down #2 → #3
  - `2026-03-27 15:16 CET` — #3 — continuation; holds #3
  - `2026-03-27 16:16 CET` — #3 — continuation; holds #3
  - `2026-03-27 17:16 CET` — #6 — continuation; rank down #3 → #6

### 3) `personal-information-gemini-can-chats`
- Status: `active`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 02:13 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `10`
- Latest title: You can now transfer your chats and personal information from other chatbots directly into Gemini
- Latest known position: `#7` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 04:13 CET` — #3 — continuation; holds #3
  - `2026-03-27 05:13 CET` — #3 — continuation; holds #3
  - `2026-03-27 06:19 CET` — #3 — continuation; holds #3
  - `2026-03-27 07:19 CET` — #3 — continuation; holds #3
  - `2026-03-27 14:16 CET` — #4 — continuation; rank down #3 → #4
  - `2026-03-27 15:16 CET` — #4 — continuation; holds #4
  - `2026-03-27 16:16 CET` — #4 — continuation; holds #4
  - `2026-03-27 17:16 CET` — #7 — continuation; rank down #4 → #7

### 4) `crypto-white-david-longer-house`
- Status: `active`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 02:13 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `15`
- Latest title: David Sacks Leaves White House AI and Crypto Czar Role
- Latest known position: `#9` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 14:16 CET` — #5 — continuation; holds #5
  - `2026-03-27 14:16 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-27 15:16 CET` — #5 — continuation; rank up #6 → #5
  - `2026-03-27 15:16 CET` — #6 — continuation; holds #6
  - `2026-03-27 16:16 CET` — #5 — continuation; rank up #6 → #5
  - `2026-03-27 16:16 CET` — #6 — continuation; holds #6
  - `2026-03-27 17:16 CET` — #8 — continuation; rank down #6 → #8
  - `2026-03-27 17:16 CET` — #9 — continuation; rank down #6 → #9

### 5) `injunction-against-department-wins-administration`
- Status: `active`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 03:13 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `9`
- Latest title: Anthropic wins injunction against Trump administration over Defense Department saga
- Latest known position: `#5` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 04:13 CET` — #1 — continuation; holds #1
  - `2026-03-27 05:13 CET` — #1 — continuation; holds #1
  - `2026-03-27 06:19 CET` — #1 — continuation; holds #1
  - `2026-03-27 07:19 CET` — #1 — continuation; holds #1
  - `2026-03-27 14:16 CET` — #2 — continuation; rank down #1 → #2
  - `2026-03-27 15:16 CET` — #2 — continuation; holds #2
  - `2026-03-27 16:16 CET` — #2 — continuation; holds #2
  - `2026-03-27 17:16 CET` — #5 — continuation; rank down #2 → #5

### 6) `anthropic-mythos-advanced-discusses-claude`
- Status: `active`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 14:16 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `4`
- Latest title: Anthropic Discusses Q4 IPO, Preps ‘Claude Mythos’ Advanced AI
- Latest known position: `#3` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 14:16 CET` — #1 — new story
  - `2026-03-27 15:16 CET` — #1 — continuation; holds #1
  - `2026-03-27 16:16 CET` — #1 — continuation; holds #1
  - `2026-03-27 17:16 CET` — #3 — continuation; rank down #1 → #3

### 7) `vcs-openai-billions-sora-betting`
- Status: `active`
- Theme: `data-center-politics`
- First seen: `2026-03-27 17:16 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `1`
- Latest title: VCs are betting billions on AI’s next wave, so why is OpenAI killing Sora?
- Latest known position: `#1` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 17:16 CET` — #1 — new story

### 8) `court-down-shuts-out-sora`
- Status: `active`
- Theme: `data-center-politics`
- First seen: `2026-03-27 17:16 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `1`
- Latest title: OpenAI shuts down Sora while Meta gets shut out in court
- Latest known position: `#2` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 17:16 CET` — #2 — new story

### 9) `doing-here-instead-done-sacks`
- Status: `active`
- Theme: `data-center-politics`
- First seen: `2026-03-27 17:16 CET`
- Last seen: `2026-03-27 17:16 CET`
- Appearances in top 10: `1`
- Latest title: David Sacks is done as AI czar — here’s what he’s doing instead
- Latest known position: `#4` at `2026-03-27 17:16 CET`
- Timeline:
  - `2026-03-27 17:16 CET` — #4 — new story

### 10) `wikipedia-down-article-cracks-use`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 00:13 CET`
- Last seen: `2026-03-27 16:16 CET`
- Appearances in top 10: `11`
- Latest title: Wikipedia cracks down on the use of AI in article writing
- Latest known position: `#8` at `2026-03-27 16:16 CET`
- Timeline:
  - `2026-03-27 03:13 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-27 04:13 CET` — #6 — continuation; holds #6
  - `2026-03-27 05:13 CET` — #6 — continuation; holds #6
  - `2026-03-27 06:19 CET` — #6 — continuation; holds #6
  - `2026-03-27 07:19 CET` — #7 — continuation; rank down #6 → #7
  - `2026-03-27 14:16 CET` — #8 — continuation; rank down #7 → #8
  - `2026-03-27 15:16 CET` — #8 — continuation; holds #8
  - `2026-03-27 16:16 CET` — #8 — continuation; holds #8

### 11) `import-google-memory-making-gemini`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 00:13 CET`
- Last seen: `2026-03-27 16:16 CET`
- Appearances in top 10: `11`
- Latest title: Google is making it easier to import another AI’s memory into Gemini
- Latest known position: `#9` at `2026-03-27 16:16 CET`
- Timeline:
  - `2026-03-27 03:13 CET` — #7 — continuation; rank down #6 → #7
  - `2026-03-27 04:13 CET` — #7 — continuation; holds #7
  - `2026-03-27 05:13 CET` — #7 — continuation; holds #7
  - `2026-03-27 06:19 CET` — #7 — continuation; holds #7
  - `2026-03-27 07:19 CET` — #8 — continuation; rank down #7 → #8
  - `2026-03-27 14:16 CET` — #9 — continuation; rank down #8 → #9
  - `2026-03-27 15:16 CET` — #9 — continuation; holds #9
  - `2026-03-27 16:16 CET` — #9 — continuation; holds #9

### 12) `reportedly-siri-plug-allow-other`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 00:13 CET`
- Last seen: `2026-03-27 16:16 CET`
- Appearances in top 10: `11`
- Latest title: Apple will reportedly allow other AI chatbots to plug into Siri
- Latest known position: `#10` at `2026-03-27 16:16 CET`
- Timeline:
  - `2026-03-27 03:13 CET` — #8 — continuation; rank down #7 → #8
  - `2026-03-27 04:13 CET` — #8 — continuation; holds #8
  - `2026-03-27 05:13 CET` — #8 — continuation; holds #8
  - `2026-03-27 06:19 CET` — #8 — continuation; holds #8
  - `2026-03-27 07:19 CET` — #9 — continuation; rank down #8 → #9
  - `2026-03-27 14:16 CET` — #10 — continuation; rank down #9 → #10
  - `2026-03-27 15:16 CET` — #10 — continuation; holds #10
  - `2026-03-27 16:16 CET` — #10 — continuation; holds #10

### 13) `playground-playlist-apple-bad-music`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-26 23:13 CET`
- Last seen: `2026-03-27 07:19 CET`
- Appearances in top 10: `9`
- Latest title: Apple’s AI Playlist Playground is bad at music
- Latest known position: `#10` at `2026-03-27 07:19 CET`
- Timeline:
  - `2026-03-27 00:13 CET` — #4 — continuation; rank down #1 → #4
  - `2026-03-27 01:13 CET` — #5 — continuation; rank down #4 → #5
  - `2026-03-27 02:13 CET` — #8 — continuation; rank down #5 → #8
  - `2026-03-27 03:13 CET` — #9 — continuation; rank down #8 → #9
  - `2026-03-27 04:13 CET` — #9 — continuation; holds #9
  - `2026-03-27 05:13 CET` — #9 — continuation; holds #9
  - `2026-03-27 06:19 CET` — #9 — continuation; holds #9
  - `2026-03-27 07:19 CET` — #10 — continuation; rank down #9 → #10

### 14) `ads-million-revenue-pilot-surpasses`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-27 00:13 CET`
- Last seen: `2026-03-27 06:19 CET`
- Appearances in top 10: `7`
- Latest title: OpenAI Surpasses $100 Million Annualized Revenue From Ads Pilot
- Latest known position: `#10` at `2026-03-27 06:19 CET`
- Timeline:
  - `2026-03-27 00:13 CET` — #5 — new story
  - `2026-03-27 01:13 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-27 02:13 CET` — #9 — continuation; rank down #6 → #9
  - `2026-03-27 03:13 CET` — #10 — continuation; rank down #9 → #10
  - `2026-03-27 04:13 CET` — #10 — continuation; holds #10
  - `2026-03-27 05:13 CET` — #10 — continuation; holds #10
  - `2026-03-27 06:19 CET` — #10 — continuation; holds #10

### 15) `more-languages-assistant-handle-search`
- Status: `inactive`
- Theme: `audio-model-race`
- First seen: `2026-03-26 21:13 CET`
- Last seen: `2026-03-27 02:13 CET`
- Appearances in top 10: `6`
- Latest title: Google’s ‘live’ AI search assistant can handle conversations in dozens more languages
- Latest known position: `#10` at `2026-03-27 02:13 CET`
- Timeline:
  - `2026-03-26 21:13 CET` — #1 — new story
  - `2026-03-26 22:13 CET` — #1 — continuation; holds #1
  - `2026-03-26 23:13 CET` — #2 — continuation; rank down #1 → #2
  - `2026-03-27 00:13 CET` — #6 — continuation; rank down #2 → #6
  - `2026-03-27 01:13 CET` — #7 — continuation; rank down #6 → #7
  - `2026-03-27 02:13 CET` — #10 — continuation; rank down #7 → #10

### 16) `data-power-see-your-bills`
- Status: `inactive`
- Theme: `data-center-politics`
- First seen: `2026-03-26 20:13 CET`
- Last seen: `2026-03-27 01:13 CET`
- Appearances in top 10: `6`
- Latest title: Data centers get ready — the Senate wants to see your power bills
- Latest known position: `#9` at `2026-03-27 01:13 CET`
- Timeline:
  - `2026-03-26 20:13 CET` — #1 — new story
  - `2026-03-26 21:13 CET` — #3 — continuation; rank down #1 → #3
  - `2026-03-26 22:13 CET` — #3 — continuation; holds #3
  - `2026-03-26 23:13 CET` — #4 — continuation; rank down #3 → #4
  - `2026-03-27 00:13 CET` — #8 — continuation; rank down #4 → #8
  - `2026-03-27 01:13 CET` — #9 — continuation; rank down #8 → #9

### 17) `erotic-another-chatgpt-yet-openai`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-26 21:13 CET`
- Last seen: `2026-03-27 01:13 CET`
- Appearances in top 10: `5`
- Latest title: OpenAI abandons yet another side quest: ChatGPT’s erotic mode
- Latest known position: `#8` at `2026-03-27 01:13 CET`
- Timeline:
  - `2026-03-26 21:13 CET` — #2 — new story
  - `2026-03-26 22:13 CET` — #2 — continuation; holds #2
  - `2026-03-26 23:13 CET` — #3 — continuation; rank down #2 → #3
  - `2026-03-27 00:13 CET` — #7 — continuation; rank down #3 → #7
  - `2026-03-27 01:13 CET` — #8 — continuation; rank down #7 → #8

### 18) `hiring-cloud-sales-groups-freezes`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-26 22:13 CET`
- Last seen: `2026-03-27 01:13 CET`
- Appearances in top 10: `4`
- Latest title: Microsoft Freezes Hiring in Major Cloud and Sales Groups
- Latest known position: `#10` at `2026-03-27 01:13 CET`
- Timeline:
  - `2026-03-26 22:13 CET` — #4 — new story
  - `2026-03-26 23:13 CET` — #5 — continuation; rank down #4 → #5
  - `2026-03-27 00:13 CET` — #9 — continuation; rank down #5 → #9
  - `2026-03-27 01:13 CET` — #10 — continuation; rank down #9 → #10

### 19) `ban-launch-ray-ready-glasses`
- Status: `inactive`
- Theme: `data-center-politics`
- First seen: `2026-03-26 19:13 CET`
- Last seen: `2026-03-27 00:13 CET`
- Appearances in top 10: `6`
- Latest title: Meta gets ready to launch two new Ray-Ban AI glasses
- Latest known position: `#10` at `2026-03-27 00:13 CET`
- Timeline:
  - `2026-03-26 19:13 CET` — #1 — new story
  - `2026-03-26 20:13 CET` — #2 — continuation; rank down #1 → #2
  - `2026-03-26 21:13 CET` — #4 — continuation; rank down #2 → #4
  - `2026-03-26 22:13 CET` — #5 — continuation; rank down #4 → #5
  - `2026-03-26 23:13 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-27 00:13 CET` — #10 — continuation; rank down #6 → #10

### 20) `bytedance-video-generation-model-dreamina`
- Status: `inactive`
- Theme: `consumer-ai-launches`
- First seen: `2026-03-26 16:25 CET`
- Last seen: `2026-03-26 23:13 CET`
- Appearances in top 10: `10`
- Latest title: ByteDance’s new AI video generation model, Dreamina Seedance 2.0, comes to CapCut
- Latest known position: `#7` at `2026-03-26 23:13 CET`
- Timeline:
  - `2026-03-26 17:08 CET` — #1 — continuation; holds #1
  - `2026-03-26 17:13 CET` — #1 — continuation; holds #1
  - `2026-03-26 18:13 CET` — #1 — continuation; holds #1
  - `2026-03-26 19:13 CET` — #2 — continuation; rank down #1 → #2
  - `2026-03-26 20:13 CET` — #3 — continuation; rank down #2 → #3
  - `2026-03-26 21:13 CET` — #5 — continuation; rank down #3 → #5
  - `2026-03-26 22:13 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-26 23:13 CET` — #7 — continuation; rank down #6 → #7

### 21) `gemini-flash-live-making-audio`
- Status: `inactive`
- Theme: `audio-model-race`
- First seen: `2026-03-26 16:23 CET`
- Last seen: `2026-03-26 23:13 CET`
- Appearances in top 10: `10`
- Latest title: Gemini 3.1 Flash Live: Making audio AI more natural and reliable
- Latest known position: `#8` at `2026-03-26 23:13 CET`
- Timeline:
  - `2026-03-26 17:08 CET` — #2 — continuation; holds #2
  - `2026-03-26 17:13 CET` — #2 — continuation; holds #2
  - `2026-03-26 18:13 CET` — #2 — continuation; holds #2
  - `2026-03-26 19:13 CET` — #3 — continuation; rank down #2 → #3
  - `2026-03-26 20:13 CET` — #4 — continuation; rank down #3 → #4
  - `2026-03-26 21:13 CET` — #6 — continuation; rank down #4 → #6
  - `2026-03-26 22:13 CET` — #7 — continuation; rank down #6 → #7
  - `2026-03-26 23:13 CET` — #8 — continuation; rank down #7 → #8

### 22) `wikipedia-bans-generated-articles`
- Status: `inactive`
- Theme: `ai-governance`
- First seen: `2026-03-26 16:02 CET`
- Last seen: `2026-03-26 23:13 CET`
- Appearances in top 10: `10`
- Latest title: Wikipedia bans AI-generated articles
- Latest known position: `#9` at `2026-03-26 23:13 CET`
- Timeline:
  - `2026-03-26 17:08 CET` — #3 — continuation; holds #3
  - `2026-03-26 17:13 CET` — #3 — continuation; holds #3
  - `2026-03-26 18:13 CET` — #3 — continuation; holds #3
  - `2026-03-26 19:13 CET` — #4 — continuation; rank down #3 → #4
  - `2026-03-26 20:13 CET` — #5 — continuation; rank down #4 → #5
  - `2026-03-26 21:13 CET` — #7 — continuation; rank down #5 → #7
  - `2026-03-26 22:13 CET` — #8 — continuation; rank down #7 → #8
  - `2026-03-26 23:13 CET` — #9 — continuation; rank down #8 → #9

### 23) `senators-pushing-find-out-much`
- Status: `inactive`
- Theme: `data-center-politics`
- First seen: `2026-03-26 15:25 CET`
- Last seen: `2026-03-26 23:13 CET`
- Appearances in top 10: `10`
- Latest title: Senators are pushing to find out how much electricity data centers actually use
- Latest known position: `#10` at `2026-03-26 23:13 CET`
- Timeline:
  - `2026-03-26 17:08 CET` — #4 — continuation; holds #4
  - `2026-03-26 17:13 CET` — #4 — continuation; holds #4
  - `2026-03-26 18:13 CET` — #4 — continuation; holds #4
  - `2026-03-26 19:13 CET` — #5 — continuation; rank down #4 → #5
  - `2026-03-26 20:13 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-26 21:13 CET` — #8 — continuation; rank down #6 → #8
  - `2026-03-26 22:13 CET` — #9 — continuation; rank down #8 → #9
  - `2026-03-26 23:13 CET` — #10 — continuation; rank down #9 → #10

### 24) `conntour-raises-general-catalyst-build`
- Status: `inactive`
- Theme: `consumer-ai-launches`
- First seen: `2026-03-26 14:41 CET`
- Last seen: `2026-03-26 21:13 CET`
- Appearances in top 10: `8`
- Latest title: Conntour raises $7M from General Catalyst, YC to build an AI search engine for security video systems
- Latest known position: `#9` at `2026-03-26 21:13 CET`
- Timeline:
  - `2026-03-26 14:41 CET` — #5 — seeded from prior live file
  - `2026-03-26 17:08 CET` — #5 — continuation; holds #5
  - `2026-03-26 17:08 CET` — #5 — continuation; holds #5
  - `2026-03-26 17:13 CET` — #5 — continuation; holds #5
  - `2026-03-26 18:13 CET` — #5 — continuation; holds #5
  - `2026-03-26 19:13 CET` — #6 — continuation; rank down #5 → #6
  - `2026-03-26 20:13 CET` — #7 — continuation; rank down #6 → #7
  - `2026-03-26 21:13 CET` — #9 — continuation; rank down #7 → #9

### 25) `cohere-launches-open-source-voice`
- Status: `inactive`
- Theme: `audio-model-race`
- First seen: `2026-03-26 14:30 CET`
- Last seen: `2026-03-26 21:13 CET`
- Appearances in top 10: `8`
- Latest title: Cohere launches an open source voice model specifically for transcription
- Latest known position: `#10` at `2026-03-26 21:13 CET`
- Timeline:
  - `2026-03-26 14:30 CET` — #6 — seeded from prior live file
  - `2026-03-26 17:08 CET` — #6 — continuation; holds #6
  - `2026-03-26 17:08 CET` — #6 — continuation; holds #6
  - `2026-03-26 17:13 CET` — #6 — continuation; holds #6
  - `2026-03-26 18:13 CET` — #6 — continuation; holds #6
  - `2026-03-26 19:13 CET` — #7 — continuation; rank down #6 → #7
  - `2026-03-26 20:13 CET` — #8 — continuation; rank down #7 → #8
  - `2026-03-26 21:13 CET` — #10 — continuation; rank down #8 → #10

### 26) `webtoon-adding-localization-tools-comics`
- Status: `inactive`
- Theme: `consumer-ai-launches`
- First seen: `2026-03-26 14:00 CET`
- Last seen: `2026-03-26 20:13 CET`
- Appearances in top 10: `7`
- Latest title: Webtoon is adding AI localization tools to its comics platform
- Latest known position: `#9` at `2026-03-26 20:13 CET`
- Timeline:
  - `2026-03-26 14:00 CET` — #7 — seeded from prior live file
  - `2026-03-26 17:08 CET` — #7 — continuation; holds #7
  - `2026-03-26 17:08 CET` — #7 — continuation; holds #7
  - `2026-03-26 17:13 CET` — #7 — continuation; holds #7
  - `2026-03-26 18:13 CET` — #7 — continuation; holds #7
  - `2026-03-26 19:13 CET` — #8 — continuation; rank down #7 → #8
  - `2026-03-26 20:13 CET` — #9 — continuation; rank down #8 → #9

### 27) `backs-nude-app-ban-delays`
- Status: `inactive`
- Theme: `ai-governance`
- First seen: `2026-03-26 13:49 CET`
- Last seen: `2026-03-26 19:13 CET`
- Appearances in top 10: `6`
- Latest title: EU backs nude app ban and delays to landmark AI rules
- Latest known position: `#9` at `2026-03-26 19:13 CET`
- Timeline:
  - `2026-03-26 13:49 CET` — #8 — seeded from prior live file
  - `2026-03-26 17:08 CET` — #8 — continuation; holds #8
  - `2026-03-26 17:08 CET` — #8 — continuation; holds #8
  - `2026-03-26 17:13 CET` — #8 — continuation; holds #8
  - `2026-03-26 18:13 CET` — #8 — continuation; holds #8
  - `2026-03-26 19:13 CET` — #9 — continuation; rank down #8 → #9

### 28) `pound-flesh-data-centers-one`
- Status: `inactive`
- Theme: `data-center-politics`
- First seen: `2026-03-26 13:00 CET`
- Last seen: `2026-03-26 19:13 CET`
- Appearances in top 10: `6`
- Latest title: A ‘pound of flesh’ from data centers: One senator’s answer to AI job losses
- Latest known position: `#10` at `2026-03-26 19:13 CET`
- Timeline:
  - `2026-03-26 13:00 CET` — #9 — seeded from prior live file
  - `2026-03-26 17:08 CET` — #9 — continuation; holds #9
  - `2026-03-26 17:08 CET` — #9 — continuation; holds #9
  - `2026-03-26 17:13 CET` — #9 — continuation; holds #9
  - `2026-03-26 18:13 CET` — #9 — continuation; holds #9
  - `2026-03-26 19:13 CET` — #10 — continuation; rank down #9 → #10

### 29) `openai-shelves-erotic-chatbot-indefinitely`
- Status: `inactive`
- Theme: `general-ai-signal`
- First seen: `2026-03-26 12:58 CET`
- Last seen: `2026-03-26 18:13 CET`
- Appearances in top 10: `5`
- Latest title: OpenAI shelves erotic chatbot ‘indefinitely’
- Latest known position: `#10` at `2026-03-26 18:13 CET`
- Timeline:
  - `2026-03-26 12:58 CET` — #10 — seeded from prior live file
  - `2026-03-26 17:08 CET` — #10 — continuation; holds #10
  - `2026-03-26 17:08 CET` — #10 — continuation; holds #10
  - `2026-03-26 17:13 CET` — #10 — continuation; holds #10
  - `2026-03-26 18:13 CET` — #10 — continuation; holds #10
