# Decision — Round 6 auxiliary-economy ratifications + "go big" doctrine (Accepted)

**Date:** 2026-05-04 (Round 6, later same day)
**Status:** Accepted
**Reversibility:** Medium (doctrine = Hard once any mode ships)
**Affects:** [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md) (advances Proposed→Accepted on 4 of 10 axes), CONCEPT.md (pending §-new "Game modes" + "Auxiliary economy structure"), Follow-up #13 numbers phase (auxiliary cross-cuts now in scope), all per-mode follow-ups.

---

## What was ratified (Round 6, 4 questions)

### Q1 — Auxiliary structure architecture
**Ratified:** **Modular slot system, mode-aware content** (PM picked Recommended).

The auxiliary structure is a single conceptual surface (one panel / building / scene) whose **slot inventory** is mode-declared. A slot is a typed plug-in (e.g. "Targeting Override", "Send-Creeps", "Maze Stone"). Each mode declares which slot families are available, gated, or absent. This collapses the single-global vs per-commander vs per-mode trilemma — the surface is universal; the *content* is mode-aware.

**Implication:** Engine architecture (Phase 4 exit) must model `AuxSlot` as a first-class polymorphic type with `mode_visibility` metadata. Content authoring per-mode is a data shape, not separate code paths.

### Q2 — Currency interface
**Ratified:** **Tribute (tactical) + Divinity (strategic) split** (PM picked Recommended).

Slots that produce *immediate-round* effect (build-queue, targeting, stone, send-creep one-shot, call-for-help) spend **Tribute**. Slots that produce *match-arc* effect (tower-count expansion, sustained Damage Bonus, sustained Economy Bonus, send-for-Interest, fusion-choice unlocks) spend **Divinity**. The split preserves Divinity's scarcity (cap 6/match) for genuinely strategic decisions, and keeps tactical fluidity priced in Tribute.

**Implication:** No third currency. Foresight-coin Follow-up #7 is now strictly a Phase-3-onward meta-progression artifact, not an in-match currency.

### Q3 — Launch surface (modes)
**Ratified:** **All 5 modes at launch** (PM rejected Recommended Solo+Horde-only scope reduction).

PM verbatim: *"We are going big or go home, there is no 'lessen load on devs' we are VERY capable and WILL complete this project regardless of scope. I can take 3 years if i have to, we are going to complete this. No holds bar."*

This locks a **project-level "no-scope-cuts" doctrine** (see §Doctrine below), not just a launch-surface decision. All 5 modes (Solo Campaign / Horde Co-op / PvE Multiplayer / PvP Interest Wars Lane / PvP Maze Lane) ship at v1.0. Patch-1+ is reserved for *new* content (additional commanders, additional civs, additional modes), never for cut-from-launch backfill.

**Implication:** Per-mode deep-dive rounds (Round 7+) will enumerate one round per mode in priority order — Solo → Horde → PvP Interest Wars → PvE-MP → PvP Maze. Each must reach ratified-conceptual-frame parity with balance-pass #1's 17-item frame before Phase 5 engine work begins.

### Q4 — Send-creeps mechanic adoption
**Ratified:** **Broad cross-mode adoption with mode-appropriate variants** (PM custom answer reinterpreted from "go big" directive — PM did not pick A/B/C/D, but the doctrine answer demands the most ambitious option).

Send-creeps is **not** a single mechanic — it is a slot family whose *target-rules* and *intent* differ per mode:

| Mode | Send-creeps variant | Intent |
|------|--------------------|--------|
| Solo Campaign | "Offensive Wave" — spend Tribute to spawn a creep wave at your own lane head, accelerating the next wave for a kill-bonus | Risk/reward DPS-pacing decision |
| Horde Co-op | "Reinforce Lane" — spend Tribute to spawn helper creeps in a *teammate's* lane (cooperative, anti-leak buffer) | Cooperative recovery |
| PvE Multiplayer | "Lane-Trade" — spend Tribute to add a creep to *your own* lane next wave; carries a kill-bonus refund. No cross-lane sends in PvE-MP. | Solo-econ optimization in parallel-lane survival |
| PvP Interest Wars | "Send-for-Interest" — spend Tribute to dispatch a creep to opponent's lane; sender accrues permanent recurring Income (Squadron TD pattern) | Adversarial economic warfare |
| PvP Maze | "Send-Through-Maze" — spend Tribute to dispatch a creep that must traverse opponent's maze; recurring Income on success | Adversarial spatial/economic |

