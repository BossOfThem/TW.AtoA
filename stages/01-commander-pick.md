# Stage 01 — Commander Pick

**Status:** Draft
**Phase in CONCEPT cascade:** 3 (Design) / 4 (Specification — per-commander spec)
**Upstream deps:** [Stage 00 — session start](00-session-start.md), [CONCEPT §3.2 Commander system](../CONCEPT.md), [CONCEPT §3.3 Lineages](../CONCEPT.md), [CONCEPT §4.1 Commander mechanical spec](../CONCEPT.md), [CONCEPT §5.1 MVP scope](../CONCEPT.md), [CONCEPT §6.4 Validation](../CONCEPT.md), [research/03 — commander archetypes](../research/03-commander-archetypes.md), [decisions/2026-04-20-commander-identity-floor.md](../decisions/2026-04-20-commander-identity-floor.md), [decisions/2026-04-20-first-run-flow.md](../decisions/2026-04-20-first-run-flow.md), [CLAUDE.md "Commander = user"](../CLAUDE.md)
**Downstream impact:** [Stage 02 — mode select](02-mode-select.md), [Stage 08 — meta progression](08-meta-progression.md), and every stage that surfaces commander identity.
**Last reviewed:** 2026-04-20

---

## 1. Scope

The identity moment. You — the Commander — choose the face, voice, silhouette, and lineage tilt that will carry across every subsequent match in Ash to Altar. First-time players arrive here immediately after Stage 00 (splash → main menu → New Game). Returning players reach here via the Commander surface on the main menu when they want to change. Either way, the pick is *persistent identity*, not a per-match loadout choice — the Commander is you, and the Commander you pick is the one the game addresses as "you" for every downstream stage until you deliberately change it.

Stage 01 covers:

- Gallery UX: how the starter roster is presented on first sight.
- Per-commander card: what you see at a glance vs. after click-to-expand.
- Roster size: how many commanders are in the gallery at launch.
- Archetype coverage: how roster slots map to lineages and how the no-over-represented-tropes guardrail is enforced.
- First-pick flow: the click path from Stage 00 handoff through confirmation and into Stage 02.
- Change-commander policy: how re-picks work from the main-menu Commander surface.
- Voice-sample UX, card layout, accessibility floor, tilt-not-cage copy discipline.

Stage 01 does **not** cover: the lineage system itself (CONCEPT §3.3), the kit economy that lineages gate (CONCEPT §4.3), or meta progression after level 1 (Stage 08). It *points to* all three and hands you off cleanly.

## 2. Upstream constraints

Every commitment in this stage inherits from one of the following. Stage 01 does not amend any of them.

- [CONCEPT §3.2 Commander system](../CONCEPT.md). Names the identity components — portrait, silhouette, color, voice, lineage tilt, passive, signature, progression. Stage 01 surfaces all of them in the gallery and per-commander card; it does not invent new components or drop any.
- [CONCEPT §3.3 Lineages](../CONCEPT.md). The five lineages — Sinew, Ember, Forge, Crown, Veil — are the tilt targets. Stage 01 shows each commander's lineage affinity; the tilt number comes from §4.1.
- [CONCEPT §4.1 Commander mechanical spec](../CONCEPT.md) + [decisions/2026-04-20-commander-identity-floor.md](../decisions/2026-04-20-commander-identity-floor.md). Identity floor **[PROPOSAL]**: 1 default portrait + 1 unlockable variant, 1 default silhouette + 1 unlockable variant, 12 voice lines (3 pick / 3 victory / 3 defeat / 3 ability-cast), 1 signature ability, 1 passive, +15% lineage tilt, 20-level progression ladder, 3 cosmetic slot types (commander skin, portrait frame, map tint). Stage 01 treats these as the per-commander spec target; the gallery and card must surface every one of them. Numbers are inherited as [PROPOSAL]; Stage 01 does not lock.
- [CONCEPT §5.1 MVP scope](../CONCEPT.md). At the playable-slice MVP, the gallery contains exactly **2 commanders** (one Sinew-leaning, one Ember-leaning) representing 2 lineages. Stage 01's gallery UX must scale from 2 (MVP) to 5–8 (post-MVP) without a re-layout.
- [CONCEPT §6.4 Validation](../CONCEPT.md). Commander re-pick rate on match 2 is the measured identity-stickiness signal. Stage 01's change-commander policy must *enable* this metric (free, reversible change from the main menu surface) without *pushing* toward re-pick (no nag UI, no "try another?" prompt).
- [decisions/2026-04-20-first-run-flow.md](../decisions/2026-04-20-first-run-flow.md). Stage 01 is the identity moment immediately after the Stage 00 "New Game" click. Click-budget [PROPOSAL] ≤6 clicks launch-to-match means Stage 01 consumes at most 2 clicks of that budget (browse + confirm), ideally one if card-browse counts as browsing-not-clicking.
- [research/03-commander-archetypes.md](../research/03-commander-archetypes.md). JUST LANDED (Draft, 2026-04-20). Stage 01 inherits the 5-slot [PROPOSAL] roster (§5 of research/03) without locking it, the "NOT shipping" list (§3 / §Deliverables), and the durable-pick synthesis (older, burdened, silhouette-distinct).
- [CONCEPT §3.10 Audio architecture](../CONCEPT.md). Voice bus sidechain-ducks Music and SFX during voice-line playback. Stage 01's voice-sample UX routes through the Voice bus so that sampling a commander in the gallery ducks menu music correctly.
- [CONCEPT §5.4 Naming conventions](../CONCEPT.md). All commander names in this stage are placeholder; nothing is locked. Fantasy labels (warmother, scholar-exile, foundry-master, paladin-king / saint-matron, trickster-courier) are descriptive, not final.

