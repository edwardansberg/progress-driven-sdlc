# Codex work request: standing agreements, autonomous collaboration, and clear progress

Work on `edwardansberg/progress-driven-sdlc`:
https://github.com/edwardansberg/progress-driven-sdlc

## 1. Outcome

Revise the framework so a business-domain expert can direct software development through goals, material decisions, and result review. The coding agent should own investigation, technical planning, implementation, verification, and project-memory maintenance within the authorized scope.

Deliver four connected improvements:

1. Agent-maintained documents that support accurate execution and resumption with selective context loading.
2. A control-panel-first design convention for new interactive applications, with consistent navigation, useful status, and keyboard/pointer access.
3. A simple, lightly gamified `docs/progress.md` that contains the same checkpoint briefing as the agent's final development update.
4. A standing working agreement with commit-and-push enabled by default, and substantial work packages that the agent can execute between relatively infrequent human decisions.

Make the guidance direct and operational. Explain the work an agent should undertake instead of making promotional claims about unused AI power. Treat improvements in productivity, enjoyment, comprehension, and business outcomes as hypotheses to evaluate.

## 2. Authority and completion boundary

This request authorizes repository inspection, relevant research, safe branch/worktree setup, a written plan, implementation of this documentation workstream, proportionate local checks, and disposable verification fixtures. It also explicitly authorizes staging, creating commits, and ordinary non-force pushes of this workstream's changes to its verified development branch on `origin` in `edwardansberg/progress-driven-sdlc`. Establish the exact branch during baseline inspection. Preserve unrelated work and use the available environment without adding paid services or dependencies.

Investigate and record the bounded plan before implementation. Then continue through implementation and verification without another plan-approval question for the scope defined here. Do not stop after producing a plan or after the first edit batch.

This instruction supersedes the earlier prompt's local-only publication restriction for this workstream. Do not ask again for routine staging, commits, or pushes covered here. PR creation, reviewer messaging, merging into main or another integration branch, deployment, repository-setting changes, live-data operations, and workplace pilots retain their separate authorization requirements. Honor any separately established, still-valid authority for named actions in this session. Do not import approval from another project or historical task.

Keep the optional execution/review controller Off. Sustained work in the current authorized coding session is distinct from activating that controller, launching unattended sessions, or creating recurring work. Revised repository policy cannot expand the authority of this session.

Finish at a published development-branch review candidate with checks, limitations, and the next human action recorded. Verify that the intended commits reached `origin`. If publication is blocked, preserve the local candidate and report the exact unpublished work and cause; do not describe that state as fully synchronized. Stop affected work for a material unresolved business decision, unsafe conflict, unavailable necessary evidence, or scope expansion. Continue independent authorized work where useful. Identify the specific constraint and smallest decision when blocked.

A long session should follow from necessary work. Do not add tasks, repeated reviews, or arbitrary time targets to make it longer.

### Standing working agreement

Implement a concise default action set that humans and agents can rely on across sessions. Make it easy to find in `AGENTS.md`; keep full procedures in the canonical core and reference them. Keep the adopted project choices and real human authorization reference in one durable home, normally `docs/context.md`. The active work record references that agreement and records workstream scope or exceptions. Do not create another approval ledger or copy the full rules into each document.

Use these defaults:

- Inspect and resume compatible authorized work. Use one isolated development branch/worktree for substantial work; do not write directly to main.
- Agent-owned planning, implementation, relevant checks, in-scope fixes, and memory updates proceed without repeated confirmation.
- Stage, commit, and push all publishable in-scope work to the verified `origin` development branch at coherent checkpoints and before a planned handoff. This default is enabled.
- Include relevant code, tests, configuration, documentation, and retained evidence. Preserve unrelated or ambiguously owned edits. Do not stage the whole tree without inspecting its contents. Exclude secrets, sensitive raw data, generated caches, and other material that must not be published.
- Follow existing naming, formatting, test, commit-attribution, and branch conventions. Infer routine details from the repository instead of asking the user to specify them again.
- Keep ordinary progress reporting non-blocking. Ask for material decisions at useful boundaries; do not stop merely because a work package, commit, or progress update finished.
- Keep acceptance, PR actions, integration into protected/main branches, deployment, destructive actions, new spending, and changes to the agreement outside routine authority unless explicitly included in the standing agreement or current request.

