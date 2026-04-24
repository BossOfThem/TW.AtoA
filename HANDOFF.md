# HANDOFF — Session Checkpoint

**Last session:** 2026-04-24 (later same day — Phase 1 vision reopen FILED + supersede cascade + CASCADE/PROGRESS bookkeeping)
**Hand-off by:** Claude (Opus 4.7, 1M context)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

The 2026-04-24 Phase 1 vision reopen is now **filed as a decision entry**, not just captured in HANDOFF. Five commits landed one-file-per-turn on `session/2026-04-24-phase-1-reopen`, fast-forwarded to `main` after each:

1. **Reopen decision filed** — [`decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md`](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) (Reversibility **Hard**, 3x debug loop inline). Thematic direction: **synthetic mythic-history braid** (history + comparative religion + mythology + philosophy braided into one invented world). Mechanics preserved. Age model deferred. `§2.4a` + `§5.4` [LOCKED] untouched. Amended once mid-session to correct supersede accounting after local-main bootstrap recovery.
2. **2026-04-21 concept tightening Status → Superseded** (status-line only; body preserved as superseded-record).
3. **2026-04-22 Step B prototype-reshape plan Status → Superseded** (18-sub-step 3/3/3 migration void; body preserved as planning-pattern template).
4. **`CASCADE.md` v0.18 → v0.19** — new 2026-04-24-later pointer block, new decisions-table row for the reopen, Superseded annotations on 2026-04-21 + 2026-04-22 rows.
5. **`PROGRESS.md`** — session-log row + new "2026-04-24 Phase 1 reopen debts" block (Step A §-edits preserved-in-tree, three 2026-04-20 decisions un-rebased, Step B void, title no longer load-bearing, Phase 1 exit gate = one-page world/role/topology answer).

Step A cascade §-edits landed 2026-04-21 across `concept/phase-1..7.md`, `CONCEPT.md` hub, `README.md` #3, `stages/01/04/05/06` stub-amends are **preserved in-tree as superseded-record** — NOT force-reverted. They serve as raw material for the reopen and candidates for re-ratification as Phase 1 exits.

`cascade-lint`: **clean**.

**Important session-start recovery note for bookkeeping accuracy:** this session opened with local `main` 31 commits stale vs `origin/main` (local was at the `a6c6114` initial snapshot — bootstrap docs were therefore wrong). Error was flagged on first push attempt, no destructive action taken, session branch rebased onto real `origin/main 1d43a61`, decision entry amended to fix errors that stemmed from the stale bootstrap (most importantly: the claim that 2026-04-21 was "informal/never filed" — it was filed; linked correctly in the amended entry).

---

## State snapshot

### Git

- Branch pushed: **`session/2026-04-24-phase-1-reopen`** (tracking origin).
- `main` HEAD: **`0d3c59c`** (PROGRESS reopen-debts commit).
- Session commits this pass: `a2ac834` → `cfa1fc7` → `c869be9` → `921e258` → `f30e127` → `0d3c59c` (six commits; the first two are the reopen decision filed then amended; the remaining four are the supersede cascade + CASCADE + PROGRESS bookkeeping).
- Working tree clean. `cascade-lint` clean (`next-open-step: Step 5` — note this is the stale PROGRESS workflow-step tag and is independent of the reopen queue).
- No PR opened.

### Phase status

- **Phase 1 is reopened.** Thematic direction: synthetic mythic-history braid. World, theme, shape, hybrid topology, and working title all open.
- Mechanics (TD / merge / debuff / magic) preserved.
- `concept/phase-2.md §2.4a` accessibility floor [LOCKED] — untouched.
- `concept/phase-5.md §5.4` naming **conventions** [LOCKED] — untouched. Specific names (Ash / Nature / Prayer / Dust / Form / Apotheosis) remain placeholders in the preserved Step A §-edits.
- Age model (within-match vs. seasonal vs. campaign-chapters) deferred until world/story/background land.
- Prototype frozen against concept edits until Phase 1 exits.
- Step 5 playtest gate and any prototype reshape are downstream of Phase 1 exit, not upstream of it.

