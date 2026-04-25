# HANDOFF — Session Checkpoint

**Last session:** 2026-04-25 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7, post-compaction continuation)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Per-tower authoring sub-pass CLOSED** (R1+R2+R3+R4+RN LANDED, all 45 launch towers bound under 4 locks; arc-close commit `43e1271`, dual-pushed). **Per-civ specialization sub-pass OPENED.** Next-track fork resolved via AskUserQuestion (PM picked Recommended #1 = per-civ specialization). R1 scope decision LANDED at [`decisions/2026-05-06-per-civ-specialization-scope.md`](decisions/2026-05-06-per-civ-specialization-scope.md) (Accepted, Medium). PM picked Recommended on both AskUserQuestion gates: **Axis A (per-civ deep-dive)** + **5-field schema lock** (matchup_affinity / identity_hook / signature_creep_types / multi_civ_play_hook / commander_synergy). 4-round queue locked: R1 (DONE) + R2 Greek profile + R3 Aztec + R4 Norse + RN cross-civ × cross-field audit + spine-doc edits. **NEXT session: produce R2 Greek profile autonomously per PM autonomy mandate.**

---

## NEXT SESSION — primary directive

**Per-civ R2 (Greek profile) — produce autonomously per the PM autonomy mandate** carried forward from per-tower R1-RN, per-commander R1-R5, CONCEPT amendment pass R1-R7, and Numbers-phase R1-R10.

**R2 deliverable:** [`decisions/2026-05-06-per-civ-r2-greek-profile.md`](decisions/2026-05-06-per-civ-r2-greek-profile.md) (Accepted, Medium). Five-field Greek civ profile (matchup_affinity / identity_hook / signature_creep_types / multi_civ_play_hook / commander_synergy) + cross-civ parity hook paragraph forward-pointing to R3 Aztec.

### Step-by-step procedure

1. **Bootstrap** per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.
2. `git fetch origin && git log --oneline HEAD..origin/main` (expect clean — last per-civ R1 push to both session branch + main).
3. **Read R1 scope file** [`decisions/2026-05-06-per-civ-specialization-scope.md`](decisions/2026-05-06-per-civ-specialization-scope.md) end-to-end.
4. **Read inputs** (Grep > full-file Read where possible):
   - [`decisions/2026-05-06-per-tower-r2-greek-roster.md`](decisions/2026-05-06-per-tower-r2-greek-roster.md) — Greek 15-tower magnitude matrix + civ-identity-hook prose.
   - [`decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md`](decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md) — type-coverage audit (Greek lacks Poison; 6 of 7 types) + cross-civ band statistics.
   - [`decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md`](decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md) — Leonidas one-pager + lane lock (Control, Hard).
   - [`decisions/2026-04-26-attack-type-mapping.md`](decisions/2026-04-26-attack-type-mapping.md) — 7-attack × 5-armor RPS matrix.
   - `concept/phase-4.md` §4.10 (RPS matrix substrate) + §4.11 (Numbers floor) — read-only.
5. **Author R2** = 5-field Greek profile decision file. Synthesis discipline: identity_hook integrates Leonidas Control + per-tower Greek lockdown signature (dps-centered / cd-1.7s / range-4.0 / armor-shred + stagger + smite + slow + stun rich) into one paragraph. matchup_affinity bins Greek 15-tower roster against §4.10 5-armor classes (Unarmored / Shielded / Heavy / Magic / Boss) — aggregate not per-tower. signature_creep_types at armor-class grain (which armor classes Greek's RPS-matrix 1.25× cells cluster against). multi_civ_play_hook = Poison-coverage gap (Greek lacks all Poison sources at launch — patch-1 commander expansion path). commander_synergy = one-sentence statement of how Leonidas Spartan-Training aura + This Is Sparta! short-CD + The Last Stand signature interface with Greek lockdown magnitude signature.
6. **Cascade-lint:** `python tools/cascade-lint.py` (expect clean except pre-existing `concept/phase-4.md` 629/600 soft-cap).
7. **Commit R2 + dual-push** (session branch + main).
8. **Continue to R3 (Aztec) autonomously if context budget healthy.** Otherwise stop after R2 and file mini-handoff.

### Discipline (carry forward)

- **No game code edits.** Concept-only — Phase 4 hasn't exited.
- **3x debug loop** on any decision touching CONCEPT constraints. R2-R4 each produce a per-civ identity_hook synthesis paragraph; 3x debug loop on identity_hook construction.
- **Dual-push every commit.** Push to session branch AND `main`.
- **Cascade-lint after every round.** Phase-4 line-cap (currently 629/600) is breached carried-state — net-neutral target for future spine-doc edits OR explicit PM ratification of cap-bump.
- **Cultural-sensitivity Follow-up #5 hard-gate** stays in force. Mechanical-content only — civ-neutral effect-type language. No art / VFX / pose / VO / civ-flavor surface direction prose. Locked content-skeleton names verbatim only.
- **Cross-arc dependency:** every per-civ row references per-tower RN type-coverage + status-proc-density audits + per-commander R5 lane locks. Any divergence is a cascade violation flagged in-round.

Surface AskUserQuestion ONLY on: Genuine forks not anticipated in R1 scope / Scope expansion beyond locked 4-round queue / Cascade-violation risk (matchup_affinity contradicting per-tower RN; signature_creep_types crossing §4.7 archetype-grain; commander_synergy crossing civ lanes) / Cultural-sensitivity surface (Follow-up #5) / Handoff trigger.

---

## What is locked (clear-safe)

### Carried forward (untouched this session)

- 17-item conceptual frame (a)-(r) + extension (s) — Accepted.
- All 10 Numbers-phase magnitudes — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure (Tribute kill-only + Divinity 6-source 4-floor+2-escalation; 6-cap discipline) — Accepted.
- "Go big, no scope cuts" doctrine — Accepted (hub Non-negotiable).
- 2026-04-25 locked content skeleton — Accepted.
- §5.4 [LOCKED] (Civilizations row).
- §2.4a [LOCKED] (accessibility floor).
- All R1-R7 CONCEPT amendment-pass §-anchors — Accepted.
- All per-commander R1-R5 spine-doc edits + lane locks (Leonidas=Control / Montezuma II=Economy / Ragnar=Summon, Hard reversibility) — Accepted.
- All per-tower R1-RN magnitude matrix + 4 locks (attack-type / dps-band / proc-kind / lane-tag) — Accepted (45/45 zero cascade-violations).
- Splash-fix `CODEX_DATA` rename — Accepted.
- All Phase C UI-verification-sweep fixes (`5d2f3c8` / `8f67a08` / `4964895` / `abcb398`) — Accepted.

### NEW this session

- **Per-tower authoring arc CLOSED** — R4 Norse + RN cross-civ audit landed; spine-doc §4.8 item #2 ticked DONE + §4.11.5 closing reference added; Phase 4 exit-gate items #1+#2 closed.
- **Per-civ specialization R1 scope** LANDED via [`decisions/2026-05-06-per-civ-specialization-scope.md`](decisions/2026-05-06-per-civ-specialization-scope.md) (Accepted, Medium). Round queue + axis + 5-field schema + hard guards locked.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit pre-handoff: `43e1271` (per-tower RN bundle dual-pushed). Per-civ R1 scope file + handoff bundle staged for this turn's chore commit. Will dual-push.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most-recent entries (per-civ R1 scope / per-tower R1 OPENED / Phase C). Phase B archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (per-civ R1 scope LANDED). Per-tower-arc-CLOSED block archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.67 + 0.66. 0.65 archived to `CASCADE-history.md`.
- cascade-lint expected clean except pre-existing `concept/phase-4.md` 629/600 soft-cap (carried — not introduced by this handoff).

### Two prototype findings still queued (not in scope for this arc)

These remain queued from Phase C close. Pick up on a context-budget-friendly side-pass between per-civ rounds if PM directs, else they wait until per-civ arc closes.

- **(a) `openReference` CIVS_DATA bug** — `prototype/index.html` ln 3310 throws `ReferenceError: CIVS_DATA is not defined` when `game.commander.civ` is falsy.
- **(b) Mode-select copy obsolete** — `prototype/index.html` ln 495 / 507 / 513 still references "three ages" / "11-age arc solo". Obsolete under post-2026-04-25 4-tier ladder.

### Open follow-ups (carried — UNCHANGED)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art + VFX + civ-flavor surface direction). **Hard-gates per-civ specialization arc visual prose** (this arc is mechanical-content only — same discipline as per-tower arc).
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance. Multi_civ_play_hook field in this arc explicitly notes the deferred patch-1 expansion path.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness** — long-deferred.
- **`research/06-tw-subgenres.md`** new stub.

### Post-arc roadmap (preserve, deferred until per-civ RN closes)

1. **Per-map / Round 11** — good-cell + wave-randomization + crystal-lock variance per §4.7 R11.
2. **§4.4 mobile unit control** — Phase 4 exit-gate OPEN BLOCKER.
3. **§4.7 enemy direction lock** — Option C hybrid leading; downstream of this arc's signature_creep_types archetype-grain output.
4. **Phase 4 numerics ratification** — Fusion balance pass [PROPOSAL] + §4.6 economy numerics [PROPOSAL].
5. **Monetization specifics / engine choice lock / art director scope.**
6. **Phase 5 readiness gate** — engine-side telemetry per §6.5; wave variance per §4.7 R11.
7. **`research/06-tw-subgenres.md`** new stub.
8. **`admin/concept.json`** migration.
9. **Follow-ups** #5 / #6 / #7 / #8 / #9 + C7.b deferred.

### Regression-watch (carried from Phase C)

- End-screen XP persist (Phase C #8) — re-verify on a fresh skirmish if any code touches `endMatch` ln 3390-3408.
- Match keybinds (Phase C #6) — re-verify after a rebind round-trip if any code touches the `Profile.setting("input.binds")` resolver.
- Tutorial Esc dismissal (Phase B carry).
- Profile scene roster (Phase B carry).
- End-screen layout post-Highest-Age row removal (Phase B carry).
- `menu-last` resolution path (Phase B carry).

---

## Cadence rules carried forward (project-level)

- **Cadence exists to manage the context window, not to gate every step.**
- **PM autonomy mandate:** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously. See `feedback_autonomy_mandate.md` in user memory.
- **AskUserQuestion is the standard interface** when gating is needed. Recommended-first.
- **MD-first preservation** — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3, CASCADE pointer to 1 block, footer to 2.
- **Preview MCP cadence:** N/A this arc — no prototype work.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. Per-tower authoring sub-pass CLOSED (R1+R2+R3+R4+RN
LANDED, arc-close commit 43e1271 dual-pushed). Per-civ specialization sub-
pass OPENED on 2026-05-06. R1 scope decision LANDED at
decisions/2026-05-06-per-civ-specialization-scope.md (Accepted, Medium).
PM picked Recommended on both AskUserQuestion gates: Axis A per-civ deep-
dive + 5-field schema lock.

4-round queue locked:
  R1 (DONE) — scope decision + 3x debug loop + 5-field schema lock
  R2       — Greek profile: 5 fields + cross-civ parity hook → R3
  R3       — Aztec profile: 5 fields + cross-civ parity hook → R4
  R4       — Norse profile: 5 fields + cross-civ parity hook → RN
  RN       — cross-civ × cross-field audit + phase-4.md §4.x per-civ
            specialization body + possible §4.8 exit-gate item add

5-field schema (LOCKED for the arc):
  matchup_affinity      (vs §4.10 7-attack × 5-armor RPS classes —
                         civ aggregate against Unarmored/Shielded/
                         Heavy/Magic/Boss; bins from per-tower RN
                         type-coverage audit)
  identity_hook         (one-paragraph mechanical thesis synthesizing
                         lane-lock + per-tower magnitude signature +
                         status-proc archetype + commander synergy;
                         civ-neutral effect-type language)
  signature_creep_types (armor-class grain pre-§4.7-lock; references
                         §4.10 5-armor substrate)
  multi_civ_play_hook   (per-tower RN type-coverage gaps: Greek-no-
                         Poison / Aztec-no-Crushing / Norse-no-Poison-
                         no-Divine-T1-T3; references deferred Foresight-
                         coin + Follow-up #6 patch-1 commanders)
  commander_synergy     (per-commander R5 lane-lock binding — Greek=
                         Control via Leonidas / Aztec=Economy via
                         Montezuma II / Norse=Summon via Ragnar)

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — produce R2 (Greek profile) AUTONOMOUSLY per the
PM autonomy mandate carried forward from per-tower R1-RN / per-commander
R1-R5 / CONCEPT amendment-pass R1-R7 / Numbers-phase R1-R10.

Surface AskUserQuestion ONLY on:
  - Genuine forks not anticipated in R1 scope.
  - Scope expansion beyond the locked 4-round queue.
  - Cascade-violation risk (matchup_affinity contradicting per-tower RN
    type-coverage audit; signature_creep_types crossing §4.7 archetype-
    grain; commander_synergy crossing civ lanes).
  - Cultural-sensitivity surface (Follow-up #5 — art / VFX / civ-flavor
    surface direction prose).
  - Handoff trigger.

R2 INPUTS (Grep > full-file Read where possible):
  decisions/2026-05-06-per-civ-specialization-scope.md
  decisions/2026-05-06-per-tower-r2-greek-roster.md
  decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md
  decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md
  decisions/2026-04-26-attack-type-mapping.md
  concept/phase-4.md  (§4.10 / §4.11 — read-only)

R2 DELIVERABLE:
  decisions/2026-05-06-per-civ-r2-greek-profile.md (Accepted, Medium)
  - 5-field Greek profile (matchup_affinity / identity_hook /
    signature_creep_types / multi_civ_play_hook / commander_synergy)
  - identity_hook synthesis: Leonidas Control + per-tower Greek lockdown
    signature (dps-centered / cd-1.7s / range-4.0 / armor-shred +
    stagger + smite + slow + stun rich) into one paragraph
  - 3x debug loop on identity_hook construction
  - Cross-civ parity hook paragraph forward-pointing to R3 Aztec

R2 PROCEDURE:
  1. Read inputs.
  2. Author 5-field Greek profile.
  3. 3x debug loop on identity_hook.
  4. Cross-civ parity hook to R3 Aztec.
  5. Cascade-lint: python tools/cascade-lint.py
     (expect clean except pre-existing phase-4 soft-cap 629/600)
  6. Commit R2 + dual-push (session branch + main).
  7. Continue to R3 (Aztec) autonomously if context budget healthy.
     Otherwise stop after R2 and file mini-handoff.

DUAL-PUSH POINTS (locked from R1 scope):
  After R2 (carries R1+R2)
  After R3 (carries R3)
  After RN (carries R4 + RN; CLOSES arc)

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 content-skeleton names
  verbatim untouched.
- 17-item frame + extension (s) Accepted.
- All Numbers-phase magnitudes Accepted.
- All R1-R7 CONCEPT amendment-pass §-anchors Accepted.
- All per-commander R1-R5 spine-doc edits + lane locks Accepted (Hard).
- All per-tower R1-RN magnitude matrix + 4 locks Accepted (45/45 zero
  cascade-violations).
- §4.7 OPEN — signature_creep_types stays at armor-class archetype-grain
  only; per-creep-row specifics defer to §4.7 lock.
- Cultural-sensitivity Follow-up #5 hard-gates non-abstract civ art /
  VFX / civ-flavor surface direction. This arc is mechanical-content
  only — civ-neutral effect-type language throughout.

NO GAME CODE EDITS. Concept-only — Phase 4 hasn't exited.
NO SPINE-DOC EDITS during R2/R3/R4. All phase-4.md §4.x body edits
  + possible §4.8 exit-gate item add happen at RN.

VERIFY each commit with: python tools/cascade-lint.py
  (expect clean except pre-existing phase-4 soft-cap 629/600)
DUAL-PUSH each commit: session branch + main.

POST-ARC ROADMAP (preserve, deferred until per-civ RN closes):
1. Per-map / Round 11 (wave-randomization + crystal-lock + good-cell).
2. §4.4 mobile unit control (Phase 4 OPEN BLOCKER).
3. §4.7 enemy direction lock (Option C hybrid leading).
4. Phase 4 numerics ratification (Fusion + §4.6 economy).
5. Monetization specifics / engine choice lock / art director scope.
6. Phase 5 readiness gate (telemetry + wave variance).
7. research/06-tw-subgenres.md / admin/concept.json migration.
8. Follow-ups #5/#6/#7/#8/#9 + C7.b deferred items.

TWO PROTOTYPE FINDINGS STILL QUEUED (independent of this arc;
side-pass between rounds only if PM directs):
  (a) prototype/index.html ln 3310 openReference CIVS_DATA undefined
      ReferenceError when game.commander.civ is falsy.
  (b) prototype/index.html ln 495/507/513 mode-select copy obsolete
      "three ages"/"11-age arc" — post-2026-04-25 4-tier ladder.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Civilizations would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Local `main` stale on session start.
- `cascade-lint` fails new (pre-existing phase-4 soft-cap is carried).
- The 17-item frame would be silently edited.
- Any Numbers-phase bound magnitude would be silently re-tuned.
- Any amendment-pass §-anchor would be silently edited.
- Any per-commander R1-R5 spine-doc surface would be silently edited.
- Any per-tower R1-RN magnitude row would be silently re-tuned out of band.
- Any per-civ matchup_affinity row contradicts the per-tower RN type-coverage audit.
- Any per-civ signature_creep_types row crosses §4.7 archetype-grain into per-creep-row specifics.
- Any per-civ commander_synergy row crosses civ lanes (e.g., Leonidas tagged on Aztec).
- A track touching CONCEPT constraints lands without 3x debug loop.
- Context budget pressure forces a mid-track split → file mini-handoff and stop cleanly.
