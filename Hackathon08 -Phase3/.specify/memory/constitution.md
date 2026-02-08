<!--
SYNC IMPACT REPORT
Version: 2.0.0 -> 3.0.0
Modified Principles:
- Complete overhaul for Phase 3 (AI Chatbot System)
- Replaced "Web Expansion" focus with "AI Chatbot" focus
- Updated Technology Mandate (Added MCP, Agents SDK)
Added Sections:
- Constitutional Principles
- Agent Law
- MCP Tool Law
- Conversation Law
- Architecture Law
Templates Status:
- .specify/templates/plan-template.md: ✅ Compatible
- .specify/templates/spec-template.md: ✅ Compatible
- .specify/templates/tasks-template.md: ✅ Compatible
-->
# MyTodoApp · AI Chatbot System (Gemini)

## Role
You are an **AI systems engineer** building a **stateless, tool-driven Todo chatbot** using Gemini reasoning, MCP architecture, and agent-based execution.

## Constitutional Principles
- Specs are authoritative
- No hidden state in memory or server
- All intelligence flows through tools
- Conversation state persists only in database
- Agents reason first, then act
- Every action must be explainable and auditable

## Objective
Introduce a **natural-language chatbot interface** that allows users to manage todos conversationally, while preserving strict backend control through MCP tools.

## Core Capabilities
- Natural language task management
- Stateless chat processing
- Persistent conversation history
- Tool-based task execution
- Multi-user isolation
- Authentication-enforced access

## Architecture Law
- Frontend communicates only with `/api/chat`
- Backend holds no in-memory session state
- AI agents **cannot directly modify database**
- All task mutations occur via MCP tools
- MCP tools are stateless and deterministic

## Technology Mandate
| Component | Required Stack |
|--------|----------------|
| Frontend | OpenAI ChatKit |
| Backend | FastAPI |
| AI Logic | OpenAI Agents SDK |
| Tool Layer | Official MCP SDK |
| ORM | SQLModel |
| Database | Neon PostgreSQL |
| Auth | Better Auth |
| AI Reasoning | Gemini |

No substitutions or bypasses allowed.

## Security Constitution
- JWT required for all chat requests
- User identity derived only from token
- Agent never trusts user-provided user_id
- Tool calls validated against authenticated user
- Cross-user access is forbidden

## Agent Law
- Agent must infer intent before acting
- Agent must choose correct MCP tool
- Agent may chain tools if required
- Agent must confirm completed actions
- Agent must handle ambiguity safely
- Agent must fail gracefully

## MCP Tool Law
- Tools expose **only task operations**
- Tools accept validated parameters
- Tools return structured results
- Tools never contain business logic outside scope
- Tools do not store memory

## Conversation Law
- Each request is independent
- History is reconstructed from database
- Messages are stored before and after agent run
- Server restart must not affect continuity

## Non-Negotiables
- No direct DB access by agent
- No implicit memory
- No silent tool calls
- No user data leakage
- No deviation from specs

## Success Criteria
- Users manage tasks via natural language
- Agent reliably maps intent → tool
- Conversations resume after restart
- Server remains fully stateless
- System behaves deterministically and securely

## Governance
This constitution supersedes all other practices. Amendments require documentation and approval. All PRs and reviews must verify compliance with these principles.

**Version**: 3.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-02-05
