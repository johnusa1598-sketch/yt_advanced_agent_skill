#!/usr/bin/env python3
"""Score a prepped video on the ten-point scorecard.

    python3 scorecard.py --identity 3 --movement 2 --phone 2 --beats 2
    python3 scorecard.py --identity 1 --movement 3 --phone 2 --beats 2 --json

Ranges: identity 0-3, movement 0-3, phone 0-2, beats 0-2.
Publish threshold: total >= 8 AND identity >= 2 AND movement >= 2.
A total of 8 with identity 1 still FAILS: the sub-thresholds
are gates, not suggestions. Exit 0 on PASS, 1 on FAIL.
"""
import argparse
import json
import sys

LIMITS = {"identity": 3, "movement": 3, "phone": 2, "beats": 2}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name, limit in LIMITS.items():
        parser.add_argument(f"--{name}", type=int, required=True,
                            help=f"0-{limit}")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    scores = {name: getattr(args, name) for name in LIMITS}
    errors = [f"{n} must be 0-{LIMITS[n]}" for n, v in scores.items()
              if v < 0 or v > LIMITS[n]]
    if errors:
        print("INVALID: " + "; ".join(errors), file=sys.stderr)
        return 2
    total = sum(scores.values())
    reasons = []
    if total < 8:
        reasons.append(f"total {total} < 8")
    if scores["identity"] < 2:
        reasons.append(f"identity {scores['identity']} < 2")
    if scores["movement"] < 2:
        reasons.append(f"movement {scores['movement']} < 2")
    verdict = "FAIL" if reasons else "PASS"
    if args.json:
        print(json.dumps({"scores": scores, "total": total,
                          "verdict": verdict, "reasons": reasons}))
    else:
        print(f"SCORECARD: identity {scores['identity']}/3, "
              f"movement {scores['movement']}/3, phone {scores['phone']}/2, "
              f"beats {scores['beats']}/2, total {total}/10 -> {verdict}")
        if reasons:
            print("Failed gates: " + "; ".join(reasons))
            print("Fix: regenerate the failing segment first; "
                  "below threshold with no fixable segment = fallback.")
    return 1 if reasons else 0


if __name__ == "__main__":
    raise SystemExit(main())
