# Active workstream: human-coordinated-agentic-development

Workstream class: Standard

Risk: Medium; documentation changes affect how adopters interpret authority and delivery gates.

Status: Ready for user validation

Current gate: Ready for user validation

Next action: User reviews local snapshot F1 using the checklist below and accepts the patch or requests corrections. Later delivery permissions remain unapproved.

Repository: edwardansberg/progress-driven-sdlc (upstream framework only)

Branch: main

HEAD and review base: dfe3667ea37b41ba6de948ca1253930a23d7d093

Snapshot: Local review snapshot F1 against the base above: six unstaged modifications listed in Delivery Summary, no staged or untracked files. Initial checkout was clean; no pre-existing work required separation or preservation.

Plan revision: r1, 2026-09-06

Started: 2026-09-06

Last substantive update: 2026-09-06 by Codex

Delivery target: Uncommitted local documentation patch for user review; this task stops before user acceptance or any release action.

Workflow: [Documentation Workflow](README.md)

## Requested Outcome

Improve the existing framework for a human coordinating a planning/review assistant with a coding agent. Keep canonical policy, one active workstream, explicit gates, evidence-based memory, and a small provider-neutral documentation surface.

## Definition of Done

The bounded patch is implemented and available checks are recorded, all ten requested contract scenarios have document-level walkthroughs, and a focused review handoff is prepared. Stop at `Ready for user validation` with user checks pending. Acceptance, release, and archival are outside this task's stopping gate.

## Context and Evidence

### Verified current behavior

The following findings describe the initial review base. The implemented local amendment and its evidence are recorded under Verification and Delivery Summary.

- Local Git inspection on 2026-09-06 identifies the requested repository on `main` at the supplied reference commit. Initial staged, unstaged, and untracked sets are empty. Sanitized remote inspection confirms the GitHub repository identity; no remote synchronization was performed.
- Read all 13 tracked Markdown files, including root and directory guidance, the complete canonical policy and progress file, singleton memory, and archive/scaffold conventions. Root `AGENTS.md` is the only repository-owned agent instruction; no applicable ancestor/global override, additional repository instructions, or repository-owned skills were found.
- Initial `docs/progress.md` says `No active workstream`; there is no incompatible active effort. Context and roadmap are uninitialized, debt has no accepted items, and no closed workstream snapshots exist. These are starter placeholders, not an application's verified state.
- The tracked inventory contains documentation only: no application code, migrations, dependency manifests, CI configuration, or repository test commands. Operations and security indexes define generic conventions only.
- At the review base, root README calls agent rules enforceable; canonical evidence ordering conflates different states. No snapshot-aware Web/human/coding-agent handoff contract or verification record shape exists.
- Default approval gates and the quick-change exclusions already exist and should be preserved. Unconditional setup instructions in root README, canonical policy, progress setup, archive guide, and scaffold conflict with the existing explicit direct-execution exception in `AGENTS.md`. Partial approval and approval provenance are underspecified.
- Canonical closure mentions completion without deployment, but status flow ends in `Released -> Archived` and archive instructions omit a successful non-release outcome. The scaffold combines push/PR approval, duplicates plan/implementation approval and next action, and forces three phases.
- Both requested official references were opened on 2026-09-06. The model guide's prompting sections discuss initiative, instruction conflicts, readable output, delegation, and proportionate testing. The instruction-discovery reference redirects to ChatGPT Learn and describes Codex-specific discovery, including overrides. Source links and selective adaptation are recorded in the [canonical source note](README.md#source-note).

### Chosen target behavior

The user's request selects a provider-neutral amendment in the six named existing files: precise scoped authorization, snapshot-aware handoffs and resumption, proportionate verification, a `Completed` terminal outcome, a streamlined scaffold, and adoption that preserves application state. Written implementation is present in F1; future agent behavior is not established by the patch.

### Inference requiring validation

The document-level consistency claim is supported by the ten walkthroughs below. Whether agents follow the contract reliably in practice remains unverified; live agent evaluations are outside this patch's scope.

### Open decision

No implementation choice blocks the authorized patch. User acceptance remains pending at the stopping gate. Any later delivery action needs its own explicit scope.

## Relevant System Map

