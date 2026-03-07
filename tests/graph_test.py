from app.workflow.math_graph import build_graph

graph = build_graph()

question = "Find derivative of x^2 + 3x"

result = graph.invoke({
    "question": question
})

print(result)