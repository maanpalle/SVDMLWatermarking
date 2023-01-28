import sklearn
import sklearn.datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics
import os

dataset = ["../data/Dry_Bean.txt", "../data/iris.txt"][0]

k = 0
dim = 0
watermarked = 0
if(dataset == "../data/Dry_Bean.txt"):
    k = 7
    dim = 16
    watermarked = 15
else:
    k = 3
    dim = 4
    watermarked = 1



def get_distance(x, y):
    dis = 0
    for j in range(len(x)):
        dis += (x[j] - y[j])**2
    return dis**(1/2) 

def parse(file):
    x = []
    y = []
    j = 0
    for line in file.readlines():
        splitted = line.replace("\n", "").split(", ")
        y.append(float(splitted[dim]))
        vector = []
        for i in range(dim):
            vector.append(float(splitted[i]))
        x.append(vector)
        j += 1
    return [x, y]

def get_original_centroids(x, y):
    model = KMeans(n_clusters=k, random_state=0, n_init="auto")

    centroids = model.fit(x).cluster_centers_

    return centroids[:, watermarked]

def eval(x, y):
    model = KMeans(n_clusters=k, random_state=0, n_init="auto")

    centroids = model.fit(x).cluster_centers_

    return centroids[:, watermarked]

thresholds = []
errors = []

for i in range(300):
    thresholds.append(pow(i, 2) * 0.00001)

host_data = open(dataset, "r")
x_or, y_or = parse(host_data)
host_centroids = get_original_centroids(x_or, y_or)

i = 0
for threshold in thresholds:
    print(i)
    if dataset == "../data/Dry_Bean.txt":
        os.system(f"./../wmEmb/emb 0 {threshold} 0")
    else:
        os.system(f"./../wmEmb/emb 0 {threshold} 1")
    wm_data = open("../data/wm.txt", "r")
    x, y = parse(wm_data)
    errors.append(get_distance(eval(x, y), host_centroids))
    i += 1

plt.rc('font', size=18)
plt.scatter(thresholds, errors, c='red')
plt.title("KMeans centroids Euclidian distance")
plt.xlabel("thresholds", fontsize=18)
plt.ylabel("Errors", fontsize=18)
plt.show()

