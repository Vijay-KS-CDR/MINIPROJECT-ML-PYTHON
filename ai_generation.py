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
                    "content":f"""
Generate exam-style questions from the paragraph.

STRICT RULES:
- Questions must be full sentences
- Start with What / Which / Who / Where

- Answers must be 2 to 4 words
- Answers must be EXACT phrases from the paragraph
- DO NOT give single-word answers
- DO NOT summarize

GOOD EXAMPLE:
Q1: What is Codeforces regarded as?
A1: ultimate proving ground

BAD EXAMPLE:
Q1: What is Codeforces regarded as?
A1: ultimate

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
    

def generate_more_questions(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": f"""
From the paragraph, generate additional questions that can be asked.

IMPORTANT:
- These are NOT quiz questions with answers
- ONLY generate QUESTIONS

RULES:
- Use numbered format:
  1. ...
  2. ...
  3. ...

- Generate MANY questions (15–30 depending on paragraph size)

- Include different types:
  * One-word answer questions
  * Short answer questions
  * Long/descriptive questions
  * Analytical questions

- Questions must be meaningful and complete sentences
- Avoid repeating quiz questions
- Cover different perspectives of the paragraph

ONLY OUTPUT QUESTIONS (NO ANSWERS)

{text}
"""
                }
            ],
            temperature=0.8
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ ERROR:", e)
        return None