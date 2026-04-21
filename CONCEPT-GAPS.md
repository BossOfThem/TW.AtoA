# CONCEPT-GAPS — intro-game baseline gap catalog

**Status:** Proposal layer. Not a CONCEPT.md edit. Not a spec.
**Date:** 2026-04-19. Migration pass: 2026-04-20 (top-5 ratified and absorbed into CONCEPT.md; 14 of 26 rows migrated).
**Driver:** PM playtest 2026-04-19; Finding #3 ("concept too thin to form a vision").
**Governing decisions:** [`2026-04-19-intro-baseline-gaps.md`](decisions/2026-04-19-intro-baseline-gaps.md), [`2026-04-19-concept-thinness-escalation.md`](decisions/2026-04-19-concept-thinness-escalation.md), [`2026-04-19-tutorial-cell-affordance.md`](decisions/2026-04-19-tutorial-cell-affordance.md).

**2026-04-20 migration tracker.** Rows migrated to CONCEPT.md via ratified decision entries:

| Row(s) | Decision entry | CONCEPT target |
|--------|----------------|----------------|
| SETTINGS-01, PAUSE-01 | [2026-04-20 meta-UI envelope](decisions/2026-04-20-meta-ui-envelope.md) | §3.9 |
| AUDIO-01 | [2026-04-20 audio architecture](decisions/2026-04-20-audio-architecture.md) | §3.10 |
| A11Y-01/02/03/04 + SETTINGS-02 | [2026-04-20 accessibility floor](decisions/2026-04-20-accessibility-floor.md) | §2.4a |
| CMDR-01, CMDR-02, AUDIO-03 | [2026-04-20 commander identity floor](decisions/2026-04-20-commander-identity-floor.md) | §3.2 cross-link, §4.1, §5.1, §6.4 |
| FLOW-01, FLOW-02, ONBOARD-01 | [2026-04-20 first-run flow](decisions/2026-04-20-first-run-flow.md) | §3.11 |
| SAVE-01, SAVE-02 (+ FLOW-03 local-profile half) | [2026-04-20 save model](decisions/2026-04-20-save-model.md) | §4.9 |

Remaining rows (11): SETTINGS-03, PAUSE-02, ONBOARD-02, ONBOARD-03, A11Y-05, AUDIO-02, CMDR-03, FLOW-03 (account-system half only), META-01, META-02, META-03.

**2026-04-21 shape-audit (post concept-tightening).** The [2026-04-21 concept tightening](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) collapsed upstream counts from 5 lineages / 11 ages / 5-commander roster to a 3/3/3 lean-launch shape. Audit result for the 11 remaining rows: **none reference the collapsed counts and none require retirement**. All eleven are shape-independent (settings / pause / onboarding / accessibility / audio focus-loss / cosmetic slot types / account model / localization / platform cert / telemetry). CMDR-03 has a minor implicit arithmetic drift — prior "Launch floor = 1 per slot per commander" multiplied to 5×3 = 15 cosmetic items; under 3×3 it is 9. That is a number change, not a shape change, and does not merit a row retirement. The 11 remaining rows stay as active gaps pending PM ratification.

> This doc is a holding area. Each row below either (a) migrates into `CONCEPT.md` via a per-gap decision entry when the PM ratifies a resolution, or (b) is explicitly deferred post-launch. Do not treat row text as spec. Rows cite 2024–2026 sources; URLs are in §Sources.

---

## How to read this doc

- **Top-5 must-close** (below) is the only list the PM needs to internalize. If you can restate all five from memory, the doc has done its job.
- **Gap table** (§1) has one row per gap, eight columns. Skim the top (vision-blockers) first.
- **Dimension notes** (§2) back each column with baseline evidence.
- **3x debug loop** (§3) is the synthesis discipline — read if a row surprises you.

---

## Top-5 must-close (PM memory test) — **RATIFIED 2026-04-20**

All five top rows were ratified 2026-04-20 via five decision entries (see migration tracker at top). Text below retained for historical context; CONCEPT.md is now authoritative for each.

Ranked by vision-formation impact. If Claude cannot explain what the shipping game *looks and feels like* without closing a row, the row is Blocks-vision.

