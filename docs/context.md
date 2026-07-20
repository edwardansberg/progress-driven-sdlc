# Project Context

Status: Maintained product and architecture context

Last verified: Not yet initialized

Evidence: Replace this line with the source, configuration, migration, test, Git, and runtime evidence used to verify the document.

This document is the durable orientation guide for the project. It should describe the current product boundary, repository structure, runtime topology, data ownership, trust boundaries, and delivery model. It is intentionally broader than an operations runbook and more stable than the active plan in [progress.md](progress.md).

When this document conflicts with executable or observed evidence, that evidence takes precedence. Correct the document in the same workstream as the behavior it describes.

Remove all bracketed prompts before treating this document as verified project context.

## Product Purpose

[Describe who the product serves, the problem it solves, and the primary user journey. Keep planned capabilities in the roadmap rather than presenting them as current behavior.]

## Architecture at a Glance

[Describe the major components and their communication paths. Add a small Mermaid diagram only if it materially improves understanding.]

## Repository Map

- `[path/]`: [Responsibility and ownership boundary.]
- `[path/]`: [Responsibility and ownership boundary.]

List only maintained areas a contributor needs to orient themselves. Do not turn this into a complete file inventory.

## Runtime and Deployment Topology

### Environments

- `[environment]`: [Source branch or artifact, purpose, URL class, and data-isolation facts.]
- `[environment]`: [Source branch or artifact, purpose, URL class, and data-isolation facts.]

### Runtime components

- `[component]`: [Runtime, ownership, health boundary, dependencies, and scaling model.]
- `[component]`: [Runtime, ownership, health boundary, dependencies, and scaling model.]

Document what actually runs, where it runs, how traffic reaches it, and which state is persistent. Do not include live secrets, addresses, credentials, or personal key names.

## Service Responsibilities and Contracts

- `[service or module]`: [What it owns, what it may call, and the durable interface or health endpoint.]
- `[service or module]`: [What it owns, what it may call, and the durable interface or health endpoint.]

Call out cross-service contracts whose changes require coordinated verification.

## Data and Persistence

- Authoritative stores: [Databases, object stores, queues, or files and what each owns.]
- Major domain groups: [Key entities and relationships.]
- Migration model: [How schema or data changes are reviewed, rehearsed, applied, and verified.]
- Backup and restore boundary: [Where the reusable procedure lives and what evidence is required.]
- Encryption and secret handling: [Names of configuration contracts may be documented; values never are.]

## Authentication and Trust Boundaries

- User authentication: [Session, token, identity provider, and ownership checks.]
- Service authentication: [Service identity, signature, grant, or network boundary.]
- Authorization authority: [Where tenant, role, entitlement, and resource access are decided.]
- External providers: [Credential ownership and the boundary where calls occur.]
- Known limitations: [Verified gaps only; move accepted postponed remediation into `techdebt.md`.]

## Build, Test, and Delivery Flow

### Local baseline

```text
[install command]
[lint command]
[test command]
[build command]
```

### Delivery

- Build artifact: [What is built and how it is identified immutably.]
- Preview path: [Trigger, target, migration behavior, and verification.]
- Production path: [Promotion mechanism and explicit authorization gates.]
- Rollback: [Source, artifact, data, and operational rollback boundaries.]

Commit, push, preview deployment, production promotion, migration, and destructive data maintenance remain separate gates unless the user explicitly combines them.

## Engineering Constraints

- [Durable contract or design constraint contributors must preserve.]
- [Reliability, tenancy, idempotency, cost, or performance constraint.]
- [Platform or compatibility constraint.]

## Sources of Truth and Freshness

Use this order when establishing present behavior:

1. observed target-environment runtime state;
2. deployed commit and effective configuration;
3. current source, migrations, schemas, manifests, workflows, and tests;
4. maintained architecture, security, and operations documentation;
5. historical material under `docs/old/`.

Update this document when a durable product boundary, service responsibility, data owner, trust boundary, topology, environment mapping, deployment mechanism, or major technology choice changes. Put procedural commands in `docs/ops/`, implementation progress in [progress.md](progress.md), and future direction in [roadmap.md](roadmap.md).
