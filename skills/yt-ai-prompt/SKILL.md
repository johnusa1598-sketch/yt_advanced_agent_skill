---
name: yt-ai-prompt
description: >-
  Write next-level AI video prompts for an AI video channel: a
  7-layer prompt with a locked character, timed action beats,
  camera, motion physics, style, and a negative prompt. Use for
  "write my AI video prompt", "prompt for this Short", "my AI
  character keeps changing", or any AI-generated video brief.
---

# yt-ai-prompt

A one-line prompt makes a one-line video. A next-level prompt is
a system, and this skill is that system. It is hard to copy
because it is not one clever sentence: it is seven layers that
have to agree with each other, plus a negative prompt and a
continuity check.

## Before you write

1. Read the channel profile, the series bible, and the character
   spec first. If there is no locked character spec, write one
   with `/yt-series` before writing a prompt.
2. Read the video brief in `templates/video-brief.md`. A prompt
   without a brief is a guess with better lighting.
3. Never invent a number, a result, or a source. If a figure
   would strengthen it and you do not have one, ask for it or
   write the line without it.

## The 7 layers, in order

1. **CHARACTER LOCK.** Hair, glasses, jewellery, freckles,
   outfit, and setting, word for word, every time. This layer
   never changes between videos in a series, except for one
   planned exception: outfit colour rotation (see below).
   Hair, glasses, jewellery, freckles, and face never rotate.
2. **SCENE LOCK.** Location, props, light, and background, so
   the next clip can be cut next to this one.
3. **ACTION BEATS, TIMED.** Each beat with a time range, a
   motion verb, and a physics rule: weight transfer before a
   jump, knees bending on a landing, hands planting flat,
   balance recovered with arms. AI gymnastics fails on physics
   before it fails on looks.
4. **CAMERA.** Shot type, angle, movement, and cuts. Full body
   for skills, face only for a reaction. Athletic framing only.
5. **STYLE AND LIGHT.** Realistic or stylised, colour, grain,
   and what the look must not become, such as glossy plastic.
6. **LOOP AND HOOK.** The first two seconds and the last line,
   so the Short loops and the title promise is confirmed.
7. **NEGATIVE AND GUARDRAILS.** Extra limbs, distorted hands,
   morphing face, changing glasses or jewellery side, changing
   outfit mid-shot, sexualized framing, text errors, and
   watermarks. The ban is on changing mid-shot — rotation
   across videos is the planned exception (see Leotard colour
   rotation below), not a violation of this layer.

## Clean output

Every prompt must demand a clean render: no watermark, no logo,
no burned-in subtitles or text except the text layers the package
itself specifies. Clean means generated clean, not cleaned after:
never strip another tool's watermark from its output — if the
rendering tool stamps its own mark, use that tool's watermark-free
export instead.

## Format lock — 9:16, shot on iPhone (v3.3.0, every prompt)

This is not a suggestion and not a layer you can swap out. It
applies to every Shorts prompt this skill writes, on top of the
7 layers, and `prompt_builder.py` writes it into every full
prompt, short prompt, and negative prompt automatically:

- **Vertical 9:16 portrait, full frame — 1080x1920
  preferred, 720x1280 at the same ratio passes (v3.3.4).**
  No horizontal 16:9, no letterbox bars, no pillarbox bars,
  no footage cropped from a horizontal shoot. A Shorts feed
  is vertical; cropped horizontal footage reads as lazy and
  wastes the frame. Do not fail a video only for being 720p,
  and do not upscale 720p to fake 1080p.
- **Shot on iPhone.** Handheld smartphone look, natural
  phone-camera optics, slight handheld movement. Not a
  cinematic DSLR or anamorphic look, not a studio-camera
  look. The video must look like it was shot on a phone,
  because that is how the audience shoots and watches Shorts.
- **Hook frame too.** The Step 1 hook-frame image in
  `/yt-production` carries the same lock: 9:16 portrait,
  iPhone look. A horizontal frame cannot become a vertical
  video later.
- **Gate:** a render that is not 9:16, or does not look
  phone-shot, fails `/yt-qa` regardless of its scorecard
  total. Do not ship it and do not "fix" it by cropping.


## Realism core (documented here; enforced by `/yt-qa`)

A prompt that only names the action produces a mannequin. When
the brief calls for a realistic human, the prompt must also
carry the realism core — skin, hair, imperfections, effort,
background, and optics:

- **Skin:** real human skin, never plastic or airbrushed.
  Visible pores, subtle tone variation, light shine on the
  forehead after effort, faint flushed cheeks, natural lip
  texture. A few tiny imperfections are GOOD.
- **Hair physics:** hair obeys real physics — loose strands
  escape and move with momentum, flyaway hairs bounce and
  settle, a bun shifts slightly and resettles. Never glued,
  frozen, or helmet-like.
