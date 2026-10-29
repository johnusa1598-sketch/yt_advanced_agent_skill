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
opt-in AI comment moderation; and face likeness detection.
Speaking-voice likeness detection was announced on 23 September
2026 for later in 2026, not yet live at the time of writing —
earlier pack wording that listed "voice and face" detection as
current was wrong (v3.3.6 correction). Enrolment in likeness
detection opened to all creators aged 18 and over in May 2026
and is not retroactive; since August 2026 disputes run in four
categories with no revenue-sharing option. Those last two
details are trade-press reporting, not verified Help text —
check Studio before acting on them. A file-based pack teaches
you how to use and verify these Studio outputs - keep the
human packaging decision, log the test result (`/yt-test`) -
rather than duplicating them.

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
  reportedly collapses (v3.4.5: both figures are
  third-party lore, not YouTube rules — no VVSA threshold
  is published). Diagnose in order: big first-3-second
  leak = hook problem; healthy VVSA but low completion =
  promise or body problem.
- **Aria Fit channel benchmark (v3.5.0, user Studio data,
  October 2026 — channel data, not a YouTube rule).**
  Channel average viewed vs swiped away 59.8%; top Shorts
  68–73%. The average sits below the reported healthy
  range above; the top videos sit just under it.
  Working target for a new Short: 68%+ viewed vs swiped
  away. The gap between the average and the top is the
  opportunity — it is a hook and first-2-seconds gap,
  not a topic gap, because the same channel already
  reaches 68–73% on its best hooks. Diagnose a Short
  under 60% as a hook failure first, whatever its
  topic; a Short at 68%+ with low completion is a
  body/promise problem, not a hook problem.
- **Diagnostic stayed bands (v3.5.2, user-supplied Studio
  data, October 2026 — channel data, not a YouTube rule).**
  Under 50% stayed = plateau zone: reach caps around
  1,000–2,000 views, whatever the topic. 65%+ stayed =
  breakout zone: the Short has cleared the first gate and
  can reach 6,000–16,000+. Between 50% and 65% is the
  contestable middle — fix the first 0.5 seconds first
  (see /yt-shorts-first), then the middle beats. A Short
  under 50% is never a packaging problem first; it is a
  hook problem first.
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
  retention maths much harder — for recorded and edited
  Shorts. For AI-generated Shorts the hard budget is 8–12
  seconds (about 9 target) per `/yt-production`; a longer
  concept is decomposed into segments, never stretched into
  one beat map.
- **Frequency:** Metricool's 2026 study finds per-post views
  highest at 2–4 Shorts per week, but monthly totals climbing
  with volume. Rule unchanged: post as often as quality
  holds, timing from your own Audience heatmap, never from a
  generic best-time table.

## v3.3.1: retrieval vs ranking — what YouTube-DNN-RecSys adds (26 October 2026)

Source: chenxingqiang/YouTube-DNN-RecSys, an implementation of
Covington et al. 2016, "Deep Neural Networks for YouTube
Recommendations". Read as a working model, not as YouTube's
current system. The repo itself is only a candidate-generation
demo (last 5 watched videos averaged into a user vector, 16
continuous features, 500 items, old TensorFlow 1 code) — it
has no ranking-model code, no live YouTube data, and no
Shorts-specific code. Nothing below is an official threshold.

- **Retrieval first, ranking second.** The system first
  retrieves a few hundred candidates from millions, using
  how similar a video is to what a viewer already watched,
  and only then ranks those candidates. For a creator this
  means two different failures: "barely shown" is a
  retrieval failure (the system did not pick this Short for
  that viewer at all), while "shown but swiped" is a ranking
  / hook failure. Fixing the hook does not fix retrieval,
  and fixing the topic does not fix a weak hook. Diagnose
  them in that order (`/yt-diagnose` already names
  "barely shown = not tested" — this is why).

- **Two-stage diagnostic, stated as a mapping (v3.3.6).**
  (i) Low shown-in-feed / impressions vs peers = retrieval /
  candidate-stage failure: wrong audience cluster, niche
  mismatch. The fix is re-targeting the cluster or topic, not
  rewriting the hook. `/yt-diagnose` now carries this as a
  RETRIEVAL note on every NOT TESTED verdict, alongside "wait
  for the test audience" — wait first, re-target if reach
  stays low after testing. (ii) Good impressions + fast
  drop-off = ranking / retention failure, and the retention
  curve places it: a cliff in the first 3 seconds is a hook
  failure, a later slide is a pacing / beat failure.
  `/yt-diagnose` cannot place the cliff itself (it only sees
  average % viewed); `/yt-retention` reads the curve, and its
  BIGGEST LEAK verdict names the one fix.
