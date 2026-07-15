import ast

def get_metrics(code: str):
    tree = ast.parse(code)

    total_lines = len(code.splitlines())
    total_functions = 0
    total_classes = 0
    total_comments = 0

    imported_modules = []
    used_names = []

    assigned_variables = []
    used_variables = []

    for line in code.splitlines():
        if line.strip().startswith("#"):
            total_comments += 1

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            total_functions += 1

        elif isinstance(node, ast.ClassDef):
            total_classes += 1

        elif isinstance(node, ast.Import):
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

    return {
        "total_lines": total_lines,
        "functions": total_functions,
        "classes": total_classes,
        "comments": total_comments,
        "imports": imported_modules,
        "used_names": used_names,
        "assigned_variables": assigned_variables,
        "used_variables": used_variables
    }