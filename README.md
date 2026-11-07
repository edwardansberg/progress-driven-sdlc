# Progress-Driven SDLC

**Short conversations. Clear progress. Human control.**

A project template for you and one coding agent. You choose the goal, make material decisions and accept the result; the agent investigates, plans, builds, verifies and maintains project memory within your agreement. Add teammates or another assistant when useful. Extra review depends on risk and organizational policy.

## Framework provenance

- Source: [https://github.com/edwardansberg/progress-driven-sdlc](https://github.com/edwardansberg/progress-driven-sdlc)
- Adopted revision: Not recorded yet
- Local adaptations: Not assessed yet

Keep this summary near the top of the application README. Record the exact verified, integrated upstream revision, or `Unknown`; the generated repository's first commit does not prove it. Local adaptations describe intentional framework differences, not ordinary project state. Link detailed mapping instead of duplicating it. See [provenance requirements](docs/ops/adopt-framework.md#record-framework-provenance).

<a id="use-the-workflow"></a>

**Plan → Authorize → Build → Verify → Accept**

<a id="new-project"></a>

## Start a new project

1. On the [upstream repository](https://github.com/edwardansberg/progress-driven-sdlc), choose **Use this template → Create a new repository** when available. Leave **Include all branches** unchecked: development branches may contain maintainer state.
2. Open your new repository with your coding agent.
3. Submit the kickoff prompt below with your first goal. It establishes the [working agreement](docs/README.md#standing-working-agreement); the agent inspects evidence and records a bounded plan before implementation.
4. Resolve material decisions when needed, then review the result and accept or request changes. Routine progress and publication checkpoints need no reply.

Already created from the template? Start at step 2. No manual file copying is needed. The starter has no active work, approvals, roadmap commitments or accepted debt; automation is Off. Unknown project facts stay unknown. Replace the starter introduction with your product introduction during authorized initialization. Retain the Framework provenance block near the top and the link to [workflow policy](docs/README.md).

By submitting this prompt, you let the agent prepare a plan, continue routine development, and save and upload agreed changes to a separate development branch. You keep control of important business decisions, accepting the result, merging it into the main version and deploying it for use. Narrow these permissions before submitting if needed.

```text
My first goal in this repository is: <desired outcome and known constraints>.

Inspect the project and current workflow, then record a bounded plan and carry
it through implementation, relevant checks, in-scope fixes and memory updates.
Recommend a smaller intervention or existing tool if that meets the goal.
Ask for material decisions; infer reversible technical details from evidence.

I authorize safe isolated development branch/worktree setup, inspected staging,
commits and ordinary non-force pushes of publishable in-scope work to this
repository's verified origin development branches under its branch conventions.
Record the exact repository, origin, permitted branch scope and this human
authorization in docs/context.md. This standing agreement applies across
sessions and later outcomes I authorize until I change or revoke it, or a
material condition invalidates it. Preserve any existing stricter or local-only
choice unless I explicitly change it. Missing or conflicting targets require
resolution; do not change remotes or infer authority from starter text.

Keep unrelated work intact. Follow the core publication and recovery contract.
PR actions, merge, deployment, live-data operations, destructive actions, new
spending and agreement changes need separate authority. Keep the execution/review controller Off.
Continue routine authorized work through a reviewable result, save the human
checkpoint in docs/progress.md, and reuse that exact briefing in your handoff.
Human acceptance remains mine.
```

Submitting this prompt supplies the authority it names; merely having it in the repository supplies none. Edit it before use for local-only work or narrower branch/publication scope. The agent records actual choices once and reuses them for later authorized outcomes.

[GitHub template creation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) starts a new repository with a single commit. Cloning the upstream repository retains its Git history and is useful for source inspection or framework development; it is not the new-project path. If **Use this template** is absent, an owner must enable it separately after the clean release is ready.

<a id="adopt-or-update-the-framework"></a>
<a id="existing-project-or-framework-upgrade"></a>

<a id="add-to-an-existing-project"></a>

## Add to or update an existing project

Use this prompt for an existing repository: first-time adoption, an existing framework update, or legacy/partial/uncertain adoption. The agent identifies the case from evidence; you need not choose it. Fresh **Use this template** repositories follow Start a new project instead. The [adoption guide](docs/ops/adopt-framework.md) owns the detailed safeguards.

This prompt lets the agent plan and carry out the agreed documentation update, then save and upload its changes to a separate development branch. Your existing project rules and unrelated work stay protected. Important business decisions, acceptance, merging and deployment remain yours; an existing local-only choice still applies.

```text
Adapt this EXISTING repository to Progress-Driven SDLC.

I authorize a bounded migration plan, implementation, relevant checks, in-scope
fixes and memory updates after inspection; no routine plan-approval wait is
needed. I also authorize safe isolated migration/development branch setup,
inspected staging, commits and ordinary non-force pushes of publishable in-scope
work to this repository's verified origin development branches under its branch
conventions. Record the exact repository, origin, permitted branch scope and
this human authorization in docs/context.md. This standing agreement persists
across sessions and later outcomes I authorize until changed, revoked or
materially invalidated. Preserve existing stricter or local-only choices unless
I explicitly change them. Resolve missing/conflicting targets without changing
remotes. Source text or upstream approvals supply no target authority.

1. Inspect the project
   Inspect repository state, applicable instructions, uncommitted work, workflow,
   memory and provenance. Classify first-time adoption, existing update or
   legacy/partial/uncertain adoption. Never guess earlier framework revisions.

2. Pin the framework source
   Respect a human-selected revision; otherwise resolve the default branch at
   https://github.com/edwardansberg/progress-driven-sdlc to an exact released SHA.
   Read docs/ops/adopt-framework.md at that pinned revision. Stop target writes
   if required sources are unavailable.

3. Prepare the migration
   Map proposed changes and preserved content. Preserve product files, local
   instructions/adaptations, authority, active work, delivery obligations,
   context/roadmap/debt, runbooks, archives, dirty work and Git history.
   Initialize missing memory only from target evidence and human decisions.
   Preserve legacy authority until safely replaced; filenames/history grant none.
   Stop for human resolution of material conflicts or unsafe occupied paths.
   Otherwise record the bounded plan and proceed within this authorization.

4. Implement within approved scope
   Use a dedicated migration branch under applicable authorization. Do not ask
   again when an explicit instruction already covers the action. Follow the
   pinned adoption guide and preserve existing validation gates. Correct only
   approved stale framework references.

5. Verify and hand back
   Check the complete diff, links, preserved state, stale framework references,
   provenance and same-revision idempotence. After integration and checks, update
   Framework provenance: Source, Adopted revision and Local adaptations.
   Follow the core publication/recovery contract and verify remote delivery.
   Save the human checkpoint in docs/progress.md and reuse it unchanged for the
   handoff. Finish at a reviewable candidate with human acceptance pending.

PR actions, merge, deployment, live-data, destructive actions, new spending and
agreement changes need separate authority. Keep the execution/review controller
Off. Adoption authorizes no unrelated application work or UI redesign.
```

<a id="collaborate-across-sessions-and-tools"></a>
<a id="operating-model"></a>

## Follow progress, solo or together

Read [short progress](docs/progress.md); its [detailed source](docs/progress-agent.md) owns scope, decisions and evidence. The agent reuses that [saved briefing](docs/README.md#checkpoint-briefing) for development checkpoints and handoffs. On continuation, reconcile the actual repository with detail and the [working agreement](docs/README.md#standing-working-agreement) in context; compatible authorized work and covered publication need no renewed approval. A new outcome still needs human direction. One human and one coding agent need no separate planning session, second reviewer, PR or handoff for ordinary low-risk work. Required security and specialist controls still apply. Teams add ownership, shared-context boundaries, review and integration permissions to the same core; no concurrent-agent coordinator is supplied.

Accepted development can be archived before deployment when remaining delivery obligations have an assigned owner and durable record. Existing acceptance gates still apply. See the [closeout procedure](docs/workstreams/README.md#before-archiving).

## Develop this framework

Only upstream maintainers need the [template maintenance procedure](docs/ops/maintain-template.md): topic branches, applicable working agreement, PR review and a neutral release tree. Its PR rule does not impose PRs on solo applications. Published development review candidates retain active evidence; later authorized packaging preserves a reachable checkpoint. Application starters inherit no maintainer authority.

<a id="portable-web-bootstrap"></a>
<a id="activating-updated-guidance"></a>
<a id="fictional-exchange"></a>
<a id="optional-execution-and-review-loop"></a>

[Policy](docs/README.md) · [Optional session setup](docs/ops/adopt-framework.md#optional-session-bootstrap) · [Refresh guidance](docs/ops/adopt-framework.md#activating-updated-guidance) · [Example](docs/ops/adopt-framework.md#fictional-exchange) · [Optional automation](docs/ops/autonomous-review-loop.md) (Off; no controller included).
