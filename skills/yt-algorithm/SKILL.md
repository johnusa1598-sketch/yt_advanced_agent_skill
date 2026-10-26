---
name: yt-algorithm
description: >-
  A working model of how YouTube ranks Shorts and long-form videos,
  and how to check each part of it against your own channel's numbers.
  Use for "how does the algorithm work", "why did this flop", "what
  should I optimise", Shorts shelf behaviour, CTR vs retention, or
  before you package a video.
---

# yt-algorithm

This is a **working model**, not an official specification. YouTube
does not publish its ranking formula, and anyone who quotes you exact
thresholds or percentages for it is inventing them. What follows is
assembled from YouTube's own public creator guidance and from behaviour
creators can observe in Studio - and every claim in it comes with the
check that would prove or break it on your channel.

## The model in one paragraph

YouTube ranks a video by how satisfied the viewers it shows it to
seem, and by whether showing it keeps the viewer watching YouTube.
Two things carry almost everything: whether people click when they
see it, and whether they stay once they do. A video that gets clicks
and loses people teaches the system to stop showing it; a video that
gets fewer clicks but holds everyone teaches it to keep showing it
to a narrower, better audience. Everything else - tags, descriptions,
upload times - matters only through those two.

## Shorts and long-form are different games

**Shorts.** A Short is offered to a small test audience first, in the
Shorts feed. The first signal is the swipe: did people stay, or swipe
away in the first seconds? A Short that survives its first audience
gets a wider one; one that gets swiped away stops. Because a Short is
short, the loop matters more than in long-form: a viewer who watches
twice counts as a viewer who stayed, and the end of the Short is
also its next beginning (`/yt-viral-loop` plans this).

**Long-form.** A long video lives on browse, suggested, and search at
the same time, and each traffic source judges it differently. Browse
and suggested reward click and session: did this video start or
extend a viewing session? Search rewards the match: did the viewer
who typed the query stay and get the answer? One video can be right
for one source and wrong for another, which is why a video's traffic
sources matter more than its total views.

## The signals, and how to validate each one

| Signal | What it means in practice | Check it in Studio |
| --- | --- | --- |
| Click-through | Of the people shown the title and thumbnail, how many clicked. A packaging problem, not a video problem. | Reach tab, impressions CTR, against your channel's own median (`/yt-analytics`). |
| Average view duration and retention | How much of the video people actually watched, and where they left. The curve, not the average, tells you what to fix (`/yt-retention`). | Engagement tab, retention curve, first-30-seconds leak. |
| Swipe-away (Shorts) | How many viewers left in the first seconds. The Shorts equivalent of a hook leak. | Shorts analytics: viewed vs swiped away. |
| Session | Whether the viewer watched something else after this video, on your channel or on YouTube at all. | Traffic sources, suggested traffic, end-screen click rate. |
| Search match | Whether the query's intent matches what the video delivers. | Search traffic terms against the title and first two description lines (`/yt-seo`). |
| Returning viewers | Whether the same people come back. A series compounds here (`/yt-series`). | Audience tab, returning vs new. |

Never compare your numbers to a global benchmark you read in a blog
post. Compare them to your own channel's median over the last ten
videos in the same format. A "bad" CTR on a channel whose median is
lower is a good video being misjudged.

## The validation protocol

1. Pick **one** signal to move per video. Change the title and the
   hook in the same video and you will never know which one worked.
2. Before you publish, write down the prediction: "this title should
   lift CTR, this hook should hold the first 3 seconds" (`/yt-post`
   writes both into the package).
3. After 48 hours, read the video against its format median, not
   against your best video. Record the result in the series log.
4. A signal that moves in the predicted direction twice is a rule for
   your channel. A signal that does not is a property of the video,
   not of the model - say so and move on.

## 2026 warnings: read the numbers right

**View redefinitions - do not compare raw views across these
dates.** On 31 March 2025, a Shorts view started counting at
play or replay start, with no minimum watch time; the old
stricter definition survives as **engaged views**. On 24 August
2026, the same first-frame definition extended to long-form,
podcasts, and live. CTR, average view duration, and retention
are still calculated on engaged views, recommendations are
unchanged, and YPP eligibility and earnings still run on
qualified and engaged views. In one partner example, only about
56% of public Shorts views were engaged views. The practical
rule: compare CTR, retention, and engaged views across the
boundary, never raw public views.

**Made on YouTube, September 2026 - tools to use, not to copy.**
Ask Studio draft feedback on pacing, structure, and
storytelling; Insights and Research destinations; channel-matched
and dynamic thumbnails (best of three by audience segment);
coming video A/B testing of up to three cuts, starting with the
hook; an Ask Studio background thumbnail refresh for older
videos; conversational Gemini editing in Shorts and Create;
opt-in AI comment moderation; and voice and face likeness
detection. A file-based pack teaches you how to use and verify
these Studio outputs - keep the human packaging decision, log
the test result (`/yt-test`) - rather than duplicating them.

**Auto-dubbing, February 2026.** Available to all creators,
27 languages, Expressive Speech in 8 (see `/yt-sound` for the
review checklist). For a visual niche it matters for coaching
voiceover and for multi-language titles, descriptions, and
thumbnails - and every dub gets reviewed for mistranslated
safety cues.

**Satisfaction, stated carefully.** Several 2026 guides claim
satisfaction signals now sit above raw watch time, and one
claims a February 2026 YouTube confirmation. That confirmation
was **not independently verified from an official source** in
the research behind this pack, so this skill phrases it as
"satisfaction-weighted" rather than as a confirmed hierarchy
change. The Studio check is the same either way: post-watch
surveys, like and comment sentiment, return-viewer rate, and
session continuation, against your own median.

## 2026 signals update, 26 October 2026 research (v3.2.0)

Full notes, with sources, in `references/2026-signals.md`.
Nothing there is an official YouTube threshold; every range
is third-party orientation, and your own channel median
overrides it.

- **Shorts first gate is viewed vs swiped away.** Reported
  healthy range roughly 70–90%, below about 60% distribution
  reportedly collapses. Diagnose in order: big first-3-second
  leak = hook problem; healthy VVSA but low completion =
  promise or body problem.
- **Hook formula:** statement in the first 3 seconds, then a
  proof point, then a promise, all in 8–12 seconds. Five
  patterns: visual disruption, face and voice, unexpected
  visual, rapid scene change or beat, text curiosity.
- **Pacing:** a visual change every 2–4 seconds, captions
  that reinforce the hook, a loop whose final frame continues
  the opening frame (a retention spike above 100% at second 1
  is the Studio sign it works), and one CTA placed in the
  payoff, not a long end-card.
- **Length orientation:** 20–35 seconds most-cited for 2026;
  under 15 gives the system little signal, over 45 makes the
  retention maths much harder.
- **Frequency:** Metricool's 2026 study finds per-post views
  highest at 2–4 Shorts per week, but monthly totals climbing
  with volume. Rule unchanged: post as often as quality
  holds, timing from your own Audience heatmap, never from a
  generic best-time table.

## What this model does not claim

- No exact ranking weights, no percentage thresholds, no "the
  algorithm boosts X for Y hours". Those numbers are not public.
- No promise that a high-scoring package will go viral. The model
  improves the odds a video gets a fair test; it does not control
  the test.
- No scraping, no botting, no engagement tricks. Anything that
  fakes a signal poisons the audience the system learns for you.

## The gate

Nothing here publishes. This skill writes and you publish. Every
algorithm pass ends with one prediction to test and the question:
**ship it, or change it?**
