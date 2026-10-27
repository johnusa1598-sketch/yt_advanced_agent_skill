#!/usr/bin/env python3
"""prompt_builder.py - build a next-level AI video prompt from a brief.

Usage:
    python3 prompt_builder.py brief.json
    python3 prompt_builder.py brief.json --json
    python3 prompt_builder.py brief.json --outfit "teal leotard"

The --outfit flag overrides the brief's outfit for one planned
rotation slot (v3.3.3). Outfit colour rotates across videos
per the plan in SKILL.md; it never changes mid-shot.
A leotard outfit must use one of the five rotation colours
(purple, teal, black, royal blue, burgundy); any other leotard
colour is rejected with exit 2 (v3.3.6). Non-leotard outfits
from the channel matrix are accepted as-is and must be logged
in the series log like a rotation slot.
When a brief carries a nose_ring field, the character lock
always uses the full v3.3.5 canonical wording for that field,
whatever the brief said, so a stale brief cannot weaken the
most-weighted layer (v3.3.6).

Input JSON example:
    {"character": {"name": "Aria", "hair": "curly dark hair in a big messy bun",
                   "glasses": "thin GOLD wire-frame glasses",
                   "nose_ring": "SMALL gold nose ring on the character's RIGHT nostril wing only (in a frontal view, on the image's LEFT side), never septum, never centre, never nose tip, never two rings",
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

Output: a full 7-layer prompt plus a mandatory format lock
(vertical 9:16, shot on iPhone), a short prompt for quick tools, a
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
    "glasses changing shape, nose ring changing side, septum ring, centre nose ring, nose ring on nose tip, two nose rings",
    "outfit changing colour or style mid-shot, jewellery disappearing",
    "sexualized framing, sexualized poses, close-ups on body parts",
    "warped beam, floating props, no watermark, no logo",
    "horizontal 16:9 video, landscape framing, letterbox bars, pillarbox bars, cropped horizontal footage, cinematic DSLR or anamorphic look",
    "no burned-in subtitles or text except the intended text layers, no text errors",
    "glossy plastic skin, cartoon look, sudden age or identity change",
]


ROTATION_COLOURS = ("purple", "teal", "black", "royal blue", "burgundy")

# v3.3.5 canonical wording. A brief that mentions a nose ring gets
# this sentence in the character lock, verbatim, even if the brief
# itself used shorter or older wording (e.g. "RIGHT nostril only"
# without the wing/centre/tip/two-rings language). A character with
# no nose_ring field is left alone: no ring is invented for them.
NOSE_CANONICAL = (
    "SMALL gold nose ring on the character's RIGHT nostril wing only "
    "(in a frontal view, on the image's LEFT side), never septum, "
    "never centre, never nose tip, never two rings"
)

# Realism core (v3.3.6): the SKILL requires every prompt to carry
# these physical details, not just the brief's style string.
REALISM_CORE = (
    "Realism: visible skin pores and fine flyaway hairs, chalk dust "
    "on hands and mat, a natural blink between beats, micro-tremor "
    "on held balances, sweat building across the video, no plastic "
    "skin, no frozen hair, no floaty weightless motion. At the peak "
    "beat, effort is SUSTAINED, never released: limbs locked with no "
    "sag across the beat, jaw set, eyes locked per the eye rule, "
    "breath controlled — a neutral face, sagging limbs, or eyes "
    "squeezed shut at the peak is a failed peak."
)


def character_block(character):
    parts = []
    for key in ("name", "hair", "glasses", "nose_ring", "earrings", "freckles", "outfit"):
        value = character.get(key)
        if value:
            if key == "nose_ring" and "nose ring" in str(value).lower():
                value = NOSE_CANONICAL
            parts.append(str(value))
    return "; ".join(parts)


def check_leotard_colour(outfit):
    """Return an error string unless a leotard outfit uses a rotation colour."""
    text = str(outfit).lower()
    if "leotard" not in text:
        return None
    if any(colour in text for colour in ROTATION_COLOURS):
        return None
    return (f"outfit {outfit!r} is not a rotation colour. "
            f"Leotard slots use only: {', '.join(ROTATION_COLOURS)}. "
            "Pick a planned slot or use a non-leotard matrix outfit.")


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
        "[FORMAT LOCK] Vertical 9:16 portrait, 1080x1920 preferred "
        "(720x1280 at the same ratio is acceptable, do not upscale), full frame. "
        "Shot on iPhone: handheld smartphone look, natural phone-camera "
        "optics, slight handheld movement, no cinematic DSLR look. "
        "Never horizontal, never letterboxed, never pillarboxed, "
        "never cropped from horizontal footage.\n"
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
        f"[REALISM] {REALISM_CORE}\n"
        f"[LOOP] {loop}\n"
        "[CONTINUITY] Same hair, glasses, nose ring on the character's "
        "RIGHT nostril wing only, earrings, "
        "freckles, and outfit in every frame. No morphing between beats."
    )
    short = (
        f"{lock}. Vertical 9:16 portrait, shot on iPhone. {scene}. "
        + " ".join(str(beat.get("action", "")) for beat in beats)
        + f" Camera: {camera}. Style: {style}."
    )
    variants = {
        "A_safe": full + "\n[VARIANT] Safe version: one continuous take, no slow motion.",
        "B_bold_camera": full + "\n[VARIANT] Bold version: low tracking shot on the "
        "run-up, then eye-level full body for the flip and landing.",
        # v3.3.6: NOT a slow-motion effect. The FINAL template bans slow
        # motion; this variant is slow, controlled movement at normal
        # speed. Do not use it where the template bans slow motion
        # unless the brief explicitly re-approves controlled movement.
        "C_slow_detail": full + "\n[VARIANT] Detail version: slow, controlled "
        "movement at the flip apex and the landing absorption, normal "
        "speed throughout, no slow-motion effect.",
    }
    checklist = [
        "Hair, bun, glasses, nose ring on character's RIGHT nostril wing only (frontal view: image LEFT), never centre/septum/tip, earrings, freckles unchanged",
        "Outfit colour and style unchanged",
        "Hands and feet anatomically correct in every beat",
        "Landing absorbs with bent knees, no floating or snapping",
        "Camera stays athletic, full body for skills",
        "Vertical 9:16, iPhone-shot look, no letterbox or cropped horizontal frame",
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
    parser.add_argument("--outfit", default=None,
                        help="Override the brief's outfit for one planned "
                             "rotation slot, e.g. 'teal leotard'")
    args = parser.parse_args()
    with open(args.brief, encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict) or not data.get("character"):
        print("prompt_builder.py: brief needs a character object", file=sys.stderr)
        return 2
    if args.outfit:
        error = check_leotard_colour(args.outfit)
        if error:
            print(f"prompt_builder.py: {error}", file=sys.stderr)
            return 2
        data["character"]["outfit"] = args.outfit
    outfit = data["character"].get("outfit", "")
    error = check_leotard_colour(outfit)
    if error:
        print(f"prompt_builder.py: {error}", file=sys.stderr)
        return 2
    if not args.outfit and str(outfit).lower() == "purple leotard":
        print("prompt_builder.py: warning: no --outfit given, using the "
              "default purple leotard. Check the series log so this "
              "video never repeats the previous slot.", file=sys.stderr)
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
        for name, text in result["variants"].items():
            print(f"\nVARIANT {name}")
            print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
