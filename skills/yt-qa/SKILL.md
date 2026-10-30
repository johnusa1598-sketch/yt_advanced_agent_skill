---
name: yt-qa
description: >-
  Score a finished AI video before it ships: the segment method,
  beat verification, face-crop QC, a ten-point scorecard with a
  hard publish threshold, and the face gate. Use for "is this
  ready to publish", "check this video", "score this", "QA",
  or any video where a missing beat or an unverifiable face
  would be a publish mistake.
---

# yt-qa

Do not fix videos one by one. Strengthen the system so the
known shortcomings cannot recur. This skill is the gate between
"rendered" and "published" — it scores, it does not praise.

## Segment method (how the video should have been made)

ONE generation = ONE skill / ONE peak moment. Never ask a
single generation for a multi-beat routine — the generator
drops planned beats. A multi-skill concept is produced as
separate segment clips (one generation per skill, each with
the character lock verbatim and the reference image first),
then ASSEMBLED in editing (best 2–4 seconds per segment, in
beat order, final segment = return to the opening pose for
the loop).

- Blueprints must decompose into a segment list (seg 1, seg 2,
  …). If a concept cannot be decomposed into single-skill
  segments, it is not a valid concept.
- A missing beat is fixed by regenerating ONLY that segment
  and re-assembling — never by regenerating the whole video.

## Beat verification (mandatory)

Check the output against the plan's segment list, beat by
beat. Every planned beat must be visibly present. A missing
or substituted beat (for example a front split instead of
middle splits) = FAIL-FIXABLE with the segment fix above.
A beat that was never in the plan does not count as a
replacement for one that was.
- **Post-peak gap.** List beats with timestamps. Any gap
  over 2 seconds between the peak beat's end and the
  tail's start with no beat = FAIL-FIXABLE (edit fix:
  trim the dead lower or move the payoff earlier).
  The skill's ending (a leg lowering, a landing, a
  release) is not a beat — Part 10 died in 6–8s of
  lowering with no beat before the 9–10s payoff.
- **Question–skill match, and one way.** Before scoring
  beats, check the concept itself: a range question
  ("HOW LOW?") needs a progressive skill, a duration
  question ("CAN SHE HOLD IT?") takes a static hold
  (see `/yt-anti-glitch` title-first gate). A static
  hold under a range question, or a question answered
  in frame 0, = FAIL at the concept — fix the
  question or the skill, not a segment. Then check
  one way: every beat and every text must serve the
  title's single question and the body's single arc.
  A text promising movement the body does not
  perform (Part 11: "DOWN, SLOWLY" over a body that
  barely descends) = FAIL-FIXABLE: re-time or
  re-word the text, or re-cut the beat.
- **Hook-drop gates (v3.4.5).** The hook-drop is two
  decays compounding (model decay + narrative decay,
  see `/yt-production` end-frame and segment rules),
  so these are checked beat by beat, not by feel.
  Each failure is FAIL-FIXABLE, even with a passing
  scorecard total; pass the verdicts to
  `scorecard.py` (flags below):
  - **End frame.** An end-frame still (peak pose and
    expression) was supplied where the tool supports
    first+last frames, OR a peak-as-its-own-segment
    fallback is documented. Neither = FAIL-FIXABLE
    (`--end-frame absent`).
  - **Segment cuts on motion.** Multi-segment videos
    cut mid-movement, so the eye follows motion
    across the seam; heads trimmed (opening freeze)
    and drift tails trimmed. Cuts on still frames
    or untrimmed drift tails = FAIL-FIXABLE
    (`--segment-cuts static`).
  - **Post-peak beat.** A beat after the peak, with
    the payoff landing 3–5 seconds before the end
    and the CTA inside the payoff — never a trailing
    end card or logo (`--post-peak absent`,
    `--end-card trailing`).
  - **Re-hook.** A cut, text twist, or sound accent
    at about 3.5 seconds and about 7 seconds
    (`--rehook absent`). The cadence is a rule of
    thumb [LORE], not a measured threshold — the
    gate is "a new visual fact before the bleed",
    not the exact second.
  - **No result before the peak.** The result, score,
    or verdict must not appear (text or visual)
    before the peak beat closes the loop early
    (`--result-early yes`).

## Face-crop QC

Extract a 200–300% zoomed face crop from the clearest
face-visible frame and verify, line by line: the locked
accessories present and on the correct side, glasses frames
correct, freckle or skin-marking weight correct, hoop or
earring size correct. Every concept must include at least ONE
face-visible beat (lens grin, close-up, upright pose) so
verification is possible. A video with no verifiable face
frame scores 0 on identity (see the scorecard).
**No nose ring (v3.5.1):** the character wears no nose ring,
so there is no ring side to verify — the v3.3.5 side check
and the v3.3.6 frontal-frame verdict rule are both retired.
Verify glasses, earrings, and freckle weight on the face
crop. If a render shows a nose ring, log it as an
observation, not a failure: the failure mode this removal
ends was the demanded ring rendering wrong (centre,
septum, duplicated) in video after video.

