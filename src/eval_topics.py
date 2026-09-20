"""Topic-routing regression eval for the Copilot agent blueprint."""
import json
from pathlib import Path

DATA = Path(__file__).parent.parent / "data" / "golden_utterances.jsonl"

def route(utterance: str) -> str:
    u = utterance.lower()
    if "invoice" in u:
        return "Invoice status"
    if "password" in u or "vpn" in u:
        return "IT helpdesk"
    if "leave" in u or "policy" in u:
        return "HR policy"
    if "human" in u or "agent" in u:
        return "Escalation"
    return "Fallback"

def main():
    passed = total = 0
    for line in DATA.read_text().splitlines():
        case = json.loads(line)
        total += 1
        ok = route(case["utterance"]) == case["expected_topic"]
        passed += ok
        print(case["id"], "PASS" if ok else "FAIL")
    print(f"{passed}/{total} passed")
    raise SystemExit(0 if passed == total else 1)

if __name__ == "__main__":
    main()
