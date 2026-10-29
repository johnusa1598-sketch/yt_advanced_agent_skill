---
name: yt-production
description: >-
  Produce an AI video in two steps instead of one: a hook-frame
  image first, then the video animated from that exact frame.
  Use for "my AI video glitches", "the face changes mid-video",
  "how do I prompt an AI video", "hook frame", "two-step video",
  or any recurring-character AI video that must stay consistent.
---

# yt-production

Never generate a video directly from a close-up portrait photo.
AI video models glitch when forced to invent an environment, full
bodies, two characters, and fast motion simultaneously. Split the
job: lock one perfect frame first, then animate only that frame.

## The pipeline

1. **Title first.** Write the title before generating anything
   (see `/yt-anti-glitch` for the title-first gate). The title
   locks the hook; the frame and the video serve it.
2. **Step 1 — hook-frame image.** Generate the exact 0.0s
   frame: by default a peak-action frame — the character
   mid-skill at maximum tension, effort on the face, the
   scene, lighting, and any co-star placed.
   **Rotation slot (v3.3.3):** the hook frame uses the
   package's planned leotard colour slot (`/yt-ai-prompt`
   rotation: purple, teal, black, royal blue, burgundy, in
   cycle), not the default purple. A hook frame in the wrong
   slot colour fails the gate like any other lock break.
   **Exception — suspense/challenge titles (v3.3.2):** if the
   title is a question whose answer IS the skill ("how low
   can she go?", "can she hold it?", "will she land it?"),
   the 0.0s frame must NOT show the peak. It shows the
   struggle or starting position instead: chalked hands,
   a breath before the attempt, lowering toward the skill,
   effort before the payoff. The peak is the payoff later
   in the video, not frame one. A peak-action frame on a
   suspense title answers the question at 0 seconds and
   kills the hook — that frame FAILS the gate, however
   clean it looks. Showcase titles, which ask no question
   to answer, keep the peak-action frame.
   Format lock, same as the video: vertical 9:16 portrait,
   1080x1920 preferred (720x1280 at the same ratio is the
   minimum acceptable, v3.3.4), shot on iPhone, handheld
   smartphone look.
   This frame locks everything the video must preserve.

## Question–skill match, and one way (v3.4.4)

Two concept rules, checked before Step 1 (see the
title-first gate in `/yt-anti-glitch`):

- **Match.** Range questions ("HOW LOW?", "HOW HIGH?",
  "HOW FAR?") need a progressive skill — a visible
  journey from start to peak. Duration questions
  ("CAN SHE HOLD IT?", "HOW LONG?") take a static
  hold. A static hold under a range question is an
  invalid concept: the answer is already visible in
  frame 0 and the body cannot progress. Part 11 is
  the precedent — "HOW LOW?" over a deep squat hold
  was one pose for 10 seconds; the same footage
  under "CAN SHE HOLD THIS SQUAT?" would pass.
- **One way.** A video is made ONE way: one question,
  one skill, one arc. The hook, every beat, every
  text, and the body all tell the SAME story. Text
  must never promise what the body does not show
  (Part 11: "DOWN, SLOWLY" over a body that barely
  descends), and no beat may belong to a different
  question than the title asks. If the hook promises
  a journey, the body must travel it; if the body
  holds, the hook must sell the hold. A video whose
  text and body tell two stories is not two ideas —
  it is a broken promise, and the viewer leaves at
  the first frame where they notice.
3. **Step 2 — video from the frame.** Feed the Step 1 frame as
   the starting frame into the video tool. The video prompt
   directs only realistic motion, audio, and the loop back to
   frame 1. It invents nothing new about who or where.
4. **Gate before Step 2.** If the hook frame shows any glitch —
   detached limbs, floaty anatomy, face morph, impossible
   physics — do NOT proceed. Simplify one rung down the
   skill-safety ladder (see `/yt-anti-glitch`) and re-lock the
   frame first.
   **No nose ring (v3.5.1):** the nose gate is retired. The
   character wears no nose ring, so the hook frame is not
   gated on ring side. A ring in the hook frame is an
   observation, not a block.
   **Burst counting (v3.3.6):** every failed generation or
   segment regen for this concept counts toward the 2-fail
   glitch burst in `/yt-anti-glitch`. On the second
   consecutive fail, stop and switch — the "regenerate once"
   allowance in `/yt-qa` is not a third attempt.

## Separated copy-paste blocks

Never paste one big prompt into both tools. Keep two blocks:

- **Block A — image generator only.** Identity, peak action,
  face and eye rule, body tension, co-star placement, scene
  realism, optics, and the format lock: vertical 9:16 portrait,
  shot on iPhone. Ends with: no watermark, no text. For Aria
  Fit, the identity in Block A IS the datasheet §8 block
  verbatim (`templates/aria-datasheet-lock.md`), not a
  summary of it.
- **Block B — video generator only, Step 1 image attached.**
  Story beats, camera and physics, mandatory native audio,
  loop bridge, comment detail, negative prompt.
  **Audio (v3.3.2 supersedes FINAL on music):** native gym
  audio is mandatory, but native audio alone is not enough —
  a licence-safe beat track starting in the first 2 seconds
  is required, finished audio −14 LUFS target, true peak at
  most −1 dBTP (measure with `loudness.py` in `/yt-sound`).
  FINAL's "music optional" no longer holds; FINAL's "music
  low, never louder than movement sounds" still does.
- **Single-skill vs multi-skill (v3.3.6).** Block B as written
  is the single-skill Short: one generation, one skill, all
  Story beats in one 8–12 second video. A multi-skill concept
  is not a longer Block B — it is a segment list per `/yt-qa`
  (one generation per skill, best 2–4 seconds each, in beat
  order), assembled in editing to the same 8–12 second budget,
  with the parasocial beat and the loop bridge preserved in
  the final segment (which returns to the opening pose).
  Verify beats per segment per `/yt-qa`, not per assembled
  video only.
- **Peak as its own segment (v3.4.2).** A single-skill
  Short stays one generation by default — EXCEPT when
  the skill is a static hold whose peak sits mid-video
  (5+ seconds from the 0.0s anchor), which is exactly
  the suspense-title shape: the hook frame anchors the
  struggle, and the peak is invented far from it, where
  the model drifts and tension releases (the Part 8/9
  defect: neutral face or eyes-shut strain at the peak
  instead of sustained tension). For those, split the
  peak into its own segment: a setup segment (anchor
  frame → movement toward the peak) and a peak segment
  generated fresh from its own peak-pose start frame
  (peak-action frame, `/yt-story` peak rule for the
  wording), assembled in editing to the same 8–12
  second budget. The peak segment's start frame is
  what anchors the peak — without it, the peak is
  always the weakest beat in the video.
- **End-frame conditioning (v3.4.5).** A single start
  frame is an anchor for the first seconds, not a
  persistent 3-D / physics memory: as a clip runs,
  conditioning on it weakens, attention to older
  frames decays, and the model regresses toward
  average motion — tense faces soften, strain turns
  eyes-shut, fine detail melts. That is model decay
  [DOC — papers and vendor docs, see the v3.4.5
  research report], and no prompt wording alone
  fixes it. Where the tool supports first+last
  frames, give the generation a DESTINATION as well
  as a start: a peak-as-end-frame still (same
  subject, lighting, framing, peak pose and
  expression), so the peak is GIVEN, not hallucinated
  mid-video. Tool support [DOC for Veo 2/3.1:
  optional ending frame, 9:16, 4/6/8s per the
  Google Cloud doc; secondary for the rest, verify
  in the tool's UI on generation day]: Veo 2/3.1,
  Kling (first+last), Hailuo H3, Adobe Firefly,
  Luma keyframes. Limits, stated honestly: the
  middle can still mush on a large pose change
  (endpoints are fixed, the interpolation is not);
  some tools disable other controls when keyframes
  are set (Firefly) or forbid combining keyframes
  with references (Hailuo H3) — check before
  committing. Where first+last is unavailable, the
  fallback is the peak-as-its-own-segment rule
  above: a peak segment generated fresh from its
  own peak-pose start frame. "One open-ended pass
  and hope the middle holds" is not a fallback.
- **Segment assembly (v3.4.5).** An 8–12 second Short
  is at or past the single-shot sweet spot of most
  tools, so a long single generation is the regime
  where anchor decay and chained-error accumulation
  bite hardest. Default for 8–12s: 2–3 short
  anchored segments, assembled in editing to the
  same budget. Rules: each segment starts from its
  own keyframe (hook, peak, or reset); cut ON
  MOTION so the eye follows movement across the
  seam; trim heads and tails — plan on about 3.5
  usable seconds per 5-second clip, trimming 8–12
  frames off each clip start (opening freeze) and
  the drift tail [LORE — stitching guides]; one
  style line verbatim across every segment prompt;
  the same reference image(s) fed to every segment;
  colour-match segments to the best one; one
  continuous audio track underneath so cuts read as
  one video, never per-clip ambience that changes
  at each seam. Extension / last-frame chaining is
  NOT the default: each extension inherits the last
  frame's drift and adds its own [DOC — chained
  conditioning accumulates error], and guides warn
  consistency degrades the longer you extend.
- **Static-hold rescue (v3.4.5).** A static hold is
  the worst case on both decays: no progression for
  the viewer, nothing for the model to track except
  a face it must keep re-drawing. Do not ask the
  model to sustain a tense expression for 10
  seconds. Rescue, in order of preference: (1)
  camera-only motion — locked body, slow push-in
  or orbit, so progression comes from the camera;
  (2) a timer / progress overlay in the edit, so
  progression comes from the count, not the body;
  (3) an editor-held peak frame — generate
  approach → peak, then hold the BEST peak frame
  as a still in the edit with a timer/bar/zoom
  overlay, so the peak expression stays
  pixel-perfect. If the hold cannot support 10
  seconds even with this scaffolding, cut the Short
  to 6–7 seconds: a short Short that loops twice
  beats a 12-second Short that bleeds at second 7.

A prompt pasted into the wrong tool is a wasted generation and
a glitch risk. If a block names the wrong tool, stop and split
it before generating.

## Reference discipline

For any recurring character, an identity reference is mandatory:

- **Reference first, every time.** The reference image is the
  first input on every single generation — image and video,
  every segment, no exceptions. A generation run without it is
  invalid: discard its output, do not post-process it, do not
  publish it.
- **The forbidden three.** The photo contributes identity ONLY
  — face, hair, accessories, body. Forever forbidden: (1) the
  photo itself becoming a frame of the video; (2) the photo, or
  a still portrait derived from it, becoming the video's first
  frame or opening — the video opens on the concept's action,
  in the concept's location; (3) the photo's own environment or
  atmosphere appearing in the video — the video lives entirely
  in the described scene, never in the reference's setting.
- **Director preamble, verbatim, on every prompt.** Prepend
  this exact text before the prompt body:

  > IDENTITY REFERENCE ONLY: The attached photo is an identity
  > reference ONLY — use it solely to lock the character's face,
  > hair, accessories and body. NEVER reproduce the photo itself
  > as a frame, NEVER open the video on the photo or a still
  > portrait, and NEVER use the photo's background, setting or
  > atmosphere — the video takes place entirely in the scene
  > described below.

  The full prompt is then: preamble + prompt skeleton + the
  character lock verbatim + the concept fill. No generation
  prompt is complete without the preamble.

## Duration

Match the generator, not the wish. If the tool caps near 10
seconds, the video is 8–12 seconds (~9 target) and the beats
are written to fit it — never a 30-second beat map for a
10-second tool. A beat map longer than the tool's cap is a
plan to drop beats.

## What to hand back

- Block A and Block B as two separate copy-paste blocks, each
  labelled with the tool it goes into.
- The reference input named explicitly, and the preamble
  included verbatim.
- The hook-frame gate stated: what a clean frame looks like,
  and what sends it one rung down the ladder.

## Worked example

Aria Fit (the pack's example channel) runs this pipeline for
every Short: a 0.0s hook frame in the gym — peak-action, except
on suspense-question titles, where it is the struggle or
starting position (see the exception above) — then the
video animated from that frame with the Story DNA beats from
`/yt-story` and the QA gates from `/yt-qa`. Aria is the example,
never the only character this skill works for.
