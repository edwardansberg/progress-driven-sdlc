# Maintain the Released Template

Scope: Development of the upstream Progress-Driven SDLC repository only. This reusable procedure contains no active maintainer task, approval or release evidence. Application teams use the ordinary workflow and their own delivery policy; a solo adopter does not inherit an upstream PR requirement.

## Product and development boundary

The default/release branch is the consumable product: reusable guidance and neutral application memory. Topic/development branches carry framework work. Do not routinely develop on main. Use reviewed PRs and explicit permission for commit, push and merge; implementation or a passing check grants no merge authority. Verify repository identity before applying this upstream procedure.

Use the existing progress-agent.md/detail and progress.md/summary on a development branch while working, plus branch-local context/roadmap/debt where needed. Do not introduce a second maintainer status system in the template. Read the relevant PR and its pinned evidence checkpoint when resuming a neutralized release candidate: neutral application state is not evidence that upstream maintenance was accepted or finished.

## Preserve evidence, then package

1. Start from inspected released main on an authorized topic branch. Read the complete candidate/diff and any pending predecessor records; preserve unrelated work and unresolved decisions. Record scope and human authority in the existing detailed record before implementation.
2. Develop and verify within that scope. Keep one detailed authority record and its derived human summary. Do not turn maintainer plans into reusable product policy without a deliberate design decision.
3. Before neutralization, commit the scoped maintainer record with its decisions, evidence, limitations and pending human gate. Preserve historical archives in reachable history before removing them from the release tree. Record the full checkpoint SHA and relevant paths in the PR description and/or final packaging commit message. Prefer a normal merge commit for this repository so checkpoint ancestry survives branch deletion; do not rewrite or delete history as packaging. If another merge strategy is chosen, first preserve a durable reachable evidence reference approved by the maintainer; do not rely only on a disposable branch.
4. In a subsequent forward commit, restore neutral starter memory and remove maintainer-only archives/reports from the proposed release tree. This is packaging, not a terminal workstream outcome. Keep pending acceptance and exact check results in the packaging commit/PR evidence. No maintainer identifier, approval or active work appears in starter memory.
5. Inspect the complete PR diff and resulting tree against the inventory below. Verify reusable links and neutral state, including files unchanged by the latest edit. Record static walkthrough results for new solo use, later collaboration, existing adoption, occupied instructions, maintainer work and the generated file set. These are document checks, not measured usability.
6. Human reviews the exact final candidate. Merge only with explicit permission, required checks satisfied, no unresolved conflicts or unrelated changes, and the resulting main tree still neutral. Recheck after a base update. Do not bypass protection. Verify the actual main tree after an authorized merge; any corrective main change also needs the applicable delivery authority.

If corrections are requested after neutralization, restore the checkpoint into the branch’s existing records under the current request, reconcile later decisions and continue there. Do not treat a historical approval as new permission. Repeat the evidence checkpoint and neutralization before review. PR history/commits carry acceptance and delivery observations; do not write a maintainer “accepted” entry back into released application memory.

## Clean release inventory

Classify the exact tree, including unexpected additions; do not rely on a selective copy operation to hide contaminants:

- README.md: Reusable new-project onboarding, existing-project adoption link and optional upstream-maintenance link. Target replaces the starter introduction during authorized initialization.
- AGENTS.md and docs/README.md: Reusable agent guidance and canonical policy; repository-mode checks prevent upstream release rules from becoming application requirements.
- docs/progress.md: Neutral, short human view with a matching detailed-source revision, no active work and automation Off.
- docs/progress-agent.md: Authoritative neutral application state; no workstream, scope grant, candidate, checks or acceptance claimed.
- docs/context.md: Target-initialized structure; unknown project facts and source revision remain explicit until verified.
- docs/roadmap.md and docs/techdebt.md: Neutral direction/debt structures; no upstream commitments or outcomes.
- docs/workstreams/: Reusable scaffold and directory/archive indexes only. No dated maintainer records in the release tree.
- docs/ops/: Reusable index, adoption/update guide, this upstream-only procedure and the optional advanced loop specification. No project-specific deployment facts or active run.
- docs/security/: Reusable guidance only until target-specific evidence exists.
- docs/old/: History guidance only; no upstream historical documents.

Framework-maintainer-only content includes active tasks, candidates, approvals, roadmap/debt and review reports. Historical maintainer content includes dated workstreams and old project context. Both remain recoverable in commits/PR evidence, not in the released working tree. Optional advanced policy may ship as reference but cannot enable itself or burden ordinary solo work. Do not copy a second policy tree, add generated role registers or introduce an installer merely for packaging.

## GitHub configuration: separate owner action

These are recommended settings, not controls enforced by this Markdown:

- After a clean release is reviewed and merged, an authorized owner can enable **Template repository** and verify that the UI offers **Use this template**.
- Protect main with a PR requirement, block force pushes and deletion. No mandatory additional reviewer or CI check is proposed until there is a concrete need and meaningful checks. Inspect actual rules and available plan capabilities; do not assert enforcement from this document.
- Repository-setting changes require their own permission. Do not change them as part of ordinary documentation development.

Use the default branch only when generating a new application. **Include all branches** can copy development state; this design does not make every development branch a neutral template. Cloning/forking retains upstream history; creating from a GitHub template starts independent history. Existing applications adopt selected content and preserve their own history rather than merging upstream ancestry.

Official references, checked 2026-09-25: [Create from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) and [configure a template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository). These document GitHub behavior; they do not prove this repository’s settings or a completed generation test.
