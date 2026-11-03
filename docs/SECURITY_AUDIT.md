# Public repository security audit — 3 November 2026

## Scope and method

Baseline ZUNA head: `5fc8bdb`; full clone, all advertised branches and fetched pull-request heads 1 and 2, no tags. `git fsck --full` passed. There are 21 reachable commits (including merges), 148 unique file blobs. Gitleaks v8.30.1 scanned all refs with `gitleaks git . --log-opts=--all --redact`; its diff scan reports 19 non-merge commits and zero findings. A separate full-blob review scanned all 148 blobs, including deleted historical files, for credential formats/assignments, email addresses and privacy-related context. Current files were also scanned with `gitleaks dir . --redact` with zero findings.

OpenAgent baseline: `c9b1858`, 10 commits and 10 unique blobs. Gitleaks full history: zero findings. No credential pattern match was found by the supplemental scanner in either repository. An email-like match in a deleted upstream reference was a generic GitHub noreply example.

## Findings and remediation

- A broader numeric/contact scan found a business contact number in the brand-voice skill (two occurrences). Removed it from the current file. It remains in historical commits and possible copies. Treat its intended public status as unconfirmed; the maintainer should assess unwanted contact risk and whether history cleanup is warranted. Other long-number candidates were dates, numeric ranges and synthetic content metrics. No credential-bearing URL or local user path was found by that supplemental scan.

- ZUNA's old `CLAUDE.md` exposes business/operating context and two Claude artifact identifiers. These are not API credentials, but may identify internal planning artifacts. Replaced the current file with public contributor guidance. The old values still exist in Git history, PR refs, clones and possible caches. They have not been purged and artifact permissions have not been verified or revoked. The maintainer should inspect the sharing settings of those two original artifacts and disable sharing if they contain private information. No claim of complete privacy remediation is made.
- `story-bank.md` and `voice-profile.md` are empty upstream templates, not populated customer records. Renamed them to `.example.md` and ignored their working filenames so later personal edits are not automatically tracked.
- Added ignores for environment files, local databases and a private folder. Ignore rules do not protect files already tracked or secrets pasted elsewhere.
- Added an MIT license for original project code; upstream skill licenses and attribution are retained. Imported skills are not original-authorship or adoption evidence.

No live API keys, passwords, payment records, guest/owner contact lists or populated identity records were identified in the reviewed material. This is a bounded code/history review, not proof that no private data exists. Pattern matching cannot establish whether business context is confidential. No credential validity was tested, no third-party artifacts were opened, and no external service sharing settings were changed.

## Limits

The audit covers Git objects reachable from advertised/fetched refs, not deleted server-side objects, forks, downloaded clones, third-party caches, Actions artifacts, GitHub account secrets or external Claude artifact contents. Removing current content does not remove historical exposure. Revoke any subsequently discovered credential before planning a history rewrite. Do not force-push or purge history without a coordinated maintainer recovery plan.

## Reproduce

```sh
git fetch origin '+refs/heads/*:refs/remotes/origin/*'
git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'
git fsck --full
gitleaks git . --log-opts=--all --redact
gitleaks dir . --redact
```

Runtime MVP boundaries: local single-user plaintext SQLite, no authentication, no external publishing. Input validation is not a comprehensive PII filter; use synthetic inputs and review output.
