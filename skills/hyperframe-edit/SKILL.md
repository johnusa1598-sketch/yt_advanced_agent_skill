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

Requirements: Node.js 20+ (24 verified working), FFmpeg 6+
on PATH (8 verified working), a Chromium/Puppeteer browser
(the CLI manages it — it downloads its own browser on
first use; no system Chromium binary is required).

Setup:
1. `git clone https://github.com/heygen-com/hyperframes`
2. Create a project folder per video; inside it:
   `npm init -y`, then pin the CLI:
   `npm i -D hyperframes@0.8.201`
3. Author the composition as `index.html` in the project
   root; put fonts in `assets/fonts/`, media in `assets/`.
4. Workflow: `check` (must reach 0 errors) → snapshot
   review → `render`.

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
- The installed checker (0.8.201) additionally requires:
  root `#stage` carries `data-composition-id` +
  `data-width` + `data-height`; the timeline is registered
  on `window.__timelines[compositionId]` (register on
  `window.timelines["main"]` too, for the reference
  system); the `<video>` element is itself a clip with its
  own `class="clip"` + `data-start` + `data-duration`.
  Lint warnings about `.clip` elements containing a nested
  `.inner` div are expected and acceptable — GSAP must
  animate the inner child, never the clip itself.

### 1.2 FFmpeg (joining, sound, mastering)

Any recent FFmpeg (6/7/8) works. Used for: cutting/trimming
clips, concatenating, cross-dissolve joins, SFX mixing,
music ducking, loudness normalisation, final encode.

### 1.3 Transcription (QC + timing)

Faster-Whisper (Python, CPU is fine; model `small` or
better) with `word_timestamps=True`. Install once with
`pip install faster-whisper` (not preinstalled — first
setup downloads the model). You need it twice:
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
  the total `data-duration`.
- Exactly ONE paused GSAP timeline, registered as
  `window.timelines["main"]`. All animation lives in it.
- NEVER tween `display`/`visibility` on a `.clip` element
  (animate its children instead), and don't put CSS
  transforms on elements GSAP also transforms. Either rule
  broken = treatments that vanish or jump in the render.
- A `<video>` clip MUST have an `id` attribute or the
  renderer silently freezes it (check error:
  `media_missing_id`). No error is raised — the frame
  just stops moving. Always check for this first when a
  clip looks frozen.
- Load GSAP from the jsdelivr CDN script tag (or a local
  vendored copy, see 1.1).
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
  clean sans, subtle border, small "prompt" label) showing
  the EXACT instruction text the script mentions.
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

- Grades are CSS filters/overlays animated in the edit
  layer, applied to the whole frame or a masked region:
  - **Warm-up grade:** warm overlay (amber tint, lifted
    shadows, slight saturation up) — the "the picture
    visibly obeys" moment.
  - **Moody grade:** desaturated, darker, cool tint,
    vignette — the "one word changes the whole grade"
    moment.
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
- Keep it subtle (small, low opacity). If it distracts
  from a caption, move it — captions always win.

### 3.7 Sound design (every graphic gets sound)

- Every graphic entrance gets an SFX: pop/tick for words,
  blip for cards, swish for covers, whoosh for grade
  changes. No silent graphics.
- Music: one licence-safe track, ducked under speech
  (music never louder than the voice), lifted slightly
  under montages and the CTA.
- All SFX and music are placed from the timing JSON, on
  the treatment's start time — never placed by eye.

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

1. **Check:** `hyperframes check` — must reach 0 errors.
   Fix every error; never render over a failing check.
   First suspect on a frozen clip: missing video `id`.
2. **Snapshot review:** render stills at each beat
   boundary and look at them: treatment placement, font
   rendering, face visibility, caption collisions. Fix
   before rendering video.
3. **Sample (new work only):** render one beat (~10s),
   show it, get the verdict. Only then render full.
4. **Render:** full composition at 1080x1920. Expect
   about 6-7 minutes per 30 seconds of output — a 60s
   short takes roughly 12-15 minutes of render time, plus
   setup and QC. Say this upfront so nobody waits
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
- [ ] Every script line verified by transcription.
- [ ] Blinking, eye movement, micro-expressions present
      in every clip (no frozen stare).
- [ ] Captions synced to word timestamps; no caption
      bleeding across beat boundaries.
- [ ] Every graphic has its SFX; music ducked under
      speech; voice never buried.
- [ ] Grades change on their spoken words, ~0.3-0.5s.
- [ ] No watermark, logo, stray text, or font fallback.
- [ ] Audio: -14 LUFS target, true peak ≤ -1 dBTP,
      measured on the finished file.
- [ ] Sample verdict obtained on new work before the
      full render shipped.
- [ ] QC report delivered with the video, gaps stated
      honestly.

## Part 7 — Failure modes and fixes (quick reference)

- Render hangs silently → run the CLI directly, not via
  npx; check TMPDIR/cache space.
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
   libx264 CRF 16). `--denoise` adds hqdn3d;
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
2. **HyperFrames** — `check` must pass with 0 errors
   (the script stops otherwise); `--snapshot "t1,t2"`
   renders stills for beat-boundary review; then
   `render` at the stage fps to
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
