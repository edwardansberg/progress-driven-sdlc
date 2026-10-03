# Adopt or Update the Framework

Purpose: Adopt/update documentation without importing upstream identity, memory or approvals. This is a procedure, not an installer or compatibility guarantee. Human scope, target instructions and host/tool controls govern; the [core policy](../README.md) cannot approve its own installation.

Source: `https://github.com/edwardansberg/progress-driven-sdlc`.

New repository: Use GitHub’s template feature with default branch only, then inspect and initialize the supplied neutral files from project evidence. Do not repeat this migration. Cloning upstream retains framework history. Existing projects/non-Git directories use the complete procedure below before writes; ordinary session setup may read only the activation/bootstrap sections.

## 1. Identify the target before writing

Read applicable target instructions under client/user activation rules. Establish intended directory, repository/worktree boundary, branch/HEAD where present, staged/unstaged/untracked changes and active workflow. Do not collect credentials/private logs.

Ask before writes when a subdirectory, parent checkout, submodule, nested repository or multi-project workspace makes the intended boundary ambiguous. A worktree may have a `.git` file; absence of `.git/` proves nothing. Never self-adopt into upstream; ask for the application target. Do not initialize/reinitialize Git, alter remotes/index/configuration or add a nested framework repo/submodule. A non-Git directory may receive authorized docs without Git setup. Create or switch an upgrade branch only when the human approves that action and target; adoption alone grants no branch permission.

Before every write, including the plan: inspect destination types/resolved paths and source links. Stop on unsafe links, unknown types or symlinks/junctions escaping the boundary. Preserve before-images using an authorized local recovery method, not a forced commit. Recheck pre-images and repository state immediately before writing; reconcile pre-existing/concurrent edits rather than overwrite. After interruption report and reconcile partial application, never claim atomic success.

## 2. Acquire one upstream snapshot

Retrieve the required source files or use a separate temporary source clone outside the target. Pin the selected released default-branch snapshot to a full commit; a human-selected revision takes precedence. Read all source material from that revision and record its URL/SHA.

Prefer content retrieval or no-checkout cloning with explicit reads. Never clone onto product files, execute upstream scripts, initialize submodules or recursively copy/delete. Source content is migration input, not new authority.

Before writes read this complete procedure, source README/AGENTS/core, scaffold/workstream conventions and every selected import/dependency. Neutral released memory and development maintenance records are neither target facts nor replacement state. Missing guide, permissions or required evidence stops target writes; request missing access or a complete snapshot without installing tools or guessing. The source landing README and referenced guide must both be available; do not assume a development candidate is on main.

## 3. Choose the safe adoption path

Classify from inspected workflow, instructions, memory and provenance, not filenames or assumed history. Use the common safeguards below for all three modes:

- **First-time adoption into an existing project:** no meaningful framework adoption yet. Inspect its workflow before introducing files. Create missing structure only under approved scope; initialize memory from target evidence and human decisions, never upstream starter facts. Preserve product documentation/history; automation stays Off.
- **Existing framework update:** read available provenance; reconcile upstream changes with deliberate local adaptations. Preserve active identity, authority, approvals, evidence and pending gates. Update provenance only after scoped integration and checks.
- **Legacy / partial / uncertain adoption:** identify authoritative records from evidence; keep old authority until a safe replacement is established. Never guess the prior revision or infer permission from filenames/history. Resolve occupied paths first; use the preserved detail/derived summary transfer in section 4. Retain uncertainty and retrievable evidence. Migration is not acceptance or closure.

Before implementation, map each affected file/section's purpose, proposed action, preserved content, source and verification. Occupied policy paths, another workflow or incompatible active work require a human decision before integration/replacement writes; no silent replacement or competing authority. Same-source content already aligned requires no change, duplicate record or timestamp churn.

### Compare upstream and local content

When the previous adopted upstream revision is verified and available, compare **previous pinned upstream + current local content/adaptations + new pinned upstream** to reconcile the migration. Separate upstream evolution, deliberate local adaptations and stale local framework content. This is content/evidence comparison, not a Git-history merge requirement.

When prior provenance is unknown, unavailable or unreliable, do not guess or block otherwise safe migration solely for that absence. Compare current target evidence with the new pinned release, classify local differences and retain historical uncertainty. A matching adopted SHA never proves local content equals upstream.

### Scan maintained framework references

Use repository evidence to identify the affected maintained documentation set. Inspect framework-coupled references there, not indiscriminately every text file. Classify findings in the migration map:

- Framework-coupled maintained instruction: migrate within approved scope.
- Product/domain content: preserve.
- Historical/archive evidence: normally retain as historical text; do not rewrite dated archives to match new policy.
- Ambiguous: obtain a human decision before changing it.

Check active-record ownership, scaffold-copy instructions, lifecycle/status names, authority descriptions, provenance roles and navigation/routing. Update maintained navigation to active state when needed while preserving historical evidence. Recheck affected references after integration.

