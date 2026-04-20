# Stage 00 — Session Start

**Status:** Draft
**Phase in CONCEPT cascade:** 3 (Design) / 5 (Implementation planning for per-screen UX)
**Upstream deps:** [CONCEPT §1.2](../CONCEPT.md), [§2.4a](../CONCEPT.md), [§3.9](../CONCEPT.md), [§3.10](../CONCEPT.md), [§3.11](../CONCEPT.md), [§4.9](../CONCEPT.md); [decisions/2026-04-20-meta-ui-envelope.md](../decisions/2026-04-20-meta-ui-envelope.md), [decisions/2026-04-20-audio-architecture.md](../decisions/2026-04-20-audio-architecture.md), [decisions/2026-04-20-accessibility-floor.md](../decisions/2026-04-20-accessibility-floor.md), [decisions/2026-04-20-first-run-flow.md](../decisions/2026-04-20-first-run-flow.md), [decisions/2026-04-20-save-model.md](../decisions/2026-04-20-save-model.md)
**Downstream impact:** [Stage 01 — commander pick](01-commander-pick.md)
**Research backing:** [05-demographics-platform.md](../research/05-demographics-platform.md) (light)
**Last reviewed:** 2026-04-20

---

## 1. Scope

Everything between you double-clicking the game icon and arriving at either the Commander selection screen (first-time) or a main menu ready for action (returning). Covers:

- Splash / studio logo / engine credit / title reveal.
- Main menu — first-time state vs returning-player state.
- Accessibility floor applied at the earliest surface the game owns.
- Pre-menu audio/visual tone-setting.
- Save / cloud-save handshake, offline detection, patch prompt.

**Out of scope:** Commander pick itself (owned by [Stage 01](01-commander-pick.md)); tutorial content (also Stage 01 and the tutorial-segment it hands off to); in-match Pause overlay ([Stage 04](04-in-match-core.md)).

## 2. Upstream constraints (inheritance table)

This stage is Phase-5 drill-down on Phase-3 design. It may not silently edit anything upstream. Each constraint below is cited so any edit to this stage can be back-checked.

- **CONCEPT §1.2 — Target player.** Strategy player coming from Kingdom Rush / BTD6 / Legion TD 2. Session-length tolerance 5–25 min. Implication: launch-to-menu latency is part of session length; a slow cold-launch is a retention bug, not a polish task.
- **CONCEPT §2.4a — Accessibility floor [LOCKED].** Top-4 GAG + WCAG 2.3.1 + Xbox AGI tag self-audit. Floor applies from the first screen the game controls (so: splash / logos, not only gameplay).
- **CONCEPT §3.9 — Meta-UI envelope.** Main menu items: Play / Commander / Backpack / Battle Pass / Store / Options / Quit. Options reachable from main menu and from Pause. This stage commits to exposing those surfaces; the per-setting list is Phase 5.
- **CONCEPT §3.10 — Audio architecture.** 5-bus (Master / Music / SFX / UI / Voice). Voice ducks Music + SFX. Focus-loss mutes Music + ambient SFX in solo modes; competitive PvP audio keeps running. User-overridable in Options.
- **CONCEPT §3.11 — First-run and returning-player flow.** Splash ≤3s, skippable. First-time click budget ≤6 to in-match; returning ≤3. Tutorial contextual + skippable ("I've played Tower Wars before").
- **CONCEPT §4.9 — Save model.** Commander profile always-persistent (Steam Cloud, continuous debounced). Mode-aware in-match saves. No account system at launch. Single local profile per install. Cloud-conflict resolution is Phase 5 UX work, but the *principle* (no silent merge) is inherited here.
- **decisions/2026-04-20-meta-ui-envelope.md** — confirms pause + options split and mode-aware pause content. This stage owns only the main-menu side.
- **decisions/2026-04-20-audio-architecture.md** — confirms 5-bus + ducking + focus-loss policy. This stage sets *intent* for pre-menu and menu beds; Phase 5 sets the numbers.
- **decisions/2026-04-20-accessibility-floor.md** — confirms the LOCKED constraint. This stage lists per-screen floor behaviors, not new policy.
- **decisions/2026-04-20-first-run-flow.md** — confirms click budgets, Continue affordance, tutorial-skip. This stage is the per-screen spec owner.
- **decisions/2026-04-20-save-model.md** — confirms persistent commander profile + Steam Cloud. This stage owns the launch-time handshake UX only.

