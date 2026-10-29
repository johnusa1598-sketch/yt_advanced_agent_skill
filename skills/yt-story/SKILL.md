---
name: yt-story
description: >-
  Give an AI Short a story spine: eight Story DNA elements in a
  fixed arc, a parasocial beat, an eye-contact rule, a dual-mode
  loop bridge, and a comment trigger. Use for "this video feels
  flat", "no story", "make it rewatchable", "loop", or any Short
  that shows a trick but makes the viewer feel nothing.
---

# yt-story

A trick is not a video. A video is a struggle the viewer feels,
a save the viewer believes, and a moment the viewer wants to
comment on. Every Short carries all eight Story DNA elements —
if one is missing, the video feels flat or fake, and it fails QC.

## Story DNA — the eight elements

- **CHALLENGE:** Opens on something genuinely hard — a position
  or skill a real viewer knows is difficult. Obvious, not
  implied.
- **STRUGGLE:** The difficulty is VISIBLE — trembling,
  micro-wobble, barely holding on. The character fights the
  skill; they never coast through it.
- **EFFORT:** Visible exertion throughout — strained face, set
  jaw, muscle tension, controlled breathing, sweat progression.
  Effort is the proof the struggle is real.
- **PERFECTION:** The finish is CLEAN — a stuck landing, a
  controlled hold, a locked save. Struggle → save, never
  struggle → sloppy.
- **PROFESSIONAL:** Movement quality is elite — tight form,
  disciplined grips, pointed toes where the skill demands them.
  No sloppy limbs, no casual flailing, no beginner body
  language.
