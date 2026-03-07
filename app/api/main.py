from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.workflow.math_graph import build_graph
from app.hitl.hitl_manager import handle_hitl
from app.multimodal.ocr import extract_text_from_image
from app.multimodal.speech_to_text import transcribe_audio


app = FastAPI()

graph = build_graph()


class MathRequest(BaseModel):
    question: str


@app.post("/solve_text")
def solve_math_problem(request: MathRequest):

    result = graph.invoke({
        "question": request.question
    })

    final_output = handle_hitl(
        request.question,
        result["parsed_problem"],
        result["solution"],
        result["verification"]
    )

    return {
        "question": request.question,
        "solution": final_output["symbolic_solution"],
        "explanation": final_output["explanation"],
        "verification": result["verification"]
    }

@app.post("/solve_image")
async def solve_image(file: UploadFile = File(...)):

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    question = extract_text_from_image(temp_path)

    os.remove(temp_path)

    result = graph.invoke({
        "question": question
    })

    final_output = handle_hitl(
        question,
        result["parsed_problem"],
        result["solution"],
        result["verification"]
    )

    return {
        "extracted_question": question,
        "solution": final_output["symbolic_solution"],
        "explanation": final_output["explanation"],
        "verification": result["verification"]
    }

@app.post("/solve_audio")
async def solve_audio(file: UploadFile = File(...)):

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    question = transcribe_audio(temp_path)

    os.remove(temp_path)

    result = graph.invoke({
        "question": question
    })

    final_output = handle_hitl(
        question,
        result["parsed_problem"],
        result["solution"],
        result["verification"]
    )

    return {
        "transcribed_question": question,
        "solution": final_output["symbolic_solution"],
        "explanation": final_output["explanation"],
        "verification": result["verification"]
    }