## 3. Gallery UX

The gallery is the first screen after you click **New Game** on the main menu. It is the moment you see "the roster" — the full starter cast — and decide who you are.

### 3.1 What the gallery surfaces

Every commander in the gallery shows, at minimum:

- **Portrait** (the default variant, per identity floor).
- **Silhouette chip** — a small, silhouette-forward art-direction preview of how the commander will read at battle-map zoom. Silhouette is load-bearing for unit recognition in match (CONCEPT §3.2, §4.1) and is surfaced here so that you are *choosing a silhouette*, not only a portrait.
- **Lineage color accent** — the lineage affinity is expressed as a ring, border, or color wash using the lineage's palette (Sinew / Ember / Forge / Crown / Veil). Color is *one* of several affinity cues, never the only one (accessibility; see §11).
- **Placeholder name + epithet** — e.g., "[PROPOSAL] Veteran-of-Something, the Warmother." Name is descriptive until the naming pass; epithet carries the fantasy.
- **One-line passive summary** — ≤8 words. Example: "Nearby walls gain small regeneration." Mechanical, plain-spoken. The full passive text lives on the expanded card.
- **Signature ability name + one-line effect** — same treatment. Fantasy + mechanics in one readable unit.
- **Voice-sample affordance** — a small speaker icon; click to play a 2–3s clip. (See §9 for UX detail.)
- **Lineage-tilt indicator** — a small chevron or pip showing "+15% [PROPOSAL]" against the affinity lineage, plus the text cue "tilted" (never "class" or "locked to"; see §12).

### 3.2 Layout options

Three candidate layouts are on the table. Leading choice is tagged; alternatives are documented in §14.

- **Grid (leading).** A 2×3 or 3×2 grid of cards at the 5-slot roster size, easily extensible to a 3×3 at 8. All commanders visible without scrolling at 1080p and above. Fastest overview, fastest compare, strongest for first-pick cognitive-load (research/03 §6).
- **Carousel.** One card at a time, swipe/arrow to advance. Better on ultrawide and on controller; worse for compare-at-a-glance. Alternate for controller-input builds.
- **List with large preview pane.** Left-column list of commanders, right-column expanded detail for the hovered/selected commander. Good for 8+ rosters where grid becomes busy; overkill at 5.

At the MVP's 2-commander roster (CONCEPT §5.1), all three layouts degenerate to "two cards side by side" — the layout decision only starts to bite at 5+, which is why Stage 01 keeps grid as the leading option without locking.

### 3.3 Roster-wide context copy

One line at the top of the gallery: "Choose your Commander. You can change later." This is load-bearing copy; it defuses the "am I locking myself in" anxiety that the research/03 durable-pick evidence shows drives new-player hesitation on rosters they don't know.

## 4. Per-commander card — at a glance vs. expanded

Clicking a gallery tile expands that commander into a full card. The card is the moment the identity floor (§4.1 floor) becomes concrete to you.

### 4.1 At-a-glance (the gallery tile itself)

