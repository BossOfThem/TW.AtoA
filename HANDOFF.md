# HANDOFF — Session Checkpoint

**Last session:** 2026-05-04 (mid-session checkpoint, NOT a clear-safe handoff yet — see "Live thread" below).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session if /clear happens, OR continuation of this session if PM continues here

---

## ⚠️ READ THIS FIRST — Live thread, /clear is NOT FULLY SAFE

This handoff exists for **mid-session preservation only**, written because PM was burned in the 2026-05-03 session by a /clear that was advised "good to go" but wasn't. If /clear happens here, you can resume safely on **Round 6 of the auxiliary-economy + game-modes ratification**, but the live thread has 10 open ratification axes and PM has not yet picked Recommended-first options on any of them. The conceptual frame for the balance-pass IS fully landed and clear-safe.

---

## TL;DR (what just happened, what's next)

**This session's work, in order:**

1. PM picked **Follow-up #13 balance-pass** (Recommended) on next-track gate.
2. PM pasted an external-LLM brainstorm prompt (variable nomenclature (a)–(k), per-round template, engagement-time integral form) and asked Claude to **complete the equation conceptually** before any numbers — explicitly "do not draft code, do not propose numbers."
3. Claude produced a gap-analysis (length: ~3000 words) flagging missing variables, unclosed economic loop, (k)-compounding anti-pattern, RHS-vs-LHS placement, status-proc cross-tower feedback, etc.
4. PM directed: use `AskUserQuestion` with Recommended-first options for ALL questions; reminded that the currency is **Tribute (primary) + Divinity (secondary)**, NOT "gold."
5. Claude ran **5 rounds of AskUserQuestion** (4 questions per round). PM picked Recommended on every option except Round 5's sell-refund (where PM proposed a custom 3-step / 4-step decay schedule that Claude ran a 3x debug loop on, then synthesized as the final ratified shape).
6. Round 5 spawned a **Priority-#1 scope expansion**: PM rejected flat Tribute-interest carry-over and proposed a **modular auxiliary economy structure** (Squadron TD-inspired) plus a **5-mode game ontology** (Solo / Horde Co-op / PvE Multiplayer / PvP Interest Wars Lane / PvP Maze Lane). PM directed all of this be locked in MD form before any further questions to prevent context loss.
7. Claude wrote the Squadron TD synthesis (training-data based, web-search not loaded), filed two decision documents, updated CASCADE/PROGRESS/CONCEPT-GAPS, rewrote HANDOFF.

**Two decision documents filed this turn:**

- [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) — **Accepted, Medium.** 17-item conceptual frame for tower-vs-unit math. The full source-of-truth for the equation. Numbers-phase Follow-up #13 consumes this frame.
- [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](decisions/2026-05-04-auxiliary-economy-and-modes-scope.md) — **Proposed, Easy.** 10 open ratification axes for Round 6+. Squadron TD send-creeps loop, Element TD research tree, BTD6 Knowledge tree, Legion TD 2 Mercenaries, Line Tower Wars maze pattern all referenced as adjacent points. Research pass `research/06-tw-subgenres.md` planned downstream.

**No code edits this turn.** This is concept/math work only. `prototype/index.html` and `prototype/data/*.json` untouched.

---

## What is locked (clear-safe)

The 17-item conceptual frame in [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) is **Accepted**. If /clear happens, the next session restores by reading that file. Frame summary:

