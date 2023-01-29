import os

def parse_wm():
    wm_file = open("../data/wm_image.txt")
    wm = []
    while True:
        wm_bit = wm_file.read(1)
        if not wm_bit == "":
            if not wm_bit == "\n":
                wm.append(int(wm_bit))
        else:
            break
    return wm

def parse_data(file):
    x = []
    for line in file.readlines():
        splitted = line.replace("\n", "").split(", ")
        vector = []
        for att in splitted:
            vector.append(float(att))
        x.append(vector)
    return x

def MSE(x, y):
    mse = 0
    for i in range(len(x)):
        mse += (x[i] - y[i])**2
    return mse

def write_data(x):
    file = open("../data/wm.txt", "w")
    for vector in x:
        for i in range(len(vector) - 1):
           file.write(str(vector[i]) + ", ")
        file.write(str(vector[len(vector) - 1]) + "\n")

def extract_wm(max, wm_index):
    os.system(f"./../wmExtr/extr {max} {wm_index}")
    return parse_wm()



# dataset is a number [0, 1] 0 referring to the dry-bean dataset 1 to the iris one.
def watermark_data(dataset, threshold):
    os.system(f"./../wmEmb/emb 0 {threshold} {dataset}")

    return parse_data(open("../data/wm.txt"))

