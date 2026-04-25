# HANDOFF — Session Checkpoint

**Last session:** 2026-05-02 — C6 slice 1 LANDED (commander-legacy sweep).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**C6 slice 1 LANDED — commander-legacy sweep, single commit, dual-pushed.** Two-stage PM gating: option 4 on initial C6 sequencing AskUserQuestion (full now / accept playability gap), then option 1 on follow-up scope-reality AskUserQuestion (land safely-deletable subset, queue rest as slice 2). Slice 2 (lineage/age teardown) deferred — coupled too deeply to running combat spine to be a clean delete; needs civ-tower placement (C4-continuation) interleave to redesign the surfaces, not just remove them.

**Deleted from `prototype/index.html`:** all 9 `// SUPERSEDED 2026-04-27 (C7.a)` comment-out blocks (covering the 12 commander-avatar surfaces from C7.a — KeyQ/KeyC handlers, net commander-move/-sig, initMatch struct + best-cell branch, onBoardClick Shift+click, towerStats aura indirection, three commander functions, startWave reset, tick-block, render-block); legacy `silhouetteSVG()` + `LINEAGE_COLORS` const; `getLineageCss()` helper; `cmdr-stat-tilt` + `cmdr-stat-generates` HTML elements + their `set()` calls.

**Deleted from `prototype/data/commanders.json`:** `commander-a` / `-b` / `-c` / `-d` / `-e` entries; `active` flipped to `leonidas`; `_comment` rewritten.

**Reshaped:** pick-card stat row (Lineage tilt → Civilization, Generates → Short CD; Signature now reads `c.stats.longCdSignature`); `commanderSilhouetteSVG/Color` simplified to civ-only path (drops `lineageTilt` fallback); placeholder commander-name in HUD (Commander A → Leonidas).

**Diff:** ~350 deletions / ~15 additions across two files. Single commit `1b4fd38`, dual-pushed to session branch + `main`. cascade-lint clean.

**Untouched (slice 2 deferred):** `prototype/data/ages.json` + `prototype/data/towers.json` files; `loadData()` boot fetches; `AGES_DATA` / `AGES` / `BALANCE.TOWERS` 5-lineage seeding; age-up + Knowledge resource + age-gate UI; tutorial Step 3 hybrid copy; 5-lineage tower buy/upgrade/sell + status-proc switch + `lineageOf()` + `lineageRole()` + HYBRIDS map + reference panel + projectile shape switch + Profile lineage greeting + cmdr-portrait/chip-dot/glyph CSS + `--sinew/--forge/--crown/--veil` color tokens + `cascade-lint` prototype-data schema checks. §2.4a + §5.4 [LOCKED] surfaces untouched. 2026-04-25 locked content-skeleton names untouched. **Prototype remains playable** on legacy 5-lineage tower wiring through slice 2.

---

## Commits this session

- `1b4fd38` — C6 slice 1 — commander-legacy sweep. Dual-pushed.
- This handoff commit — HANDOFF rewrite + PROGRESS trim.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `1b4fd38` (plus this handoff commit).
- Working tree clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures Greek/Aztec/Norse — 2026-04-25 Hard).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (decision 2026-04-27; prototype implementation across C7.a + C7.b).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28).
- **Prototype reshape plan: RATIFIED** (2026-04-29). Effective execution order: **C1 ✓ → C2 ✓ → C3 ✓ → C4 ✓ (slice; continuation deferred) → C5 ✓ → C7.a ✓ → C7.b ✓ → C6 slice 1 ✓ → C6 slice 2 (next)**.
- §2.4a + §5.4 **[LOCKED]** — both untouched this session.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries (C6 slice 1 / C7.b / C7.a). Prior C5 LANDED entry archived.
- `CASCADE.md` pointer: most recent block only (v0.33, C6 slice 1 LANDED); prior C5+C7.a+C7.b block archived.
- `CASCADE.md` version footer: 2 most recent bumps (v0.33 + v0.32 reference); v0.31 archived.
- Bootstrap remains lean.

