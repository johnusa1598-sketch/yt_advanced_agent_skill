# The YouTube agent skill, next level

Thirty-four skills that run a YouTube channel, up from eleven.
Free, MIT, no signup, no API key, nothing to connect.

**Original pack, by Jake Schincariol, MIT licence:**
https://github.com/Jakeschincariol/youtube-agent-skill
This next-level version keeps all eleven original skills and all
six original tools unchanged, and adds twenty-two skills, eleven
tools, prompt engineering for AI video, an algorithm-aware pro
tier, a research-finalised diagnosis, originality, bridge, testing,
community, and monetisation tier, a production-system tier
(two-step pipeline, story spine, anti-glitch, QA scorecard), Muse
compatibility, templates, tests, and worked examples.
v3.2.0 (26 October 2026): 2026 signals update — viewed vs swiped
away, five hook patterns, pacing and loop rules, CTR/retention
orientation ranges, and May 2026 AI auto-labelling, all flagged
as third-party research, not official thresholds.
v3.3.0 (26 October 2026): audit fixes — daily planning in
`yt-plan`, install pointing at this repo, CI, channel voice
profile paths, aligned skill descriptions, and the video-cut
A/B check in `yt-test`.
v3.3.1 (26 October 2026): algorithm update in `yt-algorithm`
only — retrieval vs ranking, audience cluster, freshness
and exploration window, and weak vs strong signals, from
YouTube-DNN-RecSys (2016 paper, candidate-generation demo
only, no live data, no official weights).
v3.3.2 (26 October 2026): production gates from the October
2026 front-split video review — suspense hook frame, text-end
rule, audio loudness and beat gate, parasocial beat cap, and
vote pinned comment for comparison Shorts.
v3.3.3 (26 October 2026): leotard colour rotation — fixed
5-colour cycle (purple anchor, teal, black, royal blue,
burgundy), one planned slot per video, everything else locked.
v3.3.4 (26 October 2026): format clarification — hard gate
is ratio + iPhone look, 1080x1920 is preferred, 720x1280 at
the same ratio passes, phone-look scores look not pixels.
v3.3.5 (26 October 2026): nose ring clarification — character's
RIGHT nostril wing only, frontal view me image ke LEFT side
par, kabhi septum, centre, nose tip ya do rings nahi, aur
QA me side sirf frontal frame par check hogi.
v3.3.6 (27 October 2026): audit fixes — two-stage diagnostic
split spelled out, viral-loop chain mirrors the hub gates,
tools kept to their skills' promises (scorecard hard gates,
publish checks, vote comment, outfit palette, realism core,
loudness measurement), October 2026 landscape updates
(AI music labels, likeness correction, originality nuances,
branded content, GIF comments, Studio columns).
v3.3.7 (27 October 2026): rewatch engineering — seamless
loop checks on top of the FINAL dual-mode bridge, one named
rewatch trigger per Short (hidden detail, missed moment,
count-the-detail, satisfying payoff, fast payoff + slow
reveal, end reframe), loop + rewatch QA gates, honest Studio
read (APV >100% = loop, engaged views = money).
v3.4.0 (27 October 2026): edit tier — hyperframe-edit skill
(supplied clips into a polished 9:16 HyperFrames edit) plus
the merged FFmpeg + HyperFrames pipeline script (clean →
check/snapshot/render → audio finish/mux → QC report);
v3.3.6 + v3.3.7, previously local only, go live in this push.
v3.4.1 (27 October 2026): hyperframe-edit upgrade against
upstream HyperFrames 0.8.207 — starter template fixed (was
failing lint with 6 errors), lint gate before check, native
grades/audio, transcribe default, vertical safe areas,
registry components, pipeline aspect fix.
v3.4.2 (27 October 2026): peak-tension fix — Part 8/9 renders
go weak at the peak beat, so the peak is now written as
sustained effort (never a state), split into its own
segment when it sits 5+ seconds from the anchor, and
gated in QA (scorecard --peak-tension sustained/released).
v3.4.3 (27 October 2026): Part 10 edit defects — frozen
timecode now ticks from the timeline, text inventory gate
(no metadata labels render), post-peak gap cap (a beat,
never a gap, between peak and tail).
See `CHANGELOG.md` for exactly what changed.

**Nothing gets published until you do it.** These skills write.
You upload.

