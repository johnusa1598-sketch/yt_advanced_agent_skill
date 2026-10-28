---
name: hyperframe-edit
description: >-
  Edit supplied video clips into a polished 9:16 vertical short
  with HyperFrames (HTML + GSAP timeline rendered to MP4):
  kinetic typography, live colour-grade transformations,
  magazine-cover graphics, chat-prompt cards, word-synced
  captions, sound design and mastering. Use for "edit this
  video like the reference", "hyperframes edit", "kinetic
  captions edit", or any 9:16 short whose spectacle is the
  editing itself. Input is supplied clips — this skill does
  not generate video clips.
---

# hyperframe-edit

The hero of this format is the editing, not the presenter.
The presenter's face, voice and words stay natural and human.
The EDIT is the spectacle: kinetic typography, colour-grade
transformations that happen live on screen, magazine-cover
graphics, chat-prompt cards, word-synced captions, and sound
design on every graphic. A viewer should stop scrolling and
think "what an edit!".

## Scope — what this skill is and is not

**It IS:** the edit layer. You give me clips (talking-head or
otherwise), a script, and the treatments you want. I build the
HyperFrames composition, render it, finish the audio with
FFmpeg, QC it, and hand back a polished 9:16 MP4.

**It is NOT:** video generation. This skill never generates
clips. On this account video generation is blocked (region
restriction, error `video_not_available`, non-retryable), so
any step that says "generate a clip" is out of scope here.
Clips must be supplied by the user, or generated on another
agent/tool whose video generation works, and then handed to
this skill for editing. If someone hands you this skill
expecting it to also generate the clips, say so plainly
before starting — do not silently substitute a still image,
a slideshow, or a text-only video for real clips.

**Inputs I need before I start:**
1. The clips (one file per script line is ideal, but any set
   of clips works), in order, with the script line each clip
   is supposed to say.
2. The script text, line by line.
3. The treatments wanted (which of the edit-layer treatments
   below, and any exact on-screen words).
4. The target duration and aspect (default: 9:16 vertical,
   1080x1920; 45-75 seconds for the talking-head format).

**What you get back:**
- The rendered MP4 (1080x1920, h264 + AAC).
- The composition (`index.html`) and project folder, so the
  edit is re-runnable and adjustable.
- Word timings JSON (from transcription, see below).
- A QC report: every line verified or flagged, every gate
  passed or failed, and anything below the reference bar
  stated honestly with its fix.

**Sample first (non-negotiable on new work):** on a new
project, render a short sample (one beat, ~10 seconds) and
get the user's verdict before rendering the full video.
Never render a full video on a first attempt and hope.

**Voice rule:** never use a cloned voice for this format
unless explicitly ordered. Use the audio that came with the
supplied clips. If a clip's audio is unusable, say so and
ask — do not clone, do not synthesise a replacement voice
on your own.

## Part 1 — Software setup (do once)

### 1.1 HyperFrames (the editing engine — HTML > video)

Repo: https://github.com/heygen-com/hyperframes (open
source, Apache-2.0). Concept: "Write HTML. Render video."
You author one `index.html` composition with timed clips
and a GSAP timeline; the CLI renders it to MP4.

Requirements: Node.js 22+ (24 verified working), FFmpeg 6+
on PATH (8 verified working), a Chromium/Puppeteer browser
(the CLI manages it — it downloads its own browser on
first use; no system Chromium binary is required).

Setup:
1. `git clone https://github.com/heygen-com/hyperframes`
2. Create a project folder per video; inside it:
   `npm init -y`, then pin the CLI:
   `npm i -D hyperframes@0.8.207`
3. Author the composition as `index.html` in the project
   root; put fonts in `assets/fonts/`, media in `assets/`,
   GSAP in `assets/js/gsap.min.js` (local, never CDN —
   a render must not depend on a network fetch).
4. Workflow: `lint` (0 errors, blocking) → `check`
   (0 errors) → snapshot review → `render`.

Upgrades (do this, never pin to unreleased main):
`npx hyperframes@latest upgrade --project . --check`
(probe, read-only), apply, re-run `check`, and name the
old → new versions in the run summary. If `check` fails
after the upgrade, revert the `package.json` pin.

VM gotchas (learned the hard way):
- If `npx hyperframes check | render` hangs silently, run
  the CLI directly, e.g.
  `node <npm-cache>/_npx/<hash>/node_modules/hyperframes/dist/cli.js check`
  — it starts in seconds.
