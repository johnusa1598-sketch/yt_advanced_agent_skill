---
name: yt-publish
description: >-
  Run the last check before a video goes out: title, thumbnail,
  description, AI disclosure, playlist, chapters, and end screen.
  Use for "ready to publish", "check this before I post", "upload
  checklist", or a video that is finished but not yet live.
---

# yt-publish

Most publish mistakes are not creative. They are a missing
disclosure, a thumbnail with four words, or a video in no
playlist. This skill catches those before the audience does.

## Before you check

1. Ask for the publish details as one JSON object: title,
   thumbnail text, description, type, whether it is AI
   generated, whether the AI disclosure is marked, playlist,
   chapters, and end screen.
2. Never invent a detail to make the checklist pass. A missing
   item is FAIL until the user supplies it.

```bash
python3 publish_check.py publish.json
```

## The checklist

- Title present, 100 characters or fewer, and checked as a
  pairing with the thumbnail in `/yt-package`.
- Thumbnail text is 1 to 3 words and does not repeat the title.
- Description opens with a line that states what the video gives.
- AI disclosure is marked when the video is AI generated.
- The video is assigned to a playlist, so a new viewer has a
  next video.
- For a long video only: chapters are included and an end
  screen is set. Shorts do not need either.

## What to hand back

- READY or NOT READY, with every failed item named and the
  exact fix for it.
- The copy-paste block: title, description first lines, tags
  from `/yt-seo`, and playlist name.
- Nothing is uploaded by this skill. The user uploads.

## The gate

Nothing here publishes. This skill writes and you publish. Every
output ends in a block the user copies, and the last line of every
run is the question: **ship it, or change it?**
