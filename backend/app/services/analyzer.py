import ast

def analyze_code(code: str):
    issues = []
    recommendations = []

    # -------------------------
    # Syntax Check
    # -------------------------
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        issues.append(f"Syntax Error at line {e.lineno}: {e.msg}")

        return {
            "score": 50,
            "grade": "D",
            "issues": issues,
            "recommendations": [
                "Fix the syntax errors before running further analysis."
            ],
            "summary": "Syntax errors detected."
        }

    # -------------------------
    # Print Statement Check
    # -------------------------
    if "print(" in code:
        issues.append("Avoid unnecessary print statements in production.")
        recommendations.append("Remove debug print statements.")

    # -------------------------
    # Security Checks
    # -------------------------
    if "eval(" in code:
        issues.append("Security Risk: Avoid using eval().")
        recommendations.append("Replace eval() with a safer alternative.")

    if "exec(" in code:
        issues.append("Security Risk: Avoid using exec().")
        recommendations.append("Avoid exec() because it can execute arbitrary code.")

    # -------------------------
    # TODO Check
    # -------------------------
    if "TODO" in code:
        issues.append("TODO comments found.")
        recommendations.append("Complete TODO items before deployment.")

    # -------------------------
    # Large File Check
    # -------------------------
    if len(code.splitlines()) > 300:
        issues.append("Large file detected.")
        recommendations.append("Split the file into smaller modules.")

    # -------------------------
    # Collect Imports
    # -------------------------
    imported_modules = []
    used_names = []

    # Variables
    assigned_variables = []
    used_variables = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imported_modules.append(alias.name)

        elif isinstance(node, ast.Name):

            if isinstance(node.ctx, ast.Store):
                assigned_variables.append(node.id)

            elif isinstance(node.ctx, ast.Load):
                used_variables.append(node.id)
                used_names.append(node.id)

    # -------------------------
    # Unused Imports
    # -------------------------
    for module in imported_modules:
        short_name = module.split(".")[0]

        if short_name not in used_names:
            issues.append(f"Unused import: {module}")
            recommendations.append(f"Remove unused import '{module}'.")

    # -------------------------
    # Unused Variables
    # -------------------------
    for variable in assigned_variables:

        if variable not in used_variables:

            if not variable.startswith("_"):

                issues.append(f"Unused variable: {variable}")
                recommendations.append(
                    f"Remove the unused variable '{variable}' or use it."
                )

    # -------------------------
    # Score
    # -------------------------
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
        "issues": issues,
        "recommendations": recommendations,
        "summary": "Code analysis completed successfully."
    }