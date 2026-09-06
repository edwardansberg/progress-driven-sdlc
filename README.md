# Progress-Driven SDLC

A reusable starter for evidence-driven development with a small, durable documentation surface. It supports a human coordinating research, planning, and review in a Web assistant with local work by a coding agent, and also works with a single assistant.

The human owns priorities and approvals. Assistants work from identified evidence and scoped authority. The [canonical workflow](docs/README.md) defines the process; documentation provides guidance, not mechanical permission enforcement.

## Operating Model

- Policy: [docs/README.md](docs/README.md) owns the workflow contract; [AGENTS.md](AGENTS.md) is concise agent guidance.
- Live state: [progress](docs/progress.md) holds one active workstream; [context](docs/context.md), [roadmap](docs/roadmap.md), and [technical debt](docs/techdebt.md) keep durable facts, confirmed direction, and accepted postponed recommendations separate.
- Reusable scaffold: [WORKSTREAM_TEMPLATE.md](docs/workstreams/WORKSTREAM_TEMPLATE.md) holds the specification, plan, decisions, verification, user validation, and delivery evidence for a substantial effort.
- History: terminal workstreams retain their outcomes in [the archive](docs/workstreams/README.md). [docs/old/](docs/old/README.md) is historical reference only.
- Procedures: [operations runbooks](docs/ops/README.md) and [security documentation](docs/security/README.md) hold reusable project-specific procedures and boundaries.

One active workstream keeps authority clear. Handoffs reuse its metadata and delivery summary; there are no separate Web, planner, engineer, QA, or reviewer status files. Context, roadmap, and debt are singleton documents, not templates copied per effort.

## Collaborate Across Sessions and Tools

Use the [collaboration contract](docs/README.md#human-coordinated-collaboration), [illustrative handoff](docs/README.md#illustrative-handoff), and [task-request shape](docs/README.md#task-request-shape). Identify what each participant inspected and supply only the missing evidence needed for the next step.

A Web review of a GitHub commit cannot verify a different uncommitted laptop patch. Transfer a focused sanitized diff and relevant files, including untracked files when needed; no commit or push is required merely to share context.

### Optional execution and review loop

The [opt-in contract](docs/README.md#optional-execution-and-review-loop) lets a human bound repeated implementation, verification, specifically authorized review-branch publication, and Web review before final human validation. Installation, adoption, and implementation approval leave it Off. Activation needs a complete human grant, distinct controls, known publication effects, and a permitted transport; review publication grants neither acceptance nor release.

The [operational reference](docs/ops/autonomous-review-loop.md) specifies messages, recovery, controls, and pilot prerequisites. This starter supplies documentation, not a working controller or tested stop mechanism. Manual relay preserves the chosen Web reviewer while automated transport permission is unresolved; an API reviewer is a separate human choice.

## Adopt or Update the Framework

This upstream framework repository and each adopting application have separate repositories, branches, evidence, active state, and permissions. Upstream `docs/progress.md` may contain real framework-maintenance work awaiting review. It is not the adopting application's project state and must not be reset upstream for packaging convenience.

Before copying or merging anything, inspect the target repository, its applicable instructions and local constraints, and its staged, unstaged, and untracked work. Establish the authorized adoption scope and preserve existing files. Framework-policy adoption does not authorize application development, release actions, or resetting live state.

### New project

1. Select the relevant starter policy, scaffold, and directory guidance for the target; do not copy upstream Git metadata or framework-maintenance state into the application.
2. Tailor policy deliberately to the project's needs. Keep entry-point instructions concise, with commands and release/recovery procedures in appropriate runbooks.
3. Initialize application `docs/context.md` from that application's verified evidence, `docs/roadmap.md` from confirmed user direction, and `docs/techdebt.md` only from accepted postponed recommendations. Leave unknowns explicit and remove setup comments when used.
4. Initialize application `docs/progress.md` as `No active workstream` only if no substantial effort is active. Otherwise record the actual requested effort and its authorization using the sole scaffold.
5. Follow [workstream initialization](docs/workstreams/README.md#starting-a-workstream): standard/high-risk work normally stops for plan approval, while recorded explicit scoped direct execution can proceed after investigation and a written plan.

### Existing project or framework upgrade

1. Compare existing `AGENTS.md`, workflow policy, active workstream, context, roadmap, debt, runbooks, and archives with the proposed framework changes.
2. Merge policy and entry points deliberately. Preserve project-specific constraints and procedures; resolve genuine conflicts under the target's authority rather than replacing instructions wholesale.
3. Preserve the active workstream's evidence, approved scope, and pending gates. An incompatible substantial adoption effort requires explicit disposition of that work before replacement. Never blindly copy the scaffold over it.
4. Retain verified application memory and historical archives. Add missing structure only where needed; do not replace live documents with upstream placeholders or import upstream approvals.
5. Verify the merged links, setup comments, instructions, and relevant contract scenarios. Updating policy alone grants no authority to implement application roadmap or debt items.

### Activating updated guidance

Editing `AGENTS.md`, overrides, or referenced policy on disk does not establish that a running session refreshed its loaded instructions. Use the tool's documented reload/new-session behavior when relevant; preserve the handoff first and do not automatically interrupt active work. Tool-specific discovery details are in the [source note](docs/README.md#source-note).

Reading amended files is distinct from demonstrating automatic instruction loading or compliant behavior. A self-reported summary is limited evidence, not enforcement. A future proportionate read-only setup check can identify accessible instruction sources and explain plan/delivery boundaries from the intended repository and directory. Keep that check user-owned when the agent cannot observe the environment, and record it as unperformed until evidence is available. Do not assume a Markdown link loads its target: retain explicit canonical-policy reading for substantial work.

## Use the Workflow

Conceptual discussion and clearly requested quick changes stay lightweight. Substantial work follows [context review and work classes](docs/README.md#work-classes), an investigated plan, and [scoped approval](docs/README.md#approval-scope), including the explicit direct-execution exception. Continue authorized steps without unnecessary pauses.

Keep evidence tied to its snapshot, run [proportionate verification](docs/README.md#verification-and-user-validation), and leave user validation to the human. Delivery permissions remain distinct. Successfully accepted work closes as [Completed or Released](docs/README.md#workstream-statuses-and-gates) according to its agreed target; archiving preserves the outcome.
