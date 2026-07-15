def check_security(code: str):
    issues = []
    recommendations = []

    if "eval(" in code:
        issues.append("Security Risk: Avoid using eval().")
        recommendations.append("Replace eval() with a safer alternative.")

    if "exec(" in code:
        issues.append("Security Risk: Avoid using exec().")
        recommendations.append("Avoid exec() because it can execute arbitrary code.")

    return issues, recommendations