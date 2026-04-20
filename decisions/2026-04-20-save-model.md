# Decision — Save model per mode (bundled SAVE-01 + SAVE-02)

**Date:** 2026-04-20
**Status:** Accepted (resolution direction). CONCEPT.md amendment lands in the same sweep as this entry. Per-screen save-slot UI, cloud-conflict resolution UX, and corruption-recovery flow deferred to Phase 5.
**Reversibility:** Medium (save format touches Phase 4 data model + Phase 5 engine work; changeable later but costs refactor, not rewrite).
**Affects:** [`CONCEPT.md`](../CONCEPT.md) §4 (Phase 4 — pending amendment to add a "Save model" sub-section), [`CONCEPT-GAPS.md`](../CONCEPT-GAPS.md) (rows `SAVE-01` and `SAVE-02` migrate out on amendment; `FLOW-03` *account system* remains Post-launch-ok but this entry commits the **local profile** half that FLOW-03 relies on), [`decisions/2026-04-20-meta-ui-envelope.md`](2026-04-20-meta-ui-envelope.md) (commits Solo Campaign "Save-and-Exit" affordance — this entry now commits the format behind it), [`decisions/2026-04-20-first-run-flow.md`](2026-04-20-first-run-flow.md) (commits "Continue" branch in returning-player flow — this entry now commits what "Continue" resumes).

Resolves: `CONCEPT-GAPS.md` rows **SAVE-01** (no save model defined per mode) and **SAVE-02** (no autosave frequency / loss-window policy) as a coupled pair. Partially resolves **FLOW-03** (single local profile half committed here; account system remains Post-launch-ok).

---

## Decision

The game uses a **mode-aware save model** with a **separate always-persistent commander profile**:

| Mode | Save model | Autosave triggers | Cloud sync |
|------|-----------|-------------------|-----------|
| Solo Campaign | Manual **Save-and-Exit** (mid-mission, single slot per mission) + auto-save at mission-end | Age-gate boundaries + manual Save-and-Exit | Steam Cloud required at launch |
| Solo Skirmish (vs AI) | Per-run only; auto-save on end. **No mid-match save slot.** | End only | Steam Cloud (run summary + settings, not mid-match state) |
| Co-op Horde | Per-run only; auto-save on end (host-side). **No mid-match save slot.** | End only | Steam Cloud (host) |
| Lane Wars 1v1 / 2v2 (incl. ranked) | **None.** No mid-match save, no restart. | N/A | N/A (stats go to profile on match end) |
| Commander profile | **Always-persistent.** XP, levels, unlocked cosmetics, voice-line unlocks, portrait frames, settings, keybinds, accessibility toggles, audio-bus levels. | Continuous (debounced write on change) | Steam Cloud required at launch |

**Launch identity model:** single **local profile** per install. No account system at launch (deferred per FLOW-03 Post-launch-ok). Steam Cloud is the sync mechanism for profile + campaign saves. Launch distribution is Steam-first; other platforms (itch.io, GOG, Epic) inherit their own cloud solution when added — Steam Cloud is a *launch commitment*, not a *forever architecture*.

**No ironman default.** They Are Billions' single-save-no-manual model was rejected in the meta-UI envelope entry (Alternative D) as incompatible with the Solo Campaign / 5–25 min session profile. Ironman as an *optional Solo Skirmish modifier* is a Phase 5 concern, not a default.

**Autosave loss-window:** in Solo Campaign, the maximum loss window is one age's worth of play (age-gate autosave floor) — typically 2–4 minutes of gameplay at target match pacing. Manual Save-and-Exit tightens the window further.

## Context

`CONCEPT-GAPS.md` rows SAVE-01 and SAVE-02 collectively flag that CONCEPT.md commits no save format, autosave cadence, or per-mode persistence policy. Severity is **Blocks-launch** for SAVE-01 (solo campaign cannot ship without save-and-exit; storefront expectations require cloud sync) and **Blocks-MVP** for SAVE-02 (autosave cadence determines how much progress a player can lose, which shapes the "is this enjoyable?" MVP validation).

