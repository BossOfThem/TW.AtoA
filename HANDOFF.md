# HANDOFF — Session Checkpoint

**Last session:** 2026-05-06.
**Hand-off by:** Claude (Opus 4.7, post-compaction continuation — RN + post-arc ratifications produced after R4 doc-hygiene refactor).
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Per-civ specialization sub-pass arc CLOSED 4/4** — RN audit LANDED ([`decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md`](decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md), commit `a98a5d3`, dual-pushed). 5×3 civ-aggregate audit (15 bindings × 5 locks; zero cascade-violations). Three-civ-three-equation-form fingerprint LOCKED as Phase-4-spec-level invariant.

**Post-arc 4-item ratification LANDED** — [`decisions/2026-05-06-post-arc-ratifications.md`](decisions/2026-05-06-post-arc-ratifications.md). Next-track = **§4.7 enemy direction + Round 11 wave-variance, bundled**; `admin/concept.json` retired from source-of-truth chain; phase-4.md soft-cap bumped 600→700 via cascade-lint per-file override; cultural-sensitivity Follow-up #5 scheduled at Phase-4 exit.

**NEXT session: open §4.7 enemy direction sub-arc.** Phase-4 OPEN exit-gate item #4 + Round 11 mandate. AskUserQuestion only on R1 scope axis-pick (per established arc-open pattern); proceed autonomously thereafter per PM autonomy mandate.

---

## State snapshot

### Git
- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commits: `a98a5d3` (Per-civ RN LANDED) → `3027361` (R4 handoff) → `5f58829` (R4 LANDED) → `00335ac` (handoff SHA fill) → `8fcdc1a` (doc-hygiene refactor).
- Post-arc ratifications commit pending in this handoff bundle.
- **Carried git debt:** `49c4c54` contains 69MB `.accord/events.jsonl` blob (>50MB GitHub warning). Removing requires destructive force-push — only on explicit PM authorization.

### Per-civ sub-pass status (CLOSED 4/4)
- R1 scope LANDED (`b0d7841`). R2 Greek LANDED (`49c4c54` + cleanup `78cba67`). R3 Aztec LANDED (`7c3f338`). R4 Norse LANDED (`5f58829`). **RN audit LANDED (`a98a5d3`).**
- All five rounds dual-pushed. Zero cascade-violations across 4/4 rounds + RN.
- 5×3 civ-aggregate matrix passes 5 locks (5-field schema / RPS verbatim / DPS ladder ±20% / lane-lock Hard / per-tower magnitude verbatim).
- Three-civ-three-equation-form fingerprint LOCKED as Phase-4-spec-level invariant: Greek deceleration-weighted (per-target-time-integral) / Aztec kill-multiplication-weighted (per-cast-multiplier × per-kill-bonus) / Norse summon-cleave-propagation-weighted (per-summoned-unit × cleave × Bleed-stack × per-stage 1→8→16). Future patch civs must surface a fourth equation form with non-overlapping free-variable-set or fingerprint reopens.
- Spine-doc: `concept/phase-4.md §4.12 Per-civ specialization profiles` NEW + `§4.8` exit-gate ✅ ticked.

### Post-arc ratifications (this turn)
1. **Next-track: §4.7 enemy direction + R11 wave-variance, bundled.** Phase-4 OPEN exit-gate item #4 + 2026-05-05 amendment-pass R6 Round 11 mandate.
2. **`admin/concept.json` retired** from source-of-truth chain. CASCADE reading-order item #8 dropped; Admin UI section flagged retired; CLAUDE handoff-trigger checklist updated; PROGRESS Debts-carried entry resolved. JSON file remains in repo as historical artifact.
3. **`concept/phase-4.md` soft-cap bumped 600→700** via per-file override in [`tools/cascade-lint.py`](tools/cascade-lint.py). Other docs retain the 600 cap. Eliminates ongoing carried-soft-cap finding.
4. **Cultural-sensitivity Follow-up #5 timing locked** to Phase-4 exit. Last exit-gate item, before any art / VFX / pose / VO / civ-flavor surface direction prose generation begins in Phase 5.

### Doc-hygiene
- `PROGRESS.md` session log: 3 most-recent entries (Ratifications / RN / R4); Doc-hygiene + R3 archived to [`PROGRESS-archive.md`](PROGRESS-archive.md).
- `CASCADE.md` pointer: 1 most-recent block (next-track state).
- `CASCADE.md` decisions table: 79 one-line hooks (matches 79 non-template files in `decisions/`).
- `CASCADE.md` version footer: 2 most-recent entries (0.72 + 0.71).
- cascade-lint clean (no findings — phase-4.md 636/700 within ratified cap).

