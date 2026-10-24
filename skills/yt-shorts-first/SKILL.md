---
name: yt-shorts-first
description: >-
  Make a Shorts-first channel work: a daily Short that survives on its
  own, with a first-two-seconds hook, a loop point, one call to action,
  and a series it belongs to. Use for "make a Short", "daily Shorts",
  "Shorts idea", "why did this Short flop", or a Shorts-only channel.
---

# yt-shorts-first

The original pack treats Shorts as cut-downs from a long video. A
Shorts-first channel has no long video to cut from, so this skill
starts from the Short itself.

## Before you write

1. Read the channel profile in `templates/channel.md` if it exists,
   and the series bible in `templates/series.md`. A Short that does
   not belong to a series is a one-off, and one-offs do not compound.
2. Read `~/.claude/youtube/voice.md` if it exists, or the Muse
   equivalent in the channel folder. If it does not exist, ask for
   three of their own videos and write it first.
3. Never invent a number, a result or a source. If a figure would
   strengthen it and you do not have one, ask for it or write the
   line without it.

## The shape of one Short

- **First two seconds.** Show the hardest moment, the fail, or the
  question. No greeting, no channel intro, no setup.
- **One idea only.** A Short that tries two skills is two Shorts,
  and the second one is the one people leave on.
- **A turn in the middle.** A claim, then something that complicates
  or proves it. Without a turn the viewer has no reason to stay.
- **A loop point.** The last line must set up the first line, so a
  rewatch feels like a continuation, not a repeat.
- **One call to action.** Not three. Name the next video, the poll,
  or the series, and stop.

## Score it before you ship it

```bash
python3 shorts_score.py --title "..." --thumb "..." --hook "..." \
  --loop yes --cta "follow for part 2" --series "Skill Challenge"
```

Fix the weakest check first. The score is a checklist, not a
predictor: a high score is not a promise, and a low score is a
reason to rewrite.

## Character and AI honesty

- When a recurring AI character is used, keep one locked spec:
  hair, glasses, jewellery, freckles, outfit, and setting. Write
  it in the series bible and check every new brief against it.
- When visuals or sounds are AI generated, mark the AI disclosure
  in the publish checklist. Do not hide it and do not claim a
  real performance that did not happen.
- Check hands, arms, and landings in the draft before publishing.
  An anatomical glitch is a trust glitch, and trust is what turns
  a view into a subscriber.

## AI video prompt, injected here

For an AI video channel, do not stop at the idea. Run the
brief through `/yt-ai-prompt` and build the 7-layer prompt
with `prompt_builder.py`: character lock, scene lock, timed
action beats with physics, camera, style, loop, and a negative
prompt. A Short idea anyone can write is not the product.
The locked prompt system, with continuity checks, is.

## What to hand back

- The Short idea in one sentence, the series it belongs to, and
  the first line.
- The full AI video prompt, the short prompt, and the negative
  prompt, when the video is AI generated.
- On-screen text for the first two seconds, different words from
  the spoken line.
- The loop point and the single call to action.
- The title and thumbnail pairing, checked with
  `../yt-package/title.py`, and the shorts score.

## The gate

Nothing here publishes. This skill writes and you publish. Every
output ends in a block the user copies, and the last line of every
run is the question: **ship it, or change it?**