Per §3.1 above. Intentionally compressed — you should be able to compare five tiles without reading paragraphs. If a tile makes you read to understand *what the commander is*, the tile has failed.

### 4.2 Expanded card — full identity floor surfacing

On expansion, the card shows:

- **Portrait** at full size, with a small "1 / 2" indicator showing the unlockable-variant slot (default visible, variant silhouetted with a lock icon and "Unlock at level N"). Inherits from the identity-floor 1 default + 1 unlockable variant [PROPOSAL].
- **Silhouette preview** at battle-map zoom — a simulated in-match render so that you can read-test the silhouette yourself before committing.
- **Lineage affinity block** — the lineage name and the tilt number: "Tilted toward [lineage] — +15% [PROPOSAL]." The word "tilted" is deliberate; see §12.
- **Passive** — full text. Small, persistent, not match-winning (per §4.1 floor). 1–2 sentences.
- **Signature ability** — full text. Deployable as Hero Unit (per CONCEPT §3.2 / §3.4). 2–3 sentences.
- **Voice-sample bank** — a compact row of the 4 voice-line *categories* (pick / victory / defeat / ability), each with a click-to-play affordance. You do not need to hear all 12 lines; you need a taste of tonal register. (See §9.)
- **Backstory preview** — one short paragraph (~50–70 words). Fantasy-first framing. Deliberately shorter than a codex entry; the gallery is not the place for lore dumps.
- **Progression ladder teaser** — a horizontal 1–20 strip showing milestone unlocks (portrait variant, silhouette variant, voice-line additions if any, cosmetic slot items). Current-player-state is "locked, level 1" for every commander until pick. The teaser exists so that you see *the shape of the ladder you are opting into* (per identity-floor [PROPOSAL] 20-level ladder).
- **Cosmetic slot preview** — 3 chips (commander skin, portrait frame, map tint), each showing the default item and (locked) the unlockable variant per slot.

### 4.3 What the card does NOT show

- Full lore / codex — deferred to an in-match or main-menu codex surface.
- Kit breakdown by unit tier — belongs to the lineage screen, not the commander.
- Balance stats / DPS charts — Stage 01 is identity, not optimization. Mechanics-first players will want this; it is a post-pick affordance, not a pre-pick one. (See §10 for card-layout tradeoff.)

## 5. Roster size [PROPOSAL]

Research/03 §6 proposes **5 at launch, one per lineage, grown to 8–10 over the first two content seasons**. Stage 01 inherits this proposal without locking. The decision belongs to a future `decisions/` entry, not to this stage doc.

Brief tradeoff summary (full argument in research/03 §6):

| Size | Pros | Cons |
|------|------|------|
| 3 | Trivially readable; minimum content budget; safe start. | Three lineages are un-headed or share a commander; no "your lineage has a face" at launch; reads as thin. |
| 5 (leading [PROPOSAL]) | One per lineage; identity cleanly maps to §3.3's five; all research/03 §4 representation axes seedable at launch; grid layout works. | Forces one commander per lineage in playtest — no balance-through-quantity if one is weak. |
| 8 | Room for two commanders per lineage in the most popular ones + one absurd-earnest + one alt-archetype; closer to OW-launch or WR-launch benchmark. | Content-budget stretch for a two-dev team (CONCEPT §2.2); pressures Stage 08 meta progression authoring; risks under-shipping each. Structurally one-way (removing commanders post-launch is high-cost — research/03 §6 reversibility note). |

MVP (CONCEPT §5.1) ships **2 commanders** in the gallery regardless. 3 / 5 / 8 is the post-MVP first-public-release question.

**Stage 01 does not lock this.** A future `decisions/<date>-roster-size.md` entry owns the ratification.

## 6. Archetype coverage

Research/03 §3 defines a "NOT shipping" list (gritty male soldier, anime swordmaiden, chosen-one orphan, scruffy scoundrel, edgy cloaked assassin, sexy elf ranger, teenage prodigy mage-girl, generic dwarven drunk). Stage 01 treats this list as a **gallery guardrail**: if any card in the gallery reads, at silhouette-and-epithet level, as one of these tropes, the character brief has drifted and the gallery tile itself is a failure condition.

The complementary guardrail is research/03 §4's under-represented-with-appetite list: at least one commander 50+, at least one explicitly queer, at least one non-human-but-dignified, at least one absurd-earnest. At the 5-slot [PROPOSAL] roster from research/03 §5, all four are seeded simultaneously — which is why 5 is the leading choice rather than 3.

