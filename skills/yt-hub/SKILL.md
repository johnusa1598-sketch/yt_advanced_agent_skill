---
name: yt-hub
description: >-
  Route a YouTube request to the right skill in this pack and run
  it end to end. Use for any YouTube request when you are not sure
  which skill fits, or for "run my channel workflow".
---

# yt-hub

This skill does not write the video. It picks the skill that
does, and it keeps the workflow in order.

## Routing

- An AI video prompt, a character that keeps changing, or a
  prompt that must be hard to copy: `/yt-ai-prompt`.
- A script, a hook, or an opening line: `/yt-script`.
- A title, a thumbnail, or a CTR problem: `/yt-package`.
- A Short, a daily Shorts plan, or a Shorts-only channel:
  `/yt-shorts-first`, then `/yt-package`.
- A series, a recurring character, or a repeat idea:
  `/yt-series`.
- Numbers, growth, or "why is growth slow": `/yt-analytics`,
  then `/yt-audit` for the single fix.
- A transcript to cut: `/yt-edit`. A long video to clip:
  `/yt-shorts`. Chapters: `/yt-chapters`. Retention:
  `/yt-retention`. What is working in a niche: `/yt-viral`.
- A description, tags, or search: `/yt-seo`. Comments:
  `/yt-comment`. A week or month plan: `/yt-plan`.
- A video that is finished: `/yt-publish`, last, always.

## The workflow for one video

1. Idea and format: `/yt-plan` or `/yt-series`.
2. AI video prompt, when the video is AI generated:
   `/yt-ai-prompt`, with the character lock and the negative
   prompt, before any other production step.
3. Script and hook: `/yt-script`.
3. Title and thumbnail: `/yt-package`.
4. Description and search: `/yt-seo`.
5. Publish check: `/yt-publish`.
6. After it is live: comments with `/yt-comment`, retention
   with `/yt-retention`, and numbers with `/yt-analytics`.

## Rules

- Read the channel profile and the voice file first, when they
  exist. Do not invent numbers, results, or sources.
- Hand back one copy-paste block per step, and end every run
  with the question: **ship it, or change it?**
- Nothing here publishes. This skill writes and you publish.
