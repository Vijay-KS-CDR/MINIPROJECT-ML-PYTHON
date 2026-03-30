from ai_generation import generate_ai_questions
from parser import parse_qa
from quiz import run_quiz

def main():
    text = input("Enter paragraph:\n")

    print("\n🚀 Generating questions...\n")
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