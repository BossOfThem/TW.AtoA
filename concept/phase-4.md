---
**Status:** Draft
**Last reviewed:** 2026-04-21
---

# Phase 4 — Specification

*Detailed system design. This is where the game actually becomes a game.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-3.md](phase-3.md). Next: [phase-5.md](phase-5.md).

## 4.1 Commander mechanical spec (identity floor [PROPOSAL], per-commander writeup OPEN)

*Decision entry: [2026-04-20 commander identity floor](../decisions/2026-04-20-commander-identity-floor.md) (rebased by [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) — floor shape survives unchanged; roster scope narrows 5→3 per `concept/phase-3.md §3.2`). Reversibility: Medium (numbers revisable; floor-existence is Phase 4 commitment).*

Each of the **3 launch commanders** (Commander A / B / C — Ash / Nature / Prayer-leaning per §3.2) ships with a minimum identity floor (numbers [PROPOSAL], shape committed):

| Component | [PROPOSAL] floor |
|-----------|------------------|
| Portrait | 1 default + 1 unlockable variant |
| Silhouette skin | 1 default + 1 unlockable variant |
| Voice lines | 12 lines (3 pick / 3 victory / 3 defeat / 3 ability) — routes through §3.10 Voice bus; captioned per §2.4a |
| Signature ability | 1 (deployable as Hero Unit per §3.4) |
| Passive buff | 1 (small, persistent, not match-winning) |
| Lineage tilt | +15% to affinity lineage outputs |
| Progression ladder | 20 levels at launch; cosmetic + VO + portrait-frame unlocks paced across. **No gameplay-power gates** (solo-first + no-pay-to-win). |
| Cosmetic slot types | 3: commander skin, portrait frame, map tint. Launch floor = 1 item per slot per commander (default counts as the 1). |

A commander shipped below this floor is "a skin with a stat modifier" — the failure mode §7.4 explicitly calls out.

Each Commander also gets a one-page mechanical writeup before Phase 4 exits, covering:
- Signature ability specifics (cooldown, duration, effect, visual).
- Passive buff specifics.
- Unlock path for cosmetics and voice lines (by commander level within the 20-level ladder).
- Solo campaign storyline (outline only at Phase 4; full script in Phase 5 polish).

## 4.2 Divergence system

*→ active drill-down: [stage 05 — age evolution](../stages/05-age-evolution.md). **Rescoped OPEN** under the 3-tier Ash→Altar arc per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md).*

At tier transitions, the player picks a fork that re-skins every lineage's expression for that tier and all future tiers of the match. The fork does not change the lineage's mechanical role — it changes how that role is expressed visually and subtly mechanically (damage types, tempo, etc.).

Under the 3-tier arc there are at most **2 tier-transition forks** per match (Dust→Form, Form→Apotheosis); prior 4-fork × 3-option (81-path) variety math no longer applies. New fork pool and per-fork-option themes are **OPEN** — they must:
- Sit inside the dungeon-cosmology aesthetic (`concept/phase-5.md §5.3`).
- Express the Ash→Altar arc rather than a technology timeline.
- Preserve enough combinatorial variety that two matches on the same commander feel different.

**Placeholder shape (not ratified):**
- **Dust → Form fork:** 3 options, themes OPEN (candidates: salvage-lean / bloom-lean / rite-lean as tier-coloration).
- **Form → Apotheosis fork:** 3 options, themes OPEN (candidates: ascension / descent / threshold).

Run variety ceiling under 2×3=6 paths is narrow; heirloom / commander-affinity / mapmod layering may reopen breadth. Full fork design is a Phase 4/5 deliverable under the new tier frame.

## 4.3 Hybrid system

*→ active drill-down: [stage 06 — hybrids & fusion](../stages/06-hybrids-fusion.md). **Contains OPEN BLOCKER** (discovery mechanic — reframed, not closed, by Ash-enabler model).*

