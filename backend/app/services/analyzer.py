def analyze_code(code: str):
    issues = []

    if "print(" in code:
        issues.append("Avoid unnecessary print statements in production.")

    if "==" not in code and "if " in code:
        issues.append("Possible logical condition issue.")

    if len(code) > 1000:
        issues.append("Large file detected. Consider splitting into modules.")

    score = max(100 - len(issues) * 10, 70)

    return {
        "score": score,
        "issues": issues,
        "summary": "Basic analysis completed successfully."
    }