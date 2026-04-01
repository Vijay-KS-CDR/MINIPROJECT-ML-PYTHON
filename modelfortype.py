import pandas as pd
from collections import defaultdict
from helper import clean_text,sentenceToVector
#here i have connected dataset to make the model train
df=pd.read_csv("datasetfortype.csv",sep="|")
questions=df.question.tolist()
types=df.Qtype.tolist()
import math

questions=[clean_text(x) for x in questions]
# print(questions[:3])

vocab = set()
for sent in questions:
    list1=sent.split()
    for x in list1:
        vocab.add(x)
vocab=list(vocab)



allVector=[]
for x in questions:
    vec=sentenceToVector(x,vocab)
    allVector.append(vec)

typedict=defaultdict(lambda:[0]*len(vocab))

for i in range(len(allVector)):
    typeof=types[i]
    vector=allVector[i]
    for j in range(len(vector)):
        typedict[typeof][j]+=vector[j]

# print(typedict.keys())
# print(typedict["fact"][:10])

class_freq={}
for label in types:
    class_freq[label]=class_freq.get(label,0)+1

total_samples=len(types)

p_class={}
for label in class_freq:
    p_class[label]=     class_freq[label]/total_samples

#words per class
words_per_class={}
for label in typedict:
    words_per_class[label]=sum(typedict[label])


def predict(sentence):
    sentence=clean_text(sentence)
    vector=sentenceToVector(sentence,vocab)
    scores={}
    for label in typedict:
        log_prob = math.log(p_class[label])
        for j in range(len(vector)):
            if vector[j]>=1:
                word_count = typedict[label][j]
                total_words = words_per_class[label]
                prob = (word_count + 1) / (total_words + len(vocab))
                log_prob += vector[j]*math.log(prob)
        scores[label] =log_prob
    best = max(scores, key=scores.get)
    exp_scores = {}
    for label in scores:
        exp_scores[label] = math.exp(scores[label])
    total = sum(exp_scores.values())
    confidence = exp_scores[best] / total
    return best, confidence * 100