### Locked carry-forward (untouched this session)
- 17-item conceptual frame (a)-(r) + extension (s) — Accepted.
- All 10 Numbers-phase magnitudes — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure — Accepted.
- "Go big, no scope cuts" doctrine — Accepted (hub Non-negotiable).
- 2026-04-25 locked content skeleton — Accepted.
- §5.4 [LOCKED] (Civilizations row); §2.4a [LOCKED] (accessibility floor).
- All R1-R7 CONCEPT amendment-pass §-anchors — Accepted.
- All per-commander R1-R5 spine-doc edits + lane locks (Leonidas=Control / Montezuma II=Economy / Ragnar=Summon, **Hard reversibility**) — Accepted.
- All per-tower R1-RN magnitude matrix + 4 locks (45/45 zero cascade-violations) — Accepted.
- Per-civ R1 scope + R2 Greek + R3 Aztec + R4 Norse + RN — Accepted (4/4 + RN).
- **Three-civ-three-equation-form fingerprint** — Phase-4-spec-level invariant.

### Two prototype findings still queued (not in scope)
- **(a)** `prototype/index.html:3310` — `openReference` throws `ReferenceError: CIVS_DATA is not defined` when `game.commander.civ` is falsy.
- **(b)** `prototype/index.html:495,507,513` — mode-select copy still references "three ages" / "11-age arc". Obsolete under post-2026-04-25 4-tier ladder.

### Open follow-ups
- **#5** — Cultural-sensitivity pass. **NOW SCHEDULED at Phase-4 exit** per ratification item 4. High-vigilance at Aztec; moderate at Norse; standard at Greek.
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`research/06-tw-subgenres.md`** new stub.

