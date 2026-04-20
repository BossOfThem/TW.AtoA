# Player Journey — Login to Match

This document describes the player experience from launching the game to finishing a match. It covers first-time experience, returning-player experience, and mid-match flow.

**All UI element names, button labels, and screen names in this document are placeholder.** Final naming and UX design are Phase 5 polish-pass responsibilities. This doc locks *flow*, not *labels*.

The **Commander is the user** throughout this document. When player-facing language says "your commander," it means the player's persistent identity.

---

## First-time player flow

### 1. Game launch

- Splash screen (studio logo, engine credit, game title reveal).
- Main menu loads.
- Audio: main theme fades in.

### 2. Main menu (first-time)

- Prominent "New Commander" button (or equivalent — label placeholder).
- Secondary options greyed out or hidden (no saves yet).
- Background: animated scene cycling through commander signature moments or heroic silhouettes.
- Audio: main theme on loop, crisp UI sounds on hover/click.

### 3. Commander selection (first visit)

- Gallery view of starter commander roster. Count is TBD (3, 5, or 8).
- Each commander displays:
  - Portrait (silhouette-forward mythic art direction).
  - Short name (placeholder until final naming pass).
  - One-line description of playstyle and fantasy.
  - Lineage affinity icon (Sinew / Ember / Forge / Crown / Veil).
  - Passive buff summary.
  - Signature ability summary.
- Hover or tap reveals backstory preview and voice line sample.
- Select button locks in the Commander. Confirmation prompt: *"This is your Commander. You can change later from the main menu."*
- Optional: player handle input (separate from commander name).

### 4. Tutorial (first-time only, always skippable)

- Skip button prominent and available on every screen.
- Tutorial structure, approximate screen count:
  1. Map view, camera controls (pan, zoom, rotate).
  2. Placing your first tower, selecting unit type.
  3. Economy basics — gold, income, upgrades.
  4. Age Gate — first age advancement moment.
  5. First hybrid discovery — adjacency trigger.
  6. Tutorial end, return to main menu with reward.
- Tutorial uses scripted waves with guaranteed outcomes. No failure state in tutorial.
- Tutorial completion rewards: small cosmetic unlock (placeholder: "Starter Crest") + initial commander XP.

### 5. Return to main menu (post-tutorial)

- Full main menu unlocked.
- Onboarding arrow points to "Play" for first match.

---

## Returning-player main menu

Top-level options (placeholder labels, to be refined in Phase 5 UX pass):

- **Play** — opens mode selection.
- **Commander** — view commander details, change commander, view progression, manage cosmetics.
- **Backpack** — inventory of gifts, components, consumables, cosmetic items.
- **Battle Pass** — current season progression track.
- **Store** — cosmetic purchases. Never gameplay power.
- **Settings** — audio, video, controls, accessibility, account.
- **Credits / About** — small corner link.

Main menu background: animated scene with parallax. If a Commander is selected, live commander portrait or idle animation in frame.

---

## Mode selection

Available options when Play is chosen:

- **Campaign** — commander-specific story missions. Progress locked to current commander. First commander's campaign unlocked by default; other commanders' campaigns unlock as you play them.
- **Solo vs AI** (Skirmish) — pick map, pick difficulty, pick any lineage restrictions. Quick game against AI.
- **Co-op Horde** — 2–4 players defending together against escalating waves. Matchmaking or private lobby.
- **Lane Wars 1v1** — competitive PvP.
- **Lane Wars 2v2** — team PvP, matchmaking or party.
- **Custom Lobby** — create user-hosted game with custom rules, invite friends.

Each mode shows:
- Short description (one sentence).
- Expected match length range.
- Unlock status (gated behind commander level or campaign progress where relevant).
- Current lobby/queue status if applicable.

---

## Mid-match flow

### Match start

- Commander banner appears with signature line (voice + text).
- Map loads. Camera sets to angled orthographic default.
- Countdown to wave 1. During countdown: initial build phase for first towers.
- Commander portrait visible in the UI corner throughout the match.

### Per-age cycle

