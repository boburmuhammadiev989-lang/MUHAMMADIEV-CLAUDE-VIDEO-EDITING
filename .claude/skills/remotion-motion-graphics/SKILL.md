---
name: remotion-motion-graphics
description: Build polished code-driven videos and motion graphics with Remotion, React and TypeScript, then render and verify them.
---

# Remotion Motion Graphics Builder

Use Remotion when the video benefits from repeatable, code-driven scenes: animated explainers, title cards, branded intros/outros, charts, UI demonstrations, kinetic typography, lower thirds and social templates.

## Decide whether Remotion fits
Use it for precise, deterministic graphics and compositions. Prefer FFmpeg for straightforward trims, joins, transcodes and media filters. Do not create a React project for a task that needs only a two-second cut.

## Project setup
1. Inspect the existing project and reuse its framework if appropriate.
2. Check Node.js and package manager versions.
3. Check whether Remotion is installed and review the current project structure.
4. Use current official Remotion documentation for API details.
5. Before commercial use, review Remotion's current license and pricing terms. Do not assume all use is free.

## Composition design
Define:
- Composition ID
- Width, height, fps and durationInFrames
- Scene sequence and frame timing
- Typography, colour tokens, spacing and visual hierarchy
- Asset paths, fonts and audio
- Responsive safe areas for target platform
- Motion curves, easing, anticipation and settling
- Reduced-motion or legibility considerations where appropriate

Build reusable components for repeated elements. Use real font files only when the user has rights to them. Avoid excessive transitions and decorative movement that competes with the message.

## Animation craft
- Animate with clear purpose: reveal, emphasize, compare, guide attention or transition.
- Keep text readable long enough to understand.
- Use consistent easing, timing and alignment.
- Avoid rapid flashing, strobing, tiny text and excessive visual clutter.
- For charts, label axes, units, sources and relevant time periods. Never create misleading scales.
- For UI demos, use accurate user-supplied screenshots or clearly labelled illustrative mockups.

## Implementation and render
- Write complete, type-safe TSX/TypeScript files with clear names.
- Keep all media inside the project or use verified asset paths.
- Handle audio timing, fades and frame alignment.
- Render with the current documented Remotion CLI/API; verify command syntax against the installed version.
- Do not rely on undocumented APIs or hardcoded machine-specific paths.
- If a render fails, inspect the error and fix the underlying issue rather than hiding it.

## Verification
Check the rendered file with ffprobe and inspect representative frames. Confirm composition duration, dimensions, fps, no missing assets, text clipping, font fallback, timing drift or broken audio. Do not report a successful render until the output file is confirmed.
