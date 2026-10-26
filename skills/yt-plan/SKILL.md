---
name: yt-plan
description: >-
  Plan a week or a month of YouTube uploads - what to post, when, and in
  what order, sized to the creator's actual capacity. Use for "plan my
  week", "content calendar", "what should I post", "I have no idea what to
  make next".
---

# yt-plan

A plan that does not fit the week is a list of regrets. Ask two questions before writing anything:
**how many hours do you actually have**, and **what is already half-made**.

## Before you write

1. Read the channel voice profile (`templates/voice.md`) if it exists, or `~/.claude/youtube/voice.md` on Claude Code. That is the user's voice profile: how they talk
   on camera, the words they never use, who they are talking to, what they will not claim. If it
   does not exist, ask for **three of their own videos**, read or transcribe them, infer the voice,
   and write the file. A script in the wrong voice is worse than no script, because they have to
   read it out loud.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have
   one, ask for it or write the line without it.

## First question: what cadence?

Ask the cadence before writing anything, and never prescribe
one cadence for every channel. The old rule in this skill —
three uploads a week, never daily — was wrong for a daily
Shorts channel, and v3.3.0 removes it.

- **Daily Shorts mode.** One Short a day (see `/yt-shorts-first`),
  plus one anchor long video a week if the channel makes
  long-form at all. The daily Short IS the plan, not a
  failure of it. The buffer is a bank of ready Shorts, not
  empty days.
- **Weekly mode.** One anchor, one cheap one, and three Shorts
  from the anchor (see `/yt-shorts`).

## The shape of a week

- **One anchor.** The video the week is for. It gets the most time and it goes out on the day the
  channel's own analytics say is best - ask for that, do not assume Tuesday.
- **One cheap one.** Built from something that exists: a clip, a reaction, a follow-up to the
  comment that got the most replies last week.
- **Shorts.** In daily mode, one Short a day, written separately
  for the Short itself. In weekly mode, three Shorts cut from the
  long video, not written separately. `/yt-shorts` finds them.

A plan that does not fit the week is a list of regrets — and
a plan that forbids daily posting on a daily Shorts channel
is a plan that does not fit its channel.

## What to hand back

A table: day, format, working title, the one sentence it promises, and what already exists for it.
Then the honest line at the bottom - how many hours this costs, and what to drop first if the week
goes wrong.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
