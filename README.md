# Progress-Driven SDLC

This directory is a reusable project starter for evidence-driven software development with a small, durable documentation surface.

The workflow keeps one active workstream in `docs/progress.md`, durable system knowledge in `docs/context.md`, product direction in `docs/roadmap.md`, and accepted deferred engineering work in `docs/techdebt.md`. Repository instructions in `AGENTS.md` make the workflow discoverable to future coding agents.

## Core Principles

- Evidence beats documentation. Verify claims against code, configuration, migrations, tests, Git history, and observed runtime state.
- Keep one active workstream by default. Put its scope, decisions, plan, execution evidence, verification, and delivery gates in `docs/progress.md`.
- Plan substantial work before implementation and stop for explicit approval.
- Keep implementation, commit, push, deployment, migration, destructive cleanup, and production promotion as separate gates.
- Record only completed reality. Failed, skipped, and user-owned checks remain visible.
- Separate active execution from product direction and deferred engineering recommendations.
- Update durable documentation in the same workstream as the behavior it describes.
- Archive closed workstreams so the active file remains useful.

## Included Structure

- `AGENTS.md`: Repository-wide instructions for coding agents.
- `docs/README.md`: Documentation map, work classes, statuses, gates, and maintenance rules.
- `docs/progress.md`: The only active standard workstream; initialized with no active work.
- `docs/context.md`: Durable product, architecture, runtime, persistence, security, and delivery context.
- `docs/roadmap.md`: Directional Current/Next/Later/Deferred outcomes.
- `docs/techdebt.md`: Accepted but intentionally postponed engineering work.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md`: Scaffold for starting a substantial workstream.
- `docs/workstreams/archive/`: Final snapshots of closed workstreams.
- `docs/ops/`: Reusable operational runbooks.
- `docs/security/`: Maintained security boundaries, inventories, and procedures.
- `docs/old/`: Historical material that is explicitly non-authoritative.

## Adopt the Template

1. Copy the contents of this directory into the root of a repository.
2. Tailor `AGENTS.md` to the repository's commands, release process, and attribution rules.
3. Replace the prompts in `docs/context.md` with facts verified from executable evidence.
4. Populate `docs/roadmap.md` with confirmed direction. Do not turn roadmap placement into implementation approval.
5. Keep `docs/progress.md` at `No active workstream` until work actually begins.
6. To start substantial work, copy `docs/workstreams/WORKSTREAM_TEMPLATE.md` over `docs/progress.md`, investigate, fill it in, and stop at `Awaiting plan approval`.
7. Add project-specific runbooks and security documents only when their durable subjects exist.

## Day-to-Day Loop

1. Read the required context in `AGENTS.md`.
2. Classify the request as quick, standard, or high-risk.
3. Investigate before planning or changing behavior.
4. For standard and high-risk work, publish the evidence-backed plan in `docs/progress.md` and obtain approval.
5. Implement within the approved scope while keeping the workstream current.
6. Run proportionate automated checks and record their real outcomes.
7. Hand the user a focused smoke-test checklist and rollback considerations.
8. Obtain separate authorization for each delivery or live-system gate.
9. Close and archive the workstream when its terminal state is known.

The detailed contract is in [docs/README.md](docs/README.md).
