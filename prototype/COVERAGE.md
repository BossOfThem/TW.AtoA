# COVERAGE — CONCEPT feature × prototype status

**Status:** Draft v0.1 — 2026-04-20 (PROGRESS Step 3).
**Purpose:** Single source of truth for "what does the prototype actually show, and what is still only in CONCEPT.md?" Drives PROGRESS Step 4 (first coverage-driven prototype pass) by making the next gap legible.
**Scope:** Concept-phase artifact. Not a spec. Rows are claims about *what the prototype JS renders today*, not promises about what it should render.

## Legend

- **✅ In** — present in prototype and roughly faithful to CONCEPT.
- **🟡 Partial** — a slice present; CONCEPT promises more.
- **⬜ Out** — not represented in prototype at all.
- **N/A** — concept-level framing (vision, target player); nothing for prototype to implement.
- **OPEN** — CONCEPT itself has an OPEN BLOCKER or [PROPOSAL] — prototype cannot fully represent until resolved.

Column "Prototype evidence" cites where the behavior lives (`index.html` region, data file, or "—" if absent).

---

## Phase 1 — Discovery

| CONCEPT ref | Feature | Status | Prototype evidence | Gap / notes |
|-------------|---------|--------|--------------------|-------------|
| §1.1 | Vision statement | N/A | — | Framing. |
| §1.2 | Target player | N/A | — | Framing. |
| §1.3 #1 Commander identity | Player's Commander is a specific character across matches | 🟡 Partial | `commanders.json` active=commander-b; Pick scene | Only 1 playable commander (Ember B). No portrait variants, voice, ladder, cosmetics. Identity floor §4.1 unrepresented. |
| §1.3 #2 Age persistence in-match | Minute-1 tower still "yours" at minute 20 | 🟡 Partial | `deriveTowerStats()` age multipliers; 3 ages | Age compound math is real; the *feeling* of persistence across 20 min of play isn't testable at 3 waves × 3 ages scale. Minimum MVP is 5 ages (§5.1); prototype is 3. |
| §1.3 #3 Multiple ways to play | Solo + co-op + lane wars + campaign share engine | ⬜ Out | — | Prototype is single-path tutorial → match → end. No mode select, no AI skirmish, no PvP. |

---

## Phase 2 — Analysis

| CONCEPT ref | Feature | Status | Prototype evidence | Gap / notes |
|-------------|---------|--------|--------------------|-------------|
| §2.2 Match length | 5–25 min targets per mode | 🟡 Partial | `BALANCE.match.waveCount = 3`; short | Prototype match is ~2 min. Genuinely-15-min solo-TD pacing is untested. |
| §2.4a Accessibility floor [LOCKED constraint] | Top-4 GAG + WCAG 2.3.1 + AGI tagging | ⬜ Out | — | Prototype relies on color (lineage), has no remap, no subtitle system, no reduce-motion. Prototype is **pre-constraint**; updates blocked until §2.4a is in scope for the prototype. |

---

## Phase 3 — Design

| CONCEPT ref | Feature | Status | Prototype evidence | Gap / notes |
|-------------|---------|--------|--------------------|-------------|
| §3.1 Core match loop | Ages → Age Gate → fork → marketplace → next age | 🟡 Partial | `deriveWaveDefs()` wave loop; age-up via knowledge cost | Age advancement works; Age Gate UI, Divergence Fork, new-towers marketplace are all absent. |
| §3.2 Commander system | Portrait / silhouette / color / voice / tilt / passive / signature / progression | 🟡 Partial | commander-b `passive` + `signature` as text; `lineageTilt: ember`; +15% knowledge in lore | Numbers-in-text only. No portrait variants, silhouette, voice content, progression ladder, cosmetics. Per §4.1 identity floor, this is "skin with a stat modifier" territory. |
| §3.3 Five lineages | Sinew / Ember / Forge / Crown / Veil, each mechanically distinct | 🟡 Partial | `towers.json`: sinew + ember only | 2 of 5 lineages. Forge/Crown/Veil absent → no economy pillar variety, no aura multiplier, no wildcard. §3.3 "ignoring a lineage will struggle" untestable at 2. |
| §3.4 Unit categories | Towers / mobile units / special effect units + Commander Hero | 🟡 Partial | Towers only | No mobile units, no special-effect units, no Commander Hero deployment. |
| §3.5 Eleven ages | Primal → Ascendant, 11 tiers | 🟡 Partial | `towers.json.ages = ["Primal","Mudbrick","Iron"]` | 3 of 11. §5.1 MVP floor is 5 ages for age-persistence feeling to emerge. |
| §3.6 Game modes | Campaign / Skirmish / Horde / Lane Wars 1v1 / 2v2 | ⬜ Out | — | Prototype is implicit-Skirmish-against-dumb-waves. No mode select. |
| §3.7 Meta systems | Commander progression / Backpack / Battle Pass / Cosmetic Store | ⬜ Out | — | Nothing persists across "matches" in prototype (no match 2). |
| §3.9 Meta-UI envelope | Options + Pause + Quit/Save-Exit/Concede per mode | ⬜ Out | — | No Esc handler, no pause overlay, no options menu, no quit-to-menu. Prototype is forced-linear. |
| §3.10 Audio architecture | 5-bus mixer + Voice duck + focus-loss asymmetry | ⬜ Out | — | No audio of any kind in prototype. |
| §3.11 First-run flow | Splash → main menu → Commander Pick → optional tutorial → match; returning-player Continue; ≤6 / ≤3 click budgets | 🟡 Partial | Title → Pick → Tutorial → Match → End scene chain | Linear, mandatory, no skip, no splash, no main-menu variants, no Continue, no save detection. Click count from Title to in-match is in range (~3) but the flow itself is the placeholder, not the fulfillment. |