The coupling to the 2026-04-20 batch is load-bearing: the meta-UI envelope entry ([`2026-04-20-meta-ui-envelope.md`](2026-04-20-meta-ui-envelope.md)) commits that Solo Campaign's pause overlay includes "Save-and-Exit (mid-mission persistence)" — that is, the *affordance* exists. This entry commits the *format* behind the affordance. The first-run flow entry ([`2026-04-20-first-run-flow.md`](2026-04-20-first-run-flow.md)) commits that the returning-player branch routes "Continue" to the last in-progress state — this entry commits what "last in-progress state" means per mode. Without SAVE-01 ratified, both prior entries cite a phantom.

Industry baselines are collected in CONCEPT-GAPS §2.4 (modern TD baseline = auto-save + 1–2 slots + Steam Cloud; They Are Billions ironman as legitimate-but-explicit counterexample; age-gate autosave as genre-appropriate granularity) and not re-cited here.

## Alternatives considered

- **Option A — Single unified save model across all modes (one slot, auto-save only, no mid-match save anywhere).** Rejected: collapses the solo/competitive-integrity split that §3.9 already commits. Solo Campaign mid-mission Save-and-Exit is a legitimate player-convenience affordance; ranked PvP save would be an exploit surface.
- **Option B — Three save slots per campaign mission (Pokémon-style).** Rejected: two-dev capacity. Multi-slot save UI, slot-switching UX, and per-slot cloud sync are meaningful engineering. Single-slot-per-mission (plus the always-persistent profile) is sized to capacity and matches the genre baseline.
- **Option C — No Steam Cloud at launch; local-only, cloud in patch 1.1.** Rejected: Steam's storefront expectation for a 2026+ PC release includes cloud sync. Shipping without it invites negative reviews and "this feels like a 2015 game" commentary. Cost-to-ship-with is modest; cost-to-add-later is a data-migration problem.
- **Option D — Full account system at launch (proprietary login separate from Steam).** Rejected: explicitly scoped post-launch per FLOW-03. Two-dev team, no backend ops appetite at launch. Single local profile + Steam Cloud covers the launch surface; cross-device sync outside Steam is a v2 concern.
- **Option E — Ironman default for Solo Campaign (TAB model).** Rejected: already rejected upstream in the meta-UI envelope entry's Alternative D. Re-litigating here would contradict that entry; optional ironman *mode* is a Phase 5 concern.
- **Option F — (Chosen.) Mode-aware save model with per-mode format + always-persistent commander profile + single local profile + Steam Cloud at launch, with no-ironman-default and loss-window bounded to one age.** Matches the 2026-04-20 batch's solo/competitive split pattern; sizes to two-dev capacity; commits the launch format without locking post-launch expansion paths.

## Reason chosen

### 3x debug loop

**Loop 1 — aggressive critique.**
- Steam Cloud as a launch hard requirement locks the game's distribution to Steam-first. If the art director or publisher later pushes for day-one Epic / GOG / itch, the commitment has to be re-negotiated — and cloud rewrites aren't cheap.
- "No mid-match save in Lane Wars" duplicates a commitment already in §3.9 (meta-UI envelope) — this entry restates it without adding.
- Age-gate autosave is a specific engineering commitment (save is synchronized with an in-match event, not just a timer) — that's a Phase 4 *data model* commitment leaking into what this entry frames as a Phase 4 *save model* commitment. Two different concerns.
- "Commander profile always-persistent" with continuous-debounced-write handwaves corruption-recovery. If the profile corrupts mid-write (crash during save), the player loses all progression. No recovery path is named.
- "No ironman default" is restated from the meta-UI envelope entry — duplicated governance.
- The single-local-profile-at-launch model means families or shared PCs cannot have per-player commander progression without separate Steam accounts. That's a real UX limitation that the entry doesn't acknowledge.
- "Steam Cloud is a launch commitment, not a forever architecture" is soothing language that may be taken as permission to defer cross-platform cloud indefinitely.

