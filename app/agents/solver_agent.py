from app.rag.retriever import retrieve_context
from app.config.llm import generate_response
from app.tools.math_tool import solve_expression


def solve_problem(parsed_problem):

    expression = parsed_problem["expression"]

    # retrieve math knowledge
    context = retrieve_context(expression)

    # compute symbolic solution
    symbolic_solution = solve_expression(expression)

    prompt = f"""
    You are a JEE-level mathematics tutor.

    Problem:
    Find the derivative of: {expression}

    Reference math knowledge:
    {context}

    Verified symbolic result:
    {symbolic_solution}

    Explain the solution step-by-step:
    1. Identify the rule(s) used (power rule, product rule, chain rule, etc.).
    2. Apply the rule clearly to the expression.
    3. Show intermediate steps.
    4. Conclude with the final derivative.

    Use the symbolic result as the final answer and ensure the explanation matches it.
    Keep the explanation clear and concise for a JEE student.
    """

    response = generate_response(prompt)

    return {
        "symbolic_solution": symbolic_solution,
        "explanation": response
    }