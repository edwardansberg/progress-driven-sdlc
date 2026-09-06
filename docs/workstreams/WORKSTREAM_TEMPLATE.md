<!-- REUSABLE SCAFFOLD: Initialize docs/progress.md only after checking existing
active state; resume compatible work and never overwrite an unresolved unrelated
workstream without the user's explicit disposition. Replace prompts with
investigated state and remove setup comments before publishing the plan.
Standard/high-risk work normally awaits plan approval; recorded explicit scoped
direct execution permits proceeding after investigation and a written plan.
Paths in this scaffold are repository-relative; adapt links when instantiating. -->

# Active workstream: <!-- short-slug -->

Workstream class: <!-- Quick, Standard, or High-risk -->

Risk: <!-- Low, Medium, or High, with reason -->

Status: Planning

Current gate: Investigation and plan publication

Next action: <!-- Owner and concrete step under the recorded authorization -->

Loop control: Off

Loop step/reason: <!-- No run granted by default; when relevant, current step/reason and outstanding request. This is not workstream status. -->

Repository: <!-- Repository identity, without credentials or personal paths -->

Branch: <!-- Branch name or detached state -->

Implementation base: <!-- Original starting revision; retain when later observations change -->

Last inspected HEAD: <!-- Observed revision, not this document's future containing commit -->

Snapshot observation: <!-- Date or capture reference, actor/source, snapshot ID and patch/bundle base; relevant staged/unstaged/untracked state and pre-existing work. Distinguish materially changed artifacts and retain historical observations. -->

Plan revision: <!-- Revision or equivalent identifier; update when the plan changes -->

Started: <!-- Available date -->

Last substantive update: <!-- Date and actor -->

Delivery target: <!-- Agreed artifact/environment and whether a release is required; mark unresolved choices -->

Workflow: `docs/README.md`

## Requested Outcome and Definition of Done

<!-- State the observable outcome, required evidence and documentation, user
acceptance, and agreed delivery conditions. Distinguish this task's stopping gate
from eventual workstream closure. -->

## Context and Evidence

### Verified current behavior

<!-- Cite files, revision/snapshot, commands, or environment observations.
Identify supplied reports as reported evidence rather than independent checks. -->

### Chosen target behavior

<!-- Record explicitly selected behavior; approval is not implementation evidence. -->

### Inference requiring validation

<!-- Pair each inference with the focused evidence needed to resolve it. -->

### Open decision

<!-- Record each unresolved choice, its owner, and the gate by which it is needed. -->

## Relevant System Map

<!-- Relevant entry points, core logic, state, external contracts, and operational
surfaces; keep concise or justify non-applicability. -->

## Scope and Constraints

Included: <!-- Proposed boundary, identifying approved and pending portions;
authorization is recorded below. -->

Excluded: <!-- Adjacent work and unauthorized actions. -->

Constraints and assumptions: <!-- Compatibility, security, cost, platform, and
ownership constraints; pair uncertain assumptions with validation. -->

## Decisions and Authorization

<!-- Keep the implementation authorization here once, including:
- State: Pending, approved scope, partial approval, or scoped direct execution.
- Covered plan revision or scope; approving actor; available decision/date reference.
- For direct execution, identify the user's request, scope/exclusions, and the plan
  implementing it. Do not claim the plan itself was approved if it was not.
- Distinguish pending/superseded portions, proposals, and material decisions.
Do not invent missing approval history. Delivery permissions are separate below. -->

### Optional Run Authorization

Not enabled; no run grant.

<!-- Leave concise when unused. For an explicitly enabled run, record one grant:
human source/reference; run ID; repository/workstream; approved plan/scope and fixed
acceptance criteria; allowed paths/classes and exclusions; approved remote/review
branch; destination alias/sharing boundary; start, expiry, round/time/spending
limits; human checkpoints and local control mechanism/limitations. Reference the
named Delivery Permissions below, including repeat allowance, instead of repeating
permissions here. Unknown required fields keep control Off. Follow canonical
Optional Execution and Review Loop and docs/ops/autonomous-review-loop.md.
Record original base, previous reviewed head (or none), exact candidate and
outstanding request when they exist; keep private transport/recovery data local. -->

## Acceptance Criteria

<!-- Independently specified outcomes, invariants, edge/failure conditions,
compatibility/security contracts, and documentation or delivery requirements. -->

## Implementation Plan

<!-- Use only as many phases as the work needs; one is sufficient for a bounded
effort. Add concrete checkbox steps and completion evidence per phase. Keep
reusable procedures in runbooks. Reference shared rollback detail when sufficient. -->

### Phase 1 — <!-- Outcome -->

- [ ] <!-- Concrete step -->

Acceptance: <!-- Evidence needed for phase completion -->

Rollback or containment: <!-- Focused boundary or reference to shared detail -->

## Risks, Migration, Rollout, Observability, and Rollback

<!-- Record meaningful risks and controls. Retain concrete migration,
compatibility, rollout, observability, rollback, and destructive-target detail
where relevant. Otherwise give concise, justified non-applicability. -->

## Verification

<!-- Use the canonical Check/Basis/Scope/Result/Limitations record for automated,
repository, runtime, or supplied-evidence checks that apply. Retain required
project checks and distinguish check performer from reviewer. -->

Check: <!-- What is tested or inspected -->

Basis: <!-- Command, files, supplied artifact, or observation; performer/source -->

Scope: <!-- Artifact or revision/snapshot and environment where relevant -->

Result: Pending <!-- Passed, Failed, Skipped, or Pending, with factual outcome -->

Limitations: <!-- What remains unverified and why -->

### User Validation Checklist

- [ ] <!-- Outcome or important edge/failure case; identify the artifact covered by user evidence/confirmation and return affected checks to Pending after changes -->
- [ ] <!-- Relevant rollback/containment or review check -->

## Delivery Permissions

<!-- For each relevant action, record pending/unapproved/approved state, exact
scope/target, actor, and available reference. One instruction may cover multiple
named actions. Omit irrelevant actions or mark Not applicable with a reason;
neither means authorized. Add separate entries for distinct targets if needed. -->

- Commit: Not requested
- Push: Not requested
- Pull-request creation: Not requested
- Pull-request merge: Not requested
- Deployment: Not requested
- Live-data operations: Not requested
- Destructive cleanup: Not requested
- Production promotion: Not requested

<!-- For loop publication/transport, add distinct Staging, Branch creation, and
Reviewer communication entries when relevant. Bind all named actions to the
run/target and reference, including repeat limits. Review publication is not
release or user acceptance. No default/release-branch writes in the initial loop. -->

## Progress Log

<!-- Dated material findings, decisions, outcomes, deviations, and verification.
Do not duplicate current metadata or copy terminal transcripts. -->

## Deviations and Blockers

None currently.

<!-- State changed scope/risks, the concrete blocker and smallest needed decision,
and whether renewed approval applies. -->

## Delivery Summary

Not delivered yet.

<!-- Use canonical Handoff and resumption: reference current metadata rather than
maintaining another status block; identify changed/reviewed material including
relevant untracked files, authorization versus pending choices, actual checks and
their sources/artifact scope, user validation, risks, rollback, and remaining action/owner.
Keep separately observed publication/delivery evidence here when relevant, with
target, exact commit/artifact, observation date, and source. Scope action reports
to their reporting actor/task; publication alone is not acceptance or authority.
Record exact delivery/acceptance evidence at the appropriate gate; do not claim a
terminal outcome or archive while required validation/release remains outstanding. -->
