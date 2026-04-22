# Decision — Commander identity floor (Phase 4 §4.1 minimum spec per commander)

**Date:** 2026-04-20
**Status:** Accepted (resolution direction). All numerical floors below are tagged **[PROPOSAL]** — they make the identity promise concrete enough to react to and to validate against in MVP, but the specific numbers are subject to revision through Phase 4 spec work and post-MVP playtest. Only the *shape* of the floor is committed.
**Reversibility:** Medium (numbers are revisable; the *existence of a floor* is the substantive commitment and it would cost a Phase 4 reopen to remove).
**Affects:** [`CONCEPT.md`](../CONCEPT.md) §3.2 (Commander system — pending amendment to point to floor) and §4.1 (Commander mechanical spec — pending amendment to embed the floor as the spec target), `CONCEPT-GAPS.md` (rows `CMDR-01`, `CMDR-02`, `AUDIO-03` migrate out on amendment; `CMDR-03` remains as Post-launch-ok), MVP scope (CONCEPT.md §5.1 — the two MVP commanders must honor this floor).

> **Rebase banner — added 2026-04-22.** This decision is **rebased (not superseded)** under the [2026-04-21 concept tightening (3/3/3 + dungeon cosmology + Ash-enabler hybrids)](2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) (Reversibility **Hard**). Rebase delta: roster scope narrows **5 launch commanders → 3**; lineage references (Sinew/Ember/Forge/Crown/Veil) are superseded by the **Ash / Nature / Prayer** prose placeholders; "two MVP commanders, one Sinew-leaning and one Ember-leaning" becomes **three launch commanders honoring the floor under the 3 lineages**. The **identity-floor shape survives intact** — portrait, silhouette, voice lines (12 [PROPOSAL]), signature, passive, lineage tilt (+15% [PROPOSAL] to affinity), progression ladder (20 [PROPOSAL]), cosmetic slots. Lineage tilt now reads against the new 3 lineages; MVP-validation framing extends to 3 commanders, not 2. See the 2026-04-21 decision §Follow-ups for the full rebase note and `concept/phase-4.md §4.1`, `concept/phase-5.md §5.1` for the cascaded amendments. Rebase banner is bookkeeping; the Accepted status stands.

Resolves: `CONCEPT-GAPS.md` rows **CMDR-01** (commander identity floor unspecified), **CMDR-02** (progression ladder depth unspecified), and **AUDIO-03** (per-commander voice-line plan). **CMDR-03** (cosmetic slot count) remains Post-launch-ok per CONCEPT-GAPS row.

---

## Decision

Each launch commander ships with a minimum identity floor consisting of:

| Component | [PROPOSAL] floor | Notes |
|-----------|------------------|-------|
| Portrait | 1 default + 1 unlockable variant | Variant is cosmetic-only; unlocks via commander progression. |
| Silhouette skin | 1 default + 1 unlockable variant | Distinct on the battle map at silhouette-forward art-direction zoom. |
| Voice lines | **12 lines [PROPOSAL]** — 3 pick / 3 victory / 3 defeat / 3 ability-cast | Routes through the Voice bus committed in the audio architecture entry. Captioned per the accessibility floor entry. |
| Signature ability | 1 (deployable as Hero Unit) | Per CONCEPT §3.2 / §3.4. |
| Passive buff | 1 (small, persistent, not match-winning) | Per CONCEPT §3.2. |
| Lineage tilt | 1 (+15% [PROPOSAL] to affinity lineage outputs) | Per CONCEPT §4.1 leading number. Tilt-not-cage principle holds. |
| Progression ladder | **20 levels [PROPOSAL] at launch** | Cosmetic + VO + portrait-frame unlocks paced across the ladder. **No gameplay-power gates** (solo-first + no-pay-to-win). |
| Cosmetic slot types | 3 named slot types: commander skin, portrait frame, map tint | Launch floor = 1 item per slot per commander (default counts as the 1; additional via store/battle-pass are Post-launch-ok). |

