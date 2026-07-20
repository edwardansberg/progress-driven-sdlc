# Progress-Driven SDLC

This repository is a reusable starter for evidence-driven software development with a small, durable documentation surface.

The workflow deliberately separates stable policy, live project state, reusable scaffolding, and closed history. That separation keeps instructions from being copied into every document and lets each file change at the cadence of the information it owns.

## Operating Model

- Policy: `AGENTS.md` makes the rules enforceable for coding agents, while `docs/README.md` is the canonical human-readable workflow contract.
- Live state: `docs/progress.md`, `docs/context.md`, `docs/roadmap.md`, and `docs/techdebt.md` contain current project information rather than repeated lifecycle instructions.
- Reusable scaffold: `docs/workstreams/WORKSTREAM_TEMPLATE.md` is the one file copied whenever a substantial workstream starts.
- History: closed workstreams move to `docs/workstreams/archive/`.

## Core Principles

- Evidence beats documentation. Verify claims against code, configuration, migrations, tests, Git history, and observed runtime state.
- Keep one active workstream by default.
- Plan substantial work before implementation and stop for explicit approval.
- Keep implementation, commit, push, deployment, migration, destructive cleanup, and production promotion as separate gates.
- Record completed reality. Failed, skipped, and user-owned checks remain visible.
- Separate active execution, durable context, product direction, and deferred engineering recommendations.
- Update durable documentation in the same workstream as the behavior it describes.
- Archive closed workstreams so the active file stays useful.

## Included Structure

- `AGENTS.md`: Repository-wide instructions for coding agents.
- `docs/README.md`: Canonical workflow policy, document contracts, statuses, gates, and lifecycle rules.
- `docs/progress.md`: The current active-workstream state; initialized with no active work.
- `docs/context.md`: Verified durable product and system state.
- `docs/roadmap.md`: Directional product outcomes.
- `docs/techdebt.md`: Accepted but intentionally postponed engineering work.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md`: The sole reusable active-workstream scaffold.
- `docs/workstreams/archive/`: Final snapshots of closed workstreams.
- `docs/ops/`: Reusable operational runbooks.
- `docs/security/`: Maintained security boundaries, inventories, and procedures.
- `docs/old/`: Historical material that is explicitly non-authoritative.

## Why There Is One Reusable Workstream Template

Specification, plan, decisions, risks, implementation progress, verification, user validation, rollback, and delivery state all describe the same active effort. Keeping them in one workstream prevents separate specification, engineering, QA, and handoff files from drifting apart.

The other live documents are not instantiated per workstream:

- `context.md` is a singleton that survives many workstreams.
- `roadmap.md` is a singleton for product direction.
- `techdebt.md` is a singleton register.
- `progress.md` is replaced from the workstream scaffold and archived at closure.

If genuinely concurrent approved work becomes routine, evolve `progress.md` into a dashboard linking to multiple active files. Do not pay that coordination cost before it is needed.

## Adopt the Template

1. Copy the repository contents into a project root.
2. Tailor `AGENTS.md` to the project's commands, release process, and attribution rules.
3. Initialize `docs/context.md` from verified executable and runtime evidence, then remove its setup comment.
4. Populate `docs/roadmap.md` with confirmed direction and remove its setup comment.
5. Leave `docs/techdebt.md` empty until the user accepts a verified recommendation and explicitly postpones it.
6. Keep `docs/progress.md` at `No active workstream` until substantial work actually begins.
7. To start substantial work, copy `docs/workstreams/WORKSTREAM_TEMPLATE.md` over `docs/progress.md`, replace its prompts, and stop at `Awaiting plan approval`.
8. Add project-specific runbooks and security documents only when their durable subjects exist.

## Day-to-Day Loop

1. Read the required context in `AGENTS.md`.
2. Classify the request as quick, standard, or high-risk.
3. Investigate before planning or changing behavior.
4. For standard and high-risk work, publish the evidence-backed plan in `docs/progress.md` and obtain approval.
5. Implement within the approved scope while keeping the workstream current.
6. Run proportionate checks and record their actual outcomes.
7. Hand the user a focused smoke-test checklist and rollback considerations.
8. Obtain separate authorization for each delivery or live-system gate.
9. Close and archive the workstream when its terminal state is known.

The detailed contract is in [docs/README.md](docs/README.md).
