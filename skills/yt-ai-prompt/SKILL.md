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
   never changes between videos in a series.
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
   outfit, sexualized framing, text errors, and watermarks.

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

- **Vertical 9:16 portrait, 1080x1920, full frame.** No
  horizontal 16:9, no letterbox bars, no pillarbox bars, no
  footage cropped from a horizontal shoot. A Shorts feed is
  vertical; cropped horizontal footage reads as lazy and
  wastes the frame.
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

## Check it before you ship it

- Run the continuity checklist against the draft, frame by
  frame if needed: hair, glasses, nose ring side, earrings,
  freckles, outfit, hands, feet, and landing.
- Run the Short through `/yt-shorts-first` for hook, loop,
  and call to action, and through `/yt-publish` for AI
  disclosure and playlist.
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