- Give npm a big TMPDIR and cache dir on slow/small disks.
- If the GSAP CDN script tag cannot load (offline or
  blocked network), vendor GSAP locally into `assets/` and
  point the script tag at it instead — a composition that
  cannot load GSAP cannot animate, and the render will
  silently lose every treatment.
- Proven on this VM (27 Oct 2026, needle-hold edit): the
  browser sandbox could NOT reach the jsdelivr CDN
  (net::ERR_TUNNEL_CONNECTION_FAILED), so `check` failed
  with 2 runtime errors and the timeline never ran — fix
  was GSAP 3.12.5 vendored to `assets/js/gsap.min.js` and
  the script tag pointed at it; after that `check` passed
  with 0 errors. Same run: this VM's `/tmp` is a 512 MB
  tmpfs, and `render` refuses with "Low disk space" —
  fix is `TMPDIR=$PWD/tmp` (a workspace dir, 98 GB free
  here) on the render command.
- The checker (0.8.207) additionally requires:
  root `#stage` carries `data-composition-id` +
  `data-width` + `data-height`; the timeline is registered
  on `window.__timelines[compositionId]` (register on
  `window.timelines["main"]` too, for the reference
  system) AFTER the tweens are built — registering an
  async-built timeline early trips the checker; the
  `<video>` element is itself a clip with its own
  `class="clip"` + `data-start` + `data-duration`.
  Lint warnings about `.clip` elements containing a nested
  `.inner` div are expected and acceptable — GSAP must
  animate the inner child, never the clip itself.
- Newer CLI diagnostics (0.8.204+): a render whose capture
  stops advancing now fails within minutes instead of
  hanging; a command silent for 60 s writes a diagnostic
  report; `check`/`snapshot` timeouts name the step they
  were on; `--timeout` accepts units like `45s`. Check
  these first on a stall — the direct-CLI and TMPDIR
  notes above stay as VM-specific fallbacks. If Chrome
  is missing or will not start: `hyperframes doctor
  --json` (gate on `.ok`) then `hyperframes browser
  ensure`.

### 1.2 FFmpeg (joining, sound, mastering)

Any recent FFmpeg (6/7/8) works. Used for: cutting/trimming
clips, concatenating, cross-dissolve joins, SFX mixing,
music ducking, loudness normalisation, final encode.

### 1.3 Transcription (QC + timing)

Default: `hyperframes transcribe` (word-level timestamps;
engines `auto` — Parakeet if installed, else Whisper —
default model `small.en`; `--language`, `--json`, `--dir`;
it also imports `.json`/`.srt`/`.vtt` transcripts, and
`transcribe transcript.json --dir <project>` replaces the
transcript inside existing captions). Fallback, if the
CLI transcribe path is unavailable: Faster-Whisper
(Python, CPU is fine; model `small` or better) with
`word_timestamps=True`, installed once with
`pip install faster-whisper` (not preinstalled — first
setup downloads the model). Map the transcribe output
onto the timings shape below, and verify that mapping
on first use — the command and flags are verified, the
output schema is not yet. You need timings twice:
1. **QC** — prove every supplied clip says exactly its
   script line.
2. **TIMING** — word start/end times drive caption
   emphasis, treatment triggers and SFX placement.

Save timings as JSON in exactly this shape:
`{clip: [[start, end, "word"], ...]}` — one entry per clip,
one triple per word, times in seconds.

### 1.4 Fonts (the reference look)

- **Anton** (heavy condensed sans) — kinetic words, tags,
  pills, giant captions.
- **Georgia / Playfair-style serif** — word-emphasis
  caption plates and the magazine masthead.
- **Monospace** (e.g. DejaVu Sans Mono) — the ticking
  timecode.

Load fonts with `@font-face` from `assets/fonts/`. Never
rely on a system font or a webfont that the render
browser may not fetch — a missing font silently changes
every treatment's look.

## Part 2 — Composition rules (follow exactly)

These rules are the difference between a composition that
renders and one that silently breaks. They come from the
reference system's hard-won experience:

- Every timed element: `class="clip"` plus `data-start`
  and `data-duration` attributes. The root element carries
  the total `data-duration`, plus `data-composition-id`,
  `data-width` and `data-height`.
- Exactly ONE paused GSAP timeline, registered on
  `window.__timelines[compositionId]` AND
  `window.timelines["main"]`, AFTER the tweens are built.
  All animation lives in it. Prefer `fromTo()` for seek
  reliability.
