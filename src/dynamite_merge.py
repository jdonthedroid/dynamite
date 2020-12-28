import os
import sys
import glob
import numpy as np
from dynamite import dynamite

for i in range(len(glob.glob1(".","saved_data_*.npz"))):
    with np.load("saved_data_" + str(i+1) + ".npz", allow_pickle=True) as data:
        if i == 0:
            data1 = data["data"]

        else:
            for j in range(len(data["data"])):
                if isinstance(data1[j], list):
                    if isinstance(data["data"][j], list):
                        data1[j] = data1[j] + data["data"][j]

                    else:
                        data1[j].append(data["data"][j])

                elif isinstance(data1[j], np.ndarray):
                    np.append(data1[j], data["data"][j])

                else:
                    data1[j] = [data1[j], data["data"][j]]

if 'data1' in locals():
    np.savez("saved_data.npz", data=data1)
    dynamite(merged_data=data1)

    for i in range(len(glob.glob1(".","saved_data_*.npz"))):
        os.remove("saved_data_" + str(i+1) + ".npz")
