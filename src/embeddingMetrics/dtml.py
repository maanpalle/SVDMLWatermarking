import sklearn
import sklearn.datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn import metrics
import os

k = 4
#k = 16

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

    model = DecisionTreeClassifier(max_depth=10, random_state=100)

    model.fit(xtrain, ytrain)

    prediction = model.predict(xtest)
    accuracy = metrics.accuracy_score(y_true=ytest, y_pred=prediction)
    return accuracy




thresholds = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]
thresholds = []
accuracies = []

for i in range(300):
    thresholds.append(pow(i, 2) * 0.00001)

i = 0
for threshold in thresholds:
    print(i)
    os.system(f"./../wmSvd/svd 0 {threshold} 1")
    wm_data = open("../data/wm.txt", "r")
    x, y = parse(wm_data)
    accuracies.append(eval(x, y))
    i += 1

host_data = open("../data/iris.txt", "r")
#host_data = open("../data/Dry_Bean.txt", "r")
x, y = parse(host_data)
print(eval(x, y))

plt.scatter(thresholds, accuracies, c = 'red')
plt.title("DescisionTreeClassifier Accuracies")
plt.xlabel("thresholds")
plt.ylabel("accuracy")
plt.show()




