# Decision — First-run flow (Phase 3 click-budget + returning-player branch + skippable tutorial)

**Date:** 2026-04-20
**Status:** Accepted (resolution direction). CONCEPT.md amendment is a separate follow-up step within this sweep; full per-screen flow spec lives in `stages/00-session-start.md` (currently Stub) and is Phase 5 work.
**Reversibility:** Easy (the click-budget and branch principles are revisable; no engine commitment).
**Affects:** [`CONCEPT.md`](../CONCEPT.md) §3 (Phase 3 — pending amendment to add a "First-run and returning-player flow" sub-section), [`stages/00-session-start.md`](../stages/00-session-start.md) (Stub becomes the owner of the eventual full-flow spec), `CONCEPT-GAPS.md` (rows `FLOW-01`, `FLOW-02`, `ONBOARD-01` migrate out on amendment; `FLOW-03` remains as Post-launch-ok).

Resolves: `CONCEPT-GAPS.md` rows **FLOW-01** (no first-run flow described), **FLOW-02** (no returning-player branch), and **ONBOARD-01** (tutorial mandatory / non-skippable). **FLOW-03** (account / save-profile concept) remains Post-launch-ok per CONCEPT-GAPS row (single local profile + Steam Cloud at launch).

---

## Decision

The intro flow is committed as follows:

**First-run path** (no save detected):
1. Launch → splash (≤3s, skippable on any input).
2. Main menu (first-time variant: prominent "New Game," secondary "Skirmish," "Options," "Quit"; no "Continue").
3. New Game → Commander Pick.
4. Commander Pick → Tutorial **with skip option** ("I've played Tower Wars before — skip tutorial" path lands the player in their first Skirmish or Campaign mission directly).
5. Tutorial-completion **incentivized via cosmetic reward**, not gated (skipping does not lock content).

**Returning-player path** (save detected):
1. Launch → splash (skippable).
2. Main menu (returning variant: prominent "Continue" — resumes last save / mission; secondary "New Match," "Commander Select," "Options," "Quit").
3. "Continue" routes directly to last in-progress state. No re-tutorial, no re-pick, no re-confirm.

**Click budget [PROPOSAL]:** ≤6 clicks from launch to in-match for a first-time player; ≤3 clicks for a returning player using "Continue."

**Tutorial is contextual + interactive + skippable**, not pop-up-based. (Per CONCEPT-GAPS §2.2 best-practice synthesis.) The actual per-screen tutorial spec lives in `stages/00-session-start.md` and `stages/01-commander-pick.md` (both currently Stub) and is Phase 5 work.

CONCEPT.md Phase 3 will gain a sub-section naming the flow shape, click-budget principle, and returning-player branch. CONCEPT.md does **not** absorb the full per-screen flow — that lives in stage 00.

## Context

`CONCEPT-GAPS.md` rows FLOW-01 / FLOW-02 / ONBOARD-01 collectively flag that CONCEPT.md describes neither the first-run intro flow nor the returning-player branch nor the tutorial-skip option. Severity is **Blocks-vision** (FLOW-01) because Claude or any reader cannot picture *what the player does in their first 60 seconds* without this. Industry best-practice 2025 is "meaningful victory in first 5 clicks" with skippable tutorial — citations in CONCEPT-GAPS §2.2 / §2.8. The 2026-04-19 PM playtest experienced the prototype's forced-linear flow (Title → Begin → Pick → Take the field → Tutorial → Match → End with no skip) as one of the load-bearing thinness symptoms.

## Alternatives considered

- **Option A — Defer entire flow to `stages/00-session-start.md` Phase C draft.** Rejected: leaves CONCEPT.md silent on flow shape at the vision level. The stage doc is the right home for *per-screen detail*; CONCEPT is the right home for *what the flow looks like at all*. Both are needed.
- **Option B — Mandatory tutorial (no skip, completion required to unlock other modes).** Rejected: violates onboarding best practice 2025 (skippable / exitable / meaningful-victory-in-first-5-clicks). TW/TD veteran target player (CONCEPT §1.2 — players who finished BTD6, KR5, LTD2) will rage-quit a forced tutorial.
- **Option C — Tutorial-skippable but no skip incentive.** Rejected: loses the cosmetic-reward design lever that drives completion among the players who *would* benefit from the tutorial. Cost-of-incentive is one cosmetic per commander; benefit is meaningfully higher tutorial-completion among players who self-identify as new but might otherwise skip out of inertia.
- **Option D — No returning-player branch (always show full main menu, never auto-resume).** Rejected: violates ≤3-click target for returning players, which is exactly the audience that retention metrics (CONCEPT-GAPS §2.2 — D1 / D7 retention benchmarks) are most sensitive to.
- **Option E — (Chosen.) Two-path flow (first-run / returning-player), skippable tutorial with cosmetic-completion incentive, click-budget targets [PROPOSAL]-tagged.** Names the shape and the targets; defers per-screen detail to the stage doc.

