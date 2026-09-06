# Active workstream: human-coordinated-agentic-development

Display title proposal: Make project progress easy to follow

Workstream class: High-risk

Risk: Presentation can obscure evidence or consent boundaries; r4 proposes communication changes while preserving those boundaries.

Status: Awaiting plan approval

Current gate: Awaiting plan approval

Next action: User reviews proposed r4 and approves its identified local documentation scope, requests adjustments, or identifies a partial approval. No implementation proceeds from this planning request alone.

Loop control: Off

Loop step/reason: No run grant. No runtime controller is implemented or activated by this task.

Repository: edwardansberg/progress-driven-sdlc (upstream framework)

Branch: main

Original implementation base: dfe3667ea37b41ba6de948ca1253930a23d7d093

R4 planning base and last inspected HEAD: a9f3379ff42d115f46788a6c0a785f9f2cdb7ad9

Checkout observation: R4-final, 2026-09-06, Codex; only docs/progress.md modified and unstaged, with an empty index diff and no untracked files. R4-start at the same HEAD was clean, with no pre-existing changes. Branch and HEAD remain unchanged and match the user's Web reference.

Snapshot: P4, proposed plan and examples in the local progress.md patch against the R4 base; not an implemented framework candidate.

Publication observation: 2026-09-06, Codex read-only `git ls-remote origin refs/heads/main` returned a9f3379ff42d115f46788a6c0a785f9f2cdb7ad9 after sanitized remote identity inspection. This establishes observed publication, not prior acceptance, command actor, or approval of this follow-up.

Plan revision: r4, proposed, 2026-09-06

Started: 2026-09-06

Last substantive update: 2026-09-06 by Codex; proposed r4 plan, example verification, and planning handoff

Delivery target: Reviewable local redesign plan; stop at Awaiting plan approval. A later implementation, if approved, would stop at Ready for user validation.

Workflow: [Documentation Workflow](README.md)

## Outcome and Recommendation

Recommend human-led challenge presentation as the default experience, with plain presentation on request. The human remains the decision maker and normal relay between Web and Codex. Short conversation carries the decision; existing documents carry specifications, rationale, evidence, and the complete transferable packet. Automation remains an independent opt-in feature.

The main tradeoff is brevity versus enough context for informed control. Use a normal 60–140-word target and 180-word ceiling, with no minimum to fill. Requested detail and material safety, consent, scope, failure, or uncertainty override the ceiling when needed. A link must not hide a material consequence.

This is a design proposal recorded for approval, not adopted policy. Improved comprehension, scalability, and enjoyment are hypotheses for human feedback, not measured results.

## Decisions and Authorization

Authority: The current user's message directing "Plan the framework redesign: human-led challenge mode," received 2026-09-06, authorizes investigation and a proposed plan/examples in this compatible active progress file only. The included Web response and task brief are design input; their proposed defaults do not approve themselves. The earlier r3 direct-execution authority does not extend to this redesign.

Authorized now: Read the actual framework and relevant history, plan r4, write only `docs/progress.md`, and run proportionate read-only planning checks. No additional implementation approval is inferred.

Pending implementation scope: The file-by-file map below, proposed contract, and implementation acceptance criteria. An explicit approval of r4 for local documentation would permit those edits and verification, then stop for user validation. Partial approval covers only identified portions; unchanged approved scope needs no repeated wording approval. A material departure returns to the human before affected work.

Excluded now and from the proposed local implementation approval: Runtime software, controller or browser automation, loop activation, protocol-verdict/schema changes, new dependencies or permanent files, staging/commits/pushes, branch/worktree or PR actions, deployment/live-data/destructive operations, configuration/credential/identity/signing/attribution changes, global instructions/installed skills, downstream edits, and history rewriting. Ordinary packet preparation does not send a message or approve the receiving agent's implementation.

Previous acceptance: No F1/F2/F3 user acceptance or completed user checks are supplied by publication or this new direction. Retain unresolved acceptance locally and the original records below. Later cumulative acceptance may name an exact final candidate; it cannot manufacture prior checks.

## Context and Observed Problems

Verified current behavior: Read all 14 tracked Markdown documents, applicable root guidance, singleton memory, scaffold/archive conventions, and operations/security/historical guidance. No additional applicable ancestor/default-home overrides or repository-owned skills were found. Git history shows the r3 documentation amendment at the exact Web reference. The workstream is compatible and unresolved; no replacement or second workstream is needed. Tracked inventory and runbooks define no executable build/test/lint/CI commands.

Findings at the R4 base:

