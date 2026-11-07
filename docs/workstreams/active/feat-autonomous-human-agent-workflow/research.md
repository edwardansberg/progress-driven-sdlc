# Research basis and proposed evaluation

Checked: 2026-11-07 against the five linked primary sources; all were accessible. Methods, findings and limitations were inspected, not independently replicated. Publication/version dates below are not experiment dates; unspecified collection or run dates remain unknown.
Scope: Supporting evidence for [active detail](../../../progress-agent.md), not policy, authorization or a second status record. Accessibility standards are assessed separately.

## Repository context and task success

Source: Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v3), v3, 2026-09-29; empirical preprint, sections 3–5 and statistical tables.

Context/method: 300 SWE-bench Lite tasks from 11 Python repositories and 138 CTXbench tasks from 12 repositories. Compared absent, generated and, for CTXbench, developer-committed context. One completion per agent/setting: Claude Code/Sonnet 4.5, Codex/GPT-5.2 and GPT-5.1 mini, Qwen Code/Qwen3-30B. CTXbench used generated task descriptions/tests with manual review. Success meant passing the benchmark tests; inference cost and tool steps were additional measures.

Findings: Context versus absence did not significantly improve overall resolution: p=0.87/0.37 for generated files and p=0.21 for developer files. Developer files outperformed generated files on CTXbench (p=0.038). Generated-file inference costs rose about 20%/23%; developer files also increased costs.

Limits: Python, selected tasks/models and test-defined success; no longitudinal project-memory, human comprehension or broad security/quality evaluation. Unknown experiment dates. Non-significance does not establish equivalence.

Design inference: Retain necessary constraints and verified commands, route selective reads, avoid duplicating discoverable content, and measure context cost alongside success. The study does not establish an optimal document length or prove this workflow improves outcomes.

## Repository context and execution effort