At kickoff or resumption, establish the outcome, scope, acceptance criteria, branch/remote, applicable standing agreement, relevant verification commands, and material stop conditions. Inspect known hook/CI effects once and recheck affected assumptions when they change. State the resolved agreement briefly; do not turn it into a configuration questionnaire or a second approval gate. Ask only for a missing material choice or actual conflict.

Revise the reusable kickoff/adoption prompts to bundle explicit authorization for the standard action set, including commit-and-push. Submitting such a prompt can establish the agreement without a separate confirmation. Preserve a user's stricter or local-only choice until they change it. A neutral template publishes the default convention; it must not claim that a future owner already approved work in an unknown repository. Repository text records and routes real authority; writing it cannot manufacture human consent or bypass host/tool controls.

Record the agreement's repository and permitted branch scope. It persists across sessions and later authorized workstreams within those boundaries until the human changes/revokes it or a material condition invalidates it. A new workstream still needs its own authorized outcome, but does not need a new commit/push approval when the standing agreement already covers it.

### Publication and recovery contract

Make “work is on origin” a checked checkpoint condition, not a promise of real-time mirroring:

1. Verify the intended repository, `origin` destination, branch, scope, and known publication effects. Never silently change the remote or publish through a different account/destination. Ordinary permitted CI can follow a push; an unapproved deployment, distribution of sensitive material, or new spending requires resolution first.
2. Build meaningful commits that preserve a coherent change or an honest recovery checkpoint. Use the applicable author/committer policy and useful messages. Do not commit after every edit or defer all publication until the end of a long session.
3. Inspect staged content and run the checks required for that checkpoint. Completed increments need their relevant verification. If branch policy permits unfinished checkpoints, publish safe partial work with failed/pending checks clearly recorded; such publication does not mean the work is ready or accepted. Do not bypass required hooks or publication gates.
4. Push normally and verify the remote result. If acknowledgement is uncertain, inspect the remote before retrying. If the remote advanced, reconcile ownership and compatible changes without overwriting another actor's work; stop only for a material conflict or missing authority. Do not force-push or rewrite published shared history.
5. Publish before planned handoff, after a meaningful verified increment, and before ending a session where possible. On interruption, preserve and publish a safe checkpoint when time, tools, and branch rules permit. Do not promise recovery from an abrupt crash before a checkpoint exists.
6. Report local-only work, publication failures, and the last verified remote checkpoint accurately. An offline/authentication failure blocks publication, not necessarily independent local work. Resume from observed state without creating duplicate commits or claiming success from an attempted push.

Avoid a self-referencing commit loop. Evidence and briefings refer to an already inspected implementation candidate or checkpoint. Commit and push the later documentation that records that evidence, then verify its delivery. Do not keep editing a document to insert the hash of the commit that must contain that edit. Distinguish the implementation candidate from a later record-only commit where relevant. If final record delivery fails, disclose the failure instead of emitting a stale success message.

## 3. Establish the actual baseline

Reference observation from 7 November 2026: released `main` was `04765e32d8832a9b80fddd0b3875234386891d14`; the open-PR collection was empty. These are starting references, not a claim about the state when you run.

1. Verify repository identity, actual default branch/HEAD, relevant branches and PRs, worktrees, and staged/unstaged/untracked changes. Preserve concurrent and unrelated work. If remote checks are unavailable, state that limitation and use an identified accessible snapshot only where sufficient.
2. Read applicable instructions, `docs/README.md`, and the upstream maintenance procedure. Recover any active or unresolved work before modifying records. Reuse a branch only if it contains this same authorized work. Otherwise create an isolated branch, for example `dev/feat-autonomous-human-agent-workflow`, from reconciled released main.
3. Inspect maintained guidance and embedded prompts. Start with `AGENTS.md`, root `README.md`, `docs/README.md`, both progress files, `docs/context.md`, the workstream scaffold/conventions, and relevant sections of the adoption and operations guides. Follow other references only when needed.
4. Map each requested behavior to its current canonical home. Identify actual conflicts, duplicates, missing instructions, and reusable rules. Read the existing Project Blueprint contract sufficiently to preserve its separate role; this task does not request blueprint creation or renderer redesign.
5. Record the working agreement, substantial work packages, acceptance criteria, exact baseline, and current authority in the existing document homes. This prompt supplies direct execution and commit/push authority for this task. Keep supporting research and verification notes in its workstream workspace. Do not create a second status or approval system.

