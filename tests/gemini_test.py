from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("KEY:", api_key)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="2+2=?"
)

print(response.text)



# from google import genai
# import os

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# # response = client.models.generate_content(
# #     model="gemini-1.5-pro",
# #     contents="Solve: derivative of x^2"
# # )

# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)


# from google import genai
# import os

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# def generate(prompt):
#     response = client.models.generate_content(
#         model="gemini-1.5-pro",
#         contents=prompt
#     )
#     return response.text