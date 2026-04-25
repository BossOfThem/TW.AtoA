# HANDOFF — Session Checkpoint

**Last session:** 2026-05-05 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Numbers-phase Follow-up #13 — Rounds 1–6 of ~10 LANDED end-to-end across two commits (b9a25a1 + 363047e), both dual-pushed to session branch + main.**

Six `AskUserQuestion`-driven ratification rounds bound concrete numbers/magnitudes onto the 17-item conceptual frame (Balance-pass #1, ratified 2026-05-04) for the PvE-arc math:

1. **Round 1 — Runner HP curve (e).** `HP_std(R) = 100 · 1.16^R` Easy baseline; boss-spike overlay R10 ×3 / R15 ×2 / R30 ×5.
2. **Round 2 — (k) compounding exponents.** Easy 1.16 / Hard 1.19 / Hardcore 1.22 (symmetric +0.03 step).
3. **Round 3 — Tribute economy (a).** `yield(R) = 5 · 1.10^R` per std kill (constant across (k)); boss lumps R10=250 / R15=400 / R30=1,500. Easy R1→R30 cumulative ≈25K Tribute.
4. **Round 4 — Speed (f) + per-map (j).** `f_base = 50 u/s` constant across R + archetype mults (Std 1.0 / Swarm 1.5 / Elite 1.0 / Boss 0.7 / Colossal 0.5); ε=0.6, N=24 defaults.
5. **Round 5 — Tower (c) DPS ladder + tier costs.** T1=1×/T2=3×/T3=9×/T4=27×/God=54× (geometric ×3×3×3×2; T1_base=20 dmg/sec) + costs T1=100 / T2-merge=300 / T3-merge=900 / T4-promote=2,500 (Fusion=Divinity-priced). Expected on-curve spend ~10.7K → ~14.3K Tribute headroom for aux + cycling.
6. **Round 6 — Commander (h) damage-variant floor.** Passive +15% / 2-cell civ-gated aura; active 4× T3 DPS / 3-cell / 4s / 30s CD (2,880 burst); signature once-per-match free tier-up T1→T2 or T2→T3.

PM picked Recommended on every question across 11 AskUserQuestion calls; no override notes. 3x debug loop ran inline pre-each-ratification. Six new decision documents filed; CASCADE bumped v0.37 → v0.43 across 6 pointer/row/footer cycles. cascade-lint clean throughout.

**No code edits this session.** Pure concept/math work. §2.4a + §5.4 [LOCKED] + 17-item conceptual frame untouched (only magnitudes for items (e), (k), (a), (f), (j), (c), (l), (m), (h) bound; shapes unchanged).

**Numbers-phase remaining:** Rounds 7–10 (aux costs + (s) ranges; per-mode tuning; skill-bar thresholds; Divinity sources).

---

## What is locked (clear-safe)

### Carried forward from 2026-05-04 (untouched)

- Balance-pass #1 conceptual frame (17 items) — Accepted.
- 6-mode ontology (Solo / Horde-A / Horde-B / PvE-MP / PvP-IW / PvP-Maze) — Accepted.
- Auxiliary economy structure (Tribute tactical / Divinity strategic; universal slot families; Send-Creeps in 3 modes) — Accepted.
- "Go big, no scope cuts" project doctrine — Accepted.
- Frame extensions: variable (s) first-class multiplicative; per-mode declarable lives.

### NEW this session (Rounds 1–6)

| Item | Locked value |
|------|--------------|
| (e) HP base curve | `HP_std(R) = 100 · 1.16^R` Easy; boss overlay R10 ×3 / R15 ×2 / R30 ×5 |
| (k) exponents | Easy 1.16 / Hard 1.19 / Hardcore 1.22 (single-axis HP-only) |
| (a) per-kill yield | `yield(R) = 5 · 1.10^R`; constant across (k); R30=87/kill |
| (a) boss lumps | R10=250 / R15=400 / R30=1,500 (Easy; constant across (k)) |
| (f) speed | f_base=50 u/s constant across R; archetype mults Std 1.0 / Swarm 1.5 / Elite 1.0 / Boss 0.7 / Colossal 0.5 |
| (j) per-map defaults | ε=0.6, N=24; per-mode N-scaling (Horde-B linear, PvP-Maze maze-cell, PvE-MP per-lane × N_lanes) deferred to Round 8 |
| (c) DPS ladder | T1=1×/T2=3×/T3=9×/T4=27×/God=54× off T1_base=20 dmg/sec Standard archetype |
| Tier-up costs | T1=100 / T2=300 / T3=900 / T4=2,500 Tribute; Fusion=0 Tribute + 1 Divinity |
| (h) passive | +15% damage to civ-matched towers within 2-cell hex aura; multiplicative; civ-gated |
| (h) active (damage variant) | 4× T3 DPS in 3-cell radius for 4s on 30s CD (= 2,880 burst) |
| (h) signature | Once-per-match instant tier-up of one targeted tower T1→T2 or T2→T3 (free; adjacency preserved; T3+ locked out) |

Hardcore winnability ground (Round 2): expert skill-stack ~5× × tier-ladder 54× = ~270× expert effective damage; Hardcore R30 std HP ~565× R1 → margin closes via passive (1.15×) + matchup (1.25×) + (s) aux (~1.2×, Round 7) + Fusion endgame.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit: **`363047e`** — "Numbers-phase #13 Rounds 4-6: speed + per-map / tower baselines / commander magnitudes."
- Prior commit: `b9a25a1` — "Numbers-phase #13 Rounds 1-3: HP curve + (k) exponents + Tribute economy."
- Both dual-pushed to session branch AND `main`. `git log HEAD..origin/main` should be empty.
- Working tree: only `.accord/` (untracked, untouched by this session) + this HANDOFF rewrite + PROGRESS log trim.

### Phase status

- All Phase 1–4 conceptual ratification carried forward. Balance-pass #2 numbers-phase 60% done (6 of ~10 rounds).
- **Numbers-phase Follow-up #13: 6 of ~10 rounds COMPLETE.** Remaining: aux costs + (s) (Round 7); per-mode tuning (Round 8); skill-bar thresholds (Round 9); Divinity sources (Round 10).
- Per-tower (cd, range, attack-type, status-proc) authoring sub-pass DEFERRED to post-Round 10 (consumes Round 5 ladder + T1_base anchor; iterates over locked 18 T1-T3 + 18 T4-Demigod + 9 God roster).

### Doc-hygiene state

- `PROGRESS.md` session log: 3 entries (Round 6 / Round 5 / Round 4). Rounds 1–3 + two 2026-05-04 entries archived to `PROGRESS-archive.md` this handoff.
- `CASCADE.md` pointer: 1 most-recent block (2026-05-05 Rounds 1–6). Prior 2026-05-04 end-of-day pointer already archived.
- `CASCADE.md` version footer: v0.43 + v0.42 reference. Older versions in `CASCADE-history.md`.
- `CONCEPT-GAPS.md`: unchanged (11 active gaps + 3 resolved).

### Open follow-ups (carried)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art).
- **#6** — Patch-1 commanders + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes (Phase-3-onward meta-progression artifact).
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **#13 — Numbers-phase balance-pass — Rounds 7–10 remaining.** Also: per-tower authoring sub-pass post-R10; per-commander effect-type-variant authoring sub-pass post-R10 (control / summon / economy variants of the 3 slots, equivalent-impact to damage variant).
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape.
- **CONCEPT.md amendment pending** — §-new "Tower-vs-Unit math" (consumes Rounds 1–6 + future 7–10), plus 12-round ratifications from 2026-05-04. Authoring-heavy.
- **`research/06-tw-subgenres.md`** new stub — Squadron TD / Legion TD 2 / BTD6 / Element TD / Line Tower Wars / Mini-TD deep dives.

### Regression-watch (unchanged this session)

- Tutorial / match flow / merge-preview hover / Promote-T4 indicator / Aztec glyph (◈) / `logBalanceCurve` / `effectiveTowerStats` / snapshot.

---

## NEXT SESSION — primary directive

**Recommended track: continue Numbers-phase Follow-up #13 — Rounds 7–10.**

Round 7 is next: aux-slot costs (Tribute + Divinity) per universal slot family + (s) auxiliary multiplier ranges. Sized against ~14.3K Tribute headroom (Round 5 cascade) and 6-cap Divinity budget (locked frame; Fusion competes for same pool at 1 Divinity per).

Alternative tracks (PM choice):

1. **(Recommended)** Numbers-phase Follow-up #13 — Rounds 7–10.
2. CONCEPT.md amendment pass — roll Rounds 1–6 + 12-round 2026-05-04 ratifications into CONCEPT.md as §-new "Tower-vs-Unit math" + "Game modes" + "Auxiliary economy structure" sections.
3. Per-tower / per-commander authoring sub-pass (post-Round 10 normally, but could overlap R7-R10 since it consumes already-bound ladders).
4. Research pass — `research/06-tw-subgenres.md` deep-dive.
5. `admin/concept.json` migration — long-deferred staleness debt.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]**.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton.
- 17-item conceptual frame (with 2026-05-04 amendments) — **Accepted**. Rounds 1–6 magnitudes — **Accepted**. Revisions require superseding decisions.
- 6-mode ontology + auxiliary economy structure (2026-05-04 Rounds 6–12) — **Accepted**.
- "Go big, no scope cuts" project doctrine — **Accepted**.