**Loop 2 — steelman.**
- Steam-first at launch is already the project's *de facto* distribution reality (CONCEPT §2.2 names "user-hosted + Steam networking," engine-leading-choice is Godot-4-Steam). Committing to Steam Cloud is honesty about the launch, not a new lock. The "recontract cloud when adding Epic/GOG" path is standard practice — Hades, Hollow Knight, and every successful indie did this. Not a trap.
- Restating the Lane-Wars-no-save rule is correct cascade discipline — each entry that touches the surface must re-affirm the rule rather than assume it. The meta-UI envelope entry named the *affordance absence*; this entry names the *format absence*. Not redundant; complementary.
- Age-gate autosave *is* data-model-adjacent, and it is correctly a Phase 4 concern. The entry is Phase 4; the concern fits. The alternative (autosave on a wall-clock timer) would be game-feel-hostile — save writes mid-wave while creeps are dying is visibly wrong. Age-gate alignment is the right semantic choice.
- Corruption recovery is flagged in Follow-ups as a separate Phase 5 concern. Not handwaved — scoped. "Continuous debounced write" is the *policy*, not the *recovery protocol*. Standard save-system 101 (write-ahead log, backup-slot-on-corrupt, last-known-good) is a Phase 5 spec.
- Restating "no ironman default" is upstream-policy reaffirmation, same as the accessibility-floor entry restating "no gameplay-power gates." Integrity, not duplication.
- The single-local-profile shared-PC critique is real. Mitigation: Steam profile switching (each Steam user on a shared PC gets their own game profile). Not bulletproof (household sharing exists), but "each Steam user = each game profile" is the industry standard on PC. Accepting this is fine.
- The "forever architecture" critique is valid wording concern. Sharpened in Loop 3.

**Loop 3 — synthesis.**
The decision survives critique with two sharpenings:
1. Steam-Cloud language sharpened: "Steam Cloud is the launch-day cloud sync mechanism. Cross-platform cloud parity is a *platform-expansion deliverable* (evaluated when adding each non-Steam storefront), not a post-launch nice-to-have."
2. Corruption-recovery explicitly flagged as a named Phase 5 follow-up (below), not left as an implicit TBD.

The mode-aware shape, per-mode save formats, always-persistent commander profile, and single-local-profile-at-launch model are the right Phase 4 commitment. Recovery protocols, conflict resolution UX, and multi-slot expansion remain correctly deferred.

## Reversibility note

**Medium.** Mode-aware save model reversal would mean:
- Reverting the CONCEPT.md §4 amendment.
- Re-routing Phase 5 engine/save work if already begun (not yet; no code commitment).
- Reverting the "Save-and-Exit" affordance commitment in §3.9 Solo Campaign row, or re-filing it with a new format.
- Public-facing: if the storefront page lists "cloud save support," reversal is a commitment-break. Manageable at concept stage; increasingly hard closer to launch.

Reversal of just the numbers (e.g., changing age-gate autosave to wave-end autosave, or adding a second save slot) is Easy and does not require a full supersession — a lightweight amendment suffices.

## Follow-ups

- **CONCEPT.md amendment** within this sweep: add Phase 4 sub-section `§4.9 — Save model` with the mode table + commander-profile note + loss-window commitment. Follows the §3.9/§3.10/§3.11 pattern of adding sub-sections after the exit condition.
- **Cross-row dependencies confirmed:** meta-UI envelope (Solo Campaign Save-and-Exit affordance — format now committed); first-run flow ("Continue" branch — target state now committed); commander identity floor (cosmetic/VO/portrait-frame unlocks live on the always-persistent profile); accessibility floor (settings + keybinds + accessibility toggles persist on profile).
- **Named Phase 5 follow-ups** unblocked or newly scoped:
  - Save-corruption recovery protocol (write-ahead log / backup-slot / last-known-good).
  - Save-slot UI (mission-select screen showing save state per mission).
  - Cloud-conflict resolution UX (local-vs-cloud mismatch on launch).
  - Ironman *as an optional Solo Skirmish modifier* (not default).
  - Platform-expansion cloud parity (when adding non-Steam storefronts).
- **Still open / not addressed:** FLOW-03 account system (Post-launch-ok); multi-profile-per-install for shared-PC scenarios beyond Steam user switching (Post-launch consideration, not committed).
- **Engine-time concern:** when engine locks at Phase 4 exit (leading Godot 4), confirm Steam SDK cloud integration and `user://` write-path conventions meet this contract. Not blocking; Godot's Steam integration (GodotSteam plugin, or equivalent) supports cloud sync natively.
- **Decision dependency on §7.1 blockers:** none. This entry does not touch hybrid discovery (#1), Veil-not-the-one-nobody-picks (#9), Crown-not-boring (#10), or any other open Phase 7 question.
