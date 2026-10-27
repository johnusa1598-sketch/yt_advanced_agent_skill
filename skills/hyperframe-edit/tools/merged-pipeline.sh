#!/usr/bin/env bash
#
# merged-pipeline.sh — FFmpeg + HyperFrames, one command.
#
# Stages:
#   0. Setup      — tools, TMPDIR (workspace tmp if /tmp is small),
#                   read the composition's stage size from index.html.
#   1. FFmpeg PRE — clean the supplied clip into assets/media/clean.mp4
#                   (fps + scale normalise; --denoise / --grade opt-in).
#                   The composition's base video src is pointed at
#                   clean.mp4 (index.html is backed up to index.html.bak
#                   on the first swap only — never to a *.html name,
#                   which the checker would discover as a second
#                   composition; every swap is printed).
#                   GSAP is vendored locally the same way if the
#                   composition still points at the CDN.
#   2. HyperFrames — lint (0 errors, blocking) -> check (0 errors)
#                   -> snapshot (optional) -> render (video-only;
#                   the base video is muted).
#   3. FFmpeg POST— finish the source audio (-14 LUFS / <= -1 dBTP,
#                   limit before normalise), mux with -shortest.
#   4. QC         — probe + loudness + frames + loop-match diff,
#                   written to renders/QC_REPORT-<name>.txt.
#
# What this script does NOT do (by design):
#   - It does not author the composition. index.html must already
#     exist in the project (start from the skill's starter template).
#   - It does not invent a rewatch trigger, captions, or SFX, and it
#     does not verify transcription. Those are human edit decisions;
#     the QC report says so explicitly.
#   - It never overwrites the supplied clip. raw.mp4 stays untouched.
#
# Usage:
#   merged-pipeline.sh --project DIR --input CLIP [--name NAME]
#     [--fps N] [--size WxH] [--denoise] [--grade warm|moody]
#     [--snapshot "0.5,4.5,7.5"] [--quality draft|looks|delivery]
#
# Example (needle-hold edit shape):
#   merged-pipeline.sh --project ~/workspace/aria-pack/needle-edit \
#     --input ~/workspace/user/media_library/video/98/raw.mp4 \
#     --name needle-hold-edited --snapshot "0.5,4.5,7.5,9.8"
#
set -u

die() { echo "ERROR: $*" >&2; exit 1; }
note() { echo "  * $*"; }
step() { echo ""; echo "== $* =="; }

PROJECT=""; INPUT=""; NAME="edited"; FPS_ARG=""; SIZE_ARG=""
DENOISE=0; GRADE="none"; SNAPSHOT=""; QUALITY="looks"

while [ $# -gt 0 ]; do
  case "$1" in
    --project)  PROJECT="$2"; shift 2 ;;
    --input)    INPUT="$2"; shift 2 ;;
    --name)     NAME="$2"; shift 2 ;;
    --fps)      FPS_ARG="$2"; shift 2 ;;
    --size)     SIZE_ARG="$2"; shift 2 ;;
    --denoise)  DENOISE=1; shift ;;
    --grade)    GRADE="$2"; shift 2 ;;
    --snapshot) SNAPSHOT="$2"; shift 2 ;;
    --quality) QUALITY="$2"; shift 2 ;;
    --help|-h)  sed -n '2,40p' "$0"; exit 0 ;;
    *) die "unknown argument: $1 (see --help)" ;;
  esac
done

[ -n "$PROJECT" ] || die "--project DIR is required"
[ -n "$INPUT" ]   || die "--input CLIP is required"
[ -d "$PROJECT" ] || die "project dir not found: $PROJECT"
[ -f "$INPUT" ]   || die "input clip not found: $INPUT"
[ -f "$PROJECT/index.html" ] || die "no index.html in $PROJECT (author the composition first)"
case "$QUALITY" in
  draft|looks|delivery) : ;;
  *) die "--quality must be draft, looks, or delivery" ;;
esac
command -v ffmpeg >/dev/null || die "ffmpeg not on PATH"
command -v ffprobe >/dev/null || die "ffprobe not on PATH"
command -v node >/dev/null || die "node not on PATH"

