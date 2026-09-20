# Power Platform Copilot Agent

Enterprise Copilot Studio agent blueprint: knowledge-grounded, governed, and measurable.

## Problem
Copilot Studio agents are easy to demo but hard to productionize: knowledge sprawl,
missing guardrails, unclear escalation, and no evals.

## What it includes
- Agent blueprint: topics, entities, knowledge sources, escalation paths
- Knowledge grounding over Dataverse, SharePoint, and enterprise APIs
- Guardrails: DLP, auth, PII handling, human-in-the-loop for sensitive actions
- ALM: solution packaging, Dev/Test/Prod, deployment pipelines
- Eval checklist for accuracy, grounding, and escalation quality

## Architecture
See `docs/ARCHITECTURE.md`.

## Quickstart
```bash
pip install -r requirements.txt
python src/agent_manifest.py
```