- Video-as-clip is the only clean shape: a `<video>`
  carries its own `class` + `data-start` + `data-duration`
  + `id` and sits as a direct child of the root. Never
  time both a video and its wrapper — if a video must
  move or resize, animate an UNTIMED wrapper around it.
  A `<video>` without an `id` silently freezes (check
  error: `media_missing_id`). Always check for this
  first when a clip looks frozen.
- NEVER tween `display`/`visibility`/`autoAlpha` on a
  `.clip` element (animate its children instead), never
  tween `left`/`top`/`width`/`height` (animate transforms
  and opacity only), and don't put CSS transforms on
  elements GSAP also transforms. Any rule broken =
  treatments that vanish or jump in the render.
- Every timeline-visible element gets a stable `id`
  (otherwise the linter warns `studio_missing_editable_id`
  and Studio has no edit target for it).
- Media `src` filenames containing `#` or `?` must be
  percent-encoded.
- GSAP is LOCAL (`assets/js/gsap.min.js`) — never a CDN
  src. A render must not depend on a network fetch.
- Audio elements need an `id` or they are left out of
  the mix; a video keeps its sound only with
  `data-has-audio="true"`, otherwise it is muted (see
  3.7 for the native mix).
- If the base `<video>` is muted in the composition, the
  render is VIDEO-ONLY — mux the real audio afterwards
  with FFmpeg. This is normal, plan for it: render video,
  then mux, never assume the render has sound.

A starter composition that follows every rule above is in
`templates/hyperframes-composition.html` next to this skill.
Start from it; do not start from a blank file.

## Part 3 — The edit layer (treatments)

All drama lives here, never baked into the clips. If a
supplied clip already has a dramatic grade baked in, it
fights the edit layer — prefer clean, consistent clips and
say so if the supplied clips are not clean. Every treatment
is timed from the transcription JSON, not guessed.

### 3.1 Kinetic typography (Anton)

- One word at a time, or one short phrase at a time, never
  a wall of text. Words pop in on their spoken timestamp
  (scale from ~0.8 + opacity 0 → 1, ~0.15s ease-out).
- Emphasis words go bigger and/or in an accent colour;
  ordinary words stay smaller and neutral. The emphasis
  list comes from the script's intent, not from volume.
- Words leave before the next beat starts — no treatment
  may bleed across a beat boundary unless the script
  explicitly asks for it.
- Sound: a soft pop or tick on every word pop, mixed low
  under speech (see 3.7).

### 3.2 Word-synced captions (serif plates)

- Caption plates in serif, one clause per plate, timed to
  the spoken words. The currently spoken word is
  highlighted (colour or underline); spoken words stay
  highlighted, unspoken words stay dim.
- Caption timing comes from word timestamps. If a word's
  timestamp is missing or wrong, the caption is wrong —
  fix the timing, never nudge captions by eye.
- No burned-in text other than the treatments in this
  section. Clean output otherwise: no watermark, no logo,
  no stray text.

### 3.3 Chat-prompt card

- A card styled like a chat message (rounded, mono or
  clean sans, subtle border) showing the EXACT
  instruction text the script mentions — and NOTHING
  else. The word "prompt" (or any component/builder
  label) must NEVER appear in the delivered video:
  Part 10 shipped a visible "prompt" label above the
  rewatch pill line, and it reads as a stray text,
  not a design element. A label in the finished video
  is a defect: remove it before render.
- The card appears on the line that mentions it, and the
  picture visibly obeys it in the same beat (e.g. a grade
  change right after the card). A card with no visible
  consequence is decoration — cut it or add the
  consequence.
- Sound: a soft message-arrival blip on appearance.

### 3.4 Magazine-cover treatment

- Serif masthead (channel or series name), cover lines
  around the presenter, and a cover-style frame or border.