### 6.1 Lineage-tilt alignment

The 5-slot [PROPOSAL] from research/03 §5:

| Slot | Lineage | Fantasy label (placeholder) |
|------|---------|------------------------------|
| 1 | Sinew | [PROPOSAL] Warmother — former siege-captain |
| 2 | Ember | [PROPOSAL] Scholar-exile — burdened academic |
| 3 | Forge | [PROPOSAL] Foundry-master — queer, non-human, pragmatic |
| 4 | Crown | [PROPOSAL] Paladin-king OR saint-matron (pick one) |
| 5 | Veil | [PROPOSAL] Trickster-courier — queer, non-lethal toolkit |

Stage 01 surfaces whichever subset actually ships. At MVP (2 commanders), Sinew slot 1 + Ember slot 2 are the leading candidates per research/03's anchor recommendations. No names locked.

## 7. First-pick flow

Inbound handoff from [Stage 00](00-session-start.md): you have clicked **New Game** on the first-time-variant main menu. Stage 01 begins.

1. **Gallery open.** The roster gallery (§3) renders. Context copy at top: "Choose your Commander. You can change later." No timer, no forced scroll, no splash interstitial.
2. **Browse.** You hover / tap tiles. Voice-sample affordances are available but not auto-triggered (§9). Lineage affinity colors are visible; silhouette chips are visible. Time on this screen is *yours*.
3. **Expand.** You click a tile. The tile expands to the full per-commander card (§4.2). Other tiles dim but remain clickable — you can bounce between expanded cards without a back-click.
4. **Select.** You click **Choose [PROPOSAL name]** on an expanded card. A confirmation modal overlays: portrait + epithet + "You will play as [name]. You can change later from the main menu." Two buttons: **Confirm** / **Back to gallery**.
5. **Confirm.** You click Confirm. A short (≤1.5s) "pick" animation — the commander's voice-line category "pick" fires through the Voice bus (§9, CONCEPT §3.10); lineage color accent sweeps; then Stage 01 hands off.
6. **Hand-off to [Stage 02 — mode select](02-mode-select.md).** Per [decisions/2026-04-20-first-run-flow.md](../decisions/2026-04-20-first-run-flow.md), a first-run player next sees the tutorial-skip prompt on the way into mode select.

**Click count for first-pick:** 1 (expand) + 1 (Choose) + 1 (Confirm) = 3 clicks inside Stage 01. Compatible with the ≤6-click launch-to-match [PROPOSAL] budget from the first-run-flow decision.

**Skippability:** Stage 01 is **not** skippable on first run. You cannot enter a match without a Commander (CONCEPT §3.2 treats Commander as persistent identity; there is no "no-commander" mode at launch — this is flagged as a cross-dependency in research/03 §6 caveat 4 and is an open question for a future entry). Alternatives are considered in §14.

## 8. Change-commander policy

From the returning-player main menu (per [decisions/2026-04-20-first-run-flow.md](../decisions/2026-04-20-first-run-flow.md)), a **Commander Select** affordance routes you back into Stage 01's gallery. This is the same gallery as first-run, with three additions:

1. **Your current Commander is marked** — a "Current" badge on the tile.
2. **Progression state is visible per commander** — the level strip on each expanded card now shows *your* progress, not a zeroed-out placeholder.
3. **Cosmetics you have unlocked appear in the slot preview** — unlocked variants are no longer locked-icon'd on the cards you have played.

### 8.1 Progression: per-commander ladder (leading)

Per identity-floor [PROPOSAL] 20-level ladder (§4.1 floor), progression is **per-commander**, not account-wide. When you change commanders, your previous commander's ladder does not reset and your new commander's ladder starts wherever you had previously taken it (at level 1 if new).

The leading direction is per-commander because:
- Stage 08 meta progression hangs unlock cadence off per-commander XP (portrait variants, silhouette variants, cosmetic slot items per identity floor).
- Per-commander ladders make *each* Commander feel like a commitment, not a skin-swap — which is the "Commander = user" promise the identity floor funds.
- Research/03 §6.4 ("commander re-pick rate on match 2" as key retention signal, promoted in the identity-floor decision) is noise-polluted if progression is account-wide: re-pick becomes free, and the signal collapses.

