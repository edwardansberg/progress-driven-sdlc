# Security Documentation

Store maintained trust boundaries, authentication and authorization inventories, threat assumptions, audit procedures, secret contracts, and security runbooks here.

## Rules

- Describe credential and secret names only when they define a reusable configuration contract; never record values.
- Derive security claims from current code, configuration, infrastructure, tests, and observed behavior.
- Distinguish authentication, authorization, tenant ownership, network placement, and encryption rather than treating one as proof of another.
- Record verified gaps and their present impact in the active workstream. If remediation is accepted but postponed, add it to `docs/techdebt.md`.
- Treat changes to authentication, authorization, secrets, trust boundaries, external exposure, privacy, or destructive controls as high-risk work.
- Keep audit evidence concise and sanitized. Do not paste sensitive payloads or raw production logs.
