import re

def parse_qa(text):
    qa_list = []

    questions = re.findall(r"Q\d+:\s*(.*)", text)
    answers = re.findall(r"A\d+:\s*(.*)", text)

    for q, a in zip(questions, answers):
        qa_list.append((q.strip(), a.strip())) 

    return qa_list


def parse_questions(text):
    questions = re.findall(r"\d+\.\s*(.*)", text)
    return [q.strip() for q in questions]