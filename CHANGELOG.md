# Changelog

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