**This is leading, not locked.** A shared-XP alternative is tractable (see §14) and a future `decisions/` entry owns the ratification.

### 8.2 Cosmetics: shared (leading)

Cosmetic *currencies* and purchased store items that are not commander-specific (generic portrait frames, map tints if they are generic) are **account-wide / shared**, not per-commander. Commander-specific cosmetics (the per-commander skin, the variant portrait, the commander-themed map tint) are per-commander by definition.

This is leading because the alternative — per-commander cosmetics for everything — forces you to re-buy frames every time you change commander, which reads as punitive and drives retention the wrong direction.

### 8.3 Change cost: free outside match (leading)

Changing Commander is **free** while you are on the main menu / outside a match. Once a match has started, the Commander is locked for that match — you cannot swap mid-match.

Free-outside-match is leading because:
- A cost gate punishes the exact behavior (re-pick on match 2) that CONCEPT §6.4 uses as the identity-stickiness signal. A gated re-pick produces a *reluctance* artifact in the metric that does not correspond to stickiness.
- Cost gates on identity changes read as pay-to-feel-like-yourself, which is adjacent to the pay-to-win non-negotiable from the CLAUDE.md "not" list.

Mid-match lock is not negotiable at MVP — every match loop assumes a stable Commander for passive / signature / tilt accounting.

### 8.4 Metric hook

CONCEPT §6.4 uses commander re-pick rate on match 2 as the measured identity-stickiness signal. Stage 01's change-commander policy is designed to **enable** that metric cleanly (free change, reversible, visible from main menu) without **pushing** toward it (no nag UI suggesting you try a different commander; no "Hey, have you tried X?" prompt). The metric should reflect your revealed preference, not the UI's.

## 9. Voice-sample UX

Voice samples surface in two places: the gallery tile (speaker icon, plays one pick-category line) and the expanded card (four category affordances — pick / victory / defeat / ability).

**Leading: click-to-play, not hover-auto.** Rationale:

- **Accessibility.** Hover-auto creates unexpected audio events for users with motion-triggered exploration patterns, screen-reader users whose focus cursor is hover-equivalent, and users on touch devices where hover is not meaningful. Click-to-play is explicit intent.
- **Audio-bus behavior** (CONCEPT §3.10). The Voice bus sidechain-ducks Music and SFX on every voice-line play. Hover-auto would trigger duck-and-release cycles constantly as you browsed tiles — which reads as broken audio, not characterful. Click-to-play fires the duck intentionally at a moment you are already mentally attending to that commander.
- **Consent.** You chose to hear this commander speak. That small consent is load-bearing for the identity framing.

**Subtitles on every sample** — per §11. Subtitles render above/beside the sample affordance during playback.

**Alternate considered:** hover-auto with a user-flippable "auto-preview on hover" preference in Options. Documented in §14.

## 10. Mechanics-first vs. fantasy-first card layout

Two card-layout philosophies compete for the top-of-card real estate on the expanded card (§4.2).

### 10.1 Fantasy-first (leading)

Top of card: portrait + epithet + backstory preview. Middle of card: passive + signature (mechanics, but written plain-spoken, fantasy-consistent). Bottom of card: lineage tilt number, progression teaser, advanced stats (collapsed by default, "Show details" expander).

Rationale:
- Matches the identity framing — you are choosing who you are, then reading what they do.
- Research/03 §1 durable-pick evidence skews toward emotional-anchor picks (Reinhardt, Ana, Invisible Woman) — these are picks made on *who*, not *math*.
- Mechanics-first players will click "Show details" and lose nothing. Fantasy-first players will not have to scroll past stat blocks to reach the backstory.

### 10.2 Mechanics-first (alternative)

Top of card: passive + signature + lineage tilt number + stat summary. Middle: portrait + epithet. Bottom: backstory + voice samples.

Rationale: TD/TW veterans (CONCEPT §1.2 — finished BTD6 / KR5 / LTD2) are mechanics-literate and evaluate commanders on kit. Stage 01's commander pick is arguably closer to a loadout than an identity pick for that cohort.

**Decision (leading): fantasy-first.** Per identity framing, per research/03 durable-pick evidence, and per the simple fact that mechanics can be fully surfaced via "Show details" while fantasy-first cannot be recovered by an expander (if the top of the card is a stat block, the identity framing has already slipped). Alternative retained in §14.

