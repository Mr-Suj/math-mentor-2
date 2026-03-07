from app.memory.sqlite_memory import save_solution


def request_human_review(question, parsed_problem, solver_output):

    print("\n⚠️ Low confidence solution detected")
    print("Question:", question)
    print("Model Solution:", solver_output["symbolic_solution"])

    corrected_solution = input("\nEnter corrected solution: ")

    corrected_explanation = input("\nEnter corrected explanation: ")

    corrected_output = {
        "symbolic_solution": corrected_solution,
        "explanation": corrected_explanation
    }

    save_solution(question, parsed_problem, corrected_output)

    return corrected_output