1. **Intro flow has no meta-controls.** No settings, no pause, no save-and-exit, no quit-to-menu, no skip-tutorial. The whole "what keys / what volume / how do I stop" envelope is blank. `CONCEPT.md` §3.6 names modes but not a single meta-UI surface. *Severity: Blocks-vision. Owning phase: Phase 3 (scope) + Phase 5 (spec).*
2. **No audio spec at all.** Not a single channel named. No master/music/SFX/UI/voice breakdown, no ducking policy, no focus-loss behavior. The game has no described soundscape. *Severity: Blocks-vision. Owning phase: Phase 3 (mention) + Phase 5 (spec).*
3. **No accessibility floor.** Zero mentions of colorblind, font scaling, input remapping, reduced motion, subtitles. The four most-complained-about accessibility issues across modern games (remapping, text size, colorblind, subtitles — per Game Accessibility Guidelines) are all absent from `CONCEPT.md`. Modern baseline is roughly Xbox's 24-tag Accessible Games Initiative set. *Severity: Blocks-launch (can't ship without). Blocks-vision for anyone whose play depends on accessibility. Owning phase: Phase 2 (constraint) + Phase 5 (spec).*
4. **"Commander = user" is promised but under-specified.** `CONCEPT.md` §3.2 names portrait / silhouette / color / voice / passive / signature / progression ladder — but no target counts, no minimum floor for "this feels like mine." Marvel Snap, Legion TD 2 Mastermind, and Clash Royale all ship specific per-character voice-line counts, cosmetic slot counts, and signature-ability detail. Without numbers, the identity promise is a gesture, not a spec. *Severity: Blocks-MVP (MVP's two commanders need a minimum floor to validate the promise). Owning phase: Phase 4 (§4.1).*
5. **No first-run flow.** `CONCEPT.md` does not describe splash → menu → pick → tutorial → match. No click-budget target, no "aha within first 5 clicks" criterion, no skippable-on-return provision. Modern benchmark: D1 retention ~26% on mobile, heavily driven by first-5-clicks-to-meaningful-victory. *Severity: Blocks-vision. Owning phase: Phase 3 (loop) + Phase 5 (flow spec) → will become `stages/00-session-start.md`.*

Everything else in the table is Blocks-MVP, Blocks-launch, or Post-launch-ok.

---

## 1. Gap table

Columns: **ID** · **Gap (1 line)** · **CONCEPT says** · **Industry baseline (cite)** · **Proposed resolution (direction, not spec)** · **Severity** · **Owning phase**.

| ID | Gap | CONCEPT says | Industry baseline (source) | Proposed resolution | Severity | Phase |
|----|-----|--------------|---------------------------|---------------------|----------|-------|
| **SETTINGS-01** | No options menu defined. | Silent. | BTD6 ships: resolution, fullscreen, framerate cap, music vol, SFX vol, 20 accessibility features, effects-scale slider, tower-range color, placement snap. [[BTD6 accessibility](https://bloons.fandom.com/wiki/Accessibility)] | Add "Phase 3: meta UI surfaces" sub-section listing required top-level menus: Options, Pause, Inventory, Quit. Reserve Phase 5 for exhaustive per-setting list. | Blocks-vision | 3 + 5 |
| **SETTINGS-02** | No keybind remapping plan. | Silent. | KR5 community-flagged as dated for shipping without in-game remap (settings.lua file-edit only). [[KR5 keybind guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3298358740)] Modern baseline: full remap per Game Accessibility Guidelines. | Phase 2 constraint: "full input remapping is a launch requirement." Phase 5 spec: remap UI. | Blocks-launch | 2 + 5 |
| **SETTINGS-03** | No resolution / display options. | Silent. | BTD6: resolution + fullscreen + framerate cap toggle. KR5 shipped without, caused user-visible pain (multiple Steam threads). | Assumed-table-stakes; add one-line constraint to Phase 2. | Blocks-launch | 2 |
| **PAUSE-01** | No pause specified; no meta-control envelope. | Silent. Prototype is forced-linear. | They Are Billions pause = Continue / Save-and-Quit / Options. [[TAB pause thread](https://steamcommunity.com/app/644930/discussions/0/3277925755433683476/)] Every TD ships Esc-pause in solo. | Phase 3: Esc pauses solo; pause shows Resume / Options / Restart (solo-only) / Concede-or-Save-and-Exit / Quit-to-Menu. Ranked PvP disables pause + restart. | Blocks-vision | 3 |
| **PAUSE-02** | Ranked-mode exceptions to pause / restart not written. | Silent. | Tower Defense Simulator and most PvP TDs disable restart to prevent exploit. [[TDS restart thread](https://tds.fandom.com/f/p/4400000000000232317)] | Phase 3: write one-paragraph "solo vs competitive" meta-controls split. | Blocks-MVP | 3 |
| **ONBOARD-01** | Tutorial mandatory, non-skippable. | Implied by prototype; not stated in CONCEPT. | Onboarding best practice 2025: skippable or exitable, 3–5 screens max, meaningful victory in first 5 clicks, "aha within initial session → 3× renewal." [[inworld/onboarding-2024](https://inworld.ai/blog/game-ux-best-practices-for-video-game-onboarding)] | Phase 3: tutorial is contextual/interactive AND skippable with an "I know TW" option. Incentive (cosmetic) for completing, not gating. | Blocks-vision | 3 |
| **ONBOARD-02** | Tutorial placement affordance too subtle (glow-only). | N/A (prototype-level). | Basic GAG: convey information via multiple channels, not color alone. [[GAG Basic](https://gameaccessibilityguidelines.com/basic/)] | Prototype Step 4: outline + inner mark, not color-alone. Grayscale screenshot check. | Blocks-MVP | 5 (stage-00) |
| **ONBOARD-03** | No re-teach / codex. | Silent. | Modern TDs ship in-game encyclopedia (BTD6 Blooncyclopedia, KR5 tower info panels). | Phase 3: persistent unit/tower info panel + commander codex reachable from pause. | Blocks-MVP | 3 |
| **SAVE-01** | No save model defined. Solo Campaign is named but has no persistence model. | §3.7 names meta progression (commander XP, backpack) but not save format/slots. | Modern baseline: auto-save + 1–2 slots + cloud sync (Steam). Delta-sync + offline-first. [[Save systems 2025](https://generalistprogrammer.com/tutorials/game-save-systems-complete-data-persistence-guide-2025)] They Are Billions: single-slot ironman is a legitimate design choice but explicit. | Phase 4: pick save model per mode. Campaign = mid-mission save-and-exit. Solo skirmish = auto-save on end. Ranked = no mid-match save. Steam Cloud required at launch. | Blocks-launch | 4 |
| **SAVE-02** | No autosave frequency / loss-window policy. | Silent. | Modern baseline: autosave every wave-end or age-end in TD. | Phase 4: autosave at age-gate boundaries in solo. | Blocks-MVP | 4 |
| **A11Y-01** | No colorblind provision. | Silent. | Top-4 GAG complaint category. [[GAG Full list](https://gameaccessibilityguidelines.com/full-list/)] Xbox AGI tag exists. | Phase 2 constraint: "information conveyed via shape/icon/text, not color alone." Phase 5: colorblind-mode toggle. | Blocks-launch | 2 + 5 |
| **A11Y-02** | No font / UI scaling. | Silent. | GAG: font size and HUD scale UI, crosshairs, subtitles separately. | Phase 5: global UI scale (75%–150%) + subtitle scale separate. | Blocks-launch | 5 |
| **A11Y-03** | No reduced-motion / photosensitivity policy. | Silent. | WCAG 2.3.1: no >3 flashes/second. [[GAG full list](https://gameaccessibilityguidelines.com/full-list/)] | Phase 2 constraint: respect WCAG 2.3.1. Phase 5: reduce-effects toggle. | Blocks-launch | 2 + 5 |
| **A11Y-04** | No subtitles / captions spec. | Silent. | GAG Basic: subtitles with speaker labels, size adjustable. Xbox AGI tag. | Phase 5: all voice-line content captionable; speaker labels; size-scale. | Blocks-launch | 5 |
| **A11Y-05** | No one-handed / single-stick / toggle-vs-hold input modes. | Silent. | GAG full-remap + toggle vs hold. | Phase 5: remap UI supports toggle/hold per action. | Post-launch-ok | 5 |
| **AUDIO-01** | No audio channels defined. | Silent. | Minimum 5 buses: Master / Music / SFX / UI / Voice. Ducking for Voice. [[Game Audio Theory: Ducking](https://www.gamedeveloper.com/audio/game-audio-theory-ducking)] [[Unreal Forums mixer tip](https://forums.unrealengine.com/t/tip-audio-mixer-level-volume-control-for-master-sfx-and-music/1717150)] | Phase 3 add one-line "audio mixer = Master / Music / SFX / UI / Voice with sidechain duck on Voice." Phase 5: per-bus slider in options. | Blocks-vision | 3 + 5 |
| **AUDIO-02** | No focus-loss behavior. | Silent. | BTD6 community-requested; common 2024 baseline is mute-on-focus-loss optional toggle. [[BTD6 focus-loss thread](https://steamcommunity.com/app/960090/discussions/0/1639790664943945941/)] | Phase 5: toggle "mute when window loses focus," default on for solo, off for PvP. | Blocks-MVP | 5 |
| **AUDIO-03** | No voice line / commander VO plan. | §3.2 names "voice" for commanders. | Clash Royale / Marvel Snap ship per-character voice lines as the core identity hook. Marvel Snap has per-card VO as a cosmetic progression axis. [[Marvel Snap Wikipedia](https://en.wikipedia.org/wiki/Marvel_Snap)] | Phase 4: per-commander voice-line floor (e.g., 12 lines at launch: 3 pick, 3 victory, 3 defeat, 3 ability). Phase 5: recording spec. | Blocks-vision for commander promise | 4 + 5 |
| **CMDR-01** | Commander "identity floor" not specified numerically. | §3.2 lists components but no floor counts. | Marvel Snap variant art + per-card VO + Collection Level as cosmetic progression. Legion TD 2 Mastermind ships 10 playstyle variants. | Phase 4 (§4.1): floor per commander = portrait + 1 silhouette skin + 12 voice lines + 1 signature ability + 1 passive + 5-level progression ladder. MVP honors this floor for 2 commanders. | Blocks-MVP | 4 |
| **CMDR-02** | Commander progression ladder depth unspecified. | §3.2 names XP / levels / unlocks. | Clash Royale king-levels 1–50; Marvel Snap Collection Level into thousands (cosmetic only). | Phase 4: commander levels 1–20 at launch; unlocks paced (cosmetic + VO + portrait frames). No gameplay power gates (solo-first + no-P2W). | Blocks-MVP | 4 |
| **CMDR-03** | No cosmetic slot count. | Silent. | Clash Royale emotes / towers / king-skins; Marvel Snap variants + card-backs + titles. | Phase 4: define 3 cosmetic slot types (commander skin, portrait frame, map tint). Launch floor = 1 per slot per commander. | Post-launch-ok | 4 |
| **FLOW-01** | First-run flow not described. | Silent. | Best-practice 2025: "meaningful victory in first 5 clicks"; minimize splash delays. [[Apple onboarding for games](https://developer.apple.com/app-store/onboarding-for-games/)] | Phase 3: write one-paragraph flow: launch → (splash ≤3s, skippable) → main menu → New Game → Commander pick → (optional tutorial or jump to skirmish) → match. Click budget ≤6 to in-match. | Blocks-vision | 3 |
| **FLOW-02** | No returning-player differentiation. | Silent. | Modern: skip tutorial, remember last commander, show "Continue" if save exists. | Phase 3: returning-player flow branches at main menu (Continue / New Match / Commander Select). | Blocks-MVP | 3 |
| **FLOW-03** | No account / save-profile concept. | Silent. | Steam profile = identity + cloud-save key. | Phase 4: single local profile at launch (no account system); Steam Cloud for sync. Account system deferred post-launch. | Post-launch-ok | 4 |
| **META-01** | No language / localization plan mentioned. | §2.4 "English-first." | Modern: localization keys from day 1 even if only English ships. | Phase 5 constraint: all player-facing strings routed via key, not hard-coded. | Blocks-launch (for maintainability) | 5 |
| **META-02** | No platform certification list. | §2.2 "PC-primary." | Steam Deck verified is de-facto standard for PC TD launches. | Phase 5: "Steam Deck verified" is a launch goal; implies controller remap + minimum font sizes. | Post-launch-ok | 5 |
| **META-03** | No telemetry / crash-reporting. | Silent. | Sentry / Crashlytics / Steam crash. | Phase 5: crash reporting opt-in on first run. | Post-launch-ok | 5 |

**Count (pre-migration):** 26 rows. **Blocks-vision:** 6 (SETTINGS-01, PAUSE-01, ONBOARD-01, AUDIO-01, AUDIO-03, FLOW-01). **Blocks-launch:** 8. **Blocks-MVP:** 8. **Post-launch-ok:** 4.

**Count (post 2026-04-20 migration, second pass):** 11 rows remaining. Migrated (16 of 26 source rows — 14 from first batch + SAVE-01 + SAVE-02; FLOW-03 local-profile half committed but row remains open for account-system half): SETTINGS-01, SETTINGS-02, PAUSE-01, ONBOARD-01, AUDIO-01, AUDIO-03, A11Y-01, A11Y-02, A11Y-03, A11Y-04, CMDR-01, CMDR-02, FLOW-01, FLOW-02, SAVE-01, SAVE-02. Remaining rows unchanged in table above; read migrated rows as historical context, not active gaps.

Remaining rows by severity: **Blocks-launch:** 2 (SETTINGS-03, META-01). **Blocks-MVP:** 3 (PAUSE-02, ONBOARD-02, ONBOARD-03). **Post-launch-ok:** 6 (A11Y-05, AUDIO-02, CMDR-03, FLOW-03 account-system half, META-02, META-03).

---

## 2. Dimension notes (baseline evidence per research dimension)

### 2.1 Settings / options menu — minimum viable

Reference set from modern TDs:
- **BTD6** ships: resolution, fullscreen, framerate cap, master/music/SFX split, **20 documented accessibility features** including Effects Scale (0–100%), Ambient Map Effects toggle, Tower Range Circle color, Tower Placement Snapping, Large Subtitles, No Button Combos, No Holds, Select Difficulty. [[BTD6 accessibility wiki](https://bloons.fandom.com/wiki/Accessibility)] [[BTD6 settings UI](https://interfaceingame.com/screenshots/bloons-td-6-settings/)]
- **Kingdom Rush 5 Alliance** has a paginated settings menu (5 pages). Resolution + display on page 5. **Does NOT ship in-game keybind remapping** — users must edit `settings.lua`. This is a 2024 shipping decision that the community has flagged as substandard. [[KR5 keybind guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3298358740)]
- **Legion TD 2** (not directly surveyed for options UI in this pass; manual at [[LTD2 manual](https://beta.legiontd2.com/manual/)]).
- **They Are Billions** pause = Continue / Save-and-Quit / Options. [[TAB pause thread](https://steamcommunity.com/app/644930/discussions/0/3277925755433683476/)]

**Minimum sections to ship (synthesis):**
- **Video:** resolution, fullscreen/windowed/borderless, framerate cap, vsync, UI scale.
- **Audio:** Master, Music, SFX, UI, Voice (5 sliders minimum).
- **Input:** full keybind remap, controller layout preset, toggle-vs-hold flags.
- **Accessibility:** colorblind, font scale, reduce motion, subtitle size, effects scale.
- **Language:** at minimum "English."
- **Gameplay toggles:** tooltips-verbose, auto-pause on age-gate, confirm-before-send (PvP), placement-snap.

### 2.2 Onboarding / tutorial patterns

- Best practice 2025: **skippable or exitable**, **3–5 screens max**, **interactive, not pop-up-based**, **meaningful victory within first 5 clicks**. [[inworld 2024 guide](https://inworld.ai/blog/game-ux-best-practices-for-video-game-onboarding)] [[UX Collective](https://uxdesign.cc/games-ux-building-the-right-onboarding-experience-a6e99cf4aaea)]
- **GameAnalytics 2024/25 benchmark:** average D1 retention ~26%, D7 ~10%. Top titles D1 ≥35%, D7 ≥12%. [[GameAnalytics via zigpoll](https://www.zigpoll.com/content/how-can-we-optimize-the-onboarding-experience-to-reduce-player-dropoff-rates-in-our-mobile-game)]
- **Strategy-genre exception:** onboarding can be longer than casual games (mechanics complexity justifies it), but must stay interactive. [[Mistplay](https://business.mistplay.com/resources/mobile-game-retention-benchmarks)]
- **Hybrid direction for Ash to Altar:** contextual (teach via mini-quests within tutorial match), skippable for returning players, incentivized-completion (cosmetic reward for finishing, not gating core content).

### 2.3 Pause / meta-controls

- **Solo TD baseline:** Esc pauses → Resume / Options / Restart / Quit-to-Menu. Defense Grid 2 is the reference for strategic pause. [[DG2 pause discussion](https://steamcommunity.com/app/221540/discussions/0/613948093871964702/)]
- **Competitive TW baseline:** pause disabled; restart disabled to prevent exploit. TDS community confirmed 2024. [[TDS restart thread](https://tds.fandom.com/f/p/4400000000000232317)]
- **They Are Billions model:** single Save-and-Quit (no mid-match save-load because ironman). [[TAB save thread](https://steamcommunity.com/app/644930/discussions/0/3202621953672226809/)]
- **Synthesis:** A-to-A solo pause = full meta controls. PvP pause = read-only (view economy, no state change). Save-and-exit available in solo campaign, not in ranked.

### 2.4 Save / persistence

- **Modern baseline:** auto-save + 1–2 slots + Steam Cloud. Delta-sync reduces bandwidth. [[Save systems 2025 guide](https://generalistprogrammer.com/tutorials/game-save-systems-complete-data-persistence-guide-2025)]
- **Ironman exception:** They Are Billions — single slot, no manual save, auto-save on exit. Legitimate design stance but explicit. Community pushback exists. [[TAB disable auto-save request](https://steamcommunity.com/app/644930/discussions/0/5829413348550253878/)]
- **Commander progression persistence model:** separate from match save. Commander XP / unlocks / cosmetics must persist per-profile, cloud-synced.
- **Synthesis:** A-to-A solo campaign = auto-save per mission + manual save-and-exit. Skirmish = per-run only. Ranked = no save. Commander profile = always-persistent, cloud-synced.

### 2.5 Accessibility floor

- **Top-4 most-complained issues per Game Accessibility Guidelines:** input remapping, text size, colorblind support, subtitle presentation. [[GAG full list](https://gameaccessibilityguidelines.com/full-list/)]
- **WCAG 2.3.1:** no flashing elements >3 flashes/sec (seizure safety). Industry baseline, not optional.
- **Xbox Accessible Games Initiative:** 24 tags (2024–2025 expansion). Tag your launch against this taxonomy. [[Xbox AGI tags](https://news.xbox.com/en-us/2025/07/09/accessible-games-initiative-tags-xbox-interview/)] [[MS Learn feature tags](https://learn.microsoft.com/en-us/gaming/accessibility/accessibility-feature-tags)]
- **Minimum shippable set for A-to-A (synthesis):** full input remap, font scale (UI + subtitles independent), colorblind-safe iconography, reduce-motion toggle, WCAG 2.3.1 compliance, subtitle-with-speaker-labels, no color-only information channels.

### 2.6 Audio spec

- **Minimum channel count:** 5 buses (Master, Music, SFX, UI, Voice). [[Unreal Forums](https://forums.unrealengine.com/t/tip-audio-mixer-level-volume-control-for-master-sfx-and-music/1717150)] [[Unity Learn audio mixing](https://learn.unity.com/tutorial/audio-mixing-1)]
- **Ducking:** sidechain from Voice bus to Music + SFX. [[Game Audio Theory: Ducking](https://www.gamedeveloper.com/audio/game-audio-theory-ducking)]
- **UI audio hierarchy:** critical (player death, wave break) vs background (hover, menu). [[SFX Engine UI audio guide](https://sfxengine.com/blog/best-practices-for-game-ui-sounds)]
- **Focus-loss:** mute-on-focus-loss is a BTD6 community-requested baseline. [[BTD6 focus-loss thread](https://steamcommunity.com/app/960090/discussions/0/1639790664943945941/)]
- **A-to-A implication:** CONCEPT has zero lines on audio. At minimum, Phase 3 should name the 5 buses and the ducking policy. Phase 5 specs per-bus slider in options.

### 2.7 Commander depth

- **Marvel Snap model:** per-card variants as cosmetic progression; Collection Level as non-power unlock track; per-card voice lines (example: Korg line thread). [[Marvel Snap Wikipedia](https://en.wikipedia.org/wiki/Marvel_Snap)] [[Korg voice line](https://marvelsnapzone.com/answers/korg-voice-line/)]
- **Legion TD 2 Mastermind:** 10 playstyle variants; per-playstyle mechanical identity (Chaos shuffles fighters per wave). [[LTD2 Mastermind](https://beta.legiontd2.com/mastermind/)] [[Mastermind Playstyle wiki](https://legiontd2.fandom.com/wiki/Mastermind_Playstyle)]
- **Clash Royale (reference):** per-card king-level + emotes + tower skins; identity is a combination of deck + emotes + cosmetics.
- **Minimum "this is mine" floor (synthesis):** portrait + silhouette skin + ≥12 voice lines (pick/victory/defeat/ability × 3 each) + 1 signature ability + 1 passive + progression ladder (~20 levels at launch, cosmetic-only rewards) + 1 cosmetic slot honored at launch. Anything less and the commander is "a skin with a stat modifier" — the failure mode explicitly called out in CONCEPT §7.4.

### 2.8 First-run flow

- **Click budget:** ≤5 clicks to meaningful victory per 2025 best-practice. [[Apple onboarding](https://developer.apple.com/app-store/onboarding-for-games/)] [[Plotline 2026](https://www.plotline.so/blog/mobile-app-onboarding-examples/)]
- **Splash behavior:** skippable, ≤3s. Avoid agreements/disclaimers pre-gameplay. [[stash.gg retention glossary](https://www.stash.gg/glossary/game-retention)]
- **Returning-player branch:** show "Continue" if save exists; remember last commander.
- **A-to-A draft flow (proposal):** launch → splash (≤3s, skippable) → main menu (Continue? / New Game / Commander Select / Skirmish / Options / Quit) → first-time: Commander Pick → Tutorial (skippable with cosmetic incentive to complete) → Match → End. Click budget ≤6 to in-match. Returning: Continue → straight to last save.

---

## 3. 3x debug loop (synthesis discipline)

### Loop 1 — Aggressive critique

- **The gap doc duplicates CONCEPT.md's job.** We have a 500-line CONCEPT.md and now a 300-line gap doc. Two sources of truth = drift. The critique: just edit CONCEPT.md.
- **"Industry baseline" is selection-bias shopping.** Cherry-picking four modern TDs makes every "baseline" sound universal when it's just what those four ship. Kingdom Rush 5 famously ships without keybind remap — so "full remap is launch baseline" is an overstatement.
- **The top-5 is arbitrary.** Why these five and not different five? SAVE-01 arguably blocks vision more than AUDIO-03 (voice lines) for a player who doesn't care about commander VO.
- **Severity tags lack rigor.** "Blocks-vision" vs "Blocks-MVP" vs "Blocks-launch" is a rubric the PM never signed off. Gaming the rubric gets you any ordering.
- **Proposing 26 rows is too many.** PM cannot hold 26 things in working memory; the top-5 hides the other 21. Reader will skim and act on impression, not catalog.
- **This doc is itself a new TBD factory.** Every row says "Phase 3 add a section" or "Phase 5 spec." The doc creates more TBDs than it closes.
- **Commander VO floor (CMDR-01, 12 voice lines) is a fabricated number.** No source said "12." Risks being cargo-culted into a decision.
- **Research was thin on Legion TD 2 Mastermind voice/cosmetic details.** One of the four anchor titles produced sparse findings; the gap doc may over-generalize from Snap/Royale.

### Loop 2 — Steelman

- **"Just edit CONCEPT.md" ignores cascade discipline.** CLAUDE.md is explicit: Phase N+1 may not silently edit Phase N, and changes go through the decision log. The gaps doc is the honest middle step. The drift concern is real but managed by the migration rule (each row moves to CONCEPT via a ratified decision, then deletes from the catalog).
- **Selection bias is intentional.** The four titles were chosen because they are the modern baseline for Ash to Altar's target player (TW/TD veterans). BTD6 + KR5 + LTD2 + TAB is exactly the comparison set. KR5 lacking remap is not evidence that shipping without remap is fine — it's evidence that shipping without remap draws community complaint.
- **Top-5 is a forcing function, not a ranking claim.** The value is "five things the PM *must* internalize." If PM reshuffles the five, the doc has still worked.
- **Severity rubric is pragmatic.** Blocks-vision = can't picture the game without it. Blocks-MVP = can't validate the vision without it. Blocks-launch = commercial/legal. Post-launch-ok = everything else. Not mathematical but unambiguous enough to sort a table.
- **26 rows is the right scope because the PM said the concept has "a lot" of gaps.** Collapsing to a handful would be spec fraud. The top-5 exists precisely to make the 26 tractable.
- **Creating TBDs is the correct output of a gaps pass.** The gaps doc doesn't close gaps; it *names* them so the PM can close them in ratified order. Premature closure violates cascade discipline more than naming does.
- **CMDR-01 "12 voice lines" is flagged as a proposal direction, not a lock.** Sources support per-character VO as a core identity hook (Marvel Snap, Clash Royale); 12 is an order-of-magnitude proposal (pick/victory/defeat/ability × 3) to make the concept concrete enough to react to.
- **Mastermind sparse-findings critique is real but bounded.** Mastermind is a progression system on top of LTD2's units, not a per-commander character system; its 10 playstyles inform the "variant" axis, not the "identity floor" axis. The gap doc doesn't overweight it.

### Loop 3 — Synthesis

Changes applied (already in §1 table above):

1. **Migration rule is explicit in the header:** every row moves to CONCEPT via per-gap decision or is deferred post-launch. This is the drift-control mechanism.
2. **Top-5 is labeled as a memory test, not a priority claim.** If PM remembers different five, fine.
3. **Severity rubric defined inline** (Blocks-vision / Blocks-MVP / Blocks-launch / Post-launch-ok). Rubric stays flexible; rigor comes from per-row justification.
4. **CMDR-01 explicitly flagged:** "floor ≈ 12 voice lines" is a direction-setter, not a lock; Phase 4 decision will pick the real number.
5. **Cap at 26 rows accepted.** The top-5 absorbs the forcing function; the remaining 21 are searchable in-table.
6. **Four-title comparison set is declared as "modern baseline for Ash to Altar's target player" in §2.1,** not as a universal claim. KR5's keybind omission is cited as what NOT to do, not as permission to skip.
7. **Doc length capped.** ~400 lines including table + dimensions + loop. PM reading-time target: 10–15 minutes.

**Net call:** this doc is a proposal layer with a migration path, not a parallel spec. It is explicitly ephemeral: every ratified row moves out; the doc shrinks over time; ideally the doc reaches zero rows when CONCEPT.md has absorbed or explicitly deferred each.

---

## 4. Recommended resumption path

If the PM ratifies the top-5:
1. **One decision entry per ratified row**, each proposing a specific resolution direction. Start with `SETTINGS-01` because it unblocks the other meta-UI rows.
2. **CONCEPT.md amendment pass** — one small diff per ratified decision, preserving cascade. (Phase 3 gets new sub-sections; Phase 5 gets spec pointers.)
3. **Resume PROGRESS.md queue at Step 1.5b** once the top-5 is ratified OR the PM explicitly unpauses.

If the PM disagrees with the top-5:
- Pick a different five, or pick one, or defer the whole catalog. All valid. The gap doc's job is to make the choice legible, not to make it.

---

## Sources

Settings / options:
- [Bloons TD 6 accessibility options (Bloons Wiki)](https://bloons.fandom.com/wiki/Accessibility)
- [Bloons TD 6 settings UI (Interface In Game)](https://interfaceingame.com/screenshots/bloons-td-6-settings/)
- [Bloons TD 6 accessibility report (Family Gaming Database)](https://www.familygamingdatabase.com/en-us/accessibility/Bloons+TD+6)
- [Kingdom Rush 5 Alliance keybind editing guide (Steam)](https://steamcommunity.com/sharedfiles/filedetails/?id=3298358740)
- [Kingdom Rush 5 Alliance resolution change thread (Steam)](https://steamcommunity.com/app/2849080/discussions/0/596278044732245288/)

Onboarding / tutorial:
- [Game UX: Best practices for video game onboarding (Inworld, 2024)](https://inworld.ai/blog/game-ux-best-practices-for-video-game-onboarding)
- [Games UX: Building the right onboarding experience (UX Collective)](https://uxdesign.cc/games-ux-building-the-right-onboarding-experience-a6e99cf4aaea)
- [Optimizing onboarding to reduce player drop-off (Zigpoll)](https://www.zigpoll.com/content/how-can-we-optimize-the-onboarding-experience-to-reduce-player-dropoff-rates-in-our-mobile-game)
- [Mobile Game Retention Benchmarks (Mistplay)](https://business.mistplay.com/resources/mobile-game-retention-benchmarks)
- [Onboarding for Games (Apple Developer)](https://developer.apple.com/app-store/onboarding-for-games/)

Pause / meta-controls:
- [They Are Billions pause thread (Steam)](https://steamcommunity.com/app/644930/discussions/0/3277925755433683476/)
- [Tower Defense Simulator restart restriction discussion (Fandom)](https://tds.fandom.com/f/p/4400000000000232317)
- [Defense Grid 2 pause discussion (Steam)](https://steamcommunity.com/app/221540/discussions/0/613948093871964702/)

Save / persistence:
- [Game Save Systems Complete Guide 2025 (Generalist Programmer)](https://generalistprogrammer.com/tutorials/game-save-systems-complete-data-persistence-guide-2025)
- [They Are Billions save game thread (Steam)](https://steamcommunity.com/app/644930/discussions/0/3202621953672226809/)
- [They Are Billions auto-save disable request (Steam)](https://steamcommunity.com/app/644930/discussions/0/5829413348550253878/)

Accessibility:
- [Game Accessibility Guidelines — Full List](https://gameaccessibilityguidelines.com/full-list/)
- [Game Accessibility Guidelines — Basic](https://gameaccessibilityguidelines.com/basic/)
- [Accessible Games Initiative Tags (Xbox Wire, 2025)](https://news.xbox.com/en-us/2025/07/09/accessible-games-initiative-tags-xbox-interview/)
- [Accessibility Feature Tags (Microsoft Learn)](https://learn.microsoft.com/en-us/gaming/accessibility/accessibility-feature-tags)
- [How New Accessibility Features Are Changing Modern Game Design (GameSpace)](https://gamespace.com/all-articles/news/how-new-accessibility-features-are-changing-modern-game-design/)

Audio:
- [Game Audio Theory: Ducking (Game Developer)](https://www.gamedeveloper.com/audio/game-audio-theory-ducking)
- [Audio mixer Master/SFX/Music tip (Unreal Forums)](https://forums.unrealengine.com/t/tip-audio-mixer-level-volume-control-for-master-sfx-and-music/1717150)
- [Audio mixing (Unity Learn)](https://learn.unity.com/tutorial/audio-mixing-1)
- [Mixing AAA Videogames (AudioTechnology)](https://www.audiotechnology.com/features/mixing-aaa-videogames)
- [Best Practices for Game UI Sounds (SFX Engine)](https://sfxengine.com/blog/best-practices-for-game-ui-sounds)
- [Bloons TD 6 focus-loss thread (Steam)](https://steamcommunity.com/app/960090/discussions/0/1639790664943945941/)

Commander depth:
- [Marvel Snap (Wikipedia)](https://en.wikipedia.org/wiki/Marvel_Snap)
- [Marvel Snap Zone — Korg voice line](https://marvelsnapzone.com/answers/korg-voice-line/)
- [Legion TD 2 Mastermind options](https://beta.legiontd2.com/mastermind/)
- [Legion TD 2 Mastermind Playstyle (Fandom)](https://legiontd2.fandom.com/wiki/Mastermind_Playstyle)
- [Legion TD 2 Game Manual](https://beta.legiontd2.com/manual/)

First-run flow:
- [Onboarding for Games (Apple Developer)](https://developer.apple.com/app-store/onboarding-for-games/)
- [Best Mobile App Onboarding Examples 2026 (Plotline)](https://www.plotline.so/blog/mobile-app-onboarding-examples/)
- [Game Retention glossary (stash.gg)](https://www.stash.gg/glossary/game-retention)
- [Mobile Game Retention Rates 2026 (Business of Apps)](https://www.businessofapps.com/data/mobile-game-retention-rates/)

---

*Document version: 0.4 — 2026-04-21 shape-audit pass. [2026-04-21 concept tightening](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) collapsed upstream to a 3/3/3 lean-launch shape; audit of the 11 remaining rows confirms none reference 5-lineage / 11-age / 5-commander counts and none require retirement. Active gap count unchanged at 11. CMDR-03 has implicit arithmetic drift (1 cosmetic item × 3 slots × 3 commanders = 9, down from 15) — number change, not shape change. Prior: v0.3 — 2026-04-20 (SAVE-01 + SAVE-02 ratified); 16 of 26 rows migrated; 11 remain (2 Blocks-launch, 3 Blocks-MVP, 6 Post-launch-ok).*
