---
name: yt-viral-loop
description: >-
  The end-to-end orchestrator: chain the pack's skills for one video
  (prompt, brief, algorithm pass, trends, packaging, analytics
  feedback) and plan its retention curve. Use for "run the whole
  workflow", "take this idea to publish", "viral loop", "full
  pipeline", or when one video must be planned end to end.
---

# yt-viral-loop

Other skills do one job. This one runs them in order, for one
video, and carries the result of each step into the next - so the
package is written for the retention plan, and the retention plan
is written for the hook, instead of each step optimising alone.

## The chain, in order

1. **Idea and format.** `/yt-plan` or `/yt-series`. One idea,
   one format, one series it belongs to. A video that belongs
   nowhere compounds nowhere.
2. **AI video prompt, when the video is AI generated.**
   `/yt-ai-prompt`, with the character lock and the negative
   prompt, before any other production step.
3. **Script and hook.** `/yt-script`. Five hooks, scored, then
   the spoken script with retention beats marked.
4. **Algorithm pass.** `/yt-algorithm`. One prediction to test:
   what signal should this video move, and against which median?
   Write it down before you publish, or you will claim every
   result afterwards.
5. **Trends.** `/yt-trends`. Evidence in, pack out. The pack the
   title is written for is the pack the video ships with.
6. **Sound and meme slots.** `/yt-sound` for the track, the
   licence and the loop point; `/yt-meme` for at most one meme
   slot, placed at the middle turn.
7. **Packaging.** `/yt-post`. Titles with CTR reasoning, thumbnail
   brief, description, tags, text layers, end screen, timing,
   pinned comment, A/B test plan - from one brief.
8. **Retention plan.** This skill's tool, below. The curve on
   paper before the curve in Studio.
9. **Publish check.** `/yt-publish`, last, always. Disclosure,
   playlist, chapters, end screen.
10. **After it is live.** `/yt-comment`, `/yt-retention`, then
    `/yt-analytics`. One fix, not twenty (`/yt-audit`).
11. **Feedback into the next brief.** The one fix from step 10 is
    the first line of the next video's brief. A loop that does not
    feed back is just a checklist with a fancy name.

## Planning the retention curve

```bash
python3 retention_plan.py brief.json
python3 retention_plan.py brief.json --json
```

The brief is the same shape `/yt-post` takes: `format`,
`duration_s`, `hook`, `loop`, `beats`, `cta`. The tool marks
three jobs:

- **Hook (0-3s).** Visible in the first frame, names the skill
  or the stakes in under 10 words, ends on an open question.
- **Beats.** Each beat gets a purpose - hook, setup, turn, or
  payoff/loop. A beat longer than the format's budget (8 seconds
  for a Short, 45 for long-form) with no change inside it is
  flagged as a likely drop point, as is a gap between beats with
  nothing planned in it.
- **Loop point and rewatch trigger (Shorts).** The last line sets
  up the first line, and the payoff is something worth seeing
  twice - a landing, a reveal, a score - not a line of
  explanation. For long-form the same slot is the end screen,
  named before the last 20 seconds.

Two mechanical flags to take seriously: a Short with no loop line
ends dead, and a long video with a long middle stretch and no
re-hook bleeds there. Everything else in the plan is judgement,
and judgement is validated after publish, not before: compare the
plan with the Studio curve and `retention.py`. A flagged beat
that held is a lesson; a held beat that was not flagged is a new
rule for your channel.

## The one-variable rule

The loop only teaches you something if one thing changes per
video. Change the title and the hook together and the next brief
learns nothing. The chain above exists so that exactly one
variable is ever in doubt: this video's prediction from step 4.

## The gate

Nothing here publishes. This skill writes and you publish. Every
run ends with the full chain, the retention plan, and the
question: **ship it, or change it?**
