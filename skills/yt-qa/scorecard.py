#!/usr/bin/env python3
"""Score a prepped video on the ten-point scorecard.

    python3 scorecard.py --identity 3 --movement 2 --phone 2 --beats 2
    python3 scorecard.py --identity 1 --movement 3 --phone 2 --beats 2 --json

Ranges: identity 0-3, movement 0-3, phone 0-2, beats 0-2.
Publish threshold: total >= 8 AND identity >= 2 AND movement >= 2.
A total of 8 with identity 1 still FAILS: the sub-thresholds
are gates, not suggestions. Exit 0 on PASS, 1 on FAIL.

v3.3.6 hard gates (optional flags; a supplied gate that fails
fails the whole scorecard, even at 10/10):
    --width/--height: format gate. 9:16 ratio required; 1080x1920
        preferred, 720x1280 at the same ratio is the minimum
        acceptable (v3.3.4). Never upscale to fake 1080p.
    --nose: frontal-frame nose-ring verdict: frontal-right passes;
        centre, septum, tip, or two rings FAIL (v3.3.5). The verdict
        must come from a FRONTAL frame, not a diagonal action frame.
    --slot: leotard colour; must be one of the five rotation
        colours (v3.3.3). This checks the palette only; whether the
        slot repeats the previous video is the series log's job.
    --lufs/--peak/--beat: audio gate (v3.3.2). Integrated loudness
        -14 LUFS target (tool tolerance -16 to -12), true peak at
        most -1 dBTP, and a beat track present. Measure with
        loudness.py (yt-sound) or a DAW; room noise alone FAILS.
    --loop-match: loop gate (v3.3.7). "matched" means the final
        frame returns to the opening frame per the FINAL loop
        bridge (static rebound, or dynamic mid-takeoff cut);
        "mismatch" FAILS. Judge it on the rendered video, not
        on the brief's claim.
    --rewatch: rewatch gate (v3.3.7). "yes" means one rewatch
        trigger is actually present in the video (a hidden
        detail, missed moment, count, or satisfying payoff);
        "no" FAILS. A trigger claimed in the brief but absent
        from the video is "no".
    --peak-tension: peak gate (v3.4.2). "sustained" means the
        peak beat shows sustained tension through the hold
        (limbs locked with no sag, tremor, set jaw, eyes per
        the eye rule); "released" FAILS — neutral face, sagging
        limbs, eyes shut, or peak form covered at the peak.

Gates this tool CANNOT verify are printed on every run, so a
PASS is never mistaken for a full QA pass: face gate (200-300%
face crop), text-end rule, parasocial tail cap, and the slot
vs previous video, plus loop match, rewatch trigger, peak
tension, text inventory, post-peak gap, question-skill match,
and one-way consistency when their flags are not supplied.
Those stay human checks in yt-qa.
"""
import argparse
import json
import sys