- **Human imperfections:** micro-wobbles, asymmetry (one
  eyebrow slightly higher, uneven smile), chalk or marks on
  hands and clothing, muscle tension and slight tremor on hard
  moves, natural blinking and gaze refocusing (never a frozen
  unblinking stare), fabric wrinkles at bent joints, grip and
  contact (toes gripping, fingers pressing, surfaces
  compressing), recovery gestures (shake out hands, wipe
  palms, one deep breath).
- **Peak hold wording:** a hold is written as sustained
  effort, never as a state. "She holds the L-sit" lets
  the model rest; write instead: legs locked straight
  at hold height for the whole beat, thighs trembling
  slightly, core braced, jaw set, eyes locked on the
  lens, breath controlled — tension holds until the
  lower. See `/yt-story` peak rule. A neutral face,
  sagging limbs, or eyes squeezed shut at the peak is
  a failed peak, not a clean one.
- **Sweat progression:** dry at the start, hairline dampness
  and shine by the payoff, a quick wipe or shake-out after the
  hardest move. Effort must look HARD — an effortless
  execution in a hard position is an AI tell.
- **Background life:** the location must feel alive, not an
  empty studio — blurred background figures far behind (never
  speaking, never distracting), dust or wear on surfaces, a
  water bottle and towel on a bench. No perfectly clean
  untouched surfaces.
- **Smartphone optics:** shot on a phone — wide-angle lens,
  deep depth of field (everything roughly in focus, no fake
  cinema bokeh), slight auto-exposure shift, occasional subtle
  focus hunting, crisp ambient lighting. The video must look
  phone-shot, not cinema-shot.

The tool's negative prompt already blocks the opposites
(plastic skin, frozen hair, watermark, logo). The realism core
is what the positive prompt must actively ask for.
`prompt_builder.py` writes a [REALISM] paragraph into every
full prompt (v3.3.6) — pores, flyaway hairs, chalk dust,
natural blink, micro-tremor on holds, sweat progression —
so the core is no longer only documentation.
**Audio (v3.3.6):** the prompt's hand-back must also carry
the audio gate — a licence-safe beat track from the first 2
seconds, finished audio −14 LUFS target, true peak at most
−1 dBTP (v3.3.2 supersedes FINAL on music: native audio
alone fails; see `/yt-sound` + `/yt-qa`).

## One action per segment, time-coded beats, negative limits (v3.4.5)

A segment prompt carries ONE subject action plus ONE camera
move — never a multi-beat routine in one generation, or the
generator drops planned beats (see `/yt-qa` segment method).
Write beats time-coded, in order, for example: "0–2s:
descend slowly, camera pushes in; 2–5s: hold at depth,
face tense, eyes open". Slow, controlled motion and
simple framing distort less than fast, complex motion
[LORE — creator guides]. The same rule covers the
peak: a hold is written as sustained effort, never as a
state (see the peak hold wording above and `/yt-story`
peak rule) — and where the tool supports first+last
frames, the peak is also supplied as an end-frame still
(see `/yt-production` end-frame conditioning), not left
to be invented mid-video.

