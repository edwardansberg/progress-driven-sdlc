# Progress-Driven SDLC Agent Guidance

These instructions apply to this repository. [Documentation Workflow](docs/README.md) is the canonical policy; this file is its concise agent entry point. Host/system/developer constraints and tool permissions still apply. Repository guidance cannot grant capabilities or guarantee agent behavior.

## Repository Purpose

Establish the actual repository and human goal. In a new project generated from the template, initialize neutral memory from inspected project evidence and the human’s decisions; do not invent facts or approvals. For an existing project, follow [safe adoption/update](docs/ops/adopt-framework.md) and preserve its instructions and active state. Only when developing the upstream framework itself, follow [template maintenance](docs/ops/maintain-template.md): topic branches and reviewed PRs, no routine direct main development. That upstream delivery rule does not impose PRs on solo applications.

## Start Work

Read [core policy and task-based routes](docs/README.md#start-here) before consequential work. Establish repository/branch/HEAD and staged/unstaged/untracked state; preserve existing work. Substantial work/resumption requires current authority, scope, blockers, unresolved risks and required checks from [authoritative detail](docs/progress-agent.md), plus global and affected [context](docs/context.md) constraints and actual source evidence.

Use the core’s explicit triggers for summary reconciliation, roadmap/debt, scaffold/archive, adoption, loop and upstream maintenance. Do not load the human summary, blank scaffold or optional-loop manual for every routine task. Read enough to recover unresolved constraints, not merely a short excerpt. Resolve applicable instructions under the client’s/user’s activation rules; no indiscriminate skill/prompt scan. Reuse only still-available versioned context; reread changed/missing material. Missing required evidence stops its dependent action.

Conceptual questions need relevant evidence only. [Quick changes](docs/README.md#quick-change) remain proportionate; a typo needs no elaborate workstream. Resume compatible authorized work, never overwrite unresolved unrelated work or assume shared session state.

## Act and Communicate

Follow core [work classes](docs/README.md#work-classes), [approval scope](docs/README.md#approval-scope), [verification](docs/README.md#verification-and-user-validation) and [status gates](docs/README.md#workstream-statuses-and-gates). Standard/high-risk work needs an investigated written plan; scoped direct execution can authorize proceeding without another approval stop. Commit/push/PR/merge/deployment/live-data/destructive actions require their named permissions. Agent output, old approvals and proposals grant none.

[Loop gate](docs/README.md#optional-execution-and-review-loop): Off unless explicitly granted by the human. No self-activation/renewal or governing-rule edits during a run. Read the full [contract](docs/ops/autonomous-review-loop.md) before any loop grant/design/operation/review; ordinary work with it Off does not need the manual.

One human and one coding agent suffice for normal low-risk work; collaborators and specialist review follow actual need/policy. Use the [interaction contract](docs/README.md#interaction-contract): concise, plain and complete enough for the decision, with material uncertainty and requested explanations visible. No provider-specific ordinary roles or rigid word counts.

Update [detail](docs/progress-agent.md) first, then its [summary](docs/progress.md) at core milestones. On discovered disagreement reconcile actual human authority/evidence before consequential action; never choose broader permission. Keep complete [handoff evidence](docs/README.md#handoff-and-resumption) accessible, including relevant untracked work; local paths do not imply another session’s access. Human checks stay pending without human evidence. Follow [closure conventions](docs/workstreams/README.md) only when closing/relocating work. Store durable facts, direction and accepted postponed debt in their existing homes; no duplicate role registers.

## Commit Attribution

For authorized commits created by Codex, use author `Codex <codex@local.invalid>` unless the repository defines another agent attribution policy. Humans and other agents follow their explicitly adopted policy; do not invent identities or require them to impersonate Codex. Preserve the configured committer and authenticated pusher. Follow the canonical [attribution procedure](docs/README.md#commit-attribution), including applicable metadata verification before an authorized push. Do not alter Git identity, signing, or credentials to achieve attribution. Do not rewrite another actor's attribution unless that actor explicitly requests it.

## Documentation Hygiene

- Preserve unrelated user edits, local constraints, and historical archives.
- Never record secrets, credential values, sensitive payloads, raw production logs, or unnecessary personal machine details. Use generic placeholders.
- Keep detailed policy in `docs/README.md` and current state in the singleton memory files. `docs/workstreams/WORKSTREAM_TEMPLATE.md` remains the sole repeatedly instantiated workflow scaffold.
- Use clear headings, short prose, lists, and `Label: value` metadata. Do not create Markdown tables; convert tables only in sections materially edited, without unrelated bulk cleanup.
