# HANDOFF — Session Checkpoint

**Last session:** 2026-05-05 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Numbers-phase Follow-up #13 — ARC CLOSED. Rounds 1–10 of 10 LANDED across 4 commits, all dual-pushed to session branch + main.**

Ten `AskUserQuestion`-driven ratification rounds bound concrete numbers/magnitudes onto the 17-item conceptual frame (Balance-pass #1, ratified 2026-05-04) + extension variable (s):

1. **Round 1 — Runner HP curve (e).** `HP_std(R) = 100 · 1.16^R` Easy baseline; boss-spike overlay R10 ×3 / R15 ×2 / R30 ×5.
2. **Round 2 — (k) compounding exponents.** Easy 1.16 / Hard 1.19 / Hardcore 1.22.
3. **Round 3 — Tribute economy (a).** `yield(R) = 5 · 1.10^R` per std kill; boss lumps R10=250 / R15=400 / R30=1,500.
4. **Round 4 — Speed (f) + per-map (j).** `f_base = 50 u/s` constant; archetype mults Std 1.0 / Swarm 1.5 / Elite 1.0 / Boss 0.7 / Colossal 0.5; ε=0.6, N=24 defaults.
5. **Round 5 — Tower (c) DPS ladder + tier costs.** T1=1×/T2=3×/T3=9×/T4=27×/God=54×; T1_base=20 dmg/sec; costs 100/300/900/2,500 Tribute (Fusion=Divinity-priced).
6. **Round 6 — Commander (h) damage-variant floor.** Passive +15% / 2-cell civ-aura; active 4× T3 DPS / 3-cell / 4s / 30s CD; signature once-per-match free tier-up.
7. **Round 7 — Aux-slot costs + (s) ranges.** Damage Bonus 1 Div=(s)=1.20 global; Economy Bonus 1 Div=+25% per-kill yield; Tower-count expansion 1 Div=+2 N (cap 3 Div); Send-Creeps 100 T / Call-for-Help 300 T / Maze Stone 25 T.
8. **Round 8 — Per-mode tuning.** Solo Off-Wave + PvE-MP Lane-Trade 100 T → 3 creeps + +50% kill-bonus; Horde Reinforce-Lane 1 helper @ 4× R-HP; PvP-Maze Send-Through +5 T/round; PvP-IW Send-for-Interest 1 Div unlock + 150 T/send + +3 T/round (Squadron pattern). Per-mode N: Horde-B = 24×player_count linear; PvP-Maze N=30. PvP tie-break: R31+ HP×1.5^(R-30) + R45 co-victory.
9. **Round 9 — Skill-bar thresholds per (k).** Matchup-correctness Hardcore 90% / Hard 75% / Easy 60% / novice 30%; Placement-coverage 80%/65%/50%/30%; Ability-uptime 80%/60%/40%/20%. Hardcore expert realized 0.576 × 1.725× = ~1.0× closes margin exactly.
10. **Round 10 — Divinity sources (CLOSES arc).** 4-Div floor (R10/R15/R30 boss + match-completion); Source 5 Perfect-Wave +1 Div per zero-leak boss-clear (max +3); Source 6 First-Hybrid +1 Div one-shot per topology-true hybrid. Ceiling 8 theoretical / 5-6 realistic expert fits 6-cap.

PM picked Recommended on every question across ~25 AskUserQuestion calls. Mid-arc (after R9) PM granted autonomy mandate: *"come to me only if you HAVE to for questions, I will continue using 'recommended' for the most part unless there is something you really need to flag me for."* Saved as feedback memory `feedback_autonomy_mandate.md`. R10 produced autonomously; final post-arc fork surfaced as genuine scope question (handoff vs which authoring sub-pass to open).

Ten new decision documents filed; CASCADE bumped v0.37 → v0.47 across the arc. cascade-lint clean throughout.

**No code edits this session.** Pure concept/math work. §2.4a + §5.4 [LOCKED] + 17-item conceptual frame untouched (only magnitudes for items (e), (k), (a), (f), (j), (c), (l), (m), (h), (s) bound + skill-bar input rates + Divinity sources defined; shapes unchanged).

**All 17 conceptual-frame variables (a)-(r) + extension (s) now have ratified magnitudes.** Numbers-phase complete.

---

## What is locked (clear-safe)

### Carried forward from 2026-05-04 (untouched)

- Balance-pass #1 conceptual frame (17 items) — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure — Accepted.
- "Go big, no scope cuts" project doctrine — Accepted.
- Frame extensions: variable (s) first-class multiplicative; per-mode declarable lives.

### NEW this session (Rounds 1–10, full arc)

| Item | Locked value |
|------|--------------|
| (e) HP base curve | `HP_std(R) = 100 · 1.16^R` Easy; boss overlay R10 ×3 / R15 ×2 / R30 ×5 |
| (k) exponents | Easy 1.16 / Hard 1.19 / Hardcore 1.22 (single-axis HP-only) |
| (a) per-kill yield | `yield(R) = 5 · 1.10^R`; constant across (k); R30=87/kill |
| (a) boss lumps | R10=250 / R15=400 / R30=1,500 |
| (f) speed | f_base=50 u/s; archetype mults Std 1.0 / Swarm 1.5 / Elite 1.0 / Boss 0.7 / Colossal 0.5 |
| (j) per-map defaults | ε=0.6, N=24; Horde-B 24×player_count; PvP-Maze N=30 |
| (c) DPS ladder | T1=1×/T2=3×/T3=9×/T4=27×/God=54× off T1_base=20 dmg/sec |
| Tier-up costs | T1=100 / T2=300 / T3=900 / T4=2,500 Tribute; Fusion=0 Tribute + 1 Divinity |
| (h) passive | +15% / 2-cell civ-gated aura |
| (h) active | 4× T3 DPS / 3-cell / 4s / 30s CD = 2,880 burst |
| (h) signature | Once-per-match free tier-up T1→T2 or T2→T3 |
| (s) Damage Bonus | 1 Div = (s)=1.20 global, max 1 active/match |
| Economy Bonus | 1 Div = +25% per-kill yield, max 1 active/match |
| Tower-count expansion | 1 Div = +2 N, cap 3 Div |
| Send-Creeps cost | 100 T baseline; PvP-IW SfI = 1 Div unlock + 150 T/send |
| Skill-bar Hardcore expert | Matchup 90% / Placement 80% / Uptime 80% |
| Skill-bar novice (all k) | Matchup 30% / Placement 30% / Uptime 20% |
| Divinity floor | 4 Div (R10 + R15 + R30 + match-completion = 1 each) |
| Divinity Source 5 | Perfect-Wave: +1 Div per zero-leak boss-clear, max +3 |
| Divinity Source 6 | First-Hybrid: +1 Div one-shot per topology-true hybrid |
| Divinity ceiling | 8 theoretical / 5-6 realistic expert (fits 6-cap) |
| PvP tie-break | R31+ HP × 1.5^(R-30) + R45 co-victory floor |

Hardcore winnability ground (Round 2): expert skill-stack ~5× × tier-ladder 54× = ~270× expert effective damage; Hardcore R30 std HP ~565× R1 → margin closes via 1.725× per-tower stack ((s) 1.20 × (h passive) 1.15 × (q matchup) 1.25) + Round 9 realized 0.576 coverage = ~1.0× realized at expert thresholds.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit: **`7ddccab`** — "Numbers-phase #13 Round 10: Divinity sources — CLOSES arc 10/10."
- Prior arc commits: `d23c651` (R7-R9), `363047e` (R4-R6), `b9a25a1` (R1-R3).
- All four arc commits dual-pushed to session branch AND `main`. `git log HEAD..origin/main` should be empty.
- Working tree: only `.accord/` (untracked, untouched).

### Phase status

- All Phase 1–4 conceptual ratification carried forward.
- **Balance-pass #2 numbers-phase 100% done (10 of 10 rounds; arc CLOSED).**
- All 17 conceptual-frame variables (a)-(r) + extension (s) now have ratified magnitudes.
- Per-tower (cd, range, attack-type, status-proc) + per-commander (effect-type variants) + per-civ specialization + per-map (good-cell authoring + wave-randomization seeds + crystal-lock variance per Round 11 mandate) authoring sub-passes ALL deferred post-arc. Estimated 5-10 rounds each.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 entries (Round 10 / Round 9 / Round 8). Rounds 1–7 + 2026-05-04 archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (2026-05-05 Rounds 1–10, arc CLOSED).
- `CASCADE.md` version footer: v0.47 + v0.46 reference. Older in `CASCADE-history.md`.
- `CONCEPT-GAPS.md`: unchanged (11 active gaps + 3 resolved).

### Open follow-ups (carried)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art).
- **#6** — Patch-1 commanders + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **#11 (NEW post-R9)** — Round 11 mandate: random-seeded wave composition + per-map crystal-lock variance to defend skill-bar threshold integrity from memorization meta. Cross-cuts all 6 modes. Subset of per-map authoring sub-pass.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape.
- **CONCEPT.md amendment pending** — §-new "Tower-vs-Unit math" (consumes Rounds 1–10) + 12-round 2026-05-04 ratifications. Authoring-heavy.
- **`research/06-tw-subgenres.md`** new stub — Squadron TD / Legion TD 2 / BTD6 / Element TD / Line Tower Wars / Mini-TD deep dives.

### Authoring sub-passes (post-arc, no order-of-operations locked)

- **Per-tower** — bind cd / range / attack-type / status-proc variance for 18 T1-T3 + 18 T4 Demigod + 9 God across 3 civs.
- **Per-commander** — bind control / summon / economy effect-type variants of the 3 (h) slots, equivalent-impact to damage-floor.
- **Per-civ** — specialization profile per Greek / Aztec / Norse (matchup affinities, identity hooks, signature creep types).
- **Per-map / Round 11** — good-cell authoring + wave-randomization seeds + crystal-lock variance.

### Regression-watch (unchanged this session)

- Tutorial / match flow / merge-preview hover / Promote-T4 indicator / Aztec glyph (◈) / `logBalanceCurve` / `effectiveTowerStats` / snapshot.

---

## NEXT SESSION — primary directive

**No single Recommended track.** The numbers-phase arc closing leaves multiple non-trivial branches with no obvious leader. PM must scope first.

Candidate tracks (in rough order of design-merit):

1. **CONCEPT.md amendment pass** — roll all 12 conceptual rounds + 10 numbers-phase rounds into CONCEPT.md as new §-sections. Doc-spine consolidation; high-value but authoring-heavy.
2. **Per-tower authoring sub-pass** — most concrete "numbers becoming game" progress. Likely 5-10 rounds binding cd / range / attack-type / status-proc across 45 towers.
3. **Per-map / Round 11 authoring sub-pass** — defends skill-bar threshold integrity. Cross-cuts all 6 modes; combines wave-randomization + crystal-lock + good-cell sets.
4. **Per-commander effect-type-variant authoring** — control / summon / economy variants of (h) slots; needs equivalent-impact-to-damage-variant constraint per R6.
5. **Per-civ specialization** — Greek / Aztec / Norse identity profiles; intersects #5 cultural-sensitivity Follow-up.
6. `research/06-tw-subgenres.md` deep-dive.
7. `admin/concept.json` migration — long-deferred staleness debt.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]**.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton.
- 17-item conceptual frame + extension (s) — **Accepted**. All Rounds 1–10 magnitudes — **Accepted**. Revisions require superseding decisions.
- 6-mode ontology + auxiliary economy structure — **Accepted**.
- "Go big, no scope cuts" project doctrine — **Accepted**.