### Post-§4.7-arc roadmap
1. §4.4 mobile-unit-control (Phase 4 OPEN BLOCKER, exit-gate item #3).
2. Phase 4 numerics ratification (Fusion + §4.6 economy details).
3. Per-map authoring (good-cell + crystal-lock variance, downstream of §4.7 + Round 11).
4. Monetization specifics / engine choice lock (Godot 4 leading) / art director scope.
5. Cultural-sensitivity Follow-up #5 consultation engagement.
6. Phase 5 readiness gate (telemetry + wave variance scaffolding) — opens only after Phase 4 exits cleanly.
7. `research/06-tw-subgenres.md` stub.
8. Follow-ups #6/#7/#8/#9 + C7.b deferred.

---

## Cadence rules carried forward

- Cadence exists to manage the context window, not to gate every step.
- **PM autonomy mandate:** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously. See `feedback_autonomy_mandate.md` in user memory.
- AskUserQuestion is the standard interface when gating is needed. Recommended-first.
- MD-first preservation — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions.
- Dual-push discipline — push to BOTH session branch AND `main` after every commit.
- **Targeted `git add` only** — never `git add -A`.
- Local-main hygiene — `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- 3x debug loop on any CONCEPT-constraint-touching proposal.
- Doc hygiene per compression standard in [`CLAUDE.md`](CLAUDE.md) — round summaries are 1-line hooks in CASCADE/PROGRESS; full content lives in the decision file only.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. Per-civ specialization sub-pass CLOSED 4/4 (RN
landed + post-arc ratifications landed). NEXT TRACK: §4.7 enemy
direction lock + Round 11 wave-composition variance mandate, bundled.

LANDED COMMITS (all dual-pushed):
  b0d7841  per-civ R1 scope
  49c4c54  per-civ R2 Greek (+ cleanup 78cba67 untracking .accord/)
  7c3f338  per-civ R3 Aztec
  5f58829  per-civ R4 Norse
  a98a5d3  per-civ RN audit + arc close + spine-doc edits
  <pending> post-arc ratifications + handoff bundle

KNOWN GIT DEBT (carried): commit 49c4c54 has 69MB .accord/events.jsonl
blob in history. Cleanup 78cba67 removes from tracking + .gitignore.
Full purge needs destructive force-push — DO NOT execute without
explicit PM authorization.

POST-ARC RATIFICATIONS (this session, decisions/2026-05-06-post-arc-
ratifications.md):
  1. Next-track = §4.7 enemy direction + R11, bundled.
  2. admin/concept.json retired from source-of-truth chain.
  3. concept/phase-4.md cap bumped 600→700 (per-file override in
     tools/cascade-lint.py).
  4. Cultural-sensitivity Follow-up #5 scheduled at Phase-4 exit.

LOCKED INVARIANTS (carry-forward, do not silently edit):
  - 17-item conceptual frame (a)-(r) + extension (s)
  - All 10 Numbers-phase magnitudes
  - 6-mode ontology + auxiliary economy
  - 2026-04-25 locked content skeleton
  - §5.4 [LOCKED] / §2.4a [LOCKED]
  - All R1-R7 CONCEPT amendment-pass §-anchors
  - Per-commander R1-R5 lane locks (Hard reversibility):
      Greek=Leonidas (Control)
      Aztec=Montezuma II (Economy)
      Norse=Ragnar Lothbrok (Summon)
  - Per-tower R1-RN 45-tower magnitude matrix + 4 locks
  - Per-civ R1+R2+R3+R4+RN profiles + 5-field schema
  - Three-civ-three-equation-form fingerprint (Phase-4-spec-level
    invariant): Greek deceleration-weighted / Aztec kill-multiplication
    -weighted / Norse summon-cleave-propagation-weighted

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS
→ CONCEPT (admin/concept.json retired from reading order 2026-05-06).

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — open §4.7 enemy direction sub-arc.

  Phase-4 OPEN exit-gate item #4 (concept/phase-4.md §4.7 currently
  has Option A/B/C placeholder + leading "Option C hybrid"). Round 11
  mandate from 2026-05-05 amendment-pass R6: random-seeded wave-
  composition variance + per-map crystal-lock variance defending
  §4.11.8 skill-bar thresholds from memorization meta.

  Likely round structure (PM picks via AskUserQuestion R1 scope axis):
    R1 — scope decision + N-round queue + axis pick (per-archetype
         creep-roster vs per-mode wave-composition vs per-property)
    R2-R(N-1) — content rounds per chosen axis
    RN — cross-arc audit + spine-doc edits at concept/phase-4.md §4.7
         + Round 11 variance body + possible §4.8 exit-gate item ticks
         (item #4 enemy direction; possibly item #2-equivalent for R11)

  Spine-doc edit scope at this arc: concept/phase-4.md §4.7 (Option
  A/B/C → locked option + body) + Round 11 variance mandate body.
  Other §-anchors out of scope (gate via AskUserQuestion).

§4.7 INPUTS (Grep > full-file Read):
  concept/phase-4.md §4.7 (current OPEN status + Option A/B/C placeholder)
  decisions/2026-05-05-concept-amendment-pass-round-6-phase-4-7-r11-
    and-phase-6-7.md (Round 11 mandate origination)
  decisions/2026-04-26-attack-type-mapping.md (5-armor-class taxonomy
    + 7-attack-type taxonomy — creep-roster armor binding lives here)
  decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md
    (signature_creep_types per-civ specialization grain — §4.7 must
    cohere with 3-civ aggregate matchup signatures)
  decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md
    (45-tower roster type-coverage table; §4.7 wave composition must
    surface coverage-gap pressures via wave mix per civ)
  decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md +
    round-2-k-exponents.md + round-8-per-mode-tuning.md (HP curve +
    boss-spike overlay + per-mode N-scaling — §4.7 wave composition
    targets these magnitudes)
  decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md
    (matchup-correctness / placement-coverage / ability-uptime axes —
    Round 11 variance defends these from memorization)

§4.7 PROCEDURE (R1 scope round):
  1. Read inputs above (Grep first, full Read only when needed).
  2. Run cascade-lint baseline.
  3. State plan + 3x debug loop on round-structure axis (per-archetype
     vs per-mode vs per-property).
  4. AskUserQuestion gate: round-queue axis + N-round count + scope
     boundary (does Round 11 variance mandate body live in this arc
     or split out?). Recommended-first.
  5. After PM "go": file decisions/2026-05-MM-attack-direction-r1-
     scope.md (or similar slug) — Accepted, Medium.
  6. cascade-lint, commit, dual-push (session branch + main).
     CRITICAL: targeted `git add <file>` only — never `git add -A`.
  7. PM autonomy mandate: proceed to R2 autonomously thereafter.

DOC-HYGIENE (per CLAUDE.md compression standard):
  - CASCADE decisions-table row: ONE LINE per round.
  - CASCADE current-work pointer: ~5 lines.
  - PROGRESS session log entry: 3-5 lines per round.
  - HANDOFF TL;DR: 3-5 sentences.

DUAL-PUSH POINTS (suggested, lock at R1 scope):
  After R1 scope, after each content round, after RN.

NO GAME CODE EDITS. Concept-only — Phase 4 hasn't exited.
SPINE-DOC EDITS at this arc allowed at concept/phase-4.md §4.7 +
  Round 11 variance body only. Other §-anchors require AskUserQuestion
  gate before touching.

VERIFY each commit with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.
TARGETED `git add` ONLY — never `git add -A`.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Civilizations would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5 — scheduling locked at Phase-4 exit, but design-stage signal still warrants flag if Aztec / Norse cultural surface direction prose appears).
- Local `main` stale on session start.
- `cascade-lint` fails new (no carried findings post-ratification — phase-4.md 636/700 is within cap).
- Spine-doc edit at this arc would touch any §-anchor other than `concept/phase-4.md §4.7` or the Round 11 variance body.
- §4.8 exit-gate item add/tick contemplated without AskUserQuestion gate (item #4 enemy direction tick is in-scope; other ticks are scope expansion).
- The 17-item frame would be silently edited.
- Any Numbers-phase bound magnitude would be silently re-tuned.
- Any amendment-pass §-anchor would be silently edited.
- Any per-commander R1-R5 spine-doc surface would be silently edited.
- Any per-tower R1-RN magnitude row would be silently re-tuned out of band.
- Any per-civ R2/R3/R4 profile field or RN audit binding would be silently edited.
- Any §4.7 wave composition contradicts the per-civ RN matchup_affinity matrix (signature_creep_types must cohere with civ-aggregate STRONG/WEAK cells; deviations need an explicit reconciliation paragraph).
- Three-civ-three-equation-form fingerprint would be touched without supersession decision.
- A track touching CONCEPT constraints lands without 3x debug loop.
- `git add -A` is about to be invoked (use targeted staging instead).
- Context budget pressure forces a mid-track split → file mini-handoff and stop cleanly.
