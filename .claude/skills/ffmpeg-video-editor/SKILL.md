---
name: ffmpeg-video-editor
description: Inspect and edit real video/audio with FFmpeg: trim, assemble, resize, reframe, transcode, mix, subtitle, filter and export reliably.
---

# FFmpeg Video Editor

Use FFmpeg and ffprobe for deterministic video/audio operations. You are an editor and media engineer: inspect first, plan the edit, execute safely, and verify every output.

## Preflight
1. Inspect the project tree and identify source files, existing outputs and naming conventions.
2. Check tool availability with `ffmpeg -version` and `ffprobe -version`.
3. Probe source metadata: duration, video/audio streams, codecs, resolution, frame rate, pixel format, sample rate and channel layout.
4. Sample frames or create a contact sheet when possible. Listen to or inspect audio when tools permit.
5. Confirm source media is readable and not corrupted before editing.

Never guess file names. Quote paths correctly, including spaces and non-ASCII characters. Do not overwrite source media. Write outputs to a separate folder such as `output/` or `renders/`.

## Edit plan
For edits longer than a few simple operations, define an edit decision list (EDL):
- Source path
- In/out timecodes
- Segment order
- Crop/reframe
- Speed changes
- Transition
- Text/graphic overlay
- Audio source, gain and fade
- Output codec and target dimensions

Verify time ranges: start < end and end <= source duration. Preserve chronology unless the creative brief asks otherwise.

## Reliable workflows
- Use stream copy only when codecs, time bases and keyframe boundaries permit clean cuts/joins.
- Re-encode when source settings differ or filters/transitions are required.
- For concatenation, use the concat demuxer only with compatible streams; otherwise use a filter graph or normalize segments first.
- Use `scale` plus `pad` or deliberate crop for aspect-ratio changes. Never stretch people or products.
- Use `aresample`, `adelay`, `amix`, fades and loudness analysis deliberately; avoid clipping and accidental phase problems.
- Use subtitle filters with a known font and escaped paths. Verify glyph support for Uzbek apostrophes, Turkish characters, Cyrillic and Arabic when relevant.
- Keep frame rate consistent unless variable frame rate or interpolation is intentional.
- Use high-quality intermediate files for multi-stage work; compress once at final delivery when possible.

## Safety and reproducibility
- Prefer explicit commands with named input/output paths.
- Do not use broad destructive shell globs.
- Do not delete intermediates until the final output is verified and the user has the requested deliverables.
- Do not run downloaded scripts or binaries without inspecting their source and origin.
- Avoid overwriting by creating unique filenames; if an output already exists, choose another name or ask before replacement.
- Preserve metadata when it matters, but remove sensitive location/device metadata from public exports when appropriate and authorized.

## Verification
After every render:
1. Confirm output file exists and size is non-zero.
2. Run ffprobe on the output.
3. Confirm expected duration, dimensions, frame rate, codecs and stream count.
4. Check beginning, middle, end and transition frames.
5. Check for black/frozen frames, missing audio, clipped sound, subtitle overflow and bad crops.
6. Compare with the EDL and intended script.
7. Report exact path and technical properties.

Do not claim visual or audio quality has been checked if only metadata was checked. State which checks were actually performed.
