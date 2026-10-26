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

## Face-crop QC

Extract a 200–300% zoomed face crop from the clearest
face-visible frame and verify, line by line: the locked
accessories present and on the correct side, glasses frames
correct, freckle or skin-marking weight correct, hoop or
earring size correct. Every concept must include at least ONE
face-visible beat (lens grin, close-up, upright pose) so
verification is possible. A video with no verifiable face
frame scores 0 on identity (see the scorecard).

## Ten-point scorecard (the verdict)

Score every prepped video out of 10:

- Identity & character match: 0–3
- Movement realism (no glitch, no float, real effort): 0–3
- Phone-look (single handheld phone shot, ambient light,
  no cinema bokeh): 0–2
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

## Face gate (hard gate — not a score)

A video may ship only if at least one frame yields a
200–300% face crop on which the locked accessories verify.
If NO such frame exists:

- QA marks the video FAIL automatically — not merely a low
  identity score. Regenerate the face-visible segment ONCE
  within the day's fix budget; if it still fails, the day's
  fallback applies (concept switch / emergency backup).
  Nobody has to "catch" it — the gate fails it by itself.
- The same gate applies to the published video on review:
  face unverifiable = identity HARD FAIL.

Every concept must therefore guarantee a face-visible beat —
a concept that cannot show the character's face cannot be
planned.

## Format gate (hard gate — not a score, v3.3.0)

Same status as the face gate. A video that is not vertical
9:16 portrait (1080x1920, full frame) or does not look shot
on iPhone — horizontal, letterboxed, pillarboxed, or cropped
from horizontal footage — FAILS, regardless of its scorecard
total. Do not ship it, and do not "fix" it by cropping a
horizontal render. Re-generate with the format lock from
`/yt-ai-prompt` (vertical 9:16, shot on iPhone) and re-run QA.

## What to hand back

- The segment list with each beat marked present or missing.
- The face-crop verdict: verified, or gate FAIL.
- The scorecard: four sub-scores, total, and PASS or FAIL
  against the threshold, with the exact fix for a failure
  (which segment to regenerate, or the fallback).
- Nothing ships on a FAIL. A good-looking output does not
  override a gate.
