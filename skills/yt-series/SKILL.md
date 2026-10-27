---
name: yt-series
description: >-
  Run a series and a recurring character without repeating yourself:
  a series bible, a character spec, and an episode log. Use for
  "start a series", "my character keeps changing", "what should I
  post next in this series", or "we already did that".
---

# yt-series

A series is a promise the viewer can follow. A character that
changes every video is a new channel every video.

## Before you write

1. Read `templates/series.md` and `templates/channel.md` if they
   exist. If they do not exist, write them from the last ten
   videos before writing a new episode.
2. Never invent a number, a result or a source. If a figure would
   strengthen it and you do not have one, ask for it or write the
   line without it.

## The series bible

For each series, name in one file:

- The promise: what the viewer gets every time, in one sentence.
- The format: the fixed beats, the length, and what never changes.
- The rotation: how episodes vary without breaking the promise.
- The end of an arc: how many episodes, and what the finale is.

A series with no finale is a treadmill. Plan the finale when you
plan episode one.

## The character spec

For a recurring character, lock in one file, and check every brief
against it:

- Hair, face, glasses, jewellery, freckles, and other marks.
- Outfit and colours, and what never changes about them.
  For a leotard rotation (`/yt-ai-prompt` v3.3.3), the log
  also records the colour slot per episode, in cycle order,
  so no colour repeats twice in a row. A non-leotard outfit
  from the channel matrix is logged in the same log, so the
  next video still never repeats all four matrix picks from
  the previous video (v3.3.6).
- Setting, camera framing, and tone.
- What the character never does and never claims.

When a new draft breaks the spec, fix the draft, not the spec.
Change the spec only in a dated revision, and say what changed.

## The episode log

Keep one line per episode: date, series, title, views, likes, and
the one thing that made it different. Before proposing a new
episode, read the log and reject any idea already done in the
last ten episodes unless it is a deliberate sequel.

## Character spec becomes a prompt lock

The character spec is not only a bible entry. It is layer one
of every AI video prompt in `/yt-ai-prompt`. Paste the spec
unchanged into `prompt_builder.py`, and check every new
prompt against it. When a prompt changes the spec, the prompt
is wrong, not the spec.

## What to hand back

- The series bible entry, or the dated change to it.
- The prompt lock derived from the character spec, when the
  series uses AI video.
- The next three episode ideas in that series, each different
  from the last ten, with the one sentence each promises.
- The character spec check for the chosen episode.

## The gate

Nothing here publishes. This skill writes and you publish. Every
output ends in a block the user copies, and the last line of every
run is the question: **ship it, or change it?**