### Open follow-ups (carried)

- **#4 — Aztec glyph styling pass.** civilizations.json has `𓁹` (Egyptian eye) for Aztec — wrong civilization. Fix in dedicated styling pass; do not surface in silhouettes/HUD until corrected.
- **#5 — Cultural-sensitivity pass.** Hard pose-lock gate on civ silhouettes. Content-lock-gate before any pose-locked / culturally-coded art ships.
- **#6 — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.**
- **#7-#9 — Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology.**
- **#11 — Norse round-30 boss CLOSED at Jörmungandr** (Fenrir post-launch).
- **#13 — [PROPOSAL] balance-pass re-ratification** for C1/C3 [PROPOSAL] numbers (RPS magnitudes, tier costs, Divinity cap, decorative CD durations, CAST_DURATIONS frame counts).
- **C4-continuation deferred items** — merge-preview ghosts / Promote-to-T4 button / tower-card tier+type stamp. Need civ-tower placement wiring; queued before or alongside C6 slice 2.
- **C6 slice 2 deferred items (NEW)** — full lineage/age teardown: `ages.json` + `towers.json` files; `loadData()` boot fetches + inline fallbacks; `AGES_DATA` / `AGES` / `BALANCE.TOWERS` 5-lineage seeding; age-up + Knowledge resource + age-gate UI; 5-lineage tower buy/upgrade/sell + status-proc switch + `lineageOf()` / `lineageRole()` + HYBRIDS map + reference panel + projectile shape switch + Profile lineage greeting + cmdr-portrait/chip-dot/glyph CSS + `--sinew/--forge/--crown/--veil` color tokens + `cascade-lint` prototype-data schema checks + tutorial Step 3 copy. **~200-300 lines coupled surgery; requires civ-tower placement (C4-continuation) interleave to not just delete but redesign running combat surfaces.**
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI surface. Queued for post-C6 polish.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape. PM direction owed: rewrite / regenerate / retire.

---

## NEXT SESSION — primary directive

**C6 slice 2 — lineage/age teardown, bundled with C4-continuation civ-tower placement.** PM "go" required before any work.

**Why bundled:** slice 2 alone removes the legacy 5-lineage tower wiring that currently drives playable matches. Without civ-tower placement shipping in the same step (or as a preceding step), the prototype goes non-playable. Surface to PM via AskUserQuestion before unilateral work.

**Recommended option (a) — bundled:** ship civ-tower placement (C4-continuation: merge-preview ghosts, Promote-to-T4 button, tower-card tier+type stamp + actual buy/place/attack wiring on civ towers) as the playable replacement for the 5-lineage system, then delete the legacy lineage/age surfaces in the same commit / same series of commits. Preserves playability through transition.

**Alternate (b):** stage in two passes — C4-continuation civ-tower placement first as its own PM-gated step (shipping playable civ towers alongside legacy, alongside-and-non-breaking pattern), then C6 slice 2 teardown after as the graduation cut.

**Alternate (c):** C6 slice 2 first, accept non-playable window, then C4-continuation to restore playability.

**Cadence:** propose plan via AskUserQuestion (Recommended first option) → PM "go" → produce → verify (`python tools/cascade-lint.py`) → tick. Single PM-gated step per HANDOFF protocol.

### Background candidates (if PM redirects)

