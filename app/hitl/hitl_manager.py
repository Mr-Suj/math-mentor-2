from app.hitl.human_review import request_human_review
from app.memory.sqlite_memory import save_solution


def handle_hitl(question, parsed_problem, solver_output, verification):

    if verification["confidence"] >= 0.7:

        save_solution(question, parsed_problem, solver_output)

        return solver_output

    else:

        corrected = request_human_review(
            question,
            parsed_problem,
            solver_output
        )

        return corrected