cd "$PROJECT" || die "cannot cd to $PROJECT"
mkdir -p assets/media renders tmp

# ---------- Stage 0: setup ----------
step "Stage 0 — setup"

# Small /tmp (e.g. a 512 MB tmpfs) breaks renders: use project tmp.
TMP_AVAIL_KB=$(df -k /tmp 2>/dev/null | awk 'NR==2 {print $4}')
if [ -n "${TMP_AVAIL_KB:-}" ] && [ "$TMP_AVAIL_KB" -lt 2000000 ]; then
  export TMPDIR="$PWD/tmp"
  note "/tmp has only ${TMP_AVAIL_KB} KB free — TMPDIR set to $TMPDIR"
fi

# Stage size: composition's data-width/data-height win; --size overrides.
STAGE_W=$(grep -o 'data-width="[0-9]*"' index.html | head -1 | grep -o '[0-9]*')
STAGE_H=$(grep -o 'data-height="[0-9]*"' index.html | head -1 | grep -o '[0-9]*')
if [ -n "$SIZE_ARG" ]; then
  STAGE_W="${SIZE_ARG%x*}"; STAGE_H="${SIZE_ARG#*x}"
fi

SRC_W=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$INPUT")
SRC_H=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$INPUT")
SRC_FPS_RAW=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$INPUT")
SRC_FPS=$(awk -F/ '{if ($2 && $2 != 0) printf "%d", ($1/$2)+0.5; else print $1}' <<< "$SRC_FPS_RAW")
FPS="${FPS_ARG:-$SRC_FPS}"
STAGE_W="${STAGE_W:-$SRC_W}"; STAGE_H="${STAGE_H:-$SRC_H}"
HAS_AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$INPUT" | head -1)
if [ -n "$HAS_AUDIO" ]; then AUDIO_NOTE="yes"; else AUDIO_NOTE="no"; fi

note "source: ${SRC_W}x${SRC_H} @ ${SRC_FPS}fps, audio: $AUDIO_NOTE"
note "stage:  ${STAGE_W}x${STAGE_H} @ ${FPS}fps"

# Keep the supplied clip untouched.
if [ "$INPUT" != "$PWD/assets/media/raw.mp4" ]; then
  cp "$INPUT" assets/media/raw.mp4
  note "raw clip copied to assets/media/raw.mp4 (original untouched)"
fi

# ---------- Stage 1: FFmpeg pre ----------
step "Stage 1 — FFmpeg pre (clean.mp4)"

FILTERS=""
# Aspect-preserving scale: plain scale=W:H stretches a non-9:16
# source into the stage. increase + crop keeps the picture intact.
[ "$SRC_W" != "$STAGE_W" ] || [ "$SRC_H" != "$STAGE_H" ] && FILTERS="scale=${STAGE_W}:${STAGE_H}:force_original_aspect_ratio=increase,crop=${STAGE_W}:${STAGE_H}"
[ "$SRC_FPS" != "$FPS" ] && FILTERS="${FILTERS:+$FILTERS,}fps=${FPS}"
[ "$DENOISE" = "1" ] && FILTERS="${FILTERS:+$FILTERS,}hqdn3d=1.5:1.5:6:6"
case "$GRADE" in
  warm)  FILTERS="${FILTERS:+$FILTERS,}eq=contrast=1.05:saturation=1.15:brightness=0.02" ;;
  moody) FILTERS="${FILTERS:+$FILTERS,}eq=contrast=1.08:saturation=0.75:brightness=-0.03,vignette=PI/5" ;;
  none)  : ;;
  *) die "--grade must be warm, moody, or none" ;;
esac

if [ -z "$FILTERS" ]; then
  ffmpeg -v error -i assets/media/raw.mp4 -map 0:v:0 -map 0:a? -c copy assets/media/clean.mp4 -y
  note "no normalisation needed — clean.mp4 is a stream copy of raw.mp4"
else
  note "filters: $FILTERS"
  ffmpeg -v error -i assets/media/raw.mp4 -vf "$FILTERS" -map 0:v:0 -map 0:a? \
    -c:v libx264 -crf 16 -pix_fmt yuv420p -c:a copy assets/media/clean.mp4 -y
