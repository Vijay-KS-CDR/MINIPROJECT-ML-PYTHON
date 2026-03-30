from groq import Groq
import re
import os
import pyttsx3
from dotenv import load_dotenv
import os


load_dotenv()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


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

STRICT RULES:
- Each question MUST be a full sentence
- Each question MUST start with What / Which / Who / Where
- DO NOT use single words as questions
- DO NOT output keywords like "Mosaic", "Location"
- Questions must be meaningful

- Answers MUST be exactly ONE WORD

GOOD EXAMPLE:
Q1: Which country is described as a mosaic of tradition and transformation?
A1: India

BAD EXAMPLE (DO NOT DO THIS):
Q1: Mosaic
A1: Diverse

Generate at least 8 questions.

Format STRICTLY:
Q1: question
A1: answer
{text}
"""
                }
            ],
            temperature=0.7
        )

        print("\n✅ AI Response Received!\n")
        return response.choices[0].message.content

    except Exception as e:
        print("\n❌ ERROR:\n", e)
        return None


# 🔹 Parse Q&A
def parse_qa(text):
    qa_list = []

    questions = re.findall(r"Q\d+:\s*(.*)", text)
    answers = re.findall(r"A\d+:\s*(.*)", text)

    for q, a in zip(questions, answers):
        qa_list.append((q.strip(), a.strip()))

    return qa_list


# 🔹 Quiz system
def run_quiz(qa_list):
    score = 0
    total = len(qa_list)

    for i, (q, a) in enumerate(qa_list, start=1):
        question_text = f"Question {i}. {q}"

        print(f"\nQuestion {i}/{total}: {q}")

        # 🔊 SPEAK QUESTION
        speak(question_text)

        user = input("Your answer: ").strip().lower()
        correct = a.strip().lower()

        if user == correct:
            print("Correct ✅")
            speak("Correct")
            score += 1
        else:
            print("Wrong ❌")
            print("Correct Answer:", correct)
            speak(f"Wrong. The correct answer is {correct}")

        print(f"Score: {score}/{i}")

    print("\n🎯 FINAL RESULT")
    print(f"Score: {score}/{total}")
    speak(f"Quiz completed. Your score is {score} out of {total}")


# 🔹 Main
def main():
    text = input("Enter paragraph:\n")

    print("\n🚀 Generating questions get ready...\n")
    output = generate_ai_questions(text)

    if not output:
        print("❌ Failed to generate questions.")
        return

    

    qa_list = parse_qa(output)

    if not qa_list:
        print("❌ Failed to parse Q&A.")
        return

    print("\n--- QUIZ START ---")
    run_quiz(qa_list)


if __name__ == "__main__":
    main()