# Decision — Meta-UI envelope (settings menu + pause/meta-controls bundle)

**Date:** 2026-04-20
**Status:** Accepted (resolution direction). CONCEPT.md amendment is a separate follow-up step; this entry only ratifies direction.
**Reversibility:** Easy (no spec text written into CONCEPT.md by this entry; only direction is committed).
**Affects:** [`CONCEPT.md`](../CONCEPT.md) §3 (Phase 3 — pending amendment to add a "Meta-UI surfaces" sub-section), [`CONCEPT-GAPS.md`](../CONCEPT-GAPS.md) (rows `SETTINGS-01` and `PAUSE-01` migrate out on amendment), [`stages/00-session-start.md`](../stages/00-session-start.md) (will own the eventual flow spec), [`stages/02-mode-select.md`](../stages/02-mode-select.md) (mode-aware pause-control split lives here).

Resolves: `CONCEPT-GAPS.md` rows **SETTINGS-01** (no options menu defined) and **PAUSE-01** (no pause / meta-control envelope) as a coupled pair. Does NOT resolve SETTINGS-02 (keybind remap — Phase 2 constraint), SETTINGS-03 (resolution/display — Phase 2 constraint), PAUSE-02 (ranked exceptions detail — partially seeded here, full spec deferred), or any AUDIO/A11Y/CMDR/FLOW row.

---

## Decision

The intro-game and in-match flows must surface a **meta-UI envelope** consisting of, at minimum: a top-level **Options** menu reachable from both the main menu and from the in-match Pause overlay; a **Pause overlay** mapped to `Esc` whose contents differ by mode; and a **Quit / Save-and-Exit / Concede** path appropriate to mode. CONCEPT.md Phase 3 will gain a new sub-section (working number `§3.9 — Meta-UI surfaces`) naming these surfaces and the solo-vs-competitive control split. Exhaustive per-setting listings (every video/audio/input/accessibility/gameplay toggle) are explicitly deferred to Phase 5.

The mode-aware pause/meta-control split is:

| Mode | Esc behavior | Pause overlay contents | Restart | Save | Quit |
|------|--------------|------------------------|---------|------|------|
| Solo Campaign | Hard pause (game state frozen) | Resume / Options / Restart Mission / Save-and-Exit / Quit-to-Menu | Allowed | Save-and-Exit (mid-mission persistence) | Confirm if unsaved |
| Solo Skirmish (vs AI) | Hard pause | Resume / Options / Restart / Quit-to-Menu | Allowed | Auto-save on end only (no mid-match save slot) | Confirm if mid-match |
| Co-op Horde | Host-pause with **vote-or-timeout** (principle named here; specifics deferred to Phase 5 stage doc) | Resume / Options (local) / Concede / Quit-to-Menu | Disabled | Auto-save on end only | Concede semantics |
| Lane Wars 1v1 / 2v2 (incl. ranked) | **Read-only overlay** (no state freeze; opens local Options/info, time keeps running) | Options / View Build / Concede / Quit-to-Menu | Disabled | None (no mid-match save) | Concede + leave |

This bakes in the principle that **competitive integrity > solo convenience**: pause and restart are tools the solo player owns and the competitive player cannot weaponize.

## Context

The 2026-04-19 PM playtest established that the prototype (and the CONCEPT behind it) ships a forced-linear flow with no volume control, no pause, no quit-to-menu, no skip path. Filed under playtest finding #2 ([`2026-04-19-intro-baseline-gaps.md`](2026-04-19-intro-baseline-gaps.md)) and escalated to a full gaps catalog ([`CONCEPT-GAPS.md`](../CONCEPT-GAPS.md)) which placed `SETTINGS-01` and `PAUSE-01` at the top of the must-close list. Both rows are flagged **Blocks-vision** because Claude (or any reader) cannot picture what the shipping game *feels like to use* without knowing how the player stops, configures, or exits a session. CONCEPT-GAPS §4 explicitly recommends opening with `SETTINGS-01` because it unblocks the rest of the meta-UI rows; `PAUSE-01` is its natural twin (the pause menu *is* the in-match entry point to Options and Save-Exit), so they are bundled here rather than filed twice.