- Used for the social-proof beat ("and I know nothing
  about editing" shape): floating clips + magazine cover.
  The cover must not cover the presenter's face or the
  active caption.
- Sound: a paper/swish on the cover's entrance.

### 3.5 Live colour-grade transformations

- Grades go through the NATIVE path first, never CSS
  filters on footage: `data-color-grading` JSON on the
  media (`preset` / `intensity` / `adjust` / `details` /
  `effects`; presets include `skin-soft` and
  `two-ink-print`; `.cube` LUTs up to 64 points/side).
  Apply and preview with the CLI: `media-treatment
  --selector … --grading … --apply` (`--dry-run` first,
  `--clear` to remove), and `grade-compare` for a
  labeled side-by-side PNG of candidate looks on the
  user's own frame before committing a warm/moody beat.
  - **Warm-up grade:** warm preset/adjust (amber tint,
    lifted shadows, slight saturation up) — the "the
    picture visibly obeys" moment.
  - **Moody grade:** desaturated, darker, cool tint,
    vignette — the "one word changes the whole grade"
    moment.
- The live-change beat survives natively: 9 grading
  properties tween on the paused timeline
  (`--hf-color-grading-intensity`, `-exposure`, `-bloom`,
  `-blur`, `-pixelate`, `-kuwahara`, `-ascii`, `-dither`,
  `-lut-intensity`). Caveats: intensity does NOT scale
  the detail/effect families (grain, halftone, bloom,
  tape, CRT) — animate the specific property instead;
  grades select pixels by value, not position, so a
  REGION grade needs a cutout layer (fixed `clip-path`
  only for near-static subjects; tracked mattes come
  from outside HyperFrames).
- CSS-filter/overlay grades are the FALLBACK, for
  non-media layers only — never on footage when the
  native path is available.
- A grade change is a BEAT: it happens on a spoken word
  or a card, over ~0.3-0.5s, never as a slow drift. The
  viewer must feel the moment it changes.
- Never bake grades into clips. If a clip arrives
  pre-graded, either re-grade it to neutral first (FFmpeg)
  or flag it — a baked grade plus an edit grade looks
  muddy, not dramatic.

### 3.6 Timecode (monospace)

- A small monospace timecode, ticking in real time, in a
  corner that never collides with captions. It sells the
  "edit" feeling and gives the viewer a sense of craft.
- TICKING IS MANDATORY, not decorative: the timecode
  text MUST be driven by the timeline's own time
  (onUpdate / ticker), so it advances every frame. A
  static "00:00:00:00" for the whole render is a
  delivery defect — Part 10 shipped a frozen timecode
  for all 10 seconds because the starter template
  printed a static string and no tween ever updated
  it. The template now drives it from `tl.time()`.
- Pre-render check: sample two frames (e.g. 1s and 5s)
  and confirm the timecode value differs. Same value
  = FAIL, do not render.
- Keep it subtle (small, low opacity). If it distracts
  from a caption, move it — captions always win.

### 3.7 Sound design (every graphic gets sound)

- Every graphic entrance gets an SFX: pop/tick for words,
  blip for cards, swish for covers, whoosh for grade
  changes. No silent graphics.
- Compose the mix NATIVELY where possible: every
  `<audio>` element needs an `id`; volume lanes via
  `data-automation`; voiceover carve via
  `data-fx-carve` (music dips only where voice sits);
  buses via `data-audio-group`; a master chain via
  `data-fx-chain` on the root. Stage per-element
  loudness in the composition with `normalize-audio
  --target <element-id> --lufs -14 --write` — note its
  default is -16, so -14 must be explicit. FFmpeg keeps
  only the final loudness finish + mux (the -14 LUFS /
  TP ≤ -1 gate is still measured on the finished file).
- Beat grid, not guessed times: `hyperframes beats`
  writes `beats/<audio>.json` for a music `<audio>`
  marked `data-timeline-role="music"` (or an id
  containing music/bgm/soundtrack); it fails on
  beatless tracks. Montage cuts and SFX ticks land on
  the real beat grid. `hyperframes audio --read` /
  `--at` / `--range` measures onsets, hits, loudness,
  silence and envelope in film time — use it for SFX
  placement and silence trimming.
- Music: one licence-safe track, ducked under speech
  (music never louder than the voice), lifted slightly
  under montages and the CTA.
- All SFX and music are placed from the timing JSON, on
  the treatment's start time — never placed by eye.

### 3.8 Vertical safe areas (9:16)

Upstream's vertical rules, for 1080x1920 (scale for
720x1280: top 112 px, band to 887 px):
- Nothing readable in the top 168 px.
- Content band 168–1330 px; below 1330 px only
  texture/decoration; no text under the right action
  rail; burned-in captions at the bottom of the band.
- Titles ×1.35 vs landscape; nothing meant to be read
  under 28 px; ~5 English words per line max (cut
  words, never shrink).