## 11. Accessibility floor at Stage 01

The Stage 00 accessibility floor (subtitles, remap, screen reader, colorblind, motion-reduction) is **table stakes**, not stretch. Stage 01 adds the following specifics:

- **Subtitles on voice samples.** Every click-to-play sample renders its line as text adjacent to the speaker affordance. Subtitles are on by default, per the accessibility-floor decision.
- **Remap for Confirm.** The Confirm action in the confirmation modal is keyboard-, controller-, and mouse-addressable. No click-only affordance.
- **Screen-reader names + epithets.** Every gallery tile and expanded card exposes "name, epithet, lineage affinity, one-line passive" to screen readers in that order. Voice samples are announced as "Voice sample — [category]"; activating them plays audio *and* reads the subtitle.
- **Colorblind-safe lineage affinity.** Lineage color accent is supplemented by a distinct icon / glyph per lineage, and by the written lineage name on every tile. Color is never the only cue (§3.1). Each lineage's glyph is distinguishable without color.
- **Motion-reduction.** The ≤1.5s pick-confirmation animation (§7 step 5) is bypassable under motion-reduction preference; the confirm still fires the voice-line pick category and the hand-off to Stage 02, but the sweep animation is replaced with a fade.
- **Focus order.** Tab order walks the gallery left-to-right, top-to-bottom. Expanded card tab order walks portrait → voice samples → passive → signature → tilt → backstory → Confirm. Back-to-gallery is always Escape.

## 12. Tilt-not-cage principle

Copy discipline across every Stage 01 surface: lineages are **tilts**, not **classes**. A commander is "Sinew-tilted," never "the Sinew class." The lineage affinity at [PROPOSAL] +15% is a nudge, not a wall — you can play any commander into any lineage's kit; the tilt changes what is *most efficient*, not what is *available*.

This is load-bearing for the CONCEPT §3.3 design intent and for retention: cage framing ("you're the Sinew guy, you play Sinew") collapses the strategic space and drives re-pick for reasons that are not identity-stickiness. Tilt framing keeps cross-lineage play viable, which keeps match-to-match variety high, which is what retention depends on.

Copy examples:

- Tile text: "Sinew-tilted" — never "Sinew class" or "Sinew-locked."
- Tilt indicator: "+15% [PROPOSAL] to Sinew outputs" — never "Sinew only" or "Specializes in Sinew."
- Backstory preview: lineage is narrative flavor, not mechanical identity.

Stage 01 copy gets a lint pass against this principle before every playtest build.

## 13. Open questions

Inherited seed list (7) plus additions. Each tagged with resolution venue.

1. **Launch roster size (3 / 5 / 8).** Resolution: `decisions/<date>-roster-size.md`. Leading: 5 per research/03 §6 [PROPOSAL].
2. **Archetype slot assignments per lineage.** Resolution: `decisions/<date>-starter-roster.md`. Leading: research/03 §5 anchors.
3. **Change-commander progression policy.** Resolution: `decisions/<date>-commander-progression.md`. Leading: per-commander XP, shared generic cosmetics, per-commander commander-specific cosmetics (§8).
4. **Gender / age / species diversity floor for starter roster.** Resolution: covered implicitly by research/03 §4's appetite-seed recommendation. Promote to a `decisions/` entry if the starter-roster ratification does not absorb it.
5. **Voice-sample UX — auto-play on hover, or click-to-play.** Resolution: `stages/01` section §9 — leading click-to-play. Ratify at first playtest or promote to `decisions/` if contested.
6. **Commander names.** Resolution: a later naming pass per CONCEPT §5.4. All current labels are placeholder.
7. **Mechanics-first vs fantasy-first card layout.** Resolution: `stages/01` section §10 — leading fantasy-first. Ratify at first playtest.
8. **[NEW] No-commander / classic mode toggle.** Does the player ever skip Stage 01 on a "classic TW, no commander" mode? Research/03 §6 caveat 4 flagged this as cross-dependent on Stage 01. Resolution: `decisions/<date>-no-commander-mode.md`, owned by whichever of mode-select (Stage 02) or commander-scope lands first.
9. **[NEW] Silhouette read-test protocol.** The identity-floor [PROPOSAL] commits to "silhouette + variant distinct at art-direction zoom." How do we *measure* distinctness before ship — developer eyeballing, playtest identification task, or both? Resolution: `research/<N>-silhouette-readability.md` or a Stage 08-adjacent playtest protocol.
10. **[NEW] Return-from-match back to Stage 01 vs. main menu.** After a match, does the end-of-match surface offer direct "Change Commander" or only route through the main menu? Affects the CONCEPT §6.4 re-pick metric collection pipeline. Resolution: `stages/07` (end-of-match) or a decisions entry when that stage drafts.

