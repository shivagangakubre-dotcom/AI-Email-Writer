from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=" * 50)
print("        AI EMAIL WRITER V1")
print("=" * 50)

print("\nSelect Email Type:")
print("1. Leave Request")
print("2. Job Application")
print("3. Meeting Request")
print("4. General Email")

choice = input("\nEnter choice (1-4): ")

email_types = {
    "1": "Leave Request",
    "2": "Job Application",
    "3": "Meeting Request",
    "4": "General Email"
}

email_type = email_types.get(choice, "General Email")

print("\nSelect Tone:")
print("1. Professional")
print("2. Friendly")
print("3. Formal")

tone_choice = input("\nEnter tone (1-3): ")

tones = {
    "1": "Professional",
    "2": "Friendly",
    "3": "Formal"
}

tone = tones.get(tone_choice, "Professional")

user_request = input("\nDescribe your email: ")

prompt = f"""
Write a {tone} {email_type} email.

User Requirement:
{user_request}

Include:
1. Subject
2. Greeting
3. Email Body
4. Closing
"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    email_text = response.text

    print("\nGenerated Email:\n")
    print(email_text)

    with open("generated_email.txt", "w", encoding="utf-8") as file:
        file.write(email_text)

    print("\nEmail saved as generated_email.txt")

except Exception as e:
    print("Error:", e)