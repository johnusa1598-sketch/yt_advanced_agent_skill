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
