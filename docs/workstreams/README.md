# Workstream Scaffold and Archive

[Core policy](../README.md) owns authority and lifecycle. This procedure is for starting, migrating or closing substantial work. Routine continuation does not reload it. One active authority stays in `docs/progress-agent.md`; `docs/progress.md` is its human summary. Supporting files are not another approval/status register. Solo work needs no extra reviewer unless risk or project rules require one.

## Starting a Workstream

1. Inspect current authority, repository, branch/HEAD, worktrees and dirty work. Resume compatible work; ask for disposition before displacing unrelated unresolved work. A quick typo needs no workspace or full scaffold.
2. Choose a stable key such as `feat-add-friends-button`, `fix-landing-page-latency` or `chore-remove-stale-documentation`. Use lower-case portable letters/numbers and hyphens, with a type prefix. The topic branch contains the same key, optionally under `dev/` or `codex/`.
3. Create/resume only the branch for this authorized work. The initial instruction can authorize safe local creation/switching; do not ask again when covered. Inspect dirty work and concurrent ownership before switching. Never overwrite a branch/directory or combine unrelated work. Resolve collisions explicitly with a stable distinct key. Branch setup grants no push, merge or deployment rights. Non-Git projects need no invented branch or Git initialization.
4. Use the sole [scaffold](WORKSTREAM_TEMPLATE.md) in progress-agent.md when safe. Keep only goal/scope, authority, current state/next action, bounded plan, criteria, relevant checks and unresolved risks. Add specialist, migration, recovery or delivery detail only when needed. Standard/high-risk work normally awaits plan approval; recorded direct execution permits proceeding after investigation and a written plan.
5. Reference `docs/workstreams/active/<key>/` when supporting files are needed. Do not populate empty templates/subdirectories. Git need not track an empty workspace. Update detail first, then the summary at meaningful checkpoints.

### Migrating an existing active record

Prepare an approved migration map before changing authority, identity or paths. Preserve scope, approvals, evidence, unique summary content and pending gates. A legacy authoritative progress.md transfers intact to progress-agent.md before progress.md becomes a derived summary. Resolve occupied/uncertain destinations before writes. Existing work need not be renamed or moved merely because this convention changed; map it deliberately. Migration is neither acceptance nor closure. Old flat archives stay valid without bulk conversion.

## Supporting material

Classify by continuing purpose, not file extension:

- Code, tests, configuration and executable product dependencies stay in normal project locations.
- Scripts/runbooks needed after development stay maintained in stable homes such as scripts/ or docs/ops/.
- Workstream investigations, alternatives, sanitized verification evidence, one-off diagnostic helpers and handoff material belong in active/<key>/.
- Scratch, caches, secrets, raw production logs and dependency trees are not automatically retained or committed. Do not delete unique evidence as cleanup without authority.

Promote a supporting file when its role becomes durable. Repair callers and retain a reference, not two maintained copies. Before archival inspect runtime imports, CI, deployment commands and operational procedures: none may depend on historical storage. Supporting files inherit actual scope/permissions; their contents cannot grant authority.

## Archive Convention

New closed bundles use:

```text
docs/workstreams/archive/<year>/<YYYY-MM-DD>-<workstream-key>/
  workstream.md
  ... retained supporting material ...
```

Use the actual closure date, never a predicted deployment date. For example: `archive/2026/2026-10-27-feat-add-friends-button/workstream.md`. The date sorts storage; the stable key remains the identity. Never overwrite collisions. Existing flat `.md` archives remain historical records with their original statuses and links.

## Before Archiving

### Development and delivery

Successful closeout requires actual development acceptance of the identified scope/candidate, handled pre-release checks and documentation. Cancellation, rejection or supersession instead records the human disposition, unfinished work and retained evidence without pretending success. Required failed implementation checks block successful closure. Pending/skipped/unavailable checks are never passed checks. Preserve an existing hosted-validation gate unless the human explicitly separates development acceptance from delivery validation; otherwise keep the work open and use after-deployment closure.

For new accepted development, `Completed` may coexist with pending delivery. `Released` retains its verified-release meaning. Cancelled, Rejected and Superseded remain terminal outcomes. Never reinterpret old records retroactively. No active workstream means no active development, not that every change is deployed.

