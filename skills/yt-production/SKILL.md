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
3. **Step 2 — video from the frame.** Feed the Step 1 frame as
   the starting frame into the video tool. The video prompt
   directs only realistic motion, audio, and the loop back to
   frame 1. It invents nothing new about who or where.
4. **Gate before Step 2.** If the hook frame shows any glitch —
   a centre, septum, or nose-tip nose ring (v3.3.5),
   detached limbs, floaty anatomy, face morph, impossible
   physics — do NOT proceed. Simplify one rung down the
   skill-safety ladder (see `/yt-anti-glitch`) and re-lock the
   frame first.
   **Nose gate, full rule (v3.3.6):** the ring must be on the
   character's RIGHT nostril wing only (frontal view: image
   LEFT), and the side is checked on a FRONTAL frame only —
   a 30–45° diagonal action frame cannot settle side vs
   centre. A centre, septum, or nose-tip ring FAILS, and a
   second centre ring alongside a correct wing ring also
   FAILS — that second ring was the exact arabesque defect
   (v3.3.5), and this gate exists to catch it before the
   video is generated, not after.
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
