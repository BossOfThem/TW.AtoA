# HANDOFF — Session Checkpoint

**Last session:** 2026-05-04 — C4-continuation polish LANDED + Follow-up #4 closed (Aztec glyph).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**First post-graduation session after C6 slice 2 closed the reshape arc.** Two tracks ran end-to-end per cadence directive (no per-step gates when plan is concrete):

**Track 1 — C4-continuation polish (commit `c45cb00`, dual-pushed, +64 lines `prototype/index.html`):**
- **Action-bar tower-button attack-type stamp.** Build-set buttons now render an attack-type pill (`Piercing`/`Slashing`/`Crushing`/`Fire`/`Poison`/`Arcane`/`Divine`) sourced from `attackTypeFor(key)`, alongside the existing tier-badge + cost. CSS rule `.action-bar .tower-btn .atk-stamp` added.
- **Merge-preview ghost on hover-existing-tower.** New helper `hoverHasSameTierCivPartner(t)` excludes self and checks for same-civ same-tier neighbors within `CIV_MERGE_RADIUS`. Render loop checks `isHovered` on each tower; if civ-tower T1/T2 with a partner, draws the dashed-hex ghost outline of `mergeTargetKeyForCiv(civ, tier)` plus `→ <target.label>` text. Mirrors the existing placement-preview ghost logic + reduce-motion branch.
- **Promote-T4 inline indicator.** T3 civ towers with valid `promoteTargetKey(t)` draw a small `↑` badge top-right of the hex. Gold + pulsing when `gold ≥ CIV_PROMOTE_T4_COST`, dim slate when not. Reduce-motion → static. Right-click context-menu Promote path + `promoteTowerToT4()` untouched; this is a discoverability layer only.

**Track 2 — Follow-up #4 closed (commit `2e56cf5`, dual-pushed):**
- `prototype/data/civilizations.json` Aztec glyph swapped from `𓁹` (Egyptian Hieroglyph D4 / Eye of Horus, U+13099 — wrong civilization) to `◈` (White Diamond Containing Black Small Diamond, U+25C8 — culturally-neutral abstract).
- Decision filed [`decisions/2026-05-04-aztec-glyph-abstract-placeholder.md`](decisions/2026-05-04-aztec-glyph-abstract-placeholder.md) (Accepted, Reversibility Easy, three alternatives analyzed inline).
- Cultural-sensitivity gate Follow-up #5 explicitly preserved: no culturally-coded replacement bypass; abstract is the highest-priority defensible interim. Greek `Ω` and Norse `ᚱ` glyphs untouched (pre-gate, in-tree at 2026-04-25 ratification). Asymmetry intentional — surfaces open #5 work rather than masking it.
- CASCADE.md decisions table row added.

cascade-lint clean throughout. §2.4a + §5.4 [LOCKED] untouched. 2026-04-25 locked content-skeleton names untouched.

---

## Commits this session

