from app.tools.math_tool import solve_expression

def verify_solution(parsed_problem, solver_output):

    expression = parsed_problem["expression"]

    expected_solution = solve_expression(expression)

    model_solution = solver_output["symbolic_solution"]

    if expected_solution == model_solution:
        confidence = 0.95
        status = "verified"

    else:
        confidence = 0.4
        status = "needs_review"

    return {
        "expected_solution": expected_solution,
        "model_solution": model_solution,
        "confidence": confidence,
        "status": status
    }