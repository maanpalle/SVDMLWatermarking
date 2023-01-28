import sklearn
import sklearn.datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn import metrics
import os

dataset = ["../data/Dry_Bean.txt", "../data/iris.txt"][0]

k = 0
if(dataset == "../data/Dry_Bean.txt"):
    k = 16
else:
    k = 4


def parse(file):
    x = []
    y = []
    j = 0
    for line in file.readlines():
        splitted = line.replace("\n", "").split(", ")
        y.append(float(splitted[k]))
        vector = []
        for i in range(k):
            vector.append(float(splitted[i]))
        x.append(vector)
        j += 1
    return [x, y]

def eval(x, y):

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, stratify=y, random_state=100)

    model = GaussianNB()

    model.fit(xtrain, ytrain)

    prediction = model.predict(xtest)
    accuracy = metrics.accuracy_score(y_true=ytest, y_pred=prediction)
    return accuracy

thresholds = []
accuracies = []

for i in range(300):
    thresholds.append(pow(i, 2) * 0.00001)

i = 0
for threshold in thresholds:
    print(i)
    if dataset == "../data/Dry_Bean.txt":
        os.system(f"./../wmEmb/emb 0 {threshold} 0")
    else:
        os.system(f"./../wmEmb/emb 0 {threshold} 1")
    wm_data = open("../data/wm.txt", "r")
    x, y = parse(wm_data)
    accuracies.append(eval(x, y))
    i += 1

host_data = open(dataset, "r")
x, y = parse(host_data)

plt.rc('font', size=18)
plt.scatter(thresholds, accuracies, c = 'red')
plt.title("BayesClassifier Accuracies")
plt.xlabel("thresholds", fontsize=18)
plt.ylabel("accuracy", fontsize=18)
plt.show()

