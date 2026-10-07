# Project Blueprint v0.1

Optional reference: read for explicit creation, schema/renderer changes, corruption, compatibility uncertainty, UX redesign or a relevant contract update. Ordinary development does not read or update blueprint files. A normal data-only refresh reads the marked data, source revision, Git delta and affected sources, not this full reference or renderer unless needed.

## Purpose and authority

`docs/project-blueprint.html` is a persistent, revision-bound human mental model of roadmap, major components, relationships and important business/data/integration flows. It favors comprehension over completeness; benefits are untested. One human and one agent suffice; optional collaborators follow existing ownership rules.

It is derived, never authoritative: progress-agent.md owns operational detail, progress.md summarizes current status, and the blueprint explains project-wide structure. Decisions return to authoritative records. UI actions grant no acceptance, merge, deployment or other permission. Creation and every refresh require explicit human requests; no automatic updates or milestone offers. Track it once created, with staging/commit/publication separately authorized. Removal follows normal change authority after preserving any unique decisions in their proper records.

Ad-hoc explainers remain separate: question-specific, usually temporary/untracked and free-form under the core visual-explanation rules. Do not force them into this schema.

## Artifact and schema v1

Copy the [neutral template](project-blueprint-template.html) only for an authorized project creation. Keep one HTML file with stable renderer and one mutable block between `BLUEPRINT_DATA_START` and `BLUEPRINT_DATA_END`, containing `script#blueprint-data` with type `application/json`.

Required top-level fields: `schemaVersion: 1`, `sourceRevision` (full Git SHA or `Unknown`), and arrays `roadmap`, `components`, `flows`. Optional `refresh` contains strings `fromRevision` and/or `notes`. Optional `sources` is an array of repository-relative authoritative-source path strings, shown as text rather than executed or fetched. Do not include secrets or sensitive URL parameters. Omit unknown optional facts; do not invent placeholder project facts.

- Roadmap: required `id`, `title`, `status`; optional `summary`, `components` (component ID strings), `gates` (strings). Status is one of `completed`, `current`, `planned`, `paused`, `unknown`; these are display categories, not replacement workflow statuses. Retain actual gates in context.
- Component: required `id`, `name`, `kind`, `summary`; optional string arrays `responsibilities`, `interfaces`, `paths`, and `relationships` objects with required `target` component ID and `kind`, optional `label`. Kinds are descriptive, not a universal ontology.
- Flow: required `id`, `name`, `steps`; optional `summary`. Ordered steps contain required `component` ID and `label`.
- IDs are nonempty lowercase ASCII/hyphen strings, unique within each entity type. Retain an ID while the same represented concept persists; a display-name change alone needs no new ID. A genuinely new or replaced concept gets its own ID. Never reuse an old ID merely to minimize a diff. Resolve all roadmap component, relationship and flow references. Roadmap IDs identify items; there is no invented roadmap-reference field.

The renderer rejects unsupported versions, unknown fields, wrong types, duplicate IDs and unresolved references before displaying model content. A schema change needs explicit reconciliation, not silently dropping data. Runtime validation proves structure, not project truth.

## Views and interaction

Overview shows only a compact roadmap/status list and major component map with concise component summaries and textual relationships, including relationship labels. Roadmap exposes summaries, related components and contextual gates. Components exposes responsibilities, relationships, useful interfaces and selected paths. Flows uses ordered textual steps linking to components. Blueprint Info shows version, represented revision, optional refresh/source references and governance/freshness limits.

Use overview first and native details on demand. Progressive disclosure may hide secondary detail, but never hide or truncate qualifications that change the meaning of visible content (such as proposed, partial, uncertain or not implemented). Keep routine governance in Blueprint Info; normal populated views with a known revision need no governance notice. Keep actionable error, Unknown-revision and empty-template notices prominent. No required purpose/persona boilerplate, separate Risks page, duplicated permanent risk/current-work widgets, fake refresh controls, approvals or repository inspection. Native buttons switch views and select/focus component detail; textual maps and ordered lists carry all visual information.

## Revision and freshness

`sourceRevision` means the project revision whose authoritative state was inspected and represented, never the future commit containing the generated HTML. If project A is inspected and blueprint commit B follows, A remains correct. There is no `deliveryRevision` field or containing-hash chase.

Inspect contents of A..B before deciding freshness. Exclude changes exclusively to the blueprint or its delivery/evidence metadata; do not exempt whole progress files if substantive project state also changed. A blueprint-only/evidence-only commit does not invalidate the model or require advancing A. Git delta routes inspection; it is not project truth. The browser cannot detect freshness.