LIMITS = {"identity": 3, "movement": 3, "phone": 2, "beats": 2}
ROTATION_COLOURS = ("purple", "teal", "black", "royal blue", "burgundy")
NOT_VERIFIED = ("face gate (200-300% face crop)", "text-end rule",
                "parasocial tail cap (beat+CTA max 2s)",
                "leotard slot vs previous video",
                "loop match (end frame = opening frame)",
                "rewatch trigger (one per video)",
                "peak tension (sustained through the hold)",
                "text inventory (no metadata labels)",
                "post-peak gap (beat between peak and tail)",
                "question-skill match (range question needs a progressive skill)",
                "one-way consistency (text and body tell one story)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name, limit in LIMITS.items():
        parser.add_argument(f"--{name}", type=int, required=True,
                            help=f"0-{limit}")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--width", type=int, default=None,
                        help="rendered video width in pixels")
    parser.add_argument("--height", type=int, default=None,
                        help="rendered video height in pixels")
    parser.add_argument("--nose", default=None,
                        choices=("frontal-right", "centre", "septum", "tip", "two"),
                        help="frontal-frame nose-ring verdict")
    parser.add_argument("--slot", default=None,
                        help="leotard colour for this video")
    parser.add_argument("--lufs", type=float, default=None,
                        help="integrated loudness in LUFS")
    parser.add_argument("--peak", type=float, default=None,
                        help="true peak in dBTP")
    parser.add_argument("--beat", default=None, choices=("yes", "no"),
                        help="beat track present from the first 2s")
    parser.add_argument("--loop-match", default=None,
                        choices=("matched", "mismatch"),
                        help="final frame returns to the opening frame")
    parser.add_argument("--rewatch", default=None, choices=("yes", "no"),
                        help="one rewatch trigger actually present")
    parser.add_argument("--peak-tension", default=None,
                        choices=("sustained", "released"),
                        help="peak beat shows sustained tension, not release")
    args = parser.parse_args()
    scores = {name: getattr(args, name) for name in LIMITS}
    errors = [f"{n} must be 0-{LIMITS[n]}" for n, v in scores.items()
              if v < 0 or v > LIMITS[n]]
    if (args.width is None) != (args.height is None):
        errors.append("--width and --height must be given together")
    if errors:
        print("INVALID: " + "; ".join(errors), file=sys.stderr)
        return 2
    total = sum(scores.values())
    reasons = []
    gates_checked = []
    if total < 8:
        reasons.append(f"total {total} < 8")
    if scores["identity"] < 2:
        reasons.append(f"identity {scores['identity']} < 2")
    if scores["movement"] < 2:
        reasons.append(f"movement {scores['movement']} < 2")
    if args.width is not None:
        gates_checked.append("format")
        ratio_ok = abs(args.width * 16 - args.height * 9) <= max(args.width, args.height)
        if not ratio_ok:
            reasons.append(f"format gate: {args.width}x{args.height} is not 9:16")
        elif args.height < 1280:
            reasons.append(f"format gate: {args.width}x{args.height} below "
                           "720x1280 minimum acceptable")
    if args.nose is not None:
        gates_checked.append("nose")
        if args.nose != "frontal-right":
            reasons.append(f"nose gate: frontal verdict is {args.nose}, "
                           "not character's RIGHT nostril wing only")
    if args.slot is not None:
        gates_checked.append("slot")
        if args.slot.lower() not in ROTATION_COLOURS:
            reasons.append(f"slot gate: {args.slot!r} is not a rotation colour "
                           f"({', '.join(ROTATION_COLOURS)})")
    if args.lufs is not None or args.peak is not None or args.beat is not None:
        gates_checked.append("audio")
        if args.lufs is not None and not (-16 <= args.lufs <= -12):
            reasons.append(f"audio gate: {args.lufs} LUFS outside -16 to -12 "
                           "(target -14 LUFS)")
        if args.peak is not None and args.peak > -1:
            reasons.append(f"audio gate: true peak {args.peak} dBTP above -1")
        if args.beat == "no":
            reasons.append("audio gate: no beat track (room noise alone FAILS)")
    if args.loop_match is not None:
        gates_checked.append("loop")
        if args.loop_match == "mismatch":
            reasons.append("loop gate: final frame does not return to the "
                           "opening frame (static rebound or dynamic "
                           "mid-takeoff cut)")
    if args.rewatch is not None:
        gates_checked.append("rewatch")
        if args.rewatch == "no":
            reasons.append("rewatch gate: no rewatch trigger actually "
                           "present (one hidden detail, missed moment, "
                           "count, or satisfying payoff per video)")
    if args.peak_tension is not None:
        gates_checked.append("peak")
        if args.peak_tension == "released":
            reasons.append("peak gate: tension released at the peak beat "
                           "(neutral face, sagging limbs, eyes shut, or "
                           "peak form covered — see yt-story peak rule)")
    not_verified = [g for g in NOT_VERIFIED
                    if not (g.startswith("loop match") and args.loop_match is not None)
                    and not (g.startswith("rewatch trigger") and args.rewatch is not None)
                    and not (g.startswith("peak tension") and args.peak_tension is not None)]
    verdict = "FAIL" if reasons else "PASS"
    if args.json:
        print(json.dumps({"scores": scores, "total": total,
                          "verdict": verdict, "reasons": reasons,
                          "gates_checked": gates_checked,
                          "gates_not_verified": not_verified}))
    else:
        print(f"SCORECARD: identity {scores['identity']}/3, "
              f"movement {scores['movement']}/3, phone {scores['phone']}/2, "
              f"beats {scores['beats']}/2, total {total}/10 -> {verdict}")
        if gates_checked:
            print("Gates checked: " + ", ".join(gates_checked))
        print("GATES NOT VERIFIED BY THIS TOOL: " + "; ".join(not_verified))
        if reasons:
            print("Failed gates: " + "; ".join(reasons))
            print("Fix: regenerate the failing segment first; "
                  "below threshold with no fixable segment = fallback.")
    return 1 if reasons else 0


if __name__ == "__main__":
    raise SystemExit(main())
