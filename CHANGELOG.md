# Changelog

## v3.3.1, algorithm update, 26 October 2026

Only `yt-algorithm` changes. Skill count unchanged at 33,
tool count unchanged at 17, file count unchanged at 124,
original author credit and MIT licence unchanged. Local
only at build time; GitHub push is a separate decision.

- `yt-algorithm`: new section "retrieval vs ranking" from
  chenxingqiang/YouTube-DNN-RecSys, an implementation of
  Covington et al. 2016. The repo was read in code, not
  just in its README: it implements candidate generation
  only (last 5 watched videos averaged into a user vector,
  16 continuous features, 500 items, old TensorFlow 1
  code), with no ranking-model code, no live YouTube data,
  and no Shorts-specific code.
- The five additions, all as a working model, never as an
  official formula: (1) retrieval failure ("barely shown")
  vs ranking/hook failure ("shown but swiped") as two
  different diagnoses; (2) audience cluster, not just
  keywords, as the retrieval check; (3) freshness and an
  exploration window — judge a direction over 5–10 Shorts,
  not from one Short alone; (4) signal strength — swipe,
  like on its own, and single-word comments are weak,
  while re-watch, share, subscribe from the Short, a
  next-skill comment, and return viewers are strong;
  (5) a retrieval question for every Short: who should
  the system retrieve this for, and what would prove it?
- Deliberately NOT added: no official weights, no
  percentage thresholds, no best-time table, no
  trending-sound chasing, no re-upload guidance, no
  scraping or botting, and no claim that the DNN
  predicts Shorts performance. The DNN is 2016 long-form
  work and does not cover swipe, loop, sound, captions,
  AI disclosure, or originality penalties.

## v3.3.0, audit fixes, 26 October 2026

Fixes from a deep audit of v3.2.0 (26 October 2026). Skill count
unchanged at 33, tool count unchanged at 17, original author
credit and MIT licence unchanged.

- `yt-plan` (FIRST change to an original skill): the old rule
  "three uploads a week, never daily" is removed. The skill now
  asks the cadence first — Daily Shorts mode (one Short a day
  via `/yt-shorts-first`, plus a weekly anchor if the channel
  makes long-form) or Weekly mode (anchor, cheap one, three
  Shorts from the anchor). A daily Shorts channel is no longer
  planned as if it were a weekly channel.
- README Install: the clone URL pointed at the original
  upstream repo, which would install v1.0, not this pack. It now
  clones this repo (`johnusa1598-sketch/yt_advanced_agent_skill`).
  The Test section's "ten newer tools" is corrected to eleven.
- CI: new `.github/workflows/test.yml` runs
  `python3 tests/test_tools.py` on every push and pull request.
  Tests existed before; nothing ran them automatically.
- Voice profile paths: six original skills (`yt-audit`,
  `yt-comment`, `yt-package`, `yt-plan`, `yt-script`, `yt-seo`)
  and `templates/voice.md` pointed only at
  `~/.claude/youtube/voice.md`. They now point at the channel
  voice profile (`templates/voice.md`) first, with the Claude
  Code path as the fallback. `yt-shorts-first` is aligned to
  the same wording.
- `yt-test`: thumbnail Test & Compare still has no Shorts
  (2026 reports; July 2026 rollout did not change that), but
  video-cut A/B testing — up to three cuts, judged on
  watch-time share, for Shorts and long videos — was announced
  at Made on YouTube (September 2026) with availability coming
  in 2027 per third-party reporting. The skill now tells you to
  check Studio first instead of blurring the two tests, and
  keeps the manual cover protocol for covers.
- `skill.yaml` descriptions aligned to the SKILL.md frontmatter
  for `yt-anti-glitch`, `yt-production`, `yt-qa`, `yt-story`,
  and `yt-test` (wording only, no behaviour change).
- Note: the original eleven skills were kept byte-identical
  from v1.0 through v3.2.0. v3.3.0 is the first version to
  touch them, and only for the two items above (yt-plan
  cadence, voice paths). Everything else in them is unchanged,
  and `workspace/youtube-agent/upstream/` is still the pristine
  original for comparison.


