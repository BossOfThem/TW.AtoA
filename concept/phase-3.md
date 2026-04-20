---
**Status:** Draft
**Last reviewed:** 2026-04-20
---

# Phase 3 — Design

*The shape of the game. High-level, not detailed.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-2.md](phase-2.md). Next: [phase-4.md](phase-4.md).

## 3.1 Core match loop (shared across all modes)

*→ active drill-down: [stage 03 — match setup](../stages/03-match-setup.md), [stage 04 — in-match core](../stages/04-in-match-core.md), [stage 05 — age evolution](../stages/05-age-evolution.md).*

A match proceeds through multiple **ages** in sequence. In PvE modes, ages advance on a wave timer or wave count. In PvP modes, ages advance on a match timer or triggered event.

Between ages, an **Age Gate** pauses play and offers:
- Automatic advancement of existing towers to the next age's form.
- A **Divergence Fork** at certain gates, presenting 2–3 path choices that re-skin future ages.
- A marketplace of new towers/units unlocked by the advancing age.

Combat within an age uses standard tower wars mechanics: towers defend your lane, units attack enemy lanes (in PvP), economy drives everything.

What makes this game different is what happens *between* ages, and the fact that your starting Commander choice persists as a visible identity through the entire arc.

## 3.2 The Commander system (central feature)

*→ active drill-down: [stage 01 — commander pick](../stages/01-commander-pick.md), [stage 08 — meta progression](../stages/08-meta-progression.md). Backing research: [commander archetypes](../research/03-commander-archetypes.md).*

A **Commander** is the player's persistent identity in the game world. At first login, the player chooses a Commander from a starter roster. Each Commander has:

- A distinctive visual identity (portrait, silhouette, color accent, voice).
- A thematic backstory, usable as solo campaign framing.
- A **lineage affinity** — a +X% tilt toward one of the core lineages. Not a cage; player can still build other lineages heavily.
- A **passive buff** — small mechanical bonus that persists across matches.
- A **signature ability** — unlocks at a commander level threshold. Deployable as a Hero Unit on the battle map in supported modes.
- A **progression track** — XP, levels, unlocked cosmetics, voice lines, portrait frames.

Commanders level up through play. Towers in a match start at age 1 (Primal) and progress through ages during that match. Commander progression is match-to-match meta. Age progression is within-match tactical. These are two distinct progression systems operating at different timescales.

