# Documentation Workflow

This directory is the maintained project memory. It records current intent, durable system knowledge, operational procedures, product direction, and accepted deferred engineering work without mirroring an agent's internal reasoning or role structure.

## Start Here

For every substantial development task, read:

1. this file;
2. [progress.md](progress.md), the current workstream;
3. [context.md](context.md), the durable product and runtime model;
4. [roadmap.md](roadmap.md), the product direction;
5. [techdebt.md](techdebt.md), accepted engineering work intentionally deferred;
6. the relevant code, configuration, tests, migrations, Git history, runbooks, and runtime evidence.

Documentation helps locate the truth; it does not override evidence. When prose conflicts with executable or observed evidence, verify the system and correct or flag the stale document in the active workstream.

## Document Map

- `docs/progress.md`: The one active workstream, including outcome, evidence, approved plan, execution, verification, user validation, and delivery state. Update it at every material transition or discovery.
- `docs/context.md`: Verified durable product, architecture, runtime, persistence, security, trust-boundary, and delivery context.
- `docs/roadmap.md`: Confirmed direction and proposed Current/Next/Later outcomes. Roadmap placement is not implementation approval.
- `docs/techdebt.md`: Verified engineering recommendations accepted by the user but intentionally postponed. Debt placement is not implementation approval.
- `docs/ops/`: Reusable deployment, recovery, maintenance, and incident procedures.
- `docs/security/`: Maintained security boundaries, inventories, threat assumptions, and procedures.
- `docs/workstreams/`: The reusable workstream scaffold and archived snapshots of closed work.
- `docs/old/`: Historical reference only. Never treat it as current implementation guidance.

Raw production logs, secrets, copied terminal transcripts, personal machine details, and sensitive payloads do not belong in maintained documentation. Verification evidence should be concise and sanitized.

## Evidence Labels

Use explicit labels when a distinction matters:

- `Verified current behavior`: Confirmed in code, configuration, tests, migrations, Git history, or runtime evidence.
- `Chosen target behavior`: A product or architecture direction explicitly selected for this workstream.
- `Inference requiring validation`: A plausible conclusion that still needs a focused check or measurement.
- `Open decision`: A choice that must be resolved at a named gate.

Do not present a plan, assumption, old document, or passing build as proof of deployed behavior.

## Work Classes

### Quick change

A direct implementation path is acceptable only when the change is unambiguous, low-risk, reversible, and isolated. It must not affect schemas or live data, authentication or security, billing, infrastructure or deployment, secrets or configuration contracts, destructive operations, or external APIs.

The user's direct request authorizes a quick change unless they ask for a plan first. Inspect the relevant surface, verify the result, and record a concise update when the change belongs to an active workstream.

### Standard workstream

This is the default for features, non-trivial defects, cross-area refactors, and meaningful behavior changes:

1. Investigate the current system.
2. Write or refresh `docs/progress.md` with evidence, scope, acceptance criteria, risks, decisions, and an implementation and verification plan.
3. Set the status to `Awaiting plan approval` and wait.
4. After explicit approval, implement only the approved scope.
5. Keep the workstream current and set it to `Ready for user validation` after proportionate automated verification.
6. The user smoke-tests and either requests fixes or accepts the work.
7. Commit, push or pull request, preview deployment, migration, destructive cleanup, and production promotion remain separate explicit gates.

### High-risk workstream

Schema or live-data changes, authentication or security, billing, infrastructure, destructive operations, production behavior, and broad architecture changes follow the standard flow with mandatory migration, rollback, observability, and release-validation detail.

Create a separate specification, architecture decision record, or runbook only when a durable contract must outlive the workstream or the active document would become genuinely unreadable.

## Workstream Statuses and Gates

Normal flow:

`Planning -> Awaiting plan approval -> Implementing -> Ready for user validation -> Awaiting release approval -> Released -> Archived`

Exception states:

- `Blocked`: Progress cannot continue without user input or an external change.
- `Cancelled`: Work was intentionally stopped without delivery.
- `Rejected`: The evaluated change was declined.
- `Superseded`: A newer approach replaced this workstream.

Rules:

- Plan approval covers only the written scope and acceptance criteria.
- Minor implementation discoveries may be recorded and handled without stopping.
- Renewed approval is required for material changes to user-visible behavior, data handling, security, infrastructure, external contracts, cost, destructive effects, or scope.
- Approval to implement does not imply approval to commit, push, open or merge a pull request, deploy, migrate live data, or promote to production.
- Never mark user-owned smoke checks complete without the user's evidence or confirmation.
- Record a failed or skipped check honestly with its reason.
- Mark work `Released` only after the exact target commit and environment are verified.

## Keeping `progress.md` Fresh

Update the active workstream:

- after initial investigation and plan publication;
- after approval or a material user decision;
- before implementation begins;
- after a phase completes or the approved plan materially changes;
- after verification completes;
- after user smoke-test feedback;
- after each delivery gate and at archive time.

It is not a command transcript. Entries capture decisions, meaningful progress, evidence, deviations, and the next owner or action.

At minimum, the active workstream contains:

- outcome and definition of done;
- evidence, constraints, assumptions, and relevant system map;
- included and excluded scope;
- acceptance criteria;
- phased implementation and verification plan;
- risks, material decisions, migration needs, rollout, and rollback where applicable;
- verification results marked Passed, Failed, Skipped, or Pending;
- user-owned smoke-test checklist;
- delivery status, commit or environment references, and remaining work.

Use [WORKSTREAM_TEMPLATE.md](workstreams/WORKSTREAM_TEMPLATE.md) when starting substantial work.

## Internal Review and Delegation

Internal specialist agents may help with plan criticism, repository audits, testing, or review when useful. The primary agent remains accountable for reconciling their findings.

Do not create permanent role-owned handoff files by default. Consolidate material conclusions, decisions, test evidence, and unresolved risks into `docs/progress.md`.

## Durable Documentation Rules

- Store each reusable procedure once and link to it elsewhere.
- Update durable docs in the same workstream as the behavior they describe.
- Keep project-specific commands in runbooks, not scattered through active plans.
- Do not create Markdown tables. Prefer headings, short paragraphs, numbered procedures, bullets, and compact `Label: value` metadata.
- Never copy secrets, keys, tokens, credential values, sensitive payloads, or raw production logs into maintained docs.
- Prefer placeholders over personal paths, hostnames, IP addresses, and key names.
- Do not cite `docs/old/` as current truth.
- Roadmap entries are directional and do not authorize implementation.
- Technical-debt entries record accepted deferred recommendations and do not authorize implementation. Promote a selected item into `docs/progress.md` and apply the normal work-class gate.
- Do not call work released until the relevant environment and deployed commit are confirmed.

## Closing and Archiving a Workstream

When work is released, completed without deployment, rejected, cancelled, or superseded:

1. Record the final outcome, verification, commit and environment references, rollback state, and unresolved follow-ups.
2. Promote desired product outcomes to `docs/roadmap.md` and accepted-but-postponed engineering improvements to `docs/techdebt.md`.
3. Archive the final workstream using [workstreams/README.md](workstreams/README.md).
4. Reset `docs/progress.md` to `No active workstream` or initialize the next approved effort.
5. Refresh roadmap state and recently delivered or parked entries when applicable.