- **Audience cluster, not just keywords.** Ranking in the
  DNN is similarity between a user vector and a video
  vector, learned from viewing behaviour, not from matching
  a hashtag. Before you publish, answer in one line: which
  viewers, by what they already watch, should this Short be
  retrieved for? If the answer is only a keyword, the
  retrieval case is weak. For a niche channel, that answer
  is a cluster (for example, viewers of gymnastics and
  flexibility Shorts), not a tag list. `/yt-trends` still
  supplies keywords; it does not replace this check.
- **Freshness and the exploration window.** A new video has
  no history, so the system must test it to learn anything
  about it, and it uses age as a signal while doing so.
  Treat a new Short as an exploratory test, not as a final
  verdict: judge a direction over 5–10 Shorts in the same
  cluster, against your own format median, not from one
  Short alone. The 48-hour check in the validation protocol
  still applies; the judgement window for a direction is
  longer than the judgement window for one video.
- **Signal strength: weak vs strong.** Watching is not the
  same as being satisfied, and not every interaction counts
  equally. Weak: a swipe in under a second, a like on its
  own, a single-word comment. Strong: a re-watch, a share,
  a subscribe from the Short itself, a comment that asks
  for the next skill, and a viewer who returns for the next
  Short. When you read Studio, weight the strong signals
  more than the weak ones — a Short with many likes but no
  shares, re-watches, or return viewers has not proved
  satisfaction.
- **The retrieval question for every Short.** Every
  algorithm pass now ends with this question as well as
  "ship it, or change it?": who should the system retrieve
  this Short for, and what would prove it retrieved it for
  the right people? If you cannot answer that in one line,
  the package is not ready, however good the hook is.

What this section deliberately does NOT add: no official
weights, no percentage thresholds, no best-time table, no
trending-sound chasing, no re-upload guidance for a failed
Short, no scraping or botting, and no claim that this repo
predicts Shorts performance. The DNN is 2016 long-form
work: it optimises next-video prediction and watch time
in minutes, not swipe, loop, and completion in seconds,
and it has nothing on sound, captions, loops, AI
disclosure, or originality penalties. Those Shorts parts
already live in `/yt-shorts-first`, `/yt-originality`,
and the 2026 signals above — this section does not
replace them.

## Loops and rewatch — what is verifiable (v3.3.7)

Shorts loop automatically, and since 31 March 2025 every
replay counts as a public view with no minimum watch time,
while monetisation and YPP eligibility run on engaged
views. Average percentage viewed above 100% in Studio is
therefore a real, readable sign that viewers looped — but
it is a metric reading, not a ranking rule. This pack
deliberately claims no ranking weight for loops: many
third-party guides call loops "one of the strongest
signals", but no official YouTube statement with a weight
was found, so that claim is not repeated here as fact.
What the pack does encode, in `/yt-shorts-first`,
`/yt-story`, and `/yt-qa`, is the craft that earns a
genuine second watch (seamless end-to-start match, clean
audio join, one real rewatch trigger) and the honest Studio
read beside it (percentage viewed plus engaged views, never
raw views alone).

## Retention honesty (v3.4.5)

YouTube publishes NO 70%, 85%, or 100% retention
thresholds, and NO 8-second checkpoint. Any blog,
guide, or pack note that quotes one as a rule the
algorithm enforces is inventing it — including
numbers that already appear in this pack, which
are relabelled here as what they are:

- The "healthy VVSA roughly 70–90%, below about
  60% distribution reportedly collapses" range in
  the v3.2.0 section above, and the "completion
  above about 85% associated with breakout Shorts"
  line in `references/2026-signals.md`, are
  third-party guide figures and creator-observed
  lore [LORE], not YouTube rules. The same holds
  for the length-tier retention ranges in that
  reference file, and for the creator-observed
  "losses cluster at 1–2 seconds and again around
  7–8 seconds" curve shape: useful diagnostics
  against your own channel's curve, never targets
  to chase as thresholds.
- What IS documented, and what this pack keeps:
  since 31 March 2025 a Shorts view counts on play
  or replay start with no minimum watch time, and
  engaged views are the stricter, revenue-relevant
  count; rewatched segments can exceed total views,
  so average percentage viewed above 100% in Studio
  is a real, readable sign that viewers looped —
  but it is a metric reading, not a ranking rule,
  and this pack claims no ranking weight for loops
  (see the v3.3.7 section above).
- The rule that replaces every threshold above:
  judge a video against your own channel's median
  over the last ten videos in the same format, and
  read the retention CURVE (where the drops are),
  not a single percentage. A "bad" number against
  a blog's threshold is not a verdict; a cliff at
  the same second across three videos is.

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
