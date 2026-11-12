# MUHAMMADIEV — Claude Video Production & Editing Skills

A practical, modular video-production system for Claude Code. It is designed to help turn a rough idea into a researched concept, compelling script, storyboard, AI-generation prompts, edited timeline, sound mix, captions, platform exports, and a quality-checked final video.

## The core promise

Tell Claude what video you have in mind. The **Video Production Director** should take ownership of the workflow, improve the idea where useful, choose the right specialist skills, and move as far as the available tools and permissions allow. It must never pretend that a render, upload, generation, or quality check happened when it did not.

## Main command

`/video-production-director`

Specialist skills:
- `/market-aware-video-strategist` — audience, positioning, concept selection, hooks and market fit.
- `/story-script-storyboard` — narrative structure, scripts, shot lists and storyboards.
- `/ai-video-prompt-director` — consistent, production-ready prompts for text/image-to-video systems.
- `/ffmpeg-video-editor` — inspect, cut, join, resize, process, mix and export footage.
- `/remotion-motion-graphics` — create animated explainers, titles, charts, interfaces and motion graphics with code.
- `/sound-voice-caption-designer` — voiceover, dialogue, music, sound effects, subtitles and audio polish.
- `/short-form-platform-adapter` — adapt one idea or master edit for Reels, TikTok, Shorts and other platforms.
- `/video-asset-designer` — plan and create visual assets, graphics, thumbnails and B-roll prompts.
- `/video-quality-controller` — technical, narrative, accessibility and continuity QA.

## Install in a project with Claude Code

1. Clone this repository:
   ```bash
   git clone https://github.com/boburmuhammadiev989-lang/MUHAMMADIEV-CLAUDE-VIDEO-EDITING.git
   ```
2. Open the cloned folder as your Claude Code project, or copy its `.claude/skills/` folder into an existing project.
3. In Claude Code, invoke `/video-production-director` or describe the video task naturally. Skills can also be selected automatically when their descriptions match.
4. Allow shell/file access only for actions you understand. Keep source footage unchanged; exports should go into a separate output folder.

## Capabilities depend on tools

Skills are instructions and reusable workflows; they do not install a renderer, generate footage by themselves, or grant access to paid services. For real editing/rendering, install or connect the required tools:

| Tool | What it enables | Official resource |
|---|---|---|
| FFmpeg + ffprobe | Video/audio inspection, cutting, filtering, encoding and muxing | https://ffmpeg.org/ |
| Node.js | Runtime used by Remotion projects | https://nodejs.org/ |
| Remotion | Programmatic video compositions and rendering | https://www.remotion.dev/docs |
| Whisper-compatible transcription | Speech transcription and subtitle source | https://github.com/openai/whisper |
| Image/video/voice generation services | New footage, stills, voiceovers and sound assets | Use only services actually connected and available to you |

Remotion's render workflow is documented at https://www.remotion.dev/docs/render. Check its current license and pricing terms before commercial use.

## Operating principles

- **Idea to finished export:** do not stop at a script when tools allow editing and rendering.
- **Market-aware, not hype-driven:** identify the audience, need, angle and evidence. Never promise virality or invent market data.
- **Research with sources:** verify current claims when browsing is available. Separate facts, estimates and creative assumptions.
- **Creative initiative:** propose stronger hooks, clearer storytelling, better visuals and alternative endings; explain meaningful changes.
- **Continuity:** maintain a continuity bible for recurring people, places, props, wardrobe, voice, lighting, camera geography and visual style.
- **Exact dialogue:** preserve approved wording and pronunciation. Do not add, remove or paraphrase dialogue during generation unless asked.
- **User preference:** when AI-video clips are requested and no duration is specified, use 10-second shots as the starting preference, then adapt to the selected model's actual limits.
- **Faceless-friendly:** do not assume the creator wants to appear on camera or record their own voice.
- **Truthful execution:** state which tools are available, what was actually run, what failed, and what remains.
- **Safe editing:** never overwrite source files or delete assets without permission. Avoid unlicensed music, fonts, footage, logos and impersonation.
- **Language:** answer in the user's language; default to Uzbek when the user writes in Uzbek.

## Example requests

- "I want a cinematic 60-second video about why people waste their time. Make the concept stronger and produce it."
- "Turn these raw clips into a fast 30-second Reel with Uzbek subtitles."
- "Create a faceless 8-minute YouTube explainer about how AI agents work."
- "Make a product launch video. Research the audience, write three concepts, choose the strongest, then edit."
- "Here is my script. Keep every spoken word exactly the same, but make the visuals more cinematic."

## Repository structure

`.claude/skills/<skill-name>/SKILL.md` contains each Claude Code skill. The skills are independent modules coordinated by the main Video Production Director.

This repository contains original workflow instructions. Tool names and external services remain the property of their respective owners; check each service's terms before use.
