# The YouTube agent skill, next level

Seventeen skills that run a YouTube channel, up from eleven. Free,
MIT, no signup, no API key, nothing to connect.

**Original pack, by Jake Schincariol, MIT licence:**
https://github.com/Jakeschincariol/youtube-agent-skill
This next-level version keeps all eleven original skills and all
six original tools unchanged, and adds six skills, four tools,
prompt engineering for AI video, Muse compatibility, templates,
tests, and a worked example.
See `CHANGELOG.md` for exactly what changed.

**Nothing gets published until you do it.** These skills write.
You upload.

## The seventeen

| command | what it does |
| --- | --- |
| `/yt-hub` | Routes any YouTube request to the right skill. |
| `/yt-ai-prompt` | NEW. Next-level AI video prompts: 7 layers, locked character, timed beats with physics, camera, style, negative prompt, and three variants. |
| `/yt-script` | One idea into a script. Five hooks off 21 formulas, scored, then the spoken script with retention beats marked. |
| `/yt-package` | Title and thumbnail as one pairing, linted for truncation, duplication and vagueness. |
| `/yt-edit` | A transcript into an edit decision list: dead air, filler cues, retakes, with timecodes. |
| `/yt-comment` | The comment section triaged into four piles, then replies in your voice. Says which one to pin. |
| `/yt-plan` | A week that fits the hours you actually have. One anchor, one cheap one, three Shorts. |
| `/yt-viral` | What is working in your niche, ranked by multiple over each channel's own median. |
| `/yt-retention` | Your retention export read properly: hook leak, the cliffs, the slide, and what to change. |
| `/yt-shorts` | The Shorts already inside a long video, with a new first line written for each. |
| `/yt-shorts-first` | NEW. A Shorts-first daily workflow: first two seconds, one idea, a loop point, one call to action, and a series it belongs to. |
| `/yt-series` | NEW. A series bible, a locked character spec, and an episode log, so a series compounds instead of repeating. |
| `/yt-analytics` | NEW. Your own numbers read properly: subs per 1000 views, format averages, outliers over the median, and one fix. |
| `/yt-publish` | NEW. The last check before a video goes out: title, thumbnail, description, AI disclosure, playlist, chapters, end screen. |
| `/yt-seo` | The description, the tags that are worth having, and the three queries this should win. |
| `/yt-chapters` | Chapters from a transcript, validated against YouTube's own rules so they render. |
| `/yt-audit` | The whole channel, ending in ONE fix rather than twenty. |

## The ten tools

Every one runs on a clean Python 3 with no dependencies.

```bash
python3 skills/yt-script/hookscore.py --hook "one line"
python3 skills/yt-package/title.py --title "..." --thumb "..."
python3 skills/yt-edit/deadair.py transcript.srt
python3 skills/yt-chapters/chapters.py transcript.srt
python3 skills/yt-retention/retention.py retention.csv
python3 skills/yt-viral/swipe.py collected.json --min 2.0
python3 skills/yt-shorts-first/shorts_score.py --title "..." --thumb "..." --hook "..." --loop yes --cta "follow for part 2"
python3 skills/yt-analytics/analytics.py videos.json --subs 92
python3 skills/yt-publish/publish_check.py publish.json
python3 skills/yt-ai-prompt/prompt_builder.py brief.json
```

## Install

Claude Code, as in the original pack:

```bash
git clone https://github.com/Jakeschincariol/youtube-agent-skill.git
cp -r youtube-agent-skill/skills/yt-* ~/.claude/skills/
```

Muse, from this next-level folder:

```bash
cp -r next/skills/yt-* ~/workspace/custom-skills/
```

Then fill in `templates/voice.md` for how you talk, and
`templates/channel.md` for your channel. Every skill reads
those two files. A script in the wrong voice is worse than no
script, because you have to read it out loud.

## Test it

```bash
python3 tests/test_tools.py
```

No network, no YouTube login, no publishing. The test runs the
original hook and title tools and all three new tools against
sample data, including the worked Aria Fit example in
`examples/aria-fit/`.

## The workflow for one video

1. Idea and format: `/yt-plan` or `/yt-series`.
2. AI video prompt, when the video is AI generated:
   `/yt-ai-prompt`, with the character lock and negative prompt.
3. Script and hook: `/yt-script`.
3. Title and thumbnail: `/yt-package`.
4. Description and search: `/yt-seo`.
5. Publish check: `/yt-publish`, last, always.
6. After it is live: `/yt-comment`, `/yt-retention`, and
   `/yt-analytics`.

Or start at `/yt-hub` and let it route you.

## The fine print, kept from the original

- It does not publish. YouTube's Data API would allow it with
  your own OAuth. It is still not built here.
- `hookscore.py` and `shorts_score.py` are heuristics, not
  predictors. A low score is a reason to look again; a high
  score is not a promise.
- The formula classifier is about the words, not the result.
- `/yt-viral` reads, it does not scrape. Public listings only.
- Tags barely matter, and this pack says so.
- Nothing invents a number. If a skill wants a figure it does
  not have, it asks you for it or writes the line without it.

## Licence

MIT. Use it, change it, ship it. Original pack copyright Jake
Schincariol, next-level additions in this folder are also MIT.
