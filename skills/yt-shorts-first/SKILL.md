---
name: yt-shorts-first
description: >-
  Make a Shorts-first channel work: a daily Short that survives on its
  own, with a first-two-seconds hook, a loop point, one call to action,
  and a series it belongs to. Use for "make a Short", "daily Shorts",
  "Shorts idea", "why did this Short flop", or a Shorts-only channel.
---

# yt-shorts-first

The original pack treats Shorts as cut-downs from a long video. A
Shorts-first channel has no long video to cut from, so this skill
starts from the Short itself.

## Before you write

1. Read the channel profile in `templates/channel.md` if it exists,
   and the series bible in `templates/series.md`. A Short that does
   not belong to a series is a one-off, and one-offs do not compound.
2. Read the channel voice profile (`templates/voice.md`) if it exists, or `~/.claude/youtube/voice.md` on Claude Code. If it does not exist, ask for
   three of their own videos and write it first.
3. Never invent a number, a result or a source. If a figure would
   strengthen it and you do not have one, ask for it or write the
   line without it.

## The shape of one Short

- **Format lock: 9:16, shot on iPhone.** Vertical portrait,
  1080x1920 preferred (720x1280 at the same ratio is the
  minimum acceptable, v3.3.4), full frame, handheld
  smartphone look. Never horizontal, never letterboxed,
  never cropped from horizontal footage. The prompt lock
  lives in `/yt-ai-prompt`; this skill
  enforces it at the idea stage, not after rendering.
- **First two seconds.** Show the hardest moment, the fail, or the
  question — unless the hook is a question whose answer is the
  skill, in which case show the struggle, not the payoff
  (suspense rule below). No greeting, no channel intro, no setup.
- **One idea only.** A Short that tries two skills is two Shorts,
  and the second one is the one people leave on.
- **A turn in the middle.** A claim, then something that complicates
  or proves it. Without a turn the viewer has no reason to stay.
- **A loop point.** The last line must set up the first line, so a
  rewatch feels like a continuation, not a repeat.
- **One call to action.** Not three. Name the next video, the poll,
  or the series, and stop.

## Hook patterns and pacing (2026 research, v3.2.0)

Full notes and sources: `../yt-algorithm/references/2026-signals.md`.
These are third-party reported patterns, not YouTube rules.

- **Five hook patterns:** visual disruption on frame one; a
  face speaking to camera; an unexpected visual (fail,
  contradiction); a rapid scene change or music beat in the
  first 1–2 seconds; text curiosity on frame one. Pick one
  per Short, and test two distinct hooks per concept
  (visual vs verbal) in staggered uploads before declaring
  a winner.
- **Hook formula:** statement in the first 3 seconds, proof
  point, promise — all in 8–12 seconds. If the first-3-second
  leak is the biggest drop, rewrite the hook, not the body.
- **Suspense rule (v3.3.2):** if the hook is a question,
  frame one must not answer it. Show the struggle, not
  the payoff. A viewer who already sees the full skill in
  frame one has no reason left to watch the answer.
- **Pacing:** a visual change every 2–4 seconds, captions
  that reinforce the hook (many viewers watch muted), and a
  loop whose final frame visually continues the opening
  frame. In Studio, a working loop shows as retention above
  100% at second 1.
- **Length orientation:** 20–35 seconds most-cited for 2026;
  18–25 for one trick, 35–55 for a short narrative arc — for
  recorded and edited Shorts only. For AI-generated Shorts the
  hard budget is 8–12 seconds (about 9 target) per
  `/yt-production`: a longer concept is decomposed into
  segments, never stretched into one beat map for a tool that
  caps near 10 seconds.
- **CTA placement:** the single CTA goes in the payoff or
  immediately after it. Harder asks go in the pinned comment.
- **Thumbnail, second job:** the feed does not click a
  thumbnail, but the channel grid, search, and related-Shorts
  panel do. A grid-readable thumbnail is worth five minutes
  on any Short meant to live on the channel page.

## Rewatch engineering (v3.3.7)

A Short that is only watched once is a Short that ends. A
Short that is watched twice is a Short whose ending feeds
its beginning. This section strengthens the FINAL template's
loop bridge dual-mode and Easter egg rule — it does not
replace them, and it does not add cuts, slow motion, or any
character change.

**Why a loop is worth engineering — stated honestly.**
Shorts loop automatically: when a Short ends without a swipe,
it restarts. Since 31 March 2025, a view is counted every
time a Short starts to play or replays, with no minimum watch
time — so a genuine second watch adds a public view, and
average percentage viewed above 100% in Studio means viewers
looped. Two limits, both load-bearing: monetisation and YPP
eligibility still run on engaged views, not total views, so
a loop inflates reach numbers, not earnings; and YouTube
publishes no ranking weight for loops. Third-party guides
widely call loops "one of the strongest signals" — that is
their claim, not a YouTube statement, and this pack does not
quote it as a rule. Judge a loop on Studio's own numbers:
average percentage viewed, and engaged views beside it.

