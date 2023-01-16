import matplotlib.pyplot as plt
import numpy as np
import os

threshold = 0.02

os.system('./../wmSvd/svd 0 ' + str(threshold))

wm_data_file = open("../data/wm.txt", "r")
data_file = open("../data/iris.txt", "r")

wm_data = []
data = []

wm_data_0_0 = []
wm_data_0_1 = []
wm_data_1_0 = []
wm_data_1_1 = []
wm_data_2_0 = []
wm_data_2_1 = []

data_0_0 = []
data_0_1 = []
data_1_0 = []
data_1_1 = []
data_2_0 = []
data_2_1 = []


for line in wm_data_file.readlines():
    splitted = line.replace("\n", "").split(", ")
    wm_data.append(splitted)
    
    classification = int(float(splitted[len(splitted) - 1]))
    if(classification == 0):
        wm_data_0_0.append(float(splitted[0]))
        wm_data_0_1.append(float(splitted[1]))
    if(classification == 1):
        wm_data_1_0.append(float(splitted[0]))
        wm_data_1_1.append(float(splitted[1]))
    if(classification == 2):
        wm_data_2_0.append(float(splitted[0]))
        wm_data_2_1.append(float(splitted[1]))

for line in data_file.readlines():
    splitted = line.replace("\n", "").split(", ")
    data.append(splitted)

    classification = int(float(splitted[len(splitted) - 1]))
    if(classification == 0):
        data_0_0.append(float(splitted[0]))
        data_0_1.append(float(splitted[1]))
    if(classification == 1):
        data_1_0.append(float(splitted[0]))
        data_1_1.append(float(splitted[1]))
    if(classification == 2):
        data_2_0.append(float(splitted[0]))
        data_2_1.append(float(splitted[1]))


fig, ax = plt.subplots(1, 2)

wm_data_0_1.sort()
wm_data_1_1.sort()
wm_data_2_1.sort()
data_0_1.sort()
data_1_1.sort()
data_2_1.sort()

ax[1].scatter(range(len(wm_data_0_1)), wm_data_0_1, c = "red")
ax[1].scatter(range(len(wm_data_1_1)), wm_data_1_1, c = "blue")
ax[1].scatter(range(len(wm_data_2_1)), wm_data_2_1, c = "green")
ax[1].legend(("Iris-setosa", "Iris-versicolor", "Iris-virginica"))
ax[1].set_title("Watermarked data with threshold = " + str(threshold))
ax[1].set_xlabel("n")
ax[1].set_ylabel("sepal width in cm")

ax[0].scatter(range(len(data_0_1)), data_0_1, c = "red")
ax[0].scatter(range(len(data_1_1)), data_1_1, c = "blue")
ax[0].scatter(range(len(data_2_1)), data_2_1, c = "green")
ax[0].legend(("Iris-setosa", "Iris-versicolor", "Iris-virginica"))
ax[0].set_title("Host data")
ax[0].set_xlabel("n")
ax[0].set_ylabel("sepal width in cm")



plt.show()


