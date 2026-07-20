# Documentation Workflow

This file is the canonical workflow contract for the repository. It defines how project memory is organized, how work is approved and verified, and when information moves between active state, durable context, directional planning, deferred debt, and history.

Do not duplicate this policy throughout the live state files. Those files should contain current project information plus a short authority reminder and a link back here.

## Start Here

For every substantial development task, read:

1. this file;
2. [progress.md](progress.md), the current workstream;
3. [context.md](context.md), the durable product and runtime model;
4. [roadmap.md](roadmap.md), the product direction;
5. [techdebt.md](techdebt.md), accepted engineering work intentionally deferred;
6. the relevant code, configuration, tests, migrations, Git history, runbooks, and runtime evidence.

Documentation helps locate the truth; it does not override evidence. When prose conflicts with executable or observed evidence, verify the system and correct or flag the stale document in the active workstream.

## Documentation Layers

### Policy

- `AGENTS.md` makes the cold-start, planning, upkeep, safety, and delivery rules discoverable to coding agents.
- `docs/README.md` is the single canonical human-readable workflow contract.
- Scoped archive, operations, and security indexes may define conventions unique to their directories, but they must not redefine the global lifecycle.

### Live state

- `docs/progress.md` records the one active standard or high-risk workstream, or truthfully states that none exists.
- `docs/context.md` records verified durable product and system facts.
- `docs/roadmap.md` records directional product outcomes.
- `docs/techdebt.md` records verified recommendations the user accepted and intentionally postponed.

Live state files do not repeat work classes, status definitions, approval rules, or complete entry instructions. Template-only HTML comments may guide first initialization; remove them after use. Comments are scaffolding, not project state.

### Reusable scaffold

`docs/workstreams/WORKSTREAM_TEMPLATE.md` is the only repeatedly instantiated workflow template. Copy it over `docs/progress.md` when substantial work begins.

The context, roadmap, and debt files are singleton registers initialized in place. Creating duplicate templates for them would add another source that could drift from the live file.

### History

`docs/workstreams/archive/` stores final snapshots of terminal workstreams. Historical material under `docs/old/` is non-authoritative and must be verified before reuse.

## Document Map

- `docs/progress.md`: Active outcome, evidence, approved plan, execution, verification, user validation, and delivery state.
- `docs/context.md`: Product purpose, repository map, architecture, runtime, persistence, trust boundaries, delivery model, and durable constraints.
- `docs/roadmap.md`: Confirmed Current, Next, Later, and Deferred product outcomes.
- `docs/techdebt.md`: Accepted but postponed engineering recommendations and their lifecycle state.
- `docs/ops/`: Reusable deployment, recovery, maintenance, and incident procedures.
- `docs/security/`: Maintained security boundaries, inventories, threat assumptions, and procedures.
- `docs/workstreams/`: The reusable workstream scaffold and archived closed work.
- `docs/old/`: Historical reference only.

Raw production logs, secrets, copied terminal transcripts, personal machine details, and sensitive payloads do not belong in maintained documentation. Verification evidence should be concise and sanitized.

## Evidence Labels

Use explicit labels when a distinction matters:

- `Verified current behavior`: Confirmed in code, configuration, tests, migrations, Git history, or runtime evidence.
- `Chosen target behavior`: Product or architecture direction explicitly selected for the active workstream.
- `Inference requiring validation`: A plausible conclusion that still needs a focused check or measurement.
- `Open decision`: A choice that must be resolved at a named gate.

Do not present a plan, assumption, historical document, local build, or roadmap entry as proof of deployed behavior.

## Work Classes

### Quick change

A direct implementation path is acceptable only when the change is unambiguous, low-risk, reversible, and isolated. It must not affect schemas or live data, authentication or security, billing, infrastructure or deployment, secrets or configuration contracts, destructive operations, or external APIs.

The user's direct request authorizes a quick change unless they ask for a plan first. Inspect the relevant surface, verify the result, and record a concise update when the change belongs to an active workstream.

### Standard workstream

This is the default for features, non-trivial defects, cross-area refactors, and meaningful behavior changes:

1. Investigate the current system.
2. Copy [WORKSTREAM_TEMPLATE.md](workstreams/WORKSTREAM_TEMPLATE.md) over `docs/progress.md` and replace its prompts with evidence, scope, acceptance criteria, risks, decisions, and an implementation and verification plan.
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
- Record failed or skipped checks honestly with their reasons.
- Mark work `Released` only after the exact target commit and environment are verified.

## Live Document Contracts

### `progress.md`

Update the active workstream:

- after initial investigation and plan publication;
- after approval or a material user decision;
- before implementation begins;
- after a phase completes or the approved plan materially changes;
- after verification completes;
- after user smoke-test feedback;
- after each delivery gate and at archive time.

It is not a command transcript. Capture decisions, meaningful progress, evidence, deviations, and the next owner or action.

At minimum, an active workstream contains:

- outcome and definition of done;
- evidence, constraints, assumptions, and relevant system map;
- included and excluded scope;
- acceptance criteria;
- phased implementation and verification plan;
- risks, material decisions, migration needs, rollout, and rollback where applicable;
- verification results marked Passed, Failed, Skipped, or Pending;
- user-owned smoke-test checklist;
- delivery status, commit or environment references, and remaining work.