1. [Durable Documentation Rules](README.md#durable-documentation-rules) already asks for readable, outcome-first prose, but supplies no ordinary-message budget, purposes, exception rule, or meaningful-choice guidance. Add a specific interaction contract and replace that overlapping output bullet with a reference. This is an underspecified experience, not evidence that concise guidance is absent.
2. [Handoff and resumption](README.md#handoff-and-resumption) correctly requires snapshot, authority, changed material, evidence, and next owner. It does not explicitly distinguish the short human briefing from the full receiver packet. The scaffold's Delivery Summary repeats these prompts. Retain the evidence requirements while clarifying where they belong; no current rule explicitly requires a full report to be pasted into every chat.
3. Root [Collaborate Across Sessions and Tools](../README.md#collaborate-across-sessions-and-tools) leads quickly into advanced loop material before adoption. The operational [Transport Selection](ops/autonomous-review-loop.md#transport-selection) calls manual relay a fallback and describes a local coordinator. That is appropriate to the loop route but incomplete for ordinary human-mediated work with no controller. Make the normal human journey explicit and put advanced-loop detail behind its reference.
4. [Human-Coordinated Collaboration](README.md#human-coordinated-collaboration) has useful role and access boundaries; it does not provide a portable Web bootstrap, demonstrate decisions in conversation, or explain that both agents can contribute ideas. Keep provider-neutral reuse while making the requested human/Web/Codex arrangement the onboarding example.
5. [Approval Scope](README.md#approval-scope), [Work Classes](README.md#work-classes), and AGENTS Start Work already avoid full audits for conceptual questions and repeated approval for routine authorized work. Retain them. No contradictory unconditional question requirement was found; new menus must not introduce one.
6. Progress at the base contains 231 lines, including detailed r3 runtime/pilot material and historical summaries. These remain useful evidence but need not dominate r4's current decision. Retain exact pinned records and locally readable unresolved decisions. The 455-line canonical document and 135-line advanced reference are inventories, not usability scores or reasons for indiscriminate deletion.

Reported evidence: The user reports Web messages are too long and that reading becomes a bottleneck across projects. The supplied Web proposal suggests challenge framing and word limits. No portfolio-wide sweep, reading-speed measurement, live agent evaluation, or comprehension trial was performed.

Chosen target behavior: Plan an interface with concise decision-ready conversation, normal human relay, and detailed maintained memory. The exact limits, framing, and wording below are proposed defaults pending r4 approval.

Inference requiring validation: A consistent brief plus an accessible evidence record may reduce reading burden while preserving control. Shorter messages may also omit necessary context or feel mechanical; the later three-exchange trial tests that tradeoff.

Open decision: Approve or revise r4's local documentation scope. F3 acceptance, runtime implementation/activation, and the separate verdict clarification remain unresolved and are not prerequisites for preparing this plan.

## Proposed Interaction Contract

### Three layers and responsibilities

- Human conversation: Briefly explain the current result/problem and meaningful decision. Use a short orientation line at a material checkpoint or project switch, not a banner on every reply.
- Repository memory: Keep useful specifications, decision rationale, alternatives, approved scope, evidence, and verification in existing documents. Record proposals as proposals. Exclude raw internal deliberation, chat transcripts, repeated tool output, and speculative filler.
- Relay material: Prepare one self-contained task/review packet at a handoff or on request, with exact source, artifact, and bounded authority. Keep it separate from the ordinary briefing. A pointer replaces packet content only when the receiver can actually access that source.

The human owns priorities, material choices, scoped approvals, and acceptance. Web primarily explores, specifies, plans, and reviews identified evidence. Codex also contributes ideas, inspects the checkout, implements authorized work, verifies it, and maintains memory. These roles are emphases, not prohibitions on collaboration or a requirement to use three participants in every adopting project.

When Web cannot write repository files, it supplies a clearly labeled draft attachment or bounded relay text. It must not call that draft recorded repository state. Codex incorporates approved decisions and appropriate evidence under actual authority; copying a suggestion into progress does not approve it or make it canonical policy. If an attachment is unavailable, provide the necessary transferable text once, labeled as a draft, with a short covering message.

### Ordinary human briefings

Proposed rules for both agents:

- Aim for 60–140 words; ordinary substantive messages must stay within 180 words. Short answers may be much shorter. Never pad, split a long answer into consecutive messages to evade the ceiling, or copy a full attached deliverable inline as well.
- Lead with the result or decision. Include change, significance, material limitation, and next owner/action when relevant. Address one decision at a time, except inseparable choices needed for informed authorization.
- At a checkpoint/project switch, orient with project, outcome-oriented challenge, and the actual gate. Use exact canonical status names; a review checkpoint can be named without inventing a new lifecycle status. A short commit prefix is orientation only when unambiguous; complete base/candidate IDs remain in evidence and packets.
- Use everyday words, short paragraphs, and complete sentences. Explain an unfamiliar term with one concrete example when it affects the decision; keep precise identifiers where necessary.
- Avoid tables, nested lists, long inventories, generic encouragement, theatrical narration, emojis by default, empty fields, and repeated closing offers. Illustrative shapes are not mandatory forms.
- Report meaningful milestones, blockers, and necessary waiting information rather than every file read or tool call. Host communication requirements still apply. Conversation checkpoints do not introduce approval pauses during authorized work.
- Keep the smallest useful source reference beside consequential factual claims and full provenance in the record. Retain distinctions between verified checkout behavior, approved targets, inference, reported checks, and unknowns.

Explicit exceptions: A request for detail overrides the ordinary limit for that answer. Source code, full prompts, specifications, research artifacts, and relay packets are deliverables rather than ordinary briefings; put them in accessible files where possible with a short introduction. Safety, consent, scope, failure, and material uncertainty must remain visible even if the shortest sufficient explanation exceeds 180 words. Do not use exceptions for routine reports or hide an important failed check behind a link.

At every material checkpoint, the briefing, orientation, and specific reference together must reveal the real outcome, current gate/next owner, verified versus reported versus uncertain evidence, what a proposed decision permits, and where detail is accessible. Do not force five labeled fields into every answer or require opening a document to discover deployment risk.

### Message purposes and choices

Use only the parts needed:

- Exploration: Real problem, recommended direction and reason, next genuine decision.
- Plan checkpoint: Proposed outcome/boundary, main tradeoff, exact plan revision/reference, permission requested, and stopping gate.
- Implementation checkpoint: Meaningful change, actual checks and limits, user checks still pending, and local/published/deployed distinction.
- Review: Verdict and material findings first, independent versus reported evidence, optional advice separate from required corrections.
- Blocker: Cause, consequence, smallest unresolved decision, and affected boundary; continue independent authorized investigation where safe.
- Return after absence: Reconcile the current repository, then state goal, last verified result, outstanding risk, and next decision. Do not replay the entire history.

Offer options only for a material choice or a requested comparison. Recommend one with a reason; ordinarily provide at most three real alternatives, each stating an action and likely consequence/tradeoff. Do not invent durations, costs, benefits, or certainty; label estimates. No menu is needed for a direct conceptual answer or one sensible authorized next step. Options in a requested comparison do not justify unrelated follow-up suggestions.

An option selection can authorize only its unambiguous current scope. It cannot silently grant commit, push, PR creation/merge, deployment, live migration, destructive operations, or loop activation. Preserve each named action/target and approval reference. Stale or ambiguous option labels and reactions such as "nice" are not acceptance. Do not package high-risk permission as a playful shortcut.

### Challenge framing and natural controls

Propose an outcome-oriented display title in existing metadata, such as "Prevent duplicate submissions," alongside the stable workstream slug. Use challenge, checkpoint, and next move sparingly. Titles and plain/challenge presentation do not create another identity, status, register, or authority.

Show evidence-backed progress, such as two of three agreed scenarios verified with recovery pending. Avoid fictional points, arbitrary percentages, badges, streaks, levels, and leaderboards based on activity counts. Pauses, negative research results, and stopping are valid outcomes. Learning is optional and relevant to decisions; no mandatory quizzes. Plain presentation is available on request and changes no verification or permissions.

Ordinary phrases need no parser, CLI, or magic syntax:

- "Where are we?" requests a short status tied to identified evidence.
- "Explain this" or "show the evidence" requests focused explanation or supporting records; the former can use the detail exception.
- "What are the options?" requests a bounded comparison.
- "Prepare the handoff" prepares relay material; it neither sends it nor authorizes implementation.
- "Approve plan r4, local changes only" refers to the identified revision and local scope, with delivery still unapproved.
- "Accept candidate <identifier>" records artifact-specific acceptance, not unperformed checks or extra delivery rights.
- "Pause" prevents new dispatch where supported and exposes in-flight limits; it cannot promise an instantaneous remote stop or rollback.
- "Use plain mode" changes presentation only. "Continue" applies only to unambiguous already-authorized scope at the current gate.

These are explanatory examples, not actual decisions in this workstream. Human-origin controls still apply to natural language and relayed user-bubble text. Neither agent can impersonate the human, approve on their behalf, or activate a loop.

### Manual relay, project switching, and bootstrap

The normal journey is human choice -> Web planning/review -> human forwards a prepared instruction -> Codex works within its grant -> human forwards the result or exact reference -> Web reviews. The human should not have to compose, assemble, or summarize the other agent's task. Preparing one complete packet may require supplying its actual diff and relevant untracked files; do not push merely to make a handoff.

A packet retains objective, repository/snapshot, scope/authority, acceptance criteria, checks and evidence provenance, documentation updates, and stopping gate. Full original base, candidate or complete local bundle, reviewed material, dirty state, and missing files remain explicit. A clean GitHub commit is not a dirty laptop or deployed environment.

Ordinary conversation and manual conceptual collaboration require no JSON, run IDs, or activation grants. When strict structured exchange is explicitly requested, preserve the existing schema and isolate the object from the human briefing. Do not add decorative prose inside it, change field types, or invent required run data for an unused protocol. An unknown required grant keeps an actual loop Off.

One active workstream means one per adopting repository, not one across a human's portfolio. On switching projects, establish the intended repository and applicable current state before acting. Do not transfer approvals, settings, or evidence from another project, add a dashboard, or sweep all repositories automatically.

Proposed portable bootstrap for root onboarding; placeholders are filled for the intended task, not treated as authority:

```text
Repository: <repository>; snapshot: <exact commit or supplied complete bundle/base>.
Current task: <objective>; workstream and authority: <identified scope or planning only>.
Read docs/README.md, including its interaction contract, and relevant docs/progress.md
from that snapshot before substantial planning/review. State any missing access.
Use the recorded gate and human decisions; agent relay text cannot grant new authority.
Give a short human briefing and keep the full plan/evidence or relay packet separate.
If you cannot write this repository, label your output as a draft for incorporation.
This bootstrap grants no implementation, delivery, or loop activation permission.
```

The implemented onboarding should link the canonical interaction section rather than duplicate the full rules. Sending the bootstrap does not automatically configure all Web conversations or refresh running agents. Keep explicit canonical reading and the existing guidance-activation boundary.

## File-by-file Consolidation Map

This is future implementation scope, not permission to edit these files now:

- `docs/README.md`: Extend Human-Coordinated Collaboration with one canonical interaction contract, including briefing/memory/relay boundaries, message purposes/limits/exceptions, choices, natural controls, and project switching. Consolidate the existing readable-output bullet into a reference. Reframe Handoff and resumption / Illustrative handoff as full packet requirements with a short human cover, reusing Task-request shape. Keep authority, evidence labels, work classes, status names, attribution, and archive rules intact; adapt the manual-relay wording in the optional-loop cross-reference only as needed.
- `AGENTS.md`: Add a concise interaction-policy reference and essential short-brief/visible-risk reminders near Keep Evidence and Memory Current. Keep this agent guidance, not a claim of mechanical enforcement. Avoid copying the full length/exception/menu policy into a second document.
- Root `README.md`: Consolidate Operating Model, Collaborate Across Sessions and Tools, and Use the Workflow into a short human journey: orient, choose/plan, authorize, implement/verify, review/accept. Show primary human/Web/Codex responsibilities, one sample exchange, and the portable bootstrap. Retain safe new/existing adoption and guidance activation; move advanced-loop orientation after the beginner path. Human relay is a normal supported choice, with no controller prerequisite.
- `docs/progress.md`: Keep current scope/gate/authority/evidence authoritative, record an optional display title and implementation decisions if approved, and produce a brief cover plus complete handoff when needed. Replace instantiated drafting examples with concise useful results after implementation, retaining their exact source or approved record rather than erasing unique history.
- `docs/workstreams/WORKSTREAM_TEMPLATE.md`: Add one optional outcome-title prompt in metadata. Replace repeated Delivery Summary instructions with a concise canonical reference and prompts for a decision-ready human cover plus full accessible relay material. No new title/status block, role file, conversation template, or permission ledger.
- `docs/ops/autonomous-review-loop.md`: Clarify only in Transport Selection / Exchange Protocol introductions that normal human relay works without a loop/controller, and that human summaries sit outside strict objects. Retain every existing schema field, control/permission requirement, source limitation, and advanced procedure. The separate verdict issue below is excluded.

No planned edits to context, roadmap, technical debt, archive conventions or historical archives, operations/security indexes, or other files. Preserve meaningful local constraints on adoption; do not import upstream active state or approvals. No new permanent files are proposed.

## Preserved Invariants and Separate Finding

Preserve canonical workflow authority and host/tool constraints; one workstream per repository; the sole scaffold; evidence-first memory; quick/standard/high-risk classification; explicit direct execution and partial approvals; no repeated permission for routine approved work; separate delivery actions; truthful local/publication/deployment and artifact acceptance; actor-specific Codex attribution without identity changes; Completed versus Released; relocation-safe archives; default-off loop, human provenance, and all existing stopping/control constraints.

Separate finding V1, proposed clarification only: The operational Review response defines severity as impact and permits `ready_for_human` with no unresolved blocking findings, but neither an explicit blocking/disposition field nor a complete derived verdict rule identifies which findings block that verdict. The ambiguity remains at the R4 base. A minor requirement defect and a minor optional suggestion need different decisions; severity alone is insufficient. This is a document ambiguity, not a reproduced runtime failure.

Recommended separate follow-up: Specify a deterministic relationship between unsatisfied agreed criteria, finding disposition, and verdict; consider treating all unresolved requirement findings as blocking and keeping recommendations in optional_improvements before adding schema fields. Review compatibility under its own scoped approval. V1 is not accepted technical debt and is excluded from ordinary r4 approval; no protocol/schema/controller amendment is bundled into this presentation redesign.

## Fictional Experience Drafts

All examples below are independent fictional exchanges, not records of repository behavior, existing attachments, approvals, or checks. Bundle names and paths inside the messages are illustrative. In real use, a cited attachment must actually exist and be supplied; claims about its contents require evidence. E7a/E7b cover the requested return-and-explanation scenario. E6 keeps the material risk visible within the ordinary limit; an exception must be used if a real case needs more.

### E1 — New challenge

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Prevent duplicate submissions · Planning

A retry can currently create a second task. We need to decide what a repeated submission should mean.

I recommend returning the original task when the same request is retried. That protects against accidental duplicates.

A — Reuse the original task: fewer duplicates; callers must reuse a request identifier.

B — Create a new task each time: supports intentional repeats; accidental retries remain possible.

Choose the behavior to investigate. Neither option approves implementation yet. Draft tradeoffs: docs/progress.md#decisions-and-authorization.
```

### E2 — Plan checkpoint

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Prevent duplicate submissions · Awaiting plan approval

Plan r2 would make retries return the original task and test simultaneous submissions. The tradeoff is keeping a record of recent request identifiers.

I recommend approving r2 for local code, tests, and documentation only. That would let Codex implement and verify the listed scope, then stop for your validation. Commits, pushes, deployment, and loop activation remain unapproved.

The exact scope and checks are in docs/progress.md#implementation-plan. Your next move is to approve that scope or request a change.
```

### E3 — Codex implementation handoff

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Prevent duplicate submissions · Ready for user validation

The local B2 patch now reuses the original task. I ran the required automated checks, including simultaneous submissions; they passed.

One human check remains: retry a task through the interface and confirm that the result is understandable. Passing tests does not complete that check.

Nothing has been published or deployed. Please perform the interface check or report a problem. The complete B2 patch and verification record are in the attached review bundle; docs/progress.md#verification identifies its base and files.
```

### E4 — Web review with a correction

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Prevent duplicate submissions · Review checkpoint

One required correction remains in bundle B2: the handler accepts an expired request identifier, contrary to criterion AC2. I inspected the handler and tests; Codex reports the suite passed, but I did not rerun it.

I recommend correcting expiry handling and adding a boundary test within the approved scope before your validation.

Optional: a helper rename might improve readability; it does not affect this verdict or authorize more work.

Full finding W1: the attached Web review draft. It has not been recorded in the repository. Next move: forward that draft for Codex to evaluate.
```

### E5 — Clean Web review

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Prevent duplicate submissions · Ready for user validation

I found no required corrections in the complete B3 bundle against the agreed criteria. I inspected the changed handler and tests. Codex reports passing checks; I did not rerun them.

The interface retry check still belongs to you. Please try it before accepting B3.

This is a recommendation for human validation, not acceptance or delivery permission. There is no reason to add another improvement round. Evidence: the attached review draft, with B3's exact base and file list.
```

### E6 — Blocker and safety exception

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Recover safely · Blocked

The restore rehearsal failed: the backup could not recreate the latest records. A live migration could leave us unable to recover lost data, so it remains blocked.

I recommend allocating separate test storage and rehearsing recovery there. That expands the approved infrastructure scope and needs your decision before preparation. It would not authorize the live migration or deletion of data.

I can continue the already-authorized read-only diagnosis. No live data was changed. The failure and proposed storage boundary are in docs/progress.md#verification.
```

### E7a — Return after a week

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Prevent duplicate submissions · Ready for user validation

I checked the current checkout: B3 still matches the handoff from a week ago. The agreed automated checks passed in that recorded snapshot; they have not been rerun today.

Your interface retry check remains pending. No publication or deployment is recorded.

The next move is to try that behavior and decide whether to accept B3. The scoped record is in docs/progress.md#verification.
```

### E7b — Requested deeper explanation

Purpose: Focused explanation explicitly requested by the human; the length exception is available but need not be used.

```text
A successful build shows that the program can be assembled. It does not prove that two requests arriving together create only one task.

Imagine two people asking for the same seat at almost the same moment. Both can see it as available before either finishes booking it. The program needs a rule that makes checking and claiming the seat one protected operation.

Our retry design has the same problem. The simultaneous-submission test checks that only one task is created and both requests receive the agreed result. The interface check asks a different question: can you understand that result when using the product?

The B3 design rationale and test evidence are in the supplied bundle. I inspected the design; Codex's test results remain reported evidence here. Neither kind of evidence replaces your acceptance decision.
```

### E8 — Handoff with an untracked file

Purpose: Ordinary human briefing; fictional, not a report or authorization for this repository.

```text
Example project · Explain retries · Review checkpoint

GitHub alone is insufficient for this review. The local B4 patch includes an untracked docs/retry-example.md that is absent from the published commit.

I recommend forwarding the prepared B4 bundle: the tracked diff, that file in full, and the relevant policy. The packet names its exact base and missing evidence, so you need not assemble a summary.

Web should review only that identified material and state any access limits. Preparing the packet does not send it or authorize further changes. No push is required.
```

## Implementation Plan After Approval

The following steps remain unstarted and depend on explicit approval of r4's local scope.

- [ ] Reconcile the actual checkout and approved portions of r4; preserve intervening edits and acceptance state. Record the approval actor/reference and permitted revision/scope before normative edits.
- [ ] Consolidate the interaction contract and packet/brief distinction in canonical policy; align root onboarding, AGENTS, and scaffold using the file map. Keep the advanced protocol change limited to the presentation boundary.
- [ ] Read the complete resulting diff and every changed example. Verify limits/exceptions, actionable choices, human-origin/approval boundaries, draft versus recorded evidence, exact snapshot/missing-file handling, plain mode, and off-loop behavior. Run existing applicable checks, local link/anchor checks, and `git diff --check`.
- [ ] Prepare the actual review candidate and complete relay material when requested; leave user-owned checks Pending and stop at Ready for user validation. Separately arrange the three-exchange readability trial through ordinary human interaction; no automated agent evaluations or live transport.

Implementation acceptance criteria:

- AC1: Both agents can find one actionable output contract: 60–140-word target, 180-word ordinary ceiling without padding, concise purposes/choices, and explicit detail/material-risk exceptions.
- AC2: Manual human relay works as the normal workflow without a controller, browser automation, strict JSON, fabricated run IDs, or loop activation; preparation is separate from sending and authority.
- AC3: Challenge/plain presentation and display titles change no canonical lifecycle, permissions, evidence requirement, repository identity, or human acceptance.
- AC4: Decisions state consequences and boundaries; options are bounded and meaningful, while conceptual answers and routine authorized implementation do not acquire unnecessary questions or pauses.
- AC5: Detailed rationale/evidence remain retrievable in the right existing documents or clearly labeled supplied drafts. No invented repository writes, hidden material risk, duplicate state register, or full-transcript memory.
- AC6: Human briefings and requested strict exchanges remain separate and compatible; schema types/fields, loop provenance, and runtime controls remain unchanged. V1 remains separately scoped.
- AC7: Root onboarding, one sample exchange, and portable bootstrap demonstrate the experience without requiring the human to read the advanced operational reference. Agents still explicitly read applicable canonical policy and relevant state.
- AC8: All eight draft scenarios have an understandable outcome, material limitation, next decision/owner, authority boundary, and accessible-source treatment where relevant. Counts are a check, not evidence of comprehension or enjoyment.
- AC9: Existing checks pass or limitations are reported; preserved invariants and link-safe history remain intact. Readability/user acceptance stay pending until actual human feedback.

## Migration, Risks, and Human Trial

Migration approach: Approve before editing policy, then consolidate in place within the six mapped files. Preserve existing anchors where useful or update every affected local reference deliberately. Do not rewrite archives or invent a new accepted artifact. Web sessions receive a portable bootstrap or supplied policy; file edits alone establish no automatic instruction loading. Preserve the handoff before any documented reload/new session; no automatic restart is part of the plan.

Risks and controls: A word cap can hide risk, so apply the visible material-risk exception and review examples for omitted consent context. Uniform forms can feel robotic, so purposes are illustrative and menus appear only for real choices. A challenge label can trivialize consequences or imply progress, so use real outcomes, exact gates, and verified counts only. More content in documents can become clutter, so retain decision rationale and reproducible evidence rather than message transcripts. A local-only reference can frustrate Web review, so prepare one complete transferable packet and disclose missing access.

Later trial proposal: Observe three real, naturally occurring exchanges after implementation: a Web plan/choice checkpoint, a Codex verified handoff, and a Web review/human-validation checkpoint. For each, record the brief/source artifact, actor and inspected snapshot, actual user feedback on what changed, what is uncertain, and what the next decision permits; note requests for missing context and whether the style felt clearer or more enjoyable. Collect feedback conversationally, with no quiz requirement, invented score, time-saving claim, or API/model evaluation. A gap prompts a focused wording/context correction and recheck. If opportunities or feedback are absent, mark the trial Pending. The user chooses challenge/plain preference and accepts the identified candidate; proposed benefits remain hypotheses meanwhile.

Rollback: For this planning task, reverse only its progress.md hunks if later requested, preserving the published r3 record and any intervening edits. For future implementation, reverse only approved local presentation hunks; do not reset repository state, archives, or attribution. No deployment, migration, live-data operation, or runtime observability change applies to this documentation-only plan.

## Verification of This Planning Patch

Check: Repository state, instruction/context review, publication, and historical retrievability.

Basis: Codex ran `git rev-parse --show-toplevel`, `git branch --show-current`, `git rev-parse HEAD`, `git status --porcelain=v1 --untracked-files=all`, staged/unstaged diffs, `rg --files`, full required document reads, `git log -4`, `git diff --name-status 3d0ee387c9a6b993c1066139c87be58c5eaffcc0 HEAD`, sanitized remote inspection and `git ls-remote origin refs/heads/main`; `git cat-file -e <revision>:docs/progress.md` for the three historical references.

Scope: R4-start on 2026-09-06 at the exact supplied a9f3379 base; primary coding-agent observation.

Result: Passed. Clean main checkout, no pre-existing/staged/untracked work, compatible active workstream, 14 Markdown files, and remote main at the same full commit. All three pinned historical objects are locally available. No unrelated workstream was replaced.

Limitations: Remote publication proves neither human acceptance nor who performed Git actions. Historical source/capability and agent checks are retained as reported evidence, not re-fetched or rerun here. No browser or runtime evaluation was used.

Check: Word limits and decision clarity of the fictional messages.

Basis: One-off read-only inline PowerShell extracts the nine fenced message bodies under E1–E8 and counts non-whitespace tokens, including orientation lines. Codex manually compared each with the user's requested scenario and the proposed outcome/limitation/decision/authority requirements.

Scope: P4 draft examples on 2026-09-06; document-level inspection only.

Result: Passed. Eight ordinary briefings are within both the 60–140 target and 180 ceiling: E1 85, E2 87, E3 89, E4 103, E5 88, E6 88, E7a 72, E8 91 words. Requested explanation E7b is 133 words; eligibility for an exception did not require making it longer. No examples were padded to reach a minimum.

Manual scenario decisions:

- E1: A meaningful choice has a recommendation, real consequences, and planning-only authority; neither option approves implementation. Passed.
- E2: Exact fictional plan revision and local scope are reviewable; the next human approval excludes delivery and activation. Passed.
- E3: Codex's performed checks and one pending human check are distinct; local work is not published/deployed. Passed.
- E4: Web identifies an inspected defect and violated criterion, labels tests as reported, separates optional advice, and does not claim its draft was incorporated. Passed.
- E5: Clean review ends at human validation, without new improvements, acceptance, or delivery permission. Passed.
- E6: Recovery failure and live-data consequences remain visible; expanded infrastructure needs a decision while already-authorized read-only diagnosis can continue. Passed.
- E7a/E7b: Return rechecks checkout identity without falsely rerunning old tests; requested detail explains the distinction between build/test/user evidence with a concrete example. Passed.
- E8: A missing untracked file prevents a GitHub-only review; a prepared complete bundle avoids asking the human to assemble the other agent's task. Passed.

Limitations: Counts and editorial walkthroughs demonstrate neither user understanding/enjoyment nor future agent compliance. Example bundles, checks, and outcomes are fictional. The actual three-exchange trial and human validation are Pending.

Check: Complete planning patch, preserved normative files, links/anchors, metadata, hygiene, and existing checks.

Basis: Original and amended progress text and full diff inspection; `git diff --exit-code HEAD -- . ':!docs/progress.md'`; `git diff --cached`; status/untracked inventory; read-only inline PowerShell over all tracked Markdown for relative paths/heading anchors, current metadata uniqueness, changed-file scope, Markdown tables, conflict markers, and credential/personal-detail patterns; `git diff --check` and `git diff --cached --check`. Inventory and runbooks, plus `git ls-files -- '*.yml' '*.yaml' 'package.json' 'pyproject.toml' 'Makefile' '*test*' '*lint*'`, checked for existing executable checks.

Scope: Local P4 planning patch and all 14 tracked Markdown documents. Example paths inside code fences are explicitly fictional data, not claimed repository links.

Result: Passed. Only progress.md is modified and unstaged; index and untracked inventories are empty, with all thirteen other tracked files unchanged. The link/metadata/hygiene scan covered 14 Markdown documents, 86 local links, and 47 anchor references with no issues; Git whitespace checks exited 0. No executable repository tests/lint/build/CI checks are defined, and no pre-existing check failure was found. The final evidence/metadata edit receives the same focused consistency/whitespace check.

Limitations: A focused Markdown/pattern inspection is not a comprehensive parser or secret detector. No policy implementation, live browser transport, automated agent evaluation, new harness, or user-comprehension result is included. No permanent checking script was created.

## User-owned Checks and Pending Decisions

- [ ] Approve proposed r4 local documentation scope or identify changes/partial approval.
- [ ] After any authorized implementation, review the identified candidate and preserved authority/evidence boundaries.
- [ ] Supply feedback from three real exchanges when available; no readability/enjoyment result is recorded yet.
- [ ] Provide artifact-specific or explicit cumulative acceptance when intended; F1/F2/F3 acceptance is not inferred.

No implementation choice blocks preparation of this plan. Default challenge presentation and the proposed message limit are recommendations for the r4 decision, not already adopted policy. The human owns any future V1 clarification, runtime scope, activation, and delivery decisions.

## Delivery Permissions

All apply to r4. Every listed action remains unapproved; this planning request grants none of them.

- Staging: Unapproved.
- Commit: Unapproved.
- Push: Unapproved.
- Branch creation or checkout: Unapproved.
- Worktrees: Unapproved.
- PR creation: Unapproved.
- PR merge: Unapproved.
- Deployment: Unapproved.
- Live-data operations: Unapproved.
- Destructive cleanup: Unapproved.
- Production promotion: Unapproved.
- Automated relay/reviewer sending: Unapproved; packet preparation only.
- Loop activation: Unapproved.

## Historical Evidence and Unresolved Acceptance

These are scoped historical summaries, not reruns. Full prior plans, decisions, check details, exclusions, and pending checklists remain at exact pinned revisions, whose progress objects were verified available locally. Navigation links are not evidence of current Web access.

- r1/F1: [Record at 86554d0](https://github.com/edwardansberg/progress-driven-sdlc/blob/86554d0f2be7c6b947031fc3e27c1d6f0d7a63da/docs/progress.md). Initial local policy/collaboration/adoption/lifecycle amendment against dfe3667ea37b41ba6de948ca1253930a23d7d093, under its own direct-execution request. Codex reported six unstaged files, no staged/untracked work, 79 local links/43 anchors across 13 documents, whitespace/hygiene checks, ten scenarios, and a specialist-driven proposed/approved scope correction. User validation remained pending.
- r2/F2: [Record at 3d0ee387](https://github.com/edwardansberg/progress-driven-sdlc/blob/3d0ee387c9a6b993c1066139c87be58c5eaffcc0/docs/progress.md). Separate local correction request against 86554d0f2be7c6b947031fc3e27c1d6f0d7a63da; six unstaged files. Reported 20 positive archive-fixture assertions, six displaced targets in a negative control, 33 actual progress relocations, 93 links/58 anchors across 13 documents, whitespace/hygiene and six scenarios. Observation scope, relocation-safe archives, guidance activation, and actor attribution were corrected; fresh-session tests were skipped and acceptance remained pending.
- r3/F3: [Record at a9f3379](https://github.com/edwardansberg/progress-driven-sdlc/blob/a9f3379ff42d115f46788a6c0a785f9f2cdb7ad9/docs/progress.md). Direct execution covered documentation/protocol and a proposed pilot only, against 3d0ee387c9a6b993c1066139c87be58c5eaffcc0. Codex reported six unstaged files plus the new operational reference; 105 links/66 anchors across 14 documents, whitespace/scope/hygiene and ten document scenarios passed. CLI/desktop metadata, help surfaces, GitHub reads, and five official-source reads were observed; no automated relay, control enforcement, instruction-loading evaluation, or runtime implementation was demonstrated. The one-round review-only pilot, service-permission uncertainty, exact-target/control prerequisites, and separate implementation/activation gates remain unapproved.
- Current unresolved state: No F1/F2/F3 user acceptance or previous user-check completion is supplied. Historical no-delivery statements concern Codex's respective tasks, not later publication or command actors. The observed main commit now contains r3; publication is not acceptance. V1 qualifies the earlier document-level consistency conclusion with a newly identified ambiguity, without pretending earlier checks were rerun or changing their scope.

## Transferable P4 Review Packet

Prepared agent-origin relay material, not sent and not a human instruction. This packet is a draft inside the existing local file; it requires the actual P4 file as an attachment or other accessible transfer. Do not point Web to published main and claim it contains the new plan.

```text
Origin: Codex-prepared review packet; no human approval is conveyed.
Objective: Review proposed r4 human-led challenge presentation for clarity,
informed control, and preservation of existing SDLC authority/evidence.
Repository: edwardansberg/progress-driven-sdlc; branch main.
Inspected base: a9f3379ff42d115f46788a6c0a785f9f2cdb7ad9.
Workstream: human-coordinated-agentic-development; proposed plan r4.
Artifact: P4, the supplied complete local docs/progress.md against that base.
Initial checkout clean; final patch only docs/progress.md, unstaged; no untracked files.
This single supplied file contains the plan, examples, and this packet; no separate
diff is needed for the planning review. Read it, then applicable canonical guidance and
dependencies from the exact base. Request only inaccessible required material.
Authority: The human requested planning and progress.md updates only.
Review scope: Proposed contract, consolidation map, examples, AC1-AC9, and trial.
No normative implementation, delivery, sending, or loop activation is granted.
V1 protocol-verdict semantics are recorded separately and excluded.
Evidence: Use Verification of This Planning Patch for actual check outcomes.
Example outcomes are fictional; word counts do not establish comprehension.
Distinguish independently inspected plan text from Codex-reported checks.
Documentation: Return a labeled review draft for human relay; do not claim repository writes.
Stopping gate: Awaiting plan approval; Loop control Off. Report concrete plan defects
or a recommendation for the human decision. Neither is user approval or acceptance.
```

## Progress Log and Delivery Summary

2026-09-06: Inspected the exact reviewed checkout and all framework documents. Identified missing interaction specificity, an unclear briefing/packet boundary, and manual-relay onboarding emphasis. Confirmed existing protections against unnecessary approval questions; reproduced V1 as a separate proposed clarification. Recorded r4 within the compatible active workstream without normative edits.

2026-09-06: Completed the eight requested scenario walkthroughs and counted all nine draft replies, including the requested explanation. Inspected the complete planning change and historical preservation; link/scope/metadata/hygiene and whitespace checks passed. No blocker to the requested planning gate or scope departure remains.

Reviewable result: Local-only P4 in this progress file contains the proposed contract, six-file future implementation map, fictional examples, acceptance criteria, migration/verification approach, human trial, and ready-to-forward review packet. The complete file is sufficient as a planning-review attachment; Web cannot obtain this local amendment from published main. No packet was sent. Rollback is limited to this task's progress.md hunks while preserving later unrelated work.

During r4 planning, Codex changed only this file and performed no normative policy implementation, runtime/controller/model evaluation, browser automation, loop activation, staging, commit, push, branch/worktree or PR action, deployment/live-data/destructive operation, dependency installation, configuration/credential/identity/signing/attribution or global instruction/installed-skill change, downstream edit, or history rewrite. Prior user checks remain pending; no acceptance, release, or closure was inferred. The current gate and next owner are recorded once in the metadata above.
