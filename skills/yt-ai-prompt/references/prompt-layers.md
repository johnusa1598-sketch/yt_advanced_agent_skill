# Prompt layers, reference

Use this file when a prompt needs more than a first draft. Each
layer answers one question, and a prompt that skips a layer
leaves that question to the generator, which is how characters
change and landings break.

## Layer 1, character lock

Write the character once, in the series bible, and paste it
unchanged into every prompt. Include hair, glasses, jewellery
with side, freckles, outfit, and age band when relevant. Never
write "same girl as before" without the spec: a generator has
no memory of before unless the prompt carries it.

## Layer 2, scene lock

Location, floor, props, background people or no people, light
direction, and time of day. A scene lock is what makes two
clips cut together. Change one element and say so, or the
next clip will be a different gym.

## Layer 3, action beats and physics

Time each beat. For gymnastics, name the contact points:
hands on the beam, feet on the mat, hips over the hands.
Name the transfer: run, spring, rotate, land, absorb. Name
the recovery: arms out, knees bent, eyes forward. This layer
is the difference between a skill and a blur.

## Layer 4, camera

Shot size, angle, movement, and cut policy. A flip needs a
full-body shot and, ideally, no cut during the rotation. A
reaction needs a face shot after the landing, not during it.
Never ask for a camera angle that sexualizes an athlete:
that is a guardrail failure, not a style choice.

## Layer 5, style and light

Realism level, colour palette, grain, and motion blur. Say
what the look is not: not glossy, not cartoon, not over
smoothed. AI video drifts glossy unless the prompt forbids it.

## Layer 6, hook and loop

First two seconds: the hardest moment or the question.
Last line: the setup for the first line. A Short without a
loop is a video that ends. A Short with a loop is a video
that replays.

## Layer 7, negative and guardrails

List what must not appear, in the negative prompt, not in
the main prompt. Extra limbs, distorted hands, morphing
face, changing jewellery side, changing outfit, sexualized
framing, text errors, watermarks. Check the draft against
this list, not against your memory of it.

## Prompt library

Keep three reusable blocks: character lock, scene lock per
location, and motion block per skill. A new prompt is then
locks plus beats plus camera, which is fast to write and
hard to copy, because the locks took ten videos to earn.
