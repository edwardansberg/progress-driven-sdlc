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

Repository: <!-- Repository identity, without credentials or personal paths -->

Branch: <!-- Branch name or detached state -->

HEAD or base commit: <!-- Exact inspected revision -->

Snapshot: <!-- Relevant staged/unstaged/untracked state and pre-existing work; identify supplied evidence and inspection limits -->

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

Scope: <!-- Revision/snapshot and environment where relevant -->

Result: Pending <!-- Passed, Failed, Skipped, or Pending, with factual outcome -->

Limitations: <!-- What remains unverified and why -->

### User Validation Checklist

- [ ] <!-- Outcome or important edge/failure case; leave pending until user evidence or confirmation -->
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
their sources, user validation, risks, rollback, and remaining action/owner.
Record exact delivery/acceptance evidence at the appropriate gate; do not claim a
terminal outcome or archive while required validation/release remains outstanding. -->
