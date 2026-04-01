import pandas as pd
from helper import clean_text,sentenceToVector


df=pd.read_csv("datasetForRegression.csv",sep="|")

questions=df.question.tolist()
scores=df.score.tolist()

questions=[clean_text(x) for x in questions]

vocab=set()
for sent in questions:
    for word in sent.split():
        vocab.add(word)
vocab=list(vocab)

X=[]
for sentence in questions:
    vec=sentenceToVector(sentence,vocab)
    X.append(vec)

weight=[0.0]*len(vocab)
bias=0.0

ttt=50
lr=0.1

for _ in range(ttt+1):
    for i in range(len(X)):
        pred=0
        for j in range(len(weight)):
            pred+=weight[j]*X[i][j]
        pred+=bias
        error=scores[i]-pred
        for j in range(len(weight)):
            if(X[i][j] == 1):
                weight[j]+=lr*error
        bias+=lr*error

def predictdiffno(sentence):
    sentence=clean_text(sentence)
    vec=sentenceToVector(sentence,vocab)
    pred=0
    for j in range(len(weight)):
        pred+=vec[j]*weight[j]
    pred+=bias

    pred=max(1,min(pred,10))
    return round(pred,2)

# print(predictdiffno("explain about cheif minister of tamilnadu"))