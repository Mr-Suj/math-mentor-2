from app.agents.parser_agent import parse_math_problem
from app.agents.solver_agent import solve_problem
from app.agents.verifier_agent import verify_solution

question = "Find derivative of x^2 + 3x"

parsed = parse_math_problem(question)

solution = solve_problem(parsed)

verification = verify_solution(parsed, solution)

print("Solution:")
print(solution)

print("\nVerification:")
print(verification)