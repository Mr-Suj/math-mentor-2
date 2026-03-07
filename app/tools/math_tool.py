import sympy as sp
import re


def normalize_expression(expr: str):
    """
    Convert human math notation into SymPy syntax
    """

    # replace ^ with **
    expr = expr.replace("^", "**")

    # convert 3x -> 3*x
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)

    return expr


def solve_expression(expression: str):

    x = sp.symbols('x')

    try:
        normalized = normalize_expression(expression)

        expr = sp.sympify(normalized)

        derivative = sp.diff(expr, x)

        return str(derivative)

    except Exception as e:
        return f"Math tool error: {e}"