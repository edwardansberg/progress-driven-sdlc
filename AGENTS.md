# Progress-Driven SDLC Working Agreement

These instructions apply to the entire repository. Tailor project-specific commands and release details before adopting the template.

## Required Context

Before substantial development work:

1. Read `docs/README.md`.
2. Read `docs/progress.md` in full.
3. Read `docs/context.md` for the durable product and runtime model.
4. Read `docs/roadmap.md` for product direction.
5. Read `docs/techdebt.md` for accepted deferred work that may intersect the task.
6. Read the relevant code and runbooks.
7. Verify documentation claims against code, configuration, migrations, tests, Git history, and runtime evidence.

Never treat `docs/old/` as current guidance.

## Planning and Approval

- Use the work classes and gates defined in `docs/README.md`.
- For a standard or high-risk workstream, investigate first and write a comprehensive plan to `docs/progress.md` before substantive implementation.
- Stop at `Awaiting plan approval` until the user explicitly approves or explicitly requests the direct-execution fast path.
- Renew approval when scope or a material decision changes user-visible behavior, data handling, security, infrastructure, external contracts, cost, or destructive effects.
- Quick, isolated, reversible, low-risk changes may be implemented directly when clearly requested.

The user's explicit instructions take precedence over this default workflow.

## Keep Project Memory Current

The coding agent owns the accuracy of the active workstream while working:

- Refresh status, current gate, next action, plan, decisions, and evidence at material milestones.
- Record deviations and failed or skipped checks honestly.
- Check boxes only after the work is actually complete.
- Keep user-owned smoke checks pending until the user confirms them.
- Update durable architecture, operations, security, and interface docs whenever implementation changes their subject.
- Propose roadmap changes, but do not treat roadmap entries as implementation authorization.
- Record accepted-but-postponed engineering recommendations in `docs/techdebt.md`, but do not treat debt entries as implementation authorization.
- When technical debt is selected, revalidate it and promote it into `docs/progress.md` before implementation.
- Keep workflow policy canonical in `docs/README.md`; keep `progress.md`, `context.md`, `roadmap.md`, and `techdebt.md` focused on current project state rather than copying lifecycle instructions into them.

Do not turn documentation into a tool-call transcript. Preserve decisions, evidence, outcomes, and actionable next steps.

## Delivery Gates

Implementation approval does not automatically authorize committing, pushing, opening or merging a pull request, deploying, migrating live data, destructive cleanup, or production promotion.

- Record automated verification before handing work to the user.
- Provide a tailored smoke-test checklist and rollback considerations.
- Await explicit authorization for each requested release action.
- Mark work `Released` only after the target commit and environment are verified.
- Archive closed workstreams according to `docs/workstreams/README.md`.

## Commit Attribution

- Every commit created by Codex should record `Codex <codex@local.invalid>` as its author unless the repository defines another agent attribution policy.
- For a normal commit, use `git commit --author="Codex <codex@local.invalid>" ...`.
- Preserve the configured human or automation identity as the committer and the authenticated hosting identity as the pusher.
- Do not change repository or global Git identity, signing, or push credentials to achieve agent attribution.
- Before pushing an agent-created commit, verify author and committer metadata with `git show -s --format=fuller HEAD`.
- Do not rewrite attribution on commits created by the user or another actor unless that actor explicitly requests it.

## Internal Review and Delegation

Use specialist review or testing agents when they materially improve quality. The primary coding agent remains accountable for reconciling their conclusions. Do not create permanent Planner, Engineer, QA, or Reviewer handoff files unless the user specifically requests them.

## Safety and Documentation Hygiene

- Never write secrets, tokens, private keys, credential values, sensitive payloads, or raw production logs into maintained docs.
- Prefer reusable placeholders over personal machine paths, IP addresses, hostnames, or key names.
- Store each reusable procedure once and link to it elsewhere.
- Keep `docs/workstreams/WORKSTREAM_TEMPLATE.md` as the sole repeatedly instantiated workflow scaffold unless observed project needs justify another template.
- Preserve unrelated user changes and historical archives.
- Do not create Markdown tables. Prefer headings, short prose, numbered steps, bullets, and compact `Label: value` lines.
- When materially editing a section that already contains a Markdown table, convert that table to readable prose or lists as part of the edit. Do not perform unrelated bulk conversions unless they are in scope.
