---
name: yt-test
description: >-
  Test thumbnails and titles properly: the Test & Compare log
  for long-form, the manual cover protocol for Shorts covers,
  and the announced video-cut A/B check. Use for "A/B test this
  thumbnail", "which title won", or "change a Short's cover".
---

# yt-test

Most thumbnail tests fail before they start, because they are
judged on the wrong number, judged too early, or run on a
format that has no native test at all. This skill keeps the two
cases apart.

## Long-form: Test & Compare, used properly

Test & Compare lives in Studio on desktop, under Advanced
Features. The rules that matter:

- Up to **3 variants** - thumbnails, titles, or whole packages.
- The winner is judged on **watch-time share, not CTR alone**.
  A variant that wins clicks and loses viewers is not the
  winner.
- A test runs **up to 2 weeks**. Do not judge it at hour 12.
- One variant below 1280x720 drags all variants down to
  854x480. Keep every variant at or above the floor.
- Log every test in `templates/test-compare-log.md`: the
  variants, the start date, the winner by watch-time share,
  and the date you stopped. A test you did not log is a test
  you will re-run by accident.

Since its 2024 launch, YouTube reports 40 million-plus
experiments run through Test & Compare. That is a usage
figure, not a promise about your test.

## Shorts: there is no native test, so run the manual protocol

Test & Compare does **not** cover Shorts. Help lists Shorts
as ineligible, and a test is lost if a video transitions into
a Short. So a Short's cover is validated before upload, and
changed only by the manual protocol below. Changing a Short's
cover on day one, or judging the change on feed traffic, tells
you nothing.

The manual Shorts-cover protocol:

1. **Catalogue Shorts only.** Never test on a new upload; a
   new Short is still in its test-and-expand phase, and any
   change confounds it. Pick a Short at least one month old.
2. **Baseline first.** Record two weeks of traffic by source
   before the change, so you know what normal looks like.
3. **Change one variable.** The cover, or the title, never
   both. Two changes and you will never know which one worked.
4. **Judge on non-feed traffic only.** Feed traffic is the
   algorithm's decision, not the cover's. Compare channel-page,
   search, and suggested traffic over an equal number of days
   before and after.
5. **Log it** in the same test log, marked "manual Shorts
   cover", with the same discipline as a native test.

## Video-cut A/B testing, announced September 2026 — check Studio first

Do not confuse two different tests, because the old version of
this skill blurred them:

- **Thumbnail Test & Compare: still no Shorts.** As of 2026
  reports, Shorts remain ineligible for thumbnail/title Test &
  Compare, and the July 2026 rollout did not change that. The
  manual cover protocol below still applies to covers.
- **Video-cut A/B: announced, coming 2027.** At Made on YouTube
  (September 2026) YouTube announced A/B testing of video cuts
  — up to three cuts of the same video, judged on watch-time
  share, for Shorts and long videos — with availability coming
  in 2027 per third-party reporting. Until it appears in your
  Studio, do not assume you have it: check Studio first. If it
  is there, run the native cut test and log it the same way as
  a Test & Compare test. If it is not, use the manual protocol.
- **Dynamic thumbnails** (YouTube serving different chosen
  thumbnails to different audience segments) were announced at
  the same event. Again: check Studio before promising it.

## What to hand back

- The test plan: variants, the one variable, the judge
  (watch-time share for long-form, non-feed traffic for
  Shorts), and the stop date.
- The log entry, filled in when the test ends - not before.
- The next test, chosen from what the last one taught you.

## The gate

Nothing here publishes. This skill writes the plan and the log,
and you run the test in Studio, ending with the question:
**ship it, or change it?**