Audit all maintained usage guidance for consistency. This is not an instruction to rewrite every file or historical record. Make targeted changes where meaning must change.

## 4. Agent ownership and human interaction

Make the operating model explicit:

- The human supplies the business goal, priorities, constraints, decisions that materially affect the outcome, and business acceptance.
- The agent inspects evidence, maps the workflow, identifies alternatives, recommends a direction, prepares the technical plan, performs authorized work, checks the result, and maintains memory.
- Start from the stated goal. Infer reversible implementation details from evidence. Ask a focused question only when its answer changes a material decision or when authority/evidence is missing. Do not begin with a large questionnaire.
- Before proposing an application, understand the current workflow and desired outcome. Consider whether a process change, existing tool, or smaller intervention could meet the goal. Do not manufacture baseline measurements.
- Present decisions in terms of user effects, tradeoffs, and a recommendation. Keep detailed implementation planning available for inspection without requiring the human to edit it.
- Continue routine authorized steps and repairs without repeated permission requests. Explain when a new decision changes scope, data, security, cost, external contracts, or irreversible effects.
- Treat updates and commit/push checkpoints as information, not requests to continue. Group non-urgent questions into one concise decision brief when they genuinely need human judgment. Raise a blocking or time-sensitive risk promptly.
- Give humans concrete review tasks with expected outcomes. The agent performs checks it can perform itself. Human work should focus on domain judgment, usability, organizational requirements, and checks that need human access or observation.
- Support learning on demand. Explain unfamiliar concepts with a small example, consequence, comparison, or analogy that fits the actual problem. Do not force an analogy into every update or reuse one metaphor for everything.

Preserve the solo human-plus-agent path. Optional collaborators receive bounded tasks, ownership, an identified snapshot, relevant constraints, and expected evidence. Isolate concurrent writes and assign one integrator for the shared progress records. Agent review is reported evidence, not independent human acceptance.

Preserve distinctions between proposal, human authorization, implementation, technical verification, business acceptance, publication, merge, and deployment. A human smoke test cannot replace a required technical or specialist review.

### Plan for long execution between human decisions

The agent writes the detailed plan for its own execution and for a future agent resuming the work. The human should be able to inspect it, but should not need to author technical instructions or approve each internal step.

Plan at two levels within the existing work record:

- Human-facing scope: a small number of meaningful outcomes, business choices, constraints, acceptance criteria, and review boundaries.
- Agent execution: the dependencies, implementation slices, checks, publication checkpoints, reversible assumptions, recovery steps, and next actions needed to deliver those outcomes.

Each substantial work package should be executable through several implementation/check cycles without another human decision. Size it by a coherent outcome and stable requirements, not by a fixed number of files, steps, hours, or tokens. Use small internal increments to keep the result reviewable and recoverable. Do not make every increment a human gate.

Prefer changes that are additive, isolated, reversible, and compatible with current contracts where they can satisfy the goal. This does not prohibit necessary behavior changes. Identify migrations, destructive effects, breaking interfaces, or major unresolved design choices early. Separate the affected boundary, prepare the evidence and recommendation, and continue independent authorized work before asking for the required decision.

Use rolling planning: investigate uncertain dependencies, plan the next executable slice precisely, and refine later implementation details as evidence improves. The agent may reorder internal tasks and revise technical steps within the agreed outcome and constraints. It may not silently weaken acceptance criteria, expand scope, decide an unresolved business policy, or turn an assumption into approval.

When a low-risk reversible choice can be made from evidence, choose it and record only material assumptions. When a choice has substantial business, security, data, compatibility, or cost consequences, present the recommendation and consequences before crossing that boundary. Fewer interactions must come from better preparation and stable scope, not from suppressing uncertainty or treating silence as consent.

Continue through all authorized work packages and in-scope corrections until the agreed outcome is ready for human review or a genuine blocker remains. Checkpoints are resumable boundaries, not automatic stop points. Do not claim that work will continue after the current session ends unless an authorized supported mechanism actually exists.

## 5. Documents as working memory

Retain the current division of responsibilities:

- `AGENTS.md`: concise entry instructions and task-based routing.
- `docs/README.md`: canonical workflow policy.
- `docs/progress-agent.md`: active scope, recorded authority, current plan, evidence, unresolved issues, and next executable action.
- `docs/progress.md`: derived human briefing for the same checkpoint.
- `docs/context.md`: durable project facts, important constraints, interfaces, and decisions that help future work.
- Existing roadmap, debt, runbooks, and archives: their current distinct purposes.

