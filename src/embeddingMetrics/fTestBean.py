import matplotlib.pyplot as plt
import numpy as np
import os
import math

def ftest(threshold):
    os.system('./../wmEmb/emb 0 ' + str(threshold) + " 0")

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
    
    wm_data = np.array(wm_data)
    data = np.array(data)

    return np.var(data) / np.var(wm_data)

    
thresholds = []

for i in range(300):
    thresholds.append(pow(i, 2) * 0.00001)

FTests = []
for i in range(len(thresholds)):
    print(i)
    FTests.append(ftest(thresholds[i]))

plt.rc('font', size=18)
plt.scatter(thresholds, FTests, c = 'red')
plt.title("F-test")
plt.xlabel("thresholds", fontsize=18)
plt.ylabel("F-test results", fontsize=18)
plt.show()

