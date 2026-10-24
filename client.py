"""Semantic Pull Request Blast Radius & Risk Scorer.
100% Python Standard Library.
"""

class PRBlastRadiusScorer:
    """Evaluates pull request lines changed, modified exports, and public API mutations to score blast radius."""

    @staticmethod
    def score_blast_radius(lines_added: int, lines_deleted: int, public_functions_changed: int, migration_scripts_touched: bool) -> dict:
        total_churn = lines_added + lines_deleted
        base_score = min(40.0, total_churn * 0.1)
        api_score = min(40.0, public_functions_changed * 10.0)
        migration_penalty = 20.0 if migration_scripts_touched else 0.0

        risk_score = round(base_score + api_score + migration_penalty, 1)
        tier = "CRITICAL_RISK" if risk_score >= 70.0 else ("MEDIUM_RISK" if risk_score >= 35.0 else "LOW_RISK")

        return {
            "total_churn_lines": total_churn,
            "public_functions_changed": public_functions_changed,
            "risk_score": risk_score,
            "risk_tier": tier,
            "requires_senior_approval": risk_score >= 50.0
        }