- `c45cb00` — C4-continuation polish: merge-preview hover + Promote-T4 indicator + tower-card attack-type stamp. Dual-pushed.
- `2e56cf5` — Follow-up #4 closed: Aztec glyph 𓁹 → ◈ abstract placeholder + decision entry + CASCADE table row. Dual-pushed.
- This handoff commit — HANDOFF rewrite + PROGRESS trim + CASCADE pointer/version bump.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `2e56cf5` (plus this handoff commit).
- Working tree clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (decision 2026-04-27; prototype implementation across C7.a + C7.b).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28).
- **Prototype reshape plan: COMPLETE.** Effective execution order: **C1 ✓ → C2 ✓ → C3 ✓ → C4 (slice + continuation across slices) ✓ → C5 ✓ → C7.a ✓ → C7.b ✓ → C6 slice 1 ✓ → C6 slice 2 (Bridge + Polish + Graduation) ✓ → C4-continuation polish ✓**. Reshape arc closed; deferred polish track also closed.
- **Follow-up #4 (Aztec glyph): CLOSED** with abstract-placeholder decision (2026-05-04). Cultural-sensitivity gate Follow-up #5 still owns the eventual culturally-coded re-evaluation.
- §2.4a + §5.4 **[LOCKED]** — both untouched this session.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries (2026-05-04 / 2026-05-03 / 2026-05-02). 2026-05-01 (C7.b) entry archived this handoff.
- `CASCADE.md` pointer: most recent block only (v0.35, 2026-05-04 polish + Follow-up #4); prior C6-slice-2 block archived.
- `CASCADE.md` version footer: 2 most recent bumps (v0.35 + v0.34 reference); v0.33 archived.
- Bootstrap remains lean.

### Open follow-ups (carried)

- **#5 — Cultural-sensitivity pass.** Hard pose-lock + content-lock gate before any culturally-coded civ art ships. Now also gates the Aztec glyph re-evaluation (post-#4 abstract interim) and a proper Greek `Ω` / Norse `ᚱ` audit alongside.
- **#6 — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.**
- **#7-#9 — Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology.**
- **#11 — Norse round-30 boss CLOSED at Jörmungandr** (Fenrir post-launch).
- **#13 — [PROPOSAL] balance-pass re-ratification** for C1/C3 [PROPOSAL] numbers (RPS magnitudes, tier costs, Divinity cap, decorative CD durations, CAST_DURATIONS frame counts). **Critical post-graduation:** `effectiveTowerStats` collapsed to scalar `damage` / `cd` (level-only multipliers); the new flat curve has not yet been validated. Load-bearing for any further combat-balance work.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI surface. Queued for post-reshape polish.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape. PM direction owed: rewrite / regenerate / retire.

### Regression-watch (still live from 2026-05-03 graduation cut)

The C6 slice 2 graduation cut was a large surgical pass; the C4-continuation polish layered on top of it. Sanity-checks worth a manual run before any new code:
- **Tutorial flow** — `TUT_TOWER_KEY = "greek_phalanx"` pin; tutorial steps 1→5 advance correctly; `selectTower` lock keeps non-phalanx unselectable until step 5. Action-bar single-button now shows attack-type stamp `Piercing`.
- **Match flow** — `initMatch` no longer pre-selects a tower; verify build-set renders + tower placement still works for all 3 civs. Each tower button shows correct attack-type stamp.
- **Merge-preview hover** — place two T1 phalanx within ~80px (default `CIV_MERGE_RADIUS`); hovering either should show the ghost outline + `→ Acropolis` (or matching T2) text. Reduce-motion: ghost still shows, no pulse-text.
- **Promote-T4 indicator** — promote a tower to T3 (or place adjacent same-civ T2 + merge); the resulting T3 should show a `↑` badge top-right. Affordable → gold + pulse; unaffordable → dim slate; reduce-motion → static.
- **Aztec civ glyph** — Aztec commander/tower paths render `◈` instead of `𓁹` in HUD, silhouettes (where glyph is read), reference panel.
- **`logBalanceCurve`** — rebuilt to `80 - cheapest * 2`; verify console.table output is sane on first wave run.
- **`effectiveTowerStats`** — reads `stat.damage` / `stat.cd` as scalars. All upgrade math should still resolve.
- **Snapshot / co-op** — `enemies[].ageIdx` field dropped from snapshot. Guests fall back to `archetypeFor(0)` for missing kind/color/accent.

---

## NEXT SESSION — primary directive

**No single load-bearing directive.** Reshape arc + deferred polish track both closed; Follow-up #4 closed. Several independent tracks remain:

**Recommended option (a) — Follow-up #13 balance-pass re-ratification.** Now the most load-bearing remaining item: post-graduation, `effectiveTowerStats` collapsed age-indexed arrays to scalars, so the flat curve is currently untuned. The pass is *PM-ratifies, Claude lands*: I propose a number set across `balance.json` + `CIV_TOWER_TIER_BASE` + decorative CD durations + `CAST_DURATIONS`, PM ratifies, then I edit + cascade-lint + dual-push. AskUserQuestion gate at proposal time (genuine ambiguity on numbers PM has not pre-specified).

**Alternate (b) — admin/concept.json migration direction.** Long-deferred; PM picks: full rewrite to 3-civ/4-tier/Fusion shape, regenerate from CONCEPT.md by extending admin/ tooling, or retire entirely in favor of `concept/phase-*.md` as sole source of truth. Direction-only this turn; execution follows in a subsequent slice depending on PM choice.

**Alternate (c) — Follow-up #5 cultural-sensitivity pass scheduling.** Now elevated by the Follow-up #4 closure: the `◈` abstract placeholder explicitly defers culturally-coded glyph work to this gate. PM defines: when does the gate run, who approves content under it, what is the audit scope (silhouettes / glyphs / commander signatures / tower names in flavor text)? Scheduling-only; no art lands this turn.

**Alternate (d) — Follow-up #6 patch-1 commanders + Thor recipe-layer dissonance.** Larger design pass. Needs scoping before execution.

**Alternate (e) — C7.b deferred items.** Builder concurrency cap + 90% refund-on-cancel UI. Self-contained; small slice.

**Cadence:** if PM picks a track and the plan is concrete, execute end-to-end (verify + commit + dual-push) without intermediate gates. AskUserQuestion only on genuine ambiguity (cardinality breaks, [LOCKED] conflicts, cultural-sensitivity, mid-step scope blow-ups, number-set proposals where PM has not pre-specified).

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]** — Lineages-row amendment LANDED 2026-04-28; no further row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton (3 civs × 6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods + 9 Fusion recipes + commander signature-ability names + Tribute/Divinity economy + 30-round arc).

