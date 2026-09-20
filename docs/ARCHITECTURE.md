# Architecture

## Components
- Copilot Studio: topics, entities, generative answers, actions.
- Knowledge: Dataverse tables, SharePoint sites, Graph connectors with ACLs.
- Actions: Power Automate flows / custom connectors for writes and approvals.
- Identity: Microsoft Entra ID, Dataverse security roles.
- Governance: DLP policies, environment strategy, CoE starter kit.

## Conversation design
- Happy path, clarification, escalation, and fallback topics.
- Every write action confirms entities before executing.
- Sensitive actions require approval and are audit-logged.

## Evals
- Golden utterances per topic; check intent routing.
- Grounding checks: answers cite knowledge sources.
- Regression run on every knowledge update.

## Production hardening
- Monitor containment, escalation rate, and CSAT; review weekly.