**Hybrid model — Ash-enabler (locked 2026-04-21).** Hybrids flow through Ash as a structural spine, not a power axis. Two hybrid families exist at launch:

- **Ash × Nature** — salvage + growth hybrids (decay-fed regeneration, scavenged bloom).
- **Ash × Prayer** — salvage + order hybrids (reliquary-aura towers, consecrated ruins).
- **Nature × Prayer does NOT hybridize.** This is structural per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md); a pure-order / pure-growth pairing expresses its interaction through stacking lineage buffs, not a new tower class.

When Ash is placed adjacent to Nature or Prayer and held adjacent for a threshold duration, a hybrid evolution unlocks in the tech tree. The player can then build the hybrid unit.

**Legibility payoff of Ash-enabler:** every hybrid reads as "Ash + X," so the rule is whiteboard-explainable and the hybrid family count is bounded (2 at launch) — no combinatorial explosion across lineage pairs. This replaces the prior 5-pair starter table (Sinew+Ember / Forge+Crown / Ember+Veil / Crown+Sinew / Forge+Veil), which is **superseded by this decision**.

Target count: 4–8 hybrid units across the 2 families × 3 tiers, with placeholder table deferred to Phase 5 under the new naming convention.

**OPEN BLOCKER — hybrid discovery mechanic (reframed under Ash-enabler):** Unlock via adjacency still creates rote placement once players learn pairings. With only 2 families the wiki-breaks-discovery problem is smaller (2 entries, not 5+), but the blocker is not closed. Resolution options remain:
1. Accept it. Discovery is a first-run experience; rote placement is fine for veterans.
2. Add randomness. Hybrids have a probabilistic unlock on adjacency, with heirloom/meta boosts.
3. Gate knowledge. Hybrid knowledge is per-commander or per-account, unlocked through play.

Decision required before Phase 5 begins.

## 4.4 Mobile hero units specification

*→ active drill-down: [stage 04 — in-match core](../stages/04-in-match-core.md). **Contains OPEN BLOCKER** (control model).*

Mobile units need:
- Movement speed per unit tier.
- Pathing mode (patrol, follow lane, direct to waypoint, attack-move).
- Engagement rules (auto-engage, hold, fall back).
- Control complexity: waypoint + mode flags, NOT full RTS per-unit micro.

**OPEN ISSUE:** Exact control model. Full RTS per-unit micro is scope-blowing and wrong genre. Waypoint + mode flags is achievable. Attack-Move command is useful. Must resolve before unit spec work starts.

Commander Hero Units (signature ability deployments) have richer control — direct movement + 2–3 abilities + return-to-base. One active Commander Hero per player per match.

## 4.5 Special effect units specification

Special effect units are limited in placement count per match to avoid spam. Examples:
- Timed zones (debuff aura for 20 seconds).
- Consumables (one-shot damage bursts, healing pulses).
- Terrain modifiers (Veil: create a tar pit, destroy it next age).

Each special effect has a cooldown, a cost, and a visible indicator on the map. Specification per-item is a Phase 5 task; Phase 4 locks the *framework* only.

## 4.6 Economy specification

*→ active drill-down: [stage 03 — match setup](../stages/03-match-setup.md), [stage 04 — in-match core](../stages/04-in-match-core.md). **Currency mapping rescoped OPEN** under 3-lineage shape per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md).*

Prior three-currency mapping (Gold / Knowledge / Influence from Forge / Ember / Crown, with Sinew + Veil as pure consumers) no longer applies — the lineages that backed those pillars don't exist in the 3-lineage shape. Under Ash / Nature / Prayer, the "every build must touch an economy lineage" invariant is auto-satisfied (only 3 lineages exist; any build touches at least one), so the prior *structural enforcement* of economy breadth is replaced by the lineage count itself.

