#!/usr/bin/env python3
"""Validate a JSON edit decision list (EDL) before assembling it.

Usage:
  python scripts/validate_edl.py project/edit.json
  python scripts/validate_edl.py project/edit.json --probe

Paths in the EDL's assets map are resolved relative to the EDL file.
With --probe, ffprobe is used to confirm that segment end-times fit source media.
This validates structure and ranges; it does not render the video.
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def media_duration(path: Path, ffprobe: str) -> float:
    cmd = [ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "ffprobe failed")
    return float(result.stdout.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("edl", type=Path, help="Path to EDL JSON file")
    parser.add_argument("--probe", action="store_true", help="Probe source durations with ffprobe")
    args = parser.parse_args()

    try:
        edl_path = args.edl.resolve()
        data = json.loads(edl_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read EDL: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        print("ERROR: EDL root must be a JSON object.", file=sys.stderr)
        return 2

    output = data.get("output")
    if not isinstance(output, dict):
        errors.append("'output' must be an object.")
    else:
        for field in ("width", "height", "fps"):
            value = output.get(field)
            if not is_number(value) or value <= 0:
                errors.append(f"'output.{field}' must be a positive number.")

    assets = data.get("assets")
    if not isinstance(assets, dict) or not assets:
        errors.append("'assets' must be a non-empty object mapping asset IDs to file paths.")
        assets = {}

    resolved_assets: dict[str, Path] = {}
    for asset_id, asset_path in assets.items():
        if not isinstance(asset_id, str) or not asset_id.strip():
            errors.append("Every asset ID must be a non-empty string.")
            continue
        if not isinstance(asset_path, str) or not asset_path.strip():
            errors.append(f"Asset '{asset_id}' must have a non-empty path.")
            continue
        path = (edl_path.parent / asset_path).resolve()
        resolved_assets[asset_id] = path
        if not path.is_file():
            errors.append(f"Asset '{asset_id}' does not exist: {path}")

    segments = data.get("segments")
    if not isinstance(segments, list) or not segments:
        errors.append("'segments' must be a non-empty array.")
        segments = []

    durations: dict[str, float] = {}
    ffprobe = shutil.which("ffprobe") if args.probe else None
    if args.probe and not ffprobe:
        errors.append("--probe was requested, but ffprobe is not on PATH.")

    previous_end = 0.0
    for index, segment in enumerate(segments, start=1):
        prefix = f"segments[{index}]"
        if not isinstance(segment, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        source = segment.get("source")
        if source not in resolved_assets:
            errors.append(f"{prefix}.source must reference an existing asset ID.")
            continue
        start, end = segment.get("start"), segment.get("end")
        timeline_start = segment.get("timeline_start", previous_end)
        if not is_number(start) or start < 0:
            errors.append(f"{prefix}.start must be a non-negative number.")
            continue
        if not is_number(end) or end <= start:
            errors.append(f"{prefix}.end must be greater than start.")
            continue
        if not is_number(timeline_start) or timeline_start < 0:
            errors.append(f"{prefix}.timeline_start must be a non-negative number.")
            continue
        duration = end - start
        timeline_end = timeline_start + duration
        if timeline_start < previous_end - 1e-6:
            warnings.append(f"{prefix} overlaps the previous segment on the timeline.")
        previous_end = max(previous_end, timeline_end)

        if args.probe and source in resolved_assets and resolved_assets[source].is_file():
            try:
                if source not in durations:
                    durations[source] = media_duration(resolved_assets[source], ffprobe)  # type: ignore[arg-type]
                if end > durations[source] + 0.05:
                    errors.append(f"{prefix}.end ({end:.3f}s) exceeds source duration ({durations[source]:.3f}s).")
            except (RuntimeError, ValueError, OSError) as exc:
                errors.append(f"Could not probe asset '{source}': {exc}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"\nEDL INVALID: {len(errors)} error(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1
    print(f"EDL VALID: {len(segments)} segment(s), {len(resolved_assets)} asset(s), {len(warnings)} warning(s).")
    print("Note: validation does not render or visually inspect the edit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
