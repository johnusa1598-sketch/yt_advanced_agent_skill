---
name: yt-trends
description: >-
  Find what is currently moving in a niche and turn it into a
  hashtag and keyword pack, from evidence the user supplies. Use for
  "what hashtags", "what keywords", "what is trending", "find tags
  for this video", or before you write a title.
---

# yt-trends

This skill does not fetch live trend data. Nobody in this pack has a
YouTube login, and a tool that claimed to know what is trending
without looking would be inventing it. What it does is two honest
things: a method for finding what is actually moving, and a tool
that turns evidence you paste in into a pack you can use.

## How to find what is currently trending

Do these in order, cheapest first, and stop when the same three
phrases keep appearing from two different places. That repetition
is the trend; a single sighting is noise.

1. **YouTube search and autocomplete.** Type the seed topic and
   read what autocomplete finishes it with. Those completions are
   real queries people typed. Do the same for the two closest
   neighbouring topics.
2. **The trending and explore pages.** Watch what formats recur,
   not what topics: a format that repeats across channels (a
   challenge shape, a fail-then-land shape) is more usable than a
   topic that is already owned.
3. **Competitor Shorts, by multiple, not by views.** Take the last
   ten Shorts of three channels in the niche and rank them by how
   far each beat its own channel's median (`/yt-viral` does this).
   The top two per channel are the working ideas.
4. **Google Trends, for the long view.** A rising query over 90
   days is a season; a spike over 7 days is a moment. Seasons get
   series, moments get one Short, fast.
5. **Your own Studio.** Traffic sources and search terms on your
   last ten videos tell you what your audience already wants from
   you, which beats any global trend list.

Write down what you found, with dates, before you run the tool.
Evidence without a date is how a pack goes stale.

## Building the pack

```bash
python3 trend_pack.py "beam backflip" --niche "AI gymnastics" \
  --brand "Aria Fit" --evidence evidence.json
```

The evidence file is three lists you paste in: `trending_titles`,
`tags_seen`, and `searches`. The tool returns four tiers:

- **Broad** - the big words of the niche, for reach.
- **Niche** - the seed topic and its long-tail combinations, for
  the audience that actually wants this video.
- **Branded** - the channel and series names, so a series compounds
  instead of scattering.
- **Evidence seen** - the hashtags that appeared in what you pasted,
  kept separate so you can see what is sourced and what is guessed.

Every tag the tool did not get from your evidence is marked as a
heuristic in the output. Treat those as suggestions to test, and
re-check them in YouTube search before you trust them.

## Using the pack

- A Short carries **3-5 hashtags**, no more. Pick one broad, two
  niche, one branded. The rest of the pack is for the title and
  the description, not the hashtag line.
- A long video carries up to 15 tags, chosen for disambiguation
  (spellings, tool names, abbreviations people actually type).
  Tags are a weak signal and this pack says so (`/yt-seo`).
- The search-intent clusters in the output are the questions
  behind the queries. Write the title for one cluster, not for
  all of them: a title that tries to answer every intent answers
  none of them well.
- An unrelated tag is not a strategy. It is against the terms,
  and it teaches the algorithm to show the video to the wrong
  audience, who will swipe away and poison the next test.

## Trend-jacking, without the cringe

A trend is usable when it passes three tests: it fits the series
you already make, you can add something to it that is yours, and
you can ship it while it is still moving. If it fails any one of
the three, skip it. Chasing a trend you do not fit costs you the
audience you already have, which is the only audience you can be
sure of.

## The gate

Nothing here publishes. This skill writes and you publish. Every
pack ends with its evidence date and the question: **ship it, or
change it?**
