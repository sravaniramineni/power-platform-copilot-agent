# Power Platform Copilot Agent

An enterprise Copilot Studio agent blueprint — knowledge-grounded, governed, and measurable — plus a runnable topic-routing regression suite so you can verify the design before building it in Copilot Studio.

## When to use this

Copilot Studio agents are easy to demo and hard to productionize: knowledge sprawl, missing guardrails, unclear escalation, no evals. This repo is the design artifact an architect hands to the delivery team: topics, knowledge sources, guardrails, escalation paths, ALM plan — with a regression suite that proves the routing logic.

## How it works

1. **Generate the agent manifest** — `python src/agent_manifest.py` prints a JSON blueprint:
   agent name, topics (IT helpdesk, HR policy, Invoice status), knowledge sources
   (Dataverse `kb_articles`, SharePoint SOP library), actions (`create_ticket`, `lookup_invoice`),
   guardrails (DLP enforced, human approval for refunds, PII redaction), and the escalation path.
2. **Recreate this manifest as topics + knowledge in Copilot Studio** — it's your build spec.
3. **Run the regression suite** — `python src/eval_topics.py` routes golden utterances from
   `data/golden_utterances.jsonl` through `route()` and checks each lands on the expected topic.
   Exit code 0 = all pass; CI runs this on every push.
4. **Follow the ALM plan** in `docs/ARCHITECTURE.md` — solution packaging across Dev/Test/Prod
   with deployment pipelines, so the agent ships like real software.

## Project structure

```
src/agent_manifest.py      Generates the agent blueprint as JSON
src/eval_topics.py         Topic-routing regression eval over golden utterances
data/golden_utterances.jsonl   {"id", "utterance", "expected_topic"} cases
docs/ARCHITECTURE.md       Topics, knowledge grounding, guardrails, ALM, eval checklist
docs/ADR-001.md            Design decisions
Dockerfile                 Container image
.github/workflows/ci.yml   CI: runs the routing eval on every push
```

## Prerequisites

- Python 3.11+ (pyyaml only, per `requirements.txt`)

## Quickstart

```bash
pip install -r requirements.txt

# 1. Print the agent blueprint
python src/agent_manifest.py
```

Example output:

```json
{
  "agent": "Enterprise Knowledge Agent",
  "topics": ["IT helpdesk", "HR policy", "Invoice status"],
  "knowledge_sources": ["Dataverse: kb_articles", "SharePoint: SOP library"],
  "actions": ["create_ticket", "lookup_invoice"],
  "guardrails": ["DLP enforced", "human approval for refunds", "PII redaction"],
  "escalation": "Route to human agent with transcript summary"
}
```

```bash
# 2. Run the topic-routing regression suite (4/4 expected)
python src/eval_topics.py
```

Expected output:

```
it-01 PASS
hr-01 PASS
inv-01 PASS
esc-01 PASS
4/4 passed
```

## Adding your own cases

Append lines to `data/golden_utterances.jsonl`:

```jsonl
{"id": "inv-02", "utterance": "Where is my invoice for last month?", "expected_topic": "Invoice status"}
{"id": "it-02", "utterance": "I forgot my laptop in the office", "expected_topic": "IT helpdesk"}
```

Then extend `route()` in `src/eval_topics.py` to handle them — the eval fails until routing is correct, which is exactly the TDD loop you want before touching Copilot Studio.

## Running the tests / CI

Every push runs the routing eval via `.github/workflows/ci.yml`:

```bash
python src/eval_topics.py
```

## Taking this to production

- Mirror the manifest's topics and knowledge sources 1:1 in Copilot Studio; keep this repo as the version-controlled source of truth.
- Add a grounding eval: for sampled answers, verify citations resolve to real `kb_articles` rows (grounding score ≥ 0.8 before release).
- Log conversations to Dataverse and track containment rate, escalation rate, and CSAT per topic.

## Further reading

- `docs/ARCHITECTURE.md` — topics, knowledge grounding, guardrails, ALM, eval checklist
- `docs/ADR-001.md` — design decisions