This floor is the **MVP validation target**: the two MVP commanders (CONCEPT §5.1, one Sinew-leaning and one Ember-leaning) must each meet this floor for the MVP to validate the "Commander = user identity" promise honestly. A commander shipped below this floor is "a skin with a stat modifier," which is the failure mode CONCEPT §7.4 explicitly calls out.

CONCEPT.md §4.1 amendment routes the floor as the per-commander spec target. CONCEPT.md §3.2 amendment points readers to §4.1 for the floor.

## Context

`CONCEPT-GAPS.md` rows CMDR-01 / CMDR-02 / AUDIO-03 collectively flag that CONCEPT.md §3.2 names the *components* of commander identity (portrait, silhouette, color, voice, passive, signature, progression) but commits no minimum *quantities*. Without quantities, "Commander = user" is a gesture, not a spec — and the MVP cannot validate the identity promise because there is no target to validate against. Industry references (Marvel Snap per-card variant + voice + Collection Level; Legion TD 2 Mastermind 10 playstyles; Clash Royale king-levels + emotes + tower skins) all ship specific per-character counts as the load-bearing identity work. CONCEPT-GAPS §2.7 synthesized a "minimum 'this is mine' floor" — this entry ratifies it with `[PROPOSAL]` numerical tags.

The entry is **Blocks-MVP** because the MVP scope (CONCEPT §5.1) names two commanders without saying what each must contain. Without the floor, MVP playtest data on "did the commander identity feel sticky" is unfalsifiable.

## Alternatives considered

- **Option A — Defer all numbers to Phase 5.** Rejected: Phase 5 is implementation planning, which means MVP scope must already be specified. Two MVP commanders without a floor cannot be implemented except by guessing the floor — which then becomes the floor by accident. Better to propose the floor explicitly and revise.
- **Option B — Lock numbers (no [PROPOSAL] tags).** Rejected: violates the placeholder discipline. No identity-spec number has been playtested. The shape is what's load-bearing; the specific 12 / 20 / 15% will move.
- **Option C — Minimum-shape-only (commit "voice lines exist," "ladder exists," but no numbers).** Rejected: useless for MVP planning. "Voice lines exist" with no count means the recording budget is unbounded; "ladder exists" with no depth means the unlock pacing is unplanned. The whole point of a floor is to size the work.
- **Option D — Higher floor (Marvel-Snap-scale variants and Collection-Level scaling into the thousands).** Rejected: scope-blowing for a two-dev team (CONCEPT §2.2). Marvel Snap is a many-dev live-service operation; copying its surface area into a two-dev team's launch is a content-explosion failure that CONCEPT §2.3 names as a top risk.
- **Option E — (Chosen.) Bundled identity floor with [PROPOSAL]-tagged numbers, sized realistically for two-dev capacity, MVP commanders honor the floor.** Names the shape and a starting point for the numbers; explicitly invites revision.

## Reason chosen

### 3x debug loop

**Loop 1 — aggressive critique.**
- "12 voice lines" is fabricated — the source critique in CONCEPT-GAPS Loop 1 already flagged this and it is being committed anyway. Cargo-culting the proposal-doc's example.
- "20 levels [PROPOSAL]" is similarly fabricated. Marvel Snap goes into thousands; Clash Royale king-levels 1–50; the entry picks 20 with no justification beyond "between."
- Cosmetic slot types (commander skin, portrait frame, map tint) duplicate what CONCEPT §3.7 already names — this entry restates without adding.
- "Lineage tilt +15%" is being re-stated from CONCEPT §4.1's existing leading number, but tagged [PROPOSAL] here, which conflicts with how it was already being treated. Either change CONCEPT §4.1 or leave it alone — restating in a new entry duplicates governance.
- The MVP validation framing assumes the MVP playtest will *test* the identity floor, but the existing MVP success metric (CONCEPT §6.4 — 70% would-play-second-match, 50% report age-persistence) does not test commander identity directly. Either the metric needs revision or the floor doesn't actually validate what the entry claims.
- "No gameplay-power gates" is restated from CONCEPT §7.4 / non-negotiables — this entry is duplicating policy.

