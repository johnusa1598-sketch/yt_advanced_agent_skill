---
name: yt-post
description: >-
  The pro packaging pipeline: turn one video brief into a complete
  publish-ready package - titles, description, tags, thumbnail brief,
  timed text layers, end screen, timing, pinned comment, and an A/B
  test plan. Use for "package this video", "ready to publish", "full
  upload package", "titles and description and thumbnail together".
---

# yt-post

`/yt-package` lints one title and thumbnail pairing. This skill
assembles the whole package, in order, from one brief - so the title,
the thumbnail, the description, the captions and the call to action
all say the same thing in different words, instead of five decisions
made separately that quietly contradict each other.

## The brief it needs

One JSON brief, in the shape of `templates/publish-package.md`
(and `examples/aria-fit/package-brief.json` shows a filled one):

- `title_idea`, `hook`, `format` (short or long), `duration_s`
- `beats` - time and text, which become the text layers
- `cta` - the one call to action, not three
- `series`, `channel`, `audience`, `keywords`

```bash
python3 package_builder.py brief.json --trends trends.json
python3 package_builder.py brief.json --json   # machine-readable package
```

Pass `--trends` with the JSON output of `trend_pack.py` and the
hashtag line and tags come from the same pack the title was written
for. Without it, the tool builds hashtags from the brief alone and
says so.

## What comes out, and why each part is there

1. **Title variants, each with its CTR reasoning.** Five or six
   titles, not one, because a title is a hypothesis. Each carries
   the reason it might click (contrast, open question, front-loaded
   subject, failure first, curiosity gap, series frame) and its own
   length warnings. Pick the one whose reason matches the audience
   you actually have.
2. **Thumbnail brief.** Three elements at most, text of three
   words at most, and the rule that matters: the thumbnail must
   carry different words from the title, or half the click surface
   is wasted.
3. **Description.** The first two lines are the only ones anyone
   reads and the search snippet - they carry the title's subject
   and the hook. Then the series line, then the audience line,
   then the hashtags.
4. **Tags (15 at most).** Disambiguation, not stuffing. Spellings,
   tool names, abbreviations people type.
5. **Timed text layers.** Every beat becomes on-screen text of
   five words at most, in a bold high-contrast style, because a
   Short watched on mute must still make sense.
   **Text-end rule (v3.3.2):** every text layer ends when
   its beat ends. A layer that lingers into the next beat,
   into the exit, or into a standing pose FAILS the package
   — re-time it, do not leave it. Check it by freezing the
   frame at each text change and at the skill exit: the text
   on screen must match the visual on screen at that second.
6. **End screen and CTA.** One line, named before the goodbye,
   pointing at the next video in the series.
7. **Upload timing.** Your own Studio audience data first - the
   tool tells you where to look and gives a default (late
   afternoon to early evening, series day) only if you have no
   data. A blog's "best time to post" is not your audience.
8. **Pinned comment.** One question that invites the answer the
   next video will be built around. Comments are content strategy,
   not decoration.
   **Vote rule (v3.3.2):** for a challenge or comparison
   Short with two skills, sides, or attempts in the video,
   the pinned comment MUST be a vote naming both sides as
   they appear in the video ("Team MIDDLE or Team FRONT —
   which split wins?"). A generic question is not enough
   for a comparison Short, and the vote must name the sides
   the viewer actually saw, in the order they saw them.
9. **A/B test plan.** Title A vs title B, thumbnail held constant,
   judged on click-through in the first 48 hours against the
   channel's own median - and kept only if average view duration
   holds. A click that leaves is a worse video, not a better
   title.

## The order of operations

Algorithm pass first (`/yt-algorithm`): what is this video's one
prediction? Then trends (`/yt-trends`): what pack does it sit in?
Then this pipeline. Then the publish check (`/yt-publish`), last,
always. Packaging after the publish check is how a disclosure or a
missing end screen ships by accident.

## The gate

Nothing here publishes. This skill writes and you publish. Every
package ends with its checklist and the question: **ship it, or
change it?**
