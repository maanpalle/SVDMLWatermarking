import matplotlib.pyplot as plt
import os 
import numpy as np
import math


def mse(threshold):
    os.system('./../wmEmb/emb 0 ' + str(threshold) + " 1")

    wm_data_file = open("../data/wm.txt", "r")
    data_file = open("../data/iris.txt", "r")

    wm_data = []
    data = []
    for line in wm_data_file.readlines():
        splitted = line.replace("\n", "").split(", ")
        wm_data.append(float(splitted[1]))

    for line in data_file.readlines():
        splitted = line.replace("\n", "").split(", ")
        data.append(float(splitted[1]))
    mn = len(data) 
    
    MSE = 0
    for i in range(mn):
        MSE = MSE + pow(data[i] - wm_data[i], 2) 

    MSE = MSE / mn

    return MSE

thresholds = []

for i in range(300):
    thresholds.append(pow(i, 2) * 0.00001)

MSEs = []
for i in range(len(thresholds)):
    print(i)
    MSEs.append(mse(thresholds[i]))

plt.rc('font', size=18)
plt.scatter(thresholds, MSEs, c = 'red')
plt.title("Mean Squared Errors")
plt.xlabel("thresholds")
plt.ylabel("Mean Squared Errors")
plt.show()

