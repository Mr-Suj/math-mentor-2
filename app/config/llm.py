import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(question: str):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
