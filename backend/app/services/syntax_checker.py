import ast

def check_syntax(code: str):
    try:
        ast.parse(code)
        return []
    except SyntaxError as e:
        return [f"Syntax Error at line {e.lineno}: {e.msg}"]