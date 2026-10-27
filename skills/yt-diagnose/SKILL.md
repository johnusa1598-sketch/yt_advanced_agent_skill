---
name: yt-diagnose
description: >-
  Diagnose a video from your own YouTube Studio CSV export: read
  the gates in order - impressions, CTR / chose-to-view, retention,
  return viewers - and name the one broken gate. Use for "why did
  this flop", "is it the title or the video", "read my analytics",
  or the weekly analytics loop.
---

# yt-diagnose

Stop guessing at "the algorithm". A video fails at exactly one
gate, and the fix for each gate is different. Repackaging a video
whose problem is retention wastes a good title; rewriting a video
whose problem is packaging wastes a good video.

## The gates, in order

Read them in this order, because a later gate means nothing when
an earlier one is broken:

1. **Reach - was it tested?** "Shown in feed" (Shorts) or
   impressions (long-form) against your peer median. A video with
   barely any shown-in-feed was never tested. That is not a hook
   failure, and no hook rewrite will fix it. Wait, or check
   whether the video was ever eligible for the feed at all.
   **Two-stage split (v3.3.6):** shown well below the peer
   median is also a retrieval / candidate-stage failure —
   wrong audience cluster, niche mismatch. The tool carries
   this as a RETRIEVAL note on the NOT TESTED verdict: wait
   for the test audience first, then re-target the cluster
   or topic if reach stays low. Rewriting the hook is the
   wrong fix for a retrieval failure.
2. **Hook - did it win the click or the stay?** For Shorts,
   "chose to view" against "shown in feed", and viewed vs
   swiped away in the first seconds. For long-form, impressions
   CTR. Below the peer median here is a first-frame, title, or
   thumbnail problem.
3. **Retention - did it deliver?** Average percentage viewed,
   and the curve, not the average. Good impressions + fast
   drop-off is a ranking / retention failure, placed by the
   curve: a cliff in the first 3 seconds is a hook failure,
   a later slide is a pacing / beat failure (`/yt-retention`
   names the biggest leak). This tool only sees the average,
   so it cannot place the cliff itself — read the curve
   before choosing the fix.
4. **Return - did it bring people back?** Returning-viewer
   share against your peer median. A video can perform and
   still fail here, and that is a series and routing problem
   (`/yt-bridge`), not a video problem.

## The two classic pairings

- **Low hook + high retention = packaging problem.** The video
  works; the title, thumbnail, or first frame does not. Repackage
  before you rewrite. For long-form, this is also what a
  Test & Compare run is for (`/yt-test`).
- **High hook + low retention = content or promise problem.**
  The packaging worked and viewers left anyway. Either the video
  did not deliver what the packaging promised, or the payoff
  came too late. Fix the first 30 seconds and the payoff
  placement, not the thumbnail.

## How to run it

1. In Studio, export the video's analytics (or the channel's
   video list) as a CSV. Include shown-in-feed, chose-to-view,
   swiped away, engaged views, average percentage viewed,
   CTR, and returning-viewer share where Studio offers them.
2. Run `skills/yt-diagnose/diagnose.py` on the export. It
   judges every video against the median of its peers in the
   same file, same format when the export says so. When fewer
   than two same-format peers exist for a gate, it falls back
   to all formats and says so in `peer_basis` — a mixed-format
   median is never silent (v3.3.6).
3. Take the verdict's **one fix** and apply it to the next
   video only. One fix per video, or you will never know what
   worked.

## The weekly loop

Baseline three videos, diagnose all three, fix the weakest gate
on the next video, publish, compare against the same peer
median. A gate that moves in the predicted direction twice is
a rule for your channel. A gate that does not is a property of
the video, not of the model.

## What this skill does not claim

- No global benchmarks. A "good" CTR or completion rate from a
  blog post is not your channel's number. Compare against your
  own last ten similar-length videos, which is the comparison
  Studio itself encourages.
- No raw-view comparisons across the view redefinitions:
  31 March 2025 for Shorts, 24 August 2026 for all formats.
  A "view" before those dates is not the same unit as a "view"
  after them. CTR, average view duration, and retention are
  still calculated on engaged views, so compare those across
  the boundary, not raw views.
- No fake data. If the export lacks a column, the gate that
  needs it is reported as unknown, not invented.

## The gate

Nothing here publishes. This skill reads your export and hands
back one diagnosis and one fix, ending with the question:
**ship it, or change it?**