---

## Phase 4 — Specification

| CONCEPT ref | Feature | Status | Prototype evidence | Gap / notes |
|-------------|---------|--------|--------------------|-------------|
| §4.1 Commander identity floor [PROPOSAL] | Portrait+variant / silhouette+variant / 12 VO / signature / passive / +15% tilt / 20-level ladder / 3 cosmetic slots | ⬜ Out | commander-b has passive + signature *as text*; no other floor rows | Zero floor rows actually implemented. §4.1 is the highest-leverage gap for MVP-identity-validation. |
| §4.2 Divergence system | Fork pools at Steamheart / Atomic / Synthetic / Stellar | ⬜ Out | — | No fork UI, no re-skin logic; prototype caps at age 3 anyway. |
| §4.3 Hybrid system — ancestry | Adjacent lineages unlock hybrid | 🟡 Partial | `towers.json.hybrid.pair = ["sinew","ember"]`; 1 hybrid (Tank Corps) | Ancestry tag only (per [2026-04-20 prototype hybrid-pair shape](../decisions/2026-04-20-prototype-hybrid-pair-shape.md)). |
| §4.3 Hybrid discovery mechanic | Accept / randomness / gating | OPEN | — | Phase 4 OPEN BLOCKER #1. Prototype cannot meaningfully prototype this until resolved. |
| §4.4 Mobile hero units | Waypoint + mode-flags, not RTS micro | ⬜ Out + OPEN | — | Phase 4 OPEN BLOCKER #2 (control model). |
| §4.5 Special-effect units | Zones, consumables, terrain modifiers | ⬜ Out | — | Whole framework absent. |
| §4.6 Economy — Gold | Forge + wave kills → tower cost/upgrade | 🟡 Partial | wave kills → implicit gold accrual; `STARTING_GOLD_MATCH = 80`; tower costs in `towers.json` | Kills-reward present; Forge-as-producer absent (no Forge in prototype). Upgrade-cost curve present only through age multipliers. |
| §4.6 Economy — Knowledge | Ember → tech unlock | 🟡 Partial | `baseKnowledge = 1` on ember; `AGE_UP_KNOWLEDGE_COST = 50` | Used for age-up only in prototype. Tech-tree-unlock semantics not modelled. |
| §4.6 Economy — Influence | Crown → aura/fork | ⬜ Out | — | No Crown, no aura system, no forks. |
| §4.6 Mythium (multiplayer) | Workers → send creeps | ⬜ Out | — | No PvP in prototype. |
| §4.7 Enemy system | Direction B-dominant hybrid with A variety | ⬜ Out | `deriveWaveDefs()` produces generic creeps | No theming, no age-appropriate variants, no bosses. |
| §4.9 Save model | Mode-aware + commander profile + Steam Cloud | ⬜ Out | — | No persistence whatsoever in prototype. |

---

## Phase 5 — Implementation planning

| CONCEPT ref | Feature | Status | Prototype evidence | Gap / notes |
|-------------|---------|--------|--------------------|-------------|
| §5.1 MVP slice target | 2 commanders, 2 lineages, 5 ages, 1 hybrid, 1 mode, identity floor honored | 🟡 Partial | 1/2 commanders playable, 2/2 lineages, 3/5 ages, 1/1 hybrid, 1/1 mode, 0 identity-floor rows | Closest-concept-achievement row in the matrix. Step 4 default target ("second commander, Sinew-leaning") closes the 1→2 commander delta. |
| §5.4 Naming conventions [LOCKED] | Lineages / ages / towers / hybrids patterns | 🟡 Partial | Placeholder names that honor the conventions (Sinew/Ember; Primal/Mudbrick/Iron; Tank Corps) | Conventions honored; specific names still placeholder per CLAUDE.md. |
| §5.5 Engine choice | Godot 4 3D angled-ortho leading | N/A for prototype | — | Prototype is explicitly throwaway JS; engine decision is downstream (Phase 4 exit). |

---

## Summary — top coverage gaps (ranked for Step 4 prioritization)

1. **Second commander + Sinew lineage** (closes §5.1 MVP floor 1→2 commanders and 2→2 lineages, unblocks hybrid-in-context validation). *Step 4 default.*
2. **Age 4 + Age 5 stats** (closes §5.1 5-age floor; unblocks §1.3 age-persistence feeling validation per §6.1).
3. **Commander identity-floor row — portrait + silhouette visibility** (closes one §4.1 row, highest-impact for MVP identity validation per §6.4).
4. **Age-Gate UI pause** (closes §3.1 age-gate affordance gap; would also surface the first Pause-overlay affordance per §3.9).
5. **Options menu stub with audio-bus sliders** (tests the §3.10 bus model at prototype scale without requiring actual audio).

Rows 6+ (Forge/Crown/Veil lineages, divergence forks, mobile units, economy-Influence, save model, meta progression) are post-MVP-slice.

## Rows deliberately not in this matrix

- **Admin UI / concept.json** — meta-tooling, not a game feature.
- **Decision log / cascade docs** — process, not feature.
- **Audio content / art** — Phase 4+ regardless of prototype.
- **Any post-launch item** — A11Y-05, AUDIO-02, CMDR-03, FLOW-03 account-system, META-02, META-03.

---

## How to update

- When a prototype pass lands, sweep this file: bump rows from ⬜ → 🟡, 🟡 → ✅, cite new evidence.
- When CONCEPT.md adds a new sub-section, add a row.
- When a row flips ✅, consider whether the prototype still needs to demonstrate it or whether it's been absorbed into engine-target spec (Phase 5 concern).

*Document version: 0.1 — 2026-04-20 (initial matrix).*