Planning documents are primarily operational material for the agent and subsequent sessions. They must remain inspectable by humans. They record decisions and useful reasons, not private chain-of-thought or conversation transcripts.

Implement these writing and retrieval rules:

1. Keep one maintained home per rule or fact. Link to it from other routes. Avoid competing summaries of permissions or acceptance criteria.
2. Retain rich information selectively: business rules, non-obvious architecture constraints, verified commands, relevant boundaries, decisions and reasons, known failure conditions, evidence references, and open questions. Do not copy source code or generate a directory encyclopedia.
3. Use stable headings, clear terms, short prose, lists, and `Label: value` metadata. Use explicit conditions and actions. Prefer structures that support search and narrow reads. Do not compress away meaning or introduce a proprietary notation without need.
4. Separate verified current behavior, chosen target behavior, inference, and open decisions. Bind important evidence to the inspected revision or complete snapshot and environment. An uncommitted result is not proved by the current HEAD alone.
5. Load mandatory instructions and relevant global constraints first. Retrieve affected details when needed. Reuse unchanged context that is still available. Reconcile stale or conflicting memory against sources before consequential action.
6. Update affected memory with the change it describes. Do not rewrite unaffected records at every turn. Keep historical evidence and current state distinguishable.
7. Keep active plans executable and bounded. Record dependencies, acceptance criteria, completed work, relevant checks, unresolved failures, and the next action. Remove resolved duplication while retaining unique evidence.
8. Before interruption or context handoff, preserve enough state for another session to resume safely: scope, authority, snapshot/dirty work, completed work, outstanding checks, pending operations, and next owner/action. A future session must reconcile actual state before continuing.

Measure the mandatory reading burden before and after for the same representative tasks. Report bytes/words or actual tokens with the counting method. Do not present estimated tokens as measured usage or claim runtime savings from document size alone.

## 6. Control-panel-first application design

Add one canonical, task-triggered application-experience guide if existing homes cannot hold this material clearly. Link a short rule from the core. Avoid adding a large UX manual to every coding task's mandatory context.

For a new human-facing application, establish the interaction shell in the first working slice:

- Clear application/workspace identity and current location.
- Consistent main navigation.
- Obvious access to relevant actions and help.
- Truthful operational status and recoverable error feedback.
- One real workflow connected end to end.

Build subsequent features into that coherent shell. Validate its structure early. Do not spend an initial phase building a decorative dashboard disconnected from working behavior.

Define “always accessible” as predictable access to relevant controls and status. Frequent actions should be directly reachable. Secondary actions may use clearly labelled menus or panels. On small screens and at zoom, controls may move or collapse. Do not require all controls to remain visible simultaneously, prohibit useful scrolling, obscure content with fixed panels, or defeat modal focus behavior.

Keep user inputs and task context stable during navigation where appropriate. Define what happens when navigation would lose unsaved work. Show only capabilities that exist, or clearly identify unavailable/prototype controls.

Operational status must reflect actual system evidence. Distinguish running, completed, failed, unavailable, stale, and cancellation requested/confirmed when relevant. Do not fake percentages, successful cancellation, monitoring, rollback, or undo. Explain unavailable actions and recovery limits in ordinary language. Expose details on demand without filling normal screens with implementation machinery.

Application runtime status, development progress, and permission are separate. A dashboard button does not grant authority. Keyboard and pointer actions must use the same authorization and validation path, including server-side enforcement where relevant.

Apply this convention to new interactive applications and explicitly scoped UI redesigns. For an existing application, assess its current navigation and constraints before proposing migration. Adopting the framework alone must not authorize rewriting the product UI. For an API, library, or command-line tool, specify appropriate commands and observability rather than inventing a frontend.

The optional Project Blueprint remains a separate, explicitly requested project explanation. It is not the application's control panel or an execution controller.

### Keyboard and accessibility contract

Use current W3C WCAG and ARIA Authoring Practices guidance as the reference for web interaction. Native applications should follow equivalent platform conventions.