## Ten-point scorecard (the verdict)

Score every prepped video out of 10:

- Identity & character match: 0–3
- Movement realism (no glitch, no float, real effort): 0–3
- Phone-look (single handheld phone shot, ambient light,
  no cinema bokeh): 0–2. This scores the look, not the
  pixel count — resolution is judged by the format gate
  below, not here.
- Beat completeness (all planned segments present): 0–2

**Publish threshold: total ≥ 8 AND identity ≥ 2 AND movement
≥ 2.** Below threshold = FAIL-FIXABLE (segment fix first) or
FAIL-REALISM. The score is written into the run record and
the QA report line. Run it with the tool:

```bash
python3 scorecard.py --identity 3 --movement 2 --phone 2 --beats 2
python3 scorecard.py --identity 1 --movement 3 --phone 2 --beats 2 --json
```

A total of 8 with identity 1 still FAILS — the sub-thresholds
are gates, not suggestions.
**Hard gates in the tool (v3.3.6; --nose retired v3.5.1):** pass the evidence to
`scorecard.py` and a failed gate fails the video even at
10/10 — `--width/--height` (9:16 ratio, 720x1280 minimum),
`--slot` (one of the five
rotation colours), `--lufs/--peak/--beat` (audio gate). Every
run prints the gates the tool cannot verify — face gate,
text-end rule, parasocial tail cap, slot vs previous video —
so a PASS is never mistaken for a full QA pass. Those stay
human checks, in this skill.

## Face gate (hard gate — not a score)

A video may ship only if at least one frame yields a
200–300% face crop on which the locked accessories verify.
If NO such frame exists:

- QA marks the video FAIL automatically — not merely a low
  identity score. Regenerate the face-visible segment ONCE
  within the day's fix budget; if it still fails, the day's
  fallback applies (concept switch / emergency backup).
  Nobody has to "catch" it — the gate fails it by itself.
  That regen counts toward the shared 2-fail glitch burst
  (`/yt-anti-glitch`): it is not a third attempt on top of
  the burst.
- The same gate applies to the published video on review:
  face unverifiable = identity HARD FAIL.

Every concept must therefore guarantee a face-visible beat —
a concept that cannot show the character's face cannot be
planned.
For Aria Fit, the face-crop check runs line by line against
the datasheet §8 block (`templates/aria-datasheet-lock.md`),
not just the generic lock: freckle weight and placement,
body proportions, and accessories all verify or the frame
fails.

## Format gate (hard gate — not a score, v3.3.0; clarified v3.3.4)

Same status as the face gate. The hard part is ratio and
look: a video that is not vertical 9:16 portrait, full
frame, or does not look shot on iPhone — horizontal,
letterboxed, pillarboxed, or cropped from horizontal
footage — FAILS, regardless of its scorecard total. Do not
ship it, and do not "fix" it by cropping a horizontal
render. Re-generate with the format lock from
`/yt-ai-prompt` (vertical 9:16, shot on iPhone) and re-run QA.
**Resolution clarification (v3.3.4):** 1080x1920 is the
preferred target. 720x1280 at the same 9:16 ratio is the
minimum acceptable and PASSES this gate — do not fail a
video only for being 720p, and do not upscale 720p to fake
1080p (upscaling adds no detail). If the rendering tool
can output 1080p, use it; if it outputs 720p, ship at
native 720p.

## Audio, text-timing, and tail gates (v3.3.2 — checks, not scores)

These checks sit beside the scorecard; they do not change
its points. A video that fails one is FAIL-FIXABLE, even
with a passing scorecard total.

- **Audio.** A beat/music track must be present (native
  room noise alone fails), and the finished audio must be
  normalised to a −14 LUFS target with true peak no higher
  than −1 dBTP (`/yt-sound` loudness gate). Measure it with
  `loudness.py` in `/yt-sound` (ffmpeg ebur128, true-peak
  mode) and pass the numbers to `scorecard.py --lufs/--peak`
  — the gate is no longer a human estimate (v3.3.6). Quiet
  or music-less = FAIL-FIXABLE: normalise and add the track,
  then re-check. Note the beat-track presence itself still
  needs a human ear: loudness.py measures level, not whether
  a beat track exists.
- **Text timing.** Freeze the frame at each text change
  and at the skill exit. The text on screen must match the
  visual on screen at that second. A text layer that lingers
  into the next beat, the exit, or a standing pose =
  FAIL-FIXABLE: re-time the layer, no full re-render needed
  if the edit allows it.