## 14. Alternatives considered

### 14.1 Roster size 3 vs. 5 vs. 8

Covered in §5 and research/03 §6. Leading: 5. The 3-slot alternative is defensible as a content-constrained launch and becomes more defensible if Stage 02 supports a no-commander mode (open question 8). The 8-slot alternative is defensible as a content-rich launch if art-direction cost per commander drops materially; it is structurally one-way because removing commanders post-launch reads to players as theft (research/03 §6 reversibility).

### 14.2 First-pick skippable vs. forced

**Leading: forced on first run.** Alternative: a "skip — pick for me" affordance that randomly assigns a Commander. Defense: reduces cognitive load for indecisive players. Counter: Commander is persistent identity; random-assigning it is a framing contradiction and collapses the Stage 01 purpose. Forced pick plus the "you can change later" copy is the better tradeoff.

A separate alternative — "no-commander mode" as a gallery option — is tracked as open question 8 and is a mode-select question, not a Stage 01 question.

### 14.3 Change-policy free vs. cost-gated

**Leading: free outside match.** Alternative: a soft-currency cost to re-pick after match 1 ("respec cost"). Defense: adds weight to the initial pick, drives consideration. Counter: the CONCEPT §6.4 re-pick metric goes noisy if re-pick is cost-gated (§8.4). Soft-currency gates on identity read as pay-to-feel-like-yourself (§8.3). The initial-pick weight is better served by the "you can change later" copy and by the identity framing, not by a cost barrier.

### 14.4 Auto-play voice vs. click-play

**Leading: click-to-play** (§9). Alternative: hover-auto-play with an Options toggle. Defense: faster discovery of voice tone across the roster; users who hate it can toggle it off. Counter: accessibility and audio-bus behavior (§9 rationale) point strongly to explicit-intent play. Default-on hover-auto is wrong; the Options toggle is the fallback for users who want it.

### 14.5 Grid vs. carousel vs. list

Covered in §3.2. Leading: grid. Carousel is the controller-build fallback; list is the 8+ roster fallback.

### 14.6 Fantasy-first vs. mechanics-first card

Covered in §10. Leading: fantasy-first with "Show details" expander for mechanics deep-dive.

## 15. Verification

Three inherited criteria plus additions from the identity-floor spec.

Inherited:

- **V1.** 70% of first-time playtesters pick a Commander within 90 seconds of gallery open.
- **V2.** 50% of first-time playtesters, after one match, articulate their Commander's fantasy in one sentence (free-response post-match, keyword-graded).
- **V3.** <20% of first-time playtesters swap Commander within their first 3 matches (indicates sticky identity; cross-references CONCEPT §6.4 re-pick metric).

Additions from identity-floor [PROPOSAL]:

- **V4.** 70% of post-match playtesters correctly name their Commander's **passive effect** in one sentence (free-response, keyword-graded). Tests whether the passive is surfaced clearly enough on the expanded card.
- **V5.** 70% of post-match playtesters correctly identify their Commander's **silhouette** when shown a side-by-side with two non-roster silhouettes at battle-map zoom ("which of these is your Commander?"). Tests the silhouette floor and connects to open question 9.
- **V6.** Voice-sample click-through rate on the expanded card ≥60% of card-expansions. If voice samples are below 60%, either the affordance is invisible (UX failure) or the bank is not compelling (content failure); either way, a signal.
- **V7.** Commander re-pick rate on match 2 (per CONCEPT §6.4 + identity-floor decision Loop-3 promotion) — target range TBD by playtest data. Floor: the metric must be non-zero (some variety) and not majority (no one-commander-dominates collapse). Stage 01's change-commander policy (§8) is designed to make this metric clean.

Verification passes are run at MVP validation and at every pre-public-release playtest. Failure on V1–V3 blocks release; failure on V4–V7 triggers an iteration loop but does not block.

---

*End of draft. Next review: after first playtest of the MVP 2-commander gallery, or on receipt of the `decisions/<date>-roster-size.md` ratification.*
