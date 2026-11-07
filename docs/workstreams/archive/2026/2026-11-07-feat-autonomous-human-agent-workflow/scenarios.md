# Static Scenario Review

Candidate: `751b14ab67351d6cc318bb553edeae6379285448`
Basis: [Invoked request, section 9](request.md#9-work-sequence-and-verification)
Observation: 2026-11-07; bounded agent review of committed files using `git show <candidate>:<path>`.
Method: Compare each hypothetical state with the candidate's stated next action, authority, gate and reading route. Links below locate the canonical sections as read at the pinned candidate; later edits do not update this evidence.
Result: Passed for the static routes below; no concrete contradiction found in these exercised cases.
Record verification: Passed scoped whitespace and all 41 local links/fragments against the exact candidate; 15 scenarios inspected.
Limitations: No application, live adoption, accessibility, remote failure, hook, deployment or crash experiment was performed. This is an agent's document walkthrough, not human usability evidence or proof of enforcement. It does not establish clean-context restart accuracy, before/after reading cost or release-tree neutrality; those require their separate evidence.

## 1. New business app with default publication

State: A business owner submits the kickoff prompt for a pickup-booking app; the inspected repository and origin are unambiguous, with no stricter agreement.

Expected next action: Investigate the existing process and smaller alternatives. Record the actual agreement, goal, criteria and bounded plan; create the authorized isolated branch and continue internal implementation/check cycles without another routine approval. If an app is justified, deliver its first working shell around a real workflow. Inspect and publish coherent in-scope increments under the agreement; stop at human validation, not acceptance or deployment.

Route: [Kickoff](../../../../../README.md#start-a-new-project), [agreement](../../../../README.md#standing-working-agreement), [packages](../../../../README.md#executable-work-packages), [first slice](../../../../ops/application-experience.md#first-working-slice).

Result: Passed (static). Submitted human instructions supply authority; merely possessing the starter does not. No app or publication was executed for this scenario.

## 2. Existing app with local-only rules, dirty work and occupied instructions

State: Adoption is requested in a product repository with an existing local-only agreement, dirty application files, local instructions and an occupied progress record whose ownership is uncertain.

Expected next action: Inspect target boundaries, instructions, Git state and authoritative records. Preserve dirty work and the stricter agreement; neither the imported defaults nor adoption text silently enables push. Pin the source and prepare a bounded migration map. Resolve uncertain occupied authority before replacement writes, keeping the proposal disposable if its normal destination would displace work. Continue independent permitted inspection; do not reset memory, rewrite the UI or introduce competing progress records.

Route: [Identify target](../../../../ops/adopt-framework.md#1-identify-the-target-before-writing), [safe adoption path](../../../../ops/adopt-framework.md#3-choose-the-safe-adoption-path), [target agreement](../../../../ops/adopt-framework.md#establish-the-target-working-agreement).

Result: Passed (static). Aligned same-source content needs no churn; missing previous provenance stays uncertain. No target migration, instruction activation or idempotence run was performed.

## 3. Small correction

State: The human requests one reversible spelling correction in an ordinary help paragraph; no security, contract or data behavior changes.

Expected next action: Inspect the affected text and existing work, make the scoped correction and run proportionate checks. Do not instantiate a substantial-work scaffold or demand another plan approval. Publish only under applicable existing authority and publication guards; the quick-change path supplies no missing delivery permission.

Route: [Quick change](../../../../README.md#quick-change), [publication](../../../../README.md#publication-and-recovery).

Result: Passed (static). The isolated-branch convention is scoped to substantial work; it does not cancel the quick-change exception. No fixture was needed to resolve this route.

## 4. Interrupted workstream

State: An authorized package has a verified remote checkpoint, newer dirty local work and a check whose completion is unknown after disconnection.

Expected next action: Preserve the agreement reference, complete dirty snapshot, completed steps, pending operation and next owner/action. On human-directed resumption inspect actual repository/remote state and recover valid authority without asking again for covered actions. Reconnect or inspect the pending check before retrying; recheck only affected evidence after changes. Do not infer a saved checkpoint after a crash or launch automatic unattended continuation.

Route: [Handoff and resumption](../../../../README.md#handoff-and-resumption), [verification](../../../../README.md#verification-and-user-validation), [publication recovery](../../../../README.md#publication-and-recovery).

Result: Passed (static). Unknown check completion remains Pending. Actual crash recovery and artifact availability were not tested.

## 5. Required verification fails

State: An export check finds that quoted names become extra columns; simple-name checks pass.

Expected next action: Record the failing scope and consequence, retain Failed and continue authorized repair/check cycles. Remain Implementing; do not claim readiness or successful closeout. Any policy-permitted unfinished recovery checkpoint must expose failed/pending checks and imply no acceptance.

Route: [Verification](../../../../README.md#verification-and-user-validation), [publication checkpoints](../../../../README.md#publication-and-recovery), [fictional failure](../../../../ops/checkpoint-examples.md#failed-verification-explain-the-consequence).

Result: Passed (static). A waiver or unrelated pass cannot convert the failed requirement into a pass. The fictional export was not executed.

## 6. Published candidate awaits human acceptance

State: Relevant technical checks passed and source publication is verified; the business owner has not tried the review build, and deployment has no authority.

Expected next action: Set Ready for user validation, identify the exact candidate and meaningful check limits, and give the owner a concrete review task. Preserve acceptance as Pending. Do not infer approval from publication, silence or a milestone label; do not merge or deploy.

Route: [Statuses](../../../../README.md#workstream-statuses-and-gates), [briefing](../../../../README.md#checkpoint-briefing), [validation example](../../../../ops/checkpoint-examples.md#human-validation-ready-to-try).

Result: Passed (static). The documents distinguish implemented, checked, published, accepted and deployed outcomes. No human acceptance was simulated.

## 7. Accepted development with pending delivery

State: A human accepted an identified development candidate; an existing durable delivery record assigns an owner and production checks. Deployment remains pending.

Expected next action: Close development as Completed only after the applicable development gates are satisfied, preserve the full archive and delivery handoff, then derive a No active workstream briefing that retains the last outcome and pending-delivery reference. Production checks remain Pending and govern release acceptance. If the original acceptance gate requires hosted validation and the human has not reallocated it, keep work open instead.

Route: [Closing](../../../../README.md#closing-and-archiving-a-workstream), [development and delivery](../../../README.md#development-and-delivery), [accepted example](../../../../ops/checkpoint-examples.md#accepted-development-delivery-still-pending).

Result: Passed (static). No active development is compatible with pending delivery; it does not mean Released. No real archive or release record was changed.

## 8. API-only project

State: The authorized outcome is a library or API with no human-facing application UI.

Expected next action: Define the relevant commands/API behavior, results, error handling and observability. Use ordinary planning, verification and publication rules. Do not build a control-panel frontend or create a Project Blueprint because framework guidance mentions them.

Route: [Reading triggers](../../../../README.md#start-here), [application boundary](../../../../ops/application-experience.md#first-working-slice), [optional Blueprint](../../../../README.md#optional-project-blueprint).

Result: Passed (static). The core provides the headless boundary without requiring the full interaction guide for ordinary API work. No API runtime was tested.

## 9. Unrelated staged work

State: The authorized package is ready to commit, but the index already contains another actor's unrelated edit.

Expected next action: Inspect ownership and the complete proposed commit boundary. Include all publishable in-scope implementation and evidence while preserving the unrelated staged edit. If safe isolation is unavailable, stop that commit rather than include or unstage someone else's work without authority. Continue independent local work where safe.

Route: [Publication, steps 2–3](../../../../README.md#publication-and-recovery), [agreement](../../../../README.md#standing-working-agreement).

Result: Passed (static). The default publication convention has an explicit staged-work guard. No index mutation or Git fixture was performed.

## 10. Failed or uncertain push and compatible remote advancement

State: A permitted push fails or loses its acknowledgement. A subsequent read might show the intended object present, absent or a remotely advanced branch.

Expected next action: Inspect the actual remote before retrying. If it contains the intended commits, report that verified publication. If absent, establish the failure cause and recheck target, authority and effects before an ordinary retry. If advanced, reconcile ownership and compatible changes without overwriting others; stop affected publication on material conflict or missing authority. Never force, rewrite shared history or manufacture duplicate commits. Offline/authentication failure can leave publication blocked while independent local work proceeds; report the last verified checkpoint and local-only changes.

Route: [Publication recovery, steps 4–5](../../../../README.md#publication-and-recovery).

Result: Passed (static). Compatible advancement is not an automatic task-wide stop, and lost acknowledgement is not proof of failure. No network failure or remote branch change was triggered.

## 11. Unexpected deployment trigger

State: Inspection discovers that pushing the permitted development branch would now trigger an unapproved deployment or new spending.

Expected next action: Stop affected publication before triggering that effect; explain the concrete decision and resolve its authority. Continue safe independent local work. Do not disable controls, redirect the push or treat ordinary source-publication permission as deployment/spending authority.

Route: [Agreement exclusions](../../../../README.md#standing-working-agreement), [publication, step 1](../../../../README.md#publication-and-recovery).

Result: Passed (static). Changed hook/CI assumptions require renewed inspection even when ordinary push remains covered. No hook, CI run or deployment was invoked.

## 12. Material choice inside a longer package

State: After several authorized implementation/check cycles, booking logic reveals an undecided cancellation cutoff while independent layout work remains authorized.

Expected next action: Prepare the business alternatives, effects and recommendation; pause the dependent cutoff implementation for the human decision. Continue independent authorized work. Refine technical sequencing without weakening criteria or silently choosing business policy; record the eventual decision in its authoritative home. Do not turn every internal increment into a new approval gate.

Route: [Interaction](../../../../README.md#interaction-contract), [executable packages](../../../../README.md#executable-work-packages), [approval scope](../../../../README.md#approval-scope).

Result: Passed (static). Routine technical replanning and material business authorization remain distinct. No business decision was inferred from the fictional example.

## 13. Unsupported host permission

State: A repository agreement permits an action, but the current host/tool cannot perform it or forbids it.

Expected next action: Respect the host/tool boundary. Identify the blocked action, accessible control/source, practical effect and smallest viable next decision or external step. Preserve evidence and continue independent permitted work; repository text cannot create capabilities, bypass the control or prove success. Do not repeatedly seek a repository approval that cannot change the host limit.

Route: [Instruction authority](../../../../README.md#instruction-authority-and-evidence), [agreement limits](../../../../README.md#standing-working-agreement), [bootstrap limits](../../../../ops/adopt-framework.md#optional-session-bootstrap).

Result: Passed (static). The agreement explicitly remains subordinate to host/tool controls. No denied operation or permission escalation was attempted.

## 14. Stale summary, failed save and late publication result

State: progress.md represents an older state than detail, a new result arrives after saving, or the briefing/record-only publication fails.

Expected next action: Reconcile actual evidence and authority in detail before consequential action; never take the stale summary's broader permission. Save the matching briefing and reuse its visible text unchanged. A material late result requires refreshing both records. If saving is impossible, label the final message an unsaved briefing and disclose the mismatch. If later record delivery fails, distinguish the already verified implementation candidate from unpublished records and refresh the saved briefing when possible; do not chase its own future containing hash or claim successful synchronization.

Route: [Checkpoint briefing](../../../../README.md#checkpoint-briefing), [publication record delivery](../../../../README.md#publication-and-recovery).

Result: Passed (static). Recovery paths cover both content equality and actual delivery. No filesystem failure, final-message comparison or record push was executed by this scenario review.

## 15. Upstream review boundary and later packaging

State: Framework implementation is ready for review but has no human acceptance, PR/merge grant or packaging authorization.

Expected next action: Publish the real development record and supporting evidence under its actual agreement; retain active evidence on the development branch. Inspect a proposed neutral tree only in a disposable copy. A later authorized packaging step first preserves a verified reachable evidence checkpoint, then creates neutral application starters without importing maintainer authority. The neutral starter is not the final maintainer briefing and cannot reset an established application's last outcome.

Route: [Template boundary](../../../../ops/maintain-template.md#product-and-development-boundary), [evidence and packaging](../../../../ops/maintain-template.md#preserve-evidence-then-package), [clean inventory](../../../../ops/maintain-template.md#clean-release-inventory).

Result: Passed (static). Upstream PR rules remain upstream-only, and publication/packaging do not manufacture acceptance. This scenario does not replace inspection of an actual disposable neutral tree.