### Supersede cascade landed this pass

| File | Before | After |
|------|--------|-------|
| [`decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md`](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) | Accepted | **Superseded by 2026-04-24** |
| [`decisions/2026-04-22-step-b-prototype-reshape-plan.md`](decisions/2026-04-22-step-b-prototype-reshape-plan.md) | Proposed | **Superseded by 2026-04-24** |

### Step A cascade §-edits — preserved in-tree as superseded-record (NOT force-reverted)

These §-edits from the 2026-04-21 Step A pass remain in the repo as raw material for the reopen and must be re-ratified, rewritten, or explicitly retired as Phase 1 exits:

- `CONCEPT.md` hub (phase-index + vision line; commit `b4af2cf`)
- `README.md` critical-context #3 (3/3/3 lean-launch floor; commit `714d922`)
- `concept/phase-1.md §1.1` (Ash→Altar arc; commit `6722da6`) + `§1.3` (Tier persistence; commit `104da80`)
- `concept/phase-2.md §2.3` (risks cascade; commit `5c8aaa6`)
- `concept/phase-3.md §3.1/§3.2/§3.3/§3.4/§3.5/§3.6/§3.8` (3-lineage/3-tier; commits `aeaa911` + `baffc67`)
- `concept/phase-4.md §4.1/§4.2/§4.3/§4.5/§4.6/§4.7` (roster 5→3, divergence 2-fork OPEN, Ash-enabler, tar-pit genericized, currency OPEN, enemy OPEN; commits `15258ac` + `fe71792` + `c165716`)
- `concept/phase-5.md §5.1/§5.2/§5.3` (MVP=3/3/3, build phases, silhouette-forward; commits `08ae397` + `61532eb`) — `§5.4 [LOCKED]` UNTOUCHED
- `concept/phase-6.md §6.1–§6.4` (tier-persistence, Post-hybrid-families; commit `9ffcc90`)
- `concept/phase-7.md §7.1/§7.3/§7.4` (roster closed at 3, questions retired; commit `41dfd8f`)
- `stages/01-commander-pick.md §2` stub-amend (commit `27debcb`)
- `stages/04-in-match-core.md` A7-style amendment banner (commit `f99fd14`)
- `stages/05-age-evolution.md §2` stub-amend (commit `e4f42e8`) + upstream-deps link (commit `8078c2f`)
- `stages/06-hybrids-fusion.md §2` stub-amend (commit `73b5694`)

### Un-rebased 2026-04-20 decisions (reconcile at Phase 1 exit)

Each carries a 2026-04-21 "rebased by" banner inline that now points at a Superseded parent. DO NOT force-revert or silently re-rebase.

- [`decisions/2026-04-20-commander-identity-floor.md`](decisions/2026-04-20-commander-identity-floor.md) — identity-floor *structure* survives; roster scope (originally narrowed 5→3) now unknown pending Phase 1 exit.
- [`decisions/2026-04-20-age-history-flavor-mapmods.md`](decisions/2026-04-20-age-history-flavor-mapmods.md) — age-gate *logic* survives; `ages.json` 11→3 tier collapse now void under age-model deferral.
- [`decisions/2026-04-20-commander-pick-identity-upgrade.md`](decisions/2026-04-20-commander-pick-identity-upgrade.md) — silhouette-test + XP-ladder logic survives; roster collapse 5→3 now unknown pending Phase 1 exit.

### Docs delta this pass

- 1 new decision entry (`2026-04-24-phase-1-vision-reopen-...`)
- 2 decision entries status-flipped (2026-04-21, 2026-04-22)
- `CASCADE.md` v0.18 → v0.19 (pointer + table + doc-version)
- `PROGRESS.md` session-log row + reopen-debts block
- **Not touched:** any `concept/phase-*.md`, `CONCEPT.md` hub, `README.md`, `stages/*`, `CONCEPT-GAPS.md`, `admin/concept.json`, any prototype file, any 2026-04-20 decision body.