---

## Cadence rules carried forward

**Cadence exists to manage the context window, not to gate every step on PM input.** PM feedback 2026-05-03: per-step "propose → go → produce" rituals overclock the context window when the plan is already concrete. Default to autonomous execution; reserve PM gates for genuine ambiguity. **2026-05-04 confirmation:** PM said "go" with no track named after C4-continuation closed; I AskUserQuestion'd to pick the next track (genuine ambiguity), then executed Follow-up #4 end-to-end. Pattern works.

- **When a plan is concrete (HANDOFF directive picked, ratified decision, queued PROGRESS step, scope already discussed):** execute end-to-end without intermediate gates. Batch independent edits in parallel. Verify with `python tools/cascade-lint.py`, commit, dual-push, summarize once at the end.
- **When to gate via AskUserQuestion:** cardinality breaks, [LOCKED] surface conflicts, cultural-sensitivity gates (Follow-up #5), mid-step scope blow-ups beyond the original plan, ambiguity that affects which file or shape to produce, **number-set proposals (e.g., balance pass) where PM has not pre-specified values**. Always include a "Recommended" first option (PM standing directive 2026-04-28).
- **Context-pressure self-trim:** when context budget tightens, batch tool calls, group parallel-safe edits, and re-gate only if context will not survive completion.
- **Alongside-and-non-breaking pattern (PM-ratified 2026-04-29):** dormant — reshape arc closed. Re-activate for any future reshape of comparable scope.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — first post-graduation session closed cleanly:
C4-continuation polish LANDED (commit c45cb00) + Follow-up #4 closed
(commit 2e56cf5, Aztec glyph 𓁹 → ◈ abstract). Reshape arc + its
deferred polish + the wrong-civ glyph follow-up are all done.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF: 2e56cf5 dual-pushed.
  Action-bar tower buttons show attack-type stamps; T1/T2 hover
  shows merge-preview ghost; T3 towers show ↑ Promote indicator
  (gold-pulse when affordable). Aztec glyph is ◈ (abstract); Greek
  Ω / Norse ᚱ untouched. Right-click Promote menu + promoteTowerToT4
  path untouched; new indicator is discoverability only.
- Open blockers: none load-bearing. Tracks open:
  Follow-up #13 balance-pass (CRITICAL — flat curve untuned post-
  graduation; PM ratifies numbers, Claude lands), admin/concept.json
  migration direction, Follow-up #5 cultural-sensitivity pass
  scheduling (now also gates Aztec glyph re-evaluation post-#4),
  Follow-up #6 commanders+Thor, C7.b deferred items (Builder cap +
  refund UI).
