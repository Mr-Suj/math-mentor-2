import os
import google.generativeai as genai

# Configure API safely
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

def generate_response(prompt: str) -> str:
    try:
        if not API_KEY:
            return "Error: GEMINI_API_KEY not set"

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text
        else:
            return "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"
