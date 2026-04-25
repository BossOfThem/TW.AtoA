# HANDOFF — Session Checkpoint

**Last session:** 2026-04-25 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7, post-compaction)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Per-tower authoring sub-pass CLOSED.** All 4 rounds + audit landed this session: R2 Greek (`04efad6`), R3 Aztec (`abe8e9a`), R4 Norse (`9e5b332`), RN cross-civ audit + arc close (this commit). All 45 launch towers bound to the locked 7-field schema (attack_type / cd / range / status_proc / dps / aux_slot_compat / notes). RN audit verdict: **zero cascade-violations across 4 locks × 45 towers** (attack-type lock 45/45 verbatim / dps-band 81/81 in band / status-proc kind 45/45 match / lane-tag 45/45 match clean). All three falsifiable per-civ magnitude signatures empirically confirmed (3/3 PASS): **Greek Control** = dps-centered/cd-1.7s/range-4.0/lockdown-procs; **Aztec Economy** = dps-band-high-T2-T3-and-God-tier/cd-1.4s/range-4.0/Poison-Fire-Slashing-bleed-compounding; **Norse Summon** = dps-centered/cd-1.15s-fastest/range-3.5-shortest/Bleed-density-6-of-15-densest. Spine-doc edits applied: §4.8 exit-gate item #2 (per-tower spec table populated) ticked DONE 2026-05-06 + §4.11.5 closing cross-reference. Phase 4 exit-gate items #1 + #2 closed. CASCADE pointer flipped off per-tower arc. NEXT session opens at **next-track fork pick — AskUserQuestion to PM** (per-civ specialization / per-map / §4.4 / §4.7 / monetization / engine / art director).

---

## NEXT SESSION — primary directive

**Open next-track fork via AskUserQuestion to PM.** Per-tower arc closed; per-commander arc closed; multiple Phase 4 exit-gate items still open. Multiple candidate next-tracks; some have cross-arc dependencies on the per-commander + per-tower outputs that just landed. PM picks fork. This is a **genuine fork** (the trigger that justifies AskUserQuestion under autonomy mandate).

### Candidate next-tracks (pick one)

1. **Per-civ specialization** — Greek / Aztec / Norse identity profiles (matchup affinities + identity hooks + signature creep types). Cross-arc dep on per-commander R5 + per-tower R1-RN: **MET**. Intersects Follow-up #5 cultural-sensitivity gate (Aztec heaviest; gate before any art lock).
2. **Per-map authoring** — good-cell + wave-randomization seeds + crystal-lock variance. Defends §4.11.8 thresholds from memorization meta. Cross-cuts all 6 modes. Cross-arc dep on per-commander summon-archetype path-engageability constraint: MET.
3. **§4.4 mobile unit control** — Phase 4 exit-gate OPEN BLOCKER. Resolution unblocks engine-side input model. No prior arc deps; fully scoped within §4.4.
4. **§4.7 enemy direction lock** — A/B/C choice ratified to Option C hybrid; locking the leading-placeholder finalizes wave-composition variance mandate from §4.7 R11. Cross-arc dep on attack-type lock + DPS ladder: MET.
5. **Phase 4 numerics ratification** — Fusion balance pass [PROPOSAL] → ratified, §4.6 economy numerics [PROPOSAL] → ratified.
6. **Monetization specifics** — cosmetic-only model is the non-negotiable; specifics (battle pass cadence, pack pricing tiers, premium currency presence/absence) remain open.
7. **Engine choice lock** — Godot 4 leading per `concept/phase-5.md §5.5`; lock or pivot.
8. **Art director scope** — engagement / scope doc / cultural-sensitivity consultant binding.
9. **Phase 5 readiness gate** — engine-side telemetry implementation per §6.5; wave-composition variance per §4.7 R11.

### Recommended pick (PM autonomy fork — surface ALL candidates + Recommended via AskUserQuestion)