Nothing here is meant to override any of those. Flag any apparent conflict to the PM for a decision entry.

## 3. Launch sequence (first-time)

The sequence below is the *first time you ever run the game*. No local save, no cloud save, no profile.

### 3.1 Beats

1. **App launch → blank window** (branded loader, <1s target). No audio yet. Platform-native launcher chrome only.
2. **Splash / studio logo** (≤1.5s, skippable from keystroke 1). Target format: a single low-motion frame with a short sting on the UI bus. Reduce-motion setting collapses to a static card with a cross-fade only.
3. **Engine credit card** (Godot or whatever locks at Phase 4 exit — [PROPOSAL]: a *single* credit card, not a chain; ≤1.5s, skippable). Legal-minimum only.
4. **Title reveal** — the game title lockup plus a short musical stinger on the Music bus. ≤1.5s. Skippable.
5. **Main menu (first-time variant)**. No Continue entry. Play CTA is visually dominant. An unobtrusive accessibility-preflight overlay offers Colorblind / Subtitles / Text-size / Input-remap shortcuts *before* the first click into Play — dismissible, not modal-blocking.

Total from double-click to first interactive menu: **target ≤6 seconds on HDD install, ≤3 seconds on SSD.** This is a target, not a commitment — confirmed at Phase 6 validation.

### 3.2 Click budget to in-match (first-time)

From §3.11: ≤6 clicks. Worked example for a new player who accepts defaults:

1. Dismiss splash chain (one chord / one click counts as 1).
2. Click **Play**.
3. Click **New Game** (or equivalent on first-time main menu).
4. Click commander card → arrives at Stage 01 picker.
5. Confirm commander (Stage 01).
6. Start match (Stage 01 / Stage 03 handoff).

Budget headroom for one accessibility detour (picking a colorblind preset) without blowing the cap. If the tutorial accepts default and auto-starts, the sixth click lands in-match.

### 3.3 Accessibility applied at each step

- **Splash / logos:** skippable from keystroke 1 (not frame 1 — input grace). Reduce-motion setting is *inferred from OS* where the platform exposes it and *asked explicitly* on the first-time accessibility preflight.
- **Audio sting:** respects a system mute and the UI-bus default attenuation. Captioned on any speech — the studio-logo card has no VO at launch by default [PROPOSAL].
- **Title reveal:** must not flash; conforms to WCAG 2.3.1 (≤3 flashes/sec).
- **Main menu:** all controls reachable by keyboard tab-order and by screen-reader label. Input-latency target on menu buttons: ≤100 ms [PROPOSAL] between click and audible+visible acknowledgement.
- **Text:** subtitle and UI scaling sliders are exposed in the preflight overlay, not buried in Options > Accessibility.

## 4. Launch sequence (returning)

A save is detected (local profile present and/or Steam Cloud confirms a commander). This is the common path after week 1.

### 4.1 Beats

1. **App launch → blank window** as above.
2. **Splash** — skippable and, per §9 Alternatives, *still shown* by default at Draft stage (auto-skip-after-first-run is an Alternative, not the current lean).
3. **Cloud handshake** happens in parallel with the splash chain. If Steam Cloud reports a newer remote save than the local one, the handshake holds at the main menu (not mid-splash) and raises a conflict dialog (§8).
4. **Main menu (returning variant)** — **Continue** CTA is the visually dominant control. Secondary: Play (mode select), Commander, Backpack, Battle Pass, Store, Options, Quit.
5. **Optional unclaimed-rewards surface** — a low-key banner above the main CTA, not a modal, not a takeover. Dismissable. See §4.3.

