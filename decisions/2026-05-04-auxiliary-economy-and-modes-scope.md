# Decision — Auxiliary economy structure + game modes ontology (Proposed)

**Date:** 2026-05-04
**Status:** Proposed (pending Round 6+ ratification)
**Reversibility:** Easy
**Affects:** CONCEPT.md (new sections pending), prototype scope (post-launch), Follow-up #7 (Divinity source), balance-pass #1 conceptual frame (`2026-05-04-balance-pass-1-conceptual-frame.md`)

---

## Proposal

Two coupled scope expansions PM raised mid-Round-5 of the balance-pass conceptual gate:

### (A) Auxiliary economy structure

A **separate building / panel / system**, present in all game modes with mode-aware content, that hosts non-tower-placement player decisions. Inspiration: Squadron TD (SC2 Arcade) send-creeps-for-income loop; Element TD research tree; BTD6 Knowledge tree + Powers; Legion TD 2 Mercenaries.

**Slot families (proposal):**

| Family | What it does | Mode-gating |
|---|---|---|
| Targeting overrides | Per-tower priority {First / Last / Strongest / Weakest / Closest} | Universal |
| Build-queue | Place towers / upgrades in a sequence the structure auto-resolves | Universal |
| Tower-count expansion | Increases (j) effective N (more buildable slots) | Universal |
| Level / upgrade / fusion choice | Surfaces (l) lifecycle decisions in one panel | Universal |
| Damage Bonus | Sustained DPS multiplier on all towers (or by archetype) | Universal |
| Economy Bonus | Sustained Tribute multiplier per kill | Universal |
| Send-troops-to-PvP-lane | Spend currency to dispatch creeps to opponent lane | PvP only |
| Call-for-help | One-shot soft-assist unit deployment for X currency | Co-op + PvE |
| Maze stone | Cheap blocker to shape pathing (upgradable to tower later) | Maze mode only |
| Send-for-Interest | Squadron-TD pattern: spending on creeps grants permanent recurring income | PvP Interest Wars |

The structure is the design answer to "more economic depth" *without* a flat banking-interest mechanic. Currency creation is **earned through aggressive plays** (sends, builds, kills) rather than passive accrual. Aligns with the player-skill-lever philosophy.

### (B) Game modes ontology — five first-class modes

| # | Mode | Lane topology | Player count | Win condition | Difficulty |
|---|------|---------------|--------------|---------------|-----------|
| 1 | **Solo Campaign** | Single-lane; map-shaped path complexity. Zoom in/out controls. | 1 | Lives > 0 at R30 | (k) Easy/Hard/Hardcore |
| 2 | **Horde Co-op** | Shared lane(s); team-mode | 2-8 | Lives > 0 at R30 | (k) + per-player-count scaling |
| 3 | **PvE Multiplayer** | 8 identical parallel lanes on shared map | 2-8 | Last alive | (k) per-player |
| 4 | **PvP Interest Wars Lane** | Per-player lane; 15-30s rounds; send-creeps-to-any-lane | 2-8 | Last alive | Player-driven, no (k) |
| 5 | **PvP Maze Lane** | Towers create the lane (Line Tower Wars pattern) + cheap stone blockers | 2-8 | Last alive (or longest survival) | Player-driven, no (k) |

Each mode consumes the balance-pass-#1 conceptual frame differently. Lane count, currency interface, win condition, and auxiliary-structure surface are per-mode declarations.

## Context

Round 5 question on Tribute carry-over interest. PM rejected interest as the gold-creation mechanic; proposed the auxiliary structure inspired by Squadron TD's send-creeps-for-income loop. Same response opened the multi-mode discussion — multi-lane scoping is mode-dependent, not a single flat decision. Both are Priority #1 per PM. Both are concept-level scope expansions affecting CONCEPT.md, the math frame, and eventual engine architecture.

Last session (2026-05-03) lost some context after a /clear that was advised "good to go" but wasn't. PM is explicit that this scope must be captured in MD form before any further AskUserQuestion rounds, so /clear is safe even if it happens unexpectedly mid-discussion. This decision exists primarily for that preservation.

## Adjacent reference points (reference, not yet researched in depth)

