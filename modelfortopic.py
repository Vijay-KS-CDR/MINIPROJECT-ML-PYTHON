import math
import pandas as pd
from helper import clean_text,sentenceToVector
from collections import defaultdict

df=pd.read_csv("datasetfortopic.csv",sep="|")

questions=df.question.tolist()
topics=df.topic.tolist()
# print(questions[:3],topics[:3])

questions=[clean_text(x) for x in questions]
    
vocab=set()
for sentence in questions:
    list1=sentence.split()
    for s in list1:
        vocab.add(s)
vocab=list(vocab)

allvector=[]
for sentence in questions:
    vec=sentenceToVector(sentence,vocab)
    allvector.append(vec)

topicdict=defaultdict(lambda:[0]*len(vocab))
for i in range(len(allvector)):
    typeof=topics[i]
    vector=allvector[i]
    for j in range(len(vector)):
        topicdict[typeof][j]+=vector[j]


class_freq={}
for label in topics:
    class_freq[label]=class_freq.get(label,0)+1

total_samples=len(topics)

p_class={}
for label in class_freq:
    p_class[label]=     class_freq[label]/total_samples

#words per class
words_per_class={}
for label in topicdict:
    words_per_class[label]=sum(topicdict[label])

def predicttopic(sentence):
    sentence = clean_text(sentence)
    vec = sentenceToVector(sentence, vocab)
    scores = {}
    for label in topicdict:
        log_prob = math.log(p_class[label])
        for j in range(len(vec)):
            if vec[j] >= 1:
                word_count = topicdict[label][j]
                total_words = words_per_class[label]
                prob = (word_count + 1) / (total_words + len(vocab))
                log_prob += vec[j]*math.log(prob)
        scores[label] = log_prob
    return max(scores, key=scores.get) 