**Identity floor per commander** — see [§4.1](phase-4.md#41-commander-mechanical-spec-identity-floor-proposal-per-commander-writeup-open) for the minimum-shape spec (portrait + silhouette variants, voice lines, signature, passive, tilt, progression ladder, cosmetic slots). Entry: [2026-04-20 commander identity floor](../decisions/2026-04-20-commander-identity-floor.md). Numerical floors are [PROPOSAL]; shape is committed.

**Starter commander roster (placeholder names, all subject to revision):**
- Commander A — Sinew-leaning frontline specialist
- Commander B — Ember-leaning tech specialist
- Commander C — Forge-leaning economy specialist
- Commander D — Crown-leaning aura specialist
- Commander E — Veil-leaning trickster

Launch roster size: TBD. Leading options are 3 (lean launch), 5 (one per lineage), or 8 (Legion TD 2 parity). Decision deferred to Phase 5.

**"Tilt, not cage" principle:** a Sinew-leaning Commander can still build Ember-heavy mid-game. They just don't get the Sinew affinity bonus. This preserves player agency.

## 3.3 The five lineages (mechanical identity within a match)

*→ active drill-down: [stage 04 — in-match core](../stages/04-in-match-core.md).*

Each lineage fills a mechanical role that the other four cannot fill. Lineages are the *unit categories* within a match, independent of Commander choice.

- **Sinew** — the front line. High HP, high damage, low range. Takes hits, deals hits. Includes mobile melee units that can push lanes.
- **Ember** — the tech accelerator. Weak alone. Unlocks techs that buff the whole board. Tower-based but outputs are board-wide buffs, not direct damage.
- **Forge** — the economy. Generates gold, produces buffs, feeds adjacent towers.
- **Crown** — the multiplier. Aura towers. Do not kill enemies; make other towers kill them harder.
- **Veil** — the wild card. Time, terrain, debuff, reality-bend. Weird by design. Includes most of the "special effect" category units.

A player who ignores any one lineage will struggle. A player who specializes narrowly will excel in that narrow domain and fail broadly. The game is built to reward balanced lineage use, not maxed lineage use.

**Open issue:** Veil's "weird by design" role has a known failure mode of being "the one nobody picks." Specification must resolve this in Phase 4.

## 3.4 Unit categories (cross-cutting, not lineage-exclusive)

Units come in three categories:

- **Towers** — static placements. Attack within their range. Most tower-wars units are towers. Evolve through the ages.
- **Mobile units** — active units placed on the board that move along paths or patrol routes. Include melee front-liners (Sinew), skirmishers, and hero-class units. Can be directed with waypoint-style commands, not full RTS micro.
- **Special effect units** — timed abilities, temporary zones, consumables, debuff fields. Predominantly Veil lineage. Limited in placement count per match to avoid spam.

The Commander, when deployed via signature ability, acts as a Hero Unit — a special high-value mobile unit with abilities. Only one Commander Hero per player on the map at a time.

## 3.5 The eleven ages (in-match tower evolution tiers)

*→ active drill-down: [stage 05 — age evolution](../stages/05-age-evolution.md). Backing research: [theme & era](../research/02-theme-era.md) — era-spine decision pending.*

The structural backbone. Each age re-skins every lineage's towers and units. The count (eleven) is conceptual and may change. Names are placeholder.

1. Primal
2. Mudbrick
3. Iron
4. Spires
5. Alchemical
6. Steamheart
7. Atomic
8. Signal
9. Synthetic
10. Stellar
11. Ascendant

Not every match reaches all eleven ages. Match length and mode determine max age reached. Solo TD missions may cap at age 6–8. Ranked lane wars may cap at age 9–10. Special endgame modes unlock ages 10–11. This is a design lever, not a bug.

Early ages are short and brutal. Late ages are longer and more strategic. Total playtime stays within mode target.

## 3.6 Game modes (launch roster)

*→ active drill-down: [stage 02 — mode select](../stages/02-mode-select.md). Backing research: [genre pulse](../research/01-genre-pulse.md).*

1. **Solo Campaign** — story missions tied to each Commander. Progresses through ages. Introduces mechanics gradually. Non-negotiable at launch. This is how the solo promise is kept.
2. **Solo vs AI (Skirmish)** — pick map, difficulty, lineage restrictions. Quick game against AI.
3. **Co-op Horde** — 2–4 players defend shared lanes against escalating waves. User-hosted or matchmade.
4. **Lane Wars 1v1** — classic competitive tower wars PvP.
5. **Lane Wars 2v2** — team PvP, matchmaking or party.

**Post-launch expansion (not at launch):**
- **Hero Line Wars** — hero-controllable extended mode. Builds on the signature ability system.
- **Ranked** — competitive laddered play with seasons.
- **Custom modes** — community-driven, tied to modding support if we add it.
- **Roguelite TD** — single-player run-based mode that borrows TTA concept ideas.

## 3.7 Meta systems (between-match progression)

*→ active drill-down: [stage 07 — match end](../stages/07-match-end.md), [stage 08 — meta progression](../stages/08-meta-progression.md). Backing research: [monetization & live-ops](../research/04-monetization-liveops.md).*

1. **Commander progression** — XP, levels, unlocks (cosmetics, voice lines, commander passive tiers, signature ability tiers).
2. **Backpack / Inventory** — gifts, evolution components, consumables, cosmetic items. Earned through play or events. Inventory UI in main menu.
3. **Battle Pass** — seasonal progression track. Free tier earnable by playing. Premium tier unlocked by purchase, rewarding cosmetics only (never gameplay power).
4. **Cosmetic Store** — skins, emotes, commander voice packs, map tints. Never sells gameplay advantage.

## 3.9 Meta-UI surfaces (launch envelope)

*Decision entry: [2026-04-20 meta-UI envelope](../decisions/2026-04-20-meta-ui-envelope.md). Reversibility: Easy.*

The intro-game and in-match flows surface at minimum:
- **Options** menu, reachable from both main menu and in-match Pause overlay.
- **Pause overlay** mapped to `Esc` whose contents differ by mode.
- **Quit / Save-and-Exit / Concede** path appropriate to mode.

Mode-aware split:

| Mode | Esc | Pause contents | Restart | Save | Quit |
|------|-----|----------------|---------|------|------|
| Solo Campaign | Hard pause | Resume / Options / Restart Mission / Save-and-Exit / Quit-to-Menu | Allowed | Save-and-Exit (mid-mission) | Confirm if unsaved |
| Solo Skirmish | Hard pause | Resume / Options / Restart / Quit-to-Menu | Allowed | Auto-save on end | Confirm if mid-match |
| Co-op Horde | Host-pause, vote-or-timeout (principle; spec deferred) | Resume / Options (local) / Concede / Quit-to-Menu | Disabled | Auto-save on end | Concede |
| Lane Wars 1v1 / 2v2 | Read-only overlay (state runs; local menus open) | Options / View Build / Concede / Quit-to-Menu | Disabled | None | Concede + leave |

Principle: competitive integrity > solo convenience. Exhaustive per-setting list deferred to Phase 5.

## 3.10 Audio architecture

*Decision entry: [2026-04-20 audio architecture](../decisions/2026-04-20-audio-architecture.md). Reversibility: Easy.*

5-bus mixer: **Master, Music, SFX, UI, Voice**. Voice bus sidechain-ducks Music and SFX during playback. Focus-loss behavior: mute Music + ambient SFX in solo modes by default; leave audio running in competitive PvP by default (no alt-tab audio-cue advantage). Both behaviors user-overridable in Options. Per-bus slider UI, ducking threshold/ratio/release numbers, and per-channel content (SFX inventory, music tracks, voice lines) are Phase 5.

## 3.11 First-run and returning-player flow

*Decision entry: [2026-04-20 first-run flow](../decisions/2026-04-20-first-run-flow.md). Reversibility: Easy. Full per-screen spec owner: [stages/00-session-start.md](../stages/00-session-start.md).*

**First-run path** (no save): launch → splash (≤3s, skippable) → main menu (first-time variant, no Continue) → New Game → Commander Pick → Tutorial with skip option ("I've played Tower Wars before — skip") → match. Tutorial completion incentivized via cosmetic reward (funded by the §4.1 identity-floor cosmetic slot), not gated.

**Returning-player path** (save detected): launch → splash (skippable) → main menu (returning variant, prominent Continue) → Continue routes to last in-progress state.

**Click budget [PROPOSAL]:** ≤6 clicks from launch to in-match for first-time; ≤3 clicks for returning.

Tutorial style: **contextual + interactive + skippable**, not pop-up-based. Per-screen spec is Phase 5 (stage 00 + stage 01).

## 3.8 Exit condition for Phase 3

The shape of the game can be drawn on a whiteboard in five minutes: commanders, five lineages, eleven ages, three unit categories, five launch modes, four meta systems. Nothing in Phase 4 introduces a new system that contradicts Phase 3.

→ **Hand off to [Phase 4](phase-4.md).**