- `Tab` and `Shift+Tab` move between controls/components. Arrow keys operate within widgets whose established pattern uses them. Keep ordinary page scrolling and text editing intact.
- Native buttons and links retain their expected `Enter`/`Space` behavior. Do not impose the same key behavior on every element.
- `Escape` dismisses the active dismissible layer with appropriate focus restoration. It does not silently reset data or cancel a background job.
- WASD is an optional navigation convenience. Keep it off by default, scoped, discoverable, and disableable or remappable. Do not activate it during text entry, editable content, or input composition. Avoid browser, operating-system, and assistive-technology conflicts.
- Every important action has a visible pointer/touch path and a complete standard keyboard path. Shortcuts supplement these paths.
- Use semantic controls, useful labels, logical focus order, visible unobscured focus, and sensible focus after dynamic changes. Handle modal focus deliberately. Avoid keyboard traps outside the intended modal interaction.
- Do not rely on color alone. Support contrast, responsive reflow, and reduced motion where motion exists. Announce relevant status changes without repeatedly moving focus.

Define future application acceptance checks for the main workflow using keyboard only and pointer separately; text-entry safety; modal entry/exit; unavailable actions; narrow width and zoom; and status/focus behavior. For web reflow, include 320 CSS-pixel width and the equivalent 400% zoom condition, with applicable standard exceptions. State the limits of automated accessibility checks.

This workstream implements guidance. Do not claim runtime accessibility or working application controls from documentation checks. Do not build a demonstration app unless a small disposable fixture is necessary to resolve a concrete design uncertainty.

## 7. One human checkpoint briefing

Make `docs/progress.md` the human-facing checkpoint that the agent also uses for its final development-status message.

Use this sequence:

1. Reconcile actual work, evidence, and authority in `progress-agent.md`.
2. Identify the workstream and state revision represented by the checkpoint.
3. Write one human briefing into `progress.md`.
4. Check it against the detailed record for status, limitations, pending decisions, and next owner.
5. Reuse the saved briefing unchanged as the final checkpoint message. Do not independently compose a second status narrative.

Define equality precisely: the visible briefing text, facts, qualifications, status, and next action must match. Only transport-required link formatting or attachment presentation may differ. There must be no conflicting claims in an added wrapper.

If a material result arrives after saving, refresh both records before issuing the final checkpoint. If saving fails or the environment is read-only, label the message as an unsaved briefing and disclose the mismatch. Never claim synchronization that did not occur.

This rule applies to development checkpoint and handoff messages. It does not require every conversational answer, explanation, research response, or intermediate update to replace the project's current status. Record material new decisions in the appropriate authoritative home. Checkpoints are snapshots, not a promise of continuous background updates.

At an accepted application closeout, the checkpoint can state `No active workstream` while explaining the last outcome and linking the archive and any pending delivery record. Keep that final message and human view aligned. Do not replace an established project's last outcome with the untouched template's first-use invitation.

Make the briefing understandable to a nontechnical business owner:

- Lead with the outcome or current obstacle.
- Explain what the change enables or prevents.
- State what was checked and the meaningful limit of that evidence.
- Make unresolved risks and required decisions visible.
- Give the next useful action and its owner. If the human needs to do nothing, say so.

Use a small adaptable structure such as “Current goal”, “This checkpoint”, “Needs attention”, and “Your next move”. Omit empty sections. Preserve the canonical workflow state and source reference without making the update a metadata dump. Do not impose a word quota or conceal risks to fit a format.

Prefer a concrete explanation such as “A repeated click should reuse the same job, so the user does not accidentally start it twice” when that accurately describes the chosen behavior. Keep the exact technical term accessible when useful. Examples illustrate meaning; they do not establish facts about a real implementation.

### Light gamification

Give development a clear goal, meaningful milestones, visible accomplishments, and an obvious next move. Use encouraging language tied to a verified outcome. A milestone can show what the user can now try or decide.

Keep the tone professional and easy to reduce on request. Do not add arbitrary XP, streaks, leaderboards, pressure to approve, or rewards for code volume, test count, agent activity, or speed. Do not invent completion percentages. If a milestone count is useful, define what is counted and update the denominator when scope changes.

“Implemented”, “checks passed”, “ready for your review”, “accepted”, “merged”, and “deployed” remain different states. A friendly label never changes the underlying gate. Human acceptance is not automatically earned by completing agent tasks.

Create a small varied set of clearly fictional examples for planning/decision, useful implementation progress, failed verification, and human validation. Include at least one case with pending delivery. Use different problem contexts and explanation techniques rather than repeating one metaphor. Keep examples outside neutral live project state.