---

## Open threads / carried debts

### Highest priority (blocks the next substantive step)

- **Q2 — World pitch.** Next session's first substantive output. What IS the world? The synthetic mythic-history braid — what are its one-paragraph flavor rules? What makes the era system feel historic + religious + mythic + philosophical simultaneously without being generic or pastiche? Do NOT proceed past Q2 before PM signs off.

### Socratic discovery sequence (Q2–Q10, one per turn, PM drives pacing)

From [`decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md`](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) Follow-up #5 (and HANDOFF 2026-04-24 earlier):

1. **Q2 — World pitch.** (See above.)
2. **Q3 — Actors.** Who is the Commander in this world? What are the lineages (how many, what do they represent)? What are towers — structures, spirits, summoned warriors? Are there sent-units/minions at all?
3. **Q4 — Match arc.** What story does one match tell in this world?
4. **Q5 — Age model.** Contextually answerable after world + actors land. Within-match, seasonal, campaign, or braid?
5. **Q6 — Hybrid topology.** Enabler? Any-pair? No hybrid distinction? What does hybridizing MEAN in this world?
6. **Q7 — Economy.** What resources drive the game in the new frame?
7. **Q8 — Title.** Candidates under §5.4 conventions; 3x debug loop on options.
8. **Q9 — 3x debug loop** over the full rebuilt concept.
9. **Q10 — Ratification + cascade execution plan.** Which phase files update, which decisions rebase, which retire.

### Phase 1 exit rubric

Phase 1 exits when the PM can answer, in one page, **three things**:

1. What the world is.
2. What the Commander's role in it is.
3. What hybrid topology expresses about the world.

Until that page exists, Phase 1 stays open. Age-model reopening, title-lock reopening, and all downstream reconciliation (Step A §-edits, un-rebased 2026-04-20 decisions, Step B re-planning) wait on this gate.

### Deferred / still open

- **Naming pass** — specific names (Ash / Nature / Prayer / Dust / Form / Apotheosis) were prose placeholders under the superseded 2026-04-21 direction. §5.4 naming conventions [LOCKED] stay locked; next naming pass is downstream of Phase 1 exit.
- **Working-title "Ash to Altar"** — no longer thematically load-bearing. Remains working-only; Q8 addresses near end of reopen sequence.
- **Prototype reshape** — whatever shape Phase 1 exits to will imply a new prototype reshape plan. The 2026-04-22 Step B plan body remains in-tree as a template pattern (18 sub-steps, lint-relax/retighten, index.html quadrant splits, PROGRESS/HANDOFF close) that can be re-instantiated against the new target shape.
- **Step 5 playtest** — parked. Downstream of Phase 1 exit + new prototype reshape.
- **11 CONCEPT-GAPS rows** — unchanged from prior handoff; all flagged shape-independent by 2026-04-21 A8 audit; remain a separate PM-gated workstream after Phase 1 exits.
- **2026-05-15 freeze date** — soft under the reopen; reassess at Phase 1 exit.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **conventions** [LOCKED] (specific names can change; conventions cannot).
- `concept/phase-2.md §2.4a` accessibility floor [LOCKED].
- Mechanics surface (TD / merge / debuff / magic) — preserved across the reopen.
- Prototype files — no edits until vision ratifies + new reshape plan filed.

---

## Cadence rules carried forward

