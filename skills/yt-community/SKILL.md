---
name: yt-community
description: >-
  The community, poll, and pinned-comment routine: drafts for
  manual posting only, never automation. Use for "what should I
  pin", "write a poll", "community post ideas", or "keep viewers
  coming back between uploads".
---

# yt-community

Returning viewers are the cheapest growth there is, and the
cheapest way to earn them is between uploads, not during them.
This skill is a routine of drafts. It never posts, replies, or
comments for you, and it never will: automation in the comment
section is both against the spirit of the thing and the fastest
way to poison the audience data you actually need.

## Pinned comments, drafted during scripting

A pinned comment is not an afterthought. It is drafted while
the script is written, because it has to point at the same
promise the video makes.

- **Length:** one to two lines. A paragraph pinned to a Short
  is a wall nobody reads.
- **Timing:** pin within 5-30 minutes of publishing, while
  the first viewers are still there.
- **Presence:** stay in the thread for 30-60 minutes after
  pinning. First-hour replies, and specific prompts, beat
  generic calls to comment.
- **First-hours replies (v3.5.0):** in the first few hours
  after publishing, reply to the first 5–10 comments.
  Replies are specific (answer the score, react to the
  vote, ask the follow-up), never generic thanks. This
  is the routine that turns the first viewers into the
  core audience that returns for the next episode — and
  it is manual, like everything in this skill: drafts
  here, you post.
- **Rotation:** rotate the format so the audience does not
  learn to ignore it - challenge one video, debate the next,
  question the one after. A bank of formats lives in
  `templates/community-routine.md`.
- **Ask "A or B?", not "comment below".** A specific prompt
  with two answers gets answers; an open prompt gets silence.
- **Vote rule (v3.3.2, from `/yt-post`).** On a challenge or
  comparison Short, the pinned comment is the vote naming
  both sides as they appear in the video, in the order the
  viewer saw them — not a generic question, and not a second
  pinned comment competing with the vote. The comment-trigger
  detail from `/yt-story` is asked inside that vote or in a
  reply. `publish_check.py` enforces this when the package
  carries `comparison_sides`.
- **Route:** where the video belongs to a series, the pinned
  comment points at the next episode or the long video, the
  same way Related Video does (`/yt-bridge`).

## Polls tied to the next video

Polls attached to an upcoming video outperform generic posts
by a wide margin in partner data - one partner dataset reports
1,500-7,700+ votes on video-tied polls against 15-40 comments
on plain text posts. That is partner data, not a YouTube
figure, and the gap is the point, not the numbers: a poll that
decides something real (which skill next, which attempt counts)
gives viewers a reason to return for the answer.

## GIF comments (mobile, late 2026)

GIF replies rolled out on mobile in October 2026, with
all-user availability planned for November 2026 (developer
documentation, not a verified live date). Desktop shows GIF
comments but has no posting button. No workaround is
recommended: answer GIF comments from mobile, and never
install a desktop extension to post them — that is not a
publishing route this pack supports.

Poll rules:

- One question, two to four answers, each answer a real option
  you will actually follow through on.
- Publish the poll before the video it decides, and name the
  video it decides in the post itself.
- Report the result in the video. A poll whose result is never
  mentioned teaches viewers their vote did not matter.

## Community posts between uploads

Since September 2026, community posts can be recommended in
the Shorts feed on web and mobile. That makes the post
calendar part of the Shorts workflow, not an extra:

- **80/20 value to promotion.** Four posts that teach, ask,
  or show something for every one that says "new video".
- A post calendar lives in `templates/community-routine.md`:
  one post per gap between uploads, tied to the series in
  progress, never a generic "like and subscribe".
- Images and questions travel further than text alone, and a
  teaser frame from the next episode beats a stock graphic.

## What to hand back

- The pinned comment draft, in the rotation format for this
  video, ready to paste by hand.
- The poll draft, tied to the next video or episode, with
  the follow-through it promises.
- The post for the gap before the next upload, in the 80/20
  calendar.

## The gate

Nothing here publishes, posts, or replies. This skill writes
drafts and you post them by hand, ending with the question:
**ship it, or change it?**