Industry-baseline citations are already collected in CONCEPT-GAPS §1 (BTD6 settings inventory, KR5 paginated settings + missing remap, They Are Billions pause = Continue / Save-and-Quit / Options, TDS competitive restart-disable convention) and not re-cited here.

## Alternatives considered

- **Option A — File SETTINGS-01 and PAUSE-01 as two separate decision entries.** Rejected: the two rows are causally entangled (Pause overlay opens Options; Save-and-Exit lives inside Pause), and splitting them would force one entry to cite the other and risk drift. The cost of bundling is one slightly-larger decision; the cost of splitting is two narrower decisions that must be read together to make sense.
- **Option B — Defer to Phase 5 and add nothing to Phase 3.** Rejected: leaves `CONCEPT.md` silent on the *existence* of these surfaces, which is the gap. Phase 3 is the right home for *what surfaces exist*; Phase 5 is the right home for *what each surface contains in detail*. Collapsing both into Phase 5 is the silent-multi-phase failure mode that cascade discipline is designed to prevent.
- **Option C — Adopt a uniform pause model across all modes (e.g., everyone gets full pause).** Rejected: breaks competitive integrity. Competitive PvP TDs (Tower Defense Simulator and the broader genre) disable mid-match pause and restart precisely to prevent exploit; treating ranked the same as solo would either hand the solo player an inferior pause or hand the competitive player a griefing surface.
- **Option D — Adopt the They Are Billions ironman model game-wide (single Save-and-Quit, no manual save).** Rejected: TAB's stance is legitimate but explicit — and incompatible with a Solo Campaign that names "story missions" and a target player profile that includes 5–25 minute sessions interrupted by life. Ironman as a *toggleable mode* is fine and is a Phase 5 concern, not a default.
- **Option E — (Chosen.) Bundled meta-UI envelope decision: name the surfaces in Phase 3, split control behavior by mode, defer exhaustive per-setting list to Phase 5.** Names what must exist without locking what each thing contains.

## Reason chosen

### 3x debug loop

**Loop 1 — aggressive critique.**
- The mode-split table treats Co-op Horde as a near-twin of competitive (disable restart, no mid-match save) but Horde is fundamentally PvE and players will expect to recover from a wipe — this risks alienating exactly the audience the solo-first promise is courting.
- "Read-only overlay" for ranked is a novel UX — most competitive TDs simply have no pause UI at all. Inventing a pattern at concept stage is over-design; the right Phase 3 move is "ranked has no pause," and let Phase 5 invent the overlay if telemetry justifies it.
- The vote-or-timeout principle for co-op is named without spec — that is a TBD-factory move that the gaps doc itself was criticized for in its own Loop 1.
- "Save-and-Exit (mid-mission persistence)" for Solo Campaign is technically a Phase 4 (save-spec) commitment riding inside a Phase 3 entry. Cascade leak.
- The bundled entry runs to two coupled decisions and a four-row table; reviewer cost goes up; if you reject one row, you must reopen the entry rather than just one of two.
- Working section number "§3.9" is a placeholder that risks being cargo-culted as a real anchor.

