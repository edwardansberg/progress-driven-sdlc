# Verification and change map

Observation: 2026-11-07; primary coding agent on Windows/PowerShell with existing Git, gh and Python. No dependencies installed.
Baseline: Released main 04765e32d8832a9b80fddd0b3875234386891d14.
Inspected implementation: 751b14ab67351d6cc318bb553edeae6379285448, plus the three corrections identified below. Evidence records keep their original snapshot scope; later record-only changes do not imply repeated runtime checks.
Authority and current status: [Active detail](../../../progress-agent.md), referencing the agreement in context. This note is supporting evidence, not another authority record.

## Requested behavior and canonical home

- Agent/human ownership, rolling execution packages, selective memory, agreement persistence, publication/recovery and exact checkpoint equality: docs/README.md. AGENTS.md routes briefly to these rules.
- Application first slice, navigation/status, keyboard/pointer/reflow and headless/existing-product boundaries: docs/ops/application-experience.md; core and ops index route only affected work there. W3C references and limits are in that guide.
- Light goal/milestone/next-move presentation: core checkpoint contract. Five fictional contexts in docs/ops/checkpoint-examples.md illustrate planning, useful progress, failed verification, human validation and accepted development with pending delivery; no points or invented progress metrics.
- New-project and adoption authorization: root README prompts. Target-preserving migration, continuation and handoff: docs/ops/adopt-framework.md. Actual agreement is recorded once in docs/context.md, with workstream reference/exceptions in detail.
- Two-level plan and execution/recovery fields: sole docs/workstreams/WORKSTREAM_TEMPLATE.md; setup/closeout conventions route to core. Established applications retain their last outcome instead of restoring a first-use invitation.
- Development evidence versus neutral application packaging: docs/ops/maintain-template.md; neutral starter exception is explicit. Blueprint changes only clarify role, applicable publication authority and briefing routing; renderer/schema/activation remain unchanged.
- Actual plan, evidence and next action: progress-agent.md; human checkpoint: progress.md. Branch-local context and roadmap identify actual upstream scope. Supporting request, research, scenarios, reading counts and disposable packaging inputs remain in this bundle.

Historical/unchanged contracts: Optional controller protocol, Blueprint HTML renderer, debt register, security guide, archive index and old-history index are unchanged from baseline. No application, controller, database, installer or synchronization service was added.

## Checks and limits

Check: Local paths and anchors.
Basis/source: Invoked request section 9 and existing adoption/maintenance rules.
Scope: check-links.py over root entry/README and all docs Markdown, excluding fenced examples; relative paths/fragments and reference-style links. External research/standards were inspected separately.
Result: Passed at first increment (22 Markdown files, 133 links), and after corrections; final bundle count is recorded in detail. Proposed neutral tree: 20 Markdown files / 134 local links; product-README portability variant: 20 / 120; zero errors in both.
Limitations: Focused one-off parser for this repository's Markdown, not a full Markdown renderer or external-link availability test. Does not prove instructional compliance.

Check: Whitespace, complete changed content and preservation.
Basis/source: Publication scope and repository conventions.
Scope: git diff --check, git diff --cached --check, complete maintained-file diffs and new supporting content; explicit staging list.
Result: Passed. Newly written CRLF records initially failed whitespace checks; normalized only those new/modified records to LF and reran successfully. Original untracked request and ste_communication_amendment.patch remain excluded and untouched; a content-equivalent request copy is retained here for resumption. Other worktree untouched.
Limitations: No application build/test command exists for this documentation change. No runtime accessibility, usability, productivity or deployment result is inferred.

Check: Scenario coverage and clean receiving context.
Basis/source: Invoked request section 9.
Scope: [15 static scenarios](scenarios.md) on 751b14a, plus a separate agent with no inherited conversation comparing the same supplied recovery scenario against baseline and candidate. Primary agent reconciled reports against source.
Result: Passed for the recorded scenarios after the concrete corrections below. Both snapshots recover safe next action: repair failed duplicate-job verification, correct stale ready-summary to Implementing, preserve another actor's staged file, recognize remotely present candidate as published, and keep acceptance/deployment pending and controller Off. Candidate makes persistence, staged-work isolation, unfinished checkpoint limits and saved-briefing equality explicit.
Reading route: AGENTS → core → global/affected context and detail → stale summary → relevant sources/checks. Ordinary continuation avoids scaffold/adoption/Blueprint/controller manuals. Audit-only reads of adoption/maintenance/scaffold were separate.
Limitations: Hypothetical facts supplied equally to one fresh receiver; baseline/candidate read in that context, not randomized independent trials. No measured human usability, live failure, crash, production or migration test. No unnecessary remote fault injection or Git fixtures were used.