### 4.2 Click budget to in-match (returning)

From §3.11: ≤3 clicks. Worked example:

1. Dismiss splash chord.
2. Click **Continue** → routes to the last in-progress state, which is either a live Solo Campaign mission (resumes from last age-gate autosave per §4.9) or, if no resumable match exists, a mode-select deep-link at your last-used mode.
3. Confirm-and-go (final click inside the deep-linked surface).

Returning players who want to change commander / mode instead take the normal Play path and fall under the first-time budget cap of 6.

### 4.3 Unclaimed-reward surface policy

Retention-vs-trust tradeoff. Aggressive surfacing (modal takeover, auto-open rewards screen) is a short-term retention lever that reads as manipulative and burns trust — which is a §7.4 identity-constraint risk for a no-pay-to-win game. Leading policy:

- **Leading [PROPOSAL]:** a single-line banner above the main menu Continue CTA, e.g. *"2 unclaimed season rewards — view"* with a clear close affordance. Banner disappears once viewed. Never autoplays animation. Never blocks Continue.
- **Not:** a modal. Not: a gated "you must open the Backpack first" flow. Not: a badge that persists across sessions once dismissed.

Alternatives in §10.

## 5. Main menu content

Per CONCEPT §3.9 the top-level menu exposes Play / Commander / Backpack / Battle Pass / Store / Options / Quit. First-time and returning variants share layout and differ in defaults and emphasis.

| Entry | First-time default | Returning default | Notes |
|-------|-------------------|-------------------|-------|
| **Continue** | Hidden | Present, visually dominant | Only variant difference in layout grammar. Routes per §4.2. |
| **Play** | Visually dominant; labelled "New Game" | Present; labelled "Play" | Expands into mode-select (Stage 02). |
| **Commander** | Present; subtle | Present | Read-only on first launch; interactive after Stage 01 completes. |
| **Backpack** | Present; empty-state copy | Present | Unclaimed-rewards count badge if applicable (§4.3). |
| **Battle Pass** | Present; "season 0 / preview" | Present | Never gated behind a store click. |
| **Store** | Present | Present | Cosmetic only, per §3.7 and §7.4. |
| **Options** | Present; accessibility row surfaced in preflight overlay too | Present | Also reachable from Pause overlay (§3.9). |
| **Quit** | Present | Present | Confirm dialog only if cloud sync is mid-flight (§8). |

Layout grammar: single vertical stack on the left, dominant art field on the right with commander silhouette (default starter silhouette for first-time, your chosen commander for returning). First-time variant shows a "Pick your Commander" affordance in the art field as a secondary hook.

Persistent footer: build version, connection/cloud status, news ticker slot ([PROPOSAL], off by default; content policy Phase 5).

## 6. Accessibility floor at Stage 00

Per §2.4a. This section is not new policy — it is the per-screen expression.

- **Colorblind.** Colorblind presets surfaced in the first-time preflight overlay. All menu affordances are icon + text + color, never color-only. The Continue vs Play distinction at returning-player main menu is primary by size + position + icon, not by color.
- **Subtitles.** On by default. Any VO on the splash / title stinger [PROPOSAL: none at launch] is captioned. Speaker labels on all captions.
- **Remap.** Full input remap available from Options on main menu. Keyboard-only navigation is a conformance requirement, not a preference.
- **Screen-reader affordance.** All menu controls carry ARIA-equivalent labels. Menu focus order is declared, not implicit. Live-region announcements on transient state (e.g. cloud conflict resolved).
- **Motion reduction.** OS-inferred where possible, explicit in preflight. Collapses splash cross-fades, disables menu parallax, freezes commander-silhouette idle animation.
- **Input-latency target.** ≤100 ms from click to acknowledgement on main-menu buttons [PROPOSAL]. Validated at Phase 6.
- **UI / subtitle scaling.** Independent sliders, 75%–150% minimum per §2.4a, exposed in preflight and Options.
- **Xbox AGI tagging self-audit.** Stage 00 is the first surface audited. Gaps noted in the launch accessibility statement, not silently dropped.

