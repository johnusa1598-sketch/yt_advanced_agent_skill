#!/usr/bin/env python3
"""loudness.py - measure a finished audio/video file against the audio gate.

    python3 loudness.py finished.wav
    python3 loudness.py finished.mp4 --json

Uses ffmpeg's ebur128 filter (true-peak mode) - no DAW, no guessing.
The audio gate (v3.3.2, yt-sound / yt-qa):
    integrated loudness -14 LUFS target (this tool allows -16 to -12)
    true peak at most -1 dBTP (ebur128 true peak reads as dBFS here;
    it is the oversampled peak, the same number the gate means)
    a beat track present from the first 2 seconds (this tool cannot
    hear whether a beat track exists - that stays a human check, and
    scorecard.py takes it as --beat yes/no)

Exit 0 on PASS, 1 on FAIL, 2 when ffmpeg is missing, the file is
missing, or the measurement cannot be parsed. This tool measures
only; it does not normalize or rewrite anything. Feed its numbers
into scorecard.py (--lufs / --peak) for the full QA verdict.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys

LUFS_LOW, LUFS_HIGH, PEAK_MAX = -16.0, -12.0, -1.0


def measure(path):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return None, "ffmpeg is not installed"
    result = subprocess.run(
        [ffmpeg, "-hide_banner", "-i", path, "-vn",
         "-af", "ebur128=framelog=quiet:peak=true", "-f", "null", "-"],
        capture_output=True, text=True, timeout=300)
    text = result.stderr
    summary = text.split("Summary:")[-1] if "Summary:" in text else text
    lufs = re.findall(r"I:\s+(-?\d+(?:\.\d+)?)\s+LUFS", summary)
    peak = re.findall(r"Peak:\s+(-?\d+(?:\.\d+)?)\s+dBFS", summary)
    if not lufs or not peak:
        return None, "could not parse an ebur128 summary from ffmpeg output"
    return {"lufs": float(lufs[-1]), "true_peak_dbfs": float(peak[-1])}, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    values, error = measure(args.file)
    if error:
        print(f"loudness.py: {error}", file=sys.stderr)
        return 2
    reasons = []
    if not (LUFS_LOW <= values["lufs"] <= LUFS_HIGH):
        reasons.append(f"{values['lufs']} LUFS outside -16 to -12 "
                       "(target -14 LUFS)")
    if values["true_peak_dbfs"] > PEAK_MAX:
        reasons.append(f"true peak {values['true_peak_dbfs']} dBFS above -1")
    verdict = "FAIL" if reasons else "PASS"
    if args.json:
        print(json.dumps({"file": args.file, "verdict": verdict,
                          "reasons": reasons, **values}))
    else:
        print(f"LOUDNESS: {values['lufs']} LUFS, true peak "
              f"{values['true_peak_dbfs']} dBFS -> {verdict}")
        for reason in reasons:
            print(f"  x {reason}")
        if not reasons:
            print("  Beat track still needs a human check: "
                  "present from the first 2 seconds?")
    return 1 if reasons else 0


if __name__ == "__main__":
    raise SystemExit(main())
