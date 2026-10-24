#!/usr/bin/env python3
"""originality_scan.py - flag repetition and disclosure questions
across a channel's recent uploads, for human review.

    python3 originality_scan.py uploads.json
    python3 originality_scan.py uploads.json --json

Input JSON:
    {"videos": [{"title": "...",
                 "structure": "attempt-fail-retry-payoff",
                 "phrases": ["only one worked", "day 12"],
                 "ai_generated": true,
                 "realistic_scene": true,
                 "real_person_or_event": false,
                 "health_claim": false,
                 "dangerous_move": true,
                 "disclaimer_included": false,
                 "minor_subject": false}]}

This tool makes NO policy verdict. It flags what a human must review
before publishing, against three rules creators trip over:

  1. Shorts originality prioritisation (1 Oct 2026): re-uploads
     without significant changes lose reach. A voiceover merely
     describing the screen, small technical edits, and applying the
     same template to many clips do NOT count as original; own
     commentary, analysis or storytelling do.
  2. YPP "inauthentic content" (15 July 2025): mass-produced or
     repetitive content is ineligible for monetisation regardless
     of how it was made. Vary the SUBSTANCE of each video, not
     just the intro, outro or template.
  3. AI disclosure: disclose realistic synthetic content a viewer
     could believe is real - a photorealistic AI gymnast doing a
     real-looking skill is exactly that case. AI-written scripts,
     titles, captions and thumbnails do NOT require disclosure,
     and neither does own-voice cloning for voiceover or dubs.

Repetition is measured, not guessed: a structure or phrase is
flagged when it appears in 3 or more of the videos supplied.
"""
import json
import sys
from collections import Counter


def scan(videos):
    structures = Counter(v["structure"] for v in videos if v.get("structure"))
    phrases = Counter()
    for v in videos:
        for p in v.get("phrases") or []:
            phrases[p] += 1
    repeated_structures = {s: c for s, c in structures.items() if c >= 3}
    repeated_phrases = {p: c for p, c in phrases.items() if c >= 3}

    reviews = []
    for v in videos:
        items = []
        if v.get("structure") in repeated_structures:
            items.append(
                f"structure '{v['structure']}' repeats "
                f"{repeated_structures[v['structure']]} times in this set - "
                "vary the substance of this video, not just its intro/outro.")
        for p in v.get("phrases") or []:
            if p in repeated_phrases:
                items.append(
                    f"phrase '{p}' repeats {repeated_phrases[p]} times - "
                    "a repeated catchphrase across many videos reads as a template.")
        if v.get("ai_generated") and v.get("realistic_scene"):
            items.append(
                "DISCLOSURE CHECK: AI-generated and realistic-looking. If a "
                "viewer could believe this scene is real, disclose it in "
                "Studio's AI-use attribute before publishing.")
        if v.get("real_person_or_event"):
            items.append(
                "DISCLOSURE CHECK: a real person appears to say or do "
                "something, or real event/place footage is altered - "
                "disclose it in Studio.")
        if v.get("health_claim"):
            items.append(
                "SAFETY REVIEW: a health claim is present. Never let a "
                "synthetic persona give health advice, and do not make "
                "miracle or guaranteed-result claims.")
        if v.get("dangerous_move") and not v.get("disclaimer_included"):
            items.append(
                "SAFETY REVIEW: a dangerous move without warm-up, "
                "progression or disclaimer language. Add the progression "
                "and the disclaimer, or cut the move.")
        if v.get("minor_subject"):
            items.append(
                "SAFETY REVIEW: a minor-appearing subject. Avoid "
                "idealised-body or weight framing, and keep the focus "
                "on the skill, not the body.")
        reviews.append({"title": v.get("title", "(untitled)"),
                        "review_items": items})
    flagged = sum(1 for r in reviews if r["review_items"])
    return {"videos_checked": len(videos),
            "repeated_structures": repeated_structures,
            "repeated_phrases": repeated_phrases,
            "videos_flagged": flagged,
            "reviews": reviews,
            "note": "This is a review prompt, not a policy verdict. "
                    "YouTube makes the call; this tool only makes sure "
                    "a human looked at the right questions first."}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    data = json.load(open(args[0], encoding="utf-8"))
    result = scan(data.get("videos", []))
    if as_json:
        print(json.dumps(result, indent=1))
        return
    print(f"\n  Originality scan: {result['videos_checked']} videos, "
          f"{result['videos_flagged']} flagged for review")
    if result["repeated_structures"]:
        print("  repeated structures: " +
              ", ".join(f"{s} (x{c})" for s, c in
                        result["repeated_structures"].items()))
    if result["repeated_phrases"]:
        print("  repeated phrases: " +
              ", ".join(f"{p} (x{c})" for p, c in
                        result["repeated_phrases"].items()))
    for r in result["reviews"]:
        if r["review_items"]:
            print(f"\n  {r['title']}")
            for item in r["review_items"]:
                print(f"    - {item}")
    print(f"\n  {result['note']}\n")


if __name__ == "__main__":
    main()
