from typing import TypedDict

from app.agents.parser_agent import parse_math_problem
from app.agents.solver_agent import solve_problem
from app.agents.verifier_agent import verify_solution
from app.rag.retriever import retrieve_context

from langgraph.graph import StateGraph

class MathState(TypedDict):

    question: str
    parsed_problem: dict
    context: list
    solution: dict
    verification: dict

def parser_node(state):

    parsed = parse_math_problem(state["question"])

    state["parsed_problem"] = parsed

    return state


def retriever_node(state):

    expression = state["parsed_problem"]["expression"]

    context = retrieve_context(expression)

    state["context"] = context

    return state


def solver_node(state):

    solution = solve_problem(state["parsed_problem"])

    state["solution"] = solution

    return state


def verifier_node(state):

    verification = verify_solution(
        state["parsed_problem"],
        state["solution"]
    )

    state["verification"] = verification

    return state

def build_graph():

    workflow = StateGraph(MathState)

    workflow.add_node("parser", parser_node)
    workflow.add_node("retriever", retriever_node)
    workflow.add_node("solver", solver_node)
    workflow.add_node("verifier", verifier_node)

    workflow.set_entry_point("parser")

    workflow.add_edge("parser", "retriever")
    workflow.add_edge("retriever", "solver")
    workflow.add_edge("solver", "verifier")

    workflow.set_finish_point("verifier")

    return workflow.compile()