- **Squadron TD (SC2 Arcade)** — send-creeps-for-permanent-income loop. Two-currency analog: Income (recurring, earned by sending) + Gold (lump, earned by killing). Cooperative-survival framing.
- **Element TD (WC3 / SC2)** — research/build-tree as the auxiliary structure (player picks "elements" mid-match, unlocking towers). Tree gates the build-set.
- **Bloons TD 6** — Heroes (commander analog) + Knowledge tree (meta-progression auxiliary) + Powers (one-shot consumables).
- **Line Tower Wars (WC3)** — Maze-build mode: tower placement creates the path. Direct match for PvP Maze.
- **Legion TD 2** — auto-battler unit-deck with "Mercenaries" (send-units) economy. Direct match for PvP Interest Wars.
- **Mini Tower Defense / Pirates Tower Defense** — interest-based banking economies (the pattern PM rejected, included as the negative reference).

A proper research pass (`research/06-tw-subgenres.md` stub, planned post-Round-6) will deep-dive these.

## Open ratification axes (Round 6+)

1. **Auxiliary structure scope** — single global building? per-commander variant? per-mode variant? Modular slot system?
2. **Mode-gated vs universal** — confirm slot family table above; surface conflicts.
3. **Currency interface** — does the auxiliary structure spend Tribute, Divinity, both, or a third currency (Influence / Knowledge / Foresight-coin)?
4. **Squadron-TD send-creeps adoption** — PvP Interest Wars only? Co-op send-to-help-others? Solo offensive-mode? Kill?
5. **Mode prioritization** — which 2-3 modes are launch vs Patch-1+? PM has stated all five are first-class for design but launch surface needs scoping.
6. **Maze-mode tower-as-path** — direct conflict with hex placement model. Adopt path-builder mode as separate physics, or unify on a single grid system?
7. **Per-mode (k)** — does Easy/Hard/Hardcore apply to all modes, or are PvP modes player-driven-only?
8. **Auxiliary structure UX** — separate scene? in-match panel? per-tower right-click? separate phase between rounds?
9. **Interaction with balance-pass-#1 frame** — auxiliary upgrades that modify (a)/(c)/(e)/(f) curves cross-cut the frame. Are they additive multipliers, or first-class equation variables (s)?
10. **Co-op send-mechanics safety** — Send-creeps-to-teammate as helpful (heal-lane / income-share) or harmful (chaos-mode)? Configurable per match?

## Reason chosen (proposal-stage)

PM Priority #1 directive. Squadron TD's send-creeps economy is a battle-tested alternative to flat interest — it couples currency creation to an aggressive player-decision moment, fitting the design's player-skill-lever philosophy (not a passive multiplier). Modes ontology surfaces real launch-vs-Patch-1 trade-offs early; without it, balance-pass #1 numbers risk being tuned for a single mode and breaking the others.

## Reversibility

Easy at Proposed status. No constraints lock until Round 6+ ratifies. Once ratified, individual sub-decisions become Medium reversibility (auxiliary structure architecture sticks once code lands; mode roster sticks once first mode ships).

## Cascade impact (proposal-stage)

- **CONCEPT.md amendment pending** — §-new "Game modes" section + §-new "Auxiliary economy structure" section once mode ontology ratifies.
- **balance-pass-#1 conceptual frame** — may need extension for auxiliary upgrade variables that cross-cut (a)/(c)/(e)/(f). Likely a new variable (s) auxiliary-state.
- **Follow-up #7 (Foresight-coin)** — possibly absorbed into auxiliary structure as a third-currency decision.
- **`research/`** — `research/06-tw-subgenres.md` (new stub) for Squadron TD / Legion TD 2 / Bloons TD 6 / Element TD / Line Tower Wars / Mini-TD deep dives.

## Follow-ups

- **Round 6 AskUserQuestion** — auxiliary structure scope + slot-family ratification + currency interface + mode prioritization.
- **Round 7+ AskUserQuestion** — per-mode deep dives (one round per mode in priority order).
- **Research pass** — `research/06-tw-subgenres.md` (new) once Round 6 lands.
- **balance-pass-#1 frame extension** — variable (s) auxiliary-state if Round 6 ratifies a structure that cross-cuts the equation.