- **Text inventory.** Freeze frames across the video and
  list EVERY visible text. Each must be in the brief's
  approved text list (kinetic words, caption lines,
  rewatch pill line, CTA). Production metadata
  (rotation slot, beat/skill names, channel bugs,
  component labels such as the word "prompt" on a pill)
  = FAIL-FIXABLE: remove the layer in the edit. A
  kinetic word clipped at the frame edge (Part 10:
  "UP, SLOWLY" cut at the left edge) = FAIL-FIXABLE:
  resize/reposition inside the safe band. A completion
  word (CLEAN!, DONE) must appear only when the visual
  completes — Part 10 showed "LEG RAISE, CLEAN!"
  while the leg was still lowering = FAIL-FIXABLE:
  re-time the layer.
- **Tail.** After the skill ends, the parasocial beat plus
  the CTA together must fit in 2 seconds, then cut or loop
  back to frame 1 (`/yt-story` cap). A longer tail =
  FAIL-FIXABLE: trim it.
- **Leotard slot (v3.3.3).** The leotard colour must match
  the package's planned rotation slot, not always purple.
  A video in the wrong slot colour = FAIL-FIXABLE
  (re-generate the segment in the planned slot). All other
  identity elements — hair, glasses,
  earrings, freckles — must still match exactly; a change
  there is identity drift, not rotation.

## Loop + rewatch gates (v3.3.7 — checks, not scores)

These sit beside the scorecard like the audio, text, and
tail gates. A video that fails one is FAIL-FIXABLE, even
with a passing scorecard total.

- **Loop match.** Static holds: the final frame rebounds to
  the exact opening position, framing, and tension. Dynamic
  skills: the final frame cuts mid-takeoff matching the
  opening airborne frame. Last 2 seconds match the first 2
  in light, angle, and position; the beat continues across
  the join with no silence gap or pop; no subscribe end-card,
  black screen, or held goodbye frame after the ≤2 second
  tail. Pass the verdict to `scorecard.py --loop-match
  matched/mismatch` — a mismatch fails even at 10/10.
- **Rewatch trigger, present not claimed.** One trigger per
  Short (hidden detail, missed moment, count-the-detail,
  satisfying payoff, fast payoff + slow information reveal,
  or end reframe — see `/yt-shorts-first`). Verify it is
  actually visible in the video; a trigger named in the
  brief but absent from the render is a fail, not a pass.
  The pinned comment must ask about it (or the vote must
  carry the ask on a comparison Short). Pass the verdict to
  `scorecard.py --rewatch yes/no`.
- **Scope note.** The Monday 26-October handstand pack was
  approved as-is before this rule and carries no rewatch
  trigger; it is exempt from this gate until the user
  decides otherwise (see the changelog question list). New
  videos are not exempt.
- **Reading the loop in Studio.** Average percentage viewed
  above 100% means viewers looped — that is the loop
  working, not a data error. Judge it beside engaged views:
  since 31 March 2025 every replay counts as a public view,
  but monetisation runs on engaged views, so raw views alone
  overstate a rewatchable clip. A loop that only inflates
  views without engaged views or return viewers has not
  proved anything.

## Peak-tension gate (v3.4.2 — check, not score)

Sits beside the scorecard like the loop and rewatch
gates. A video that fails it is FAIL-FIXABLE, even
with a passing scorecard total.

- **Peak tension, sustained not released.** Freeze the
  frame at the peak beat (the PERFECTION beat: the hold,
  the stuck landing, the locked save) and check it
  against `/yt-story`'s peak rule: limbs locked in the
  peak position with no sag across the beat, tension
  visible throughout (slight tremor, braced core, set
  jaw, controlled breath), eyes per the eye rule
  (static holds: locked on the lens). A neutral, blank,
  or relaxed face in the peak position FAILS; limbs
  that sag or drop height across the beat FAIL; eyes
  squeezed shut at the peak FAIL; a text layer or
  grade change covering the peak form FAILS. Pass the
  verdict to `scorecard.py --peak-tension
  sustained/released` — released fails even at 10/10.
- **Why it exists.** On suspense titles the peak is
  invented mid-video, far from the anchor frame, and
  renders go weak there in every generation (Part 8
  pistol squat, Part 9 L-sit: tension released or
  collapsed into strain at the peak). The fix is in
  `/yt-production` (peak as its own segment) and
  `/yt-story` (peak-sustain wording); this gate catches
  it when the fix was not applied.

## What to hand back

- The segment list with each beat marked present or missing.
- The face-crop verdict: verified, or gate FAIL.
- The scorecard: four sub-scores, total, and PASS or FAIL
  against the threshold, with the exact fix for a failure
  (which segment to regenerate, or the fallback).
- Nothing ships on a FAIL. A good-looking output does not
  override a gate.
