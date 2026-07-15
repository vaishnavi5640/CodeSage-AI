from app.services.syntax_checker import check_syntax
from app.services.security_checker import check_security
from app.services.metrics import get_metrics
from app.services.quality_checker import check_quality


def analyze_code(code: str):

    # -------------------------
    # Syntax Check
    # -------------------------
    syntax_issues = check_syntax(code)

    if syntax_issues:
        return {
            "score": 50,
            "grade": "D",
            "metrics": {},
            "issues": syntax_issues,
            "recommendations": [
                "Fix syntax errors before running further analysis."
            ],
            "summary": "Syntax errors detected."
        }

    # -------------------------
    # Metrics
    # -------------------------
    metrics = get_metrics(code)

    # -------------------------
    # Security
    # -------------------------
    security_issues, security_recommendations = check_security(code)

    # -------------------------
    # Quality
    # -------------------------
    quality_issues, quality_recommendations = check_quality(code, metrics)

    # -------------------------
    # Merge Results
    # -------------------------
    issues = security_issues + quality_issues
    recommendations = security_recommendations + quality_recommendations

    score = max(100 - len(issues) * 10, 50)

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"

    return {
        "score": score,
        "grade": grade,
        "metrics": {
            "total_lines": metrics["total_lines"],
            "functions": metrics["functions"],
            "classes": metrics["classes"],
            "comments": metrics["comments"]
        },
        "issues": issues,
        "recommendations": recommendations,
        "summary": "Code analysis completed successfully."
    }