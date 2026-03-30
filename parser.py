import re

def parse_qa(text):
    qa_list = []

    questions = re.findall(r"Q\d+:\s*(.*)", text)
    answers = re.findall(r"A\d+:\s*(.*)", text)

    for q, a in zip(questions, answers):
        a = a.split()[0]  # force one-word answer
        qa_list.append((q.strip(), a.strip()))

    return qa_list