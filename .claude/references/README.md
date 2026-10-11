# Facebook skill references

These text files come from https://github.com/sergebulaev/facebook-skills at commit b78a2984f16906018ecbb203bcbf46d09fae4905.
The `fb-*` skills in `.claude/skills/` read them via `../../references/`.

When an `fb-*` skill says "see root `SKILL.md` Voice rules", use `voice-rules.md` in this folder.

`voice-profile.md` and `story-bank.md` are blank templates. Fill them through `fb-humanizer --mode profile` and `--mode interview`, and never put owner or guest personal data in them.

The upstream `lib/` (Publora, Apify, Pixfaro API clients) is intentionally not installed, so the skills only produce drafts. Nothing is published.