**Loop 2 — steelman.**
- Co-op Horde *not* getting restart is the right principled call — Horde is shared multiplayer state, and restart in a shared session is host-griefing potential. Auto-save-on-end + concede is enough; "recover from wipe" lives inside the run-loop design, not the meta-UI envelope. The decision protects co-op from a real failure mode the critique is hand-waving away.
- The "read-only overlay" for ranked is the lesser of two bads. Pure no-pause leaves the player unable to access local Options (audio, captions, accessibility) mid-match — which violates the accessibility floor before it is even written. Read-only as a *principle* (state keeps running, local-only menus open) is exactly the cascade-respecting move: name the principle in Phase 3, let Phase 5 spec the affordance.
- The vote-or-timeout principle is named-not-specced *deliberately* — this entry covers Phase 3 ("name the surface"), and the spec is an explicit follow-up. Naming it here prevents the next reviewer from forgetting it exists.
- "Save-and-Exit" appearing in the Solo Campaign row is **not** a Phase 4 save-format commitment; it is a Phase 3 statement that the affordance must exist. The actual save format (slots, autosave frequency, cloud sync) is `SAVE-01` / `SAVE-02` and stays in CONCEPT-GAPS until ratified separately.
- The bundle/split tradeoff was considered and bundled won — see Alternative A. Re-litigating in Loop 2 doesn't change the answer.
- "§3.9" is flagged as a working number in the entry text. Final anchor is determined when the CONCEPT.md amendment lands.

**Loop 3 — synthesis.**
The decision survives critique with three sharpenings, applied above:
1. The Co-op Horde row explicitly notes vote-or-timeout is a **principle, spec deferred** (not a half-formed lock).
2. The Lane Wars row uses **read-only overlay** language with the principle stated (state keeps running, local-only menus open) — this is the minimum needed to keep the accessibility floor reachable without breaking competitive integrity.
3. "Save-and-Exit" in Solo Campaign is bounded to "the affordance must exist"; save format remains a separate CONCEPT-GAPS row.

The bundled scope is correct: SETTINGS-01 and PAUSE-01 are entangled enough that splitting forces cross-reference. The cascade leak risk is real but managed by deferring all *contents* (per-setting lists, save format, voice spec, A11Y toggles) to their owning rows.

## Reversibility note

**Easy.** This entry commits a direction; no CONCEPT.md text is written by this entry. The CONCEPT.md amendment is a separate follow-up step that the PM gates independently. To reverse: mark this entry Superseded, do not file the amendment, and `SETTINGS-01` / `PAUSE-01` revert to open in `CONCEPT-GAPS.md`. Downstream artifacts that have not yet been written (stage 00, stage 02, Phase 5 spec rows) are unaffected.

If reversed *after* the CONCEPT.md amendment lands, cost rises to **Medium**: revert the §3 amendment, restore the gaps rows, and any decision entries filed against this one (e.g., a future per-setting list spec) must be re-rooted or themselves superseded.

## Follow-ups

- **Next step (PM-gated):** draft the CONCEPT.md Phase 3 amendment — a small new sub-section (working `§3.9 — Meta-UI surfaces`) naming the surfaces + the mode-split table above. Should be ≤30 lines. Routes through Phase 3 properly (no Phase N+1 silent edit).
- On amendment landing: migrate `SETTINGS-01` and `PAUSE-01` rows out of `CONCEPT-GAPS.md`; update `CONCEPT-GAPS.md` row counts in §1 footer; bump `CASCADE.md` decisions table with this entry; `PROGRESS.md § Debts carried` notes the first ratified gap closure.
- **Unblocks:** `ONBOARD-01` (skippable tutorial — needs Pause/Quit-to-Menu to exist as exit affordance), `ONBOARD-03` (codex reachable from pause), `AUDIO-01` follow-on (audio-bus sliders live in Options), `A11Y-01..04` (accessibility toggles live in Options), `FLOW-02` (returning-player branch needs a main menu).
- **Still open / not addressed by this entry:** SETTINGS-02 (keybind remap — Phase 2 constraint, separate entry), SETTINGS-03 (resolution/display — Phase 2 constraint, separate entry), PAUSE-02 detail (ranked-mode exception specifics beyond "no restart, read-only overlay"), all SAVE/A11Y/AUDIO/CMDR/FLOW rows.
- **Decision dependency on §7.1 blockers:** none. This entry does not touch hybrid discovery (#1), Veil-not-the-one-nobody-picks (#9), Crown-not-boring (#10), or any other open Phase 7 question.
