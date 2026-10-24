"""Example usage for PR Blast Radius Scorer."""
from client import PRBlastRadiusScorer

if __name__ == "__main__":
    res = PRBlastRadiusScorer.score_blast_radius(120, 30, 4, True)
    print("Risk Tier:", res["risk_tier"], "Score:", res["risk_score"])
