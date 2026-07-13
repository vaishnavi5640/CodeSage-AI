import ast

def analyze_code(code: str):
    issues = []

    # Check Python syntax
    try:
        ast.parse(code)
    except SyntaxError as e:
        issues.append(f"Syntax Error at line {e.lineno}: {e.msg}")

    # Check for print statements
    if "print(" in code:
        issues.append("Avoid unnecessary print statements in production.")

    # Security checks
    if "eval(" in code:
        issues.append("Security Risk: Avoid using eval().")

    if "exec(" in code:
        issues.append("Security Risk: Avoid using exec().")

    # Check for TODO comments
    if "TODO" in code:
        issues.append("TODO comments found. Complete them before deployment.")

    # Check for very long files
    lines = code.splitlines()
    if len(lines) > 300:
        issues.append("Large file detected. Consider splitting it into smaller modules.")

    # Calculate score
    score = max(100 - (len(issues) * 10), 50)

    # Assign grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"

    # Recommendations
    recommendations = []

    if "print(" in code:
        recommendations.append("Remove unnecessary print statements.")

    if "eval(" in code:
        recommendations.append("Replace eval() with safer alternatives.")

    if "exec(" in code:
        recommendations.append("Avoid exec() to prevent code injection risks.")

    if "TODO" in code:
        recommendations.append("Finish all TODO items before deployment.")

    if len(lines) > 300:
        recommendations.append("Split large files into smaller modules.")

    return {
        "score": score,
        "grade": grade,
        "issues": issues,
        "recommendations": recommendations,
        "summary": "Code analysis completed successfully."
    }