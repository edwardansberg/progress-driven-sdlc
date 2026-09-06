# Active workstream: human-coordinated-agentic-development

Workstream class: High-risk

Risk: High; the amendment defines autonomous authority and trust boundaries. This task changes documentation only.

Status: Ready for user validation

Current gate: Ready for user validation

Next action: User reviews local F3 with the checklist below and accepts the identified cumulative documentation candidate or requests corrections. Runtime implementation and live pilot activation require separate future human orders.

Loop control: Off

Loop step/reason: No run granted; runtime implementation not started; live activation requires a separate explicit human order.

Repository: edwardansberg/progress-driven-sdlc (upstream framework only)

Branch: main

Original implementation base: dfe3667ea37b41ba6de948ca1253930a23d7d093

R3 base and last inspected HEAD: 3d0ee387c9a6b993c1066139c87be58c5eaffcc0

Checkout observation: R3-final, 2026-09-06, Codex in this task; six unstaged modified files, empty index diff, and one untracked operational reference. R3-start at the same HEAD was clean with no pre-existing changes. Branch and HEAD remain unchanged and match the supplied Web review base.

Snapshot: F3, the complete six-file unstaged diff against the R3 base plus the full untracked docs/ops/autonomous-review-loop.md, as inspected at R3-final. This local artifact is distinct from the already-published F1/F2 amendments; a tracked diff alone is incomplete.

Publication observation: 2026-09-06, Codex read-only `git ls-remote origin refs/heads/main` returned 3d0ee387c9a6b993c1066139c87be58c5eaffcc0 after sanitized remote inspection. The GitHub connector also retrieved that exact commit in this session. Neither observation establishes human acceptance, earlier command actors, or this Web conversation's access.

Plan revision: r3, 2026-09-06

Started: 2026-09-06

Last substantive update: 2026-09-06 by Codex; r3 contract, verification, and F3 handoff. The investigated plan was recorded before normative edits.

Delivery target: Local uncommitted documentation/protocol amendment and pilot plan. Stop at Ready for user validation; no runtime, activation, acceptance, release, or archival.

Workflow: [Documentation Workflow](README.md)

## Outcome and Scope

Add an optional human-granted execution/review loop without changing the default workflow. Specify activation, review publication, exchange validation, human controls, failure handling, and a minimal future pilot. Documentation is the deliverable; an executable controller and live round trip are excluded.

Included: Six existing files (`docs/README.md`, `AGENTS.md`, root `README.md`, `docs/workstreams/WORKSTREAM_TEMPLATE.md`, `docs/ops/README.md`, and this workstream), plus the authorized new operational reference `docs/ops/autonomous-review-loop.md`. Compact earlier records using the pinned sources below; preserve unresolved acceptance locally.

Excluded: Staging, commits, pushes, branch/worktree changes, PR actions, deployment, live-data operations, destructive cleanup, history rewriting, dependencies, new paid usage, identity/signing/credential changes, global instructions/configuration, installed skills, downstream repositories, live controller construction/launch, automated ChatGPT interaction/extraction, nested model/API evaluations, and background tasks. Context, roadmap, debt, archive guidance, and archives remain intact.

## Context and Capability Evidence

Verified current behavior: All 13 tracked Markdown documents were read, including full policy/progress, scaffold, archive, operations, and security guidance. Root AGENTS.md is the only repository-owned instruction; applicable ancestor/default-home override checks found no additional files or repository skills. The compatible active r2 workstream remains unresolved. All four r2 corrections are present. Tracked inventory and runbooks define no executable tests, CI, dependency manifests, or controller. No custom Git hooks path or non-sample default hooks were found; remote service triggers are not established by this observation.