## 8. Preserve the framework's architecture

Preserve the clean reusable template, safe existing-project adoption, local adaptations, one active detailed work record, proportional work classes, meaningful evidence, and separate delivery/acceptance gates.

Reconcile the current “no mandatory game framing” language deliberately: support the requested light milestone presentation while keeping labels adaptable and allowing a plain professional presentation. Do not let the old wording accidentally cancel the new feature or make theatrical language mandatory.

Update embedded onboarding, adoption, continuation, and handoff prompts only where needed to route the new behavior. An adoption prompt still preserves the target's product documentation, active work, history, instructions, and local constraints. Framework adoption must not initialize imaginary project facts or import maintainer approvals.

Keep the current optional controller protocol and activation requirements intact. Change only necessary routing or terminology. Do not build a controller, installer, agent fleet, new progress database, or automatic chat/file synchronization service.

Follow `docs/ops/maintain-template.md` for the upstream/product boundary. Commit and push the actual development record and supporting evidence with this workstream's changes. Inspect the proposed neutral release tree in a disposable copy and record its checks. Keep the published development branch's active evidence intact at this task's review boundary. Any later neutral-packaging step must preserve a durable reachable evidence checkpoint through the established release procedure; do not erase the only work record or imply that packaging grants acceptance or merge authority.

In that proposed release tree, starters remain neutral: no active workstream, inherited human approval, real project model, maintainer evidence, or enabled execution/review controller. The reusable commit/push convention is enabled by default, while project-specific agreement/targets remain unestablished until actual kickoff/adoption. The new human starter should invite the first goal in simple language and match its neutral detailed source. Document the packaging exception to checkpoint-message equality: a neutral application starter is not the final maintainer-session briefing. The maintainer briefing belongs to the preserved development checkpoint.

## 9. Work sequence and verification

Use a small number of coherent work packages. Complete their internal increments, relevant checks, and publication checkpoints, then continue without routine human approval waits. Suggested order:

1. Baseline and change map.
2. Standing agreement, recurring action defaults, agent planning, and working-memory contracts.
3. Application control/navigation guidance.
4. Human briefing, synchronization contract, and examples.
5. Cross-document reconciliation, verification, and published development review candidate.

Use existing tools first. A small temporary checker is appropriate for an objective property such as links or briefing equality. Do not add a permanent validation framework merely to check prose. Delegate bounded independent research or review only when it adds clear value. Reconcile findings against the exact changed revision; multiple agents are not independent proof of correctness.

Verify these outcomes:

- Each requested behavior has one canonical home and appropriate entry routing.
- Instructions remain consistent across new-project use, existing adoption/update, ordinary continuation, handoff, and upstream maintenance.
- The human/agent responsibility split is clear. No rewritten rule silently expands authority or hides a material gate.
- Commit/push is enabled by default within an established agreement. Current task permission is explicit. Kickoff/adoption establishes real authority once; resumption does not ask again unless the target, scope, authority, or material conditions changed.
- The agent can complete a substantial work package through multiple reversible internal steps without routine human intervention. Questions occur at material decision boundaries, and technical replanning preserves the agreed criteria.
- Publication includes all publishable in-scope changes and evidence, preserves other actors' work, and reports remote confirmation accurately. Source publication does not imply human acceptance or deployment.
- The briefing and final checkpoint use the same content, with a defined recovery path for failed saves, new results, and stale summaries.
- Examples preserve truthful statuses and make the result, uncertainty, and next action clear.
- Dashboard guidance covers first-slice behavior, navigation, real status, responsive access, keyboard/pointer use, and headless/existing-product boundaries.
- All changed links and anchors resolve. The complete diff preserves unrelated work and historical evidence.
- The proposed release tree is neutral and usable; actual maintainer evidence remains intact.

Run focused scenario walkthroughs: a new business app, an existing app with local instructions/dirty work, a small correction, an interrupted workstream, a failed check, pending human acceptance/deployment, and an API-only project. Combine cases when useful. Include default commit/push, an explicit local-only override, unrelated staged changes, a failed or uncertain push, an unexpected deployment trigger, a material decision within a longer package, an unsupported permission request, and a stale progress summary. Use disposable local Git fixtures for edge cases only when useful; do not deliberately trigger remote failures, expose data, or alter protected branches to test the rules.

