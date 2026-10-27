# Progress-Driven SDLC

**Short conversations. Clear progress. Human control.**

A project template for you and one coding agent. You choose the goal, authorize the scope and accept the result; the agent investigates, builds and verifies. Add teammates or another assistant when useful. Extra review depends on risk and organizational policy.

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
3. Tell it your first goal. It follows the [task-based reading route](docs/README.md#start-here), inspects project evidence and prepares a scoped plan before implementation.
4. Authorize the plan, review the verification, and accept or request changes.

Already created from the template? Start at step 2. No manual file copying is needed. The starter has no active work, approvals, roadmap commitments or accepted debt; automation is Off. Unknown project facts stay unknown. Replace the starter introduction with your product introduction during authorized initialization. Retain the Framework provenance block near the top and the link to [workflow policy](docs/README.md).

[GitHub template creation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) starts a new repository with a single commit. Cloning the upstream repository retains its Git history and is useful for source inspection or framework development; it is not the new-project path. If **Use this template** is absent, an owner must enable it separately after the clean release is ready.

<a id="adopt-or-update-the-framework"></a>
<a id="existing-project-or-framework-upgrade"></a>

<a id="add-to-an-existing-project"></a>

## Add to or update an existing project

Use this prompt for an existing repository: first-time adoption, an existing framework update, or legacy/partial/uncertain adoption. The agent identifies the case from evidence; you need not choose it. Fresh **Use this template** repositories follow Start a new project instead. The [adoption guide](docs/ops/adopt-framework.md) owns the detailed safeguards.

```text
Adapt this EXISTING repository to Progress-Driven SDLC.

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
   Otherwise present a bounded plan.

4. Implement within approved scope
   Use a dedicated migration branch under applicable authorization. Do not ask
   again when an explicit instruction already covers the action. Follow the
   pinned adoption guide and preserve existing validation gates. Correct only
   approved stale framework references.

5. Verify and hand back
   Check the complete diff, links, preserved state, stale framework references,
   provenance and same-revision idempotence. After integration and checks, update
   Framework provenance: Source, Adopted revision and Local adaptations.
   Stop at a reviewable candidate.

Infer no staging, commit, push, PR, merge, deployment, live-data, automation or
unrelated application permission.
```

<a id="collaborate-across-sessions-and-tools"></a>
<a id="operating-model"></a>

## Follow progress, solo or together

Read [short progress](docs/progress.md); its [detailed source](docs/progress-agent.md) owns scope, decisions and evidence. One human and one coding agent need no separate planning session, second reviewer, PR or handoff for ordinary low-risk work. Required security and specialist controls still apply. Teams add ownership, shared-context boundaries, review and integration permissions to the same core; no concurrent-agent coordinator is supplied.

Accepted development can be archived before deployment when remaining delivery obligations have an assigned owner and durable record. Existing acceptance gates still apply. See the [closeout procedure](docs/workstreams/README.md#before-archiving).

## Develop this framework

Only upstream maintainers need the [template maintenance procedure](docs/ops/maintain-template.md): topic branches, explicit publication permissions, PR review and a neutral release tree. Its PR rule does not impose PRs on solo applications. Branch records and commit history retain maintainer evidence; application starters do not inherit it.

<a id="portable-web-bootstrap"></a>
<a id="activating-updated-guidance"></a>
<a id="fictional-exchange"></a>
<a id="optional-execution-and-review-loop"></a>

[Policy](docs/README.md) · [Optional session setup](docs/ops/adopt-framework.md#optional-session-bootstrap) · [Refresh guidance](docs/ops/adopt-framework.md#activating-updated-guidance) · [Example](docs/ops/adopt-framework.md#fictional-exchange) · [Optional automation](docs/ops/autonomous-review-loop.md) (Off; no controller included).