| # | Item | Locked value |
|---|------|--------------|
| 1 | (k) difficulty | Easy / Hard / Hardcore (3 tiers, locked) |
| 2 | Win condition | Lives > 0 at end of R30; per-leak severity tunable |
| 3 | Damage form | `Σ_T [DPS(T) × t_engaged(T,R) × matchup × passive_modifiers × status_state]` |
| 4 | (o) Divinity | First-class second currency; cap 6/match; drain 2 (Fusion menu) + 1×N (per fusion) |
| 5 | (l) lifecycle | Tier × Level both axes first-class. Tier {T1,T2,T3,T4,God} via merge/promote/fuse. Level {1,2,3} via in-place Tribute upgrade. |
| 6 | (k) compounding | Single-axis exponent shift on HP-curve only. No multi-axis. |
| 7 | Commander (h) | Three slots (passive / short-CD active / long-CD signature) × four effect types (damage / control / summon / economy) |
| 8 | Status + armor | (p) 5-bucket armor + (q) 7-proc status full feedback + cross-tower combos explicit |
| 9 | Round slot typology | 7-slot (Standard / Swarm / Elite / Modifier / Telegraph / Boss / Recovery) |
| 10 | R-assignments | R5 Modifier · R10 Boss · R15 Elite · R20 Modifier · R25 Telegraph · R30 Final Boss |
| 11 | (j) map model | Per-map (ε, N) tuple — engagement coefficient + buildable hex count |
| 12 | Lives | 10 fixed across all (k) |
| 13 | Sell refund | Pre-wave 100% / same-wave 90% / R+1 80% / R+2 70% / R+3+ 60% flat. T4 capped 60%. (k)-coupled (Easy full / Hard floor 60% / Hardcore floor 50%) |
| 14 | Targeting | AI default First; per-tower override {First / Last / Strongest / Weakest / Closest} |
| 15 | Boss reward | R10 medium lump + 1 Divinity. R15 medium lump + 0 Divinity. R30 huge lump + 2 Divinity. |
| 16 | Divinity source (interim) | R10/+1 · R20-zero-leak-streak/+1 · R30/+2 · 2 escalation hooks TBD. Foresight-coin Follow-up #7 final ratification. |
| 17 | Skill bars | 3 axes — matchup-rate / placement-coverage / ability-uptime |

Numbers are NOT in this frame. Numbers-phase = Follow-up #13.

---

## Live thread — Round 6 onward (NOT clear-safe yet)

PM has not picked Recommended on these yet. If /clear happens, the next session resumes by reading [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](decisions/2026-05-04-auxiliary-economy-and-modes-scope.md) and surfacing Round 6 questions.

**10 open ratification axes:**

1. Auxiliary structure scope (single global / per-commander / per-mode / modular slot system)
2. Mode-gated vs universal slot families (table proposed in decision; needs ratification)
3. Currency interface (Tribute? Divinity? third currency?)
4. Squadron-TD send-creeps adoption (PvP Interest Wars only? Co-op? Solo? kill?)
5. Mode prioritization (which 2-3 modes ship at launch vs Patch-1+?)
6. Maze-mode tower-as-path conflict with hex placement model
7. Per-mode (k) — does Easy/Hard/Hardcore apply to all modes?
8. Auxiliary structure UX (separate scene? in-match panel? right-click? between-rounds phase?)
9. Interaction with balance-pass-#1 frame — auxiliary upgrades cross-cut (a)/(c)/(e)/(f); first-class variable (s)?
10. Co-op send-mechanics safety (helpful or harmful or configurable?)

**5-mode roster (PM-stated):**

1. Solo Campaign — single-lane, map-shaped path complexity, (k) Easy/Hard/Hardcore, zoom controls
2. Horde Co-op — 2-8 players team-mode, scales with player count × difficulty
3. PvE Multiplayer — 8 identical parallel lanes, last-alive elimination
4. PvP Interest Wars Lane — own lane, send-creeps + interest-from-sends, 15-30s rounds, send-to-any-lane chaos
5. PvP Maze Lane — towers create the lane (Line Tower Wars pattern) + cheap stone blockers

**Auxiliary structure slot families (proposed):**

- Universal: targeting overrides, build-queue, tower-count expansion, level/upgrade/fusion choice, Damage Bonus, Economy Bonus
- PvP only: send-troops-to-PvP-lane
- Co-op + PvE: call-for-help (one-shot soft-assist)
- Maze mode only: maze stone (cheap blocker upgradable to tower)
- PvP Interest Wars: send-for-Interest (Squadron TD pattern)

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest pushed commit: `2e56cf5` (prior session's Aztec glyph close), dual-pushed.
- **This session's work uncommitted as of this HANDOFF write.** Files staged for next commit:
  - `decisions/2026-05-04-balance-pass-1-conceptual-frame.md` (NEW)
  - `decisions/2026-05-04-auxiliary-economy-and-modes-scope.md` (NEW)
  - `CASCADE.md` (pointer + decisions table + version footer)
  - `PROGRESS.md` (session log)
  - `CONCEPT-GAPS.md` (rows ECON-04 + MODE-01 + MATH-01)
  - `HANDOFF.md` (this rewrite)
- Working tree dirty pending commit + dual-push.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (2026-04-27 + C7.a/C7.b prototype).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28).
- **Prototype reshape arc: COMPLETE** + C4-continuation polish + Follow-up #4 closed (2026-05-04 earlier).
- **Balance-pass #1 conceptual frame: RATIFIED** (this turn, 2026-05-04 later).
- **Auxiliary economy + game modes ontology: PROPOSED** (this turn, Round 6+ ongoing).

