---
name: yt-analytics
description: >-
  Read a channel's own numbers and name one fix: views, like rate,
  subs per 1000 views, format averages, and outliers over the
  channel median. Use for "why is growth slow", "what is working",
  "analyse my channel numbers", or a pasted list of videos with
  views and likes.
---

# yt-analytics

Views without subscribers is a different problem from no views
at all. This skill separates the two before it recommends anything.

## Before you write

1. Ask for numbers you do not have. Do not invent views, likes,
   or subscriber counts, and do not read them off a thumbnail.
2. Put the numbers in one JSON list first, one object per video,
   with title, views, likes, date, and format when known.

```bash
python3 analytics.py videos.json --subs 92 --json
```

## What to read, in this order

1. **Subs per 1000 views.** Total subs divided by total views,
   times 1000. Under 1 is a conversion problem, not a reach
   problem: people watch and do not follow.
2. **Format averages.** Which format averages most views, and
   which averages least. A format 1.5 times the channel average
   is the next three uploads, not a new experiment.
3. **Outliers over the median.** A video 3 times its own channel
   median is worth studying. A video on a big channel with big
   views is not, on its own, an idea.
4. **Like rate.** Likes divided by views. A high-view, low-like
   video was curiosity, not satisfaction.
5. **The shape over time.** Daily uploads with no gaps are a
   strength. A gap, a format change, or a title change on the
   same week as a drop is a clue, not proof.

## What to hand back

- The single biggest fix, named, with what to do this week.
- The best format, the worst format, and the top five videos
  with their multiples over the median.
- What NOT to do yet, and why.
- The numbers you used, so the user can check them.

Never open with praise you do not mean, and never end with a
list of twenty things. If the numbers say the video is fine and
the problem is packaging, send them to `/yt-package`.

## The gate

Nothing here publishes. This skill writes and you publish. Every
output ends in a block the user copies, and the last line of every
run is the question: **ship it, or change it?**
