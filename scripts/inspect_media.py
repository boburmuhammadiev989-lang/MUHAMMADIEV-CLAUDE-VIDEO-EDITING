#!/usr/bin/env python3
"""Inspect video/audio files with ffprobe and print a readable inventory.

Usage:
  python scripts/inspect_media.py path/to/video.mp4
  python scripts/inspect_media.py path/to/media_folder --recursive --json inventory.json

Requires ffprobe (normally installed alongside FFmpeg) on PATH.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v", ".mpg", ".mpeg", ".mxf"}
AUDIO_EXTS = {".wav", ".mp3", ".aac", ".m4a", ".flac", ".ogg", ".aiff", ".aif"}


def run_probe(path: Path, ffprobe: str) -> dict[str, Any]:
    command = [
        ffprobe, "-v", "error", "-show_entries",
        "format=duration,format_name,size,bit_rate:stream=codec_type,codec_name,width,height,avg_frame_rate,r_frame_rate,sample_rate,channels,channel_layout",
        "-of", "json", str(path),
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        message = result.stderr.strip() or f"ffprobe exited with status {result.returncode}"
        raise RuntimeError(message)
    data = json.loads(result.stdout or "{}")
    fmt = data.get("format", {})
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), {})
    audio = next((s for s in streams if s.get("codec_type") == "audio"), {})
    return {
        "path": str(path.resolve()),
        "file_name": path.name,
        "file_size_bytes": path.stat().st_size,
        "duration_seconds": float(fmt["duration"]) if fmt.get("duration") else None,
        "container": fmt.get("format_name"),
        "video_codec": video.get("codec_name"),
        "width": video.get("width"),
        "height": video.get("height"),
        "average_frame_rate": video.get("avg_frame_rate"),
        "audio_codec": audio.get("codec_name"),
        "sample_rate": audio.get("sample_rate"),
        "channels": audio.get("channels"),
        "channel_layout": audio.get("channel_layout"),
        "bit_rate": fmt.get("bit_rate"),
    }


def collect_files(inputs: list[Path], recursive: bool) -> list[Path]:
    found: list[Path] = []
    for item in inputs:
        if not item.exists():
            print(f"WARNING: not found: {item}", file=sys.stderr)
            continue
        if item.is_file():
            found.append(item)
        elif item.is_dir():
            iterator = item.rglob("*") if recursive else item.glob("*")
            found.extend(p for p in iterator if p.is_file() and p.suffix.lower() in VIDEO_EXTS | AUDIO_EXTS)
    # Deduplicate while preserving order.
    return list(dict.fromkeys(p.resolve() for p in found))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Media files or folders")
    parser.add_argument("--recursive", action="store_true", help="Search folders recursively")
    parser.add_argument("--json", dest="json_path", type=Path, help="Also write the inventory to this JSON file")
    args = parser.parse_args()

    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        print("ERROR: ffprobe was not found on PATH. Install FFmpeg and ensure ffprobe is available.", file=sys.stderr)
        return 2

    files = collect_files(args.paths, args.recursive)
    if not files:
        print("No media files found.")
        return 1

    records: list[dict[str, Any]] = []
    failures = 0
    for path in files:
        try:
            record = run_probe(path, ffprobe)
            records.append(record)
            dims = f'{record["width"]}x{record["height"]}' if record["width"] else "audio-only"
            duration = f'{record["duration_seconds"]:.2f}s' if record["duration_seconds"] is not None else "unknown duration"
            print(f'OK  {path.name} | {duration} | {dims} | video={record["video_codec"] or "-"} | audio={record["audio_codec"] or "-"}')
        except (RuntimeError, json.JSONDecodeError, OSError, ValueError) as exc:
            failures += 1
            print(f"FAIL {path}: {exc}", file=sys.stderr)

    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"\nInventory written to: {args.json_path}")

    print(f"\nInspected {len(records)} file(s); {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
