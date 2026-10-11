# Skill sources

Skills in this folder were copied from the original repositories below at the listed commits.
Upstream licenses are in `_licenses/`. No scripts were run during install and no API keys are configured.

| Source | Commit | Skills | Notes |
|---|---|---|---|
| https://github.com/Jakeschincariol/instagram-agent-skill | d03c56bb598be770c60b201f94237e5d1a4268a6 | `ig-*` (13) | |
| https://github.com/Jakeschincariol/youtube-agent-skill | a2feb2104981a375ffd4f87ee04f4f5344ac43c6 | `yt-*` (11) | |
| https://github.com/Jakeschincariol/linkedin-agent-skill | add2c23882fe79180737d242ff80a5da205eda6a | `li-*` (11) | |
| https://github.com/sergebulaev/facebook-skills | b78a2984f16906018ecbb203bcbf46d09fae4905 | `fb-*` (7) | Excluded `fb-audience-insights` and `lib/` (network clients that read API keys). Skills run in draft-only mode. Their text references (`references/*.md`) are in `.claude/references/`. |
| https://github.com/social-media-skills/skills | 6e30eeb2f6736bda8683b6bbaa674af3641d7945 | `pinterest-seo` | Only this skill. |
| https://github.com/sickn33/antigravity-awesome-skills | b9cd01cc4620796a17c9c16610ab946417f068ed | content-creator, content-marketer, content-strategy, copywriting, copywriting-psychologist, linkedin-content-generator, linkedin-post-writer, linkedin-profile-optimizer, social-content, social-orchestrator, social-post-writer-seo, social-proof-architect, xiaohongshu-content-strategist, youtube-seo-optimizer | 14 selected skills only. |

Not installed: https://github.com/garrytan/gstack (imports browser cookies, asks for database passwords, runs network update checks).

Removed: https://github.com/rebelytics/one-skill-to-rule-them-all (task-observer) — it runs at the start of every session and writes observation files to the workspace.
