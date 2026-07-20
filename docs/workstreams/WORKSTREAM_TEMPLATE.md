# Active workstream: [short-slug]

Workstream class: [Quick, Standard, or High-risk]

Risk: [Low, Medium, or High, with a short reason]

Status: Planning

Current gate: Investigation and plan publication

Next action: Verify current behavior, complete this plan, and move to `Awaiting plan approval` before substantive implementation.

Started: YYYY-MM-DD

Last substantive update: YYYY-MM-DD by [actor]

Plan approval: Pending

Delivery target: [Local only, pull request, preview, production, or another explicit target]

Release state: Not started

This file is the single source of truth for the active workstream. Keep it aligned with actual work as evidence changes, implementation proceeds, verification completes, and the user reviews or releases the result.

The operating rules, status transitions, and archive process live in [Documentation Workflow](../README.md).

## Requested Outcome

[State the user-visible or operational outcome in plain language.]

## Definition of Done

- [Observable condition that proves the requested outcome.]
- [Required verification and documentation condition.]
- [Required delivery or environment condition, if authorized.]

## Context and Evidence

### Verified current behavior

- [Claim confirmed in current code, configuration, migration, test, Git, or runtime evidence. Cite the path, symbol, commit, or sanitized observation.]

### Chosen target behavior

- [Behavior or architecture explicitly selected for this workstream.]

### Inferences requiring validation

- [Plausible conclusion and the check that will confirm or reject it.]

### Open decisions

- [Decision, options, owner, and gate by which it must be resolved.]

## Relevant System Map

- Entry points: [Routes, commands, jobs, or user surfaces.]
- Core logic: [Services, modules, or components.]
- State: [Databases, files, queues, caches, or external state.]
- External contracts: [APIs, providers, consumers, or compatibility boundaries.]
- Operations: [Build, deploy, migration, monitoring, or rollback surfaces.]

## Scope

### Included

- [In-scope behavior, files, or systems.]

### Not included

- [Explicitly excluded adjacent work.]

## Constraints and Assumptions

- [Compatibility, time, cost, security, platform, or ownership constraint.]
- [Assumption plus how it will be verified.]

## Decisions

1. **[Decision title].** [Decision, rationale, and important tradeoff.]

## Acceptance Criteria

- [Specific behavior or invariant.]
- [Failure, edge-case, compatibility, or security condition.]
- [Documentation, observability, or release condition.]

## Implementation Plan

### Phase 1 — [Investigation, contract, or foundation]

- [ ] [Concrete implementation or validation step.]
- [ ] [Concrete implementation or validation step.]

Acceptance:

- [Evidence required before the phase is complete.]

Rollback:

- [How to safely undo or contain this phase.]

### Phase 2 — [Main implementation]

- [ ] [Concrete implementation step.]
- [ ] [Concrete implementation step.]

Acceptance:

- [Evidence required before the phase is complete.]

Rollback:

- [How to safely undo or contain this phase.]

### Phase 3 — [Integration, verification, and handoff]

- [ ] [Integration or migration step, if applicable.]
- [ ] [Automated verification step.]
- [ ] [Documentation and user-handoff step.]

Acceptance:

- [Evidence required before the phase is complete.]

Rollback:

- [How to restore or contain the delivered behavior.]

## Risks and Controls

- Risk: [Concrete failure mode or uncertainty.]
  - Control: [Prevention, detection, or containment.]
  - Evidence gate: [Test, rehearsal, measurement, or approval.]

## Migration, Rollout, Observability, and Rollback

Migration: [Required procedure and data compatibility, or `Not applicable` with a reason.]

Rollout: [Environment sequence, flags, staged exposure, and ownership, or `Not applicable` with a reason.]

Observability: [Health, logs, metrics, alerts, and exact success or failure signals.]

Rollback: [Code, artifact, configuration, data, and operational rollback boundaries.]

Destructive effects: [Exact targets and separate approval, or `None`.]

## Verification

Use `Passed`, `Failed`, `Skipped`, or `Pending`. Include the command or evidence and a concise result. Never mark a check passed because it is planned.

### Automated and repository checks

- Pending: [Focused unit, contract, or route tests.]
- Pending: [Lint, type, build, migration, or configuration validation.]
- Pending: [Regression or end-to-end checks proportionate to the change.]

### Runtime or environment checks

- Pending: [Health, version, effective configuration, migration, or observability evidence.]

### User validation checklist

- [ ] [Primary happy-path smoke check.]
- [ ] [Important edge or failure-path smoke check.]
- [ ] [Rollback or containment check when appropriate.]

User-owned checks remain pending until the user supplies evidence or confirmation.

## Delivery Gates

- Implementation approval: Pending
- Commit approval: Pending or not requested
- Push or pull-request approval: Pending or not requested
- Preview deployment approval: Pending or not applicable
- Live migration or destructive-operation approval: Pending or not applicable
- Production promotion approval: Pending or not applicable
- Released commit and environment verification: Pending

## Progress Log

### YYYY-MM-DD — Investigation

- [Meaningful finding, decision, or evidence.]

### YYYY-MM-DD — Implementation

- [Completed phase, deviation, or verification result.]

Keep this concise. Do not copy tool calls or terminal transcripts.

## Deviations and Blockers

None currently.

[When present, state what changed, why, impact on scope or risk, and whether renewed approval is required.]

## Delivery Summary

Not delivered yet.

[At handoff, state the user-visible outcome, important implementation facts, checks run, remaining user validation, rollback considerations, and exact delivery state.]

## Next Action

Complete investigation and obtain plan approval.