**Loop 2 — steelman.**
- "12 voice lines" being fabricated is the *correct critique* and the [PROPOSAL] tag is the correct response. The entry's job is not to source a number from prior art (no prior art for this game exists); it is to make the floor concrete enough to react to. 12 is a sensible starting size for a two-dev team's launch (3 pick / 3 victory / 3 defeat / 3 ability is a meaningful identity surface without ballooning recording budget). If the right answer is 8 or 20, MVP playtest will surface that.
- "20 levels" sized between Clash Royale (50) and Marvel Snap (thousands) is not "between for the sake of between" — it is sized to the two-dev capacity to *author cosmetic content for 20 levels per commander* over a launch window. Higher counts force pacing problems (empty levels) or unreasonable content commitments. Lower counts feel shallow. 20 is defensible-by-sizing.
- Cosmetic slot types are restated from CONCEPT §3.7 because §3.7 names the *meta systems* (battle pass, store) without specifying *what cosmetic slots exist on the commander itself*. Naming the slots here is additive, not duplicative. CONCEPT §3.2 amendment will cross-link.
- Lineage tilt +15% being [PROPOSAL]-tagged here when CONCEPT §4.1 already states it is a *legitimate tightening* — CONCEPT §4.1 currently treats it as a "leading" number, not a locked one. The [PROPOSAL] tag is the correct status. The CONCEPT amendment does not lock it; it just consolidates the floor.
- MVP validation framing: the critique is correct that CONCEPT §6.4 metrics do not test commander identity. **This is a real gap surfaced by this entry** — addressed in Follow-ups: a Phase 6 metric for "commander re-pick rate" exists in CONCEPT §6.2 secondary questions ("Do players re-pick the same commander on match 2?"), which is exactly the identity-stickiness signal the floor enables. The metric should be promoted from §6.2 secondary to a measured MVP-success criterion at the next CONCEPT amendment pass.
- Restating "no gameplay-power gates" is correct cascade discipline — each ratified entry that touches monetization-adjacent territory must affirm the non-negotiable, not assume it. Not duplication; it is integrity.

**Loop 3 — synthesis.**
The decision survives critique with one structural sharpening:
1. Promote the "commander re-pick on match 2" question from CONCEPT §6.2 (secondary) to a measured MVP-success criterion in the §6 Validation amendment that lands in this sweep. This makes the identity floor *validatable*.

The floor shape and [PROPOSAL]-tagged numbers are the right Phase 4 commitment. Numbers move with playtest data; the shape is the load-bearing claim.

## Reversibility note

**Medium.** The numbers are revisable freely (re-tag, supersede the entry with new [PROPOSAL] numbers — no downstream code commitment yet). The *existence of a floor* — that every launch commander ships with at minimum portrait/silhouette variants, voice lines, signature, passive, tilt, ladder, and cosmetic slots — is a Phase 4 §4.1 amendment that downstream Phase 5 implementation work depends on. Reversing the floor existence (e.g., "commanders ship with no progression ladder at launch") would force MVP scope reopen and reroute every Phase 5 implementation row.

## Follow-ups

- **CONCEPT.md amendments** within this sweep: §3.2 cross-link to §4.1; §4.1 embed the floor as the per-commander spec target; §6 promote "commander re-pick on match 2" from secondary to measured MVP-success criterion; §5.1 MVP scope note that the two MVP commanders honor the floor.
- **Cross-row dependencies:** Voice bus from audio architecture entry; subtitle floor from accessibility entry; Options menu from meta-UI envelope entry (volume sliders that affect the Voice bus live there).
- **Still open / not addressed:** CMDR-03 cosmetic-slot expansion beyond the launch floor of 1-per-slot; per-commander signature ability detail (Phase 4 §4.1 per-commander writeup work); commander launch roster size (CONCEPT §7.1 #6 — separate Phase 5 decision).
- **Numerical revision triggers:** any of the [PROPOSAL] numbers should be revisited if (a) MVP playtest data contradicts the sizing (recording budget overruns, ladder feels empty), (b) art-direction contracting (Phase 4–5) changes per-commander art cost, or (c) the launch roster size decision (3 / 5 / 8) changes total content load.
