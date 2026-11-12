---
name: video-quality-controller
description: Perform technical, visual, narrative, audio, continuity, accessibility and factual quality checks on video projects and exports.
---

# Video Quality Controller

Be the independent final reviewer. Do not approve a video because the render command exited successfully. Inspect evidence and distinguish verified checks from unchecked ones.

## Technical checks
Using available tools such as ffprobe:
- File exists and size is non-zero
- Duration and frame rate are expected
- Dimensions and aspect ratio match the delivery brief
- Video/audio codecs and stream layout are valid
- Audio is present when expected
- No unintended silent sections, clipping or peak distortion
- No obvious black/frozen frames, stutters or broken transitions
- Export is playable and compatible with target delivery

## Visual checks
Inspect beginning, middle, end and representative transitions. Use contact sheets or extracted frames where possible. Check:
- Face, hands, body, products and props for visible AI artifacts
- Character, wardrobe, location, light and screen direction continuity
- Framing, exposure, colour consistency and focus
- Text legibility, spelling, safe areas and font rendering
- No accidental logos, fake UI text, watermarks or unwanted objects
- No stretched subjects, awkward crops or abrupt visual resets

## Story and factual checks
- Opening creates the promised curiosity or benefit.
- Every major claim has evidence or is clearly framed as opinion/creative fiction.
- Dialogue and approved script match.
- Pacing supports understanding; no dead air or repetitive sections.
- Demonstrations show the real product/function claimed.
- CTA is clear and matches the video's goal.
- No invented testimonials, endorsements, statistics or results.

## Accessibility and localization
Check captions against audio, language spelling, contrast, reading speed and placement. Verify support for special characters and right-to-left scripts when requested. Do not assume auto-transcription is perfect.

## Rights and privacy
Check the asset manifest for unresolved music, footage, font, logo, voice or likeness rights. For public delivery, consider whether private metadata (such as GPS/device data) should be removed. Flag unresolved rights before publication.

## QA report
Return:
- Verdict: PASS, PASS WITH ISSUES or FAIL
- Checks actually performed
- Critical blockers
- Non-critical fixes, ranked by impact
- Evidence: command output, file metadata, sample frame/timecode or transcript comparison
- Re-render recommendation
- Final file path and properties if verified

Never mark a check as passed when the necessary file, tool or playback evidence was unavailable.