- **CHEERS:** Someone celebrates — a co-star gasps, claps,
  cheers, fist-bumps; background energy lifts. The win is
  witnessed, not performed alone in silence. Duo is the
  default; solo is the exception, capped at the channel's
  stated weekly number (Aria Fit: 2–3/week). On a designated
  solo slot, CHEERS must still be witnessed — state how
  (a spotter's reaction, a crowd beat, a comment call) — or
  the beat is missing, not waived.
- **DEDICATION:** The grind texture — chalk dust, worn grips,
  repetition energy, the "one more try" feel. Years of practice
  implied behind one clean moment.
- **EMOTIONAL TOUCH:** A human moment at the end — relief,
  pride, a breathless grin, eye contact with the viewer that
  says "I did it." The viewer must FEEL something, not just
  watch a trick.

## The arc (every video, in order)

CHALLENGE (hard position, visible struggle) → EFFORT (the
fight — wobble, strain, breath) → PERFECTION (clean save /
stuck landing) → CHEERS (co-star + energy) → EMOTIONAL TOUCH
(relief/pride + eye contact with the viewer). DEDICATION is the
texture through all of it; PROFESSIONAL is the standard of
every movement.

**QC rule:** If any Story DNA beat is missing in QC, the video
fails QC — do not ship it and hope the next one covers it.

## One way (v3.4.4)

One video is made one way: one question, one skill,
one arc. The hook question, every beat, every text,
and the body all serve the same single claim. A text
that promises movement the body does not perform, or
a beat that answers a different question than the
title asks, breaks the video — the viewer notices
the mismatch before they notice the skill. Part 11
is the precedent: "DOWN, SLOWLY" over a body that
barely descends told two stories, and the video
felt broken from the first frame where they split.

## The peak beat (sustain, never release) (v3.4.2)

The peak is the PERFECTION beat — the hold, the stuck
landing, the locked save — and it is where renders most
often go weak. The reason is structural (see
`/yt-production`): on a suspense title the hook frame is
the struggle, so the peak is invented mid-video, far
from the only anchored frame, exactly where the model
drifts. A peak written as a state ("she holds it",
"clean!") reads to the model as rest: tension releases,
the face goes neutral, limbs sag — or strain collapses
into a scrunched, eyes-shut struggle. Both read as weak,
and both fail this rule.

Write the peak as SUSTAINED effort, not a state:
- Limbs locked in the peak position for the whole beat
  — straight legs stay straight, the hold height does
  not drop, the shape at the end of the beat matches
  the shape at its start.
- Tension visible throughout: slight tremor in the
  working muscles, braced core, set jaw, controlled
  breath. Tension does NOT release until the lower or
  release beat that follows the peak.
- Face follows the eye rule at the peak: static holds
  keep direct, intense eye contact locked on the lens;
  a blank, neutral, or relaxed face in the peak
  position is a fail, and so are eyes squeezed shut —
  strain is shown through the jaw, the breath, and the
  tremor, never by losing the eyes.
- The peak form stays VISIBLE: no text layer, grade
  change, or graphic may cover the working limbs or
  the face during the peak beat. Text and grades frame
  the peak; they never hide it.

## After the peak, a beat — never a gap (v3.4.3)

The peak is not the end of the video. The seconds
between the peak beat and the parasocial tail must
carry a beat: a CHEERS reaction, a second-angle
payoff, the rewatch detail reveal, or the payoff beat
itself. The skill's ending — a leg lowering, a
landing, a release — is NOT a beat; it is the skill
finishing. Part 10 died here: peak at ~5s, then 6–8s
of nothing but the leg lowering under junk texts,
and the payoff only at 9–10s. The viewer decides the
video is over the moment the skill finishes and
leaves before the CTA. Cap: no more than 2 seconds
between the peak beat's end and the next beat
without one. If the raw render leaves a gap, the
edit fills it: cut the dead lower, or move the
payoff earlier — never let the video sit on a
finished skill.

A completion word (CLEAN!, DONE, NAILED IT) appears
only when the visual completes — never mid-lowering,
mid-landing, or mid-release. Part 10 showed "LEG
RAISE, CLEAN!" while the leg was still lowering.

## Post-peak beat (v3.4.5)

The gap cap above is the floor; this is the shape.
The payoff — the result, the score, the verdict —
lands 3–5 seconds before the end, and the CTA sits
INSIDE the payoff beat, overlaid on motion (the
reaction, the second-angle replay, the reset toward
the hook pose). Never a trailing end card or logo
held after the skill: once the viewer can predict
"nothing else is coming", they leave, whether the
signal is a spoken outro or a visibly completed
skill [LORE — telegraphed-outro collapse]. The
parasocial tail cap still holds (beat + CTA fit in
2 seconds, then cut or loop) — the payoff beat and
the tail together are the final seconds, and the
loop frame closes them. A video whose peak is its
last fact has no post-peak beat, whatever its
scorecard total says; `/yt-qa` gates it.

## Re-hooks (v3.4.5)

No more than ~2.5 seconds without a new visual
fact. In practice that means a re-hook beat — a
cut, a text twist, or a sound accent — at about
3.5 seconds and again at about 7 seconds, placed
BEFORE the bleed, not after it. The 3–8 second
bleed zone in retention curves is where a video
with a good hook but no middle beat dies [LORE —
creator-observed curve shapes, not a YouTube
rule]; the cadence numbers here are rules of
thumb, not measured thresholds, and the direction
(change something) is the rule, not the exact
second. A re-hook must add information (a new
angle, a stakes line, a progress marker) — a
re-hook that repeats the hook is a repeat, not
a beat.

## Comment prompt placement (v3.4.5)

The comment trigger in the section below is placed
AFTER the payoff only, never as a substitute for a
middle beat: one prompt, at most 6 words, rating-
only, overlaid during the payoff/reset motion (see
`/yt-community` priority for the vote form on
comparison Shorts). NEVER claim a comment prompt
holds viewers mid-video: no source found measures
a retention effect for comment prompts [research
report §3.4]. It converts viewers who already
stayed into commenters, and gives a reason to
rewatch to check a detail — it is not a beat, and
a video that leans on it instead of a re-hook or
a post-peak beat will still bleed.

## The parasocial beat (mandatory, never skipped)

Near the end, the character looks directly into the lens with
a breathless, genuine grin, and connects: a small signature
gesture (adjusting glasses, a chalky knuckle, a wave) and, if
a co-star is present, a quick clean fist-bump. This beat must
actually appear — never skipped, softened, or drifted past.
It turns a viewer into a follower; a video without it is a
performance with no one to perform to.
**Cap (v3.3.2):** the parasocial beat is 1–2 seconds, never
a 3–4 second end card. After the skill ends, the beat plus
the CTA together must fit in 2 seconds, then cut or loop
back to frame 1. A smile that runs past 2 seconds after
the skill is a retention tail, not a beat — trim it.

## Eye-contact split rule (pick ONE by skill type)

- **Static hold** (handstand, balance, hold): direct, intense
  eye contact locked into the camera lens.
- **Dynamic skill** (flip, jump, drop): the athlete's spotter
  gaze locked strictly on the landing spot or apparatus —
  never a mid-air camera stare.

A blank, neutral, or relaxed face in a hard position is a
fail. So is a random smile at peak exertion. Expressions
progress with effort: intensity at the opening, tension on
corrections, release and a genuine smile at the payoff.

## Loop bridge, dual-mode

Never end sitting, standing idle, or posed smiling away from
the skill. The last seconds return to the 0.0s opening:

- **Static holds:** place hands/feet back onto the apparatus
  and rebound cleanly into the exact body position, framing,
  and tension of the opening frame.
- **Dynamic jumps/flips:** swing arms back, bend knees, and
  launch upward so the final frame cuts mid-takeoff at the
  exact height and body vector of the opening airborne frame.

Audio cuts cleanly on the final rebound/takeoff breath so the
loop restarts without a gap or pop. No visible loop reset, no
drift off the skill at any point.

## Rewatch engineering (v3.3.7)

The loop bridge above is the mechanism; this is what makes
a viewer use it a second time. Shorts loop automatically,
and since 31 March 2025 every replay counts as a public
view — but monetisation runs on engaged views, and YouTube
publishes no ranking weight for loops, so this pack claims
none (see `/yt-shorts-first` for the honest statement).

**Loop-match check.** The last 2 seconds must match the
first 2 in light, angle, and body position, and the beat
must continue across the join — no hard cut to silence, no
subscribe end-card, no black screen, no held goodbye frame
after the ≤2 second parasocial tail. The CTA sits inside
the tail, then the video loops. Motion hides the join only
at the join itself (the dynamic mid-takeoff cut); the video
itself stays one continuous shot, no cuts.

**One rewatch trigger per Short.** The Easter egg rule,
named before the shoot (`rewatch_trigger` in the brief):
one hidden detail, missed moment, count-the-detail,
satisfying payoff, fast payoff + slow information reveal,
or end reframe — pick one from the menu in
`/yt-shorts-first`. The trigger must actually be present in
the video; a trigger claimed in the brief but absent fails
the rewatch gate in `/yt-qa`. The pinned comment asks about
it; on a comparison Short the vote carries the ask (see
`/yt-community` priority). Speed ramps are excluded: their
slow portion is slow-motion footage, which FINAL bans.

## Duel format — two skills, one question (v3.5.0)

A Duel is a comparison Short with a vote, not two videos
cut together. It works because the vote is a decision the
viewer makes, and a decision replays: the channel's Poll
Duel (Back Handspring vs Front Aerial, user Studio data
October 2026: 16.4K views, 120.5% average view percentage)
is the precedent — an average view percentage over 100%
means viewers watched more than once, which is the vote
and the loop doing their job, not a claim about ranking.

One-way still holds: a Duel has ONE question ("A or B?"),
and both skills serve it. A Duel that is really two
unrelated tricks with a vote pasted on top is two videos
and fails one-way. The question must be answerable from
the video alone: the viewer must SEE both skills well
enough to pick a side.

Structure for a ~9s Duel (one continuous shot per skill,
same rules as any Short):
- 0–2s: BOTH sides named, in video order, with the
  stakes in one line — "Back Handspring vs Front Aerial —
  YOU pick the next skill." No setup, no greeting, no
  channel intro (see /yt-shorts-first hook rules).
- Skill A attempt: the full arc in miniature — struggle
  visible, clean finish. Not a clip of a clip.
- Skill B attempt: the same standard. A Duel where one
  side is visibly weaker is rigged, and viewers read
  rigged as fake — both sides must be genuinely hard
  and genuinely clean.
- Payoff + vote: the CTA sits inside the payoff beat
  (see post-peak beat above), naming both sides in the
  order the viewer saw them. The pinned comment is the
  vote (see /yt-community vote rule) — one pinned
  comment, one job; the vote carries the ask, and any
  trigger detail is asked inside the vote or in a
  reply, never as a competing pinned comment.
- Follow-through (non-negotiable): the winning side
  BECOMES the next video, and the next video says so
  ("You voted Front Aerial — here it is"). A vote whose
  winner never appears teaches viewers their vote did
  not matter, and the next Duel gets no votes. See
  /yt-community poll rules: a deciding vote is
  reported in the video it decides.

Duel variants that keep one question:
- **Progression ladder:** Level 1 to Level 5 of one skill
  family, hardest tier last. The question is "how far
  does she get?" — the ladder IS the arc, and the
  finale tier is planned before episode one (see
  /yt-series: a series with no finale is a treadmill).
- **Road to Mastering [skill]:** Day 1 vs Day 7 of one
  skill. Same skill, visible progress — the question is
  "did she get it yet?" The Day 1 attempt must be
  honestly weaker, never faked worse than it was.
- **Testing Your Challenge Requests:** the skill is the
  one viewers asked for most. Name the request and the
  requester count in the video ("most-voted request"),
  attempt it clean, and say what happens to the
  runner-up requests — or viewers stop requesting.

Episodic CTA (v3.5.0): the subscribe ask names the
next episode's stake, never a generic "subscribe".
"Subscribe to see if she lands this on the beam
tomorrow" beats "subscribe for more" because the
viewer is subscribing to an outcome, not a channel.
The CTA still fits inside the payoff beat (2 seconds
with the parasocial tail, then cut or loop).

## Comment trigger (one per video)

Include ONE small comment-worthy detail: a tiny Easter egg, a
relatable detail, or a small debatable moment — a chalk
handprint left on the surface, a wobble that looks like a
near-fail. Never forced, never distracting from the skill.
The pinned comment (see `/yt-community`) then asks about it,
so the detail and the comment work as a pair. Priority
(v3.3.6): on a comparison or challenge Short, the pinned
comment is the vote naming both sides in video order
(`/yt-post` vote rule) — the trigger detail is then asked
inside that vote or in a reply, not as a competing pinned
comment. One pinned comment, one job.

## What to hand back

- The eight elements mapped onto this video's beats, in arc
  order, with the missing one named plainly if any is missing.
- The parasocial beat written as an actual beat, not a note.
- The eye rule picked (lens or landing spot) and the loop
  mode picked (rebound or mid-takeoff cut).
- The one comment trigger, named in one line.
- For a Duel: both sides named in video order, the vote
  question, and the follow-through promised (which video
  the winner becomes).
