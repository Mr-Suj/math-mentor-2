from app.agents.parser_agent import parse_math_problem

question = "Find derivative of x^2 + 3x"

result = parse_math_problem(question)

print(result)