import json
from app.config.llm import generate_response


def parse_math_problem(text: str):
    prompt = f"""
    You are an AI math parser.

    Convert the math question into structured JSON.

    Question:
    {text}

    Extract:
    - problem_type: algebra | calculus | trigonometry | geometry | statistics | arithmetic
    - operation: solve | simplify | derivative | integral | evaluate | factor | expand | limit
    - expression: main mathematical expression
    - variables: list of variables present
    - difficulty: school | jee | olympiad

    Return valid JSON only (no markdown):
    {{
    "problem_type": "",
    "operation": "",
    "expression": "",
    "variables": [],
    "difficulty": ""
    }}

    """

    response = generate_response(prompt)

    try:
        parsed = json.loads(response)
    except:
        parsed = {
            "problem_type": "unknown",
            "operation": "unknown",
            "expression": text,
            "variables": [],
            "difficulty": "unknown"
        }

    return parsed