---

## Cadence rules carried forward

- **Cadence exists to manage the context window, not to gate every step.** Concrete plan = execute end-to-end; gate via AskUserQuestion only on genuine ambiguity.
- **AskUserQuestion is the standard interface.** Always Recommended-first.
- **MD-first preservation** — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions. /clear must be safe at any prompt.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit. Commit at every ~3 rounds.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — Numbers-phase Follow-up #13, Rounds 1-6 of ~10
LANDED 2026-05-05. Bound magnitudes: HP curve + (k) exponents + Tribute
economy + speed + per-map + tower (c) DPS ladder + tier costs +
commander (h) damage-variant floor. Six decision documents filed; two
commits dual-pushed (b9a25a1 + 363047e). cascade-lint clean.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty after dual-push

STATE ALOUD (before producing anything):
- Phase status: Numbers-phase 6 of ~10 rounds complete; Rounds 7-10
  remaining (aux costs + (s) ranges / per-mode tuning / skill-bar
  thresholds / Divinity sources). Per-tower + per-commander authoring
  sub-passes deferred post-R10. CONCEPT.md amendment still pending.
  admin/concept.json staleness debt outstanding.
  research/06-tw-subgenres.md not yet written.
- Open blockers: none load-bearing.
- Specific next-step: surface AskUserQuestion with Recommended-first
  options for next track. Recommended = continue numbers-phase Round 7
  (aux-slot costs Tribute + Divinity per universal slot family + (s)
  multiplier ranges; sized against ~14.3K Tribute headroom + 6-cap
  Divinity budget).

CADENCE: AskUserQuestion is standard interface. Recommended-first.
MD-first on scope expansions. Execute end-to-end when plan concrete;
gate on genuine ambiguity. Commit + dual-push every ~3 rounds.

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
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract civ art.
- 17-item frame (with 2026-05-04 amendments) Accepted.
- Rounds 1-6 magnitudes Accepted.
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
- Any Round 1-6 bound magnitude would be silently re-tuned without a superseding decision entry.
- A scope expansion occurs and PM has not landed it in MD before further questions.
- Any recommendation invokes "lessen dev load" without explicit PM override of the "Go big" doctrine.
- A balance-pass numbers commit lands without a `decisions/<date>-balance-pass-N-round-M-*.md` entry capturing the ratified magnitudes.
