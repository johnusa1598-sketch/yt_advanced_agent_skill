# Changelog

## v3.5.0, duel-format upgrade, 29 October 2026

Channel data (user Studio data, October 2026) behind this
upgrade: channel average viewed vs swiped away 59.8%,
top Shorts 68–73%; Poll Duel: Back Handspring vs Front
Aerial 16.4K views at 120.5% average view percentage.
The Duel is the format that closes the average-to-top
gap: a vote is a decision, and a decision replays.
Skill count unchanged at 34, tool count unchanged at
18, file count unchanged at 141.

- **Duel format, vote-decides-next, ladders, episodic
  CTA (yt-story):** two skills, one question ("A or
  B?"); both sides named in video order in the first
  2 seconds, both attempts genuinely hard and clean,
  vote CTA inside the payoff beat, pinned comment is
  the vote; the winning side BECOMES the next video
  and the next video says so. Variants: progression
  ladder (Level 1 to Level 5, finale planned first),
  Road to Mastering (Day 1 vs Day 7, honestly weaker
  Day 1), Testing Your Challenge Requests (most-voted
  request attempted, runner-ups addressed). Subscribe
  ask names the next episode's stake, never generic.
- **Vote-decides-next log field, ladder arcs
  (yt-series):** episode log records the vote result
  and whether it was honoured; an unhonoured promise
  is logged as broken. Ladder arcs record the tier
  reached per episode.
- **First-hours replies (yt-community):** reply to the
  first 5–10 comments in the first few hours, specific
  replies only, manual as always.
- **Aria Fit viewed-vs-swiped benchmark
  (yt-algorithm):** channel average 59.8%, top 68–73%,
  working target 68%+ for a new Short; under 60% is
  diagnosed as a hook failure first.
- **Deliberately unchanged:** yt-shorts-first (hook
  rules already say no greeting/intro/setup, text
  curiosity on frame one), yt-qa (vote-carries-the-ask
  gate already exists), yt-package (vote enforcement
  via publish_check.py unchanged).

## v3.4.5, hook-drop research upgrade, 28 October 2026

Deep research (27 October 2026) into why AI Shorts
look great at the hook and die in the middle found
two decays compounding: model decay (a single start
frame anchors the first seconds but is not a
persistent 3-D / physics memory, so conditioning
weakens with distance, chained steps accumulate
error, and 8–12s sits at or past single-shot
limits) and narrative decay (no beat after the
peak, so the hook's open loop closes and viewers
leave before the end card). The fix is not a
better prompt alone: a destination, short
segments, and a post-peak beat. Skill count
unchanged at 34, tool count unchanged at 18, file
count unchanged at 141.

- **End-frame conditioning, segment assembly,
  static-hold rescue (yt-production):** peak-as-
  end-frame where the tool supports first+last
  frames (Veo 2/3.1 [DOC], Kling, Hailuo,
  Firefly, Luma — verify in UI on generation
  day), peak-as-segment as fallback; 2–3 short
  anchored segments for 8–12s, cut on motion,
  trim heads/tails (about 3.5 usable seconds per
  5s clip, 8–12 frames off each start), one
  style line verbatim, same references,
  colour-match, one continuous audio track;
  extension/chaining is not the default (it
  compounds drift). Static holds get camera-only
  motion, a timer/progress overlay, or an
  editor-held peak frame — or a cut to 6–7s.
- **Post-peak beat, re-hooks, comment placement
  (yt-story):** payoff 3–5s before the end, CTA
  inside the payoff, never a trailing end card
  or logo; a cut, text twist, or sound accent at
  about 3.5s and about 7s [LORE cadence]; the
  comment prompt sits after the payoff only, one
  prompt of at most 6 words, rating-only, and
  is never claimed to hold viewers mid-video
  (no measured retention effect found).
- **Hook-drop gates (yt-qa, scorecard.py):** new
  beat-verification checks — end frame (or
  peak-as-segment fallback), segment cuts on
  motion, post-peak beat present, re-hook
  present, no trailing end card, no result
  revealed before the peak — each FAIL-FIXABLE
  even at 10/10, with matching NOT_VERIFIED
  entries and five new tests in
  tests/test_tools.py.
- **Prompt rules (yt-ai-prompt):** one subject
  action plus one camera move per segment,
  time-coded beats, and the honest limit on
  negatives: they are biases, not guarantees,
  and cannot override missing visual
  information or an overly complex shot.
- **Retention honesty (yt-algorithm):** YouTube
  publishes no 70%/85%/100% retention thresholds
  and no 8-second checkpoint. The VVSA 70–90% /
  60% figures and the 85% completion association
  already in this pack are relabelled as
  third-party lore, never YouTube rules; the
  documented mechanism stands (views count on
  start/replay since 31 March 2025, engaged
  views separate, rewatched segments can exceed
  total views).
- **Edit layer (hyperframe-edit):** re-hook
  overlays at about 3.5s and about 7s (§3.10),
  and editor-held peak plus progress overlay
  for holds, both inside the safe band and in
  the text inventory, with a matching Part 6
  gate line.

## v3.4.4, question–skill match and one way, 27 October 2026

Part 11 (deep squat hold, black Slot 3) repeats the
"good hook, dead video" pattern at the CONCEPT level,
not the edit level: v3.4.3's edit fixes all held
(ticking timecode, clean texts, no pill label,
sustained hold tension), yet the video is one pose
for 10 seconds. Skill count unchanged at 34, tool
count unchanged at 18, file count unchanged at 141.

- **Question–skill match (yt-anti-glitch title-first
  gate, yt-production, yt-qa):** the question type
  must match the skill type, checked before Step 1.
  Range questions ("HOW LOW?", "HOW HIGH?", "HOW
  FAR?") need a progressive skill — a visible journey
  from start to peak, the answer unfolding across
  the video, never sitting in frame 0. Duration
  questions ("CAN SHE HOLD IT?", "HOW LONG?") take
  a static hold, where time is the stake. A static
  hold under a range question is an invalid concept:
  change the question or change the skill, do not
  generate. Part 11 is the precedent — "HOW LOW?"
  over a deep squat hold answered itself in frame 0;
  the same footage under "CAN SHE HOLD THIS
  SQUAT?" would pass.
- **One way (yt-production, yt-story, yt-qa):** a
  video is made one way — one question, one skill,
  one arc. The hook, every beat, every text, and
  the body all tell the same single story. Text must
  never promise what the body does not show (Part
  11: "DOWN, SLOWLY" over a body that barely
  descends), and no beat may answer a different
  question than the title asks. A text–body split
  is a broken promise: the viewer leaves at the
  first frame where they notice. Both checks join
  scorecard.py's printed human-check list.

## v3.4.3, Part 10 edit defects, 27 October 2026

Part 10 (standing leg raise, teal Slot 2, rendered with
v3.4.2) carries three edit defects, all checked frame by
frame (1s, 5s, 6s, 8s, 9s, 10s). Skill count unchanged at
34, tool count unchanged at 18, file count unchanged
at 141.

- **Frozen timecode (hyperframe-edit):** the timecode
  read 00:00:00:00 in every sampled frame for all 10
  seconds. Cause in the repo: the starter template
  printed a static string and no tween ever updated
  it, while SKILL.md §3.6 promised "ticking in real
  time". Fix: the template now drives the timecode
  from the timeline's own time (onUpdate, 24fps
  HH:MM:SS:FF), and the skill requires a two-frame
  tick check before render. Same value at 1s and 5s
  = FAIL.
- **Metadata texts on screen (hyperframe-edit, yt-qa):**
  6–8s showed "TEAL SLOT 2" (rotation metadata),
  "STRONG HOLD" (beat label), "ARIA FIT" (channel
  bug) and a "prompt" label above the rewatch pill —
  the last one traced to the skill itself, whose
  chat-prompt card section specified a "prompt"
  label as part of the design. Fix: a text-inventory
  gate — every visible text listed before render,
  only approved texts ship (kinetic words, caption
  lines, rewatch pill line, CTA); metadata and
  component labels never render. The pill card now
  shows ONLY the instruction text. A kinetic word
  clipped at the frame edge (Part 10: "UP, SLOWLY"
  cut at the left edge) is also a FAIL: resize or
  reposition inside the safe band.
- **Post-peak gap (yt-story, yt-qa):** peak at ~5s,
  then 6–8s of nothing but the leg lowering, payoff
  only at 9–10s — the viewer decides the video is
  over when the skill finishes and leaves before the
  CTA. Fix: a post-peak rule — at most 2 seconds
  between the peak beat's end and the next beat
  without one; the skill's ending is not a beat; the
  edit cuts the dead lower or moves the payoff
  earlier. A completion word (CLEAN!, DONE) must
  appear only when the visual completes — Part 10
  showed "LEG RAISE, CLEAN!" while the leg was
  still lowering. Both checks join scorecard.py's
  printed human-check list.

## v3.4.2, peak-tension fix, 27 October 2026

The Part 8 pistol squat and Part 9 L-sit renders go weak
at the peak beat: the start is strong, but mid-video the
tension releases (L-sit: effort face on the lift, neutral
face on the hold) or collapses into strain (pistol: eyes
squeezed shut at the peak, peak form hidden behind text
and grade). Cause, checked in the repo: on suspense
titles the hook frame anchors the struggle, so the peak
is invented mid-video, far from the anchor, where the
model drifts — and no rule in the pack described the
peak as sustained effort. Skill count unchanged at 34,
tool count unchanged at 18, file count unchanged at 141.

- **Peak sustain (yt-story, yt-ai-prompt):** the peak
  beat is written as sustained effort, never as a state
  — limbs locked with no sag across the beat, slight
  tremor, braced core, set jaw, controlled breath,
  eyes per the eye rule; a neutral face, sagging limbs,
  or eyes shut at the peak is a failed peak. Peak form
  stays visible: no text or grade may cover the working
  limbs or the face during the peak beat. The realism
  paragraph in `prompt_builder.py` now emits this
  wording in every full prompt.
- **Peak as its own segment (yt-production):** for
  static holds whose peak sits 5+ seconds from the
  anchor, split the peak into its own segment —
  setup segment plus a peak segment generated fresh
  from its own peak-pose start frame — assembled to
  the same 8–12 second budget. Without its own anchor,
  the peak is always the weakest beat in the video.
- **Peak-tension gate (yt-qa, scorecard.py):** new
  check beside the scorecard, FAIL-FIXABLE even at
  10/10: `scorecard.py --peak-tension
  sustained/released`. Released (neutral face, sag,
  eyes shut, or covered peak form) fails.

## v3.4.1, hyperframe-edit upgrade (HyperFrames 0.8.207), 27 October 2026

The edit skill is upgraded against the upstream HyperFrames
repo (heygen-com/hyperframes, HEAD c2b68fb, release
0.8.207 pinned — unreleased main work is NOT pinned).
Skill count unchanged at 34, tool count unchanged at 18,
file count unchanged at 141. Original author credit and
MIT licence unchanged. The upgrade was verified, not
assumed: the old template was linted with 0.8.207 (6
errors, as documented below), the new template lints
with 0 errors, and the pack tests still pass ALL PASS.

- **Template fixed**: the starter composition failed
  current lint with 6 errors (no composition id, no
  dimensions, timeline on the wrong registry, video
  without its own data-start). Rewritten to the
  needle-edit shape that passes 0.8.207 lint with 0
  errors: video-as-clip, timeline on
  window.__timelines[compositionId] (plus
  timelines["main"]) after the tweens are built,
  stable ids on every treatment, GSAP local.
- **Lint gate**: `lint` now runs before `check` in the
  workflow and in the merged pipeline (both blocking);
  `check --json` and `check --at-transitions` added.
  The `audio_none` info on a muted composition is
  documented as not a failure.
- **Native grades + audio**: grades via
  data-color-grading / media-treatment / grade-compare
  (CSS filters now the fallback for non-media layers
  only); mix via native audio elements, data-automation
  lanes, data-fx-carve, normalize-audio --lufs -14
  (explicit — its default is -16). FFmpeg keeps only
  the final loudness finish + mux.
- **Transcription**: `hyperframes transcribe` is now
  the default (Parakeet/Whisper, small.en); faster-
  whisper stays as fallback. Output-schema mapping to
  the skill's timings shape must be verified on first
  use (stated in the skill).
- **Vertical safe areas**: top 168 px clear, band
  168–1330 px, captions at the bottom of the band,
  frame-0 hook, must work muted — added to the
  treatments and the ship gates (scaled for 720x1280).
- **Registry + tools**: named caption components
  (kinetic-slam, highlight, blend-difference,
  pill-karaoke), text-behind-subject cutout, opt-in
  speed ramps, sub-composition shape, themes,
  timeline CLI edits, snapshot --review/--against,
  render --quality draft|looks|delivery, beats +
  audio --read for the beat grid.
- **Pipeline fixes**: aspect-preserving scale
  (increase + crop — plain scale stretched non-9:16
  sources); --quality passthrough; doctor/browser
  ensure + 0.8.204 diagnostics in the failure notes.
- **Deliberately NOT added**: Studio/desktop flows,
  cloud rendering, HeyGen-gated media, HDR/4K
  supersampling, GIF/HLS/WebM transparency, decks,
  telemetry, deprecated aliases — listed in the skill
  so the skill does not drift again.
- **Upgrade procedure**: probe with
  `npx hyperframes@latest upgrade --project . --check`,
  apply, re-run check, name old → new versions;
  revert the pin on failure. Node requirement is
  now 22+ (24 verified).

## v3.4.0, edit tier, 27 October 2026

This push brings the local-only v3.3.6 and v3.3.7 to GitHub
and adds the edit tier. Skill count 33 to 34, tool count
unchanged at 18, file count 138 to 141 (four new files:
hyperframe-edit SKILL.md, starter composition template,
merged-pipeline script, skill.yaml; one binary test fixture
removed, see below). Original author credit
and MIT licence unchanged. Only work-relevant content is
included: the v3.3.8 needle lessons were NOT approved and
are not in this push, and no undecided item was bundled.

- **v3.3.6 + v3.3.7 now live** (previously local only):
  audit fixes including the two-stage diagnostic split,
  and rewatch engineering including loop + rewatch QA
  gates. See their entries below.
- **hyperframe-edit (NEW)**: edit supplied clips into a
  polished 9:16 short with HyperFrames (HTML + GSAP):
  kinetic typography, live grade transformations,
  magazine-cover graphics, chat-prompt cards, word-synced
  captions, sound design and mastering. Editing only —
  it never generates clips. Sample-first rule; the run
  ends with the ship-or-change verdict on the sample.
- **Merged FFmpeg + HyperFrames pipeline**
  (`tools/merged-pipeline.sh`): one command — FFmpeg
  pre-clean (fps/scale normalise, opt-in denoise/grade)
  → HyperFrames check (0 errors) → snapshot → render →
  FFmpeg audio finish (-14 LUFS / ≤ -1 dBTP, limit
  first) + mux → QC report (duration, resolution,
  loudness, loop-match diff). Proven end to end on the
  needle-hold edit (10.0s, 720x1280, -14.19 LUFS /
  -1.92 dBTP, loop diff 5.3).
- **Routing**: `/yt-hub` now routes supplied-clip editing
  to `/hyperframe-edit`.
- **Pushability fix**: snapshot pushes accept UTF-8 text
  only, so the binary loudness-test fixture
  (`tests/fixtures/tone-14lufs.wav`) cannot be pushed —
  and GitHub CI needs it to pass. The test now generates
  its own -14 LUFS tone with the Python standard library
  instead, so the pack stays self-contained and CI-green
  with no binary fixture in the repo.

## v3.3.7, rewatch engineering, 27 October 2026

Extra web research on what makes a Short earn a second watch,
encoded where it is checkable. Skill count unchanged at 33,
tool count unchanged at 18, file count 137 to 138 (one new
test fixture). Original author credit and MIT licence
unchanged. Local only; GitHub push is a separate decision,
not taken here.

Research, with source honesty: Shorts loop automatically;
since 31 March 2025 every replay counts as a public view
with no minimum watch time, while monetisation and YPP
eligibility run on engaged views; average percentage viewed
above 100% in Studio means viewers looped. What was NOT
found, and is therefore NOT claimed anywhere in this
version: any official YouTube ranking weight for loops.
Third-party guides widely call loops "one of the strongest
signals" — that is their claim, not a YouTube statement,
and the pack says so wherever loops are discussed. No
benchmark percentages from blogs (replay shares, retention
lifts, APV thresholds) were imported: every number in this
version is either a YouTube rule (31 March 2025 view
definition) or a pack rule (2-second tail cap, one trigger
per video).

- **Seamless loop engineering** (`yt-shorts-first`,
  `yt-story`): strengthens, never replaces, the FINAL loop
  bridge dual-mode (static rebound / dynamic mid-takeoff
  cut). Added checks: last 2 seconds match the first 2 in
  light, angle, and position; the beat continues across the
  join with no silence gap or pop; no subscribe end-card,
  black screen, or held goodbye frame after the ≤2 second
  tail (the CTA sits inside the tail, then the video loops).
  Motion hides the join only at the join itself — the video
  itself stays one continuous shot, no cuts, per FINAL.
- **One rewatch trigger per Short** (`yt-shorts-first`,
  `yt-story`, `yt-viral-loop`, `yt-qa`): the FINAL Easter
  egg rule, named in the brief (`rewatch_trigger`) before
  the shoot, from a fixed menu — hidden detail, missed
  moment, count-the-detail ("dobara dekho aur batao"),
  satisfying payoff, fast payoff + slow information reveal,
  end reframe. One only, so the second watch has exactly
  one job. The pinned comment asks about it; on a
  comparison Short the vote carries the ask (v3.3.6
  priority unchanged).
- **Checkable gates** (`yt-qa`, `scorecard.py`,
  `retention_plan.py`): loop match and rewatch presence are
  new QA gates (FAIL-FIXABLE even at 10/10) with
  `scorecard.py --loop-match matched/mismatch` and
  `--rewatch yes/no`; a trigger claimed in the brief but
  absent from the video is a fail, not a pass. The
  retention plan flags a Short with no trigger
  (`no-rewatch-trigger`) and carries a named trigger as a
  guard. Loop match and rewatch join the scorecard's
  not-verified banner when their flags are not supplied.
- **Honest Studio read** (`yt-algorithm`, `yt-analytics`):
  APV above 100% = loop working, read beside engaged views;
  raw views alone overstate a rewatchable clip; a loop that
  inflates views without engaged views or return viewers
  has proved nothing.
- **Retention design** (`yt-shorts-first`): pattern
  interrupts vary in type (angle, caption animation, sound
  cue, brief silence) so they do not habituate; the rewatch
  trigger IS the Short's open loop — no stacking several
  unanswered questions into 8–12 seconds.
- **Tests:** 58 to 62 checks, ALL PASS. New: retention plan
  with/without trigger, scorecard loop fail, scorecard
  loop + rewatch pass. New fixture
  `tests/fixtures/retention-rewatch-brief.json`.
- **Not encoded, and why — questions for the user:**
  (1) **Speed ramps** are excluded from the rewatch menu:
  their slow portion is slow-motion footage, which the FINAL
  template bans ("no slow-motion floatiness"). Question:
  keep the ban (no speed ramps at all), or allow a
  speed-ramp exception, and if so, speed-up portions only
  or slow portions too? (2) **Monday 26-October handstand
  pack** was approved as-is before the rewatch-trigger rule
  and carries no trigger; `yt-qa` exempts it until decided.
  Question: add a trigger to it (for example, "dobara dekho
  — hold me kitne micro-wobble the?"), or leave the
  approved pack untouched? (3) No conflict was found with
  the locked character spec: every trigger is about detail,
  pacing, or the comment, never about hair, glasses, nose
  ring, earrings, freckles, or outfit — so nothing in this
  version touches the character lock.

## v3.3.6, audit fixes (internal consistency + tools + landscape), 27 October 2026

Three read-only audits (internal consistency vs the FINAL
template and the recent review lessons; October 2026 landscape
research; all 17 tools vs their skills' promises) found 14
internal gaps, 8 landscape gaps, and 19 tool gaps. This version
fixes them locally. Skill count unchanged at 33, tool count 17
to 18 (new `loudness.py`), file count 124 to 137. Original
author credit and MIT licence unchanged. Local only; GitHub
push is a separate decision, not taken here.

- **Two-stage diagnostic, spelled out** (`yt-algorithm`,
  `yt-diagnose`, `diagnose.py`): low shown-in-feed vs peers =
  retrieval / candidate-stage failure (wrong audience cluster,
  niche mismatch) — fix by re-targeting the cluster or topic,
  not by rewriting the hook; good impressions + fast drop-off
  = ranking / retention failure, placed by the retention curve
  (first-3s cliff = hook, later slide = pacing). `diagnose.py`
  carries the mapping as a RETRIEVAL note on every NOT TESTED
  verdict, reports `peer_basis` per gate (same-format, or
  all-formats fallback when fewer than two same-format peers
  exist, never silent), and the retention finding now names
  the cliff-vs-slide read.
- **Viral-loop chain mirrors the hub** (`yt-viral-loop`):
  title-first + anti-glitch, production 2-step, Story DNA,
  then script; QA gate and originality + disclosure between
  the retention plan and the publish check. The old chain let
  a video ship without title-first, Story DNA, segment QA,
  the scorecard threshold, or the face gate.
- **Duration contradiction resolved** (`yt-shorts-first`,
  `yt-algorithm`): the 20–35s orientation is scoped to
  recorded/edited Shorts; AI-generated Shorts keep the hard
  8–12s (~9s) budget per `yt-production`, longer concepts
  decomposed into segments.
- **Mia duo-default + solo cap restored** (`yt-anti-glitch`,
  `yt-story`, `examples/aria-fit/series-bible.md`): duo is the
  default, solo the exception capped at the channel's stated
  weekly number (Aria Fit: 2–3/week, Mia the default
  co-star); on a solo slot CHEERS must still be witnessed.
- **Datasheet §8 appendix** (`templates/aria-datasheet-lock.md`,
  `yt-production`, `yt-ai-prompt`, `yt-qa`,
  `examples/aria-fit/ai-brief.json`): the FINAL template §15
  §8 block verbatim, with freckle/body/accessory locks and
  the Drift Check; the generic lock fields no longer silently
  replace it. A teal-slot example brief
  (`ai-brief-teal.json`) joins the purple Slot 1 brief.
- **Beat-track gate propagated** (`yt-production`,
  `yt-ai-prompt`): v3.3.2 supersedes FINAL on music — native
  audio alone fails; a licence-safe beat track from the first
  2s is required, −14 LUFS / ≤ −1 dBTP, music low, never
  louder than movement sounds.
- **Suspense rule, qualified everywhere** (`yt-production`
  worked example, `yt-shorts-first` shape rule): peak-action
  frame except on suspense-question titles, where frame one
  shows the struggle, not the payoff.
- **Vote pinned comment, propagated** (`yt-community`,
  `yt-story`, `yt-publish`, `package_builder.py`,
  `publish_check.py`): the vote rule now lives where pinned
  comments are drafted, with priority over the comment-trigger
  ask; `package_builder.py` emits the vote from
  `comparison_sides` (warns when a comparison brief has no
  sides) and `publish_check.py` fails a vote that misses a
  side.
- **Production nose gate completed** (`yt-production`): full
  `yt-qa` wording, including the second-centre-ring FAIL and
  the frontal-frame-only rule; `yt-qa` names the frontal
  face-visible beat (parasocial lens grin) as the verdict
  frame.
- **Leotard rotation, default holes closed**
  (`yt-ai-prompt`, `prompt_builder.py`,
  `examples/aria-fit/channel.md`): layer 7 bans changing
  outfit mid-shot (rotation across videos is the planned
  exception); the tool rejects leotard colours outside the
  five-colour palette (exit 2) and warns on the default
  purple with no `--outfit`; the channel example records
  the rotation and the last slot (teal); the cycle governs
  leotard slots, non-leotard matrix outfits are logged in
  the same series log.
- **Format headline fixed** (`yt-ai-prompt`): "1080x1920
  preferred, 720x1280 at the same ratio passes" is now the
  headline, not a clarification below it.
- **Segment assembly bridged** (`yt-production`): single-skill
  = Block B as written; multi-skill = segment list per
  `yt-qa`, assembled to the same 8–12s budget with parasocial
  + loop preserved in the final segment. The `C_slow_detail`
  variant is slow, controlled movement at normal speed, not
  a slow-motion effect (FINAL bans slow motion).
- **Publish gate + burst accounting shared** (`yt-publish`,
  `yt-production`, `yt-qa`): the publish checklist requires
  naming the QA report and states it is not a substitute for
  `yt-qa`; hook-frame fails, segment regens, and face-gate
  regens all count toward the same 2-fail glitch burst.
- **Generic timing default removed** (`yt-post`,
  `package_builder.py`): no generic best-time default; without
  an Audience heatmap, publish on the series' usual day and
  record the heatmap as the first post-publish task.
- **Scorecard hard gates** (`scorecard.py`, `yt-qa`):
  `--width/--height` (9:16 ratio, 720x1280 minimum),
  `--nose` (frontal-right only), `--slot` (rotation
  palette), `--lufs/--peak/--beat` (audio gate, −16 to −12
  LUFS tool tolerance, peak ≤ −1). Every run prints the
  gates the tool cannot verify (face gate, text-end rule,
  parasocial tail cap, slot vs previous video), so a PASS is
  never mistaken for a full QA pass.
- **Publish checks completed** (`publish_check.py`,
  `yt-publish`): thumbnail-vs-title repeat, format, and
  clean/watermark checks added (missing format or clean is
  FAIL, not a guess); branded-content disclosure check
  (disclose yourself, never rely on auto-detection).
- **Package builder kept to its promises**
  (`package_builder.py`): thumbnail text derived from the
  hook minus title variant 1's words, never hardcoded
  "LAND IT?"; text layers carry `end_s`/`beat_end_s` and
  flag `ends_past_beat`.
- **Prompt builder kept to its promises**
  (`prompt_builder.py`, `yt-ai-prompt`): text mode prints
  all three variants in full; the [REALISM] paragraph
  (pores, flyaway hairs, chalk dust, blink, micro-tremor,
  sweat progression) is injected into every full prompt;
  the nose_ring field is canonicalised to the full v3.3.5
  sentence whatever a stale brief said.
- **Honest scoring** (`shorts_score.py`, `title.py`):
  HOOK no longer falls back to the title (empty hook = 0);
  LOOP scores full marks only when `--loop-text` shares a
  word with the hook/title (bare `--loop yes` = half marks,
  claimed not verified); CLOSE counts imperative verbs
  (exactly one scores); `title.py` thumbnail ceiling fixed
  to 3 words (was `> 4` against its own message).
- **New loudness tool** (`loudness.py`, `yt-sound`, `yt-qa`):
  ffmpeg ebur128 true-peak measurement against the audio
  gate; fixture `tests/fixtures/tone-14lufs.wav` measures
  −14.0 LUFS / −10.3 dBFS. Beat-track presence still needs
  a human ear.
- **Smaller tool fixes** (`analytics.py`: outliers at 3x the
  median + upload gaps over 7 days; `trend_pack.py`:
  `--evidence-date` + 30-day stale flag; `retention_plan.py`:
  parasocial + CTA over 2s flagged as long-tail;
  `retention.py`: hook leak is the value AT the 30s mark,
  not the minimum before it, plus a BIGGEST LEAK verdict;
  `deadair.py`: docstring corrected to time order + 0.45s
  default documented; `hookscore.py`: exit 2 on a missing
  file instead of 0; `chapters.py`: sibling-import
  requirement documented).
- **Landscape updates** (`yt-originality`, `yt-sound`,
  `yt-algorithm`, `yt-bridge`, `yt-publish`, `yt-community`,
  `yt-analytics`): AI-generated music labels (YouTube Music
  rollout from 14 October 2026, main YouTube later, no date;
  label = transparency marker, no claimed recommendation or
  royalty effect; partner-declaration tiers flagged as trade
  coverage); likeness detection corrected to face-only with
  voice announced 23 September 2026 for later in 2026;
  1 October originality nuances (recommendation change, not
  a Guideline/YPP rule; channel-level and reversible;
  Posts-tab alternative flagged second-hand); Shorts Series
  members-only mobile update and unconfirmed discovery
  surfaces (check Studio first); branded-content
  auto-labelling (policy rewritten 3 September 2026);
  GIF comments (mobile October 2026, all-user November
  2026 planned, no desktop workaround); Studio Content tab
  redesign (Notices column, Estimated revenue ~2-day lag);
  Views (Co-Viewed) metric (modelled TV estimate, up to 48h
  delay, never compared to public views or earnings).
- **Tests:** 33 to 58 checks, ALL PASS. The four previously
  untested tools (chapters, deadair, retention, swipe) are
  now exercised; new fixtures cover the new gates; the
  structure check no longer claims "every tool runs" — the
  checks above are what run them. `check()` still accepts
  exit 0/1 because several tools legitimately exit 1 on a
  FAIL verdict; a new `check_exit()` covers tools that must
  reject input with exit 2.
- **Not fixed, and why:** manual-argv parsing in 11 tools
  (unknown flags silently ignored, numeric-looking tokens
  stripped) was left as a documented limitation — migrating
  all 11 to argparse in one version risks breaking the
  tools' tested behaviour for little user gain; the one
  user-facing case (hookscore exit 0 on a missing file) is
  fixed. Consecutive-colour and slot-logging checks stay the
  planner's job: one tool run cannot see the previous video.
  The YouTube Music blog URL could not be verified in full
  and is not cited; the announcement is cited via Variety /
  ANI reporting instead.

## v3.3.5, nose ring clarification, 26 October 2026

Fixes the nose ring drift found in the October 2026
arabesque video (teal leotard, Part 5): on frontal frames
at 300% zoom, a centre/septum-like ring appeared alongside
the nostril ring, even though the lock said "RIGHT nostril
only". The cause was ambiguity, not a missing ban: "RIGHT"
alone does not say character's right or image's right, and
a small ring drifts to the centre as the head turns and
the face smiles. Skill count unchanged at 33, tool count
unchanged at 17, file count unchanged at 124, original
author credit and MIT licence unchanged. Local only at
build time; GitHub push is a separate decision.

- **Full wording, everywhere** (`yt-ai-prompt`,
  `prompt_builder.py`, examples): "SMALL gold nose ring
  on the character's RIGHT nostril wing only (in a
  frontal view, on the image's LEFT side), never septum,
  never centre, never nose tip, never two rings."
- **Negative prompt expanded** (`prompt_builder.py`):
  now bans centre nose ring, nose ring on nose tip, and
  two nose rings, as well as septum ring and changing side.
  Continuity and checklist lines carry the same wording.
- **QA frontal-frame rule** (`yt-qa`): the nose ring side
  must be verified on a FRONTAL frame, not a side-profile
  frame, where side and centre cannot be told apart. A
  centre, septum, or nose-tip ring FAILS, even if the
  other accessories pass, and a second centre ring
  alongside a correct wing ring also FAILS.
- **Hook-frame gate** (`yt-production`): a centre,
  septum, or nose-tip ring in the hook frame fails the gate.
- **Test:** new `prompt_builder_nose` test checks that
  the prompt output bans centre nose ring.

## v3.3.4, format clarification, 26 October 2026

Fixes a contradiction found while rating the October 2026
middle-split video (720x1280, 9:16): the scorecard's
phone-look criterion scores look, not pixels, but the
format gate's "1080x1920" wording read as a pixel-perfect
hard fail, so a good 720p video would score 10/10 and still
fail the gate. Skill count unchanged at 33, tool count
unchanged at 17, file count unchanged at 124, original
author credit and MIT licence unchanged. Local only at
build time; GitHub push is a separate decision.

- **Format gate clarified** (`yt-qa`): the hard part is
  ratio and look — vertical 9:16, full frame, looks shot
  on iPhone. Horizontal, letterboxed, pillarboxed, or
  cropped-from-horizontal footage still FAILS.
- **Resolution rule** (`yt-qa`, `yt-ai-prompt`,
  `yt-production`, `yt-shorts-first`, `yt-publish`,
  `templates/ai-video-prompt.md`, `prompt_builder.py`):
  1080x1920 is the preferred target. 720x1280 at the same
  9:16 ratio is the minimum acceptable and PASSES the gate.
  Do not fail a video only for being 720p, and do not
  upscale 720p to fake 1080p.
- **Phone-look clarified** (`yt-qa`): the scorecard's
  phone-look (single handheld phone shot, ambient light,
  no cinema bokeh) scores the look, not the pixel count.

## v3.3.3, leotard colour rotation, 26 October 2026

The user noticed every video was coming out in the purple
leotard. The cause was in the pack itself: the Aria example
and `prompt_builder.py` defaulted to "purple leotard", and
the character lock said the outfit never changes between
videos — even though the user's own template already had a
variety rotation matrix. This version fixes the pack side.
Skill count unchanged at 33, tool count unchanged at 17,
file count unchanged at 124, original author credit and MIT
licence unchanged. Local only at build time; GitHub push is
a separate decision.

- **Fixed 5-colour cycle** (`yt-ai-prompt`): purple (anchor,
  Slot 1), teal, black, royal blue, burgundy, then back to
  purple. No other leotard colours unless a dated revision
  adds one. Purple stays the anchor and the colour to return
  to whenever a slot is in doubt.
- **One planned slot per video** (`yt-ai-prompt`,
  `yt-production`, `yt-series`): the package names the slot
  before the hook frame is made, the hook frame and the video
  use the same slot, and the series log records the slot per
  episode so no colour repeats twice in a row.
- **Tool flag** (`prompt_builder.py`): new `--outfit` flag
  overrides the brief's outfit for one planned slot, for
  example `--outfit "teal leotard"`. The default stays purple
  for backward compatibility; rotation is chosen in the plan,
  not by the tool.
- **What never rotates** (`yt-ai-prompt`, `yt-qa`): hair,
  messy bun, gold wire-frame glasses, nose ring side, silver
  hoop earrings, freckles, face, and body proportions. A change
  there is identity drift, not rotation, and QA fails it.
  QA also fails a video in the wrong slot colour
  (FAIL-FIXABLE: re-generate in the planned slot). Rotation
  happens across videos, never mid-shot — the negative
  prompt's ban on outfit changing colour mid-shot stands.
- **Test:** new `prompt_builder_outfit` test checks that
  `--outfit "teal leotard"` puts teal in the prompt.

## v3.3.2, production gates, 26 October 2026

Fixes for the five shortcomings found in the October 2026
front-split video review (10-second Short, middle split then
front split, measured about −29 LUFS with gym noise only).
Skill count unchanged at 33, tool count unchanged at 17,
file count unchanged at 124, original author credit and MIT
licence unchanged. Local only at build time; GitHub push is
a separate decision. No tool code changed, so no test count
change — the existing suite still covers the tools.

- **Suspense hook frame** (`yt-production`, `yt-shorts-first`):
  the old rule always wanted a 0.0s peak-action frame. That
  rule itself answered a suspense question ("how low can she
  go?") in frame one. Now, for a title that is a question
  whose answer IS the skill, the 0.0s frame must show the
  struggle or starting position, and the peak is the payoff
  later. Showcase titles with no question to answer keep
  the peak-action frame.
- **Text-end rule** (`yt-post`, `yt-qa`): every text layer
  ends when its beat ends. A layer lingering into the next
  beat, the exit, or a standing pose fails the package and
  fails QA — re-time it.
- **Audio loudness and beat gate** (`yt-sound`, `yt-qa`):
  native room noise alone fails. A beat/music track from a
  licence-safe source must start in the first 2 seconds,
  and finished audio must be normalised to a −14 LUFS
  target with true peak no higher than −1 dBTP. −14 LUFS
  is used as the publishing target (YouTube's normalisation
  level), not as a ranking claim.
- **Parasocial beat cap** (`yt-story`, `yt-qa`): the beat
  stays mandatory, but it is 1–2 seconds. After the skill
  ends, beat plus CTA together fit in 2 seconds, then cut
  or loop. A longer smile tail is a retention tail — trim it.
- **Vote pinned comment** (`yt-post`): for a challenge or
  comparison Short with two skills, sides, or attempts, the
  pinned comment must be a vote naming both sides as they
  appear in the video, in the order they appear.

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