- Every text element sits FULLY inside the band at
  every visible moment: a kinetic word clipped at the
  frame edge (Part 10: "UP, SLOWLY" cut at the left
  edge) is a defect — resize or reposition, never
  ship a half-word.
- Frame 0 is the thumbnail/hook — face, result, or one
  bold line, never black, never a logo.
- The video must work muted.
Caveat: check the platform the clip is for (a Shorts
right rail is not a TikTok bottom bar). A delivered
project that deliberately breaks the band (e.g. a low
CTA that tested well) stays as-is; new work follows
the band.

### 3.9 Upstream pieces that plug into this workflow

- Registry first: `hyperframes add` / catalog. Caption
  components matching this skill's treatments:
  `caption-kinetic-slam` (one full-screen word per
  beat), `caption-highlight` (one word highlighted at
  a time), `caption-blend-difference` (auto-inverts per
  pixel — legibility over busy gym footage),
  `caption-pill-karaoke`; blocks `yt-lower-third`,
  `yt-vertical-fill`, `yt-prism-title`,
  `grade-split-reveal`. Start from the named component,
  re-time to the transcription, re-size for 9:16
  (components ship as landscape demos — re-authoring
  is expected, not a workaround). One caption identity
  per section; emphasize keywords only, never every
  word.
- Text-behind-subject via the `remove-background`
  cutout layer — the advanced kinetic treatment (type
  passing under the subject's silhouette);
  single-subject only, needs the cutout as a separate
  layer.
- Speed ramps via a `data-automation` rate lane
  (0.1–10 clamp, log interpolation, pitch kept;
  presets Montage/Hero/Bullet/Jump cut/Flash in/Flash
  out) — opt-in beat emphasis only, never a default.
  Note: this is edit-layer work on supplied clips and
  does not touch the yt pack's separate slow-motion
  question.
- Sub-composition shape (the direction lint is
  pushing): one scene per file in `<template>`, the
  root holds hosts. For multi-beat Shorts, one
  sub-composition per beat keeps the timeline
  readable. Mind the linked-stylesheet warning: a
  sub-composition's linked stylesheet must not select
  its root id — use an inline `<style>` inside the
  `<template>` instead.
- Themes (`themes/bold.css`, `editorial.css`,
  `neutral.css` — CSS variable sets) as optional look
  presets; bold fits hype Shorts, editorial fits the
  magazine treatment.
- Timeline CLI edits for Part 4's trim/cut fixes:
  `timeline move|trim|split|set|duplicate|delete|
  apply|undo|ids` — auditable edits with `--plan`
  preview and receipt undo, instead of hand-editing
  HTML.
- `snapshot --review` (each scene start+0.3 s +
  middle, data-beats, 5-frame seam strips,
  phone-width frames) and `snapshot --against <video>`
  (render-vs-reference pair sheets) — a direct
  loop-match verification against the source clip.
  `keyframes` (onion-shot diagnostics) verifies motion
  between beats, not just stills. `compare` puts two
  grades/caption variants on one labeled sheet for
  A/B decisions.
- `render --quality draft|looks|delivery` — draft for
  the sample (fast iteration), delivery for the final
  master; `looks` (CRF 16) is the default. Optional
  delivery knobs, default off: `--keyframe-interval 2
  --max-bitrate 8M` (YouTube re-encodes anyway).

### 3.10 Re-hook overlays and held-peak overlays (v3.4.5)

The edit layer is where the hook-drop is rescued
when the supplied clips go weak mid-video or after
the peak (see `/yt-production` end-frame and
segment rules, `/yt-story` post-peak beat and
re-hooks). Two treatments, both inside the safe
band (§3.8) and both in the text inventory (Part 6)
before render:

- **Re-hook overlays at about 3.5s and about 7s.**
  A new text fact, stakes line, or angle-cut accent
  at each point — placed BEFORE the retention
  bleed, not after it. The overlay must add
  information (a progress marker, the difficulty,
  the "but…"), never repeat the hook text. The
  cadence is a rule of thumb [LORE], not a
  measured threshold: the gate is "a new visual
  fact before the bleed", not the exact second.
  Sound accent on each re-hook (§3.7: every
  graphic gets sound).
- **Editor-held peak + progress overlay for
  holds.** Do not stretch a weak hold: hold the
  BEST peak frame as a still in the edit, with a
  timer, progress bar, or slow zoom over it, so
  progression comes from the overlay, not from
  hallucinated motion — and the peak expression
  stays pixel-perfect. The overlay must never
  cover the working limbs or the face during the
  peak beat (see `/yt-story` peak rule). If the
  hold cannot support the full duration even
  held, cut the Short to 6–7 seconds rather than
  padding it with a frozen frame.

## Part 4 — Transcription QC (mandatory, before editing)

Transcribe every clip with word timestamps and compare
against the script word by word. Do not skip this: AI
speech mumbles, adds stray words, repeats lines and
stumbles, and a treatment built on a wrong line looks
broken even when the edit is perfect.

Known failure modes and their edit fixes:
- **Stray first word** (e.g. an extra "But"): trim the
  clip start at that word's end time; shift that clip's
  timings by the trimmed amount.
- **Repeated word or line:** cut the repeated region at
  its word boundaries; re-join with a short cross-dissolve
  if the cut is audible.
- **Mumbled or wrong word:** if the meaning survives,
  caption the intended word and note it in the QC report;
  if the meaning changes, the clip is unusable for that
  line — flag it and ask for a replacement clip. Never
  caption a word the viewer cannot hear as if it were said.
- **Stumble or long pause:** cut the pause at word
  boundaries if it breaks the beat; keep natural pauses
  that sound human.
- **Missing line:** the clip does not contain its script
  line at all — flag it, do not stretch another line to
  cover it.

After fixes, re-run transcription on the FIXED clip and
re-save the timings. The timings JSON used by the edit
must describe the final audio, not the original.

**Micro-detail check (every clip):** watch for blinking,
eye movement and micro-expressions. A talking head that
never blinks looks unhuman and kills the video. If a clip
has a frozen stare, flag it — no treatment fixes a dead
face. Note it in the QC report even if the clip ships.

## Part 5 — Render workflow

1. **Lint, then check:** `hyperframes lint` first
   (blocking — it catches template-class errors before
   the browser gate), then `hyperframes check --json`
   (machine-readable findings with `Fix:` lines; use
   `check --at-transitions` to sample every tween
   start/end boundary for seam issues). Both must reach
   0 errors; never render over a failing gate. First
   suspect on a frozen clip: missing video `id`. Note:
   a muted composition with no audio elements reports
   the info `audio_none` ("The film has no sound") —
   that is not a failure.
2. **Snapshot review:** render stills at each beat
   boundary and look at them: treatment placement, font
   rendering, face visibility, caption collisions. Fix
   before rendering video. `snapshot --review` gives
   the review set; `snapshot --against <video>` pairs
   render vs reference for loop-match verification.
3. **Sample (new work only):** render one beat (~10s)
   at `--quality draft`, show it, get the verdict. Only
   then render full (final at `--quality delivery`).
4. **Render:** full composition at 1080x1920. Expect
   roughly 3 minutes per 30 seconds on this VM
   (measured: 10 s in 57.1 s, screenshot capture +
   software GPU — the slow path); upstream quotes a
   30 s film in a minute or two on faster setups. Say
   the measured number upfront so nobody waits
   confused.
5. **Mux audio:** if the render is video-only, mux the
   real audio (voice + SFX + ducked music) with FFmpeg.
6. **Master:** loudness normalisation to **-14 LUFS
   target, true peak at most -1 dBTP**. Limit before
   normalising — a straight gain on audio whose peaks
   already sit near 0 will clip. Verify with a loudness
   measurement on the finished file, not on the mix.
7. **Final QC (watch the whole video once, no skipping):**
   every line says what the script says; captions sync
   to words; treatments land on their beats; grades
   change on their words; SFX on every graphic; no
   frozen stare; no watermark, logo or stray text; audio
   clean, voice always above music; 9:16 throughout.
8. **Deliver:** MP4 + composition + timings JSON + QC
   report. State honestly anything below the reference
   bar and what would fix it.

## Part 6 — Quality gates (all must pass to ship)

- [ ] 9:16 vertical, 1080x1920, single continuous edit.
- [ ] `lint` 0 errors and `check` 0 errors (the
      `audio_none` info on a muted composition is not
      a failure).
- [ ] Vertical safe areas: nothing readable in the top
      168 px, captions at the bottom of the band, no
      text under the right action rail.
- [ ] Frame 0 is the hook (face, result, or one bold
      line — never black, never a logo); the video
      works muted.
- [ ] Every script line verified by transcription.
- [ ] Blinking, eye movement, micro-expressions present
      in every clip (no frozen stare).
- [ ] Captions synced to word timestamps; no caption
      bleeding across beat boundaries.
- [ ] Every graphic has its SFX; music ducked under
      speech; voice never buried.
- [ ] Grades change on their spoken words, ~0.3-0.5s.
- [ ] No watermark, logo, stray text, or font fallback.
- [ ] Text inventory: every visible text listed before
      render; only approved texts ship (kinetic words,
      caption lines, rewatch pill line, CTA).
      Production metadata NEVER renders — rotation
      slot, beat/skill names, channel bugs, component
      labels (Part 10 shipped "TEAL SLOT 2",
      "STRONG HOLD", "ARIA FIT" and a "prompt" label
      as visible texts). A layer with metadata text
      is removed before render, not after.
- [ ] Timecode ticks: two sampled frames (e.g. 1s and
      5s) show different timecode values. A frozen
      timecode is a FAIL.
- [ ] Re-hook overlays at about 3.5s and about 7s
      (§3.10), each adding a new visual fact inside
      the safe band; held-peak overlays (timer/bar/
      zoom) on static holds instead of a stretched
      weak hold, never covering peak limbs or face.
- [ ] Audio: -14 LUFS target, true peak ≤ -1 dBTP,
      measured on the finished file.
- [ ] Sample verdict obtained on new work before the
      full render shipped.
- [ ] QC report delivered with the video, gaps stated
      honestly.

## Part 7 — Failure modes and fixes (quick reference)

- Render stalls or a command goes silent → first check
  the 0.8.204+ diagnostics (stalled capture now fails
  within minutes; 60 s of silence writes a diagnostic
  report; `--timeout 45s` sets a unit timeout); then run
  the CLI directly, not via npx; check TMPDIR/cache space.
- Chrome missing or will not start → `hyperframes
  doctor --json` (gate on `.ok`), then `hyperframes
  browser ensure`.
- Clip frozen in render → video element missing `id`
  (`media_missing_id`).
- Treatments vanish or jump → `display`/`visibility`
  tweened on a `.clip`, or CSS transform fighting a GSAP
  transform on the same element.
- Fonts look wrong → `@font-face` path wrong or font
  file missing from `assets/fonts/`; render browser fell
  back silently.
- Animations missing entirely → GSAP failed to load
  (CDN blocked) — vendor it locally.
- Audio missing from render → base video was muted;
  mux afterwards with FFmpeg (normal, planned).
- Edit looks muddy → a grade was baked into a clip and
  another grade was added on top; neutralise the clip
  first or flag it.
- Caption sync off → timings JSON is stale (describes
  the pre-fix clip); re-transcribe after every trim.

## Part 8 — Merged pipeline (FFmpeg + HyperFrames in one command)

Each tool on its strength: FFmpeg owns pixels and audio
precision (normalise, denoise, grade, loudness, mux, QC
measurement); HyperFrames owns the edit layer (motion
graphics, text, loop fixes). The wrapper script runs both
in order, so a run is reproducible instead of a series of
hand-typed commands:

`tools/merged-pipeline.sh --project DIR --input CLIP --name NAME`

Stages (the script prints every step; it stops on the
first failure instead of rendering over a broken stage):
0. **Setup** — checks ffmpeg/ffprobe/node; if /tmp has
   under 2 GB free it sets TMPDIR to the project's own
   `tmp/` (a 512 MB tmpfs /tmp breaks renders).
   Stage size comes from the composition's `data-width` /
   `data-height` (`--size WxH` overrides); fps comes from
   the source clip (`--fps N` overrides).
1. **FFmpeg pre** — the supplied clip is copied untouched
   to `assets/media/raw.mp4`, then normalised into
   `assets/media/clean.mp4`: fps + scale to the stage
   size (stream copy when already matching, otherwise
   libx264 CRF 16). Scaling keeps aspect: `scale` with
   `force_original_aspect_ratio=increase` + `crop` —
   a plain `scale=W:H` stretches a non-9:16 source into
   the stage and is a bug. `--denoise` adds hqdn3d;
   `--grade warm|moody` adds a modest eq grade (off by
   default — never grade silently). Source audio is kept
   aside as `assets/media/source_audio.m4a`.
   The composition's base video src is pointed at
   `clean.mp4` (backup `index.html.bak` on the first swap
   only — never a `*.html` name, which the checker would
   discover as a second composition); a loop still
   (`opening.png`) is regenerated
   from clean.mp4 frame 0 (backup `opening.raw.png`),
   because the still must match the clip that renders.
   A CDN GSAP src is swapped to a locally vendored copy
   (`assets/js/gsap.min.js`, downloaded if missing) —
   a browser that cannot reach the CDN loses every
   treatment, silently or as a check failure.
2. **HyperFrames** — `lint` first (0 errors, blocking),
   then `check` (0 errors; the script stops otherwise);
   `--snapshot "t1,t2"` renders stills for
   beat-boundary review; then `render` at the stage fps
   (`--quality` passthrough: draft for samples,
   delivery for finals, looks default) to
   `renders/<name>-videoonly.mp4`.
3. **FFmpeg post** — the source audio is finished, not
   the muted render's silence: loudnorm single pass
   (I=-14, TP=-1.5, LRA=11), then up to two corrective
   gain + limiter rounds (alimiter 0.79) until the
   measurement is within 0.3 LU of -14 with peaks under
   -1 dBTP; verified on the finished file. Muxed with
   `-c:v copy -c:a copy -shortest` to
   `renders/<name>.mp4`.
4. **QC** — `renders/QC_REPORT-<name>.txt` with:
   duration, resolution, final-file loudness, a
   start-vs-end frame pixel diff for the loop match
   (<15 mean abs diff on a 72x128 thumbnail = PASS
   heuristic, labelled as one), and frame stills in
   `qc-<name>/`. The report states what the script does
   NOT check: rewatch-trigger presence, caption/word
   sync, SFX placement, frozen stare, clean output —
   those need a human watch.

Conventions the pipeline relies on: the composition's
base video is `assets/media/clean.mp4` once the pipeline
has run (raw.mp4 is the untouched original); fonts live
in `assets/fonts/`; GSAP is local, never CDN-only; the
render browser's temp lives under the project when /tmp
is small. A run ends with the same question as every
other run: **ship it, or change it?**

## Out of scope (upstream features we deliberately don't use)

Upstream HyperFrames does much more than Shorts edits.
These stay out, so the skill does not drift:
- Studio/desktop-app flows (`open`, `catch-up`, Framey,
  preview loop) — needs a desktop + HeyGen account;
  this skill is CLI + files on a VM.
- Cloud / Lambda / Cloud Run rendering — local works;
  Lambda is SDR-only and bills compute; HeyGen cloud
  needs an account. Only if local becomes the
  bottleneck.
- HeyGen-gated media — avatar presenter, generated
  clips (out of scope: this skill edits supplied clips;
  generation is blocked on this account anyway), the
  10,000-track catalog (use licence-safe local tracks).
  `tts` stays out by the skill's own voice rule (no
  synthesized voice unless ordered).
