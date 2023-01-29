from UpdateAttack import updateAttack
from DeleteAttack import deleteAttack 
from ZeroOutAttack import zeroOutAttack
from InstertAttack import insertionAttack
from MultiFacedAttack import multiFacedAttack 
from lib import parse_wm, parse_data, write_data, extract_wm, MSE 

import os
import matplotlib.pyplot as plt
import numpy as np

# Change the dataset used (0: Dry-Bean, 1: Iris)
dataset = 0
# Change the attack used by changing the array index
attack = [updateAttack, deleteAttack, zeroOutAttack, insertionAttack, multiFacedAttack][4]

file = [open("../data/Dry_Bean.txt", "r"), open("../data/iris.txt", "r")][dataset]
info = [[0.999733, 15], [4.4, 1]][dataset]


original_wm = parse_wm()

if (attack == updateAttack):
    percentages = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
else:
    percentages = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]

watermarks = []

for percentage in percentages:
    print(percentage)
    os.system(f'./../wmEmb/emb 0 0.05, {dataset}')
    x = parse_data(open("../data/wm.txt", "r"))
    y = attack(x, percentage)
    write_data(y)
    new_wm = extract_wm(info[0], info[1])
    
    watermarks.append(np.array(new_wm).reshape([int(len(new_wm) ** (1/2)), int(len(new_wm) ** (1/2))]))

fig, ax = plt.subplots(1, 11)
ax[0].set_title(f'\n{attack.__name__}: \n{percentages[0]}')
for i in range(len(watermarks)):
    ax[i].imshow(watermarks[i],  cmap=plt.cm.gray, interpolation="none")
    ax[i].set_xticklabels([""]*watermarks[i].shape[0])
    ax[i].set_yticklabels([""]*watermarks[i].shape[1])
    if not i == 0: ax[i].set_title(f'{percentages[i]}')

plt.show()




    

    