## Reason chosen

### 3x debug loop

**Loop 1 — aggressive critique.**
- "≤6 clicks to in-match" and "≤3 clicks for Continue" are fabricated — sources cite ≤5 clicks for mobile onboarding generally; transposing to a PC-first TW game is an unjustified leap.
- "Cosmetic reward for tutorial completion" requires an actual cosmetic to exist per commander, which is now an art commitment riding on a flow decision.
- "Save detected" branching assumes a save-profile concept that the entry simultaneously declares "Post-launch-ok via FLOW-03." Either save-detection works at launch (need a profile concept) or it doesn't (no Continue button).
- Skip-tutorial for veterans assumes the game can detect veteran status; otherwise every player sees and chooses the skip prompt, which is itself a friction surface.
- The two-path flow creates a UI-state-machine commitment (main menu has two variants) that should be a Phase 5 spec, not a Phase 3 commit.
- ONBOARD-01 resolution claims tutorial is "contextual + interactive" but the entry defers all per-screen detail to the stage doc — the resolution is therefore content-free at this entry's level.

**Loop 2 — steelman.**
- Click-budget numbers are tagged [PROPOSAL] *because* they are starting points, not locks. The 5-click mobile baseline is the closest published reference; +1 click for PC's typically-richer main menu is defensible. Numbers move with first-week playtest data.
- Cosmetic-reward-for-tutorial-completion does require a cosmetic per commander, which is *already* committed in the commander identity floor entry's cosmetic slot floor (default + 1 unlockable variant per slot type). The "1 unlockable variant" can be the tutorial-completion reward. No new art commitment beyond what the identity floor already commits.
- Save-detection for the Continue branch does *not* require a full account-system; it requires a single local profile (FLOW-03's "single local profile at launch"). FLOW-03 is Post-launch-ok in the sense that *account systems* are deferred; *local profile* is launch-ready. The critique conflates account ≠ local profile.
- Skip-tutorial prompt as friction: a single prompt on Commander Pick → match transition ("First time playing Tower Wars? [Yes, show me / No, skip tutorial]") is one extra click for everyone, which fits inside the 6-click budget and pays for itself in not force-tutorial-ing veterans. The friction is bounded.
- Two-path main menu is a *Phase 3 surface* commit (the menu has two states) and a *Phase 5 spec* (what each state's affordances look like in detail). Phase 3 owns "the menu has a Continue affordance when save exists;" Phase 5 owns "the Continue affordance shows the last commander's portrait in a 64×64 frame at the top-left." Same split as the meta-UI envelope entry — surfaces here, contents there.
- ONBOARD-01 resolution being "contextual + interactive + skippable" is a *commitment to a tutorial style*, not a per-screen spec. Tutorials can be pop-up-based (modal text walls), tooltip-based (passive on-hover), or contextual-interactive (the player learns by doing within the actual match). The entry commits to the third style. That is substantive, not content-free.

**Loop 3 — synthesis.**
The decision survives critique with one sharpening:
1. Explicitly cite the commander identity floor entry as the source of the cosmetic that funds the tutorial-completion reward — done in §Decision (implicit) and tightened in this loop.

The flow shape, click-budget [PROPOSAL] numbers, returning-player branch, and contextual-interactive tutorial style are the right Phase 3 commitment. Per-screen detail correctly defers to stages/00.

## Reversibility note

**Easy.** No engine, no code, no per-screen art commitment. To reverse: mark Superseded, do not file the CONCEPT.md amendment, FLOW-01/02 + ONBOARD-01 revert to open in CONCEPT-GAPS.md, stages/00-session-start.md remains Stub. Click-budget numbers can move freely without supersession (re-tag in stage 00 spec when it lands).

## Follow-ups

- **CONCEPT.md amendment** within this sweep: small Phase 3 sub-section naming the two-path flow shape, click-budget [PROPOSAL] targets, returning-player branch, contextual-interactive-skippable tutorial commitment.
- **`stages/00-session-start.md`** remains Stub but its scope is now anchored to this entry — Phase C draft work (PROGRESS.md Step 8) will spec the per-screen detail against this entry's commitments.
- **Cross-row dependencies:** main-menu surface from the meta-UI envelope entry; cosmetic-reward funded by the commander identity floor entry; subtitle/colorblind compliance from the accessibility floor entry; audio cues from the audio architecture entry.
- **Still open / not addressed:** FLOW-03 (account system) deferred Post-launch-ok; per-commander tutorial-completion cosmetic content (Phase 5); save-profile-corruption recovery flow (Phase 4 / save model — `SAVE-01` / `SAVE-02`, not in this sweep); offline-mode handshake (stage 00 Open Question, deferred).
- **Click-budget revision trigger:** post-MVP playtest data on first-time-player time-to-in-match; if median exceeds the [PROPOSAL] budget, the budget revises (not the player).