## Concrete review findings and resolution

F1 — Portability: Candidate adoption guide introduced links to root onboarding headings that need not survive preservation of a product README. Corrected both routes to target-local core agreement guidance and recovery of the actual human instruction. Verified by replacing the disposable tree's README with product text plus only required provenance/workflow links, running link checks, then restoring it. Neutral starter briefing uses a local core agreement link too. No actual product README was overwritten.

F2 — Authority: Baseline required named authority for live-data operations; candidate's shortened exclusions omitted that explicit boundary in core/new-project kickoff. Restored it in both. Adoption already retained it. Rechecked the affected authority text against approval scope, scenarios 11/13 and the unchanged controller grant contract; no new capability or live-data grant follows.

Corrected complete file blob identities (git hash-object; these bind uncommitted observations beyond HEAD):

- README.md: 290f6d2a8aa310ce2111fe8b9e82b1139e886bc9.
- docs/README.md: 6d470edbb1c905f01f9bebb2cb513a56b440d52f.
- docs/ops/adopt-framework.md: 5f42b91d89cf86e8214329125e0e4145caadd555.

No other policy files changed after 751b14a. No unresolved concrete finding remains. Static review is reported agent evidence, not independent human acceptance.

## Proposed neutral release tree

Method: Enumerated all 24 tracked candidate files with git ls-tree, materialized each exact blob in a fresh disposable directory, and classified every file before exclusion. Removed only the three candidate workstream supporting files from that copy, then applied the proposed neutral memory replacements and corrected policy blobs. All later supporting files under this bundle have the same maintainer-only classification. The actual development records remain intact and published.

Retained proposed inventory: 21 files — root AGENTS/README; docs core/context/progress-agent/progress/roadmap/debt; old/security indexes; workstreams index, sole scaffold and archive index; ops index, adoption, maintenance, application experience, fictional checkpoint examples, optional controller specification, Blueprint contract and neutral renderer. No generated Blueprint or runtime model.

Neutrality checks: Passed. No workstream key or implementation-candidate hash in any release file; no maintainer active/archive files; detail and summary both starter-1 / No active workstream / controller Off; no checks, acceptance or adopted agreement claimed. Context retains unknown application facts and an enabled convention with human/repository/origin/branch scope unestablished. Root provenance stays Not recorded yet / Not assessed yet. Roadmap/debt are neutral.

Reproduction input: [neutral-starters.patch](neutral-starters.patch) is a disposable proposal against the four live memory files at exact 751b14a, not an instruction to apply it to current development or an established application. Extract that candidate, classify its complete tree, exclude maintainer evidence only in the disposable copy, apply this zero-context patch with git apply --unidiff-zero and the three corrected blobs above, then run check-links.py against that copy. It is retained review evidence, not a second maintained scaffold. Later real packaging requires its own authority and a durably reachable evidence checkpoint under the maintenance procedure.

Same-source adoption: Static walkthrough confirms aligned content needs no rewrite or timestamp/provenance churn, and preserved product text/local overrides remain outside the migration map. No executable adopter exists; no live migration/idempotence claim is made.

## Reading cost and research

[Measured route floors](reading-cost.md) report normalized UTF-8 bytes and whitespace-separated words for identical task routes, using neutral memory on both sides. Core/entry reading increases; this is a documented regression, not a claimed performance improvement. Application guidance/examples/research remain task-triggered. No tokens, runtime savings or human comprehension were measured.

[Research basis](research.md) records five primary sources, versions/methods/limits, conflicting metrics and design inferences; the application guide records W3C references. Proposed later evaluation separates comprehension, decision/review effort, restart accuracy, rework, success, maintained quality, context cost and enjoyment, including training/coordination/maintenance. No workplace pilot is authorized or performed.

## Publication and final briefing

First publication: git push -u origin HEAD:refs/heads/codex/feat-autonomous-human-agent-workflow succeeded; git ls-remote returned exact 751b14ab67351d6cc318bb553edeae6379285448. Author Codex <codex@local.invalid>; configured committer/signing/credentials preserved. No active local hooks, configured hooks path or tracked GitHub workflows observed; no changes to those assumptions.

Final sequence: Publish checked correction/evidence candidate and verify its exact remote ref. Update detail with that known candidate, derive the saved human briefing, compare its facts/state/next action with detail, commit/push the records, then verify final delivery without inserting its future containing hash. Reuse the saved briefing in the final response with only transport-required link formatting. Any failed final save/delivery must be disclosed and reflected in the saved briefing where possible. Current results and final candidate are in active detail, not duplicated as a competing status here.
