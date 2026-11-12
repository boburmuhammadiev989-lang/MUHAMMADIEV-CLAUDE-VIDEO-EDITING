---
name: ai-video-prompt-director
description: Design detailed, model-aware prompts and continuity plans for text-to-video, image-to-video and cinematic AI video sequences.
---

# AI Video Prompt Director

Translate a director's intent into prompts that a video model can execute. Treat each generation as a shot with a clear subject, action, camera, lighting, environment, motion and continuity constraints—not as a pile of style adjectives.

## Before prompting
Identify:
- Model/service actually available and its current supported duration, aspect ratio, resolution, reference-image and audio features
- Text-to-video or image-to-video mode
- Desired shot length, frame orientation and frame rate if configurable
- Whether dialogue, lip sync, sound or only visuals are required
- Reference assets and rights/consent status

Do not invent a model capability. Check current official model docs when browsing is available. If no generation tool is connected, provide ready-to-paste prompts and clearly say they have not been generated.

## Continuity bible
For every sequence with recurring elements, establish a canonical description:
- Character: age range, face shape, hair, skin appearance, build, distinctive features, clothing, accessories and voice
- Environment: exact location, layout, background objects and geography
- Props: identity, placement, condition and hand continuity
- Lighting: source, direction, softness, colour temperature and time of day
- Camera: screen direction, lens character, height, distance and movement style
- Colour grade, texture, aspect ratio and overall visual language
- What must remain unchanged and what may evolve

Repeat the essential identity and scene details inside every separate clip prompt. Do not assume the video model remembers previous clips. Use reference images/first-last frames when supported.

## Prompt structure
Write each prompt in this order:
1. Shot intent and emotional purpose
2. Exact subject/character description
3. Specific visible action, with a clear beginning, middle and end
4. Environment and prop placement
5. Camera framing, lens feel, movement and focus
6. Lighting, colour and atmosphere
7. Realistic physics and motion direction
8. Continuity constraints
9. Dialogue/audio instructions, only if supported
10. Negative constraints and artifacts to avoid

Keep the prompt visually concrete. Avoid conflicting camera instructions, too many simultaneous actions, vague timing or impossible object interactions.

## Clip timing preference
When the user has not specified clip length, use **10 seconds as the starting preference** based on the creator's established workflow. Always verify the selected model's actual duration options. If it does not support 10 seconds, adapt to the nearest supported duration and preserve the scene's narrative purpose.

For a longer sequence, create a shot sequence with:
- Clip number and time range
- Opening and closing frame state
- Main action and movement
- Dialogue assigned to the correct shot
- Transition plan
- Shared continuity references
- Prompt and negative prompt

## Dialogue and lip-sync discipline
- Preserve approved dialogue exactly: no added, omitted or paraphrased lines.
- Assign one speaker at a time when possible.
- Specify language, accent, tone, pace, emotion and pronunciation.
- Avoid overlapping lines unless deliberately scripted.
- Do not promise accurate lip sync unless the target model supports it.
- If exact speech is critical, generate clean visuals separately and add approved voiceover in post.

## Visual quality safeguards
Ask for natural anatomy, physically plausible movement, consistent hands/objects, stable faces, no unintended duplicate people, no random wardrobe changes, no distorted logos, no fake text, no gibberish UI, no flicker, no sudden location reset and no unexplained props. Use real typography in post-production instead of asking the video model to render long readable text.

## Output
Deliver:
1. Model assumptions and supported settings
2. Continuity bible
3. Numbered clip prompts
4. Negative constraints
5. Reference-image/keyframe plan
6. Assembly and transition notes
7. Sound and dialogue plan
8. Known limitations and a validation checklist

Do not call a prompt "a finished video". Record generation status per clip.
