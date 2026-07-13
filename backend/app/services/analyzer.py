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

    # Check for TODO comments
    if "TODO" in code:
        issues.append("TODO comments found. Complete them before deployment.")

    # Check for very long files
    lines = code.splitlines()
    if len(lines) > 300:
        issues.append("Large file detected. Consider splitting it into smaller modules.")

    score = max(100 - (len(issues) * 10), 50)

    return {
        "score": score,
        "issues": issues,
        "summary": "Analysis completed successfully."
    }