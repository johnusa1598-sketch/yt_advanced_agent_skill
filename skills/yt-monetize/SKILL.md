---
name: yt-monetize
description: >-
  The YouTube Partner Programme runway planner: current
  thresholds, the 1 February 2027 change for new applicants,
  the Shorts pool rules, and honest revenue maths from your own
  numbers only. Use for "when can I monetise", "YPP
  requirements", "Shorts earnings", or "is this channel viable".
---

# yt-monetize

The single most important fact in this skill is a date:
**1 February 2027**. For new ad and Premium applicants, the
bar doubles on that day. A channel planning around the old bar
in 2026 is planning for a programme that will not exist when
it applies. Plan around the new bar, and treat anything that
arrives earlier as a bonus.

## The thresholds

| | Until 31 January 2027 | From 1 February 2027, new applicants |
| --- | --- | --- |
| Subscribers | 1,000 | 1,000 (unchanged) |
| Watch hours, 365 days, **or** | 4,000 qualified hours | **8,000 qualified hours** |
| Qualified Shorts views, 90 days | 10 million | **20 million** |

Existing YPP members are unaffected on entry. But to earn
from the Shorts Creator Pool each month, a creator must
maintain **10 million qualified Shorts views per 90 days**;
missing it pauses Shorts pool earnings only, not YPP status
and not long-form earnings.

Fan funding and Shopping are unchanged: 500 subscribers plus
3,000 hours or 3 million Shorts views. A newer activity rule
also applies: 1,000 hours, or 1 million Shorts views, or
2 long-form / 5 Shorts uploads per 90 days, with a 90-day
grace window.

**Deadline that is easy to miss:** accept the updated terms
in Studio by **31 January 2027**, or monetisation features
pause from 1 February 2027.

One edge case to confirm in Studio rather than assume:
partner sources report that applications filed by 23:59 UTC
on 31 January 2027 are judged at the old bar. The official
page confirms the 1 February date; the cutoff handling for a
rejected-then-reapplied channel is not confirmed here, so do
not build a deadline strategy on it.

## How Shorts actually pays

Shorts pay from a pool: ads run between Shorts, music-licensing
costs come off first, and creators keep **45%** of their
allocation (against 55% for long-form). The pool is monthly,
and the 10-million-per-90-days maintenance rule above decides
whether you are in it that month.

Shorts RPM is structurally cents per 1,000 views against
dollars for long-form. Third-party ranges vary wildly - one
guide cites $0.01-$0.10 per 1,000 as typical, one partner study
of 274 channels reports $0.02-$1.48 with a US figure near
$0.33. **This pack never quotes a fixed RPM**, because any
single number would be false for most channels. The only
honest revenue maths uses your own Studio RPM and your own
engaged views, in `templates/ypp-runway.md`. And because
public view counts are inflated by the view redefinitions
(see `/yt-algorithm`), YPP eligibility and earnings run on
qualified and engaged views, not on the public number.

The conclusion writes itself, and it is the strategy of this
skill: a Shorts-only channel faces both the 10-million pool
maintenance rule and the 20-million entry bar. Conversion to
long-form watch time (`/yt-bridge`) is not a nice extra; it is
the plan.

## Advertiser-friendly, including the packaging

Advertiser-friendly rules apply to the title, thumbnail,
description, and tags as well as to the video, with three
outcomes: full, limited, or no ads, across fourteen content
categories. In 2026 YouTube loosened full-ad eligibility for
non-graphic dramatised or discussion content on some sensitive
topics, while child abuse and eating-disorder content remain
ineligible for full monetisation.

For gymnastics and flexibility specifically:

- No idealised-body or weight framing repeated to teens:
  YouTube limits repeated recommendations of such content to
  viewers aged 13-17.
- No miracle or guaranteed-result health claims.
- No dangerous-challenge framing, and no synthetic persona
  giving health advice (see `/yt-originality`).

## How to run it

1. Fill in `templates/ypp-runway.md` with your own Studio
   numbers: subscribers, qualified watch hours, qualified
   Shorts views, and your own RPM if you have one.
2. Read the gap against the **February 2027** bar, not the
   current one, unless you will apply before the deadline.
3. Set the bridge target from the gap: how much long-form
   watch time the Shorts traffic must convert into, and by
   when (`/yt-bridge` tracks the conversion).

## The gate

Nothing here publishes. This skill hands back a runway with
your numbers and the February 2027 bar, ending with the
question: **ship it, or change it?**
