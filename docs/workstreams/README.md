# Workstream Archive

`docs/progress.md` is the only active standard or high-risk workstream by default. This directory contains the one reusable workstream scaffold and final snapshots of closed work.

The lifecycle policy is canonical in [Documentation Workflow](../README.md). This file defines only the scaffold and archive conventions unique to this directory.

## Starting a Workstream

1. Confirm there is no unresolved active workstream.
2. Copy `WORKSTREAM_TEMPLATE.md` over `docs/progress.md`.
3. Investigate and replace every prompt with evidence-backed content.
4. Classify the work and set its truthful initial status.
5. For standard or high-risk work, publish the plan and stop at `Awaiting plan approval`.

`WORKSTREAM_TEMPLATE.md` is the only repeatedly instantiated scaffold. Context, roadmap, and technical debt are singleton live documents and are not copied per workstream.

Do not create active workstream files in this directory preemptively.

## Archive Convention

Use:

```text
docs/workstreams/archive/YYYY/YYYY-MM-DD-<type>-<short-slug>.md
```

Types normally match conventional change intent: `feat`, `fix`, `docs`, `chore`, `refactor`, or `style`.

Examples:

```text
docs/workstreams/archive/2027/2027-02-11-docs-development-workflow.md
docs/workstreams/archive/2027/2027-03-04-feat-account-export.md
```

## Before Archiving

- Set a truthful terminal status: `Released`, `Rejected`, `Cancelled`, or `Superseded`.
- Record the final outcome and why the workstream closed.
- Record checks actually run and leave failed or skipped checks visible.
- Record relevant commit, pull request, preview, production, migration, and rollback references.
- Resolve follow-ups or promote them to `docs/roadmap.md` or `docs/techdebt.md`.
- Ensure no secrets, sensitive payloads, raw logs, or unnecessary terminal dumps are present.

After archiving, initialize `docs/progress.md` for the next workstream or set it to `No active workstream`.

## Concurrency

One active workstream is the default because it keeps authority obvious. If genuinely concurrent approved development becomes routine, revise the workflow deliberately so `docs/progress.md` becomes a dashboard linking to `docs/workstreams/active/<slug>.md`. Do not introduce parallel active documents ad hoc.
