# Technical Debt Register

Status: Maintained register

Last substantive update: Not yet initialized

Authority: Records accepted recommendations but does not authorize implementation

This file records verified engineering improvements that the user agrees are worthwhile but intentionally postpones. It prevents useful recommendations from disappearing without turning them into active work or delivery commitments.

## How to Use This Register

Add an item only when:

- a concrete weakness, risk, maintenance burden, or missed engineering improvement has been verified;
- a credible remedy is understood well enough to describe;
- the user accepts the recommendation but chooses not to implement it now; and
- the item is not already represented by an active workstream.

Each active item records:

- a stable ID and concise title;
- its state and affected area;
- the verified problem and impact;
- the accepted recommendation;
- why implementation is postponed;
- the trigger for reconsideration;
- relevant evidence, dependencies, and cautions.

An entry in this file is not implementation approval. When the user selects an item:

1. create or update the active workstream in [progress.md](progress.md);
2. investigate whether the evidence and recommendation remain current;
3. write the implementation, verification, rollout, and rollback plan;
4. obtain the approval required by the work class;
5. mark the debt item `Promoted` and link the active or archived workstream;
6. after delivery, mark it `Resolved` with concise commit and release evidence.

Use these states:

- `Deferred`: Accepted but intentionally postponed.
- `Promoted`: Selected and represented by an active workstream.
- `Resolved`: Delivered and verified.
- `Rejected`: Reconsidered and intentionally declined.
- `Superseded`: Replaced by another item or architecture decision.

Review relevant items when starting adjacent work, after an incident exposes the same risk, when operational cost increases, and when closing a workstream. Do not invent deadlines or priority scores without a real user decision.

## Active Debt

No accepted deferred items yet.

## Entry Template

```markdown
### `<AREA>-001` — Concise title

- State: Deferred
- Area: Affected system or practice
- Identified: YYYY-MM-DD
- Problem: Verified weakness or maintenance burden.
- Impact: Concrete risk, cost, or constraint.
- Accepted recommendation: The remedy the user agrees is worthwhile.
- Reason postponed: Why it is intentionally not active now.
- Reconsider when: Evidence-based trigger, not an invented date.
- Evidence: Relevant files, tests, incidents, metrics, or runtime observations.
- Dependencies: Required decisions or prerequisite work, if any.
- Caution: Important rollout, compatibility, or safety concern.
```

## Resolved or Closed Debt

No items yet.
