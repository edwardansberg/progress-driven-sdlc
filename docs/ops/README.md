# Operations Runbooks

Store reusable deployment, recovery, maintenance, observability, and incident procedures here. Active implementation detail belongs in `docs/progress.md`; durable system shape belongs in `docs/context.md`.

## References

- [Optional execution and review loop](autonomous-review-loop.md): Message protocol, controller target behavior, operator/recovery procedure, and pilot prerequisites. Documentation only; no controller is included or enabled. Authority remains in [canonical policy](../README.md#optional-execution-and-review-loop).

## Runbook Shape

Each runbook should contain only the sections it needs, normally:

- Purpose and scope.
- Preconditions, access boundary, and required authorization.
- Safety checks and exact target identification.
- Procedure using placeholders instead of credentials or personal machine details.
- Expected output or health evidence.
- Failure handling and escalation.
- Rollback or recovery.
- Last verification date and evidence source.

## Rules

- Store each reusable procedure once and link to it elsewhere.
- Separate preview and production steps when their authority or risk differs.
- Never imply that an example command is safe for every environment.
- Verify exact targets before migration, reset, restore, deletion, or broad file operations.
- Do not store secret values, raw production logs, private addresses, or personal key names.
- Update a runbook in the same workstream as the operational behavior it documents.