### Doc-hygiene state

- `PROGRESS.md` session log: 4 entries (2026-05-04 later · 2026-05-04 earlier · 2026-05-03 · 2026-05-02). At next handoff trim 2026-05-02 to archive.
- `CASCADE.md` pointer: 2 most-recent blocks (this turn + earlier-same-day Aztec glyph). Trim earlier block to history at next handoff.
- `CASCADE.md` version footer: v0.36 + v0.35 reference.
- `CONCEPT-GAPS.md`: 11 active gaps + 3 new (ECON-04 / MODE-01 / MATH-01-resolved). MATH-01 marked resolved-by-decision.

### Open follow-ups (carried)

- **#5 — Cultural-sensitivity pass.** Hard pose-lock + content-lock gate. Now also gates Aztec glyph re-eval.
- **#6 — Patch-1 commanders + Thor recipe-layer dissonance.**
- **#7 — Foresight-coin / PvE campaign + AGES + leveling + attributes.** Now also owns final Divinity-source ratification (interim pattern locked in balance-pass-#1).
- **#8 / #9 — non-boss enemy ontology / additional commanders.**
- **#11 — Norse round-30 boss CLOSED at Jörmungandr.**
- **#13 — Numbers-phase balance-pass.** Now downstream of conceptual frame; consumes frame to produce ratified values for (a)/(c)/(e)/(f) curves + (g) magnitudes + (h) ability magnitudes + (k) exponent values + (j) per-map (ε, N) values + skill-bar threshold numbers per (k).
- **NEW — Auxiliary economy + game modes ontology (Round 6+).** 10 open axes; 5-mode roster proposed; slot-family table proposed. Awaiting PM Recommended-first picks.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape.

### Regression-watch (still live from prior cuts)

- Tutorial / match flow / merge-preview hover / Promote-T4 indicator / Aztec glyph (◈) / `logBalanceCurve` / `effectiveTowerStats` / snapshot — all from 2026-05-03 + 2026-05-04 earlier session, unchanged this turn.

---

## NEXT SESSION — primary directive

**If you are reading this after a /clear:** the live thread is **Round 6 of the auxiliary-economy + game-modes ratification**. Do this:

1. Read [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) (the ratified frame).
2. Read [`decisions/2026-05-04-auxiliary-economy-and-modes-scope.md`](decisions/2026-05-04-auxiliary-economy-and-modes-scope.md) (the live thread).
3. Surface Round 6 via `AskUserQuestion` with Recommended-first options. Suggested first batch:
   - Q1: Auxiliary structure scope (single global / per-commander / per-mode / modular slot system) — **Recommend modular slot system**, mode-aware content.
   - Q2: Currency interface (Tribute only / Divinity only / both / third currency) — **Recommend both Tribute + Divinity**, with Tribute for tactical slots and Divinity for strategic slots.
   - Q3: Mode prioritization for launch — **Recommend Solo Campaign + Horde Co-op as launch surface**; PvE-MP / PvP Interest Wars / PvP Maze as Patch-1+.
   - Q4: Send-creeps mechanic adoption — **Recommend PvP Interest Wars only at launch**; explore Co-op variant Patch-1+.
4. Continue rounds based on PM picks. Per-mode deep-dives (Round 7+) follow.