- Wave plays out. Player defends, sends creeps (PvP modes), manages economy.
- End of wave: gold awarded, income tick.
- Every N waves or on trigger: **Age Gate** activates. Play pauses. Screen dims slightly. Age advancement visuals play.
- Age Gate offers:
  - Automatic advancement of existing towers to new age forms.
  - If fork age: 2–3 divergence fork choices.
  - New tower / unit unlocks in the build menu.
- Play resumes in new age.
- Commander's signature ability becomes available on cooldown in supported modes.

### Match end

- Victory / defeat screen.
- Stats: waves survived, towers built, creeps sent, kills, MVP lineage, final age reached.
- XP awarded to commander with visible level-progress bar.
- Battle pass progression awarded.
- Backpack drop check (chance to find evolution components, cosmetic shards).
- Options: Replay (same config), Return to Menu, Queue Again.

---

## Post-match flow

- Return to main menu.
- New unlock notifications if any: commander level up, battle pass tier, backpack item, cosmetic unlock.
- Subtle animation or highlight on unlocked content — visible but not intrusive.
- If commander leveled up: tier-up flourish, new ability tier preview.

---

## Commander surface

Inside the Commander menu (accessed from main menu):

- Current level and XP bar.
- Unlock track: cosmetics, voice lines, signature ability tiers, portrait frames.
- Signature ability description, cooldown, and current tier.
- Passive buff description.
- Lineage affinity indicator.
- Stats: matches played, wins, favorite lineage mix, favorite modes, best age reached, etc.
- **Change Commander** button. Always available. Confirmation prompt.
- Customization: equip cosmetics, voice pack, portrait frame.

**Open decision:** Does changing commander lock progression from the previous commander, or does everything carry over per-commander? Leading direction: per-commander progression (each commander levels independently), shared account-wide cosmetic and backpack inventory.

---

## Backpack surface

Inventory grid with category tabs:

- **Evolution components** — affect in-match tower upgrades or unlock paths. Earned through play.
- **Cosmetic items** — skins, tints, emotes.
- **Commander-specific items** — voice packs, portrait frames, commander cosmetics.
- **Consumables** — if the design includes any (currently uncertain; flagged for Phase 4 decision).
- **Gifts** — event or seasonal rewards.

Each item shows rarity, source, and applicable commanders / towers / maps.

---

## Battle Pass surface

Linear progression track with tiers.

- **Free track:** rewards on every tier, earnable purely through play. Includes battle-pass XP, minor cosmetics, backpack items.
- **Premium track:** unlocked by one-time seasonal purchase. Additional cosmetics on every tier. Never gameplay advantages.
- Seasonal theme applied to cosmetics (e.g., "Season of the Steamheart" — all unlocks are Steamheart-themed).
- XP earned through play. No pay-to-skip at launch.
- Season length: TBD. Leading: 10–12 weeks per season.

---

## Store surface

Cosmetic items organized by category:

- Commander skins.
- Tower/unit skins (per-lineage or cross-lineage bundles).
- Map tints (visual themes applied to all maps).
- Voice packs (replace commander voice lines with alternate sets).
- Emotes.
- Bundles.

**No item in the store provides any gameplay advantage.** This is not a marketing pledge. It is an identity constraint and will be enforced by design review. See `CONCEPT.md §7.4`.

---

## Open questions in this document

- Commander change: per-commander progression lock or shared? (Leading: per-commander XP, shared cosmetics.)
- Matchmaking UX: surface rank visibly or hide it until placement matches complete?
- Party system UX: invite flow, voice chat integration, party size limits per mode.
- Offline play: what modes work without an internet connection? Leading: Campaign + Solo vs AI always offline-capable.
- Accessibility: colorblind modes, difficulty options, input remapping, screen reader support, subtitle options.
- First-run vs returning-player menu layout — do they share structure or diverge?
- Cosmetic preview: can players try skins on their commander before purchase? (Should be yes.)
- Return-and-forget flow: does the game remind players of unclaimed rewards? How aggressively?

---

*Document version: 0.1 — initial player journey draft. All names and labels placeholder. Final UX design is a Phase 5 polish responsibility.*