For dirty work, distinguish HEAD evidence from uncommitted observations. By default represent committed project state and disclose excluded dirty work in the workstream. Do not label mixed dirty facts as represented by HEAD; resolve the intended snapshot with the human before including them. `Unknown` is honest recovery metadata, not a substitute for a known dirty snapshot. A verified refresh binds to the exact reconciled committed state; if that cannot be established, retain uncertainty and report the refresh incomplete.

## Create or refresh

Before writes inspect identity, instructions, authority, branch/HEAD and staged/unstaged/untracked work; preserve occupied artifacts and concurrent changes. Record scope/checks in the existing workstream, not a new status register. No dependency installation or extra delivery authority follows from a request.

Creation: read this contract and template; inspect relevant authoritative records and implementation for major concepts. Build and validate data, safely embed it, then create `docs/project-blueprint.html`. Keep it absent from the upstream neutral starter. Inspect HTML/scripts before local preview. Hand off actual evidence and limitations for human review.

Explicit refresh:

1. Extract exactly one marked data block; read its version and sourceRevision A. Resolve HEAD B and dirty state.
2. Inspect `git log A..B` and a bounded diff/change summary. Verify ancestry; classify maintenance-only changes by content as above.
3. Map project-relevant changes to roadmap, components, relationships and flows. Inspect affected authoritative sources/implementation sufficient to verify those concepts.
4. Update only structured data; preserve stable IDs and normally every renderer byte outside the block. Advance sourceRevision only to the project revision actually reconciled, after checks. If no project-relevant change exists, make no data/metadata churn.
5. Validate structure, references, affected facts and appropriate rendering. Repeating the same refresh must propose no unnecessary changes. Report omitted evidence and pending human checks.

Broaden inspection when A is Unknown/unavailable, history was rewritten, delta is too large/ambiguous, data is inconsistent, or selective coverage cannot be justified. Explain the limitation; do not fabricate continuity. First creation, schema mismatch/change, renderer defect/change, corruption, uncertain compatibility, explicit UX redesign or relevant contract updates require full contract/template reading. Normal refresh does not silently upgrade the renderer. Recheck file pre-images before writes; reconcile concurrent edits rather than overwrite them.

## Security and accessibility

Self-contained/offline is not a sandbox. Use semantic HTML, inline CSS and small vanilla JS; ordinary `file://` viewing needs no server. No external dependencies/assets/fonts, network APIs, telemetry, cookies/storage, service workers, automatic filesystem/repository access, iframe, `eval`, `new Function` or project-controlled HTML sinks. CSP is not required and is not a sandbox. Do not add outbound links containing sensitive data.

Serialize JSON first, then replace literal `<` with `\u003c` before embedding; this prevents project text such as a closing script tag from terminating the data element. Do not concatenate raw project strings into HTML. Parse only the identified JSON block; use createElement/textContent/append for project text. Display paths/interfaces as text, not executable links.

Provide landmarks/headings, native controls, logical focus order, visible focus, clear labels, text states (not color alone), sufficient contrast and responsive reflow. Keep textual relationships and ordered flow steps; no motion is needed. If motion is later introduced, honor reduced-motion preferences. Preserve a readable text alternative when rendering is unavailable; do not invent a preview URL or attachment.

## Validation and recovery

Record actual commands/fixtures, artifact scope and limits in the existing workstream. Use the smallest meaningful checks; no permanent harness or installation is required.

- Data: parse JSON; verify version, required/types/allowed fields, unique IDs and all references. Check representative roadmap gates, relationships, flows and selected paths against independent source evidence, not renderer output alone.
- Static safety: inspect HTML/scripts for prohibited resources/APIs, secrets, unsafe sinks and script-context serialization. Check neutral template contains no real project model.
- Renderer when available: local opening and runtime errors, five views, component links from map/roadmap/flows, keyboard/focus, narrow width/zoom and textual details. Report unavailable screen-reader/browser checks; never infer WCAG conformance.
- Disposable fixtures outside released state: neutral; 3–5 components/one flow; completed/current/planned roadmap and gate; closing-script/HTML/quotes/Unicode strings; missing reference; duplicate ID; unsupported version; data-only refresh; renderer-change escalation; A followed by blueprint-only B; Unknown/unavailable A; keyboard/navigation.
- Refresh: compare bytes outside the data block, stable IDs and second-pass no-op. Test maintenance-only delta exclusion independently of commit identity. Renderer changes require their relevant full checks.

On malformed/corrupt input, preserve the previous artifact and report the error; do not overwrite unknown facts with neutral data. Roll back only scoped changes after checking intervening edits, retaining evidence. Rendering success proves neither factual accuracy, usability, accessibility conformance nor human acceptance. Publication follows existing named permissions.