- **One file per turn.** Propose → PM "go" → produce → verify → tick.
- **Push to BOTH `session/2026-04-24-phase-1-reopen` AND `main` after every commit.** Fast-forward only.
- **Local-main hygiene:** if local `main` is ever diverged from `origin/main` by a pushed branch, reset local to origin before merging (safe pattern used this session; don't force-push main).
- Q2–Q10 pacing: one question per turn, PM drives. No batching.
- 3x debug loop on any CONCEPT-constraint-touching proposal, unprompted.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. 2026-04-25+ session — Phase 1 vision reopen
FILED and cascading. Bootstrap per CLAUDE.md:
README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

Before bootstrapping: verify local main is current.
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty
If not, pull --ff-only before reading any doc — the 2026-04-24
session recovered from a 31-commit-stale local main; don't repeat.

State aloud (before producing anything):
- Phase status + drift vs. last HANDOFF (2026-04-24 later).
- Open blockers (Phase 1 exit gate = one-page world/role/topology;
  Q2 is the first substantive ask).
- Specific next-step proposal: Q2 — world pitch. ONE candidate
  world-statement draft (not a ratification), following the
  synthetic mythic-history braid direction. 3x debug loop inline.

Wait for PM "go" before producing anything. One step per turn;
no batching.

CADENCE: ONE FILE PER TURN. Push to BOTH session branch AND main
every commit (fast-forward only).

ACTIVE DIRECTION (ratified 2026-04-24):
- Full Phase 1 reopen. Vision, theme, shape, hybrid topology, title
  all open. Reversibility Hard.
- Thematic direction: synthetic mythic-history braid — history +
  comparative religion + mythology + philosophy braided into ONE
  invented world. Not remix. Not side-by-side pastiche. Not
  multiverse.
- Mechanics preserved (TD/merge/debuff/magic).
- §2.4a accessibility floor [LOCKED], §5.4 naming conventions
  [LOCKED] — untouched.
- Age model deferred until world/story/background land.
- Prototype frozen. Step 5 playtest + any reshape downstream of
  Phase 1 exit.

DO NOT:
- Force-revert Step A §-edits (they're preserved in-tree as
  superseded-record; raw material for the reopen).
- Silently re-rebase the three un-rebased 2026-04-20 decisions
  (commander-identity-floor / age-history-flavor-mapmods /
  commander-pick-identity-upgrade) — reconcile only at Phase 1 exit.
- Touch §2.4a or §5.4 conventions.
- Touch any prototype file.
- Edit any concept/phase-*.md, CONCEPT.md, README.md, or stages/*
  before Q10 ratification.
- Treat "Ash to Altar" working title as load-bearing. It is not.

FIRST MOVE NEXT SESSION:
  Q2 — World pitch. One candidate world-statement (draft, not
  ratified) following the synthetic mythic-history braid direction.
  3x debug loop inline. Output is a single artifact — likely a new
  scratch file under decisions/ as a Proposed entry, OR a conversation
  response for PM to iterate on. PM chooses format.

Then Q3..Q10 one per turn, PM drives pacing.

Phase 1 exits when PM can answer in ONE PAGE:
  (1) what the world is,
  (2) the Commander's role in it,
  (3) what hybrid topology expresses about the world.
```

---

## Escalation triggers (for any future autonomous pass on Phase 1)

Hard-stop and flag if:

- A proposed sub-decision would touch `§2.4a` or `§5.4`.
- A proposed sub-decision would force-revert Step A §-edits rather than re-ratify/rewrite/retire.
- A proposed sub-decision would silently re-rebase the un-rebased 2026-04-20 decisions.
- A proposed sub-decision would touch mechanics (TD/merge/debuff/magic) — reopen Option B was explicitly rejected.
- A proposed direction drifts away from synthetic (toward remix), braided (toward side-by-side), or single invented world (toward multiverse).
- Local `main` is stale on session start — stop and resync before reading docs.
- `cascade-lint` fails and fix > 5min.

---

*End of HANDOFF — 2026-04-24 later. Phase 1 vision reopen FILED. Supersede cascade landed. Next session: Q2 world pitch, Socratic Q2–Q10 one per turn PM-driven. Phase 1 exit gate = one-page world/role/topology answer.*