**Seamless loop engineering (extends the FINAL dual-mode).**
The FINAL modes stay the law: static holds rebound to the
exact opening position, framing, and tension; dynamic
skills cut mid-takeoff matching the opening airborne frame.
On top of them, check these before shipping:

- **End = opening, in the last 2 seconds as in the first 2.**
  Same light, same angle, same body position. A viewer who
  cannot tell where the video ended has no reason to swipe.
- **Audio joins cleanly.** The cut lands on the rebound or
  takeoff breath, the beat continues across the join, no hard
  cut to silence, no gap or pop. A silent join is a visible
  seam, and a seam ends the loop.
- **No finality after the CTA.** The single CTA sits inside
  the ≤2 second parasocial tail, then the video loops — never
  a subscribe end-card, a black screen, or a held goodbye
  frame after it. Finality is the loop's off switch.
- **Motion hides the join, only at the join.** The dynamic
  mode's mid-takeoff cut is the one place motion covers the
  seam. This is not permission for mid-video cuts: FINAL
  still requires a single continuous shot, no cuts, no
  whip-pans, inside the video itself.

**One rewatch trigger per Short (the Easter egg rule,
extended).** FINAL requires ONE comment-worthy detail per
video. Name it in the brief (`rewatch_trigger`) before the
shoot, from this menu — one only, so the second watch has
exactly one job:

- **Hidden detail.** A small element in the background or
  inside the action that is not obvious on the first watch
  (a chalk handprint, a background figure's reaction).
- **Missed moment.** A micro-event the pinned comment asks
  about ("did you catch the wobble at second 6?") — the
  viewer rewinds to find it.
- **Count-the-detail.** "Dobara dekho aur batao" — count the
  micro-wobbles, the chalk marks, the attempts. The pinned
  comment asks for the number.
- **Satisfying payoff, replayed.** A clean stuck landing or
  a perfect hold, framed so the second watch shows the
  technique, not just the result. Satisfaction replays.
- **Fast payoff + slow reveal.** The payoff lands fast, and
  the how or why is revealed gradually across the video.
  This is an information reveal, NOT slow-motion footage:
  FINAL bans slow motion, and no rewatch trick overrides
  that ban (see the question list in the changelog).
- **End reframe.** A final line that recontextualises the
  opening, so the viewer replays to see it coming. The line
  goes at the END only — on a suspense-question title it
  must never appear in frame one (suspense rule above).

**Comment-driven rewatch.** The pinned comment asks about
the trigger ("how many did you spot?", "did you catch it?"),
so the comment and the second watch work as a pair. Priority
from v3.3.6 still holds: on a comparison or challenge Short,
the pinned comment is the vote naming both sides, and the
trigger ask goes inside that vote or in a reply — never a
competing pinned comment.

**Retention design around the loop.** Pattern interrupts
already live in this skill (a visual change every 2–4
seconds) — vary their type (angle, caption animation, sound
cue, a brief silence after a dense beat) so the interrupts
themselves do not become predictable and habituate. The
rewatch trigger IS the Short's open loop: one detail shown
but unexplained, resolved late or on the second watch. Do
not stack several unanswered questions into an 8–12 second
video — one loop, one trigger, one payoff.

**What fails the rewatch check.** A trigger claimed in the
brief but absent from the video (QA checks presence, not
the claim); a subscribe end-card or black screen after the
CTA; a silent audio join; a loop that traps rather than
earns — a viewer who feels tricked swipes and never
returns. Speed ramps are NOT in this menu: their slow
portion is slow-motion footage, which FINAL bans.

## Score it before you ship it

```bash
python3 shorts_score.py --title "..." --thumb "..." --hook "..." \
  --loop yes --cta "follow for part 2" --series "Skill Challenge"
```

Fix the weakest check first. The score is a checklist, not a
predictor: a high score is not a promise, and a low score is a
reason to rewrite.

## Character and AI honesty

- When a recurring AI character is used, keep one locked spec:
  hair, glasses, jewellery, freckles, outfit, and setting. Write
  it in the series bible and check every new brief against it.
- When visuals or sounds are AI generated, mark the AI disclosure
  in the publish checklist. Do not hide it and do not claim a
  real performance that did not happen.
- Check hands, arms, and landings in the draft before publishing.
  An anatomical glitch is a trust glitch, and trust is what turns
  a view into a subscriber.

## AI video prompt, injected here

For an AI video channel, do not stop at the idea. Run the
brief through `/yt-ai-prompt` and build the 7-layer prompt
with `prompt_builder.py`: character lock, scene lock, timed
action beats with physics, camera, style, loop, and a negative
prompt. A Short idea anyone can write is not the product.
The locked prompt system, with continuity checks, is.

## What to hand back

- The Short idea in one sentence, the series it belongs to, and
  the first line.
- The full AI video prompt, the short prompt, and the negative
  prompt, when the video is AI generated.
- On-screen text for the first two seconds, different words from
  the spoken line.
- The loop point and the single call to action.
- The title and thumbnail pairing, checked with
  `../yt-package/title.py`, and the shorts score.

## The gate

Nothing here publishes. This skill writes and you publish. Every
output ends in a block the user copies, and the last line of every
run is the question: **ship it, or change it?**