Negative prompts are biases, not guarantees. A negative
line ("no morphing, no flicker, no extra limbs, stable
face, eyes open") can bias the output toward stability,
but it cannot override missing visual information or an
overly complex shot [LORE — stated explicitly in creator
guides]: it cannot invent the far side of a face, hold
an expression the model was never shown, or rescue a
pose change the geometry does not support. Keep the
negative list short, so it does not compete with the
positive prompt — and when a negative keeps failing to
hold a beat, fix the production (end frame, segment,
or edit), not the wording.

## Build it with the tool

```bash
python3 prompt_builder.py brief.json
python3 prompt_builder.py brief.json --json
```

The tool returns a full prompt, a short prompt for quick tools,
a negative prompt, a continuity checklist, and three variants
that keep the character lock and change only camera and motion
emphasis: safe, bold camera, and slow detail. Show the user all
three variants, and let them pick one. Do not merge variants
into a fourth prompt without checking the lock again.

## The difficulty is the system, not the sentence

- A prompt anyone can write says "a gymnast does a backflip".
- A prompt that is hard to copy says which gymnast, in which
  outfit, with which jewellery on which side, from which
  camera, with which weight transfer, which landing
  absorption, and what must never change or appear.
- Keep a prompt library: one locked character prompt, one
  scene prompt per location, and one motion prompt per skill.
  New videos reuse locks and change only beats and camera.
  That is how a channel gets a look nobody can copy by
  typing one sentence.

## Leotard colour rotation (v3.3.3)

Why this exists: a recurring character whose every video
wears the same purple leotard starts to look like one
video repeated. The fix is a planned rotation, not a random
change — the audience must still recognise the character
instantly, because everything except the leotard colour
stays locked.

- **Palette, in fixed cycle order:** purple (anchor, Slot 1),
  teal, black, royal blue, burgundy, then back to purple.
  No other leotard colours unless the plan adds one in a
  dated revision. Purple stays the anchor: it is Slot 1,
  the channel's example colour, and the colour to return
  to whenever a rotation slot is in doubt.
- **One slot per video, planned before generation.** The
  package names the slot ("Slot 2 — teal leotard") before
  the hook frame is made. The hook frame and the video use
  the same slot. Use the tool flag for it:
  `prompt_builder.py brief.json --outfit "teal leotard"`.
- **Never the same colour twice in a row,** and never a
  colour change mid-shot. The negative prompt's ban on
  outfit changing colour mid-shot still stands — rotation
  happens across videos, never within one.
- **Everything else is locked.** Hair, messy bun, gold
  wire-frame glasses, nose ring side, silver hoop earrings,
  freckles, face, and body proportions do not rotate with
  the colour. If any of those change, that is identity
  drift, not rotation, and QA fails it.
- **Log the slot.** The series log records the slot per
  episode (`/yt-series`), so the next video never repeats
  the last colour by accident and the cycle stays in order.
- **Tool enforcement (v3.3.6).** `prompt_builder.py` rejects
  a leotard outfit outside the five colours (exit 2, palette
  named) and warns when no `--outfit` is given and the brief
  falls back to the default purple — the default is how
  "every video purple" recurs. The tool cannot see the
  series log, so the never-twice-in-a-row check stays the
  planner's job, not the tool's.
- **Scope (v3.3.6).** This cycle governs leotard slots. When
  a non-leotard outfit from the channel matrix is chosen
  (for example a top-and-leggings set), record that choice
  in the same series log, so the next video still never
  repeats all four matrix picks from the previous video
  (`/yt-anti-glitch` variety matrix).

## Nose ring side, stated without ambiguity (v3.3.5)

"RIGHT nostril only" on its own is ambiguous to a video
model: it does not say whether RIGHT means the character's
right or the image's right, and when the character turns
her head, a small side ring drifts to the centre or
duplicates (one on the wing, one at the nose tip), as
happened in the October 2026 arabesque video. From now on,
every prompt states it in full, and `prompt_builder.py`
writes it into the character lock, the continuity line,
and the negative prompt:

- **Character's RIGHT nostril wing only** — not the
  character's left, not the image's right.
- **In a frontal view, it appears on the image's LEFT
  side.** That sentence is part of the lock, not a note.
- **Never septum, never centre, never nose tip, never
  two rings.** A centre ring alongside a correct wing
  ring is still a fail, not a pass.
- The negative prompt now bans centre nose ring, nose
  ring on nose tip, and two nose rings, as well as septum
  ring and changing side.
- **Stale briefs cannot weaken the lock (v3.3.6).**
  `prompt_builder.py` canonicalises the nose_ring field: any
  brief that mentions a nose ring gets the full sentence
  above in the character lock, whatever shorter wording the
  brief itself used. A character with no nose_ring field is
  left alone — no ring is invented for them.
- **Aria datasheet lock (v3.3.6).** For Aria Fit, the
  character lock IS the datasheet §8 block verbatim from
  the FINAL template (see `templates/aria-datasheet-lock.md`
  in this pack): freckles LIGHT, fine, scattered on the nose
  bridge and upper cheeks only; body proportions constant,
  never reduced or flattened. The generic lock fields in a
  brief do not replace that block — paste it verbatim.

## Check it before you ship it

- Run the continuity checklist against the draft, frame by
  frame if needed: hair, glasses, nose ring side, earrings,
  freckles, outfit, hands, feet, and landing.
- Run the Short through `/yt-shorts-first` for hook, loop,
  and call to action, and through `/yt-publish` for AI
  disclosure and playlist.
- In text mode the tool now prints all three variants in full
  (v3.3.6), not just their names — read them before picking
  one. The "slow detail" variant is slow, controlled movement
  at normal speed, not a slow-motion effect: the FINAL
  template bans slow motion, so do not use that variant
  for Aria Fit unless the brief explicitly re-approves
  controlled movement.
- If a draft breaks the lock, fix the prompt, not the lock.
  Change the lock only in a dated revision, and say what
  changed.

## What to hand back

- The full 7-layer prompt, in a copy-paste block.
- The short prompt, for tools that take one line.
- The negative prompt, as a separate block.
- The three variants, labelled, with the one you recommend.
- The continuity checklist, with the draft checked against it.

## The gate

Nothing here publishes, and nothing here generates video by
itself. This skill writes prompts and you render and upload.
Every output ends in a block the user copies, and the last line
of every run is the question: **ship it, or change it?**
