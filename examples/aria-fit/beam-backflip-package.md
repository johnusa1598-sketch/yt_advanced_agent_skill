# Worked example: one AI Short, raw idea to algorithm-tuned package

Channel: Aria Fit (AI gymnastics Shorts). Character lock: curly dark
hair in a big messy bun, thin GOLD wire-frame glasses, SMALL gold
nose ring in the RIGHT nostril only, SMALL silver hoop earrings,
light thin freckles, purple leotard. The full AI prompt for this
video is built from `ai-brief.json` by `prompt_builder.py`; what
follows is everything that happens after the prompt.

Inputs: `package-brief.json` (the brief) and `trend-evidence.json`
(three trending titles, four tags, three searches pasted in by hand
on 24 October 2026). Every tool output below is the real output of
the v3 tools on those inputs, not a hand-written ideal.

## 0. Raw idea

Aria does a beam backflip and sticks the landing.

## 1. Algorithm pass (yt-algorithm)

One prediction to test, written before publish: this Short should
move **swipe-away in the first 3 seconds** (the hook is a question
the landing answers) and **rewatch via the loop** (the last line
sets up a harder attempt). Judged after 48 hours against the
channel's own Shorts median, not a global benchmark. If the hook
holds but the loop does not, the next brief changes the loop line
only - one variable per video.

## 2. Trends pack (yt-trends)

Built by `trend_pack.py` from the pasted evidence. Tags from the
evidence are marked; the rest are heuristics from the seed topic.

- Broad: #ai #gymnastics #shorts #viral #fyp
- Niche: #beambackflip #beambackfliptutorial #beambackflipchallenge
  #beambackflipfail #beambackfliptips #beambackfliptraining
  #beambackflipskills
- Branded: #ariafit #aria #fit
- Evidence seen: #gymnastics #shorts #beam #gymnast
- Search-intent clusters: how to beam backflip / beam backflip
  challenge / beam backflip fail or win / best beam backflip /
  beam backflip vs beginner / beam backflip trend
- Ship line (3-5 hashtags on the Short): #ariafit #beambackflip
  #beambackflipchallenge #beambackflipfail #gymnastics

## 3. Sound brief (yt-sound)

Energy: building (attempts, then a payoff), so 95-120 BPM, rising
toward the landing, full only on the landing itself. Source:
YouTube Audio Library first, licence noted per track; the series
keeps one signature loop across episodes. Loop point: the last
beat lands on the last frame and picks up the first frame cleanly
- tested by watching the Short twice back to back with sound on.

## 4. Meme slot (yt-meme)

One slot, at the middle turn, not the hook and not the loop: after
the launch, a reaction caption over the airborne frame - "WAIT
FOR IT" - two words, bold sans, high contrast, centre, 1-2
seconds, sound effect on the cut. The joke is built from Aria's
own footage, not lifted from another creator.

## 5. Package (yt-post)

Built by `package_builder.py` from the brief plus the trends pack.
Titles are drafts to pick from, not orders.

Titles (with CTR reasoning):

1. "I tried the beam backflip clean - only 1 landing stuck"
   (54 chars) - contrast + specificity
2. "Can she land the beam backflip clean?" (37 chars) - open
   question up front
3. "beam backflip clean in one take - no cuts" (41 chars) -
   front-loaded subject
4. "She fell twice before this beam backflip clean" (46 chars) -
   failure first
5. "Watch the landing, not the flip - beam backflip clean"
   (53 chars) - curiosity gap
6. "Skill Challenge: the beam backflip clean that took all
   week" (59 chars) - series frame

Pick: title 2 for a cold audience (the question is the click),
title 6 for the series audience (the frame is the click).

Thumbnail brief: text "LAND IT?", the hardest moment frozen
mid-action, one face, one reaction, no clutter. The thumbnail
words differ from the title words, so the pairing carries twice
the information.

Description (first two lines are the search snippet):

> I tried the beam backflip clean - only 1 landing stuck. Did
> she land it?
>
> Aria Fit - Skill Challenge
> For gymnastics fans, 13-25.
>
> #ariafit #aria #fit #beambackflip #beambackfliptutorial
> #beambackflipchallenge #beambackflipfail #beambackfliptips

Tags: beam, backflip, clean, landing, skill, challenge, ai,
gymnastics.

Text layers (5 words on screen at most, bold high contrast):

- [0-3s] Aria mounts the beam, eyes
- [3-8s] She runs two steps, springs,
- [8-14s] Backflip over the beam, tucked
- [14-20s] Clean landing on the mat,
- [20-26s] Slow-motion replay of the landing
- [26-30s] Harder one next - follow

End screen CTA: follow for part 2. Pinned comment: "Which part
was hardest - the flip or the landing? Tell me and I will film
Skill Challenge around your answer."

Upload timing: check Studio -> Analytics -> Audience for when
Aria Fit's viewers are on; default late afternoon to early
evening, series day, if there is no data yet.

A/B test: title 2 vs title 6, thumbnail held constant, judged
on click-through in the first 48 hours against the channel's own
median, kept only if average view duration holds.

## 6. Retention plan (yt-viral-loop)

Built by `retention_plan.py` from the same brief. Flags: none -
the plan has no mechanical holes.

- Hook (0-3s): "Did she land it?" - visible in the first
  frame, names the stakes, ends on an open question.
- Beats: mount (hook), run-up (setup), flip (setup), landing
  (setup), replay (setup), harder-next (payoff/loop).
- Guards: a mid-turn before the halfway mark; the loop point
  in the last 2 seconds; a rewatch trigger that is visible, not
  explained - the landing itself.
- After publish: compare this plan with the Studio curve and
  `retention.py`, and carry the one fix into the next brief.

## 7. Publish check (yt-publish)

Last, always: AI disclosure on (the visuals are AI generated),
playlist Skill Challenge, end screen set, pinned comment ready.
Then you upload. Nothing in this pack publishes for you.