- `docs/README.md`: canonical policy, evidence, collaboration, verification, and lifecycle.
- `AGENTS.md` and root `README.md`: agent entry point and human orientation/adoption.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md` and `docs/workstreams/README.md`: single scaffold and local archive conventions.
- `docs/progress.md`: this actual workstream, authorization, results, and handoff.
- Other singleton documents, runbook indexes, and history remain intact unless a directly necessary consistency correction is found.

## Scope

Included: Amend the six named files, inspect the full local diff and relevant untracked material, verify links and policy consistency, record ten scenario walkthroughs, and prepare review and rollback guidance.

Excluded: Commits, pushes, PR creation or merge, branch switching, new worktrees, deployment, live migration or other live operations, destructive cleanup, repository/global identity or signing changes, credential changes, personal/global instructions or installed skills, downstream repositories, new permanent files, CI, dependencies, hooks, validators, evaluation harnesses, or model/runtime configuration.

## Constraints and Assumptions

Preserve existing Git attribution, unrelated changes, historical material, and deliberate adopting-project constraints. Use no Markdown tables. Keep policy in its canonical file and task state here. Do not invent application context, roadmap commitments, or accepted debt. No application or live environment is involved in this documentation patch.

## Decisions and Authorization

1. Direct execution: The user explicitly authorized investigation, an evidence-backed plan, local implementation, verification, and review handoff in the request titled "Patch Progress-Driven SDLC for human-coordinated agentic development," section "Execution authority for this task," received 2026-09-06. Plan r1 implements that bounded request; it is not a separately user-approved plan and does not grant itself authority. The framework's normal plan-approval requirement remains unchanged.
2. File placement: Consolidate reusable collaboration, authority, verification, and lifecycle rules in canonical policy; keep the scaffold proportional and entry points short. No new status register or template is needed.
3. Source adaptation: Apply prompting guidance only inside the user's authorized scope. Do not adopt example permission to create worktrees/PRs or API migration advice. Tool-specific discovery remains an official-documentation reference.
4. Memory: Keep this real framework-maintenance workstream active through user review. Preserve uninitialized application-memory placeholders and explain their adoption boundary in root README.
5. Review correction: Clarified proposed/approved/pending included scope in the scaffold after independent review. This is a wording correction within r1, not new behavior or expanded authorization. Removed the optional concurrency-dashboard suggestion to retain the requested single active workstream; allowed justified non-environment release evidence for artifact targets while preserving verified-release requirements.

## Acceptance Criteria

- Canonical policy distinguishes instruction authority, factual evidence, proposals, scoped user authorization, and tool permissions without claiming universal tool precedence or mechanical enforcement.
- Collaboration and resumption identify snapshots, dirty/untracked material, evidence provenance, decisions, and next owner without requiring commits, exports, multiple agents, or extra registers.
- Quick/standard/high-risk decisions, partial approval, direct execution, and separate delivery permissions are consistent across all entry points and setup comments.
- Verification uses the requested evidence labels and Check/Basis/Scope/Result/Limitations record; unknown process completion, skipped checks, and user validation remain truthful.
- `Completed`, `Released`, and archival retain distinct, consistent meanings. The sole scaffold has one current status/gate/next action, one implementation authorization record, distinct delivery permissions, and flexible phases.
- New and existing adoption preserves local constraints, active state, and archives. All ten requested scenario decisions have supporting sections and no unresolved contradiction.
- Only the bounded local documentation patch remains, with available checks passed and user validation pending.

## Implementation Plan

### Phase 1 — Policy, entry points, and scaffold

- [x] Inspect current checkout, required documents, instruction sources, history, and official references; record plan r1 and user authorization before substantive edits.
- [x] Amend canonical policy for authority, collaboration, approval, verification, lifecycle, and selective source guidance.
- [x] Align agent entry point, adoption instructions, archive conventions, and scaffold; remove overlapping or contradictory rules.

Acceptance: The requested contract is expressed in the six existing files without expanding task permissions or adding permanent artifacts.

Rollback: Review and reverse only this task's uncommitted hunks against the recorded base, preserving any intervening work.

### Phase 2 — Verification and review handoff

- [x] Inspect the full staged/unstaged diff and relevant untracked material; check links/anchors, paths, setup comments, statuses, duplication, hygiene, and table additions.
- [x] Run existing applicable checks and `git diff --check`; record actual outcomes and limitations.
- [x] Walk through all ten requested scenarios against final policy and reconcile an independent bounded review if used.
- [x] Update this workstream and prepare the user checklist, rollback considerations, and snapshot-aware handoff at the requested stopping gate.

Acceptance: Available checks and document walkthroughs are recorded after final substantive edits. User checks stay pending.

## Risks and Controls

- Permission drift: Review approval and lifecycle scenarios against the user's explicit boundaries and preserve the original quick-change exclusions and commit attribution.
- Duplicated authority: Keep detailed policy canonical, link entry points to it, and use one current metadata block in the scaffold/workstream.
- Overstated evidence: Scope claims to the checkout or supplied sources; document walkthroughs do not prove future agent behavior or Web inspection of a laptop patch.
- Adoption data loss: Replace blind-copy onboarding with deliberate initialization/merge guidance that preserves existing state and constraints.

## Migration, Rollout, Observability, and Rollback

Migration, rollout, and runtime observability: Not applicable; only local Markdown changes, with no application or environment target.

Rollback: The initial checkout is clean at the recorded base. If the user rejects the patch, review and reverse only its six-file diff, preserve later unrelated edits, and record the disposition before any future closure. No rollback or cleanup is performed by this task.

Destructive effects: None authorized.

## Verification

Checks below were performed by the primary coding agent on 2026-09-06 after normative edits, unless another source is identified. The final evidence update also passed the consistency/whitespace checks: 13 Markdown files, 79 local links, 43 anchor targets, six expected changed paths, and zero inspection issues. The final gate/owner update changes no policy or evidence basis.

### Repository Scope and Diff

Check: Repository identity, complete patch, unchanged surrounding files, and staged/untracked material.

Basis: `git branch --show-current`, `git rev-parse HEAD`, `git status --porcelain=v1 --untracked-files=all`, `git diff HEAD --numstat`, complete `git diff` for all six changed files, `git diff --cached`, and `git ls-files --others --exclude-standard`; manual reading of the resulting patch.

Scope: Local F1 checkout at the recorded base; primary agent inspection.

Result: Passed. Branch/HEAD unchanged; six named files modified and unstaged; no staged or untracked material. The seven other tracked Markdown files remain unchanged. No new permanent files or downstream changes were made.

Limitations: This verifies the local checkout, not a remote branch or deployed environment. A Web reviewer must receive this diff and relevant files to review F1.

### Links, Paths, and Hygiene

Check: Markdown targets/anchors, metadata uniqueness, patch boundaries, tables, conflict markers, and accidental sensitive or personal details.

Basis: One-off read-only inline PowerShell inspection over `git ls-files -- '*.md'`: resolve Markdown link targets relative to each file; compare fragments with normalized headings; inspect changed paths from `git diff HEAD --name-only`; count status/gate/next-action metadata; scan for table/conflict-marker, private-key/token, credential-URL, personal-path, and IP-address patterns. Manual diff review covers generic examples and policy semantics.

Scope: All 13 tracked Markdown files for local links; six changed files for patch hygiene; progress and scaffold for current-metadata uniqueness. Official external references were opened separately and their cited headings inspected.

Result: Passed. No missing local paths/anchors, unexpected changed files, duplicate current metadata, table additions, conflict markers, or sensitive/personal-detail findings. Illustrative paths in handoff/archive examples are explicitly generic data, not claims that those files exist in this repository.

Limitations: This focused inspection is not a general Markdown parser or comprehensive secret detector. External links were checked through the source reads, not a crawler. No validator or tooling was added to the repository.

### Whitespace and Existing Checks

Check: Git whitespace checks and discovery of applicable project checks.

Basis: `git diff --check` and `git diff --cached --check`; tracked-file inventory, required document/runbook reads, and `git ls-files -- '*.yml' '*.yaml' 'package.json' 'pyproject.toml' 'Makefile' '*test*' '*lint*'`.

Scope: Local six-file patch and index after normative edits.

Result: Passed. Both Git whitespace checks exited 0 with no diagnostics. Inventory and runbook inspection found no existing executable test/lint/build/CI checks to run; no pre-existing check failure was identified.

Limitations: Application builds, runtime checks, and live agent evaluations are Skipped as not applicable to this documentation-only repository/task. This is not evidence of application behavior or model compliance.

### Policy and Independent Review

Check: Entry points, setup comments, policy duplication, lifecycle, authorization, and source adaptation.

Basis: Complete diff and unchanged directory/memory guidance; `rg -n 'TEMPLATE SETUP|REUSABLE SCAFFOLD|Awaiting plan approval|Push or pull-request|agent enforcement|makes the rules enforceable|active/<slug>' --glob '*.md'`; primary-agent review plus the read-only specialist `contract_review` report supplied in this task.

Scope: Normative F1 documents. The specialist reviewed the six-file diff before final evidence/metadata updates and independently confirmed branch/HEAD and dirty state.

Result: Passed after one correction. The specialist identified the scaffold's proposed-scope ambiguity; the primary agent changed Included to distinguish proposed, approved, and pending portions, then inspected the correction. No remaining contradiction was found. Default gates, quick exclusions, attribution, and one active workstream remain intact. Detailed attribution moved to canonical policy with a concise agent reference.

Limitations: Specialist conclusions are supplied review evidence. The primary agent independently read and reconciled them; the specialist did not independently verify the initial clean state or official-source contents. Neither review is user acceptance or a live agent evaluation.

### Scenario Walkthroughs

Check: All ten requested decisions against the written contract.

Basis: The user's acceptance scenarios; direct reading of the supporting sections linked below, reconciled with the specialist review.

Scope: F1 policy, entry points, and scaffold after the proposed-scope correction; document-level validation only.

Result: Passed, 10 of 10 expected decisions supported; no unresolved contradiction found.

Limitations: These walkthroughs evaluate the documents, not live agent compliance, runtime behavior, or a Web assistant's access to local files.

1. Conceptual question and typo. Expected decision: Answer from relevant evidence without creating substantial work; a clearly requested isolated typo uses the quick path. Result: Passed. Support: [Start Here](README.md#start-here), [Quick change](README.md#quick-change), and agent guidance's Start Work.
2. Non-trivial feature versus direct execution. Expected decision: Investigate and publish a plan, then stop at `Awaiting plan approval` unless the user explicitly authorizes scoped direct execution. That exception still requires the written plan and respects exclusions. Result: Passed. Support: [Standard workstream](README.md#standard-workstream), [Approval Scope](README.md#approval-scope), and [Starting a Workstream](workstreams/README.md#starting-a-workstream).
3. Partial approval and material change. Expected decision: Only identified approved portions/revisions proceed; pending scope remains pending, and a later material change needs approval before affected work. Result: Passed after the scaffold wording correction. Support: [Approval Scope](README.md#approval-scope) and scaffold Scope and Constraints / Decisions and Authorization.
4. Unrelated active work and dirty files. Expected decision: Preserve both; require explicit disposition before replacing incompatible active work and continue independent safe investigation. Result: Passed. Support: [Start Here](README.md#start-here), [Starting a Workstream](workstreams/README.md#starting-a-workstream), and scaffold initialization comment.
5. Clean GitHub snapshot versus dirty laptop patch. Expected decision: Limit Web review to inspected material; request the missing focused diff/dependencies and explicitly identify relevant untracked files. A reported summary is not independent patch verification. Result: Passed. Support: [Human-Coordinated Collaboration](README.md#human-coordinated-collaboration) and [Handoff and resumption](README.md#handoff-and-resumption).
6. Resumed session with intervening changes. Expected decision: Compare snapshot and authorization with actual state; revalidate affected evidence without repeating unrelated work or renewing unchanged scoped authorization. Result: Passed. Support: [Handoff and resumption](README.md#handoff-and-resumption).
7. Automated success and remaining gates. Expected decision: User checks remain pending until user evidence; commit, push, PR creation/merge, deployment, and live operations remain individually unauthorized unless named in actual authorization. Result: Passed. Support: [Verification and User Validation](README.md#verification-and-user-validation), [Approval Scope](README.md#approval-scope), and scaffold Delivery Permissions.
8. Timed-out wait with unknown completion. Expected decision: Mark `Pending`/unknown, inspect or reconnect to the existing process, and do not claim pass/failure or duplicate/terminate solely due to a wait ending. Result: Passed. Support: [Verification and User Validation](README.md#verification-and-user-validation).
9. Accepted non-release work versus unfinished release. Expected decision: Successfully accepted work whose target needs no release can close as `Completed`; a required unverified release cannot. Archival preserves the terminal outcome. Result: Passed. Support: [Workstream Statuses and Gates](README.md#workstream-statuses-and-gates), [Closing and Archiving](README.md#closing-and-archiving-a-workstream), and [Before Archiving](workstreams/README.md#before-archiving).
10. Framework upgrade in an existing application. Expected decision: Inspect and merge policy while preserving local instructions, approved work, memory, dirty files, and archives. Do not import upstream state/authority or infer application-development permission. Result: Passed. Support: root [Adopt or Update the Framework](../README.md#adopt-or-update-the-framework) and [Existing project or framework upgrade](../README.md#existing-project-or-framework-upgrade).

### User Validation Checklist

- [ ] Review canonical authority, collaboration, direct execution, and partial-approval wording against the intended human-coordinated workflow.
- [ ] Review the scaffold and the `Completed`/`Released` archive distinction using the scenario evidence.
- [ ] Review new/existing-project adoption guidance and confirm local state and deliberate constraints are protected.
- [ ] Accept the local patch or identify corrections; any later delivery actions remain a separate decision.

## Delivery Permissions

- Commit: Unapproved; excluded by this request.
- Push: Unapproved; excluded by this request.
- Pull-request creation: Unapproved; excluded by this request.
- Pull-request merge: Unapproved; excluded by this request.
- Deployment: Unapproved; excluded by this request.
- Live-data operations: Unapproved; excluded by this request.
- Destructive cleanup: Unapproved; excluded by this request.
- Production promotion: Unapproved; excluded by this request.

## Progress Log

- 2026-09-06: Completed starting-state investigation and opened both official references. Confirmed the reported inconsistencies still exist at the exact reference base. Recorded plan r1 and the user's scoped direct-execution authorization before patching policy.
- 2026-09-06: Implemented canonical amendments and aligned the entry points, adoption guide, archive conventions, and flexible scaffold. Kept all seven other tracked files intact. Proceeding to repository checks and document-level scenario review.
- 2026-09-06: Reconciled the independent review's single scaffold correction. Final repository consistency and whitespace checks passed, including the evidence update; all ten document-level scenarios support the requested decisions. Prepared the final review handoff at the requested stopping gate; user checks remain pending.

## Deviations and Blockers

No scope departures or remaining blockers. The scaffold correction is within plan r1. No additional files, tooling, application changes, or delivery actions were needed.

## Delivery Summary

Review material: F1 is the complete local six-file diff against the recorded base, with an empty staged diff and no untracked files. A reviewer using only the clean GitHub base has not reviewed this amendment. Share a sanitized diff plus the relevant unchanged dependencies as needed; no commit or push is necessary.

Changed files and outcomes:

- `docs/README.md`: Canonical authority, human/assistant responsibilities, snapshot handoffs/resumption, scoped and partial approval, proportionate verification/process uncertainty, terminal outcomes, attribution, and dated source adaptation.
- `AGENTS.md`: Shorter actionable agent entry point with essential constraints and canonical references.
- Root `README.md`: Human orientation and deliberate adoption/upgrade that preserves application state and permissions.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md`: Snapshot and approval provenance, one current metadata block and implementation authorization, flexible phases, focused verification, and distinct delivery permissions.
- `docs/workstreams/README.md`: Safe initialization and archive conventions preserving `Completed` or another truthful terminal outcome.
- `docs/progress.md`: The actual plan, user-request authorization, evidence, scenario decisions, pending user checklist, and review handoff.

The six-file boundary and the framework's small documentation surface are preserved. No invented context, roadmap commitments, or accepted debt were added; the other seven tracked files are unchanged. Checks and limitations are recorded above. Remaining decisions belong to the user: accept the local patch or request corrections, then separately decide whether any later delivery action is wanted. Rollback is limited to reviewing and reversing this patch's hunks while preserving intervening work.

No commit, push, PR creation/merge, branch switch, worktree creation, deployment, live operation, destructive cleanup, Git identity/signing/credential change, global configuration/instruction change, installed-skill edit, or downstream application edit was performed. No user acceptance, release, or archival is claimed. The current gate and next owner remain authoritative in the metadata above.