- Specific next-step proposal: Recommended = Follow-up #13 balance-
  pass. Surface via AskUserQuestion with options. Alternate = admin/
  concept.json direction. Alternate = Follow-up #5 scheduling.
  Alternate = Follow-up #6 commanders+Thor. Alternate = C7.b deferred.

CADENCE (2026-05-03 PM directive, 2026-05-04 confirmed): cadence is
for managing the context window, NOT gating every step. When the plan
is concrete (HANDOFF directive, ratified decision, queued PROGRESS
step), execute end-to-end without intermediate "go" gates — batch
parallel-safe edits, verify with cascade-lint, commit, dual-push,
summarize once at the end. AskUserQuestion is reserved for genuine
ambiguity (cardinality breaks, [LOCKED] conflicts, cultural-sensitivity
gates, mid-step scope blow-ups, NUMBER-SET PROPOSALS where PM has not
pre-specified values — Follow-up #13 falls here). Always include
"Recommended" first option when you do gate.

REGRESSION-WATCH (carries from 2026-05-03 + 2026-05-04 polish):
- Tutorial: TUT_TOWER_KEY = "greek_phalanx" pin; steps 1→5 advance.
  Action-bar single-button shows "Piercing" stamp.
- Match: initMatch no longer pre-selects tower; build-set renders
  + each button shows correct attack-type stamp + tower placement
  works for all 3 civs.
- Merge-preview hover: place 2 T1 of same kind within ~80px;
  hovering either shows ghost outline + → target label. Reduce-
  motion: ghost only, no text.
- Promote-T4 indicator: T3 towers show ↑ badge top-right.
  Affordable → gold + pulse; unaffordable → dim slate; reduce-
  motion → static. Right-click Promote still works.
- Aztec glyph: ◈ in HUD/silhouettes/reference panel (NOT 𓁹).
- logBalanceCurve, effectiveTowerStats, snapshot — see prior
  HANDOFF regression-watch (still live).

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED] post-amendment; §2.4a [LOCKED]; 2026-04-25
  locked content skeleton untouched.
- Cultural-sensitivity Follow-up #5 still hard-gates any non-
  abstract civ art. The 2026-05-04 ◈ swap is the abstract-
  placeholder pattern; do NOT replace ◈ with a culturally-coded
  Aztec glyph without #5 ratification.
- Reshape arc is closed. Do not regress legacy lineage/age
  surfaces back into the prototype.

If PM redirects off these tracks, fall back to: follow-ups #7/#8/#9
(Foresight-coin / PvE campaign + AGES + leveling + attributes / non-
boss enemy ontology).
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5) — hard pose-lock + content-lock gate on any non-abstract civ art. The 2026-05-04 `◈` swap is the abstract pattern; replacing it with culturally-coded Aztec content requires #5 ratification.
- A reshape step would silently break a running surface without an alongside fallback or AskUserQuestion gate.
- Scope balloons mid-step beyond the proposed delete — re-gate via AskUserQuestion with slice options before continuing.
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
- Any attempt to regress the retired lineage/age surfaces (sinew/ember/forge/crown/veil; AGES; ageIdx; HYBRIDS; age-banner) back into the prototype.
- A balance-pass commit lands without a corresponding `decisions/<date>-balance-pass-N.md` entry capturing the [PROPOSAL] → ratified-numbers diff.
