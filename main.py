from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=" * 50)
print("          EMAIL WRITER AI")
print("=" * 50)

# Get user input
email_request = input("\nEnter your email requirement: ")

prompt = f"""
You are a professional email writer.

Write a complete professional email based on the user's request.

User Request:
{email_request}

Instructions:
1. Generate a suitable subject line.
2. Write a professional greeting.
3. Write the email body.
4. Write a professional closing.
"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nGenerated Email:\n")
    print(response.text)

except Exception as e:
    print("Error:", e)