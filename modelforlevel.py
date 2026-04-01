import math
import pandas as pd
from helper import clean_text,sentenceToVector
from collections import defaultdict
df=pd.read_csv("datasetforlevel.csv",sep="|")
questions=df.question.tolist()
level=df["level"].tolist()

#print(questions.head(),level.head())

#print(level(questions)) 

questions=[clean_text(x) for x in questions]

#print(level (questions))

vocab = set()
for q in questions:
    list1=q.split()
    for word in list1:
        vocab.add(word)
vocab=list(vocab)

allvector=[]
for s in questions:
    vec=sentenceToVector(s,vocab)
    allvector.append(vec)

leveldict=defaultdict(lambda:[0]*len(vocab))
for i in range(len(allvector)):
    levelof=level[i]
    vector=allvector[i]
    for j in range(len(vector)):
        leveldict[levelof][j]+=vector[j]



class_freq={}
for label in level:
    class_freq[label]=class_freq.get(label,0)+1

total_samples=len(level)

p_class={}
for label in class_freq:
    p_class[label]=     class_freq[label]/total_samples

#words per class
words_per_class={}
for label in leveldict:
    words_per_class[label]=sum(leveldict[label])


def predictlevel(sentence):
    sentence = clean_text(sentence)
    vec = sentenceToVector(sentence, vocab)
    scores = {}
    for label in leveldict:
        log_prob = math.log(p_class[label])
        for j in range(len(vec)):
            if vec[j] >= 1:
                word_count = leveldict[label][j]
                total_words = words_per_class[label]
                prob = (word_count + 1) / (total_words + len(vocab))
                log_prob += vec[j]*math.log(prob)
        scores[label] = log_prob
    return max(scores, key=scores.get)           