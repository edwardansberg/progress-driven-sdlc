# Workstream Scaffold and Archive

`docs/progress.md` holds the one active substantial workstream. This directory contains the sole reusable scaffold and final snapshots of closed work.

The lifecycle policy is canonical in [Documentation Workflow](../README.md). This file defines only initialization and archive conventions unique to this directory.

## Starting a Workstream

1. Inspect the actual repository and active state. Resume a compatible workstream in place; preserve unrelated dirty files. Do not overwrite an unresolved unrelated workstream without the user's explicit disposition.
2. When initialization is appropriate, use [WORKSTREAM_TEMPLATE.md](WORKSTREAM_TEMPLATE.md) in `docs/progress.md`. Replace prompts with investigated state and remove setup comments.
3. Use as many phases as the work needs. Keep current status, gate, and next action/owner only in the metadata; record implementation authorization once with revision/scope and available actor/decision/date reference.
4. Follow canonical [work classes](../README.md#work-classes) and [approval scope](../README.md#approval-scope). Standard/high-risk plans normally stop at `Awaiting plan approval`; explicit scoped direct execution proceeds after investigation and a written plan with the user's authorization recorded.

The scaffold is the only repeatedly instantiated workflow template. Context, roadmap, and debt are singleton documents. Do not create parallel active files or separate role/handoff registers. For adoption into another repository, use [safe adoption guidance](../../README.md#adopt-or-update-the-framework); upstream maintenance state is not application state.

## Archive Convention

Use:

```text
docs/workstreams/archive/YYYY/YYYY-MM-DD-<type>-<short-slug>.md
```

Use the closure date. Types normally match conventional change intent: `feat`, `fix`, `docs`, `chore`, `refactor`, or `style`.

Example:

```text
docs/workstreams/archive/2027/2027-02-11-docs-usage-guide.md
```

## Before Archiving

- Confirm a truthful [terminal outcome](../README.md#workstream-statuses-and-gates): `Completed`, `Released`, `Rejected`, `Cancelled`, or `Superseded`. Preserve that status in the archive; do not replace it with `Archived`.
- Record why the work closed, and user acceptance for successful work. `Completed` requires an agreed target needing no release; an intended but unverified release cannot use that outcome.
- Retain checks and evidence, including failed, skipped, or waived checks and their disposition. Include applicable commit, PR, environment, migration, and rollback references; justify non-applicability.
- Resolve follow-ups or place confirmed direction and accepted postponed debt according to the [closing policy](../README.md#closing-and-archiving-a-workstream).
- Sanitize secrets, sensitive payloads, raw logs, and unnecessary terminal dumps before preserving the snapshot. Do not rewrite earlier archived workstreams to fit a new scaffold.

After preserving the terminal workstream, set `docs/progress.md` to `No active workstream` or initialize the next requested effort under its actual authorization. Pending user validation is not closure.
