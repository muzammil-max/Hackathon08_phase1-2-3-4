<!--
SYNC IMPACT REPORT
Version: 1.0.0 -> 2.0.0
Modified Principles:
- Replaced "Minimal & Fast Interactions" with "Single Source of Truth"
- Replaced "Clear Structure" with "Stability & Preservation"
- Replaced "Reliability & Persistence" with "Deterministic & Auditable"
- Replaced "Modularity & Extensibility" with "Security First"
- Replaced "Incremental Progression" with "Modern Stack Mandate"
Added Sections:
- Role
- Objective
- Mandatory Capabilities
- Technology Mandate
- API Constitution
- Security Constitution
- Backend Rules
- Frontend Rules
- Data Integrity
- Non-Negotiables
- Success Criteria
Templates Status:
- .specify/templates/plan-template.md: ✅ Compatible
- .specify/templates/spec-template.md: ✅ Compatible
- .specify/templates/tasks-template.md: ✅ Compatible
-->
# MyTodoApp — Web Expansion Constitution

## Role

You are an **expert full-stack engineer** operating under a **strict spec-driven workflow** using **Gemini**.
You must evolve MyTodoApp from a CLI tool into a **secure, multi-user web application**.

## Core Principles

### I. Single Source of Truth
Specs are the **single source of truth**. There must be no implementation without spec reference. If the spec and code disagree, the spec is right (or must be updated first).

### II. Stability & Preservation
No breaking changes to Phase 1 logic are permitted. All Phase 1 Todo features must be preserved in the new system. The system must evolve, not regress.

### III. Deterministic & Auditable
Behavior must be deterministic and auditable. Gemini must reason before generating code. Every action should have a clear, traceable cause and effect.

### IV. Security First
Security is foundational, not an afterthought. The system must support multi-user isolation with JWT-based authentication. User identity is derived **only** from the JWT. Server enforces task ownership.

### V. Modern Stack Mandate
The technology stack is non-negotiable. No substitutions allowed.
- **Frontend**: Next.js (App Router)
- **Backend**: FastAPI
- **ORM**: SQLModel
- **Database**: PostgreSQL (Neon)
- **Auth**: Better Auth (JWT)
- **AI**: Gemini

## Objective

Transform the existing CLI Todo app into a **modern full-stack web app** with authentication, persistence, and a stable API—while preserving core task semantics.

## Mandatory Capabilities

- Multi-user support
- JWT-based authentication
- Persistent database storage
- RESTful API
- Responsive web interface
- All Phase 1 Todo features preserved

## API Constitution (Immutable)

- REST-only
- Stateless
- User-scoped resources

**Endpoints:**
- `GET    /api/tasks`
- `POST   /api/tasks`
- `GET    /api/tasks/{id}`
- `PUT    /api/tasks/{id}`
- `DELETE /api/tasks/{id}`
- `PATCH  /api/tasks/{id}/complete`

API shapes must not change across phases.

## Security Constitution

- JWT required for all routes.
- Token via `Authorization: Bearer <token>`.
- User identity derived **only** from JWT.
- Server enforces task ownership.
- Missing or invalid token → `401`.

## Backend Rules

- Stateless FastAPI.
- No session storage.
- SQLModel for all DB access.
- Strict user isolation.
- No hardcoded secrets.

## Frontend Rules

- Next.js App Router.
- Auth-aware routing.
- Centralized API client.
- Clear loading and error states.

## Data Integrity

- Each task belongs to exactly one user.
- No cross-user data access.
- Deletions are permanent unless archived.

## Non-Negotiables

- No silent failures.
- No undocumented behavior.
- No shared user data.
- No deviation from spec.

## Success Criteria

- Secure multi-user Todo web app.
- Stable REST API.
- Persistent PostgreSQL storage.
- Clean separation of concerns.
- Fully spec-compliant Gemini output.

## Governance

This constitution supersedes all other practices. Amendments require documentation and approval. All PRs and reviews must verify compliance with these principles.

**Version**: 2.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-02-05