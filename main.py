from ai_generation import generate_ai_questions, generate_more_questions
from parser import parse_qa, parse_questions
from quiz import run_quiz

def main():
    text = input("Enter paragraph:\n")

    # 🔹 Phase 1: Quiz Generation
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

    # 🔹 Phase 2: More Questions + ML Analysis
    print("\n🧠 Generating more questions for analysis...\n")
    more_output = generate_more_questions(text)

    if not more_output:
        print("❌ Failed to generate additional questions.")
        return

    questions = parse_questions(more_output)

    if not questions:
        print("❌ Failed to parse questions.")
        return

    print("\n--- QUESTION ANALYSIS ---")

    from modelfortype import predict
    from modelfortopic import predicttopic
    from modelforlevel import predictlevel
    from regressionModel import predictdiffno

    for i, q in enumerate(questions, start=1):
        q_type,conf = predict(q)
        q_topic = predicttopic(q)
        q_level = predictlevel(q)
        q_diff = predictdiffno(q)

        print(f"\nQ{i}: {q}")
        print(f"Type: {q_type} ({conf:.2f}%)")
        print(f"Topic: {q_topic}")
        print(f"Level: {q_level}")
        print(f"Difficulty: {q_diff}/10")


if __name__ == "__main__":
    main()