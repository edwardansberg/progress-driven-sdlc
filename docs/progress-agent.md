# Active workstream: project-blueprint-v0.1

State revision: r2-BP2
Status: Ready for user validation
Current gate: Project Blueprint BP2 — ready for human review
Next action: Codex implements/verifies BP2 for human review of existing PR #7.
Loop control: Off
Repository: edwardansberg/progress-driven-sdlc
Branch: dev/project-blueprint-v0.1
Implementation base: e7f1f09688f8afe451185f96d28adce42498215e
Correction base / inspected HEAD: db430242b6978fe46ee6681186ab880e196401a4
Observation: 2026-10-07, Codex Git/gh. Local and remote branch match; main remains the implementation base; PR #7 OPEN/unmerged. Index/tracked tree clean; unrelated ste_communication_amendment.patch remains excluded.

## Authority and history

Human BP2 request authorizes bounded correction and validation. The explicit preceding “please commit and push for pr” grant continues for this same work/branch and existing PR, as permitted by the BP2 authority clause; update PR #7 only. Merge, settings, downstream adoption, deployment, research and experiments remain unapproved. Human acceptance pending; no loop grant.

[BP1 checkpoint](https://github.com/edwardansberg/progress-driven-sdlc/blob/22bec5888a2d49092946a62a9ef5007d805892f4/docs/progress-agent.md) preserves original plan, decisions and artifact-scoped checks. BP1 was published at the correction base; publication is not acceptance. Unaffected evidence retains its original scope.

## Investigated plan and criteria

1. In the existing renderer, show required component summaries and relationship labels in Overview, without truncation or status inference. Remove normal header/footer/known-revision notice boilerplate; preserve Info and visible error/Unknown/empty notices. Wrap all heading levels without truncation.
2. In the contract, clarify concept identity and meaningful-qualification visibility. No schema, revision, refresh, routing or other policy changes.
3. Extend external disposable fixtures with a proposed/not-implemented component, long component/flow/roadmap names, Unknown and corrupt data. Verify all five views at 320px, summary text/labels, actionable notices/Info, keyboard/focus, hostile text and schema/reference rejection. Compare validator/data and revision sections to BP1 byte-for-byte; check cumulative PR scope, links/whitespace and unrelated patch.
4. Preserve corrected maintainer evidence in a checkpoint, then restore neutral progress in a forward packaging commit. Recheck named publication boundaries and update only existing PR #7.

## Risks and validation

No screen-reader, WCAG, real-project correctness, comprehension or adoption claim. Static checks and browser smoke tests cover only tested fixtures. Rollback reverses BP2 hunks after inspecting intervening work, preserving BP1 and unrelated files. Human reviews corrected Overview, warnings, narrow layout and identity wording. Affected verification passed as recorded below; human acceptance pending.

## Corrections and verification — 2026-10-07

Production changes only: docs/ops/project-blueprint-template.html and docs/ops/project-blueprint.md. Overview now displays the existing required summary in each card, retains relationship labels and does not infer implementation from roadmap status. Header subtitle/footer removed; known-revision populated model hides the empty notice. Info governance stays; Unknown, invalid and empty notices stay visible. All heading levels wrap without truncation. IDs persist only for the same concept; new/replaced concepts receive new IDs, not recycled IDs to shrink diffs.

Check: Review cases 1–12 (meaning, notices, layout, interaction and validation).
Basis: Disposable validate.cjs in the local BP2 review directory; Node v24.20.0 and isolated Chrome file://, Codex performed; new fictional fixture includes proposed/not-implemented summary and labeled relation plus unbroken component/flow/roadmap names. Screenshot inspected at 320px.
Scope: BP2 renderer.
Result: Passed exact visible Overview summary/qualification and relationship label; no header paragraph/footer or successful notice for populated known revision; Info still contains revision/governance/freshness; neutral, Unknown, malformed JSON, invalid references and unsupported schema show appropriate notices. All five views fit 320px without document overflow. Native Tab/Enter, focus outline and component navigation passed. Hostile HTML/script-like text remains literal with no injected image; type/required/extra-field/duplicate/reference/version rejection passed. Zero observed runtime exceptions. 200% CSS zoom sanity passed.
Limitations: Browser smoke checks are not complete keyboard/screen-reader or accessibility certification. CSS zoom is not browser-UI zoom. No observed human comprehension, real-project correctness or downstream adoption.

Check: Cases 13–18 (safety, neutrality, semantic preservation, scope).
Basis: Static prohibited API/resource/sink scan; byte comparison against BP1; complete correction and cumulative PR diff review; git diff --check and git diff --cached --check; local link/fragment check at packaging.
Scope: BP2 plus unchanged BP1 production integration.
Result: Passed no external assets/network/storage/unsafe HTML introduced; validator and neutral data block byte-identical; revision/refresh/security/validation contract sections byte-identical; only two production files changed since BP1. Original cumulative PR remains six production files. No generated docs/project-blueprint.html. Non-scope files and pre-existing patch preserved (SHA256 129052a427a080991d213407b1cbd07a963cd411e7174db1480bed3b4d80fe65). Progress views change only to preserve checkpoint evidence, then return to neutral base bytes. No other production correction needed.
Limitations: No fresh live refresh/no-churn evaluation: unaffected BP1 procedure evidence retains original scope. Static checks are not general security or WCAG proof.

Publication preflight: main and PR head match inspected references; no custom local hooks, remote hooks, Actions workflows or Pages observed. No configured CI pass claimed. Preserve evidence with an attributed commit, then neutral progress in a forward packaging commit. Only update PR #7; never merge. Human acceptance remains pending, Loop Off.

Human review: confirm qualifications remain understandable, the normal screen is clean, narrow headings readable, and concept-ID wording correct. Undo only BP2 hunks after checking intervening edits; preserve BP1 checkpoint/history and unrelated work.