- `snapshot --describe` (needs a Gemini key) and
  `audio --quality best` (uploads to HeyGen audio
  services, may bill) — external services the workflow
  does not need.
- HDR, 4K supersampling (4× slower, 3–5× larger, adds
  no detail to 1080p video, platforms transcode down),
  HLS, transparent WebM/MOV, GIF export (no audio,
  30 fps cap), PNG sequences — none serve 9:16 Shorts
  delivery.
- Slideshow/`present` decks, Figma skill,
  remotion-to-hyperframes, shader transitions,
  Lottie/Three.js adapters — different inputs or
  spectacle beyond the Shorts edit layer.
- Project history (`history begin/undo`) — trial
  feature; the skill's `.bak` backups + pipeline
  conventions already cover undo.
- `feedback --rating` telemetry, `render --docker
  --strict`, `render --batch` — telemetry is not the
  workflow; Docker is overkill while local Chrome
  works; batch only matters for variable-driven
  multi-version runs (future).
- Deprecated aliases (`validate`, `inspect`, `layout`)
  — use `lint` + `check`.

## What to hand back

- The rendered MP4, the composition and project folder,
  the timings JSON, and the QC report.
- The last line of every run is the question: **ship it,
  or change it?** On new work, that question is asked
  about the SAMPLE first, not about the finished video.

## The gate

Nothing here generates video, and nothing here publishes.
This skill edits supplied clips. Every output ends in a
file the user can open, and every gap from the reference
bar is stated in the QC report, not hidden. If the clips
are not good enough for the reference bar, say so before
rendering the full video — a polished edit cannot rescue
a dead face or a wrong line.