Source: Lulla et al., [On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](https://arxiv.org/html/2601.20404v2), v2, 2026-03-30; empirical preprint, sections 3–5.

Context/method: 124 merged code PR tasks across 10 sampled repositories with qualifying root-only AGENTS.md files; at most 100 changed lines and five files per task. Paired same-snapshot runs with/without the file used Codex/gpt-5.2-codex in Docker and generated issue descriptions based on PR diffs. Measured wall-clock time and token categories.

Findings: Median runtime fell from 98.57 to 70.34 seconds (28.64%); median output tokens fell 16.58%. Runtime/output differences were significant. The paper's median total tokens increased 1.29%; reductions were not uniform across token metrics.

Limits: Small selected changes, one model/configuration, stochasticity and unknown run dates. A 50-task manual sanity check established nontrivial outputs, not full semantic correctness, maintainability or equivalence to merged PRs. Timing excludes a measured end-to-end human workflow.

Design inference: Evaluate task-specific guidance with both time and quality measures. Read alongside Gloaguen; differing tasks, configurations and outcome definitions prevent treating either result as a universal instruction-file effect.

## Instruction consistency and preservation

Source: Shanto et al., [Toward an Evidence-Based Template for Agent Instruction Files](https://arxiv.org/html/2611.02383v1), v1, 2026-11-02; empirical preprint, sections 3–7 and 9.

Context/method: 3,387 files from 1,000 GitHub repositories sampled across two popularity cohorts; four instruction formats. Manual category coding and 386 corresponding section-pair assessments. AGIT-Instruct compared GPT-4o-mini zero-shot/RAG and CodeLlama-13B base/QLoRA on 62 category-selected evaluation files, using structural coverage, text similarity and manual intent assessment.

Findings: 62/386 pairs (16.1%) diverged; none were classified contradictory. Only 48.2% shared scope, so differences may reflect legitimate component needs. Of 278 manually assessed RAG category instances, 19.4% fully and 61.2% partially preserved intent; 19.4% were missing. Category presence did not establish complete operational guidance.

Limits: Selected public repositories, subjective coding, potentially dependent section pairs and category-balanced generation evaluation. Generic-intent conversion can remove commands/constraints. No downstream coding outcomes; complete corpus collection dates unknown. Descriptive template categories are not universally required.

Design inference: Maintain one home per rule, preserve scoped exceptions, and check rewritten conditions/permissions against source meaning. Heading coverage and semantic similarity alone cannot verify the new briefing, standing agreement or resumption contract.

## Long-running development practice

Source: Anthropic/Prithvi Rajasekaran, [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps), published 2026-03-24; vendor engineering account, not an independent controlled user study.

Context/method: Selected frontend/full-stack demonstrations using Claude Agent SDK, Playwright MCP, tuned grading criteria and planner/generator/evaluator roles. Models changed from Sonnet 4.5 experience to Opus 4.5/4.6; exact run dates and a comprehensive task sample are unspecified.

Findings: Reports benefits from concrete criteria, file handoffs and evaluation feedback, with substantial overhead: one Opus 4.5 game-maker comparison cost $200 over six hours versus $9 over 20 minutes solo. Opus 4.5 allowed removing context resets; Opus 4.6 allowed removing sprint structure and reducing evaluation frequency. Demonstrations still had limitations.

Limits: Selected examples, author preferences and evolving prompts/models prevent isolated component-effect or business-productivity claims. Token costs omit a complete accounting of human setup/maintenance effort.

Design inference: Use executable criteria, recoverable state and rolling plans; keep orchestration optional and proportionate. This supports investigating substantial packages, not mandatory agents, resets, long sessions or expanded product scope.

## Gamification and quality

Source: Straubinger et al., [Gamifying Testing in IntelliJ: A Replicability Study](https://arxiv.org/html/2504.19294v1), v1, 2025-04-27; empirical controlled study, sections 3–4.

Context/method: Main experiment in 2024; exact dates unspecified. Random group assignment; 174 analyzed master's students from 232 participants. A 150-minute task implemented 11 TypeScript date functions. IntelliJ/IntelliGame achievement treatment versus recording-only control; Jest, Stryker, Smelly Test, activity logs and exit survey.

Findings: More tests and executions, but no significant line/branch coverage or mutation-score improvement. Measured smell ratio was higher (0.13 versus 0.03; p=0.013); 101/108 smells were console output, often alongside assertions. Final golden-test failures favored treatment (p=0.054), which is not statistically significant at 0.05.

Limits: Student convenience sample, missing reports/setup exclusions, short task and date-sensitive tests; no business-user coding-agent or long-term motivation evaluation. Test-smell counts are imperfect quality proxies. Favorable abstract/conclusion language exceeds some endpoint evidence.

Design inference: Use truthful accomplishments and next moves, with optional plain presentation; avoid rewarding activity volume or pressuring approval. Measure enjoyment, task correctness and maintained quality separately; this experiment does not validate the proposed briefing.

## Decisions not established by research

Inference requiring validation: Selective memory, two-level plans, substantial packages, the control-panel convention and one saved human briefing are design choices, not demonstrated productivity gains. Briefing equality is an inspectable consistency property; it does not establish understanding. Commit/push defaults, human acceptance and controller limits come from actual authorization and policy, not these studies. No paradigm-shift or isolated causal-effect claim is supported.

## Proposed later evaluation

Status: Proposal only; no recruitment, employee monitoring, private-data collection, production experiment or internal-findings publication is authorized by this note. A later human grant must bound participants, data, environment, retention and reporting.

Design: Compare the current and revised workflow on comparable agreed tasks with fixed acceptance criteria. Where feasible, counterbalance order and account for learning, task difficulty and participant experience. Include interrupted work/resumption and failed-check/pending-delivery cases. Record framework commit, agent/model/tool versions, settings, task snapshot, domain/software/AI experience and deviations. Establish an observed baseline; do not invent one.

Measures, kept separate:

- Understanding: Ask the human to identify goal, actual status, uncertainty, next action and owner; score against the recorded state and retain confidence separately from accuracy.
- Review/decision effort: Active human minutes, clarification rounds and material decisions, distinguishing useful decisions from avoidable interruptions.
- Restart accuracy: Fresh-context recovery of scope, authority, evidence, pending gates and next action; record omissions, unsafe assumptions, retrieval effort and recovery time.
- Rework/task success/quality: Correction effort and reopened defects; independently assessed task criteria; relevant regression, maintainability, security and accessibility evidence over an agreed follow-up period.
- Documentation/context cost: Authoring and maintenance time, reading volume, tokens, inference spend and stale/conflicting guidance.
- Enjoyment: Separate voluntary rating and comments about clarity, satisfaction, pressure and willingness to continue; do not infer enjoyment from activity.

Accounting: Report elapsed time and active human/agent effort separately, including training, setup, planning, review, coordination, waiting, corrections and maintenance. Report failures, missing observations, variation and uncertainty. A small feasibility comparison is not proof of business benefit; a bundled workflow comparison cannot isolate each component's causal contribution. Static walkthroughs and agent recovery checks remain distinct from human usability evidence.
