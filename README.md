# Progress-Driven SDLC

A reusable framework for a human working with ChatGPT Web and laptop Codex through short, natural, decision-ready conversation. Treat each project as a real problem-solving challenge: choose the outcome, see verified progress, and stay in control. Detailed specifications, decisions, alternatives, and verification remain in repository documents.

Human relay is a normal supported workflow. No controller or automation is required, and the framework also works with one assistant or other providers. The [canonical workflow](docs/README.md) defines the rules; documentation guides behavior rather than mechanically enforcing it.

## Use the Workflow

1. Understand the challenge: State the outcome you want. Conceptual discussion stays lightweight; substantial work begins with the repository's [required context review](docs/README.md#start-here).
2. Choose and plan: Explore meaningful alternatives, then have the coding agent investigate the actual checkout and record an actionable plan.
3. Authorize: Approve an identified scope under [Approval Scope](docs/README.md#approval-scope). Standard/high-risk work normally stops for that decision; clearly requested quick changes and recorded scoped direct execution follow their existing paths.
4. Implement and verify: Codex carries out authorized work and [records checks](docs/README.md#verification-and-user-validation), continuing routine steps without repeated approval questions.
5. Review and accept: Web can review the exact supplied candidate; you validate the result and decide acceptance. Passing checks or a clean review does not authorize delivery. Accepted work reaches [Completed or Released](docs/README.md#workstream-statuses-and-gates) only when its agreed conditions are satisfied.

The [interaction contract](docs/README.md#interaction-contract) keeps ordinary briefings short while preserving visible risks and access to detail. Ask for an explanation, evidence, options, a handoff, or plain presentation in natural language.

## Collaborate Across Sessions and Tools

- You own priorities, material choices, permissions, and user validation.
- ChatGPT Web primarily helps explore, specify, plan, and review identified evidence.
- Laptop Codex primarily investigates the actual checkout, implements authorized changes, verifies them, and maintains repository memory.

Both agents can contribute ideas; neither approves on your behalf. You can forward a prepared instruction to Codex and its complete result back to Web. The sending agent prepares one accessible packet using the [handoff contract](docs/README.md#handoff-and-resumption), so you need only transfer it.

No participant assumes shared history or filesystem access. A GitHub commit cannot verify a different uncommitted laptop patch. A local path helps you open a file but does not give Web access; transfer the complete prepared material, including relevant untracked files. No commit or push is required solely for review. Web drafts remain drafts until incorporated under actual authority.

### Fictional exchange

Illustrative only: this is not this repository's behavior, evidence, or approval.

Human: “What should a retry do?”

```text
Example project · Prevent duplicate submissions · Planning

We need to decide whether retrying the same request should create another task. I recommend returning the original task, because that avoids accidental duplicates.

A — Return the original: callers reuse a request identifier; accidental retries stay safe.

B — Create another task: intentional repeats are easy, but accidental duplicates remain possible.

Choose the behavior to investigate. That choice permits planning, not implementation. The detailed tradeoffs will be recorded in the active workstream after investigation.
```

### Portable Web bootstrap

Use this with the intended application's repository and snapshot, not this upstream maintenance workstream. Supply accessible evidence and the actual current task; do not invent authority or ask the human to reconstruct a handoff. This short bootstrap points to policy instead of duplicating it:

```text
Repository: <intended application repository>
Snapshot: <exact published commit, or supplied complete bundle with full base>
Current task: <objective and relevant workstream, if one exists>
Authority: <actual human-approved scope/reference, or planning/read-only only>
Read that repository's docs/README.md, including Interaction contract. Follow
its applicable reading requirements for this task, including agent/directory
guidance and active progress/context/roadmap/debt for substantial work.
Use the identified snapshot and that repository's decisions, not upstream
framework-maintenance state or another project's approvals.
State missing access; request only necessary missing material.
Keep the human briefing short and the complete evidence/relay material separate.
If you cannot write the repository, label proposed decisions/reviews as drafts.
This bootstrap grants no implementation, delivery, or loop activation permission.
```

A repository edit or bootstrap does not configure every existing Web conversation or refresh a running agent. See [Activating updated guidance](#activating-updated-guidance); reading a link's text is not reading its target.

## Operating Model

- Policy: [docs/README.md](docs/README.md) owns workflow and interaction rules; [AGENTS.md](AGENTS.md) is concise agent guidance.
- Live state: [progress](docs/progress.md) holds one active workstream per repository. [Context](docs/context.md), [roadmap](docs/roadmap.md), and [technical debt](docs/techdebt.md) keep verified facts, confirmed direction, and accepted postponed recommendations separate.
- Scaffold and history: [WORKSTREAM_TEMPLATE.md](docs/workstreams/WORKSTREAM_TEMPLATE.md) is the sole repeated scaffold. Terminal workstreams retain their outcomes in [the archive](docs/workstreams/README.md); [docs/old/](docs/old/README.md) is historical reference only.
- Procedures: [Operations](docs/ops/README.md) and [security](docs/security/README.md) hold reusable local procedures and boundaries.

Handoffs reuse workstream metadata and the delivery summary. There are no separate role reports, game-state registers, or cross-project approval stores.

## Adopt or Update the Framework

This upstream framework repository and each adopting application have separate repositories, branches, evidence, active state, and permissions. Upstream `docs/progress.md` may contain real framework-maintenance work awaiting review. It is not the adopting application's project state and must not be reset upstream for packaging convenience.

Before copying or merging anything, inspect the target repository, its applicable instructions and local constraints, and its staged, unstaged, and untracked work. Establish the authorized adoption scope and preserve existing files. Framework-policy adoption does not authorize application development, release actions, or resetting live state.

### New project

1. Select the relevant starter policy, scaffold, and directory guidance for the target; do not copy upstream Git metadata or framework-maintenance state into the application.
2. Tailor policy deliberately to the project's needs. Keep entry-point instructions concise, with commands and release/recovery procedures in appropriate runbooks.
3. Initialize application `docs/context.md` from that application's verified evidence, `docs/roadmap.md` from confirmed user direction, and `docs/techdebt.md` only from accepted postponed recommendations. Leave unknowns explicit and remove setup comments when used.
4. Initialize application `docs/progress.md` as `No active workstream` only if no substantial effort is active. Otherwise record the actual requested effort and its authorization using the sole scaffold.
5. Follow [workstream initialization](docs/workstreams/README.md#starting-a-workstream): standard/high-risk work normally stops for plan approval, while recorded explicit scoped direct execution can proceed after investigation and a written plan.

### Existing project or framework upgrade

1. Compare existing `AGENTS.md`, workflow policy, active workstream, context, roadmap, debt, runbooks, and archives with the proposed framework changes.
2. Merge policy and entry points deliberately. Preserve project-specific constraints and procedures; resolve genuine conflicts under the target's authority rather than replacing instructions wholesale.
3. Preserve the active workstream's evidence, approved scope, and pending gates. An incompatible substantial adoption effort requires explicit disposition of that work before replacement. Never blindly copy the scaffold over it.
4. Retain verified application memory and historical archives. Add missing structure only where needed; do not replace live documents with upstream placeholders or import upstream approvals.
5. Verify the merged links, setup comments, instructions, and relevant contract scenarios. Updating policy alone grants no authority to implement application roadmap or debt items.

### Activating updated guidance

Editing `AGENTS.md`, overrides, or referenced policy on disk does not establish that a running session refreshed its loaded instructions. Use the tool's documented reload/new-session behavior when relevant; preserve the handoff first and do not automatically interrupt active work. Tool-specific discovery details are in the [source note](docs/README.md#source-note).

Reading amended files is distinct from demonstrating automatic instruction loading or compliant behavior. A self-reported summary is limited evidence, not enforcement. A future proportionate read-only setup check can identify accessible instruction sources and explain plan/delivery boundaries from the intended repository and directory. Keep that check user-owned when the agent cannot observe the environment, and record it as unperformed until evidence is available. Do not assume a Markdown link loads its target: retain explicit canonical-policy reading for substantial work.

## Optional Execution and Review Loop

For advanced use, the [opt-in contract](docs/README.md#optional-execution-and-review-loop) lets a human bound repeated implementation, verification, specifically authorized review-branch publication, and Web review before final human validation. Installation, adoption, and implementation approval leave it Off. Activation needs a complete human grant, distinct controls, known publication effects, and a permitted transport; review publication grants neither acceptance nor release.

The [operational reference](docs/ops/autonomous-review-loop.md) specifies messages, recovery, controls, and pilot prerequisites. This starter supplies documentation, not a working controller or tested stop mechanism. Normal manual collaboration above needs neither. Automated transport permission remains unresolved in the recorded source observations; an API reviewer is a separate human choice.
