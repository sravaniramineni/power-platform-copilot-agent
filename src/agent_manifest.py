"""Generate a Copilot Studio agent manifest (blueprint)."""
import json

manifest = {
    "agent": "Enterprise Knowledge Agent",
    "topics": ["IT helpdesk", "HR policy", "Invoice status"],
    "knowledge_sources": ["Dataverse: kb_articles", "SharePoint: SOP library"],
    "actions": ["create_ticket", "lookup_invoice"],
    "guardrails": ["DLP enforced", "human approval for refunds", "PII redaction"],
    "escalation": "Route to human agent with transcript summary",
}

print(json.dumps(manifest, indent=2))