## 7. Audio intent

Per §3.10. This stage sets character, not numbers.

- **Main theme [PROPOSAL].** A short, modal, percussion-forward motif referencing the age-arc (low drone → bell ornament → clean resolution). Loopable under main menu without fatigue at 5–10 minute idle. *Not* a bombastic fanfare — the game's tonal promise is compressed civilizational arc, not epic heroism.
- **Music bus** — carries the main theme and splash/title stinger.
- **SFX bus** — menu hover / click / focus / error. Brief, diegetic-adjacent (paper / stone / metal textures referencing the lineages), never over-synthetic.
- **UI bus** — toast notifications (cloud sync complete, unclaimed rewards), never duck Music.
- **Voice bus** — silent at Stage 00 by default; ducks Music and SFX when Commander voice lines fire at Stage 01 (per commander identity floor §4.1).
- **Master bus** — single user-facing "volume" default, with per-bus sliders behind Options > Audio.
- **Focus-loss behavior** at Stage 00: mute Music + ambient SFX on alt-tab. Menu is a solo-mode surface in the §3.10 sense. User-overridable.

Track count, stems, adaptive transitions, and per-bus default levels are Phase 5.

## 8. Offline / patch / cloud-save handshake

The launch flow must survive three adversarial conditions without breaking the click budget.

### 8.1 Offline

- Detection is non-blocking — the main menu loads regardless.
- Modes that run offline per §4.9 and §3.6: **Solo Campaign, Solo Skirmish.** Everything else (Co-op Horde, Lane Wars 1v1/2v2, Battle Pass progression, Store) gates with a clear "offline" affordance, not a generic error.
- Commander profile continues to operate from local storage; queued changes sync on reconnection.

### 8.2 Patch prompt

- Patch detection happens in parallel with splash. If a patch is available, a dialog raises at the main menu *after* splash completes — never mid-splash, never during Continue routing.
- Dialog copy [PROPOSAL]: "A new version is available. Updating is required to play online. Update now / Play offline / Later."
- If the patch is mandatory (e.g. competitive parity), "Play offline" is the only non-update option, and the main menu renders with PvP entries disabled.

### 8.3 Steam Cloud conflict

- Principle per §4.9: **never silent merge.** Leading UX [PROPOSAL]: a modal that shows both saves with timestamp + summary (commander name, level, last-played mode) and requires an explicit pick. Default highlight on the newer save. No auto-dismiss.
- Conflict dialog raises at the main menu, not mid-splash, so the returning-player click budget only suffers when there *is* a genuine conflict.
- "Pick newer" is offered as a single-click shortcut. Destructive-write warning surfaces if the user picks the older save.

Detailed per-slot UI, corruption recovery, and multi-device reconciliation edge cases are Phase 5 per §4.9.

## 9. Open questions

Carried from the stub plus newly-surfaced:

1. **Shared vs diverged menu layout (first-time vs returning).** Leading: shared grammar, differentiated defaults (see §5). *Resolution: here at Stage 00 on next review, or via a decision entry if scope bloats.*
2. **Unclaimed-rewards aggression.** Leading: banner, not modal (§4.3). *Resolution: decision entry before Phase 5 exit.*
3. **Offline capability surface.** Leading: Campaign + Skirmish offline-capable, everything else gated. *Resolution: confirm in Stage 02 mode-select doc.*
4. **NEW — Engine credit card count and duration.** [PROPOSAL] one card ≤1.5s. *Resolution: Phase 4 engine lock.*
5. **NEW — Pre-menu accessibility preflight vs deferring all accessibility to Options.** Preflight is leading because a player who needs colorblind mode needs it *before* the first Play click. *Resolution: decision entry if PM wants to commit.*
6. **NEW — News-ticker slot on main menu footer.** Off by default. Content ownership + moderation policy is live-ops scope. *Resolution: live-ops decision entry before launch.*
7. **NEW — Auto-Continue into last-match-mode for returning players.** Leading: no, main menu always shown (see §10). *Resolution: decision entry before Phase 6 playtest, because validation wants to measure the difference.*
8. **NEW — VO on splash / logos.** [PROPOSAL] none at launch. *Resolution: audio Phase 5.*

