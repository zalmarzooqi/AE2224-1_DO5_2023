import pandas as pd
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import sys

#use the glob module to get a list of all CSV files in the folder.
folder_path = 'Immersion Uninhibited/LocalAnalysis_Margin=004px_time=10800/1_LocalImgAnal_Num'
folder_path = os.path.abspath(folder_path)
csv_files = glob.glob(folder_path + '/*.csv')

#read each CSV file and store its data in a Pandas DataFrame object.
data_frames = []

for file in csv_files:
    df = pd.read_csv(file, header = None)
    data_frames.append(df)
    
#convert each DataFrame to a NumPy array by using the values attribute.
arrays = []

for df in data_frames:
    arr = df.values
    arrays.append(arr)

matrixsize = (arrays[0].shape[0]-1, arrays[0].shape[1]-2)
changearray = np.zeros(matrixsize)
#print(matrixsize, changearray)

for row in range(arrays[0].shape[0]):
    if row < 1566:
        changerow = arrays[0][row+1, 2:arrays[0].shape[1]] - arrays[0][row, 2:arrays[0].shape[1]]
        changearray[row,:] = changerow

positivearray = np.where(changearray > 0, changearray, 0)
np.set_printoptions(threshold=sys.maxsize) 
print(positivearray[0])

rowsums = np.sum(positivearray, axis = 1)

print(rowsums)
    
    