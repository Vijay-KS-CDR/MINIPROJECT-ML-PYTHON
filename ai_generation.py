from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ai_questions(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Generate exam-style questions from the paragraph.

RULES:
- Questions must be full sentences
- Start with What / Which / Who / Where
- Answers must be ONE WORD

Format:
Q1: question
A1: answer

{text}
"""
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ ERROR:", e)
        return None