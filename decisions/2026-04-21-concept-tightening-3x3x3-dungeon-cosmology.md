# Decision — Concept tightening: 3/3/3 shape + dungeon cosmology + Ash-enabler hybrids

**Date:** 2026-04-21
**Status:** Accepted
**Reversibility:** Hard
**Affects:** `CONCEPT.md` hub phase-index; `concept/phase-1.md` §1.1; `concept/phase-3.md` §3.2, §3.3, §3.5, §3.8; `concept/phase-4.md` §4.1, §4.2, §4.3, §4.6; `concept/phase-5.md` §5.1, §5.3 (§5.4 [LOCKED] UNTOUCHED); `stages/01-commander-pick.md` §2; `stages/05-age-evolution.md` §2; `stages/06-hybrids-fusion.md` §2; `README.md` critical-context #3; `CONCEPT-GAPS.md` migration tracker; `CASCADE.md` pointer + decisions table; `PROGRESS.md` session log. Rebases (does NOT supersede): `decisions/2026-04-20-commander-identity-floor.md`, `decisions/2026-04-20-age-history-flavor-mapmods.md`, `decisions/2026-04-20-commander-pick-identity-upgrade.md`.

---

## Decision

Collapse the concept's mechanical surface area to a **3 × 3 × 3** launch shape — **3 lineages** (Ash / Nature / Prayer, names placeholder), **3 tiers** (Dust / Form / Apotheosis, names placeholder) replacing 11 civilizational ages, and **3 playable commanders** at launch — under a **dungeon-cosmology** world-frame (an Ash→Altar arc, mysterious and compressed, not a civilizational timeline). Hybrids flow through a single enabler: **Ash × Nature** and **Ash × Prayer** hybridize; **Nature × Prayer does NOT hybridize**. This is the ratified structure for the concept cascade. Naming pass is explicitly deferred — `concept/phase-5.md §5.4 [LOCKED]` is NOT touched this pass; Ash / Nature / Prayer / Dust / Form / Apotheosis are prose shorthand only.

## Context

Prior structure (5 lineages × 11 ages × 5-commander roster) was load-bearing aspirational. The 2026-04-19 concept-thinness escalation paused the workflow queue; subsequent 2026-04-20 passes amended floors but kept the 5/11/5 scaffolding intact. The 2026-04-21 PM session (plan mode, four framing questions) ratified a tighter shape: enough mechanical identity to whiteboard in five minutes, small enough to ship under two-dev throughput, and thematically anchored by "Ash to Altar" as an arc (not a timeline). Docs-first — prototype reshape and playtest come after.

## PM-locked inputs (verbatim from 2026-04-21 HANDOFF)

1. **§5.4 naming conventions [LOCKED] vs. Ash / Nature / Prayer.** *"Defer naming pass. Ratify structure now; §5.4 UNTOUCHED. Ash / Nature / Prayer are thematic shorthand in prose only until a later naming-pass decision."*
2. **Tier conceptual frame.** *"Dungeon cosmology. Replace 11 civilizational ages with 3 tiers expressing an Ash→Altar arc. Placeholder tier names: Dust / Form / Apotheosis."*
3. **Hybrid mechanical model.** *"Ash as hybrid-enabler. Only Ash×Nature and Ash×Prayer hybridize. Nature×Prayer does NOT hybridize. Two hybrid families."*
4. **Pivot timing.** *"Docs first, prototype after, playtest after. Step A = concept docs pivot (this next session). Step B = prototype reshape (separate PM-gated pass). Step C = Step 5 playtest on reshaped prototype."*

World-aesthetic lock (same session, PM direct quote): *"dungeon-like and mysterious."* Reinforces `concept/phase-5.md §5.3` silhouette-forward mythic direction as load-bearing.

## Alternatives considered

