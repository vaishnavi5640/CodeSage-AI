def check_quality(code: str, metrics):
    issues = []
    recommendations = []

    if "print(" in code:
        issues.append("Avoid unnecessary print statements in production.")
        recommendations.append("Remove debug print statements.")

    if "TODO" in code:
        issues.append("TODO comments found.")
        recommendations.append("Complete TODO items before deployment.")

    if metrics["total_lines"] > 300:
        issues.append("Large file detected.")
        recommendations.append("Split the file into smaller modules.")

    for module in metrics["imports"]:

        short_name = module.split(".")[0]

        if short_name not in metrics["used_names"]:
            issues.append(f"Unused import: {module}")
            recommendations.append(f"Remove unused import '{module}'.")

    for variable in metrics["assigned_variables"]:

        if variable not in metrics["used_variables"]:

            if not variable.startswith("_"):
                issues.append(f"Unused variable: {variable}")
                recommendations.append(
                    f"Remove unused variable '{variable}'."
                )

    return issues, recommendations