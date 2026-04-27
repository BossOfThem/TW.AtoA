# Decision — Co-op Horde card + lobby copy: truth-in-advertising

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (mode-select Co-op Horde card text + tag, lobby-coop scene comment + lobby-status default copy)

---

## Decision

The Co-op Horde mode-card and lobby copy are updated to reflect what the prototype actually does. The card tag flips from "Phase 10.3 — lobby opens, match not yet wired" to "Phase 10.3 — playable shell via PeerJS"; the body adds a one-line caveat that match autosave is C5/C6 (matches what the new Campaign card now says about persistence). The `#lobby-status` default copy flips from "PeerJS integration lands in Phase 10.3." to actionable instructions ("Host a match to generate an invite code, or paste a friend's code to join."). The HTML scene comment is updated from "Phase 10.3 — stub" to "Phase 10.3 — playable shell." No code logic changes; this is presentation truth-in-advertising.

## Context

After the Campaign-mode shell scene landed (decision: 2026-04-26-campaign-mode-prototype-shell.md), Co-op Horde became the loudest remaining lying-card in the prototype. Its onClick already wires `startMode("horde")` → `goto("lobby-coop")`, both `coopHost()` and `coopJoin()` are implemented, the PeerJS handshake propagates `hello`/`snapshot`/`intent`/`chat`/`match-end`, and after the open event both peers `goto("match")` and the host runs `_startSnapshotLoop()`. The R2/R3 swarm work in this session was specifically hardening that path (snapshot inner-element validation, hello-required gate, chat caps, profile schema-version backfill, immediate-quit on `_onClose`, R3 isFinite/clamp-order/match-end-preserve fixes). The card text was a fossil from the period before any of that wiring shipped.

The same pattern that justified enabling the Campaign card applies here: the disabled/lying signal is itself the bug. A user looking at the mode-select screen today is being told the feature isn't wired when it is. That confuses playtesting, it confuses contributors, and it actively hides where the next round of attention should go (content + autosave) by burying the structural fact that the shell already works.

## Alternatives considered

- **Option A — Leave the copy as-is, defer to C5/C6.** Honest about "match autosave doesn't persist," dishonest about everything else. The "match not yet wired" line is false today. Rejected.
- **Option B — Rewrite to silently elide the phase number.** Drop "Phase 10.3 — …" and just describe the feature. Rejected: keeping the phase tag preserves the parallel structure with the Campaign / Tutorial / Skirmish cards and gives readers a quick grep-anchor against PROGRESS.md / CONCEPT phase rows.
- **Option C — Update the tag to "playable shell via PeerJS" + caveat autosave + flip lobby-status to actionable copy.** (Chosen.) Smallest possible delta that stops lying without overpromising. Mirrors the Campaign card's "playable shell, content placeholder" phrasing so users learn one mental model.

## Reason chosen

Option C is alignment with reality, not new design. The wiring already exists; the cards just had not been re-audited since it shipped. Per "Port findings, not code" — the finding is that copy diverges from behavior, and the fix is copy.

3x debug loop:
- **Loop 1 (attack):** "'Playable shell via PeerJS' overpromises — PeerJS broker can be down, NAT can break the connection, the user's first impression of co-op might be a frozen lobby." — Counter: the lobby-status copy is actionable ("Host a match…") and the network status overlay already surfaces broker/NAT failures via `updateNetStatus`. The card tag describes the prototype's build state, not the broker's uptime. The autosave caveat in the body is the only persistence claim, and it explicitly defers.
- **Loop 2 (steelman):** "Maybe the original copy was self-protective: it sets expectations low so the first contributor who tries co-op and hits a broker hiccup doesn't think the feature is broken." — Reasonable framing, but the cost is wrong. New contributors who read "match not yet wired" will not even attempt to test the wired path; that is a worse failure than a transient broker error, which is recoverable and visible.
- **Loop 3 (synthesis):** Ship the copy. Keep the autosave caveat. Trust the network-status overlay to communicate transient broker/NAT issues at runtime. Flag a follow-up to revisit if PeerJS reliability complaints surface in playtest.

## Reversibility note

Easy. To revert: restore the four edited strings (mode-tag, mode-body trailing sentence, scene HTML comment, `#lobby-status` default text). No state, no schema, no data migration involved.

## Follow-ups

- C5/C6 (engine port) owns: real autosave for Horde sessions (currently in-memory only), broker-failover or relay strategy if PeerJS public broker proves unreliable in playtest, and lobby-room directory (current model is one-on-one invite codes; multi-room lobby is engine work).
- PROGRESS.md: when the next handoff runs, the Phase 10.3 row should advance from "stub" to "playable shell" — symmetric with what the campaign-shell decision did for Phase 10.2.
- If a future R1 swarm finds the network-status overlay does not clearly communicate broker/NAT failures, revisit Loop 1's counter-claim.