- **Option A — Keep 5 × 11 × 5, amend only.** Preserve existing scaffolding; file gap-resolutions against it. Rejected: the scaffolding was the source of concept thinness (too wide to fill); amending further would compound, not resolve, the 2026-04-19 escalation.
- **Option B — 3 × 5 × 3 (three lineages, five tiers).** Tighter lineage count but retains a timeline frame. Rejected: five tiers still implies civilizational progression and works against the dungeon-cosmology aesthetic PM ratified. Does not escape the "too wide to fill" problem cleanly.
- **Option C — 3 × 3 × 3, dungeon cosmology, Ash-enabler hybrids.** (Chosen.) Matches all four locked PM answers. MVP and launch roster converge (§5.1 = full roster). Hybrid legibility is a single rule ("Ash + X"). World-frame is aesthetic, not chronological.

## Reason chosen — 3x debug loop

**Loop 1 — aggressive critique.**
- Deleting 2 lineages and 8 ages mid-concept erases mechanical surface area; a 3-commander roster may not express enough pick-variance for a tower-wars roster even at launch.
- "Dungeon cosmology" is evocative but structureless. Dust / Form / Apotheosis are three nouns, not three distinct gameplay loops. Picking the frame does not produce the tier mechanics.
- Ash-as-enabler privileges Ash mechanically — every hybrid path requires Ash as a parent. That risks a must-pick lineage or a skewed meta and violates the "all lineages have equal identity" implicit principle.
- §5.4 [LOCKED] examples are Sinew / Ember / Forge / Crown / Veil — five one-syllable nouns. Ratifying a three-lineage structure with prose shorthand Ash / Nature / Prayer creates a latent contradiction the naming-pass deferral only papers over.
- The 11-age research work (biome mapmods, per-age enemy archetypes) is silently retired without a written retirement note.
- Reversibility is labeled **Hard** yet no playtest has happened. We are ratifying shape before evidence.
- "Ash to Altar" becomes thematically load-bearing while the title remains working-only — a naming-pass landmine.

**Loop 2 — steelman.**
- 3 commanders at launch is not an expression ceiling — it is a lean-launch floor that honors two-dev throughput and industry onboarding norms from `research/03-commander-archetypes.md`. Expansion is explicitly not cascade-blocked; the shape is launch-lean, not final.
- Dungeon cosmology is an **aesthetic gate**, not a ruleset. Tier mechanics are still to be designed (A4 §4.2 / A5 §5.1); the frame constrains *what those mechanics feel like*, not what they are. Critique conflates "world-frame chosen" with "mechanics designed."
- Ash-enabler is a **legibility spine**, not a power axis. The rule "hybrids require Ash as one parent" means all hybrids read as "Ash + X" — that is readability, not supremacy. Balance sits on numbers, not topology. The asymmetry is informational, not mechanical.
- §5.4 examples are **pattern illustrations** ("one-syllable ancient noun"), not a canonical list. Ash fits the pattern; Nature and Prayer are flagged placeholders precisely because the naming pass is deferred. No silent §5.4 edit occurs. The contradiction is provisional and tracked.
- 11-age flavor work compresses rather than dies: per-age biomes collapse into per-tier biome rotation pools; per-age enemies collapse into per-tier archetypes with Dust / Form / Apotheosis accents. Step B prototype reshape carries the port.
- Hard reversibility is appropriate precisely because this is a **shape ratification**. Playtest validates the shape-as-implemented, not the shape-as-ratified; re-opening the shape post-playtest would require a fresh upstream decision, as cascade discipline demands.
- Title "Ash to Altar" is thematically load-bearing; the arc (Ash → Altar) is what's load-bearing, not the string. Title lock stays deferred.