Where tools allow, use a clean receiving context to recover the correct next action and constraints from the candidate documents, and compare it with the baseline using the same scenario. If this cannot be executed, label it a static walkthrough. Do not present a simulated reader as a human usability test.

Review the required reading path before and after. Report regressions as well as improvements. A shorter file is not enough if it loses a constraint; a richer file is not enough if it adds irrelevant reading.

Fix concrete in-scope findings and rerun affected checks. Stop when the agreed criteria and required checks are satisfied. If repeated attempts produce no new evidence or progress, record the blocker and needed decision rather than continuing an open-ended improvement loop.

## 10. Research basis and evaluation limits

Use the following checked primary sources as a starting set. Read the relevant methods and limits before relying on a claim. Research additional sources only for a concrete unresolved design question. Do not turn this implementation into an unlimited literature review.

- Gloaguen et al., *Evaluating AGENTS.md*, v3, 29 September 2026: https://arxiv.org/html/2602.11988v3 . Controlled coding-agent comparisons on 300 SWE-bench Lite and 138 CTXbench tasks found no statistically significant overall task-success improvement, with increased inference costs. Python tasks and test-defined success limit generalization. This does not evaluate the proposed longitudinal working-memory workflow.
- Lulla et al., *On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents*, v2, 30 March 2026: https://arxiv.org/html/2601.20404v2 . Paired runs on 124 small PR tasks reported 28.64% lower median runtime. Full semantic correctness was outside scope. Read this alongside the preceding result, not as proof that instructions always improve quality or cost.
- Shanto et al., *Toward an Evidence-Based Template for Agent Instruction Files*, v1, 2 November 2026: https://arxiv.org/html/2611.02383v1 . This recent preprint reports divergent guidance in 16.1% of 386 reviewed section pairs and incomplete intent preservation in generated instructions. It did not test downstream coding outcomes. Check rewritten conditions and exceptions, not just structural coverage.
- Anthropic, *Harness design for long-running application development*, 24 March 2026: https://www.anthropic.com/research/harness-design-long-running-apps . Vendor engineering experience supports exploring concrete criteria and structured handoffs. Its selected demonstrations do not establish independent evidence of business-user productivity or justify mandatory multi-agent machinery.
- Straubinger et al., *Gamifying Testing in IntelliJ: A Replicability Study*, 2025: https://arxiv.org/html/2504.19294v1 . A 150-minute controlled task with 174 analyzed master's students increased test-writing activity but found no significant coverage or mutation-score improvement. Its measured test-smell ratio was higher, largely involving console output. This is not evidence about business employees using coding agents or long-term motivation.
- W3C, reflow: https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
- W3C, keyboard interaction: https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/
- W3C, character shortcuts: https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html
- W3C, modal dialogs: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- W3C, status messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html

Keep a compact supporting evidence note with source/version/date, study population/context, method/tool context, findings, limitations, and relevance to each consequential design choice. Distinguish empirical findings, standards, vendor practice, and our design inferences. Unknown study dates remain unknown.

Record a lightweight proposed evaluation for later authorized use: human understanding of status and next action, decision/review effort, restart accuracy, rework, task success, maintained quality, documentation/context cost, and enjoyment measured separately. Record framework/tool versions and relevant experience. Measure end-to-end workflow effort, including training, review, coordination, and maintenance. Do not claim that this documentation change proves a paradigm shift or that its components have isolated causal effects.

Workplace recruitment, employee monitoring, private-data collection, production experiments, and publication of internal findings require separate authorization. This session prepares guidance and static evidence; it does not conduct that pilot.

## 11. Final handoff

Update the detailed record, derive the human briefing from observed results, and verify their agreement. Commit and push the final in-scope records under the publication contract, verify remote delivery, and use the saved briefing as your final response. Lead with the achieved result or actual blocker. State what changed, the meaningful verification result, remaining uncertainty, and the next human action. Put the complete file/change map, source references, check evidence, and resumption details in the linked workstream record.

Identify the actual branch/base and inspected implementation candidate, and report that candidate's verified publication without chasing a document's future containing hash. A later record-only commit can deliver the final briefing; verify its delivery without calling the earlier candidate the latest branch head. Retain and publish appropriate evidence. If anything remains only local or intentionally excluded, state the material reason. Report publication and deployment truthfully. Do not mark the work accepted, completed, released, or archived without the required human evidence.

Begin with baseline inspection and carry this authorized work through to the defined review boundary.