**Co-op send-mechanics safety (Open Axis #10 from prior decision):** Resolved as **helpful-only in Co-op modes**; harmful-send is exclusive to PvP modes. No "chaos mode" toggle at launch — that's a Patch-N optional rule.

**Implication:** Slot family table in [`2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md) supersedes — "Send-troops-to-PvP-lane" row replaced by **"Send-Creeps"** universal slot family with 5 mode-variants.

---

## Doctrine — "Go Big or Go Home, No Scope Cuts"

**Status:** Project-level doctrine (Hard reversibility once any mode ships).

PM 2026-05-04 verbatim: *"We are going big or go home, there is no 'lessen load on devs' we are VERY capable and WILL complete this project regardless of scope. I can take 3 years if i have to."*

**Operative rules:**

1. **No "launch-surface" cuts.** Every conceptually ratified system ships at v1.0. Patch-1+ is reserved for *additive* content (new commanders / new civs / new modes), never for "we'll add this later" backfill of v1.0-promised features.
2. **No "lessen dev load" trades.** When Claude proposes Recommended options, dev-load reduction is *not* a tiebreaker. Conceptual completeness, mode coverage, and design integrity are the tiebreakers.
3. **Three-year horizon acceptable.** Schedule pressure is not grounds for scope cut. PM has explicitly authorized a multi-year build.
4. **Recommended-first still stands** for *conceptual* alternatives (where the question is "which design"), but Claude must NOT recommend the smallest-scope option *because* it is smallest. Recommend on design merit only.
5. **Scope expansion mid-design is normal.** Round 5's blow-up from "Tribute interest?" → "auxiliary economy + 5 modes" is the expected pattern under this doctrine, not an exception. MD-first preservation discipline (PM 2026-05-04 directive) is the safety rail.

**Anti-pattern flag:** Any future "let's defer X to Patch-1 to reduce load" recommendation by Claude must be rejected unless PM explicitly invokes a load-reduction directive that supersedes this doctrine.

---

## Round 6 advances on the 10 open axes

From [`2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md):

| # | Axis | Status |
|---|------|--------|
| 1 | Auxiliary structure scope | **Ratified** — modular slot system, mode-aware |
| 2 | Mode-gated vs universal slot families | **Partially ratified** — universal/PvP-only/Co-op-only/Maze-only buckets stand; Send-Creeps reclassified as universal-with-variants |
| 3 | Currency interface | **Ratified** — Tribute (tactical) + Divinity (strategic) split |
| 4 | Send-creeps adoption | **Ratified** — broad cross-mode adoption, 5 mode-variants |
| 5 | Mode prioritization | **Ratified** — all 5 at launch (no-scope-cuts doctrine) |
| 6 | Maze tower-as-path vs hex grid | **Open** — Round 7+ per-mode deep-dive (PvP Maze) |
| 7 | Per-mode (k) | **Open** — Round 7+ (likely: Easy/Hard/Hardcore for Solo+Horde+PvE-MP; player-driven for both PvP modes) |
| 8 | Auxiliary structure UX | **Open** — Round 7+ |
| 9 | Auxiliary cross-cut to balance-pass-#1 frame (variable (s)?) | **Open** — coupled with Q8; consume into frame extension |
| 10 | Co-op send-mechanics safety | **Ratified** — helpful-only in Co-op; harmful exclusive to PvP |

**6 of 10 axes ratified or partially ratified after Round 6.** 4 remain open for Round 7+ per-mode deep dives.

---

## Cascade impact

- **CONCEPT.md amendment scope expanded:** §-new "Game modes" must enumerate all 5 modes at launch parity. §-new "Auxiliary economy structure" must define the modular slot system + currency split + 5-variant Send-Creeps mechanic.
- **balance-pass-#1 frame extension** — auxiliary upgrades that modify (a)/(c)/(e)/(f) curves are now confirmed cross-cuts. Variable (s) auxiliary-state will be added to the frame as a first-class equation variable in a follow-up decision after Round 7+ closes.
- **Follow-up #7 (Foresight-coin)** — narrowed to Phase-3-onward meta-progression artifact only (no in-match currency role).
- **Follow-up #13 numbers-phase** — scope expanded; must produce ratified values for auxiliary slot costs (Tribute + Divinity), Send-Creeps variant costs/income-yields per mode, and cross-cut multipliers.
- **`research/06-tw-subgenres.md`** still planned; Squadron TD send-for-Interest mechanic specifics now load-bearing (PvP Interest Wars + PvP Maze variants both consume the pattern).

## Reason chosen

PM directive on every axis. The doctrine elevation makes "no-scope-cuts" a project-level constraint rather than a one-off ratification — every future Recommended-first option must be evaluated under it.

## Reversibility

Medium for the four ratified axes; Hard for the doctrine itself once any mode reaches Phase 5 engine work. Doctrine reversal would require a written PM override invoking a new load-reduction directive.

## Follow-ups

- **Round 7 (next)** — Solo Campaign deep-dive: lane topology, map-shape complexity, zoom controls, (k) tier surfacing, auxiliary slot enablement per Solo, win-condition specifics, narrative-arc carry through R30.
- **Round 8** — Horde Co-op deep-dive.
- **Round 9** — PvP Interest Wars Lane deep-dive (Squadron TD pattern specifics).
- **Round 10** — PvE Multiplayer deep-dive.
- **Round 11** — PvP Maze Lane deep-dive (Line Tower Wars pattern + hex-grid reconciliation).
- **Round 12+** — Auxiliary structure UX (Axis #8) + frame extension variable (s) (Axis #9) + per-mode (k) (Axis #7).
