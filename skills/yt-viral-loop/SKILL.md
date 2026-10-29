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

This chain mirrors `/yt-hub` (steps 2–4 and 11–12 there). Do not
run a shorter version of it for AI video: the steps below that
look skippable — title-first, the production gate, Story DNA,
the QA gate, originality — are the ones that stop a video
shipping with a wrong hook frame, a missing beat, or a failed
face gate. The publish check at step 13 is not a QA substitute.

1. **Idea and format.** `/yt-plan` or `/yt-series`. One idea,
   one format, one series it belongs to. A video that belongs
   nowhere compounds nowhere.
2. **Title first, then anti-glitch.** `/yt-anti-glitch`. The
   title is fixed before any prompt is written; the skill is
   checked against the Skill-Safety Ladder, the variety matrix
   (including the leotard rotation slot), and the
   never-retry-denied rule.
3. **Production, two steps.** `/yt-production` with
   `/yt-ai-prompt`: the hook-frame image first, gated (format,
   character lock, suspense rule), then the video
   animated from that frame. A single-skill Short is one Block B
   video; a multi-skill concept is a segment list, assembled
   to the same 8–12 second budget.
4. **Story DNA.** `/yt-story`. All eight beats in arc order,
   the parasocial beat, the loop bridge, the comment trigger —
   before the script is written, so the script serves the beats
   and not the other way round.
5. **Script and hook.** `/yt-script`. Five hooks, scored, then
   the spoken script with retention beats marked.
6. **Algorithm pass.** `/yt-algorithm`. One prediction to test:
   what signal should this video move, and against which median?
   Write it down before you publish, or you will claim every
   result afterwards.
7. **Trends.** `/yt-trends`. Evidence in, pack out. The pack the
   title is written for is the pack the video ships with.
8. **Sound and meme slots.** `/yt-sound` for the track, the
   licence and the loop point; `/yt-meme` for at most one meme
   slot, placed at the middle turn.
9. **Packaging.** `/yt-post`. Titles with CTR reasoning, thumbnail
   brief, description, tags, text layers, end screen, timing,
   pinned comment, A/B test plan - from one brief.
10. **Retention plan.** This skill's tool, below. The curve on
    paper before the curve in Studio.
11. **QA gate.** `/yt-qa`. Scorecard threshold (total 8 or more,
    identity 2 or more, movement 2 or more), face gate, format
    gate, audio gate, text-end rule, parasocial tail cap,
    leotard slot. A FAIL stops the chain here, not at publish.
12. **Originality and disclosure.** `/yt-originality`. The
    substance varies, not just the intro and outro; AI
    disclosure is marked; the licence log is clean.
13. **Publish check.** `/yt-publish`, last, always. Disclosure,
    playlist, chapters, end screen — after QA has passed, not
    instead of it.
14. **After it is live.** `/yt-comment`, `/yt-retention`, then
    `/yt-analytics`. One fix, not twenty (`/yt-audit`).
15. **Feedback into the next brief.** The one fix from step 14 is
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
  **Rewatch (v3.3.7):** name one rewatch trigger in the brief
  (`rewatch_trigger`) — a hidden detail, missed moment,
  count-the-detail, satisfying payoff, fast payoff + slow
  information reveal, or end reframe, per `/yt-shorts-first`.
  The plan flags a Short with no trigger (`no-rewatch-trigger`),
  and the loop-match check is end = opening in the last 2
  seconds as in the first 2, audio joined cleanly, no
  end-card after the ≤2 second tail. A trigger claimed but
  absent from the video fails QA, not just the plan.

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
variable is ever in doubt: this video's prediction from step 6.

## The gate

Nothing here publishes. This skill writes and you publish. Every
run ends with the full chain, the retention plan, and the
question: **ship it, or change it?**
