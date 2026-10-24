#!/usr/bin/env python3
"""shorts_score.py - score a Short before you publish it.

Usage:
    python3 shorts_score.py --title "..." --thumb "..." --hook "..." \
        --loop yes --cta "follow for part 2" --series "Skill Challenge"
    python3 shorts_score.py --title "..." --thumb "..." --json

Scores five checks, 0-20 each, for a total of 0-100:
  TITLE   60 characters or fewer, with a concrete word or number
  THUMB   thumbnail text does not repeat the title, 3 words or fewer
  HOOK    first line asks a question, states stakes, or gives a number
  LOOP    the last line sets up the first line again
  CLOSE   exactly one call to action, not three

This is a checklist heuristic, not a predictor. A high score does not
promise views and a low score is a reason to rewrite, not a verdict
on the idea. It does not touch media and it does not publish.
"""
import argparse
import json
import re
import sys


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--thumb", default="")
    parser.add_argument("--hook", default="")
    parser.add_argument("--loop", default="no")
    parser.add_argument("--cta", default="")
    parser.add_argument("--series", default="")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    checks = {}

    title_score = 0
    if len(args.title) <= 60:
        title_score += 10
    if re.search(r"\d", args.title):
        title_score += 10
    checks["TITLE"] = {
        "score": title_score,
        "note": "Title is 60 characters or fewer and carries a number."
        if title_score == 20 else
        "Shorten the title to 60 characters or fewer and add a concrete number.",
    }

    thumb_words = words(args.thumb)
    title_words = set(words(args.title))
    overlap = [w for w in thumb_words if w in title_words]
    thumb_score = 0
    if len(thumb_words) <= 3:
        thumb_score += 10
    if not overlap:
        thumb_score += 10
    checks["THUMB"] = {
        "score": thumb_score,
        "note": "Thumbnail text is 3 words or fewer and does not repeat the title."
        if thumb_score == 20 else
        f"Thumbnail repeats {overlap} from the title or has more than 3 words.",
    }

    hook_score = 0
    hook = args.hook or args.title
    if "?" in hook:
        hook_score += 10
    if re.search(r"\b(only|first|last|win|lose|fail|secret|test)\b", hook.lower()):
        hook_score += 10
    checks["HOOK"] = {
        "score": hook_score,
        "note": "First line opens a question or stakes."
        if hook_score == 20 else
        "Open with a question, a stake, or a test, not a greeting.",
    }

    loop_score = 20 if args.loop.strip().lower() in ("yes", "y", "true", "1") else 0
    checks["LOOP"] = {
        "score": loop_score,
        "note": "Last line loops back to the first line."
        if loop_score else "Add a loop point: the last line should set up the first line.",
    }

    cta_score = 20 if args.cta.strip() else 0
    checks["CLOSE"] = {
        "score": cta_score,
        "note": "Exactly one call to action."
        if cta_score else "End with exactly one call to action.",
    }

    total = sum(item["score"] for item in checks.values())
    verdict = "READY" if total >= 80 else "REWRITE" if total < 60 else "FIX THE WEAK CHECK"
    result = {
        "total": total,
        "verdict": verdict,
        "series": args.series,
        "checks": checks,
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Shorts score: {total}/100  {verdict}")
        for name, item in checks.items():
            print(f"  {name}: {item['score']}/20 - {item['note']}")
    return 0 if total >= 60 else 1


if __name__ == "__main__":
    raise SystemExit(main())