**Recommended: per-civ specialization** (#1) — natural successor to per-commander + per-tower; banks Phase 4 exit-gate progress on identity surface; per-tower arc explicitly deferred civ-flavor surface direction (Follow-up #5) and per-civ specialization is where that gate gets engaged. Cross-arc deps already met. **Caveat:** Follow-up #5 hard-gates art / VFX / VO direction — per-civ specialization can do *mechanical-content* (matchup affinity tables / signature creep types) without engaging the gate, but stops short of any art lock.

**Alternative if PM wants to clear blockers first:** §4.4 mobile unit control (#3) — explicit Phase 4 OPEN BLOCKER; resolution unblocks engine-port discipline (§4.10.9). Smaller scope than #1.

### Step-by-step procedure

1. **Bootstrap** per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.
2. `git fetch origin && git log --oneline HEAD..origin/main` (expect clean — last RN push to both session branch + main).
3. **Open next-track fork via AskUserQuestion** — present 9 candidates + Recommended (#1 per-civ specialization) per the structure above. Surface caveats (Follow-up #5 gate on per-civ; cross-arc-dep on per-commander+per-tower already met).
4. **Wait for PM pick.**
5. **Open scope round (R1) of picked track** — same scope-decision discipline as 2026-05-06 per-tower R1 (axis pick + schema lock + 3x debug loop + hard guards + dual-push schedule + sub-arc round queue).
6. **Proceed autonomously per PM autonomy mandate** — surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation / cultural-sensitivity / handoff trigger.

### Discipline (carry forward)

- **No game code edits.** Concept-only — Phase 4 hasn't exited.
- **3x debug loop** on any decision touching CONCEPT constraints.
- **Dual-push every commit.** Push to session branch AND `main`.
- **Cascade-lint after every round.** Phase-4 line-cap (currently 629/600) is breached carried-state — net-neutral target for future spine-doc edits OR explicit PM ratification of cap-bump.

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
- Splash-fix `CODEX_DATA` rename — Accepted.
- All Phase C UI-verification-sweep fixes (`5d2f3c8` / `8f67a08` / `4964895` / `abcb398`) — Accepted.

### NEW this session (R1 scope)

- **Per-tower authoring R1 scope** LANDED via `decisions/2026-05-06-per-tower-authoring-scope.md` (Accepted, Medium). Round queue + axis + 7-field schema + hard guards locked.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit (pre-handoff): `8d8550f` (chore handoff doc-hygiene from Phase C). R1 scope file + handoff bundle staged for this turn's chore commit. Will dual-push.
- Working tree at handoff: `decisions/2026-05-06-per-tower-authoring-scope.md` new + CASCADE.md + CASCADE-history.md + PROGRESS.md + PROGRESS-archive.md + HANDOFF.md modified. `.accord/` untracked (carried).

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most-recent entries (R1 scope / Phase C / Phase B). Phase A entry archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (R1 scope LANDED). Prior pointer (Phase C LANDED) archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.66 + 0.65. 0.64 archived to `CASCADE-history.md`.
- cascade-lint expected clean except pre-existing `concept/phase-4.md` 626/600 soft-cap (carried — not introduced by this handoff).

### Two prototype findings still queued (not in scope for this arc)

These are independent of the per-tower arc and remain queued from Phase C close. Pick up on a context-budget-friendly side-pass *between* per-tower rounds if PM directs, else they wait until the per-tower arc closes.

- **(a) `openReference` CIVS_DATA bug** — `prototype/index.html` ln 3310 throws `ReferenceError: CIVS_DATA is not defined` when `game.commander.civ` is falsy. Pre-existing.
- **(b) Mode-select copy obsolete** — `prototype/index.html` ln 495 / 507 / 513 still references "three ages" / "11-age arc solo". Obsolete under post-2026-04-25 4-tier ladder.

### Open follow-ups (carried — UNCHANGED)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art + VFX + civ-flavor surface direction). **Hard-gates per-tower arc visual prose** (this arc is mechanical-content only).
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness** — long-deferred.
- **`research/06-tw-subgenres.md`** new stub.

### Post-arc roadmap (preserve)

1. **Per-civ specialization** — Greek/Aztec/Norse identity profiles (matchup affinities, identity hooks, signature creep types). Intersects Follow-up #5.
2. **Per-map / Round 11** — good-cell authoring + wave-randomization + crystal-lock variance per §4.7 R11 mandate.
3. **Phase 5 readiness gate** — engine-side telemetry per §6.5 + wave variance per §4.7 R11.
4. **`research/06-tw-subgenres.md`** new stub.
5. **`admin/concept.json`** migration.
6. **Follow-ups** #5 / #6 / #7 / #8 / #9 + C7.b deferred.

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
- **Preview MCP cadence:** prefer `preview_eval` for state probes over `preview_screenshot` (cheaper, deterministic). Screenshot only when visual layout is the question. **N/A this arc — no prototype work.**

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. Per-tower authoring sub-pass OPENED on 2026-05-06.
R1 scope decision LANDED at decisions/2026-05-06-per-tower-authoring-scope.md
(Accepted, Medium). PM picked Recommended on both AskUserQuestion gates:
Axis A (per-civ across tiers) + 7-field schema lock.

4-round queue locked:
  R1 (DONE) — scope decision + 3x debug loop + schema lock
  R2       — Greek roster: 15 towers × 7 fields + civ-identity-hook prose
            + per-tier reading + Leonidas controlled_by interface bind
  R3       — Aztec roster: 15 towers × 7 fields + Montezuma II
            economy_target interface bind
  R4       — Norse roster: 15 towers × 7 fields + Ragnar summon_anchor
            interface bind
  RN       — cross-civ × cross-tier audit + phase-4.md §4.x per-tower
            spec body + §4.8 exit-gate item #2 tick

7-field schema (LOCKED for the arc):
  attack_type (verbatim-confirms 2026-04-26 mapping)
  cd          (§4.10 (g) / ±20% tier band)
  range       (§4.10 (j) / ε=0.6 default)
  status_proc (2026-04-26 status-proc table — kind locked)
  dps         (2026-05-05 R5 ladder T1=20/T2=60/T3=180/T4=540/God=1080 ±20%)
  aux_slot_compat (§4.6a 7-slot universal default)
  notes       (civ-identity hook + per-commander affinity-target tag)

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — produce R2 (Greek roster) AUTONOMOUSLY per the
PM autonomy mandate carried forward from 2026-05-05 Numbers-phase /
CONCEPT-amendment-pass / per-commander arc precedent.

Surface AskUserQuestion ONLY on:
  - Genuine forks not anticipated in R1 scope.
  - Scope expansion beyond the locked 4-round queue.
  - Cascade-violation risk (attack_type deviating from 2026-04-26;
    dps beyond ±20% of 2026-05-05 R5 baseline; per-commander
    affinity-target tag crossing civ lanes).
  - Cultural-sensitivity surface (Follow-up #5 — art / VFX / civ-
    flavor surface direction prose).
  - Handoff trigger.

R2 INPUTS (Grep > full-file Read where possible):
  decisions/2026-05-06-per-tower-authoring-scope.md
  decisions/2026-04-26-attack-type-mapping.md
  decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md
  decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md
  concept/phase-4.md  (§4.6 / §4.6a / §4.10 / §4.11)
  concept/phase-3.md  (locked Greek tower content-skeleton names)

R2 DELIVERABLE:
  decisions/2026-05-06-per-tower-r2-greek-roster.md (Accepted, Medium)
  - 15-row table (6 T1-T3 + 6 T4 Demigod + 3 God) × 7 fields
  - Civ-identity-hook prose (Greek lockdown / control archetype)
  - Per-commander affinity-target tags binding Leonidas controlled_by
  - Per-tier reading at close (T1 / T2 / T3 / T4 / God paragraphs)
  - Cross-arc parity hook → R3 Aztec / R4 Norse / RN audit

R2 PROCEDURE:
  1. Read inputs.
  2. Author 15 Greek tower rows in locked 7-field schema.
  3. Cascade-lint: python tools/cascade-lint.py
     (expect clean except pre-existing phase-4 soft-cap 626/600)
  4. Commit R2 + dual-push (session branch + main).
  5. Continue to R3 (Aztec) autonomously if context budget healthy.
     Otherwise stop after R2 and file mini-handoff.

DUAL-PUSH POINTS (locked from R1 scope):
  After R2 (carries R2)
  After R3 (carries R3)
  After RN (carries R4 + RN; CLOSES arc)

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 content-skeleton names
  verbatim untouched.
- 17-item frame + extension (s) Accepted.
- All Numbers-phase magnitudes Accepted.
- All R1-R7 CONCEPT amendment-pass §-anchors Accepted.
- All per-commander R1-R5 spine-doc edits Accepted.
- Effect-type lane locks (Greek=Control / Aztec=Economy / Norse=Summon)
  Hard reversibility — every per-tower notes affinity-target tag
  resolves cleanly to one of these three lanes.
- 2026-04-26 attack-type lock — every attack_type column verbatim-
  confirms the locked mapping.
- 2026-05-05 R5 baseline DPS ±20% band — every per-tower dps within
  band; out-of-band magnitude requires cascade-violation flag.
- Cultural-sensitivity Follow-up #5 hard-gates non-abstract civ art /
  VFX / civ-flavor surface direction. This arc is mechanical-content
  only — civ-neutral effect-type language throughout.

NO GAME CODE EDITS. Concept-only — Phase 4 hasn't exited.
NO SPINE-DOC EDITS during R2/R3/R4. All phase-4.md §4.x body edits
  + §4.8 exit-gate tick happen at RN.

VERIFY each commit with: python tools/cascade-lint.py
  (expect clean except pre-existing phase-4 soft-cap 626/600)
DUAL-PUSH each commit: session branch + main.

POST-ARC ROADMAP (preserve, deferred until RN closes):
1. Per-civ specialization (Greek/Aztec/Norse identity profiles;
   Follow-up #5 gate).
2. Per-map / Round 11 (wave-randomization + crystal-lock + good-cell).
3. Phase 5 readiness gate (telemetry + wave variance).
4. research/06-tw-subgenres.md.
5. admin/concept.json migration.
6. Follow-ups #5/#6/#7/#8/#9 + C7.b deferred items.

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
- Any per-tower `attack_type` deviates from 2026-04-26 mapping.
- Any per-tower `dps` falls outside ±20% of the 2026-05-05 R5 baseline.
- Any per-commander affinity-target tag crosses civ lanes.
- A track touching CONCEPT constraints lands without 3x debug loop.
- Context budget pressure forces a mid-track split → file mini-handoff and stop cleanly.