**Loop 3 — synthesis.**
The collapse is internally consistent once three disciplines are accepted:
1. **3/3/3 is launch-lean, not a ceiling.** CONCEPT hub phase-index and §3.2 both state this explicitly so future expansion is not blocked by a mis-read of this decision.
2. **Ash-enabler is legibility, not power.** §4.3 hybrid-discovery (open blocker #1) reframes under "Ash + X" hybrids but does not close this pass; the balance question lives on numbers, not topology.
3. **Dungeon cosmology is aesthetic, not mechanical.** Dust / Form / Apotheosis carry tier identity to be *designed* (A4 / A5), under the §5.3 mysterious-compressed frame. Tier gameplay differences are still owed work.

Stop-gaps: §5.4 examples remain on the five-noun pattern; three filed decisions are **rebased** under this entry, not superseded; CONCEPT-GAPS rows that cite 5/11 counts are audited in A8; §4.3 blocker #1 remains open; the "Ash to Altar" title remains working-only.

## Reversibility note

**Hard.** Undoing this decision would require re-opening Phase 1 vision framing, Phase 3 design surface, Phase 4 identity floor, and Phase 5 MVP scope simultaneously, plus reverting the three rebased 2026-04-20 decisions and re-migrating CONCEPT-GAPS rows. Any partial undo (e.g., restoring 11 ages while keeping 3 lineages) would create cascade violations. Reversal is permitted but must be staged as an explicit upstream reopen per `CLAUDE.md` cascade discipline, not papered over.

## Follow-ups

- **A2–A12 (this session, one file per turn):** amend `concept/phase-1.md` §1.1; `concept/phase-3.md` §3.2/§3.3/§3.5/§3.8; `concept/phase-4.md` §4.1/§4.2/§4.3/§4.6; `concept/phase-5.md` §5.1/§5.3; `CONCEPT.md` hub + `README.md`; `stages/01,05,06`; audit `CONCEPT-GAPS.md`; bump `CASCADE.md` to v0.14 + log to `PROGRESS.md`; run `tools/cascade-lint.py`; commit + push to `claude/bootstrap-ata-setup-aOpao` (branch note: prior HANDOFF referenced `B2cJv`; that branch merged via PR #1 — this session develops on `aOpao`, same SHA as current `origin/main` HEAD).
- **Rebased (NOT superseded) by this entry — each gets a "rebased by 2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md" note, Status remains Accepted:**
  - `decisions/2026-04-20-commander-identity-floor.md` — identity-floor *shape* survives; roster scope narrows 5 → 3.
  - `decisions/2026-04-20-age-history-flavor-mapmods.md` — age-gate *logic* survives; `ages.json` collapses 11 → 3 (tier entries, not age entries).
  - `decisions/2026-04-20-commander-pick-identity-upgrade.md` — silhouette-test + XP-ladder logic survives; roster collapses 5 → 3.
- **Step B (separate PM-gated pass, NOT this session):** prototype reshape — `prototype/data/*.json` migrations (towers 5×11=55 → 3×3=9 base + hybrid families; commanders 5 → 3; ages 11 → 3 tiers; enemies + mapmods + events re-tier); `prototype/index.html` scene + UI updates; `tools/cascade-lint.py` schema-check updates.
- **Step C (separate PM-gated pass, NOT this session):** Step 5 playtest on the reshaped prototype → findings as dated decisions.
- **Deferred / still open after this pass:**
  - Naming pass — either reopen §5.4 to admit multi-syllable ancient nouns (Nature, Prayer, Apotheosis) or pick §5.4-compliant one-syllable placeholders. Do NOT silently edit §5.4.
  - Title lock — "Ash to Altar" remains working-only; arc is load-bearing, string is not.
  - `concept/phase-4.md §4.3` hybrid-discovery (blocker #1) — reframes under Ash-enabler, does not close here.
  - Economy currency mapping (§4.6) under 3-lineage shape — flag as OPEN in A4 if ambiguous.
  - `CONCEPT-GAPS.md` 11 un-migrated rows — audit for 5/11-count obsolescence in A8; separate PM workstream otherwise.
  - Tier-gameplay identity for Dust / Form / Apotheosis — owed to A4/A5 under §5.3 aesthetic frame.

---

*Decision author: Claude (Opus 4.7, 1M ctx). PM-locked inputs captured verbatim. 3x debug loop real. Naming pass explicitly deferred; §5.4 UNTOUCHED.*
