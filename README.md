# ZUNA AI

A local, dependency-free holiday-home listing draft and approval desk, with an attributed social-content skill library.
**Early MVP:** deterministic templates, SQLite persistence and audit events. No LLM integration, publishing, messaging, booking sync, authentication or production deployment.

## Run in five minutes

Python 3.10+; clone this repository and run from its root. No API keys or dependencies required.

```sh
python -m zuna create examples/listing.json
python -m zuna show 1
python -m zuna approve 1
python -m zuna events 1
python -m unittest discover -s tests -v
```

Use `reject 1` instead of approval to reject a pending draft. Decisions are final for that draft; create a new draft to revise it. `--db /path/to/local.sqlite3` goes before the subcommand. The default local database is ignored by Git. Approval records a local decision and **does not publish**.

Input must contain exactly `building`, `area`, `bedrooms` (0–10), `nightly_aed` (finite, 1–100000), and unique `amenities` chosen from Wi-Fi, pool, gym, parking, kitchen, balcony. Building/area accept public place names without digits or contact syntax. These checks reduce accidental disclosure but are not a general personal-data detector: review inputs yourself. The example is synthetic, not a real offer. Availability, fees and regulatory suitability must be verified separately before any real listing is used.

## Safety and limitations

Single-user local tool. The database is plaintext and has no access control beyond your operating system; anyone who can edit it can alter approvals. Do not put sensitive records in it. No arbitrary plugins, shell execution, HTTP server or external side effects are included. Drafts present two wording choices based only on supplied facts.

## Development and contribution

Submit small changes with reproduction steps and tests for behavior. Use synthetic fixtures; do not inflate activity for benefits applications. See [SECURITY.md](SECURITY.md), [security audit](docs/SECURITY_AUDIT.md), and [application evidence](docs/CLAUDE_OSS_APPLICATION.md).

## License and attribution

Original project code is MIT (see LICENSE). Imported `.claude/skills` and reference material retain their upstream license and attribution: see [.claude/skills/SOURCES.md](.claude/skills/SOURCES.md) and `.claude/skills/_licenses`. A root license does not replace upstream conditions. Imported skills are not evidence of original code authorship or external adoption.
