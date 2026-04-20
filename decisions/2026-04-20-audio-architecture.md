# Decision — Audio architecture (5-bus mixer + ducking + focus-loss principle)

**Date:** 2026-04-20
**Status:** Accepted (resolution direction). CONCEPT.md amendment is a separate follow-up step within this sweep; per-bus slider UI and per-channel content spec deferred to Phase 5.
**Reversibility:** Easy (no engine commitment; mixer architecture is industry-standard and trivially reconfigurable in any engine).
**Affects:** [`CONCEPT.md`](../CONCEPT.md) §3 (Phase 3 — pending amendment to add a "Audio architecture" sub-section), [`CONCEPT-GAPS.md`](../CONCEPT-GAPS.md) (row `AUDIO-01` migrates out on amendment), Phase 5 spec (per-bus slider in Options menu lives here; per-commander voice spec is `AUDIO-03` / `CMDR-01`, not this entry).

Resolves: `CONCEPT-GAPS.md` row **AUDIO-01** (no audio channels defined). Does NOT resolve `AUDIO-02` (focus-loss toggle UI — principle named here, toggle deferred), `AUDIO-03` (per-commander voice-line spec — covered by CMDR identity floor entry).

---

## Decision

The game uses a **5-bus audio mixer**: **Master, Music, SFX, UI, Voice**. The Voice bus sidechain-ducks Music and SFX during playback (industry-standard for dialogue clarity). Window focus loss mutes Music and ambient SFX in solo modes by default; competitive PvP modes leave audio running by default (so a player cannot gain advantage by alt-tabbing). Both behaviors are user-overridable in Options (Phase 5 spec). CONCEPT.md Phase 3 will gain a sub-section naming the buses + ducking + focus-loss principle. Per-bus slider UI in Options menu and per-channel content (specific SFX inventory, music tracks, voice lines) are explicitly Phase 5.

## Context

`CONCEPT-GAPS.md` row AUDIO-01 flagged that CONCEPT.md is silent on audio in every dimension — no buses named, no ducking policy, no focus-loss behavior, no soundscape described. The gap is **Blocks-vision** because a TD/TW game's feel is non-trivially carried by audio (wave-break stinger, kill SFX layering, age-gate music swell), and a reader of CONCEPT.md cannot picture what the game *sounds like* — not even at the structural level of "how many channels, who ducks who." The 5-bus baseline (Master/Music/SFX/UI/Voice) is the minimum modern shipping standard per game-audio references cited in CONCEPT-GAPS §2.6; ducking-on-Voice is industry-standard from the same sources; focus-loss-mute is a community-requested baseline (BTD6 thread cited in same).

## Alternatives considered

- **Option A — Defer audio entirely to Phase 5.** Rejected: leaves CONCEPT.md silent on audio architecture at the vision level, which is the gap. Phase 3 owns "what kinds of systems exist;" Phase 5 owns "the contents of those systems." Audio buses are a Phase 3 concern.
- **Option B — 3-bus minimum (Master / Music / SFX).** Rejected: collapses UI and Voice into SFX, which makes per-channel mixing impossible and breaks the dialogue-ducking contract. Modern shipping minimum is 5 buses for a reason.
- **Option C — 7+ bus expansion (split Ambient from SFX, split Stinger from Music, etc.).** Rejected: over-design for concept stage. The 5-bus model is extendable (Phase 5 can split Ambient out if shipping needs it); committing to 7+ now locks complexity that may not pay off.
- **Option D — Always-on audio regardless of focus.** Rejected for solo: alt-tabbing is normal solo behavior (look up a strategy, check Discord); blasting menu music at the user is hostile. Accepted-as-default for competitive: muting on focus-loss in PvP would let a player audio-cue when their opponent alt-tabs.
- **Option E — (Chosen.) 5-bus mixer + Voice-ducks-Music+SFX + focus-loss-mute default-on-solo / default-off-PvP, all overridable in Options.** Names the architecture without locking content.

## Reason chosen

### 3x debug loop

**Loop 1 — aggressive critique.**
- "Industry-standard 5-bus" is post-hoc generalization from a small sample (Unity / Unreal mixer tutorials). The "standard" varies by genre — competitive multiplayer games sometimes split Voice from VO from Comms, while narrative games merge UI into SFX.
- Default mute-on-focus-loss for solo *and* default off for PvP encodes an asymmetry that the CONCEPT.md reader will not predict — risks surprising players who switch modes.
- Naming "ducking" without specifying threshold/ratio/release is half-spec — Phase 3 should name the *principle* but the entry pretends to commit more.
- Voice bus exists but `AUDIO-03` (per-commander voice content) is a separate row — the bus sits empty until that row resolves. Risks shipping the architecture to "explain audio" while the game has no voice content.
- "Override in Options" assumes Options menu exists, which it does only because the prior decision entry (meta-UI envelope) named it. Implicit chained dependency that should be cited.

**Loop 2 — steelman.**
- The 5-bus model is the minimum that makes per-channel sliders possible without re-architecting later. Splitting further later (Ambient, Stinger) is additive; collapsing later is destructive. Picking the small-and-extendable shape is correct cascade discipline.
- The solo/PvP focus-loss asymmetry maps to a real constraint (competitive integrity, same principle as the meta-UI envelope's pause split). Documenting the asymmetry inside the same entry that names the buses is consistent with how the meta-UI envelope handled the solo/PvP split — and this entry now cites that prior entry as the precedent.
- Ducking *principle* (Voice ducks Music+SFX) without threshold/ratio/release is exactly the right Phase 3 / Phase 5 split. Phase 3 names the contract; Phase 5 sets the numbers. The critique is asking for over-specification.
- Voice bus existing-without-content is the right state for a concept doc. The bus existing makes the AUDIO-03 / CMDR-01 voice content row *land somewhere* when ratified; the alternative (no bus until content exists) creates a chicken-and-egg.
- Implicit Options dependency now cited in the Decision text and the Affects line.

**Loop 3 — synthesis.**
The decision survives critique with one sharpening:
1. Cite the meta-UI envelope precedent explicitly for the solo/PvP asymmetry — done in §Decision and in the Reason chosen via this loop.

The 5-bus + ducking + focus-loss-asymmetry shape is the right Phase 3 commitment. Numerical thresholds, slider UI, and per-channel content stay deferred.

## Reversibility note

**Easy.** No engine, no code, no content commitment. The 5-bus model is reconfigurable in Godot (AudioBus resources), Unity (AudioMixer), or Unreal (Submixes) without breaking dependent systems — the buses are namespaces, not contracts. To reverse: mark Superseded, do not file the CONCEPT.md amendment, AUDIO-01 reverts to open in CONCEPT-GAPS.md.

## Follow-ups

- **CONCEPT.md amendment** within this sweep: small Phase 3 sub-section naming buses + ducking + focus-loss principle.
- **Phase 5 spec rows** unblocked by this entry: per-bus slider UI (lives in Options); focus-loss toggle UI (`AUDIO-02`); ducking threshold/ratio/release numbers; per-channel content inventory.
- **Cross-row dependency:** Voice bus is the destination for `AUDIO-03` / `CMDR-01` voice-line content. Those rows are addressed in the CMDR identity floor entry filed in this same sweep.
- **Engine-time concern:** when engine locks (Phase 4 exit, leading Godot 4), confirm AudioBus / sidechain support meets this contract. Not blocking; Godot, Unity, and Unreal all support it natively.