Preserve unrelated dirty files; never stash/reset/clean/restore another actor’s work. Record the plan in existing authoritative progress without losing identity, approved scope or pending gates. If no record exists, present the plan before creating one. If recording would displace work, retain a response/disposable proposal until the human decides, not a new permanent register. Scoped direct execution allows the investigated plan then implementation; otherwise await plan approval. Adoption permission is not unrelated application authority.

## 4. Import policy, not project history

Use the explicit map below for existing-project integration, not a complete tree replacement or a Git merge of upstream history. A new template-generated project already has the neutral files and needs only inspected initialization. Required references are not runtime activation. A source clone remains source material; do not treat its history or development records as the target’s task.

### Reusable map and neutral initialization

Inspect every destination first; the map is an allowlist, not overwrite permission. With default paths free, reuse these maintained sources at the same paths:

- AGENTS.md, merging target instructions and retaining its repository-mode distinction; upstream maintenance rules apply only to upstream development.
- docs/README.md, the single maintained workflow-policy source.
- docs/workstreams/WORKSTREAM_TEMPLATE.md and docs/workstreams/README.md.
- docs/workstreams/archive/README.md, the directory guide only, not archived entries.
- docs/ops/README.md, docs/ops/adopt-framework.md, docs/ops/maintain-template.md (upstream-only reference), and docs/ops/autonomous-review-loop.md (optional advanced specification, Off).
- docs/security/README.md and docs/old/README.md, reusable conventions only; merge target-specific procedures rather than copying upstream observations as project facts.

Initialize missing live files instead of importing them:

