import matplotlib.pyplot as plt
import numpy as np
import os

threshold = 0.002

os.system('./../wmSvd/svd 0 ' + str(threshold))

wm_data_file = open("../data/wm.txt", "r")
data_file = open("../data/Dry_Bean.txt", "r")

wm_data = []
data = []

wm_data_0 = []
wm_data_1 = []
wm_data_2 = []
wm_data_3 = []
wm_data_4 = []
wm_data_5 = []
wm_data_6 = []

data_0 = []
data_1 = []
data_2 = []
data_3 = []
data_4 = []
data_5 = []
data_6 = []

for line in wm_data_file.readlines():
    splitted = line.replace("\n", "").split(", ")
    wm_data.append(splitted)
    
    classification = int(float(splitted[len(splitted) - 1]))
    if(classification == 0):
        wm_data_0.append(float(splitted[15]))
    if(classification == 1):
        wm_data_1.append(float(splitted[15]))
    if(classification == 2):
        wm_data_2.append(float(splitted[15]))
    if(classification == 3):
        wm_data_3.append(float(splitted[15]))
    if(classification == 4):
        wm_data_4.append(float(splitted[15]))
    if(classification == 5):
        wm_data_5.append(float(splitted[15]))
    if(classification == 6):
        wm_data_6.append(float(splitted[15]))

for line in data_file.readlines():
    splitted = line.replace("\n", "").split(", ")
    data.append(splitted)

    classification = int(float(splitted[len(splitted) - 1]))
    if(classification == 0):
        data_0.append(float(splitted[15]))
    if(classification == 1):
        data_1.append(float(splitted[15]))
    if(classification == 2):
        data_2.append(float(splitted[15]))
    if(classification == 3):
        data_3.append(float(splitted[15]))
    if(classification == 4):
        data_4.append(float(splitted[15]))
    if(classification == 5):
        data_5.append(float(splitted[15]))
    if(classification == 6):
        data_6.append(float(splitted[15]))

fig, ax = plt.subplots(1, 2)

wm_data_0.sort()
wm_data_1.sort()
wm_data_2.sort()
wm_data_3.sort()
wm_data_4.sort()
wm_data_5.sort()
wm_data_6.sort()

data_0.sort()
data_1.sort()
data_2.sort()
data_3.sort()
data_4.sort()
data_5.sort()
data_6.sort()

s = 3

ax[1].scatter(range(len(wm_data_0)), wm_data_0, c = "red", s=s)
ax[1].scatter(range(len(wm_data_1)), wm_data_1, c = "blue", s=s)
ax[1].scatter(range(len(wm_data_2)), wm_data_2, c = "green", s=s)
ax[1].scatter(range(len(wm_data_3)), wm_data_3, c = "black", s=s)
ax[1].scatter(range(len(wm_data_4)), wm_data_4, c = "yellow", s=s)
ax[1].scatter(range(len(wm_data_5)), wm_data_5, c = "orange", s=s)
ax[1].scatter(range(len(wm_data_6)), wm_data_6, c = "purple", s=s)
ax[1].legend(("Seker", "Barbunya", "Bombay", "Cali", "Horoz", "Sira", "Dermason"))
ax[1].set_title("Watermarked data with threshold = " + str(threshold))
ax[1].set_xlabel("n")
ax[1].set_ylabel("ShapeFactor4")

ax[0].scatter(range(len(data_0)), data_0, c = "red", s=s)
ax[0].scatter(range(len(data_1)), data_1, c = "blue", s=s)
ax[0].scatter(range(len(data_2)), data_2, c = "green", s=s)
ax[0].scatter(range(len(data_3)), data_3, c = "black", s=s)
ax[0].scatter(range(len(data_4)), data_4, c = "yellow", s=s)
ax[0].scatter(range(len(data_5)), data_5, c = "orange", s=s)
ax[0].scatter(range(len(data_6)), data_6, c = "purple", s=s)
ax[0].legend(("Seker", "Barbunya", "Bombay", "Cali", "Horoz", "Sira", "Dermason"))
ax[0].set_title("Host data")
ax[0].set_xlabel("n")
ax[0].set_ylabel("ShapeFactor4")



plt.show()






