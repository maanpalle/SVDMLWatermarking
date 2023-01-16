import matplotlib.pyplot as plt
import os 
import numpy as np
import math


def mse(threshold):
    os.system('./../wmSvd/svd 0 ' + str(threshold))

    wm_data_file = open("../data/wm.txt", "r")
    data_file = open("../data/Dry_Bean.txt", "r")

    wm_data = []
    data = []
    for line in wm_data_file.readlines():
        splitted = line.replace("\n", "").split(", ")
        wm_data.append(float(splitted[15]))

    for line in data_file.readlines():
        splitted = line.replace("\n", "").split(", ")
        data.append(float(splitted[15]))
    mn = len(data) 
    
    MSE = 0
    for i in range(mn):
        MSE = MSE + pow(data[i] - wm_data[i], 2) 

    MSE = MSE / mn

    return MSE

thresholds = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]
thresholds = []

for i in range(300):
    thresholds.append(pow(i, 2) * 0.00001)

MSEs = []
for i in range(len(thresholds)):
    print(i)
    MSEs.append(mse(thresholds[i]))

plt.scatter(thresholds, MSEs, c = 'red')
plt.title("Mean Squared Errors")
plt.xlabel("thresholds")
plt.ylabel("Mean Squared Errors")
plt.show()