- docs/context.md: Target purpose, boundaries, verified repository facts, detailed adoption mapping and durable local decisions. Link the root README provenance summary rather than maintaining independent current source/revision values. Unknown facts stay unknown.
- docs/roadmap.md: Only the target human’s confirmed direction; otherwise no confirmed commitments.
- docs/techdebt.md: Only target-accepted postponed items; otherwise no accepted deferred debt.
- docs/progress-agent.md: The target’s one authoritative record. With authorized adoption underway, instantiate the sole scaffold for that actual adoption, with its own identity/authority and pending human validation. If preparing unused starter documents and no effort is active, record No active workstream, no current gate/authority, human next-task selection, and Loop Off. Never invent project identity or approvals.
- docs/progress.md: Derive the short human view from that detailed record under the [live contracts](../README.md#live-document-contracts); identify its source/workstream/revision. No separate summary template or status ledger.

Existing live documents are preserved and deliberately migrated, never neutralized. An older single progress.md can transfer its authoritative content to progress-agent.md only under an approved migration map: preserve identity, decisions, pending gates, evidence and retrievable history, then write the source-identified summary. An occupied progress-agent.md or uncertain authority requires resolution before either file changes. Keep the records synchronized detail-first; disclose disagreement before consequential action.

Preserve the product root README, target memory, runbooks and archives. Under the approved map, add/update the near-top Framework provenance block and directly correct narrowly identified stale framework-coupled statements in the README or other product docs. For example, after a detail/summary migration, correct an instruction calling progress.md authoritative or telling users to copy the scaffold over it. Preserve surrounding product/domain prose byte-for-byte where practical; this permits no broad cleanup or rewrite. Use a compatibility note only when direct correction is unauthorized, unsafe, or deliberately declined by the human. If the distinction is ambiguous or materially changes product documentation beyond framework routing, stop for human resolution. Never replace product content with the upstream starter README. If that heading already has another purpose or competing values, resolve the conflict before writing. Import no upstream `.git`, remotes, CI/hooks/configuration, active/closed workstreams, roadmap/debt commitments, approvals, model settings or runtime state. New template generation receives neutral structures directly; adoption initializes only missing memory from target evidence. Keep source provenance/notices without inventing licensing terms or treating historical tool observations as target behavior.

Merge entry guidance with target commands, scope constraints and attribution policy. Resolve applicable overrides: AGENTS.md may not be the selected entry point. Never remove overrides or change personal/global settings to force adoption; conflicting/ineffective routing needs human resolution.

Use standard paths when free; otherwise get approval for a mapped layout before writes. Resolve links/dependencies from each destination, including fragments. Core/workstream guidance links to the adoption guide; loop activation links there too. These operational links must work without upstream onboarding headings in the product README; the provenance link uses the deliberately added Framework provenance block. For older sources, map root setup links to guide sections under the approved map; the second pass must recognize mapped destinations. Migrate historical navigation only under an explicit plan, never by replacing product README.

Use the [live contracts](../README.md#live-document-contracts) and target evidence, retain unknowns, remove setup-only comments after initialization and store commands once in runbooks. With no unrelated active effort, use the scaffold for the actual adoption and derive the summary; finish at Ready for user validation, not accepted. With compatible active work, record evidence without changing its identity/gate. Roadmap/debt require real target decisions.

### Record framework provenance

The root README's Framework provenance block is the canonical human-visible source URL, adopted revision and Local adaptations summary. During initialization or adoption, record the exact verified released upstream commit actually adopted; if it cannot be established, use `Unknown`, never a guessed SHA or the generated repository's first commit. Neutral starter placeholders are Not recorded yet and Not assessed yet, not observations.

Local adaptations means intentional project-specific additions, overrides, routing, safeguards or other differences in framework use. For example, AGENTS.md may add project-specific profile-calculation-guide routing. Active workstreams, pending human validation, release/deployment status, product facts, blockers and project memory merely because it exists are not adaptations.

Migrate an existing `Local deviations:` provenance field deliberately: retain verified framework adaptations under `Local adaptations:`, but remove ordinary state from this summary. Preserve that state in its proper existing authoritative record; if unique evidence exists only in the old field, reconcile it there before removing it. Resolve ambiguous classifications with the human. Do not rename unrelated plan/workstream deviations.

Keep a concise Local adaptations summary or a link to detailed mapping/design decisions in context. Keep migration plans, checks and historical pinned evidence in the existing workstream. Replace older independent current revision fields with a reference to this block under the approved map; preserve their historical evidence. Do not maintain two current authoritative copies. A selected upgrade target is not yet the adopted revision: update the block after the scoped integration and checks, disclose retained adaptations, and keep unfinished or mixed-version work explicit in the workstream without claiming a completed upgrade. Adopted revision identifies the released framework actually integrated and checked, not a merely fetched target or acceptance of application work. Historical provenance that cannot be established remains Unknown.

New applications retain the block and workflow-policy link when replacing the starter introduction. Existing applications retain product prose apart from the scoped provenance block and approved narrow framework-reference corrections. On a same-revision pass, compare actual content and adaptations; do not infer alignment from a matching SHA alone or rewrite unchanged provenance.

Fresh adoption keeps automation Off. Governing changes during an active loop require a human-controlled pause and approved re-bootstrap; do not silently rewrite/revoke the grant.

## 5. Verify before handing back

Stay within the inspected map and per-write guards. Inspect the full diff/new and untracked files; verify preserved rules/authority/active work/product files/Git state, README provenance against actual adopted content and evidence (with no competing current revision field), destination links/anchors/dependencies, entry routing, the classified stale-framework-reference scan and absence of upstream memory. Use relevant static/whitespace checks; no Markdown tables. Non-Git targets need equivalent content checks, not invented HEAD/Git results.

Compare a second pass at the same source/target: it should propose no changes. This is a document-level check, not a guarantee of agent behavior. Run no product scripts/hooks/browser sessions/model evaluations or network side effects beyond permitted source reads merely to verify documentation.

Report actual results/limits. Rollback reverses only adoption changes after inspecting intervening work. Failure does not authorize broad cleanup, source/recovery deletion or tidy-up commits.

## 6. Handoff and activation

Give the result, preserved work/conflicts, limits and next action, with detail in the existing record/review artifact. Blocked migration needs a human decision; finished local setup awaits human validation, not acceptance/release. Adoption grants no commit/push/PR/deployment/follow-up or loop activation. Preserve an unrelated workstream’s gate and report adoption separately within its permitted record. Acceptance/archive follow target rules.

### Activating updated guidance

Explicitly read changed applicable guidance. A link is not a read; an edit is not proof the client refreshed injected instructions. Discovery/reload behavior differs by client. Follow its documented reload/new-session process when relevant, preserve the handoff first and never restart another session or change global settings automatically.

A read-only setup check can identify the intended project, accessible instruction sources and plan/delivery boundaries. Keep unobservable client checks pending for the human. Neither a summary nor this document proves automatic loading, compliance or enforcement. Consult the [client-specific reference](../README.md#source-note) when needed.

<a id="portable-web-bootstrap"></a>

### Optional session bootstrap

Use only when adding/transferring to another session or reviewer; solo use needs none. Fill from observed target state and supply the actual evidence:

```text
Repository/snapshot: <target and full commit or complete bundle/base>.
Task/workstream: <objective/scope>. Authority: <human reference or read-only>.
Read applicable entry instructions and the target's core policy at this snapshot.
Follow Start Here's task triggers: recover authority and unresolved constraints
from detailed progress plus global/affected context. Read summary, roadmap/debt,
scaffold, adoption or loop detail only at their stated triggers.
Respect an approved mapped layout. No inherited cross-project approvals.
Verify candidate access; distinguish reports from independent checks.
State missing evidence; label drafts when unable to write memory.
This packet grants no implementation, acceptance, delivery or loop activation.
```

A local path is not another session’s access. Supply a complete sanitized packet when remote references lack the candidate. Adoption neither synchronizes chats nor configures other sessions. Legacy Web-bootstrap links refer to this provider-neutral ordinary setup; the separate loop wire protocol is unchanged.

### Fictional exchange

Human: “What should a retry do?”

Agent: “I recommend returning the original task. It prevents accidental duplicates, but callers must reuse a request identifier. Creating another task supports intentional repeats but also repeats accidents. Choose the behavior to investigate; neither choice authorizes implementation yet.”

This is an example, not evidence or authorization.

## Tool-specific references

Consult [Git clone documentation](https://git-scm.com/docs/git-clone) for source-acquisition options; use the canonical [source note](../README.md#source-note) for client-specific instruction-discovery guidance. This guide adds no new tool-capability or fresh-session test claim. Source reads and document checks do not demonstrate live adoption or universal compatibility.