**Placeholder mapping [PROPOSAL] — flagged OPEN for Phase 4 resolution:**
- **Gold** — generated by Nature towers (growth / economy pillar) and wave kills. Spent on tower placement and tower upgrades.
- **Faith** — generated by Prayer towers (aura / order pillar). Spent on aura upgrades and fork choices.
- **Cinders** — generated by Ash towers and tower losses / recycles. Spent on hybrid crafting and salvage-line upgrades. The salvage-loop is a load-bearing identity piece: Ash is the only lineage that converts *losing* towers into currency.

**Multiplayer-only fourth currency (unchanged from prior spec):**
- **Mythium** (placeholder) — time-based income from workers (Legion TD 2 pattern). Spent on sending creeps/mercenaries to opponent lanes.

**OPEN under new shape:**
- Whether all three lineages produce currency (breadth-by-default) or whether one lineage is a pure consumer (breadth-by-constraint). Prior design used a producer/consumer split for deliberate tension; with a 3-lineage roster, making any one lineage pure-consumer risks making it skip-able.
- Currency names (Gold / Faith / Cinders) are placeholders, not §5.4-ratified.
- Hybrid-crafting cost model (does Cinders gate hybrid unlock, or just accelerate?) — depends on §4.3 blocker #1 resolution.

Bookkeeping is standard; balance work is extensive and deferred to Phase 5 under the new shape.

## 4.7 Enemy system (PvE modes)

Two directions:
- **A — Parallel evolution.** Enemies march through the ages alongside the player. Stone beasts → bronze raiders → iron barbarians → etc.
- **B — The Left Behind.** Enemies are what humanity abandoned at each age. Beasts we displaced. Plagues we outgrew. Gods we stopped believing in. Machines we discarded. Finally: past versions of ourselves.

**Leading direction: hybrid — B-dominant with A as wave-variety baseline.** Regular waves use Direction A patterns (parallel evolution, easier to art and balance). Age bosses and special waves use Direction B (thematically rich, marketing-heavy). This gets you the trailer moments without tripling the art burden.

Decision required before Phase 5 begins.

## 4.9 Save model

*Decision entry: [2026-04-20 save model](../decisions/2026-04-20-save-model.md). Reversibility: Medium.*

Mode-aware save model + always-persistent commander profile:

| Mode | Save | Autosave | Cloud |
|------|------|----------|-------|
| Solo Campaign | Manual Save-and-Exit (single slot per mission) + auto-save at mission-end | Age-gate boundaries + manual | Steam Cloud |
| Solo Skirmish | Per-run only; auto-save on end | End only | Steam Cloud (summary + settings) |
| Co-op Horde | Per-run only; auto-save on end (host) | End only | Steam Cloud (host) |
| Lane Wars 1v1 / 2v2 | None (no mid-match save, no restart — per §3.9) | N/A | Stats to profile on end |
| Commander profile | Always-persistent (XP, unlocks, cosmetics, settings, keybinds, audio levels, accessibility toggles) | Continuous (debounced) | Steam Cloud |

**Launch identity model:** single local profile per install. No account system at launch (FLOW-03 Post-launch-ok). Steam Cloud is the launch-day sync mechanism; cross-platform cloud parity evaluates per storefront on expansion.

**No ironman default** (reaffirmed from §3.9 Alternative D). Ironman as an optional Solo Skirmish modifier is a Phase 5 concern.

**Autosave loss-window:** in Solo Campaign, capped at one age's worth of play (age-gate autosave floor) — typically 2–4 minutes at target pacing.

Per-slot UI, cloud-conflict resolution UX, corruption-recovery protocol, and multi-profile-per-install are Phase 5.

## 4.8 Exit condition for Phase 4

- Commander spec complete (one-page per commander).
- Hybrid discovery mechanic resolved.
- Mobile unit control model resolved.
- Enemy direction locked.
- Economy balanced on paper (spreadsheet with currencies, costs, income curves).
- Monetization model specifics resolved.
- Engine choice locked.
- Art director engaged or scoped.

→ **Hand off to [Phase 5](phase-5.md).**