## The thirty-four

| command | what it does |
| --- | --- |
| `/yt-hub` | Routes any YouTube request to the right skill. |
| `/hyperframe-edit` | NEW in v3.4 (edit tier). Supplied clips into a polished 9:16 short: HyperFrames kinetic edit, live grades, merged FFmpeg pipeline, QC report. Editing only, never generates clips. |
| `/yt-production` | NEW in v3.1 (production tier). Two-step AI video: hook-frame image first, then video from that frame, with reference discipline. |
| `/yt-story` | NEW in v3.1 (production tier). Story DNA: eight elements in a fixed arc, parasocial beat, eye-contact rule, dual-mode loop bridge, comment trigger. |
| `/yt-anti-glitch` | NEW in v3.1 (production tier). Skill-safety ladder, banned combos only, face-visibility lock, duo separation, glitch burst rule. |
| `/yt-qa` | NEW in v3.1 (production tier). Pre-publish QA: segment method, beat verification, face-crop QC, ten-point scorecard with publish threshold, face gate. |
| `/yt-diagnose` | NEW in v3 (research finalisation). A Studio CSV export read gate by gate: reach, hook, retention, return viewers - and the one fix. |
| `/yt-originality` | NEW in v3 (research finalisation). The pre-publish gate: substance variation, AI disclosure, health claims, dangerous moves, human sign-off. |
| `/yt-bridge` | NEW in v3 (research finalisation). Shorts views into long-form watch time: Related Video routing, Shorts Series, series bible. |
| `/yt-test` | NEW in v3 (research finalisation). Test & Compare log for long-form, manual cover protocol for Shorts. |
| `/yt-community` | NEW in v3 (research finalisation). Pinned comments, polls, and community posts - drafts only, never automation. |
| `/yt-monetize` | NEW in v3 (research finalisation). The YPP runway planner: current thresholds, the 1 February 2027 change, the Shorts pool rules. |
| `/yt-viral-loop` | NEW in v3. The whole chain for one video, end to end, plus its retention plan. Start here for a full pipeline. |
| `/yt-algorithm` | NEW in v3. A working model of YouTube ranking for Shorts and long-form, with the Studio check for every claim. No invented numbers. |
| `/yt-trends` | NEW in v3. What is moving in a niche, turned into a hashtag and keyword pack from evidence you supply. |
| `/yt-post` | NEW in v3. The full publish package at once: titles, description, tags, thumbnail brief, text layers, timing, pinned comment, A/B plan. |
| `/yt-sound` | NEW in v3. Music and sound design: mood and tempo mapped to energy, licence-safe sources, meme effects, loop points. Extended in the research finalisation with the SRT QA script, the audio licence log, and the auto-dub review checklist. |
| `/yt-meme` | NEW in v3. Meme slots done right: format selection, punchline timing, caption styling, trend-jacking without cringe. |
| `/yt-ai-prompt` | Next-level AI video prompts: 7 layers, locked character, timed beats with physics, camera, style, negative prompt, and three variants. |
| `/yt-script` | One idea into a script. Five hooks off 21 formulas, scored, then the spoken script with retention beats marked. |
| `/yt-package` | Title and thumbnail as one pairing, linted for truncation, duplication and vagueness. |
| `/yt-edit` | A transcript into an edit decision list: dead air, filler cues, retakes, with timecodes. |
| `/yt-comment` | The comment section triaged into four piles, then replies in your voice. Says which one to pin. |
| `/yt-plan` | A week that fits the hours you actually have. One anchor, one cheap one, three Shorts. |
| `/yt-viral` | What is working in your niche, ranked by multiple over each channel's own median. |
| `/yt-retention` | Your retention export read properly: hook leak, the cliffs, the slide, and what to change. |
| `/yt-shorts` | The Shorts already inside a long video, with a new first line written for each. |
| `/yt-shorts-first` | A Shorts-first daily workflow: first two seconds, one idea, a loop point, one call to action, and a series it belongs to. |
| `/yt-series` | A series bible, a locked character spec, and an episode log, so a series compounds instead of repeating. |
| `/yt-analytics` | Your own numbers read properly: subs per 1000 views, format averages, outliers over the median, and one fix. |
| `/yt-publish` | The last check before a video goes out: title, thumbnail, description, AI disclosure, playlist, chapters, end screen. |
| `/yt-seo` | The description, the tags that are worth having, and the three queries this should win. |
| `/yt-chapters` | Chapters from a transcript, validated against YouTube's own rules so they render. |
| `/yt-audit` | The whole channel, ending in ONE fix rather than twenty. |

