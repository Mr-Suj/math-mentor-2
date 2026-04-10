from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.workflow.math_graph import build_graph

app = FastAPI()


class MathRequest(BaseModel):
    question: str


# -------------------------
# TEXT ENDPOINT
# -------------------------
@app.post("/solve_text")
async def solve_text(request: MathRequest):
    result = build_graph(request.question)

    return {
        "solution": result["solution"],
        "explanation": result["explanation"],
        "verification": result["verification"]
    }


# -------------------------
# IMAGE ENDPOINT (TEMP DISABLED HEAVY LOGIC)
# -------------------------
@app.post("/solve_image")
async def solve_image(file: UploadFile = File(...)):

    # Just save file (no OCR to avoid heavy memory usage)
    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    os.remove(temp_path)

    return {
        "extracted_question": "Image processing temporarily disabled (free tier limitation)",
        "solution": "Not available",
        "explanation": "OCR disabled to reduce memory usage",
        "verification": {}
    }


# -------------------------
# AUDIO ENDPOINT (TEMP DISABLED)
# -------------------------
@app.post("/solve_audio")
async def solve_audio(file: UploadFile = File(...)):

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    os.remove(temp_path)

    return {
        "transcribed_question": "Audio processing temporarily disabled (free tier limitation)",
        "solution": "Not available",
        "explanation": "Speech-to-text disabled to reduce memory usage",
        "verification": {}
    }

@app.get("/")
def home():
    return {"message": "Backend is running"}