Observed local metadata: `codex --version` returned `codex-cli 0.153.4`; `Get-AppxPackage '*Codex*'` returned `OpenAI.Codex 26.901.6511.0`. No nested run was started. Session tool descriptions expose browser control (native app APIs disabled in this surface), app task messaging/waiting/automations, GitHub reads, and shell process interaction. Their presence does not establish a permitted ChatGPT relay, access to the intended account/conversation, or measured interruption. The GitHub connector retrieved the exact published commit; browser, messaging, scheduling, and cancellation interfaces were not exercised. Private browser state, credentials, and accounts were not inspected. This session has unrestricted shell access; no protected controller or human-control channel has been demonstrated. A same-identity pilot would provide cooperative control, not adversarial isolation.

Source verification: The five requested official sources were opened on 2026-09-06. Browser support is documented, while Europe Terms restrict automated/programmatic extraction. No applicable exception for this proposed relay was verified. Codex instruction discovery is documented per run; non-interactive structured output and app-server events/approval/cancellation provide possible local interfaces, not access to this Web conversation. See [source observations](ops/autonomous-review-loop.md#source-observations) for exact references, documented behavior, and adaptation limits.

CLI help inspection: `codex app-server --help` advertises stdio and marks the command experimental; `codex exec --help` advertises JSONL, structured output, and sandbox options. Both exited 0 without launching a server or model. This confirms installed command surfaces only, not compatibility, approval-channel isolation, cancellation reliability, or permission to use a Web relay.

Chosen target behavior: Default-off bounded grants, exact candidate review, external message/state validation, distinguishable human controls, and fail-closed publication/recovery. These are contract requirements, not implemented runtime properties.

Inference requiring validation: A small foreground local coordinator may support the pilot using existing Codex interfaces and manual Web relay. Its enforcement, account/transport permission, stop latency, recovery, and reliability require separate implementation and observed tests.

Open decision: User review of F3; later runtime implementation scope and separate pilot activation. No run ID, isolated branch, destination binding, grant expiry, or live budget has been approved. Automated Web transport remains unavailable pending verified permission and capability.

## Decisions and Authorization

Authority: The current user's request "Add an opt-in, human-controlled execution-and-review loop," section "Authority for this task," received 2026-09-06, grants scoped direct execution for this documentation amendment, read-only capability investigation, and offline verification. Plan r3 implements that request; it does not independently authorize itself. An agent relaying the text would not supply human authority. No live loop grant is made by this request.

Scope decision: Keep global authority canonical; put message shapes and operator/failure procedures in the single authorized operations reference. Keep progress as the only human-readable active state. Runtime private recovery data is only a future design, not another project plan or permission source.

Historical acceptance: No artifact-specific acceptance evidence for F1/F2 has been supplied. Their pending checks are not marked passed. They are superseded review artifacts within this still-active workstream; the human may explicitly accept an identified final cumulative candidate without repeating historical checklists or pretending earlier tests occurred.

Delivery Permissions: See the single ledger below. No prior publication or future example grants this task delivery or communication authority.

## Acceptance Criteria

- AC1: Activation requires a genuine complete bounded human grant; installation, implementation approval, relayed prose, and examples keep the loop off.
- AC2: Named repeated review-branch actions may be authorized together; review publication is distinct from acceptance/release, and unrelated staged work or consequential triggers prevent unsafe publication.
- AC3: Bounded request/response fields identify exact artifacts, origin, correlation, evidence, and verdicts; unsupported findings are reconciled and missing/mismatched evidence never authorizes action.
- AC4: Human provenance, status/pause/stop/resume, limits, no self-modification, and conservative recovery are specified with cooperative-control limitations.
- AC5: Transport permission and demonstrated reliability remain distinct; manual relay is compatible and no API reviewer silently replaces ChatGPT Web.
- AC6: Pilot implementation and activation gates, checks, rollback, unresolved targets/permissions, and ten document-level scenarios are reviewable; existing policy and historical evidence remain intact.

## Implementation and Verification Plan

- [x] Inspect current state/instructions, historical records, installed metadata, connector visibility, and all five official sources; record r3 authority, scope, and investigated plan before normative edits.
- [x] Amend canonical authority and review-publication flow; align concise entry points, scaffold, and operations index.
- [x] Specify bounded messages, controller guard/recovery contract, controls, source limitations, and implementation-ready pilot with manual relay as the current fallback.
- [x] Walk through all ten requested scenarios against independently specified expected decisions; inspect complete changed/new material, links/anchors, metadata, hygiene, and unchanged contracts.
- [x] Run applicable existing checks and `git diff --check`; record exact outcomes and limitations, then prepare F3 at the requested stopping gate with user checks pending and loop Off.

## Risks and Rollback

Permission drift and spoofed human authority are the central risks. Documentation alone cannot enforce either. Active-run policy changes require a pause and human re-bootstrap; a future controller must assess effects of tests, Git hooks, and publication. Automation must stay off when required provenance or service permission cannot be established.

Migration, deployment, and runtime observability: Not applicable to this local documentation amendment. Future pilot checks must measure controls and recovery before activation.

Rollback: If later requested, reverse only r3 local hunks against the R3 base and remove only its new reference after inspecting intervening work. Preserve the published F1/F2 policy and all unrelated edits. No rollback is performed now.

## Proposed First Pilot

Proposal only: A one-round review-only pilot of an identified frozen cumulative framework candidate in `edwardansberg/progress-driven-sdlc`. This exercises publication/exchange/control while avoiding an active run that changes its own governing documents. It does not demonstrate autonomous implementation or correction execution; those paths need offline coverage and a later human-selected non-governing change.

Runtime implementation gate: A separate human request must authorize a small foreground local coordinator, implementation location, and bounded development checks. Recommended components are a strict version-1 message validator, one writer lock, private journal/outbox and grant/revocation adapter, local operator console, guarded Git adapter, and manual-relay input/output. Use installed Codex app-server over local stdio for explicit turn events/cancellation if implementation-time compatibility checks confirm it; use non-interactive JSONL only if equivalent control requirements are demonstrated. No agent framework, database, daemon, or automatic browser adapter is needed. Freeze and inspect the coordinator before enabling any run; implementation happens with the loop Off.

Target and artifacts: Use the current upstream repository only, an exact human-selected base/candidate, and an isolated review branch on the verified `origin`. The branch name has not been selected or authorized; default/release branches are excluded. Do not invent a containing commit for F3 now. Before activation, identify the actual original base, previous reviewed head, candidate and frozen policy revision. The latest supplied Web review currently covers 3d0ee387c9a6b993c1066139c87be58c5eaffcc0; revalidate that reference against any intervening review evidence. The pilot permits no model edits to policy, approval records, controller, or tools; any findings return to the human after its single review.

Control boundary: The human operates a local console outside model/relay input and project data. The coordinator blocks new dispatch on Pause/Stop, journals revocation, and requests cancellation of a known in-flight turn/process when supported. Measure gate-closure latency, acknowledgement, and in-flight effects at each guarded step using offline fakes before any live side effect. If independent protection from the execution identity cannot be established, declare cooperative control and require direct human checkpoints before consequential actions; do not claim secure unattended enforcement. No local stop measurement has been performed in this task.

Transport boundary: Use manually shared version-1 objects in the actual human-selected ChatGPT Web conversation until a supported permitted automated route is verified. The human privately binds a destination alias and confirms exact repository/candidate visibility, source labeling, and allowed public/sanitized data. No conversation URL or account detail belongs here. An API alternative would need explicit reviewer/context/spending choices; it is not assumed to share this conversation.

Proposed run limits: One round, one writer, one outstanding review, 60 minutes total including waits, no new paid services/API spending, and final human validation. Grant start/expiry and control channel must be concrete at activation. Staging, branch creation, commit, push, and reviewer communication each require a named scoped entry, with any permitted repeats bounded by that grant. Hook/CI/deployment/cost effects must be checked before publication; unknown consequential effects block it. Existing publication does not authorize the next one.

Verification before activation: Offline fault injection for malformed/stale/duplicate/partial responses, uncertain send/push outcomes, concurrent edits, journal/lock loss, crash/expiry without budget reset, provenance spoofing, and pause/stop at every dispatch boundary. Separately inspect scoped test/credential effects, Git target/attribution, and source-loading behavior from the intended directory. After an explicit activation order, measure one permitted manual round's exact-candidate visibility, correlation, complete response handling, and local stop behavior; report observed latency and residual effects. No second round or post-round fix occurs under the first pilot grant.

Rollback and recovery: Keep review publication isolated. Stop revokes continuation and preserves the candidate, patch, and recovery evidence; inspect any in-flight side effect before further action. Reversal of pilot hunks, branch disposal, and private-record cleanup each need their actual authorization; no force push, history rewrite, default-branch reset, or destructive automatic cleanup. Runtime implementation rollback is limited to its future approved local files, without global configuration changes.

Unresolved activation requirements: Human approval of runtime implementation and subsequent evidence review; exact branch/candidate/scope; private destination/account binding and service permission for any automatic route; a demonstrated local control boundary and stop limits; known publication effects; a complete time-bounded human grant with named permissions. None blocks this documentation handoff, and none is fulfilled merely by accepting F3. Use the [operator procedure](ops/autonomous-review-loop.md#pilot-preparation-activation-and-stop) only after the respective future orders.

## Verification

Checks below were performed by Codex in r3 on 2026-09-06. F1/F2 evidence retains its original scope/source and is not reported as rerun. The final evidence/metadata update receives a focused consistency and whitespace recheck; no runtime result is inferred.

Check: Starting state, capability metadata, source claims, and publication observation.

Basis: `git rev-parse --show-toplevel`, `git branch --show-current`, `git rev-parse HEAD`, `git status --porcelain=v1 --untracked-files=all`; sanitized remote identity and `git ls-remote origin refs/heads/main`; GitHub connector `github_fetch_commit` for the exact published SHA; `git cat-file -e` for both pinned progress records; all required document reads; `codex --version`, `codex app-server --help`, `codex exec --help`, and `Get-AppxPackage '*Codex*'`; exposed tool descriptions and the five opened official pages.

Scope: R3-start checkout and the dated source/local-metadata observations above.

Result: Passed for read-only observation. Checkout and remote matched the supplied commit; no pre-existing changes or incompatible workstream. All four r2 corrections are present. Installed version/help surfaces and this session's GitHub commit access were observed; all five official references were accessible.

Limitations: Help/tool descriptions are not operational tests. No Web account/conversation access, automatic instruction loading, protected human channel, reliable relay, or stop latency was demonstrated. Service permission for the automated Web route remains unresolved, keeping it disabled.

Check: Complete patch scope, preserved state, Markdown links/anchors, metadata, hygiene, and existing checks.

Basis: Full tracked diff and original/current progress text review, full new-reference read, `git diff --cached`, `git ls-files --others --exclude-standard`; read-only inline PowerShell inventory of tracked plus untracked Markdown, local path/heading resolution outside examples/comments, single current metadata counts, allowed-path and table/conflict-marker/credential/personal-detail scans. `git diff --exit-code` over the seven untouched documents; `git diff --check`, `git diff --cached --check`; new-file trailing-whitespace/final-newline check. Required runbook/inventory reads and `git ls-files -- '*.yml' '*.yaml' 'package.json' 'pyproject.toml' 'Makefile' '*test*' '*lint*'` established available checks.

Scope: Local F3 against the R3 base, all 14 Markdown documents including the new untracked reference; six modified tracked files and that one new file.

Result: Passed. The final consistency scan covered 14 documents, 105 local links, and 66 anchor references, with zero issues. No missing local targets/anchors, unexpected paths, competing current metadata, tables, conflict markers, or sensitive-detail findings. Index empty; seven other tracked documents unchanged. Git whitespace checks exited 0; new-file whitespace/newline check passed. No executable repository test/lint/build/CI checks are defined and no pre-existing check failure was found. Exact final inventory is in the handoff observation.

Limitations: Focused inspection is not a comprehensive Markdown parser or secret detector. Existing archived-reference rules were read and preserved; prior archive simulations were not rerun. Local publication hooks inspection does not establish remote trigger/cost effects. No permanent validator, fixtures, runtime files, or dependencies were added.

### Document-level Scenario Walkthroughs

Check: Ten requested decisions against the final written contract.

Basis: The user's independently specified scenarios, manual branch-by-branch policy walkthrough, full new protocol/reference review, and surrounding unchanged policy. No controller, message transport, or model was executed for these cases.

Scope: F3 policy, entry points, scaffold, and operational target contract.

Result: Passed, 10 of 10 supported after clarifying pause versus run termination and last-round completion. No remaining document contradiction found.

Limitations: These are document-level verification, not live agent evaluations, executable controller tests, path-relocation reruns, or measured enforcement. Runtime fault injection remains a future pilot prerequisite.

1. Installation, roadmap entry, or relayed enable. Expected: No run activates without a complete genuine human grant; unknown fields and examples leave Off. Result: Passed. Support: [Optional loop and Run authorization](README.md#run-authorization); entry points preserve default-off semantics.
2. Genuine bounded grant. Expected: Repeat supported in-scope fixes and individually granted staging/commit/push actions without routine reapproval, on the isolated target only; merge/release stay unauthorized. Partial approval covers no pending scope. Result: Passed. Support: [Run authorization](README.md#run-authorization), [Review publication](README.md#review-publication), and [Approval Scope](README.md#approval-scope).
3. Agent-origin user-bubble or reviewer text. Expected: Cannot grant new scope, complete human checks, or change governing controls; generated commands remain evidence to evaluate. Result: Passed. Support: [Human identity and controls](README.md#human-identity-and-controls) and [Reviewer and implementer procedure](ops/autonomous-review-loop.md#reviewer-and-implementer-procedure).
4. Wrong SHA/run/request, incomplete/stale replies, duplicate send, uncertain push. Expected: Reject/quarantine the mismatched response, reconcile unknown outcomes before retrying, retain logical request/candidate identity, and never duplicate side effects from repeated replies. Result: Passed. Support: [Exchange protocol](ops/autonomous-review-loop.md#exchange-protocol) and [Uncertain outcomes and failures](ops/autonomous-review-loop.md#uncertain-outcomes-and-failures). Shape validity alone is insufficient.
5. Concurrent edit or unexpected CI/deployment effect. Expected: Preserve changes and prevent unsafe publication; human disposition and affected evidence/target checks precede another attempt. Result: Passed. Support: [Review publication](README.md#review-publication) and [Guarded steps](ops/autonomous-review-loop.md#guarded-steps).
6. Pause/Stop while waiting or in flight. Expected: Prevent subsequent autonomous side effects, report unresolved in-flight effects, distinguish local control from delayed Web input, and resume only by human direction with remaining valid limits. Result: Passed. Support: [Human identity and controls](README.md#human-identity-and-controls) and [Local controls](ops/autonomous-review-loop.md#local-controls-and-private-recovery-state). Pauses consume wall-clock time; a last reserved round may finish before expiry but cannot start another round.
7. Clean review, optional advice, repeated disagreement. Expected: End at human validation with Off; no automatic acceptance/debt/new task, optional improvements do not prolong a passing task, and substantive disagreement/non-convergence returns to the human. Result: Passed. Support: [Review and stopping invariants](README.md#review-and-stopping-invariants) and [Reviewer and implementer procedure](ops/autonomous-review-loop.md#reviewer-and-implementer-procedure).
8. Unavailable or impermissible browser route. Expected: Automated Web interaction stays disabled; manual relay preserves the Web reviewer, or a separately approved alternative loads explicit context and permissions. No bypass or presumed API access to this conversation. Result: Passed. Support: [Transport selection](ops/autonomous-review-loop.md#transport-selection) and [Source observations](ops/autonomous-review-loop.md#source-observations).
9. Crash, expiry, or changed control policy. Expected: No automatic restart, grant resurrection/expansion, cleared lock, or reset budgets; preserve unknown effects, reconcile, and require valid human direction/re-bootstrap. Result: Passed. Support: [Guarded steps](ops/autonomous-review-loop.md#guarded-steps), [Local recovery state](ops/autonomous-review-loop.md#local-controls-and-private-recovery-state), and [Run authorization](README.md#run-authorization).
10. Loop Off. Expected: Conceptual/quick work remains lightweight; standard/high-risk plans retain approval/direct-execution/partial-scope boundaries; evidence labels, user validation, attribution, terminal outcomes, and relocation-safe archives remain intact. Result: Passed. Support: [Work classes](README.md#work-classes), [Evidence labels](README.md#evidence-labels), [Verification](README.md#verification-and-user-validation), [Attribution](README.md#commit-attribution), and unchanged [Archive conventions](workstreams/README.md#preserve-references-at-closure). No F1/F2 user checks were inferred from publication.

Check: Live controller/round trip, fresh-session behavior, automated browser transport, and local stop enforcement.

Basis: Explicit task exclusions and absence of runtime implementation.

Scope: Future pilot and runtime behavior, not F3 documentation acceptance.

Result: Skipped; not authorized or implemented. User-owned F3 review remains Pending.

Limitations: No end-to-end reliability, compliant automatic Web integration, or tested kill switch is claimed. These missing runtime results block future activation, not this documentation stopping gate.

## User Validation Checklist

- [ ] Review F3's bounded activation, origin/control boundary, and distinct review-publication permissions.
- [ ] Review protocol, recovery, stop semantics, and the stated cooperative-control limitation.
- [ ] Review transport evidence and the one-round pilot's separate implementation/activation gates.
- [ ] Confirm the cumulative final documentation candidate or request corrections; prior acceptance is not inferred.

## Delivery Permissions

All entries apply to r3; none is authorized by a historical publication or an illustrative future grant.

- Staging: Unapproved; excluded.
- Commit: Unapproved; excluded.
- Push: Unapproved; excluded.
- Branch creation: Unapproved; excluded.
- Branch checkout/change: Unapproved; excluded.
- Worktrees: Unapproved; excluded.
- Reviewer communication/automated relay: Unapproved; excluded; read-only research is allowed.
- PR creation: Unapproved; excluded.
- PR merge: Unapproved; excluded.
- Deployment: Unapproved; excluded.
- Live-data operations: Unapproved; excluded.
- Destructive cleanup: Unapproved; excluded.
- Production promotion: Unapproved; excluded.

## Historical Evidence and Unresolved Acceptance

These summaries retain source/snapshot scope; exact plans, unique decisions, full check records, and original pending checklists are retrievable at the pinned documents. They are historical reports, not reruns in r3. Both pinned objects were verified available locally with `git cat-file -e <commit>:docs/progress.md`.

- r1/F1: [Record at 86554d0](https://github.com/edwardansberg/progress-driven-sdlc/blob/86554d0f2be7c6b947031fc3e27c1d6f0d7a63da/docs/progress.md). Codex's 2026-09-06 handoff reported six unstaged files against dfe3667ea37b41ba6de948ca1253930a23d7d093, no staged/untracked files, and pending user validation. The initial direct-execution request covered local policy/collaboration/adoption/lifecycle amendments only. Reported evidence: 13-document link scan (79 local links, 43 anchors), whitespace/scope/hygiene checks, ten policy scenarios; a supplied specialist review prompted the proposed/approved/pending scaffold correction. No live evaluation or user acceptance was claimed.
- r2/F2: [Record at 3d0ee387](https://github.com/edwardansberg/progress-driven-sdlc/blob/3d0ee387c9a6b993c1066139c87be58c5eaffcc0/docs/progress.md). Codex's 2026-09-06 handoff reported six unstaged corrections against 86554d0f2be7c6b947031fc3e27c1d6f0d7a63da and pending user validation, under the separate post-publication direct-execution request. Reported evidence: 20 positive archive-fixture assertions, six displaced targets in the unchanged-copy negative control, 33 actual progress-link relocations, 13-document scan (93 links, 58 anchors), whitespace/scope/hygiene, and six scenarios. Fresh-session evaluation was explicitly skipped. Corrections addressed observation scope, archive relocation, guidance activation, and actor-specific attribution.
- Publication: r2 observed remote main at 86554d0; r3 independently observes main at 3d0ee387 as recorded above. Publication establishes neither prior smoke checks nor acceptance, delivery authority, or command actor. Earlier no-delivery reports apply only to Codex's respective tasks. No accusation or retroactive permission is inferred.
- Unresolved locally: Human acceptance of the current cumulative artifact; actual fresh-session behavior remains unperformed. Prior checklists covered workflow/scaffold/adoption plus the four r2 corrections. F3 review includes preservation of those contracts; no historical user check has been completed on the human's behalf.

## Progress Log and Handoff

2026-09-06: Resumed compatible work as r3 at the exact reviewed commit; recorded direct-execution authority and plan before normative edits. Condensed r1/r2 repetition with exact pinned records while preserving unresolved acceptance. No scope departure or blocker to the local documentation work found.

2026-09-06: Implemented the opt-in authority, exchange, control/recovery contract, and pilot plan. Walkthroughs clarified pause versus termination, completion of the last reserved round, and retention of a supplied previous review before the first protocol round. Ten scenarios and final consistency/whitespace checks passed. No remaining contradiction or local amendment blocker was found.

Review material: F3 consists of the complete local tracked diff plus the full new operational reference. A Web reviewer with only published main has not reviewed F3; supply that new file explicitly with the focused diff and required dependencies. No commit or push is needed to review this amendment.

Changed files and outcomes:

- `docs/README.md`: Canonical opt-in grant, review-publication exception, human origin/control and stopping invariants; cumulative acceptance and concise historical references.
- `AGENTS.md`: One concise default-off/no-self-authorization entry with canonical and operational references; actor-specific attribution preserved.
- Root `README.md`: Optional-loop orientation, activation prerequisites, and contract-versus-controller limitation.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md`: Optional grant prompts referencing the existing permission ledger and compact loop control/step metadata.
- `docs/ops/README.md`: Link to the authorized operational reference.
- `docs/ops/autonomous-review-loop.md`: New untracked protocol and controller/operator target contract, recovery and pilot prerequisites, and dated official-source observations.
- `docs/progress.md`: Actual r3 authority, observations, plan, pilot proposal, verification, and pending user review; earlier unique evidence remains retrievable through pinned records.

Scope departures: None. The proposed first live pilot is deliberately review-only and one round; autonomous implementation/fix execution remains a later verification need, not a claimed result. No runtime code, private recovery state, new status register, or permanent testing infrastructure was created. All prior user acceptance remains unresolved; the current checklist permits explicit cumulative acceptance of the identified final candidate.

Rollback remains limited to r3's local hunks and its new reference, preserving published F1/F2 and any intervening work. During this r3 task, Codex performed no staging, commit, push, branch/worktree or PR action, release/deployment, live-data operation, destructive cleanup, history rewrite, dependency installation, new paid service/API usage, identity/signing/credential or global configuration/instruction change, installed-skill edit, downstream edit, controller/model launch, automated ChatGPT interaction/extraction, or background task. No acceptance, release, or archival was claimed. The current gate and next owner are authoritative in the metadata above.