**If PM redirects off this thread:** fall back to numbers-phase Follow-up #13 (the conceptual frame is locked; numbers can be tuned independently of the auxiliary thread, with the caveat that auxiliary upgrades may cross-cut (a)/(c)/(e)/(f) requiring frame extension).

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]** — Lineages-row amendment LANDED 2026-04-28; no further row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton (3 civs × 6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods + 9 Fusion recipes + commander signature-ability names + Tribute/Divinity economy + 30-round arc).
- The 17-item conceptual frame in `2026-05-04-balance-pass-1-conceptual-frame.md` is **Accepted**. To revise any item, file a superseding decision; do not silently edit the frame.

---

## Cadence rules carried forward

**Cadence exists to manage the context window, not to gate every step.** PM 2026-05-03 + 2026-05-04 confirmed: per-step "propose → go → produce" rituals overclock the context window when the plan is concrete.

- **When a plan is concrete:** execute end-to-end without intermediate gates. Batch parallel-safe edits. Verify with `python tools/cascade-lint.py`. Commit. Dual-push. Summarize once at the end.
- **When to gate via AskUserQuestion:** cardinality breaks, [LOCKED] surface conflicts, cultural-sensitivity gates, mid-step scope blow-ups, **number-set proposals where PM has not pre-specified values**, **conceptual ratifications across multiple alternatives**. Always include a "Recommended" first option.
- **Context-pressure self-trim:** when context budget tightens, batch tool calls, group parallel-safe edits, and re-gate only if context will not survive completion.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.
- **MD-first preservation:** PM 2026-05-04 directive — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions. /clear must be safe at any prompt.

---

## Next-session prompt (copy-paste after `/clear` only if PM explicitly says clear is safe)

```
Resuming Ash to Altar — Balance-pass #1 conceptual frame is RATIFIED
(decision 2026-05-04-balance-pass-1-conceptual-frame.md, Accepted/Medium,
17-item frame across 5 AskUserQuestion rounds). Auxiliary economy
structure + game modes ontology is PROPOSED (decision 2026-05-04-
auxiliary-economy-and-modes-scope.md, Proposed/Easy, 10 open axes).
Live thread: Round 6 of the auxiliary-economy ratification.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty after dual-push

STATE ALOUD (before producing anything):
- Phase status: balance-pass-#1 frame Accepted; aux-economy + modes
  Proposed; numbers-phase Follow-up #13 downstream of frame; reshape
  arc + C4-continuation + Follow-up #4 closed.
- Open blockers: none load-bearing (frame locked). Live thread:
  10 ratification axes for Round 6+ on aux-economy + modes.
- Specific next-step: surface Round 6 via AskUserQuestion with
  Recommended-first options. Suggested first batch in HANDOFF
  "NEXT SESSION" section.

CADENCE: PM 2026-05-04 directive — MD-first preservation. Land in
MD before further questions on scope expansions. AskUserQuestion
with Recommended-first for all conceptual ratifications. Execute
end-to-end when plan concrete; gate on genuine ambiguity.

CURRENCY REMINDER: Tribute (primary) + Divinity (secondary, cap 6/match,
drain 2 + 1×N for Fusion). NOT "gold." External LLM brainstorm prompts
that say "gold" map to Tribute on the LHS.

REGRESSION-WATCH (carries from earlier sessions):
- Tutorial / match flow / merge-preview / Promote-T4 indicator /
  Aztec glyph ◈ / logBalanceCurve / effectiveTowerStats / snapshot
  — all unchanged this turn.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 locked content skeleton
  untouched.
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract
  civ art.
- Reshape arc closed. Do not regress legacy lineage/age surfaces.
- The 17-item conceptual frame is Accepted. Revisions go through a
  superseding decision, not silent edits.

If PM redirects off Round 6 thread: fall back to numbers-phase
Follow-up #13 (frame is locked; numbers tunable independently with
caveat about auxiliary cross-cuts).
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
- Any attempt to regress retired lineage/age surfaces back into the prototype.
- A balance-pass numbers commit lands without a `decisions/<date>-balance-pass-N-numbers.md` entry capturing [PROPOSAL] → ratified-numbers diff.
- **The 17-item conceptual frame would be silently edited.** Revisions must file a superseding decision.
- **A scope expansion occurs and PM has not landed it in MD before further questions.** Per 2026-05-04 directive — preserve before progressing.