1. **C6 slice 2 + C4-continuation bundled** (Recommended).
2. **C4-continuation only** — civ-tower placement first, defer slice 2.
3. Cultural-sensitivity pass scheduling (Follow-up #5).
4. Patch-1 commanders per civ (Follow-up #6).
5. `admin/concept.json` migration direction.
6. Other follow-ups #7 / #8 / #9 / #4 / #13.

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **[LOCKED]** — Lineages-row amendment LANDED 2026-04-28; no further row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- 2026-04-25 locked content skeleton (3 civs × 6 T1-T3 towers + 5 units + 6 T4 Demigods + 3 Gods + 9 Fusion recipes + commander signature-ability names + Tribute/Divinity economy + 30-round arc).

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **AskUserQuestion tool for PM gates** with "Recommended" first option (PM standing directive 2026-04-28).
- **Alongside-and-non-breaking pattern (PM-ratified 2026-04-29):** when a step would break running surfaces, add new code/files alongside legacy; surface cardinality conflicts to PM via AskUserQuestion before unilateral action. C6 is the explicit graduation point — slice 1 graduated commander-legacy surfaces; slice 2 graduates lineage/age surfaces (gated on civ-tower placement playability bridge).
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.
- **Context-pressure self-trim + scope re-gate:** when context budget tightens OR scope balloons mid-step beyond proposed delete, stop and re-gate via AskUserQuestion with slice options. Precedent: C4 slice + C7.b two-slice split + C6 two-slice split (this session).

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — primary directive C6 slice 2 (lineage/age teardown), bundled with C4-continuation civ-tower placement.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF: C6 slice 1
  (1b4fd38) dual-pushed. Commander-legacy sweep done:
  9 C7.a comment blocks + silhouetteSVG() + LINEAGE_COLORS
  + getLineageCss() + commander-a..e + cmdr-stat-tilt/generates
  all deleted; pick-card reshaped to civ-shape; active flipped
  to leonidas. Prototype remains playable on legacy 5-lineage
  tower wiring (slice 2 surfaces preserved). Handoff commit
  on top of slice 1.
- Open blockers: slice 2 alone breaks playability —
  removes legacy 5-lineage tower wiring that currently
  drives playable matches. Civ-tower placement
  (C4-continuation: merge-preview / Promote-T4 /
  tower-card stamp + buy/place/attack wiring) is the
  playable replacement and must ship in the same step
  or as a preceding step.
- Specific next-step proposal: surface plan via
  AskUserQuestion with Recommended first option —
  bundled C6 slice 2 + C4-continuation civ-tower
  placement, preserving playability through the cut.
  Alternate: stage in two passes (C4-continuation first
  alongside legacy, then C6 slice 2 graduation cut).
  Alternate: slice 2 first, accept non-playable window.

CADENCE: one-step-at-a-time with PM "go" gates.
USE AskUserQuestion for PM gates; always include a Recommended
first option per 2026-04-28 PM standing directive.
ALONGSIDE-AND-NON-BREAKING pattern (PM-ratified 2026-04-29):
slice 2 is the lineage/age graduation cut — gate on civ-tower
placement playability bridge.

EXECUTION ORDER on standby (one PM gate per step):
  C6 slice 2 + C4-continuation (bundled or staged).

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED] post-amendment; §2.4a [LOCKED]; 2026-04-25
  locked content skeleton untouched.
- Aztec glyph "𓁹" in civilizations.json is wrong (Egyptian
  eye) — Follow-up #4; do not surface until corrected.
- Slice 2 surfaces (BALANCE.TOWERS spine, status-proc,
  HYBRIDS, lineageOf/lineageRole, reference panel, tutorial
  Step 3, projectile renderers, HUD, options, mapmods events,
  snapshot fields, lint schemas, --sinew/--forge/--crown/--veil
  tokens, cmdr-portrait/chip-dot/glyph CSS) are coupled —
  touch only under bundled civ-tower placement plan.

If PM redirects off slice 2, fall back: C4-continuation only,
cultural-sensitivity pass scheduling (Follow-up #5),
patch-1 commanders per civ (Follow-up #6),
admin/concept.json migration direction, follow-ups #7/#8/#9/#13.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5) — hard pose-lock gate on any non-abstract civ art.
- A reshape step would silently break a running surface without an alongside fallback or AskUserQuestion gate.
- Scope balloons mid-step beyond the proposed delete — re-gate via AskUserQuestion with slice options before continuing.
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