## The eighteen tools

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
python3 skills/yt-trends/trend_pack.py "beam backflip" --niche "AI gymnastics" --brand "Aria Fit"
python3 skills/yt-post/package_builder.py brief.json --trends trends.json
python3 skills/yt-viral-loop/retention_plan.py brief.json
python3 skills/yt-diagnose/diagnose.py studio-export.csv
python3 skills/yt-sound/srt_qa.py captions.srt --safety-words safety.txt
python3 skills/yt-originality/originality_scan.py uploads.json
python3 skills/yt-qa/scorecard.py --identity 3 --movement 2 --phone 2 --beats 2
python3 skills/yt-sound/loudness.py <audio-file>
```

## Install

Claude Code, this pack (the original pack remains the upstream
credit at https://github.com/Jakeschincariol/youtube-agent-skill):

```bash
git clone https://github.com/johnusa1598-sketch/yt_advanced_agent_skill.git
cp -r yt_advanced_agent_skill/skills/yt-* ~/.claude/skills/
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
original hook and title tools and all eleven newer tools against
sample data, including the worked Aria Fit example in
`examples/aria-fit/`.

## The workflow for one video

1. Idea and format: `/yt-plan` or `/yt-series`.
2. AI video prompt, when the video is AI generated:
   `/yt-ai-prompt`, with the character lock and negative prompt.
3. Script and hook: `/yt-script`.
4. Algorithm pass: `/yt-algorithm` - one prediction to test.
5. Trends: `/yt-trends` - the hashtag and keyword pack.
6. Sound and meme slots: `/yt-sound`, then `/yt-meme`.
7. The full package: `/yt-post`, with the retention plan from
   `/yt-viral-loop`.
8. Description and search: `/yt-seo`.
9. Originality, disclosure, and safety gate: `/yt-originality`,
   before anything goes out.
10. Publish check: `/yt-publish`, last, always.
11. After it is live: `/yt-comment`, `/yt-retention`,
    `/yt-analytics`, and `/yt-diagnose` - and the one fix feeds
    the next brief.
12. Between uploads: `/yt-community` drafts, `/yt-bridge`
    routing, `/yt-test` logging, and `/yt-monetize` runway
    checks.

Or start at `/yt-hub` and let it route you, or at
`/yt-viral-loop` and let it run the whole chain.

## The fine print, kept from the original

- It does not publish. YouTube's Data API would allow it with
  your own OAuth. It is still not built here.
- It does not render video. These skills write prompts, briefs
  and packages; you render and upload.
- `hookscore.py` and `shorts_score.py` are heuristics, not
  predictors. A low score is a reason to look again; a high
  score is not a promise.
- `trend_pack.py`, `package_builder.py` and `retention_plan.py`
  are planning tools, not predictors. Trend packs built without
  evidence are heuristics, clearly marked as such.
- The formula classifier is about the words, not the result.
- `/yt-viral` reads, it does not scrape. Public listings only.
- Tags barely matter, and this pack says so.
- Nothing invents a number. If a skill wants a figure it does
  not have, it asks you for it or writes the line without it.
- `/yt-algorithm` is a working model, not an official spec.
  Every claim in it names the Studio check that would prove or
  break it on your own channel. Its 2026 warnings (view
  redefinitions, Made on YouTube tooling, auto-dubbing) are
  dated and sourced to the research notes, and third-party
  benchmarks anywhere in the pack are labelled as third-party,
  never as YouTube figures.
- `/yt-diagnose` reads only the Studio CSV you export. It
  judges videos against their peers in the same file, never
  against a global benchmark.
- `/yt-originality` flags questions for a human; it never
  verdicts a policy question, and it never automates
  publishing, comments, watermark removal, or re-uploads.
- `/yt-monetize` never quotes a fixed RPM. Revenue maths uses
  your own Studio RPM and your own engaged views, or it says
  it is a guess.

## Licence

MIT. Use it, change it, ship it. Original pack copyright Jake
Schincariol, next-level additions in this folder are also MIT.
