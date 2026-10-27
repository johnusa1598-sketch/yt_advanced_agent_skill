---
name: yt-anti-glitch
description: >-
  Keep AI video from glitching: the skill-safety ladder, the only
  banned combos, face-visibility lock, single continuous shot,
  duo separation, variety rotation, title-first, never-retry-denied,
  and the glitch burst rule. Use for "limbs merge", "face morphs",
  "too many glitches", "what skills are safe", or any AI video
  that falls apart on fast motion.
---

# yt-anti-glitch

Glitches are not bad luck. They are a skill too hard for the
tool, a face hidden at the wrong moment, two bodies too close,
or a prompt that asks for a cut the tool cannot make. Fix the
system, not the clip.

## Skill-safety ladder

Safety comes from the pipeline, not from banning skills. Dynamic
skills are allowed. The rule is the hook-frame check from
`/yt-production`: lock the 0.0s frame FIRST. If the frame shows
any glitch — detached limbs, floaty anatomy, face morph,
impossible physics — simplify the skill ONE rung down the
ladder and re-lock the frame. For example: backflip → back
handspring → cartwheel → split jump. Only proceed to video
once the hook frame is clean.

## Banned — multi-axis twisting combos ONLY

Twisting double flips, 360° twisting aerials, and any combined
twist+flip. These genuinely detach limbs. Everything else on
the approved list below is allowed subject to the hook-frame
check. A ban broader than this throws away good videos.

## Approved high-retention skills

Prefer clean, reliably generatable skills: handstand holds
(one-arm or two-arm), balance micro-wobble saves, straddle
L-holds, split drops, explosive box/mat jumps,
cartwheel-to-freeze, split jumps, needle holds, synchronized
balance challenges, and single-axis dynamic skills (backflip,
back handspring, layout — allowed subject to the hook-frame
check). Prefer slow, controlled, readable skills over fast
complex rotations: unreal movement is the biggest AI tell.

## Face-visibility lock

The lead's head must never pass behind their arms or knees
during the main action. Keep the camera at a 30-to-45-degree
front-diagonal so glasses, jewellery, and face stay anchored
without morphing. A face hidden behind motion blur, hair,
equipment, or an extreme angle is a fail, not a style choice.

## Single continuous shot

Never prompt for cuts, whip-pans, or camera angle switches
mid-video. One continuous handheld shot with subtle breathing
sway and a smooth pinch-zoom on the payoff. The "cinema" look
— shallow depth of field, polished separation — is an AI
tell; the phone look (wide angle, deep depth of field, ambient
light) is the cover.

## Separation rule for duos

Keep 15–20 cm visual separation between two characters during
fast moves. Use rapid fist-bumps or quick single-hand taps
instead of complex overlapping hugs or grapples — overlapping
bodies merge limbs. Never swap the two characters' outfits,
hairstyles, or accessories. A duo's lowest-glitch role is
off-camera POV: voice plus a hand entering for a fist-bump
only.

## Variety rotation matrix

Pick one from each per video — never repeat all four from the
previous video:

- **Outfit:** rotate the lead's outfits (a fixed list per
  channel; a classic competition outfit may be one option).
- **Location zone:** rotate the set or zone.
- **Co-star role:** motivator / challenger / partner /
  off-camera POV — duo is the default, solo only as the
  exception, capped per week by the channel's own rule
  (Aria Fit: 2–3 solo Shorts per week, Mia the default
  co-star). Record the solo count in the series log with
  the rotation slot.
- **Camera style:** handheld tracking / static tripod-style /
  slow push-in.

Rotation is variety, not originality: the skill itself must
still be new (see `/yt-originality`).

## Title-first gate

Write the title before generating anything. The title locks
the hook; the concept, hook frame, and video serve it. Record
it before Step 1. A useful shape is skill + stake/number
("Straddle L-Hold — Can She Hold It?!"), but the hook matters
more than the shape.

**Question–skill match (v3.4.4, checked at this gate,
before Step 1).** The question type must match the skill
type, or the concept is invalid — change the question or
change the skill, do not generate:
- Range questions ("HOW LOW?", "HOW HIGH?", "HOW FAR?")
  need a PROGRESSIVE skill: a visible journey from
  start to peak (a descent, a lift, an extension). The
  answer must unfold across the video, never sit in
  frame 0.
- Duration questions ("CAN SHE HOLD IT?", "HOW LONG?")
  take a STATIC hold: the hold itself is the content,
  and the stake is time, not range.
- A static hold paired with a range question FAILS
  this gate. Precedent: Part 11 paired "HOW LOW?" with
  a deep squat hold — the deepest squat sat in frame
  0, the body never progressed, and the video was one
  pose for 10 seconds. The same footage under "CAN
  SHE HOLD THIS SQUAT?" would have passed: same
  skill, matched question.

## Never-retry-denied rule

If the generation tool denies a request (an outfit, a skill,
a concept), NEVER retry it — not reworded, not the next day
as the same request. Fall back: switch the concept to one
within the tool's proven competence, or use the emergency
backup. A denial is the tool stating a boundary; retries
waste the day's budget and teach nothing.

## Glitch burst rule

If TWO consecutive generations for the same day/concept fail
on glitch or identity grounds (melted or fused limbs/fingers,
a blacklist hit, face unverifiable, identity drift), that is
a GLITCH BURST:

1. STOP generating that concept immediately — no third
   attempt, no reworded retry.
2. Switch the concept (a different skill within the
   generator's proven competence) or use the emergency backup.
3. Record the burst with the failing artifacts, and one line
   in the improvement ledger.

A burst is the generator declaring the concept outside its
competence today; more attempts make worse videos, not better
ones.
**Counting (v3.3.6):** the count is shared. A failed hook
frame in `/yt-production`, a failed segment regen, and a
face-gate regen in `/yt-qa` all count toward the same two
consecutive fails — the "regenerate once" allowances in those
skills are not extra attempts on top of the burst.

## What to hand back

- The skill placed on the ladder, and the one rung down if the
  hook frame glitches.
- The banned check: is this a multi-axis twisting combo? If
  yes, it does not get made.
- The face, shot, separation, rotation, and title-first
  checks, each passed or failed by name.
- On a burst: the stop, the switch, and the ledger line — not
  a third attempt.
