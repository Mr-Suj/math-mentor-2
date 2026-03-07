from app.agents.parser_agent import parse_math_problem
from app.agents.solver_agent import solve_problem

question = "Find derivative of x^2 + 3x"

parsed = parse_math_problem(question)

solution = solve_problem(parsed)

print(solution)