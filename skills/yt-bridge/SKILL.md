---
name: yt-bridge
description: >-
  Turn cheap Shorts views into long-form watch time and returning
  viewers: Related Video routing, the Shorts Series seasons and
  episodes system, and a series bible. Use for "how do Shorts
  viewers find my long videos", "start a Shorts series", or
  "convert Shorts traffic".
---

# yt-bridge

Shorts views pay cents and do not, on their own, build a
channel. Long-form watch time is what the monetisation bar
counts (`/yt-monetize`), and returning viewers are what the
algorithm compounds. The bridge between the two is not automatic.
It is built, one Short at a time, out of three pieces.

## Piece 1: Related Video is the only routing

Shorts have no end screens and no cards. The only in-player
route from a Short to a long video is **Related Video**, set
per Short in Studio. Every Short that belongs to a series or
points at a long video needs its Related Video set before it
goes out, and the last three seconds of the Short must say
where it goes. A Short with no Related Video and no spoken
pointer is a dead end: the viewer swipes on, and the view is
spent.

The per-Short checklist, run at packaging time (`/yt-post`):

- Related Video set to the matching long video or the next
  episode, not to the channel page.
- Last-3-seconds line spoken and captioned: what the next
  video gives that this one did not.
- Pinned comment pointing the same way (`/yt-community`),
  so the route survives even if the viewer misses the ending.

## Piece 2: Shorts Series, seasons and episodes

Shorts Series, announced at Made on YouTube in September 2026,
groups Shorts into seasons and episodes with custom thumbnails
and sequential playback across web, mobile, and TV. A series
gives the viewer the next episode instead of the next random
Short, which is exactly the returning-viewer machine a
Shorts-only channel lacks.

Two warnings, both honest:

- Rollout was reported as gradual and YPP-first from
  23 September 2026. Check your own Studio before building a
  workflow on it; if Series is not there yet, the playlist
  version below is the fallback.
- Members-only episodes on mobile were reported in October
  2026 as coming "in coming weeks" — no verified live date,
  so do not promise members-only episodes until Studio shows
  them. Possible future discovery surfaces (Search,
  Recommended, Continue watching) were also reported, not
  confirmed: discovery through Series is not guaranteed,
  and the playlist fallback stays the reliable route.
- For gymnastics and flexibility, the format maps directly to
  progressions: "30-day splits", "backbend ladder", "handstand
  journey". A progression is a series with a built-in reason
  to return: the next episode is the next step, not a new idea.

## Piece 3: the series bible

One file per series, from `templates/series-bible.md`:

- The promise: what the viewer gets every episode, in one
  sentence.
- The arc: season by season, where the progression ends, and
  what the finale is. A series with no finale is a treadmill.
- The episode shape: the fixed beats, and what varies without
  breaking the promise (variation in substance, not just in
  intro and outro - see `/yt-originality`).
- The routing: each episode's Related Video target and its
  last-3-seconds pointer, written before the episode is made.
- The fallback: the long-form playlist order, for viewers and
  channels without Series access.

## The conversion tracker

Measure the bridge, or it does not exist. For each Short,
record Related-Video clicks against Shorts views. As a
**third-party benchmark, not a YouTube figure**, one partner
source reports 0.5-1% conversion as strong against a 0.04%
typical rate. Treat both numbers as uncertain and directional
only: your own channel's baseline over its last ten Shorts is
the number that matters, and the goal is to beat it, not to
hit someone else's percentage.

## Repurposing, done without breaking the bridge

A long video re-cut into a Short still needs the bridge: the
Short starts on the payoff or the tension, not on the setup,
gets its own captions rewritten for speed, tells one standalone
story, and points back at the long video it came from via
Related Video. Studio's Remix "Edit into a Short" caps the
selection at 60 seconds and cannot add Audio Library music in
that flow. Never upload a TikTok-watermarked file, and never
re-upload someone else's clip: your own long-form re-cut with
new commentary or editing is different from a re-upload, and
`/yt-originality` is the test that tells them apart.

## The gate

Nothing here publishes. This skill hands back the series bible
entry, the routing checklist, and the conversion log, ending
with the question: **ship it, or change it?**