---

## Cadence rules carried forward

- **Cadence exists to manage the context window, not to gate every step.** Concrete plan = execute end-to-end; gate on genuine ambiguity only.
- **PM autonomy mandate (NEW 2026-05-05):** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously without per-question gates. Surface AskUserQuestion only on genuine forks (no clear Recommended), scope expansion, cascade-violation risk, or handoff trigger. See `feedback_autonomy_mandate.md`.
- **AskUserQuestion is the standard interface** when gating is needed. Always Recommended-first.
- **MD-first preservation** — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions. /clear must be safe at any prompt.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit. Commit at every ~3 rounds.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — Numbers-phase Follow-up #13 ARC CLOSED 2026-05-05.
All 10 of 10 rounds LANDED. All 17 conceptual-frame variables (a)-(r) +
extension (s) now have ratified magnitudes. Four commits dual-pushed
across the arc (b9a25a1 + 363047e + d23c651 + 7ddccab). cascade-lint clean.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty after dual-push

STATE ALOUD (before producing anything):
- Phase status: Numbers-phase 10/10 COMPLETE; arc CLOSED. Per-tower /
  per-commander / per-civ / per-map authoring sub-passes ALL deferred
  post-arc (5-10 rounds each, no order-of-operations locked). CONCEPT.md
  amendment still pending (now consumes all 22 rounds: 12 conceptual +
  10 numbers). admin/concept.json staleness debt outstanding.
  research/06-tw-subgenres.md not yet written. Round 11 mandate
  (wave-randomization + crystal-lock variance) flagged within per-map
  sub-pass.