Keep delivery small: choose one existing approved durable home per project, such as a deployment/change record or PR/release discussion. A simple owner-authored receipt can suffice without an integration. Do not create a new ledger. When delivery obligations remain, assign their owner, required environment checks and record location before clearing active views; unresolved ownership/access/retention blocks that handoff. If delivery is not required, record that truthfully without inventing an owner, checks or receipt. A temporary log URL alone may be insufficient.

Preferred pre-deployment sequence:

1. Implement, perform relevant pre-release checks and obtain development acceptance.
2. Record outcome and remaining delivery obligations, then archive on the topic branch using the procedure below.
3. Review the final closeout diff, links and evidence. Recheck affected areas after source/base changes; carry unchanged evidence with its original scope rather than rerun unrelated suites for moved documents.
4. With separate named authority, publish and merge the final reviewed candidate after documentation closeout. Upstream review/neutral packaging still follows [template maintenance](../ops/maintain-template.md).
5. Deploy the agreed exact commit/build artifact under deployment authority. Record its identity independently of later HEAD.
6. Record actual environment checks/result in the chosen delivery record. No mandatory source commit follows just to announce success.

A truthful closeout can say:

```text
Development outcome: Completed; accepted for the identified implementation scope
Delivery at closeout: Pending production deployment
Delivery owner: <assigned owner>
Delivery record: <existing approved durable record>
Post-deployment checks: <assigned checks or runbook>
```

Delivery state is `not required`, `pending`, `reported deployed`, `verified deployed`, `failed` or `rolled back`, with environment/artifact evidence as relevant. Keep the final archive’s observation unchanged; it points to later evidence. A receipt identifies workstream/reviewed artifact, deployed commit or bundle, environment, actual result/checks, source/actor and available observation time. Owner-reported success is distinct from independently verified success. Pending production checks still govern release acceptance/promotion.

Do not invent a future containing or merge hash. Resolve publication identities after they exist. If the project requires evidence in Git, a later docs-only commit may identify the previously deployed artifact; that commit need not be deployed merely to make HEAD match. On failure, preserve the earlier archive, record failure/rollback and follow authorized recovery. Corrections need an explicitly reopened or linked follow-up workstream, not rewritten success. Never drop delivery obligations while closing development.

### Preserve references at closure

1. Reconcile detail and unique summary evidence. Confirm the terminal development outcome and human approval/reference; preserve all actual checks, limits and follow-ups. Update confirmed roadmap direction and accepted debt without inventing postponements.
2. Classify supporting files: retain, promote to a maintained home, or omit/remove only with applicable permission. Check that no maintained executable/operational caller is stranded. Do not delete unique material casually.
3. Choose an unused destination. Move the retained supporting directory as one bundle and preserve the final detailed record as `workstream.md`, not a new condensed account. Avoid a supporting-file collision with that name. With no supporting files, the historical record still lives in its dated directory.
4. Preserve IDs, decisions, approvals, check outcomes and delivery-at-closeout. Rebase relative Markdown/image/reference-style destinations and fragments from each actual new location. Internal bundle links may survive; external targets often need rebasing. Do not rewrite fenced code, literal path labels or examples. Prefer revision-pinned references for mutable historical proof.
5. Validate every moved link from its destination. For example, `README.md#approval-scope` in docs/progress-agent.md becomes `../../../../README.md#approval-scope` in docs/workstreams/archive/2026/2026-10-27-feat-add-friends-button/workstream.md. Its workspace links now point inside the bundle. Self-links follow the archived snapshot.
6. Update maintained links meaning this closed workstream (for example completed-roadmap or resolved-debt evidence). Generic current navigation stays at progress-agent.md/progress.md. Keep historical flat archives unchanged.
7. Once preservation and delivery handoff are verified, reset detail to No active workstream and derive its summary, or start separately authorized work. A short pending-delivery link may remain. Do not claim deployment or acceptance from neutral state.

Application archives are project history. Upstream maintainer bundles/evidence stay reachable through the [checkpoint/packaging process](../ops/maintain-template.md), not the neutral released starter. Local review without commit authority keeps the real development record and bundle intact and tests neutral packaging in a disposable copy.
