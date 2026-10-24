# Video brief (for yt-post / yt-viral-loop)

Fill this in, save it as JSON, and hand it to `package_builder.py`
and `retention_plan.py`. One brief feeds both tools, so the package
and the retention plan never disagree about the video.

```json
{
  "title_idea": "beam backflip",
  "hook": "Did she land it?",
  "format": "short",
  "duration_s": 30,
  "beats": [
    {"time": "0-3s", "text": "Aria mounts the beam, eyes forward"},
    {"time": "3-8s", "text": "She runs two steps and springs"},
    {"time": "8-14s", "text": "Backflip over the beam"},
    {"time": "14-20s", "text": "Clean landing, arms up, smiling"},
    {"time": "20-26s", "text": "Slow-motion replay of the landing"},
    {"time": "26-30s", "text": "Harder one next - follow for part 2"}
  ],
  "loop": "The clean landing sets up the next, harder attempt",
  "cta": "follow for part 2",
  "series": "Skill Challenge",
  "channel": "Aria Fit",
  "audience": "gymnastics fans, 13-25",
  "niche": "AI gymnastics",
  "keywords": ["gymnastics", "beam", "backflip"]
}
```

Rules for the brief:

- One idea only. A brief that tries two skills is two videos.
- The hook is the 0-3s line, not a summary of the video.
- Beats are what happens, in order, with times. The text layers
  and the retention plan are both built from them.
- The loop line is required for a Short: the last line sets up
  the first line, so a rewatch feels like a continuation.
- Nothing in this file is published. `package_builder.py` writes
  the package; you upload.
