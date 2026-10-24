#!/usr/bin/env python3
"""srt_qa.py - quality-check an SRT caption file before upload.

    python3 srt_qa.py captions.srt
    python3 srt_qa.py captions.srt --safety-words safety.txt --json

Checks (text files only, no rendering):
  - timing overlaps and out-of-order cues (ERROR)
  - empty cues (ERROR)
  - cues shorter than 0.4s or longer than 7s (WARN - readability guide)
  - reading speed above 20 characters/second (WARN - readability guide)
  - more than 2 lines in a cue, or a line longer than 42 characters
    (WARN - safe-zone / readability guide)
  - a cue whose text does not end in sentence punctuation (WARN)
  - with --safety-words: which listed safety terms appear in the file
    and which are missing, so a translated caption can be checked for
    dropped safety cues (warm-up, spotter, stop, pain, mat, ...)

The speed, line and duration numbers are readability guidelines, not
YouTube rules. YouTube publishes no SRT speed limit; the check is
there so a human looks at the cue, not so a script can pass it.
"""
import json
import re
import sys


def to_ms(t):
    m = re.match(r"(\d+):(\d+):(\d+)[,.](\d+)", t.strip())
    if not m:
        return None
    h, mi, s, ms = (int(x) for x in m.groups())
    return ((h * 3600 + mi * 60 + s) * 1000) + ms


def parse(path):
    text = open(path, encoding="utf-8-sig").read()
    blocks = re.split(r"\n\s*\n", text.strip())
    cues = []
    for block in blocks:
        lines = block.strip().splitlines()
        if len(lines) < 2:
            continue
        m = re.search(r"(\S+)\s*-->\s*(\S+)", lines[1] if len(lines) > 1 else "")
        if not m:
            continue
        start, end = to_ms(m.group(1)), to_ms(m.group(2))
        if start is None or end is None:
            continue
        cue_text = " ".join(l.strip() for l in lines[2:] if l.strip())
        cues.append({"n": len(cues) + 1, "start": start, "end": end,
                     "lines": [l for l in lines[2:] if l.strip()],
                     "text": cue_text})
    return cues


def check(cues, safety_words=None):
    errors, warns = [], []
    for i, c in enumerate(cues):
        dur = (c["end"] - c["start"]) / 1000.0
        if not c["text"]:
            errors.append(f"cue {c['n']}: empty text")
            continue
        if i > 0 and c["start"] < cues[i - 1]["end"]:
            errors.append(f"cue {c['n']}: overlaps previous cue "
                          f"(starts before cue {cues[i-1]['n']} ends)")
        if i > 0 and c["start"] < cues[i - 1]["start"]:
            errors.append(f"cue {c['n']}: out of order")
        if dur < 0.4:
            warns.append(f"cue {c['n']}: very short ({dur:.1f}s) - "
                         "may flash past sound-off viewers")
        if dur > 7:
            warns.append(f"cue {c['n']}: very long ({dur:.1f}s) - "
                         "split it so the text keeps up with the video")
        cps = len(c["text"]) / dur if dur > 0 else 0
        if cps > 20:
            warns.append(f"cue {c['n']}: reading speed {cps:.0f} chars/s "
                         "- fast for sound-off viewers, consider splitting")
        if len(c["lines"]) > 2:
            warns.append(f"cue {c['n']}: {len(c['lines'])} lines - "
                         "keep to 2 lines max so text stays in the safe zone")
        for line in c["lines"]:
            if len(line) > 42:
                warns.append(f"cue {c['n']}: line over 42 characters - "
                             "may run outside the safe zone on TV")
                break
        if not re.search(r"[.!?\u2026)\"]\s*$", c["text"]):
            warns.append(f"cue {c['n']}: no sentence punctuation at the end "
                         "- a cut-off cue reads as unfinished")
    safety = None
    if safety_words:
        blob = " ".join(c["text"].lower() for c in cues)
        safety = {"present": [w for w in safety_words if w.lower() in blob],
                  "missing": [w for w in safety_words if w.lower() not in blob]}
    return {"cues": len(cues), "errors": errors, "warnings": warns,
            "safety": safety,
            "verdict": ("FAIL - fix the errors above" if errors
                        else "PASS with warnings - review them" if warns
                        else "PASS")}


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    safety_path = None
    files = []
    i = 0
    while i < len(args):
        if args[i] == "--safety-words" and i + 1 < len(args):
            safety_path = args[i + 1]
            i += 1
        elif not args[i].startswith("--"):
            files.append(args[i])
        i += 1
    if not files:
        print(__doc__)
        sys.exit(1)
    safety_words = None
    if safety_path:
        safety_words = [l.strip() for l in
                        open(safety_path, encoding="utf-8")
                        if l.strip() and not l.startswith("#")]
    result = check(parse(files[0]), safety_words)
    if as_json:
        print(json.dumps(result, indent=1))
    else:
        print(f"\n  SRT QA: {files[0]} ({result['cues']} cues)")
        for e in result["errors"]:
            print(f"    ERROR: {e}")
        for w in result["warnings"]:
            print(f"    WARN: {w}")
        if result["safety"]:
            print(f"    safety terms present: {result['safety']['present']}")
            print(f"    safety terms missing: {result['safety']['missing']}")
        print(f"    VERDICT: {result['verdict']}\n")
    sys.exit(1 if result["errors"] else 0)


if __name__ == "__main__":
    main()
