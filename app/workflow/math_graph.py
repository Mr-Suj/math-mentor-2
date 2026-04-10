from app.config.llm import generate_response

def build_graph(question: str):
    return {
        "solution": generate_response(question),
        "explanation": "Generated using Gemini",
        "verification": {}
    }