fi

# Source audio, kept aside for finishing (never from the muted render).
if [ -n "$HAS_AUDIO" ]; then
  ffmpeg -v error -i assets/media/raw.mp4 -map 0:a:0 -c:a copy assets/media/source_audio.m4a -y
fi

# Point the composition at clean.mp4 (backup on first swap only).
# NOTE: the backup MUST NOT end in .html — the checker discovers
# every root-level *.html file as a composition, and a backup copy
# fails the check with multiple_root_compositions. index.html.bak
# is invisible to it.
if grep -q 'assets/media/raw.mp4' index.html; then
  [ -f index.html.bak ] || cp index.html index.html.bak
  sed -i 's|assets/media/raw.mp4|assets/media/clean.mp4|g' index.html
  note "index.html video src: raw.mp4 -> clean.mp4 (backup: index.html.bak)"
fi

# Loop stills must come from the clip that actually renders.
if [ -f assets/media/opening.png ]; then
  [ -f assets/media/opening.raw.png ] || cp assets/media/opening.png assets/media/opening.raw.png
  ffmpeg -v error -ss 0 -i assets/media/clean.mp4 -frames:v 1 assets/media/opening.png -y
  note "opening.png regenerated from clean.mp4 frame 0 (backup: opening.raw.png)"
fi

# GSAP must load in the render browser: vendor it locally if still on CDN.
if grep -q 'cdn.jsdelivr.net/npm/gsap' index.html; then
  if [ ! -f assets/js/gsap.min.js ]; then
    mkdir -p assets/js
    if curl -sL -o assets/js/gsap.min.js https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js \
       && head -c 20 assets/js/gsap.min.js | grep -q 'GSAP'; then
      note "GSAP 3.12.5 vendored to assets/js/gsap.min.js"
    else
      rm -f assets/js/gsap.min.js
      note "WARNING: GSAP download failed — CDN src left as-is; check may fail in the browser"
    fi
  fi
  if [ -f assets/js/gsap.min.js ]; then
    [ -f index.html.bak ] || cp index.html index.html.bak
    sed -i 's|https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js|assets/js/gsap.min.js|g' index.html
    note "index.html GSAP src: CDN -> assets/js/gsap.min.js"
  fi
fi

# ---------- Stage 2: HyperFrames ----------
step "Stage 2 — HyperFrames lint / check / snapshot / render"

LINT_OUT=$(npx hyperframes lint 2>&1 | tail -25)
echo "$LINT_OUT"
echo "$LINT_OUT" | grep -q '0 error(s)' || die "lint did not pass — fix the errors above, then re-run"

CHECK_OUT=$(npx hyperframes check 2>&1 | tail -25)
echo "$CHECK_OUT"
echo "$CHECK_OUT" | grep -q 'Check passed' || die "check did not pass — fix the errors above, then re-run"

if [ -n "$SNAPSHOT" ]; then
  npx hyperframes snapshot --at "$SNAPSHOT" -o "snapshots-$NAME" --no-end 2>&1 | tail -4
  note "snapshots in snapshots-$NAME — review them before trusting the render"
fi

npx hyperframes render -f "$FPS" -q "$QUALITY" -o "renders/${NAME}-videoonly.mp4" 2>&1 | tail -6
[ -f "renders/${NAME}-videoonly.mp4" ] || die "render produced no file"

# ---------- Stage 3: FFmpeg post (audio finish + mux) ----------
step "Stage 3 — FFmpeg post (audio finish + mux)"

measure() { # measure <file> -> prints "I TP" (LUFS, dBTP)
  ffmpeg -i "$1" -af loudnorm=print_format=json -f null - 2>&1 \
    | grep -E '"input_i"|"input_tp"' \
    | sed -E 's/.*: "(-?[0-9.]+)".*/\1/' | tr '\n' ' '
}

