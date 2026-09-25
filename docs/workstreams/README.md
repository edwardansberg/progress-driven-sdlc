# Workstream Scaffold and Archive

`docs/progress-agent.md` holds the one authoritative active substantial workstream; `docs/progress.md` is its short, source-identified human view. This directory contains the sole reusable scaffold and final snapshots of closed work.

The lifecycle policy is canonical in [Documentation Workflow](../README.md). This file defines only initialization and archive conventions unique to this directory. Application history stays here; upstream framework-maintenance evidence follows the separate [template packaging procedure](../ops/maintain-template.md) and does not ship as dated starter archives.

## Starting a Workstream

1. Inspect the actual repository and active state. Resume a compatible workstream in place; preserve unrelated dirty files. Do not overwrite an unresolved unrelated workstream without the user's explicit disposition.
2. When initialization is appropriate, use [WORKSTREAM_TEMPLATE.md](WORKSTREAM_TEMPLATE.md) in `docs/progress-agent.md`, then derive the human summary in `docs/progress.md`. Replace prompts with investigated state and remove setup comments.
3. Use as many phases as the work needs. Keep authoritative status, gate, and next action/owner only in detailed metadata; refresh their derived human summary after changes; record implementation authorization once with revision/scope and available actor/decision/date reference.
4. Follow canonical [work classes](../README.md#work-classes) and [approval scope](../README.md#approval-scope). Standard/high-risk plans normally stop at `Awaiting plan approval`; explicit scoped direct execution proceeds after investigation and a written plan with the user's authorization recorded.

The scaffold is the only repeatedly instantiated workflow template. Context, roadmap, and debt are singleton documents. The canonical detail plus human summary are the only active views; do not create independent role/handoff registers. For adoption into another repository, use [safe adoption guidance](../ops/adopt-framework.md); upstream maintenance state is not application state.

### Migrating an existing active record

Under approved migration scope, inspect both destinations and preserve the old record’s identity, scope, approvals, pending gates, evidence, and source revision. Move its authoritative content from progress.md to progress-agent.md before replacing progress.md with the derived summary. Do not initialize over an occupied or incompatible destination; resolve the collision first. Summarize older unique evidence only with retrievable pinned references. Migration is neither acceptance nor closure.

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

### Preserve references at closure

1. Choose an unused archive path; do not overwrite an existing archive. Before producing the first archived copy, identify the intended targets of relative links and images, including reference-style destinations and fragments. Rebase them for the destination directory or use an appropriate stable reference. Do not blindly rewrite code examples or repository-relative path labels.
2. Preserve workstream identity, terminal outcome, approvals, and evidence. Prefer revision-pinned references when mutable source content serves as historical proof; an ordinary navigational link is not automatically such evidence. Self-links to the closing workstream follow its archived copy.
3. Validate links and fragments from the archive location, not only from the active detailed record. For example, `README.md#approval-scope` in `docs/progress-agent.md` must become `../../../README.md#approval-scope` in `docs/workstreams/archive/2026/example.md` to retain the canonical-policy target.
4. Before reusing either active view, update maintained references intended to identify the just-closed workstream (such as resolved-debt or delivered-roadmap evidence) to its stable archived location. Leave general human navigation at `docs/progress.md` and current detailed-record navigation at `docs/progress-agent.md`. Preserve any unique evidence accidentally left only in the summary before replacing it; do not create a second authoritative archive.

Then set `docs/progress-agent.md` to `No active workstream` or initialize the next requested effort under its actual authorization, and refresh `docs/progress.md` from it. Pending user validation is not closure. These steps preserve the first archive copy and its references; do not rewrite older archives to fit a new scaffold.
