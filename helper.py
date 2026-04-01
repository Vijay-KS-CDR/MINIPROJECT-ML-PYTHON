import re

def clean_text(sentence):
    sentence=sentence.lower()
    sentence=re.sub(r'[^a-zA-Z\s]','',sentence)
    stopwords = {
        "is","the","of","and","in","to","a","an","for","on","with","as"
    }
    words=sentence.split()
    sent=[w for w in words if w not in stopwords]
    return " ".join(sent)
# print(questions[:3])
# print(types[:3])

def sentenceToVector(sentence,vocab):
    words=sentence.split()
    vector=[]
    for word in vocab:
        vector.append(words.count(word)) 
    return vector
# print(sentenceToVector(questions[0]))