One active workstream is the default. If genuinely concurrent approved work becomes routine and causes coordination or merge conflicts, deliberately convert `progress.md` into a dashboard linking to `docs/workstreams/active/<slug>.md`. Do not introduce parallel active documents ad hoc.

### `context.md`

Record durable facts contributors need across workstreams:

- product purpose and current boundary;
- architecture and major component responsibilities;
- repository map;
- runtime and environment topology;
- service and external contracts;
- authoritative data stores and migration model;
- authentication, authorization, trust, privacy, and credential boundaries;
- build, test, delivery, rollback, and durable engineering constraints.

Use this order when establishing present behavior:

1. observed target-environment runtime state;
2. deployed commit and effective configuration;
3. current source, migrations, schemas, manifests, workflows, and tests;
4. maintained architecture, security, and operations documentation;
5. historical material under `docs/old/`.

Update context when a durable product boundary, service responsibility, data owner, trust boundary, topology, environment mapping, deployment mechanism, or major technology choice changes. Put procedures in `docs/ops/`, active implementation detail in `progress.md`, and future direction in `roadmap.md`.

If context becomes difficult to navigate because several independently maintained subsystems are documented in depth, keep `context.md` as the orientation index and link to focused durable documents. Do not split it merely because it has grown by an arbitrary line count.

### `roadmap.md`

Roadmap horizons mean:

- `Current`: Confirmed outcome currently receiving product attention; still not implementation authorization.
- `Next`: Confirmed outcome likely to follow Current work.
- `Later`: Meaningful direction not yet selected.
- `Deferred`: Product outcome intentionally parked.
- `Recently Delivered or Parked`: Concise orientation only; detailed evidence stays in archived workstreams.

Each substantive outcome should state its status, user or product value, intended observable result, exit evidence, and active-workstream link when selected. Keep implementation checklists in `progress.md`.

The user owns priorities. Refresh the roadmap when priorities change or a workstream starts, ships, is rejected, is cancelled, or is parked. Do not invent dates, estimates, scores, or commitments without evidence and a user decision.

### `techdebt.md`

Add an item only when:

- a concrete weakness, risk, maintenance burden, or missed engineering improvement has been verified;
- a credible remedy is understood well enough to describe;
- the user accepts the recommendation but chooses not to implement it now; and
- the item is not already represented by an active workstream.

Use these states:

- `Deferred`: Accepted but intentionally postponed.
- `Promoted`: Selected and represented by an active workstream.
- `Resolved`: Delivered and verified.
- `Rejected`: Reconsidered and intentionally declined.
- `Superseded`: Replaced by another item or architecture decision.

Each active item records a stable ID, area, identified date, verified problem and impact, accepted recommendation, reason postponed, reconsideration trigger, evidence, dependencies, and cautions.

When the user selects an item:

1. promote it into `progress.md`;
2. revalidate its evidence and recommendation;
3. apply the normal work-class, planning, verification, rollout, and rollback gates;
4. mark it `Promoted` and link the workstream;
5. after delivery, mark it `Resolved` with concise commit and release evidence.

Review relevant debt when starting adjacent work, after an incident exposes the same risk, when operational cost increases, and when closing a workstream. Debt placement is never implementation approval.

## Internal Review and Delegation

Internal specialist agents may help with plan criticism, repository audits, testing, or review when useful. The primary agent remains accountable for reconciling their findings.

Do not create permanent role-owned handoff files by default. Consolidate material conclusions, decisions, test evidence, and unresolved risks into `progress.md`.

## Durable Documentation Rules

- Store each reusable procedure once and link to it elsewhere.
- Update durable docs in the same workstream as the behavior they describe.
- Keep project-specific commands in runbooks, not scattered through active plans.
- Keep live state files focused on current state; change workflow rules here and agent enforcement in `AGENTS.md`.
- Do not create Markdown tables. Prefer headings, short paragraphs, numbered procedures, bullets, and compact `Label: value` metadata.
- Never copy secrets, keys, tokens, credential values, sensitive payloads, or raw production logs into maintained docs.
- Prefer placeholders over personal paths, hostnames, IP addresses, and key names.
- Do not cite `docs/old/` as current truth.
- Do not call work released until the relevant environment and deployed commit are confirmed.

## Automation Threshold

Do not add validation infrastructure merely because this template could support it. Add focused checks after observed drift or repeated review cost justifies them.

Useful first checks may include required-file presence, relative-link validity, recognized workstream statuses, one-active-workstream consistency, and forbidden secret or historical-reference patterns. Automated checks supplement review; they do not determine whether a claim is true in a runtime environment.

## Closing and Archiving a Workstream

When work is released, completed without deployment, rejected, cancelled, or superseded:

1. Record the final outcome, verification, commit and environment references, rollback state, and unresolved follow-ups.
2. Promote desired product outcomes to `roadmap.md` and accepted-but-postponed engineering improvements to `techdebt.md`.
3. Archive the final workstream using [workstreams/README.md](workstreams/README.md).
4. Reset `progress.md` to `No active workstream` or initialize the next approved effort.
5. Refresh roadmap state and recently delivered or parked entries when applicable.
