import pandas as pd
import re
from collections import defaultdict
#here i have connected dataset to make the model train
df=pd.read_csv("dataset.csv",sep="|")
questions=df.question.tolist()
types=df.Qtype.tolist()
# print(questions[:3])
# print(types[:3])
def clean_text(sentence):
    sentence=sentence.lower()
    sentence=re.sub(r'[^a-zA-Z\s]','',sentence)
    return sentence

questions=[clean_text(x) for x in questions]
# print(questions[:3])

vocab = set()
for sent in questions:
    list1=sent.split()
    for x in list1:
        vocab.add(x)
vocab=list(vocab)

def sentenceToVector(sentence):
    words=sentence.split()
    vector=[]
    for word in vocab:
        if word in words:
            vector.append(1)
        else:
            vector.append(0)
    return vector

# print(sentenceToVector(questions[0]))

allVector=[]
for x in questions:
    vec=sentenceToVector(x)
    allVector.append(vec)

typedict=defaultdict(lambda:[0]*len(vocab))

for i in range(len(allVector)):
    typeof=types[i]
    vector=allVector[i]
    for j in range(len(vector)):
        typedict[typeof][j]+=vector[j]

# print(typedict.keys())
# print(typedict["fact"][:10])

def predict(sentence):
    sentence=clean_text(sentence)
    vector=sentenceToVector(sentence)
    scores={}
    for label in typedict:
        sc=0
        for j in range(len(vector)):
            if vector[j]==1:
                sc+=typedict[label][j]
        scores[label]=sc
    return max(scores,key=scores.get)