- Open blockers: none load-bearing.
- Specific next-step: surface AskUserQuestion with NO clear Recommended —
  PM must scope first. Candidate tracks (rough design-merit order):
    1. CONCEPT.md amendment pass (consolidates doc spine).
    2. Per-tower authoring sub-pass (cd/range/attack-type/status-proc
       across 45 towers).
    3. Per-map / Round 11 authoring (wave-randomization + crystal-lock
       + good-cell sets).
    4. Per-commander effect-type-variant authoring (control/summon/
       economy variants of (h) slots).
    5. Per-civ specialization (Greek/Aztec/Norse identity profiles).
    6. research/06-tw-subgenres.md.
    7. admin/concept.json migration.

CADENCE: AskUserQuestion is standard interface when gating needed.
Recommended-first. MD-first on scope expansions. Execute end-to-end
when plan concrete; gate on genuine ambiguity only. Commit + dual-push
every ~3 rounds.

PM AUTONOMY MANDATE (2026-05-05): once an arc establishes a stable
"PM picks Recommended" pattern, proceed autonomously within that arc.
Surface gates only on genuine forks / scope expansion / cascade-risk /
handoff. See feedback_autonomy_mandate.md.

CURRENCY REMINDER: Tribute (primary, kills) + Divinity (secondary,
cap 6/match, drain 2 + 1×N for Fusion). NOT "gold."

DOCTRINE REMINDER: "Go big, no scope cuts." Do NOT recommend the
smallest-scope option for dev-load reduction; recommend on design
merit only.

REGRESSION-WATCH: Tutorial / match flow / merge-preview / Promote-T4
indicator / Aztec glyph ◈ / logBalanceCurve / effectiveTowerStats /
snapshot — unchanged.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 locked content skeleton
  untouched.
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract civ
  art (intersects per-civ specialization track).
- 17-item frame + extension (s) Accepted.
- All Rounds 1-10 numbers-phase magnitudes Accepted.
- 6-mode ontology + auxiliary economy structure Accepted.
- "Go big, no scope cuts" doctrine Accepted.
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
- The 17-item frame would be silently edited.
- Any Round 1-10 bound magnitude would be silently re-tuned without a superseding decision entry.
- A scope expansion occurs and PM has not landed it in MD before further questions.
- Any recommendation invokes "lessen dev load" without explicit PM override of the "Go big" doctrine.
- An authoring-sub-pass commit lands without a `decisions/<date>-*-<slug>.md` entry capturing the bindings.
