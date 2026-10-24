#!/usr/bin/env python3
"""retention_plan.py - plan the retention curve of one video before it is made.

    python3 retention_plan.py brief.json
    python3 retention_plan.py brief.json --json

Brief JSON fields:
    format      - "short" or "long" (default: short)
    duration_s  - length in seconds (default: 30)
    hook        - the 0-3s hook line
    loop        - the loop idea for a Short ("last line sets up first line")
    beats       - [{"time": "0-3s", "text": "what happens"}]
    cta         - the one call to action

The plan is a checklist, not a prediction. It marks the three jobs every
video has: hold the first 3 seconds, re-earn attention before every
likely drop, and for a Short, end on a line that makes a rewatch feel
like a continuation. Two mechanical checks run on the beats themselves:
  - a beat longer than the format's beat budget with no change inside
    it is flagged as a likely drop point
  - a Short with no loop line, or a long video with no re-hook in a
    long middle stretch, is flagged, because the plan has a hole in it
Validate the plan against the video's own retention curve afterwards
with retention.py - a flagged beat that held is a lesson, not a failure.
"""
import json, os, re, sys

def parse_time(spec):
    """'0-3s' or '12s' -> (start, end) in seconds, or None."""
    m = re.match(r"\s*(\d+)\s*(?:-\s*(\d+)\s*)?s?\s*$", str(spec or ""))
    if not m:
        return None
    a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
    return (a, max(b, a))

def build(brief):
    fmt = (brief.get("format") or "short").lower()
    dur = int(brief.get("duration_s") or (30 if fmt == "short" else 600))
    hook = (brief.get("hook") or "").strip()
    loop = (brief.get("loop") or "").strip()
    cta = (brief.get("cta") or "").strip()
    beats_in = brief.get("beats") or []
    budget = 8 if fmt == "short" else 45  # seconds a beat may run unchanged

    beats, flags = [], []
    prev_end = 0
    for b in beats_in:
        span = parse_time(b.get("time", ""))
        start, end = span if span else (prev_end, prev_end)
        text = (b.get("text") or "").strip()
        length = end - start
        purpose = "setup"
        if start == 0:
            purpose = "hook"
        elif text and any(w in text.lower() for w in
                          ["but", "fail", "wrong", "however", "twist", "turn"]):
            purpose = "turn"
        elif end >= dur - 3:
            purpose = "payoff/loop"
        beats.append({"time": b.get("time", ""), "start": start, "end": end,
                      "text": text, "purpose": purpose,
                      "length_s": length})
        if length > budget:
            flags.append({"at": b.get("time", ""), "kind": "long-beat",
                          "fix": f"{length}s with no change inside it - split it, "
                                 f"cut in a reaction, or move the payoff earlier"})
        if start - prev_end > budget:
            flags.append({"at": f"{prev_end}-{start}s", "kind": "gap",
                          "fix": "a stretch with no planned beat - put a re-hook, "
                                 "a question, or a visual change in it"})
        prev_end = max(prev_end, end)

    guards = []
    if fmt == "short":
        guards.append("Mid-turn: one complication or proof before the halfway mark, "
                      "or the swipe comes there.")
        if loop:
            guards.append(f"Loop point (last 2s): {loop} - the last line must "
                          "set up the first line so a rewatch feels continuous.")
        else:
            flags.append({"at": "end", "kind": "no-loop",
                          "fix": "no loop line - write one: the last line sets up "
                                 "the first line, or the Short ends dead"})
        guards.append("Rewatch trigger: the payoff must be visible again on a "
                      "second watch - a landing, a reveal, a score - not a line "
                      "of explanation.")
    else:
        guards.append("Re-hook every beat: each section opens with its own "
                      "question, not a recap of the last one.")
        guards.append("End screen: the next video is named on screen before "
                      "the last 20 seconds, not after the goodbye.")

    curve = [
        {"phase": "0-3s HOOK", "job": "earn the next 10 seconds",
         "check": "hardest moment, fail, or question on screen - no greeting, "
                  "no intro, no setup"},
        {"phase": "middle", "job": "re-earn attention at every beat",
         "check": "each beat ends on a reason to stay, not a summary"},
        {"phase": "end", "job": "payoff, then the next video",
         "check": "CTA is one line, and the loop (Short) or end screen "
                  "(long) is already in motion"},
    ]
    return {
        "format": fmt,
        "duration_s": dur,
        "hook": hook,
        "hook_checklist": [
            "the hook is visible in the first frame, not just spoken",
            "it names the skill or the stakes in under 10 words",
            "it ends on an open question the video will answer",
        ] if hook else ["no hook supplied - write one before anything else"],
        "beats": beats,
        "drop_off_guards": guards,
        "flags": flags,
        "loop": loop,
        "cta": cta,
        "curve": curve,
        "validate_after": "Compare this plan with Studio's retention curve and "
                          "retention.py: a flagged beat that held is a lesson, "
                          "a held beat that was not flagged is a new rule.",
    }

def show(plan):
    print(f"\n  RETENTION PLAN - {plan['format']} {plan['duration_s']}s")
    print(f"\n  HOOK: {plan['hook'] or '(none supplied)'}")
    for c in plan["hook_checklist"]:
        print(f"    - {c}")
    print("\n  BEATS")
    for b in plan["beats"]:
        print(f"    [{b['time']}] ({b['purpose']}) {b['text']}")
    print("\n  DROP-OFF GUARDS")
    for g in plan["drop_off_guards"]:
        print(f"    - {g}")
    if plan["flags"]:
        print("\n  FLAGS - fix before you shoot")
        for f in plan["flags"]:
            print(f"    x [{f['at']}] {f['kind']}: {f['fix']}")
    else:
        print("\n  FLAGS: none - the plan has no mechanical holes")
    print(f"\n  LOOP: {plan['loop'] or '(none)'}")
    print(f"  CTA: {plan['cta'] or '(none)'}")
    print(f"\n  {plan['validate_after']}\n")

def main():
    a = sys.argv[1:]
    as_json = "--json" in a
    files = [x for x in a if not x.startswith("--")]
    if not files or not os.path.exists(files[0]):
        print(__doc__); sys.exit(1)
    brief = json.load(open(files[0], encoding="utf-8"))
    plan = build(brief)
    if as_json:
        print(json.dumps(plan, indent=1)); return
    show(plan)

if __name__ == "__main__":
    main()
