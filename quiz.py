from voice import speak
from model import predict
def run_quiz(qa_list):
    score = 0
    total = len(qa_list)
    
    speak("Let's start the quiz")

    for i, (q, a) in enumerate(qa_list, start=1):
        q_type=predict(q)
        print(f"\nQuestion {i}/{total}: {q}")
        speak(f"Question {i}. {q}")
        
        print(f"Type: {q_type}")
        speak(f"This is a {q_type} question.")


        user = input("Your answer: ").strip().lower()
        correct = a.lower()

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
    speak(f"Your score is {score} out of {total}")