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
