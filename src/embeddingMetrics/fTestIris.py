import matplotlib.pyplot as plt
import numpy as np
import os
import math

def ftest(threshold):
    os.system('./../wmSvd/svd 0 ' + str(threshold))

    wm_data_file = open("../data/wm.txt", "r")
    data_file = open("../data/iris.txt", "r")

    wm_data = []
    data = []
    for line in wm_data_file.readlines():
        splitted = line.replace("\n", "").split(", ")
        wm_data.append(float(splitted[15]))

    for line in data_file.readlines():
        splitted = line.replace("\n", "").split(", ")
        data.append(float(splitted[15]))
    
    wm_data = np.array(wm_data)
    data = np.array(data)

    return np.var(data) / np.var(wm_data)

    
thresholds = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]
thresholds = []

for i in range(300):
    thresholds.append(pow(i, 2) * 0.00001)

FTests = []
for i in range(len(thresholds)):
    print(i)
    FTests.append(ftest(thresholds[i]))

print(FTests)
plt.rc('font', size=15)
plt.rc('axes', titlesize=15)
plt.scatter(thresholds, FTests, c = 'red')
plt.title("F-test")
plt.xlabel("thresholds")
plt.ylabel("F-test results")
plt.show()