- Format lock (added to v3.3.0 at the user's request, same
  release): every Shorts video this skill generates must be
  vertical 9:16 portrait (1080x1920, full frame) and look shot
  on iPhone — handheld smartphone look, natural phone-camera
  optics. `prompt_builder.py` now writes a [FORMAT LOCK] block
  into every full prompt, the short prompt, and the negative
  prompt (which now also bans 16:9, letterbox, pillarbox, and
  cropped horizontal footage). The lock is also in
  `yt-ai-prompt`, `yt-shorts-first`, `yt-production` (hook frame
  included), `yt-publish` (checklist), `yt-qa` (hard format gate,
  like the face gate), and `templates/ai-video-prompt.md`. A
  non-9:16 or non-iPhone-looking render fails QA even if its
  scorecard passes.

## v3.2.0, 2026 signals update, 26 October 2026

Web research (26 October 2026, third-party guides and studies,
not official YouTube thresholds — every range is orientation
only, and a channel's own median overrides it):

- `yt-algorithm` + new `references/2026-signals.md`: viewed vs
  swiped away as the Shorts first gate (reported healthy range
  roughly 70–90%), first-3-seconds leak vs completion diagnosis,
  satisfaction signals (surveys, repeat viewing, session
  continuation, shares, comment sentiment), CTR by traffic
  source and retention by length as orientation ranges only,
  Metricool 2026 frequency finding (per-post best at 2–4/week,
  monthly totals climbing with volume — quality rule unchanged,
  no generic best-time table), and Shorts thumbnails' second
  job on grid, search, and related panels.
- `yt-shorts-first`: five hook patterns, the statement-proof-
  promise hook formula, visual change every 2–4 seconds,
  caption and loop rules, 20–35 second length orientation,
  single CTA in the payoff, two-hook staggered testing.
- `yt-originality`: May 2026 AI auto-labelling, reported —
  prominent single-format labels (overlay on Shorts, below
  player on long-form), YouTube applying the label itself for
  undisclosed photorealistic AI, correction in Studio except
  for Veo/Dream Screen and C2PA fully-generative files, where
  the label is permanent. Rule unchanged: disclose yourself
  at upload, every time.
- Deliberately NOT added: any benchmark presented as an
  official YouTube threshold, a generic best-time table,
  trending-sound chasing, publishing/comment automation,
  watermark removal, or re-upload guidance.
- Version bumped to 3.2.0; plugin and marketplace descriptions
  corrected to thirty-three skills (they still said
  twenty-nine / seventeen). Skill count unchanged at 33,
  tool count unchanged at 17, original author credit and MIT
  licence unchanged.


## v3.1.0, production-system tier, 24 October 2026

This release includes the previously unpushed v3.0.1 clean-output
rule below, because GitHub is still at v3.0.0 — v3.1.0 is the
first push since v3.0.0, so it carries both. Production-system
pieces taken from the Aria Fit final video template, rewritten
as GENERIC skills (Aria is only the worked example, never the
only character):

- `yt-production`: the two-step pipeline (hook-frame image
  prompt, then video prompt from that frame), separated
  copy-paste blocks, and the director-preamble +
  reference-discipline rules (reference mandatory on every
  generation; the forbidden three; verbatim preamble).
- `yt-story`: Story DNA (eight elements + arc + the QC rule
  that a missing beat fails QC), the mandatory parasocial beat,
  the eye-contact split rule (static = lens, dynamic = landing
  spot), the loop bridge dual-mode (static rebound / dynamic
  mid-takeoff cut), and the comment trigger.
- `yt-anti-glitch`: the Skill-Safety Ladder (simplify one rung
  on hook-frame glitch), banned multi-axis twisting combos
  only, the approved-skills list, the face-visibility lock,
  the single continuous shot, the separation rule for duos,
  the variety rotation matrix, the title-first gate, the
  never-retry-denied rule, and the glitch burst rule (two
  fails = switch concept, no third attempt).
- `yt-qa` + `scorecard.py`: the segment method (one generation
  = one skill, assembled 2–4s segments), beat verification,
  face-crop QC, the ten-point scorecard with its publish
  threshold (total ≥ 8 AND identity ≥ 2 AND movement ≥ 2),
  and the face gate hard fail.
- `yt-ai-prompt` extended (tool output unchanged): the realism
  core documented — skin, hair physics, imperfections, sweat
  progression, background life, smartphone optics — alongside
  the clean-output rule from v3.0.1.
- `yt-hub` routing and workflow updated for the new skills
  (anti-glitch → production → story → script → … → QA gate
  before the originality gate and publish check).

## v3.0.1, clean-output rule, 24 October 2026

- `yt-ai-prompt`: the negative prompt now demands a clean render
  explicitly — no watermark, no logo, no burned-in subtitles or
  text except the text layers the package itself specifies — plus
  a clean-output rule in the skill doc: clean means generated
  clean, never strip another tool's watermark; use that tool's
  watermark-free export instead.
- `yt-publish`: the pre-publish checklist gains a clean-render
  check (watch the render itself for watermarks, logos, and
  burned-in text).

## v3.0.0, algorithm-aware pro tier, 24 October 2026

### Added (research finalisation, same version)

Research: `research_notes/youtube-creator-pack-gaps-2026-20261024-1204/report.md`
(24 October 2026, index-only research, not a live Studio session).
Its ranked shortlist, implemented in full, taking the pack from
23 to 29 skills and from thirteen to sixteen tools:

- `yt-diagnose` + `diagnose.py`: a Studio-CSV analyser that
  reads the gates in order - impressions, CTR / chose-to-view,
  retention, return viewers - against the peer median in the
  same export. Low hook + high retention reads as packaging;
  high hook + low retention as content or promise; barely any
  shown-in-feed reads as not tested, not a hook failure. No
  global benchmarks, no invented thresholds.
- `yt-originality` + `originality_scan.py`: the pre-publish
  gate - substance variation measured across recent uploads,
  the 1 October 2026 Shorts originality prioritisation
  (voiceover, small edits, and same-template application do
  NOT count as original), the 15 July 2025 YPP "inauthentic
  content" rule (vary substance, not intro/outro), and the AI
  disclosure decision tree (photorealistic AI gymnast doing a
  real-looking skill must be disclosed; AI scripts, titles,
  captions, and own-voice cloning are exempt). Flags questions
  for a human; it never verdicts a policy question.
- `yt-bridge`: Shorts-to-long-form routing - Related Video is
  the only in-player route (no end screens on Shorts), Shorts
  Series seasons and episodes (gradual, YPP-first rollout from
  23 September 2026 - check Studio), a series bible template,
  and a conversion tracker. The 0.5-1% vs 0.04% conversion
  figures are reported as a third-party benchmark with their
  uncertainty flagged, never as YouTube figures.
- `yt-test`: Test & Compare log for long-form (up to 3
  variants, watch-time share as the judge, up to 2 weeks, the
  1280x720 floor) plus the manual Shorts-cover protocol,
  because Test & Compare does NOT cover Shorts.
- Caption and audio extension to `yt-sound` (not a duplicate
  skill): `srt_qa.py` checks timing overlaps, reading speed,
  line length and count, and missing punctuation, with an
  optional safety-words check for translated captions; plus
  the audio licence log template (Shorts-library tracks are
  Shorts-only; no seconds-length is safe by default) and the
  auto-dub review checklist (February 2026, 27 languages,
  Expressive Speech in 8).
- `yt-community`: pinned-comment, poll, and community-post
  routine - drafts only, never automation. Polls tied to the
  next video, pinned within 5-30 minutes, rotation of formats,
  80/20 value-to-promotion calendar.
- `yt-monetize`: the YPP runway planner - current thresholds
  and the 1 February 2027 change for new applicants (1,000
  subscribers + 8,000 hours/365 days OR 20 million qualified
  Shorts views/90 days, up from 4,000/10 million), the 10
  million/90-day Shorts pool maintenance rule, terms acceptance
  by 31 January 2027, the 45% Shorts pool creator share, and
  RPM honesty (cents vs long-form dollars, ranges vary - never
  a fixed RPM).
- `yt-algorithm` updated with the 2026 warnings: the Shorts
  view redefinition (31 March 2025, engaged views as the old
  definition) and its extension to all formats (24 August
  2026); Made on YouTube September 2026 items (Ask Studio
  feedback, dynamic thumbnails, coming 3-cut video A/B tests);
  and auto-dubbing (February 2026, 27 languages, Expressive
  Speech in 8).
- `yt-hub` routing updated for all six new skills, and the
  one-video workflow now runs the originality gate before the
  publish check, diagnosis after publication, and community,
  bridge, and test work between uploads.
- Templates: `series-bible.md`, `audio-licence-log.csv`,
  `test-compare-log.md`, `ypp-runway.md`,
  `originality-gate.md`, `community-routine.md`.
- Worked example: `examples/aria-fit/series-bible.md` for the
  30-Day Splits series.
- Tests now cover all three new tools in human and JSON
  output, plus fixtures for a Studio export, an SRT file, and
  a recent-uploads list. The full suite is still ALL PASS.
- Deliberately NOT added: a generic "best time to post" table
  (the data contradicts itself - the pack uses the creator's
  own Audience heatmap instead), trending-sound chasing
  (licence risk, low weight for Shorts), any publishing or
  comment automation, watermark removal, re-upload guidance,
  template factories varying only intro/outro, another
  title/tag generator, and any benchmark presented as a
  YouTube-published threshold. The hook/loop blueprint from
  the shortlist was also not added as a separate skill: it is
  already covered by `yt-viral-loop`'s retention plan and
  `yt-shorts-first`.

### Added

- Six new skills, taking the pack from 17 to 23: `yt-algorithm`,
  `yt-trends`, `yt-post`, `yt-sound`, `yt-meme`, and the
  orchestrator `yt-viral-loop`.
- Three new dependency-free Python tools, taking the pack from
  ten to thirteen: `trend_pack.py`, `package_builder.py`, and
  `retention_plan.py`.
- `yt-algorithm`: a working model of YouTube ranking for Shorts
  and long-form (CTR, retention, swipe-away, session, search
  match, returning viewers), framed honestly as a model with a
  Studio validation check for every claim - no invented
  thresholds, no fake official facts.
- `yt-trends` + `trend_pack.py`: hashtag and keyword packs in
  broad, niche, branded and evidence-seen tiers, plus
  search-intent clusters. The tool works from evidence the user
  pastes in and marks everything else as heuristic; it never
  claims live trend data it did not fetch. Includes the method
  for finding what is currently trending.
- `yt-post` + `package_builder.py`: the pro packaging pipeline -
  title variants with CTR reasoning, description, tags,
  thumbnail brief, timed text-layer script, end-screen CTA,
  upload timing guidance, pinned comment idea, and an A/B test
  plan, as JSON and Markdown.
- `yt-sound`: mood and tempo mapped to video energy, licence-safe
  music sources, meme sound effects, ducking, and Shorts loop
  points.
- `yt-meme`: format selection, punchline placement and timing,
  caption styling, trend-jacking without cringe, and a meme
  library method. Recreate, do not rip.
- `yt-viral-loop` + `retention_plan.py`: the end-to-end chain
  (prompt, brief, algorithm pass, trends, packaging, analytics
  feedback) and a retention curve plan - hook 0-3s, beats with
  purposes, drop-off guards, loop point, rewatch trigger.
- Template: `templates/publish-package.md` brief shape.
- Worked example: `examples/aria-fit/beam-backflip-package.md` -
  one AI Short from raw idea to algorithm-tuned package, built
  with the new tools.
- Tests now cover all three new tools in human and JSON output,
  plus a structural check that every skill ships a SKILL.md and
  a skill.yaml. The full suite is still ALL PASS.

### Changed

- `yt-hub` routes the new requests: "algorithm", "trends /
  hashtags", "package / publish", "music", "memes", and "viral"
  now reach the new skills, and the one-video workflow runs the
  algorithm pass, trends, sound, meme slots and full package
  before the publish check. `/yt-viral-loop` runs the whole
  chain.
- README and plugin manifest updated to 23 skills and 13 tools.

### Kept, unchanged

- All eleven original skills, the MIT licence, and the
  original author's credit.
- The core rule: nothing here publishes, and nothing here
  generates or renders video by itself. These skills write
  prompts, briefs and packages; you render and upload.

## v2.1.0, prompt engineering injected, 24 October 2026

### Added

- One new skill, taking the pack from 16 to 17: `yt-ai-prompt`.
- One new dependency-free Python tool, taking the pack from
  nine to ten: `prompt_builder.py`.
- A 7-layer prompt framework: character lock, scene lock,
  timed action beats with physics, camera, style and light,
  hook and loop, and negative and guardrails, plus three
  variants that keep the lock and change only camera and
  motion emphasis.
- A prompt library method: locked character prompts, scene
  prompts per location, and motion prompts per skill, so new
  prompts reuse locks and change only beats and camera.
- Templates: `ai-video-prompt.md` brief.
- Worked example: `examples/aria-fit/ai-brief.json` and the
  full prompt it builds in `ai-prompt-example.md`, using the
  locked Aria character spec.

### Changed

- Prompt engineering is now injected, not separate. `yt-hub`
  routes AI video prompts to `yt-ai-prompt` first, `yt-shorts-first`
  builds its AI prompt from the same brief, and `yt-series`
  turns its character spec into the prompt lock.
- Tests now cover `prompt_builder.py` in both human and JSON
  output, and the full suite is still ALL PASS.

### Kept, unchanged

- All eleven original skills, the MIT licence, and the
  original author's credit.
- The core rule: nothing here publishes, and nothing here
  generates video by itself. These skills write prompts and
  you render and upload.

## v2.0.0, next level, 24 October 2026

### Added

- Five new skills, taking the pack from 11 to 16:
  `yt-shorts-first`, `yt-series`, `yt-analytics`, `yt-publish`,
  and the router `yt-hub`.
- Three new dependency-free Python tools, taking the pack from
  six to nine: `shorts_score.py`, `analytics.py`, and
  `publish_check.py`.
- Muse compatibility: a `skill.yaml` beside every skill, so the
  pack is discoverable in Muse as well as in Claude Code. The
  original Claude frontmatter in each `SKILL.md` is unchanged.
- Templates: `channel.md`, `series.md`, and a single
  `video-brief.md` that every skill reads and hands on unchanged.
- Tests: `tests/test_tools.py` with sample fixtures, covering
  the original hook and title tools and all three new tools.
- Worked example: `examples/aria-fit/` with a filled-in channel
  profile and a 21-video analytics sample.

### Changed

- `yt-plan` is no longer the only planning shape. Shorts-first
  channels now use `yt-shorts-first` for a daily Short and
  `yt-series` for arcs, while `yt-plan` keeps the weekly
  anchor-plus-cheap-plus-Shorts shape for long-form channels.
- The publish step is now explicit. `yt-publish` runs last in
  every workflow and checks AI disclosure, playlist, chapters,
  and end screen before anything goes out.

### Kept, unchanged

- All eleven original skills, all six original Python tools,
  the MIT licence, and the original author's credit.
- The core rule of the original pack: nothing here publishes.
  These skills write. You upload.

## v1.0.0, upstream

- Eleven Claude skills and six Python tools, by Jake Schincariol,
  MIT licence, as published at
  https://github.com/Jakeschincariol/youtube-agent-skill
