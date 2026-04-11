import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(question: str):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=question
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
