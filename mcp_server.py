"""MCP server for PR Blast Radius Scorer."""
import sys
import json
from client import PRBlastRadiusScorer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "score_pr_blast_radius",
                "description": "Calculates deployment risk score based on PR churn and public symbol mutations",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "lines_added": {"type": "integer"},
                        "lines_deleted": {"type": "integer"},
                        "public_functions_changed": {"type": "integer"},
                        "migration_scripts_touched": {"type": "boolean"}
                    },
                    "required": ["lines_added", "lines_deleted", "public_functions_changed"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "score_pr_blast_radius":
            args = params.get("arguments", {})
            res = PRBlastRadiusScorer.score_blast_radius(
                int(args.get("lines_added", 0)),
                int(args.get("lines_deleted", 0)),
                int(args.get("public_functions_changed", 0)),
                bool(args.get("migration_scripts_touched", False))
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
