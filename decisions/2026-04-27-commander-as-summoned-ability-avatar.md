# Decision — Commander-as-Summoned-Ability-Avatar (+ Builder unit class + historic match-arc beats)

**Date:** 2026-04-27
**Status:** Accepted
**Reversibility:** Medium
**Affects:** `concept/phase-3.md §3.2 / §3.4` (Commander system + match loop framing references); `concept/phase-4.md §4.1` (in-match presence model — new subsection); `concept/phase-4.md §4.4a` (NEW — Builder unit class); `concept/phase-4.md §4.7` (historic match-arc beats — solo-only banner extension); `decisions/2026-04-26-prototype-reshape-plan.md` (C4 Cast-bar extension + new C7 step); `decisions/2026-04-20-commander-on-field-hero.md` (status flipped → Superseded by this entry); `CASCADE.md` decisions table; `PROGRESS.md` debt note

**Supersedes:** [`2026-04-20-commander-on-field-hero.md`](2026-04-20-commander-on-field-hero.md)

---

## Amendment 2026-04-27 (later — plan-mode round 2, 8-question PM refinement pass)

After this entry was filed, PM ran an 8-question refinement pass via clickable prompts. Material changes ratified:

- **Aztec framing locked: pre-contact Montezuma II.** Cortés is OUT of all acts. La Noche Triste / "first Spanish envoy" / Spanish conquistador captain / Spanish cavalry + cannon are replaced with pre-contact analogs (Tlaxcalan war parties + named Tlaxcalan captains in Acts I-II).
- **Round-30 antagonists locked at placeholder level:**
  - **Greek — Xerxes I** (named historic). 300-ideology audit gates the lock.
  - **Aztec — two-phase boss:** Tlaxcalan war-leader (Xicotencatl-coded; mortal phase) → Tezcatlipoca avatar (myth phase). Highest content cost across the three civs; strongest "mundane outside, myth inside" execution. Adds a phase-transition spec to §4.7.
  - **Norse — Jörmungandr / Fenrir** (myth-overlay). Sub-question OPEN: which one for launch (or both, on alternating match seeds). Defer to §4.7 turn or to its own decision. ✅ **CLOSED 2026-04-27 — Jörmungandr locked** for launch round-30; Fenrir reserved for post-launch PvE / Hero-Mode. See [`concept/phase-4.md §4.7 Historic match-arc beats`](../concept/phase-4.md#historic-match-arc-beats-solo-only--new-2026-04-27) and Follow-up #11 closure below.
- **Cross-civ asymmetry note for §4.7:** round-30 antagonist tier escalates Greek (mortal) → Aztec (mortal→myth bridge) → Norse (pure myth). This is an intentional tonal arc, not an oversight. §4.7 banner extension must cite as such so it doesn't read as inconsistency.
- **Historicity tier: mixed.** Confirms 2026-04-25 (Leonidas + Montezuma II historic; Ragnar legendary). No body change.
- **Match-arc framing: myth-mode counterfactual.** "Win = myth wins; lose = history." Confirms decision-body framing in §5 of the source plan. No body change.
- **Builder labels: keep working.** Mason Crew / Priest-Builder / Thrall Gang stay as placeholders; Aztec "Priest-Builder" remains explicitly flagged for Follow-up #5 cultural consultation (caste-flattening concern — macehualtin commoners did construction, not priests).
- **§5.4 [LOCKED] Lineages-row: deletion-in-principle confirmed.** The lineage names (Sinew / Ember / Forge / Crown / Veil) and the one-syllable-kenning convention they instantiate are pure legacy of the superseded 2026-04-21 / 2026-04-24 shapes. Nothing in the current 3-civ / 4-tier / Fusion frame consumes that convention. **New Follow-up #10** below schedules a dedicated §5.4 amendment decision to delete the row and add a Civilizations row.

**Cultural-sensitivity scope (Follow-up #5) narrows materially:** Cortés-related framing exits concept docs entirely. Remaining gates are (a) Xerxes / 300-ideology audit, (b) Tlaxcalan portrayal accuracy + Mexica-Tlaxcalan relations sensitivity, (c) Aztec "Priest-Builder" caste accuracy, (d) TV-vs-history framing for Ragnar. The Norse myth-overlay round-30 boss is essentially safe (mythic figures, no living-descendant concerns).

The body of this decision below (Decision / Context / Alternatives / Loop 1-2-3 / Reversibility / original Follow-ups) is **preserved as the historical reasoning record**. Cortés appears in Loop 1 critique #4 and in the body's three-alternative enumeration; both stay as part of the trail. The decision now reflects the *resolved* state of the cultural-sensitivity question via this amendment, not via redaction.

### New follow-ups (10-11) added by this amendment

10. **§5.4 [LOCKED] amendment** — file a dedicated decision entry to (a) delete the Lineages row from §5.4, (b) add a new "Civilizations" row (pattern: real-culture proper nouns; not invented placeholders, no convention rule beyond "real cultures with native myth"), (c) preserve the historic Lineages convention rule in [`CASCADE-history.md`](../CASCADE-history.md) for archival traceability. Touches a [LOCKED] surface; cannot land in this decision and cannot land autonomously.
11. **Norse round-30 boss narrow — Jörmungandr vs. Fenrir.** Sub-options: (a) pick one for launch (cleaner content lock, ships faster), (b) both as alternating per-match-seed boss (variety + replay value, +content cost), (c) Fenrir for solo-mode + Jörmungandr reserved for future PvE/Hero-Mode content. Defer to dedicated decision when §4.7 banner extension turn lands. ✅ **CLOSED 2026-04-27** — sub-option (a) selected with inversion of (c): **Jörmungandr locked for launch round-30 Norse boss**, Fenrir reserved for post-launch PvE / Hero-Mode. Rationale: cleanest cross-civ tonal scaling (mortal → bridge → cosmic across Xerxes / Tlaxcalan→Tezcatlipoca / Jörmungandr); sea-emergence pageant gives the round-30 cinematic budget more visual room than a bound→unbound Fenrir staging; Fenrir's mythic role as slayer-of-Odin reads better as a future Hero-Mode setpiece. Banner landed in `concept/phase-4.md §4.7 Historic match-arc beats`.

---

## Decision

The Commander is **not present on the field by default**. They have three in-match surfaces and no others: (1) a 2D **identity plinth** in the HUD top-left (portrait + name + level + XP); (2) an **invisible board-wide passive**, signaled per-tower by a small icon pip overlay; (3) **active casts** (short-CD / long-CD / signature), which summon the Commander avatar onto the board to act at a target, then retreat off-board. Tower construction is mediated by a **separate civ-coded Builder unit class** (Greek Mason Crew / Aztec Priest-Builder / Norse Thrall Gang — all working labels, §5.4 untouched), specced as a degenerate mobile unit (no AI, no combat). The 30-wave match is **scored to the Commander's historic arc in solo mode only** — three 10-wave acts (Rising / Campaign / Reckoning), with the round-30 main boss being the Commander's historic antagonist (Xerxes / Cortés-or-analog / King Ælle — all gated behind cultural-sensitivity Follow-up #5). PvP retains the 2026-04-25 lane-wars shape unchanged.

## Context

The 2026-04-20 on-field-hero design (persistent 1.4× avatar + 2-cell dashed aura + Shift-click move + Q signature + non-destructible with knock-back) was implemented in the prototype as a WC3/SC2/HoMM-flavored RTS hero. At the 2026-04-26 prototype review, PM identified that this **does not match concept intent**. The Commander was never meant to stand on the board between casts; the intent is that the Commander emerges *only* when invoked, performs an evocative act (Leonidas shouts "This Is Sparta!"), and recedes — preserving tower-wars pacing while giving the Commander identity tangible in-match texture.

Four orthogonal forks were resolved in 2026-04-27 plan-mode dialog:
1. **Tower construction agency.** Commander is not the builder; a separate Builder unit handles construction. Commander-as-hero is deferred to a future game variant ("Hero-Mode") and is out of scope here.
2. **Short-CD cast frequency.** Commander emerges for *every* active cast (passive excluded), with tiered animation budgets to manage fatigue.
3. **Passive visibility.** Invisible + board-wide. Communicated via per-tower icon pip, not avatar flicker.
4. **Historic-event surface.** Full match-arc beats; 30 waves scored to the Commander's historic timeline; round-30 = historic antagonist. Solo-only.

These four answers + the supersede decision are bundled here because they form a single coherent design — separating them would produce four entries that all inherit the same scope guardrails and cultural-sensitivity gate.

## Alternatives considered

- **Option A — Keep 2026-04-20 persistent on-field hero.** Why not: contradicts PM intent ("not present by default"), drags RTS-hero mechanics (HP / aura / movement / collision) into TW pacing the 2026-04-25 ratification was designed to anchor.
- **Option B — Pure HUD commander, no on-board appearance ever.** Why not: forfeits the Leonidas-shouts-"This-Is-Sparta!" texture the PM explicitly wants. Identity collapses back to a stat chip with VO captions.
- **Option C — Big-beats-only emergence (signature only; short-CD/long-CD stay HUD).** Why not: cheaper animation budget but reduces the in-match Commander texture to ~1-2 appearances per match. PM explicitly chose every-cast emergence over this option in plan-mode.
- **Option D — Summoned-on-cast for every active + separate Builder + historic arc beats (solo-only).** (Chosen.) Preserves the locked 2026-04-25 frame, gives the Commander tangible per-cast presence, isolates RTS-hero appetite into a parked Hero-Mode without contaminating baseline TW.

## Reason chosen

### Loop 1 — aggressive critique

1. **Builder as separate unit class is scope creep.** §4.4 already has an OPEN BLOCKER on mobile-unit control. Adding spawn-walk-animate-despawn logic compounds unresolved scope. Could a 1-second "ritual bloom" VFX deliver 80% of the flavor at 10% of the cost?
2. **"Emerge every cast" animation-fatigue is cognitive, not just visual.** At 8s short-CD recharge, 3-4 emergences per minute across the back-half of a match plus Builder walk-to-plot at every purchase = noisy board. Reduce-motion toggle exists but accessibility-as-default-off means the *shipped* experience stays noisy.
3. **Full match-arc beats break shared-PvP-content.** If rounds 1-30 are scored to Leonidas's arc, what happens in PvP when Leonidas faces Ragnar? Whose arc dominates ambient beats?
4. **Cortés-as-round-30-boss is a marketing flashpoint.** Even with cultural-sensitivity pass, shipping Aztec match-arc with Cortés at climax risks coverage cycles. Asymmetric handling (Leonidas + Ragnar get historic antagonists; Montezuma gets a myth-overlay) reads as exception-handling for one demographic.
5. **Builder home-anchor → path-walk requires friendly-unit pathing the game doesn't have.** TD games typically don't path friendly units along enemy paths.
6. **Signature 4.5s is a long input-non-block window.** In PvP at round 29 under attack, losing 4.5s to your own signature breaks "signatures are match-defining."

### Loop 2 — steelman

1. **Builder vs. instant-bloom VFX.** Builder gives tangible civ flavor a shared VFX cannot — Greek masons vs. Aztec priest-builders vs. Norse thralls is "mundane outside, myth inside" operating *inside* the build moment. Mitigation: build as a **degenerate** mobile-hero (single anim, no AI, spawn-walk-despawn) — ~30% of full mobile-hero complexity; resolves §4.4 OPEN BLOCKER's no-AI-no-combat sibling case.
2. **Animation-fatigue.** PM chose every-cast knowing the trade. Mitigation isn't override — it's making short-CD emergence so brief (~1.2s) it reads as punctuation, not performance. VO rotation banks (6 alts/cmdr/short-CD) + reduce-motion toggle (§2.4a [LOCKED]) cover residual risk.
3. **PvP arc-conflict** is tractable as scope narrowing: **historic match-arc beats are solo-only**. PvP keeps 2026-04-25 lane-wars shape unchanged. Each player's HUD plays their own commander's act-framing VO only to them; shared board uses the *defender's* framing for ambient beats. Round-30 boss replaced by standard PvP victory condition (opponent's base destroyed).
4. **Cortés risk is real, and the cultural-sensitivity pass is the gate.** Shipping Cortés-as-boss was never the plan — listing is a forcing function. Three alternatives already named (Cortés analog / myth-overlay / pre-contact framing). Asymmetry across commanders is *already true* in 2026-04-25 ratification (Aztec T4 demigods skew archetypal because named demigods are obscure).
5. **Builder pathing solves as free-space lerp.** Builder walks the build-grid (not enemy-path-grid), straight-line / 4-direction shortest. Godot handles natively (separate NavigationRegion2Ds); JS prototype fakes with lerp-to-target. No general friendly-unit pathing introduced.
6. **Signature input-non-block.** Cinematic is passive-layer visual: camera nudge + audio privileged, but towers keep firing, enemies keep advancing, player can still click. Fast-mode toggle (~1.5s) lives under §2.4a [LOCKED] floor as accessibility fallback.

### Loop 3 — synthesis

Direction is structurally sound with **five guardrails**:

- **(a)** Builder is a degenerate mobile-hero (single animation, no AI, no targeting). Lives at `concept/phase-4.md §4.4a`, not as a peer of §4.4.
- **(b)** Short-CD emergence is **≤1.2s** with rotating 6-alt VO banks and reduce-motion-toggle opt-out (turns short-CD into non-avatar VFX burst).
- **(c)** Historic match-arc beats are **solo-mode only**. PvP retains 2026-04-25 lane-wars shape unchanged.
- **(d)** Cultural-sensitivity pass is a **hard gate** before any act-III antagonist locks. Cortés/Ælle/Xerxes are leading *placeholders*; none final until Follow-up #5 closes with external consultation. Asymmetric per-civ treatment (Aztec gets myth-overlay if consultation recommends) explicitly allowed.
- **(e)** Signature cinematic is input-non-blocking by default; fast-mode accessibility toggle is the fallback.

With those five, summoned-on-cast + builder-separate + historic-arc-solo is cleaner than the 2026-04-20 model, preserves all 2026-04-25 locks, and gives the Commander the tangible in-match texture PM wanted without dragging RTS-hero mechanics into tower-wars pacing.

## Reversibility note

**Reversibility: Medium.** What it would cost to undo:

- §4.1 in-match presence subsection deleted; §4.4a Builder subsection deleted; §4.7 banner extension reverted. Three concept-level edits.
- 2026-04-20 on-field-hero decision flipped Superseded → Accepted again. Banner reversal.
- Reshape plan C7 row removed; C4 Cast-bar extension removed. Plan stays Proposed throughout — no execution to roll back.
- No locked names touched. §2.4a + §5.4 [LOCKED] untouched.

Cost is bounded because no code is touched (prototype frozen until reshape plan ratified) and no [LOCKED] surface is amended. Higher-than-Easy because the 2026-04-20 supersede also reaches into prototype design intent — but no shipped artifact is on the line yet.

## Follow-ups

1. **§4.1 amendment turn** — add "In-match presence model (summoned-on-cast)" subsection with the three-surface model + three-tier cast budget + explicit non-goals + pointers to §4.4a and §4.7.
2. **§4.4a NEW subsection turn** — Builder unit class spec (civ-coded labels [PROPOSAL]; spawn-walk-anim-despawn shape; concurrency cap = 3 [PROPOSAL]; 90% refund pre-50% cancel rule; non-targetable by regular waves; boss-threat scope deferred to §4.7 ratification).
3. **§4.7 banner-extension turn** — historic match-arc beats solo-only; act-III antagonist roster (Xerxes / Cortés-or-analog / Ælle) cited as **placeholders gated behind Follow-up #5** cultural-sensitivity pass.
4. **Reshape plan addendum turn** — C4 Cast-bar extension bullet (passive pip-count display + short-CD CD arc + long-CD CD arc) and new **C7** row (gut persistent on-field avatar logic from 2026-04-20: remove aura render / Shift-click handler / Q handler / knock-back / `moveCommanderTo` / aura snapshot field; add three-tier cast-emerge animation pipeline reusing 1.4× silhouette render; add Builder class as `BuilderUnit` with `builders: [{x, y, target, ttl}]` additive snapshot field).
5. **Cultural-sensitivity pass scheduling** (Follow-up #5 from 2026-04-25) — external consultation must close before any act-III antagonist locks. Specifically: Cortés framing alternatives (analog / myth-overlay / pre-contact); 300-ideology audit for Leonidas; TV-vs-history framing for Ragnar.
6. **§4.4 OPEN BLOCKER narrowing** — note that Builder resolves the no-AI-no-combat sibling case; full mobile-hero control still open.
7. **PvP-mode arc-conflict resolution** — proposed rule (each player's HUD plays own commander VO only; shared board uses defender's act framing for ambient beats; cross-fade if both attacked) needs PvP-mode dedicated review when modes work begins.
8. **Hero-Mode parking note** — Commander-as-persistent-on-field-avatar parked as future game variant. Flag if any §4.1 / §4.4 design decision accidentally forecloses Hero-Mode compatibility.
9. **Custom Games Framework data-model flag** — keep data model flexible enough for host-side rule injection (raised by PM 2026-04-27 in expansion-context dialog).

## Surviving data surfaces from 2026-04-20

The supersede preserves the following from [`2026-04-20-commander-on-field-hero.md`](2026-04-20-commander-on-field-hero.md) for traceability:

- `commanders.json.stats.signature` string schema — still used for long-CD signature text.
- 20-level XP ladder + cosmetic slots from [`2026-04-20-commander-identity-floor.md`](2026-04-20-commander-identity-floor.md) — separate decision, unaffected.
- Silhouette-test harness from [`2026-04-20-commander-pick-identity-upgrade.md`](2026-04-20-commander-pick-identity-upgrade.md) — still runs; the silhouette is now what emerges on cast rather than a persistent sprite.

## Dying primitives from 2026-04-20

The following die under this supersede (will be removed in reshape plan C7, not before):

- Persistent on-field commander avatar render.
- 2-cell dashed aura ring + aura-scoped passive buff.
- Shift+click / `C`-toggle movement gesture + 1-move/wave cap.
- `Q` signature global aura empowerment (+20% dmg / −15% cd).
- Knock-back on enemy overlap.
- Snapshot field `commander: {x, y, lineage, cd, sigActiveTtl, auraCells}` and the two messages `{type:'commander-move'}` / `{type:'commander-sig'}`.

Replacement snapshot field: `commander: {castState, castTarget, castTtl}` (additive; guests tolerate absence) — added under reshape plan C7.