## 10. Alternatives considered

- **Splash-skip-after-first-run vs always-skippable.** Chosen [PROPOSAL]: always-skippable, always-shown. Alternative: auto-skip the studio+engine chain after first successful launch. Pros of alt: trims 3s from returning-player cold-launch; pros of chosen: legal/partner-contract hygiene is simpler when the chain always renders; splash is already skippable so the cost is one keystroke, not 3s; and the §3.11 returning-player budget already accommodates it. **Revisit if playtest data shows returning-player cold-launch is the #1 friction.**
- **Returning-player auto-Continue into last match vs main menu.** Chosen: main menu with dominant Continue CTA. Alternative: launch the player directly back into the last mode without a menu beat. Pros of alt: ≤2 clicks to play. Pros of chosen: a menu beat is *orienting*, not friction — the player confirms they want this session to continue the last thing, rather than being dropped in. Also: a Continue-skip path that bypasses the cloud-conflict dialog would be a correctness bug. **Revisit only if playtest retention data demands it.**
- **Unclaimed-rewards as banner vs modal vs badge.** Chosen: banner (§4.3). Modal rejected for the trust cost (§7.4 identity constraint on monetization hygiene). Persistent badge rejected because it never stops shouting and trains the player to ignore it. Banner is dismissable per session and re-surfaces only on new unclaimed content.
- **Accessibility preflight overlay vs Options-only.** Chosen: preflight + Options. Options-only rejected because it buries the decision behind the very clicks that the player with impairments can't comfortably make yet. Preflight-only rejected because it becomes noise for returning players who already set preferences.
- **Patch prompt mid-splash vs at main menu.** Chosen: at main menu. Mid-splash rejected because it interrupts the only unskippable-feeling beat and surfaces a choice before the menu context is loaded.

## 11. Verification

Goal inherited from the stub: **a first-time player reaches Stage 01 within 30 seconds of launch, feeling oriented, not flooded.** Additional measurable criteria for Draft → Stable promotion at Phase 6:

1. **Click budget conformance.** Instrumented: ≥95% of first-time sessions reach in-match in ≤6 clicks; ≥95% of returning sessions reach in-match in ≤3 clicks. Violations are bugs, not polish.
2. **Accessibility preflight engagement.** ≥90% of first-time players see all four preflight affordances (colorblind / subtitles / text scale / input remap) before their first Play click. Measured by the preflight overlay impression event; dismissing without interaction still counts as "seen." Non-dismissed overlays are a bug.
3. **Returning-player Continue latency.** Median clicks from launch to *playing* (not just menu-present) ≤2 for returning players who have a resumable state.
4. **Cold-launch time-to-menu.** p75 launch-to-interactive-menu ≤6s on HDD install, ≤3s on SSD. Violation means the splash chain is competing with load time and needs trimming.
5. **Cloud-conflict correctness.** 0 silent merges across validation builds. Any save divergence raises the dialog, every time.
6. **Unclaimed-rewards friction check.** Dismiss rate of the banner within 2s of main-menu load <30% — higher means the banner is reading as noise and needs content filtering, not removal.

---

*Last reviewed: 2026-04-20. All names and numbers not cited as [LOCKED] in CONCEPT are [PROPOSAL] and revisable via decision-entry supersession.*
