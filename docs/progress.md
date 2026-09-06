# Active workstream: human-coordinated-agentic-development

Workstream class: Standard

Risk: Medium; these narrow documentation corrections affect interpretation of evidence, archive references, instruction activation, and actor attribution.

Status: Ready for user validation

Current gate: Ready for user validation

Next action: User reviews F2 using the four-item checklist below and accepts that artifact or requests corrections. Acceptance of F1 remains unresolved; no later delivery action is authorized.

Repository: edwardansberg/progress-driven-sdlc (upstream framework only)

Branch: main

Original implementation base: dfe3667ea37b41ba6de948ca1253930a23d7d093

Follow-up base and last inspected HEAD: 86554d0f2be7c6b947031fc3e27c1d6f0d7a63da

Checkout observation: R2-final, 2026-09-06, Codex in this task; six unstaged modified files, empty index diff, no untracked files. The clean R2-start observation is retained under Context and Evidence.

Snapshot: F2, the complete six-file local correction diff against the follow-up base, as inspected at R2-final; distinct from historical F1 and the published prior amendment. Files are identified in the r2 handoff below.

Publication observation: 2026-09-06, Codex read-only `git ls-remote origin refs/heads/main` returned 86554d0f2be7c6b947031fc3e27c1d6f0d7a63da. This independently corroborates the user's publication report; it does not establish acceptance, prior permissions, or the actor who invoked Git.

Plan revision: r2, 2026-09-06; r1/F1 history retained below

Started: 2026-09-06

Last substantive update: 2026-09-06 by Codex, r2 verification and handoff

Delivery target: Local uncommitted F2 correction patch for user review; acceptance, release, and archival remain outside this task's stopping gate.

Workflow: [Documentation Workflow](README.md)

## Follow-up r2 — Post-publication Corrections

### Context and Evidence

Verified current behavior: At R2-start on 2026-09-06, Codex observed a clean checkout exactly matching the user-reviewed published commit: no staged, unstaged, untracked, or pre-existing changes. All 13 tracked Markdown files and applicable guidance were read; no additional repository-owned skills or agent instructions were found, and ancestor/global instruction checks found no additional files. The existing workstream was compatible and unresolved; it is resumed here without a branch or history change.

The following findings were independently reproduced in that checkout:

- Metadata conflates the original base and F1 handoff with current state; the prior checklist is still unchecked. F1 remains valid historical reported evidence, not a claim about today's dirty state.
- Archive conventions omit relocation of links and maintained historical references. An in-memory URI check shows that unchanged `README.md#approval-scope` would target the archive directory's README instead of `docs/README.md`. The archive tree contains only its index, so no existing broken archived workstream was found.
- Adoption does not distinguish amended files from instructions already loaded in a session. The [official Codex reference](https://developers.openai.com/codex/guides/agents-md), opened 2026-09-06, redirects to ChatGPT Learn and documents instruction-chain construction at run/session startup and restart for stale guidance. This supports a safeguard; no live loading failure was demonstrated.
- `AGENTS.md` applies the author instruction to any authorized commit, broader than canonical policy's Codex-created-commit condition.

Chosen target behavior: Distinguish base, dated/source-attributed observations, publication, and artifact-specific evidence; preserve archive targets and historical references; clarify instruction activation; restore actor-specific attribution. Keep existing classes, approval boundaries, lifecycle, and file surface.

Inference requiring validation: Document-level consistency is supported by the checks below. Actual instruction loading and live agent compliance remain unverified; the safeguard is not a claim of a reproduced runtime failure.

Open decision: User acceptance of F1 was not supplied and is not inferred from publication. F2 acceptance remains pending; the user owns both any acceptance decision and any later delivery authorization.

### Scope, Plan, and Authority

Authority: The user's request "Progress-Driven SDLC: focused post-publication corrections," section "Authority and stopping gate," received 2026-09-06, explicitly authorizes this bounded local investigation, written plan, corrections, verification, and documentation upkeep. Plan r2 implements that request; it is not independently user-approved or self-authorizing. The supplied Web review is input, not authorization or a rerun of local checks.

Included: The four corrections in the six expected files: `docs/README.md`, `AGENTS.md`, root `README.md`, `docs/workstreams/WORKSTREAM_TEMPLATE.md`, `docs/workstreams/README.md`, and this workstream.

Excluded: Staging, commits, pushes, PR creation/merge, branch changes, worktrees, deployment, live-data operations, destructive cleanup, history rewriting, Git identity/signing/credential changes, global instructions/configuration, installed skills, nested agent/API evaluations, downstream repositories, new permanent files/tooling, and edits to context, roadmap, debt, or archives.

Acceptance criteria:

- F1, published commit, and F2 observations remain distinct; evidence and acceptance identify their artifact and source. Metadata does not promise to name its own future containing commit.
- Archive guidance preserves link/image/reference-style destinations and fragments, validates from the destination, and redirects historical references without redirecting active navigation or overwriting an archive.
- Activation guidance remains provider-neutral, uses the official source for Codex details, retains explicit canonical-policy reading, and claims no automatic loading or fresh-session evaluation.
- Only Codex-created commits receive the applicable Codex author rule; other actors retain their adopted policy. No attribution or history changes occur.
- All six follow-up scenarios have supported decisions; available checks pass; user-owned checks remain pending at `Ready for user validation`.

Implementation and verification plan:

- [x] Inspect actual state, required documents, publication evidence, and official guidance; reproduce findings and record r2 before normative edits.
- [x] Make small canonical, entry-point, adoption, scaffold, and archive refinements; preserve identifiable r1/F1 evidence.
- [x] Simulate archive relocation in memory using independently specified targets, including fragments, images/reference definitions, self-links, code/path-label exclusions, and historical versus active inbound references.
- [x] Inspect all changed hunks, links/anchors, metadata, policy consistency, hygiene, and staged/untracked state; run `git diff --check` and any existing applicable repository checks.
- [x] Record six document-level scenario decisions and actual outcomes, then prepare the F2 handoff at the authorized stopping gate.

Risks and rollback: Historical reports could be mistaken for current facts; label r1/F1 as history and give F2 its own observation. Preserve unaffected evidence only with its original source/scope. Rollback, if requested later, is limited to this follow-up's hunks against 86554d0f2be7c6b947031fc3e27c1d6f0d7a63da, preserving the published r1 patch and intervening unrelated work. Migration, rollout, and runtime observability are not applicable to this local documentation task.

### Verification

The following checks were performed by Codex in this r2 task on 2026-09-06. They concern F2 and the specified observations, not a rerun of the earlier r1 agent review. The final evidence update passed the focused link/diff/state checks: 13 documents, 93 local links, 58 anchor targets, six expected unstaged files, and zero inspection issues. The final gate/owner annotation changes no policy, links, or evidence basis.

Check: Local state, published reference, and complete follow-up diff.

Basis: `git rev-parse --show-toplevel`, `git branch --show-current`, `git rev-parse HEAD`, `git status --porcelain=v1 --untracked-files=all`, full `git diff`, `git diff --cached`, `git ls-files --others --exclude-standard`, `git diff --name-status dfe3667ea37b41ba6de948ca1253930a23d7d093 86554d0f2be7c6b947031fc3e27c1d6f0d7a63da`, and read-only `git ls-remote origin refs/heads/main` after sanitized remote-identity inspection.

Scope: R2-start and local F2; publication observation at the date above.

Result: Passed. Local branch/HEAD match the reviewed published snapshot. The correction diff affects only the six expected files; index and untracked inventory are empty. All seven other tracked documents remain intact. The published commit contains the prior six-file amendment, independent of the earlier local dirty-state report.

Limitations: Publication does not establish prior acceptance, permissions, or command actor. F1 evidence retains its original reported source/scope. No new specialist or live agent evaluation was performed.

Check: Archive relocation and maintained-reference intent.

Basis: One-off inline PowerShell, entirely in memory, with independently named target files/fragments. Eight inline/image/reference-definition/self/external destinations were resolved at source and archive locations; a negative control copied destinations unchanged. Protected code/path labels and separate delivered-work/current-work inbound links were also checked. Actual progress links were simulated from the nested archive against canonical-policy, root-orientation, and archive-guide targets.

Scope: F2 archive procedure; virtual `docs/progress.md` and `docs/workstreams/archive/2026/example.md`, with real target headings and one virtual image. No maintained fixtures or archive copies were created.

Result: Passed. Twenty positive fixture assertions; the unchanged-copy control reproduced six displaced relative destinations. Corrected paths preserved file targets and fragments, reference definitions, images, self-links, and external URLs. Historical inbound references followed the archived work; active navigation stayed on progress. After adding the verification/handoff narrative, a focused final simulation validated all 33 relative progress links against their intended files/fragments; the unchanged fixed fixtures were not rerun.

Limitations: Document-level path simulation, not a general Markdown rewriting tool, actual closure, or live agent evaluation. The archive still contains only its index; no broken existing historical workstream was alleged or repaired.

Check: Link/anchor integrity, scope, metadata, hygiene, and available repository checks.

Basis: Read-only inline PowerShell inventory via `git ls-files -- '*.md'`, resolution of inline/image/reference-style targets and heading fragments outside code/comments, current-metadata counts, expected changed paths, and table/conflict-marker/credential/personal-detail pattern inspection; manual changed-hunk review for meaning and duplication. `git diff --check` and `git diff --cached --check`; required runbook reads and `git ls-files -- '*.yml' '*.yaml' 'package.json' 'pyproject.toml' 'Makefile' '*test*' '*lint*'` to discover existing checks.

Scope: All 13 tracked Markdown documents for links, six changed files for follow-up hygiene, and F2 versus the published base for semantic review.

Result: Passed. No missing targets/anchors, unexpected files, competing current metadata, table additions, conflict markers, or sensitive-detail findings. Both Git whitespace checks exited 0 without diagnostics. No executable test/lint/build/CI checks are defined; no pre-existing check failures were found. Classes, partial/scoped approval, user validation, and terminal outcomes remain unchanged.

Limitations: Focused document inspection, not comprehensive secret detection or runtime testing. The current instruction-discovery reference was opened; unchanged external sources and earlier F1 checks are not reported as re-fetched or rerun. No permanent tooling was added.

#### Follow-up Scenario Walkthroughs

Check: Six requested post-publication scenarios.

Basis: The user's independently specified expected decisions and direct reading of the supporting sections below, with the archive simulation as additional evidence.

Scope: F2 written contract; document-level verification only.

Result: Passed, six of six supported; no remaining contradiction found.

Limitations: No user acceptance or live instruction-loading/compliance result is implied.

1. Publication after an uncommitted handoff. Expected: Distinguish historical F1, observed publication, and current F2, leaving acceptance unresolved and command actor unknown. Result: Passed. Support: [Handoff and resumption](README.md#handoff-and-resumption) and this workstream's dated checkout/publication observations and historical preface.
2. Same-scope correction after review. Expected: Retain valid evidence with its artifact/source, return affected user checks to Pending, and rerun relevant checks without blanket implementation reapproval or a future-commit-hash cycle. Result: Passed. Support: [Handoff and resumption](README.md#handoff-and-resumption), [Approval Scope](README.md#approval-scope), and the scaffold's Last inspected HEAD / verification prompts.
3. Nested archival and progress reuse. Expected: Rebase links/images/reference destinations while retaining fragments and workstream identity; redirect historical evidence references, retain active navigation, and avoid occupied archive paths. Result: Passed by document review and the in-memory simulation. Support: [Preserve references at closure](workstreams/README.md#preserve-references-at-closure) and [Closing and Archiving](README.md#closing-and-archiving-a-workstream).
4. Instructions edited during a session. Expected: Separate amended text, documented discovery, and actual observed loading; preserve handoff before any relevant documented restart, with no automatic interruption or evaluation. Result: Passed for the documentation; fresh-session behavior remains unperformed. Support: [Activating updated guidance](../README.md#activating-updated-guidance), [Instruction Authority and Evidence](README.md#instruction-authority-and-evidence), and [Source Note](README.md#source-note).
5. Codex versus human-created commits. Expected: Only Codex-created commits use its applicable author policy; other actors retain their adopted policy and identities. Result: Passed by reading both attribution sections; no Git identity/history changes performed or command actor inferred. Support: [Commit Attribution](README.md#commit-attribution) and AGENTS.md, Commit Attribution.
6. Existing planning and delivery gates. Expected: An unapproved standard feature stops; explicit scoped direct execution and partial approvals cover only their scope; green checks neither authorize delivery nor pass user checks. Result: Passed. Support: [Standard workstream](README.md#standard-workstream), [Approval Scope](README.md#approval-scope), and [Verification and User Validation](README.md#verification-and-user-validation).

Fresh-session behavior check: Skipped; this task expressly excludes nested agent/API evaluations. Reading the updated files and official documentation does not demonstrate automatic instruction loading. Any later setup check requires evidence from the intended environment and is not required to finish this documentation patch.

### User Review Checklist

- [ ] Review F1/publication/F2 observation and evidence distinctions; identify any artifact-specific acceptance you intend to provide.
- [ ] Review archive relocation and historical-reference preservation, including the simulation results.
- [ ] Review activation guidance and its unperformed fresh-session check limitation.
- [ ] Review actor-specific attribution and confirm or request corrections to F2.

All F1 user checks below remain pending; publication is not a substitute for their evidence. F2 changes affect these four review subjects, so no prior check is carried forward as their acceptance.

### Delivery Permissions and Handoff

- Staging: Unapproved; excluded for r2.
- Commit: Unapproved; excluded for r2.
- Push: Unapproved; excluded for r2.
- PR creation: Unapproved; excluded for r2.
- PR merge: Unapproved; excluded for r2.
- Deployment: Unapproved; excluded for r2.
- Live-data operations: Unapproved; excluded for r2.
- Destructive cleanup: Unapproved; excluded for r2.
- Production promotion: Unapproved; excluded for r2.

No prior publication retroactively authorizes this task. F2 is the complete six-file local diff against the follow-up base, with no staged or untracked material. It is separate from both historical F1 and the published prior amendment.

Changed files: `docs/README.md` separates observations/evidence and links the activation/archive details; `AGENTS.md` restores actor-specific attribution; root `README.md` explains instruction activation; `docs/workstreams/WORKSTREAM_TEMPLATE.md` distinguishes base, inspected HEAD, observation, and evidence scope; `docs/workstreams/README.md` preserves archive and maintained-reference targets; this workstream records r2 and retains r1/F1 history.

All four wording/procedure gaps were reproduced and corrected within the expected file set. Neither an existing broken archive nor a live instruction-loading failure was demonstrated. F1 acceptance remains unresolved; F2 review is pending using the four-item checklist above. Rollback, if requested, is limited to r2's local hunks against the published base, preserving the earlier amendment and any later unrelated work.

During this r2 task, Codex performed no staging, commit, push, PR action, branch/worktree change, deployment, live-data operation, destructive cleanup, history rewrite, Git identity/signing/credential change, global instruction/configuration or installed-skill edit, nested agent/API evaluation, or downstream edit. No workstream was accepted, released, or archived. The authoritative current gate, observation, and next owner are in the metadata above; no blocker or scope departure remains.

## Historical r1/F1 Record

Capture/source: Codex's r1 handoff on 2026-09-06 described F1 as six unstaged files against the original implementation base, with no staged/untracked files. It recorded `Ready for user validation` and user review as next action. The record is also preserved in [the published progress document at 86554d0](https://github.com/edwardansberg/progress-driven-sdlc/blob/86554d0f2be7c6b947031fc3e27c1d6f0d7a63da/docs/progress.md).

The sections below retain that earlier plan, decisions, results, and pending checklist. References to "this task," "the base," or "F1" in them concern the r1 handoff, not r2 or subsequent publication. Their document links are navigation; use the pinned published record to inspect the historical material. Earlier checks are not claimed as rerun for F2.

### Requested Outcome

Improve the existing framework for a human coordinating a planning/review assistant with a coding agent. Keep canonical policy, one active workstream, explicit gates, evidence-based memory, and a small provider-neutral documentation surface.

### Definition of Done

The bounded patch is implemented and available checks are recorded, all ten requested contract scenarios have document-level walkthroughs, and a focused review handoff is prepared. Stop at `Ready for user validation` with user checks pending. Acceptance, release, and archival are outside this task's stopping gate.

### Context and Evidence

#### Verified current behavior

The following findings describe the initial review base. The implemented local amendment and its evidence are recorded under Verification and Delivery Summary.

- Local Git inspection on 2026-09-06 identifies the requested repository on `main` at the supplied reference commit. Initial staged, unstaged, and untracked sets are empty. Sanitized remote inspection confirms the GitHub repository identity; no remote synchronization was performed.
- Read all 13 tracked Markdown files, including root and directory guidance, the complete canonical policy and progress file, singleton memory, and archive/scaffold conventions. Root `AGENTS.md` is the only repository-owned agent instruction; no applicable ancestor/global override, additional repository instructions, or repository-owned skills were found.
- Initial `docs/progress.md` says `No active workstream`; there is no incompatible active effort. Context and roadmap are uninitialized, debt has no accepted items, and no closed workstream snapshots exist. These are starter placeholders, not an application's verified state.
- The tracked inventory contains documentation only: no application code, migrations, dependency manifests, CI configuration, or repository test commands. Operations and security indexes define generic conventions only.
- At the review base, root README calls agent rules enforceable; canonical evidence ordering conflates different states. No snapshot-aware Web/human/coding-agent handoff contract or verification record shape exists.
- Default approval gates and the quick-change exclusions already exist and should be preserved. Unconditional setup instructions in root README, canonical policy, progress setup, archive guide, and scaffold conflict with the existing explicit direct-execution exception in `AGENTS.md`. Partial approval and approval provenance are underspecified.
- Canonical closure mentions completion without deployment, but status flow ends in `Released -> Archived` and archive instructions omit a successful non-release outcome. The scaffold combines push/PR approval, duplicates plan/implementation approval and next action, and forces three phases.
- Both requested official references were opened on 2026-09-06. The model guide's prompting sections discuss initiative, instruction conflicts, readable output, delegation, and proportionate testing. The instruction-discovery reference redirects to ChatGPT Learn and describes Codex-specific discovery, including overrides. Source links and selective adaptation are recorded in the [canonical source note](README.md#source-note).

#### Chosen target behavior

The user's request selects a provider-neutral amendment in the six named existing files: precise scoped authorization, snapshot-aware handoffs and resumption, proportionate verification, a `Completed` terminal outcome, a streamlined scaffold, and adoption that preserves application state. Written implementation is present in F1; future agent behavior is not established by the patch.

#### Inference requiring validation

The document-level consistency claim is supported by the ten walkthroughs below. Whether agents follow the contract reliably in practice remains unverified; live agent evaluations are outside this patch's scope.

#### Open decision

No implementation choice blocks the authorized patch. User acceptance remains pending at the stopping gate. Any later delivery action needs its own explicit scope.

### Relevant System Map

- `docs/README.md`: canonical policy, evidence, collaboration, verification, and lifecycle.
- `AGENTS.md` and root `README.md`: agent entry point and human orientation/adoption.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md` and `docs/workstreams/README.md`: single scaffold and local archive conventions.
- `docs/progress.md`: this actual workstream, authorization, results, and handoff.
- Other singleton documents, runbook indexes, and history remain intact unless a directly necessary consistency correction is found.

### Scope

Included: Amend the six named files, inspect the full local diff and relevant untracked material, verify links and policy consistency, record ten scenario walkthroughs, and prepare review and rollback guidance.

Excluded: Commits, pushes, PR creation or merge, branch switching, new worktrees, deployment, live migration or other live operations, destructive cleanup, repository/global identity or signing changes, credential changes, personal/global instructions or installed skills, downstream repositories, new permanent files, CI, dependencies, hooks, validators, evaluation harnesses, or model/runtime configuration.

### Constraints and Assumptions

Preserve existing Git attribution, unrelated changes, historical material, and deliberate adopting-project constraints. Use no Markdown tables. Keep policy in its canonical file and task state here. Do not invent application context, roadmap commitments, or accepted debt. No application or live environment is involved in this documentation patch.

### Decisions and Authorization

1. Direct execution: The user explicitly authorized investigation, an evidence-backed plan, local implementation, verification, and review handoff in the request titled "Patch Progress-Driven SDLC for human-coordinated agentic development," section "Execution authority for this task," received 2026-09-06. Plan r1 implements that bounded request; it is not a separately user-approved plan and does not grant itself authority. The framework's normal plan-approval requirement remains unchanged.
2. File placement: Consolidate reusable collaboration, authority, verification, and lifecycle rules in canonical policy; keep the scaffold proportional and entry points short. No new status register or template is needed.
3. Source adaptation: Apply prompting guidance only inside the user's authorized scope. Do not adopt example permission to create worktrees/PRs or API migration advice. Tool-specific discovery remains an official-documentation reference.
4. Memory: Keep this real framework-maintenance workstream active through user review. Preserve uninitialized application-memory placeholders and explain their adoption boundary in root README.
5. Review correction: Clarified proposed/approved/pending included scope in the scaffold after independent review. This is a wording correction within r1, not new behavior or expanded authorization. Removed the optional concurrency-dashboard suggestion to retain the requested single active workstream; allowed justified non-environment release evidence for artifact targets while preserving verified-release requirements.

### Acceptance Criteria

- Canonical policy distinguishes instruction authority, factual evidence, proposals, scoped user authorization, and tool permissions without claiming universal tool precedence or mechanical enforcement.
- Collaboration and resumption identify snapshots, dirty/untracked material, evidence provenance, decisions, and next owner without requiring commits, exports, multiple agents, or extra registers.
- Quick/standard/high-risk decisions, partial approval, direct execution, and separate delivery permissions are consistent across all entry points and setup comments.
- Verification uses the requested evidence labels and Check/Basis/Scope/Result/Limitations record; unknown process completion, skipped checks, and user validation remain truthful.
- `Completed`, `Released`, and archival retain distinct, consistent meanings. The sole scaffold has one current status/gate/next action, one implementation authorization record, distinct delivery permissions, and flexible phases.
- New and existing adoption preserves local constraints, active state, and archives. All ten requested scenario decisions have supporting sections and no unresolved contradiction.
- Only the bounded local documentation patch remains, with available checks passed and user validation pending.

### Implementation Plan

#### Phase 1 — Policy, entry points, and scaffold

- [x] Inspect current checkout, required documents, instruction sources, history, and official references; record plan r1 and user authorization before substantive edits.
- [x] Amend canonical policy for authority, collaboration, approval, verification, lifecycle, and selective source guidance.
- [x] Align agent entry point, adoption instructions, archive conventions, and scaffold; remove overlapping or contradictory rules.

Acceptance: The requested contract is expressed in the six existing files without expanding task permissions or adding permanent artifacts.

Rollback: Review and reverse only this task's uncommitted hunks against the recorded base, preserving any intervening work.

#### Phase 2 — Verification and review handoff

- [x] Inspect the full staged/unstaged diff and relevant untracked material; check links/anchors, paths, setup comments, statuses, duplication, hygiene, and table additions.
- [x] Run existing applicable checks and `git diff --check`; record actual outcomes and limitations.
- [x] Walk through all ten requested scenarios against final policy and reconcile an independent bounded review if used.
- [x] Update this workstream and prepare the user checklist, rollback considerations, and snapshot-aware handoff at the requested stopping gate.

Acceptance: Available checks and document walkthroughs are recorded after final substantive edits. User checks stay pending.

### Risks and Controls

- Permission drift: Review approval and lifecycle scenarios against the user's explicit boundaries and preserve the original quick-change exclusions and commit attribution.
- Duplicated authority: Keep detailed policy canonical, link entry points to it, and use one current metadata block in the scaffold/workstream.
- Overstated evidence: Scope claims to the checkout or supplied sources; document walkthroughs do not prove future agent behavior or Web inspection of a laptop patch.
- Adoption data loss: Replace blind-copy onboarding with deliberate initialization/merge guidance that preserves existing state and constraints.

### Migration, Rollout, Observability, and Rollback

Migration, rollout, and runtime observability: Not applicable; only local Markdown changes, with no application or environment target.

Rollback: The initial checkout is clean at the recorded base. If the user rejects the patch, review and reverse only its six-file diff, preserve later unrelated edits, and record the disposition before any future closure. No rollback or cleanup is performed by this task.

Destructive effects: None authorized.

### Verification

Checks below were performed by the primary coding agent on 2026-09-06 after normative edits, unless another source is identified. The final evidence update also passed the consistency/whitespace checks: 13 Markdown files, 79 local links, 43 anchor targets, six expected changed paths, and zero inspection issues. The final gate/owner update changes no policy or evidence basis.

#### Repository Scope and Diff

Check: Repository identity, complete patch, unchanged surrounding files, and staged/untracked material.

Basis: `git branch --show-current`, `git rev-parse HEAD`, `git status --porcelain=v1 --untracked-files=all`, `git diff HEAD --numstat`, complete `git diff` for all six changed files, `git diff --cached`, and `git ls-files --others --exclude-standard`; manual reading of the resulting patch.

Scope: Local F1 checkout at the recorded base; primary agent inspection.

Result: Passed. Branch/HEAD unchanged; six named files modified and unstaged; no staged or untracked material. The seven other tracked Markdown files remain unchanged. No new permanent files or downstream changes were made.

Limitations: This verifies the local checkout, not a remote branch or deployed environment. A Web reviewer must receive this diff and relevant files to review F1.

#### Links, Paths, and Hygiene

Check: Markdown targets/anchors, metadata uniqueness, patch boundaries, tables, conflict markers, and accidental sensitive or personal details.

Basis: One-off read-only inline PowerShell inspection over `git ls-files -- '*.md'`: resolve Markdown link targets relative to each file; compare fragments with normalized headings; inspect changed paths from `git diff HEAD --name-only`; count status/gate/next-action metadata; scan for table/conflict-marker, private-key/token, credential-URL, personal-path, and IP-address patterns. Manual diff review covers generic examples and policy semantics.

Scope: All 13 tracked Markdown files for local links; six changed files for patch hygiene; progress and scaffold for current-metadata uniqueness. Official external references were opened separately and their cited headings inspected.

Result: Passed. No missing local paths/anchors, unexpected changed files, duplicate current metadata, table additions, conflict markers, or sensitive/personal-detail findings. Illustrative paths in handoff/archive examples are explicitly generic data, not claims that those files exist in this repository.

Limitations: This focused inspection is not a general Markdown parser or comprehensive secret detector. External links were checked through the source reads, not a crawler. No validator or tooling was added to the repository.

#### Whitespace and Existing Checks

Check: Git whitespace checks and discovery of applicable project checks.

Basis: `git diff --check` and `git diff --cached --check`; tracked-file inventory, required document/runbook reads, and `git ls-files -- '*.yml' '*.yaml' 'package.json' 'pyproject.toml' 'Makefile' '*test*' '*lint*'`.

Scope: Local six-file patch and index after normative edits.

Result: Passed. Both Git whitespace checks exited 0 with no diagnostics. Inventory and runbook inspection found no existing executable test/lint/build/CI checks to run; no pre-existing check failure was identified.

Limitations: Application builds, runtime checks, and live agent evaluations are Skipped as not applicable to this documentation-only repository/task. This is not evidence of application behavior or model compliance.

#### Policy and Independent Review

Check: Entry points, setup comments, policy duplication, lifecycle, authorization, and source adaptation.

Basis: Complete diff and unchanged directory/memory guidance; `rg -n 'TEMPLATE SETUP|REUSABLE SCAFFOLD|Awaiting plan approval|Push or pull-request|agent enforcement|makes the rules enforceable|active/<slug>' --glob '*.md'`; primary-agent review plus the read-only specialist `contract_review` report supplied in this task.

Scope: Normative F1 documents. The specialist reviewed the six-file diff before final evidence/metadata updates and independently confirmed branch/HEAD and dirty state.

Result: Passed after one correction. The specialist identified the scaffold's proposed-scope ambiguity; the primary agent changed Included to distinguish proposed, approved, and pending portions, then inspected the correction. No remaining contradiction was found. Default gates, quick exclusions, attribution, and one active workstream remain intact. Detailed attribution moved to canonical policy with a concise agent reference.

Limitations: Specialist conclusions are supplied review evidence. The primary agent independently read and reconciled them; the specialist did not independently verify the initial clean state or official-source contents. Neither review is user acceptance or a live agent evaluation.

#### Scenario Walkthroughs

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

#### User Validation Checklist

- [ ] Review canonical authority, collaboration, direct execution, and partial-approval wording against the intended human-coordinated workflow.
- [ ] Review the scaffold and the `Completed`/`Released` archive distinction using the scenario evidence.
- [ ] Review new/existing-project adoption guidance and confirm local state and deliberate constraints are protected.
- [ ] Accept the local patch or identify corrections; any later delivery actions remain a separate decision.

### Delivery Permissions

- Commit: Unapproved; excluded by this request.
- Push: Unapproved; excluded by this request.
- Pull-request creation: Unapproved; excluded by this request.
- Pull-request merge: Unapproved; excluded by this request.
- Deployment: Unapproved; excluded by this request.
- Live-data operations: Unapproved; excluded by this request.
- Destructive cleanup: Unapproved; excluded by this request.
- Production promotion: Unapproved; excluded by this request.

### Progress Log

- 2026-09-06: Completed starting-state investigation and opened both official references. Confirmed the reported inconsistencies still exist at the exact reference base. Recorded plan r1 and the user's scoped direct-execution authorization before patching policy.
- 2026-09-06: Implemented canonical amendments and aligned the entry points, adoption guide, archive conventions, and flexible scaffold. Kept all seven other tracked files intact. Proceeding to repository checks and document-level scenario review.
- 2026-09-06: Reconciled the independent review's single scaffold correction. Final repository consistency and whitespace checks passed, including the evidence update; all ten document-level scenarios support the requested decisions. Prepared the final review handoff at the requested stopping gate; user checks remain pending.

### Deviations and Blockers

No scope departures or remaining blockers. The scaffold correction is within plan r1. No additional files, tooling, application changes, or delivery actions were needed.

### Delivery Summary

Review material: F1 is the complete local six-file diff against the recorded base, with an empty staged diff and no untracked files. A reviewer using only the clean GitHub base has not reviewed this amendment. Share a sanitized diff plus the relevant unchanged dependencies as needed; no commit or push is necessary.

Changed files and outcomes:

- `docs/README.md`: Canonical authority, human/assistant responsibilities, snapshot handoffs/resumption, scoped and partial approval, proportionate verification/process uncertainty, terminal outcomes, attribution, and dated source adaptation.
- `AGENTS.md`: Shorter actionable agent entry point with essential constraints and canonical references.
- Root `README.md`: Human orientation and deliberate adoption/upgrade that preserves application state and permissions.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md`: Snapshot and approval provenance, one current metadata block and implementation authorization, flexible phases, focused verification, and distinct delivery permissions.
- `docs/workstreams/README.md`: Safe initialization and archive conventions preserving `Completed` or another truthful terminal outcome.
- `docs/progress.md`: The actual plan, user-request authorization, evidence, scenario decisions, pending user checklist, and review handoff.

The six-file boundary and the framework's small documentation surface are preserved. No invented context, roadmap commitments, or accepted debt were added; the other seven tracked files are unchanged. Checks and limitations are recorded above. Remaining decisions belong to the user: accept the local patch or request corrections, then separately decide whether any later delivery action is wanted. Rollback is limited to reviewing and reversing this patch's hunks while preserving intervening work.

At the r1/F1 handoff, Codex reported performing no commit, push, PR creation/merge, branch switch, worktree creation, deployment, live operation, destructive cleanup, Git identity/signing/credential change, global configuration/instruction change, installed-skill edit, or downstream application edit during that task. It did not claim user acceptance, release, or archival. This actor/task-scoped report does not describe later publication or the current checkout.
