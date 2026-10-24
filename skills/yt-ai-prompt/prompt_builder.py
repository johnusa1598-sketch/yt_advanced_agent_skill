#!/usr/bin/env python3
"""prompt_builder.py - build a next-level AI video prompt from a brief.

Usage:
    python3 prompt_builder.py brief.json
    python3 prompt_builder.py brief.json --json

Input JSON example:
    {"character": {"name": "Aria", "hair": "curly dark hair in a big messy bun",
                   "glasses": "thin GOLD wire-frame glasses",
                   "nose_ring": "SMALL gold nose ring in the RIGHT nostril only",
                   "earrings": "SMALL silver hoop earrings",
                   "freckles": "light thin freckles",
                   "outfit": "purple leotard"},
     "scene": "bright indoor gymnastics hall, beam and mats, no crowd",
     "series": "Skill Challenge",
     "title": "Beam backflip, clean landing",
     "hook": "Did she land it?",
     "loop": "The landing sets up the next attempt",
     "action_beats": [
        {"time": "0-2s", "action": "Aria mounts the beam, eyes on the end"},
        {"time": "2-6s", "action": "She runs two steps, springs, and backflips"},
        {"time": "6-10s", "action": "She lands, absorbs with bent knees, arms up"}],
     "camera": "full-body tracking shot, eye level, no cut during the flip",
     "style": "realistic, natural light, slight film grain, not glossy"}

Output: a full 7-layer prompt, a short prompt for quick tools, a
negative prompt, a continuity checklist, and three variants that
keep the character lock and change only camera and motion emphasis.
This tool writes prompts. It does not generate video, and it does
not publish anything. Athletic framing only: no sexualized angles,
poses, or close-ups, and no change to the character spec.
"""
import argparse
import json
import sys

NEGATIVE = [
    "extra limbs, extra fingers, distorted hands, morphing face",
    "glasses changing shape, nose ring changing side, septum ring",
    "outfit changing colour or style mid-shot, jewellery disappearing",
    "sexualized framing, sexualized poses, close-ups on body parts",
    "warped beam, floating props, text errors, watermark, logo",
    "glossy plastic skin, cartoon look, sudden age or identity change",
]


def character_block(character):
    parts = []
    for key in ("name", "hair", "glasses", "nose_ring", "earrings", "freckles", "outfit"):
        value = character.get(key)
        if value:
            parts.append(str(value))
    return "; ".join(parts)


def build(data):
    character = data.get("character", {})
    lock = character_block(character)
    beats = data.get("action_beats", [])
    beat_lines = "\n".join(
        f"- {beat.get('time', '')}: {beat.get('action', '')}".strip()
        for beat in beats
    ) or "- The full skill, start to finish, with a clean landing."
    camera = data.get("camera", "full-body shot, eye level, steady tracking")
    style = data.get("style", "realistic, natural light, not glossy")
    scene = data.get("scene", "")
    series = data.get("series", "")
    hook = data.get("hook", "")
    loop = data.get("loop", "")

    full = (
        f"[CHARACTER LOCK] {lock}. This exact character, no change.\n"
        f"[SCENE LOCK] {scene}\n"
        f"[SERIES] {series}\n"
        f"[HOOK, FIRST 2 SECONDS] {hook}\n"
        f"[ACTION BEATS, WITH PHYSICS]\n{beat_lines}\n"
        "Motion rules: weight transfers before each jump, knees bend on "
        "landing to absorb impact, hands plant flat and fingers stay "
        "together, feet point on extension and flex on landing, balance "
        "is recovered with arms, never with a teleport or a cut.\n"
        f"[CAMERA] {camera}. Athletic framing only, full body for skills, "
        "face only for a reaction, no sexualized angle.\n"
        f"[STYLE AND LIGHT] {style}\n"
        f"[LOOP] {loop}\n"
        "[CONTINUITY] Same hair, glasses, nose ring side, earrings, "
        "freckles, and outfit in every frame. No morphing between beats."
    )
    short = (
        f"{lock}. {scene}. "
        + " ".join(str(beat.get("action", "")) for beat in beats)
        + f" Camera: {camera}. Style: {style}."
    )
    variants = {
        "A_safe": full + "\n[VARIANT] Safe version: one continuous take, no slow motion.",
        "B_bold_camera": full + "\n[VARIANT] Bold version: low tracking shot on the "
        "run-up, then eye-level full body for the flip and landing.",
        "C_slow_detail": full + "\n[VARIANT] Detail version: slow motion on the "
        "flip apex and the landing absorption only, normal speed elsewhere.",
    }
    checklist = [
        "Hair, bun, glasses, nose ring side, earrings, freckles unchanged",
        "Outfit colour and style unchanged",
        "Hands and feet anatomically correct in every beat",
        "Landing absorbs with bent knees, no floating or snapping",
        "Camera stays athletic, full body for skills",
        "AI disclosure marked in the publish checklist",
    ]
    negative = list(NEGATIVE)
    for extra in data.get("negative_extra", []):
        negative.append(str(extra))
    return {
        "full_prompt": full,
        "short_prompt": short,
        "negative_prompt": ", ".join(negative),
        "continuity_checklist": checklist,
        "variants": variants,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("brief")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    with open(args.brief, encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict) or not data.get("character"):
        print("prompt_builder.py: brief needs a character object", file=sys.stderr)
        return 2
    result = build(data)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("FULL PROMPT")
        print(result["full_prompt"])
        print("\nNEGATIVE PROMPT")
        print(result["negative_prompt"])
        print("\nSHORT PROMPT")
        print(result["short_prompt"])
        print("\nCONTINUITY CHECKLIST")
        for item in result["continuity_checklist"]:
            print(f"- {item}")
        print("\nVARIANTS: A_safe, B_bold_camera, C_slow_detail")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
