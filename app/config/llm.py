import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt: str) -> str:
    try:
        # Load Gemini model
        model = genai.GenerativeModel("gemini-pro")

        # Generate response
        response = model.generate_content(prompt)

        # Return text safely
        if response and hasattr(response, "text"):
            return response.text
        else:
            return "No response generated."

    except Exception as e:
        return f"Error generating response: {str(e)}"