if [ -n "$HAS_AUDIO" ]; then
  ffmpeg -v error -i assets/media/source_audio.m4a \
    -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k assets/media/finished_audio.m4a -y
  # Corrective loop (max 2): gain toward -14, capped by a limiter so
  # peaks stay under -1 dBTP. Straight loudnorm alone can land
  # >1 LU off target and AAC encoding can push true peaks over 0.
  for _ in 1 2; do
    read -r MI MTP <<< "$(measure assets/media/finished_audio.m4a)"
    GAIN=$(awk -v mi="$MI" 'BEGIN {printf "%.2f", -14 - mi}')
    ABS_GAIN=$(awk -v g="$GAIN" 'BEGIN {printf "%.2f", (g < 0 ? -g : g)}')
    note "finished audio now: ${MI} LUFS / ${MTP} dBTP (correction ${GAIN} dB)"
    if awk -v a="$ABS_GAIN" 'BEGIN {exit !(a < 0.3)}'; then break; fi
    ffmpeg -v error -i assets/media/finished_audio.m4a \
      -af "volume=${GAIN}dB,alimiter=limit=0.79:attack=5:release=50:level=false" \
      -c:a aac -b:a 192k assets/media/finished_audio2.m4a -y
    mv assets/media/finished_audio2.m4a assets/media/finished_audio.m4a
  done
  ffmpeg -v error -i "renders/${NAME}-videoonly.mp4" -i assets/media/finished_audio.m4a \
    -map 0:v:0 -map 1:a:0 -c:v copy -c:a copy -shortest "renders/${NAME}.mp4" -y
else
  cp "renders/${NAME}-videoonly.mp4" "renders/${NAME}.mp4"
  note "source had no audio — final is the video-only render"
fi

# ---------- Stage 4: QC ----------
step "Stage 4 — QC"

FINAL="renders/${NAME}.mp4"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$FINAL")
FW=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$FINAL")
FH=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$FINAL")
MID=$(awk -v d="$DUR" 'BEGIN {printf "%.2f", d/2}')
END=$(awk -v d="$DUR" 'BEGIN {printf "%.2f", d-0.1}')
mkdir -p "qc-$NAME"
ffmpeg -v error -ss 0 -i "$FINAL" -frames:v 1 "qc-$NAME/f_start.png" -y
ffmpeg -v error -ss "$MID" -i "$FINAL" -frames:v 1 "qc-$NAME/f_mid.png" -y
ffmpeg -v error -ss "$END" -i "$FINAL" -frames:v 1 "qc-$NAME/f_end.png" -y

LOOP_DIFF="n/a (PIL not available)"
if python3 -c "import PIL" 2>/dev/null; then
  LOOP_DIFF=$(python3 -c "
from PIL import Image
a = Image.open('qc-$NAME/f_start.png').convert('RGB').resize((72,128))
b = Image.open('qc-$NAME/f_end.png').convert('RGB').resize((72,128))
d = sum(abs(x-y) for p1, p2 in zip(a.getdata(), b.getdata()) for x, y in zip(p1, p2)) / (72*128*3)
print(f'{d:.1f}')
")
fi

REPORT="renders/QC_REPORT-${NAME}.txt"
{
  echo "QC report — $NAME (merged FFmpeg + HyperFrames pipeline)"
  echo "final: $FINAL"
  echo "duration: ${DUR}s | resolution: ${FW}x${FH} | stage: ${STAGE_W}x${STAGE_H} @ ${FPS}fps"
  if [ -n "$HAS_AUDIO" ]; then
    read -r FI FTP <<< "$(measure "$FINAL")"
    echo "loudness (final file): ${FI} LUFS / ${FTP} dBTP — gate: -14 LUFS target, TP <= -1"
  else
    echo "loudness: no audio in source (gate n/a)"
  fi
  echo "loop-match: mean abs pixel diff start-vs-end frames = $LOOP_DIFF (0-255; <15 = PASS heuristic)"
  echo "frames: qc-$NAME/f_start.png, f_mid.png, f_end.png"
  echo "check: 0 errors required (script stops otherwise)"
  echo ""
  echo "NOT checked by this script (verify by watching): rewatch trigger"
  echo "presence, caption/word sync, SFX placement, frozen stare, clean output."
  echo "Last line of every run: ship it, or change it?"
} | tee "$REPORT"

echo ""
echo "Done: $FINAL"
echo "Report: $REPORT"
