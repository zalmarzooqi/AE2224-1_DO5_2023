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


#timesteps
timesteps_unin = np.zeros(arrays[0].shape[0])
for i in range(arrays[0].shape[0]):
    timesteps_unin[i] = arrays[0][i, 1]

#sum matrix
matrixsize1 = (len(arrays),arrays[0].shape[0])
sum  = np.zeros(matrixsize1)

#changed matrix
matrixsize = (arrays[0].shape[0]-1, arrays[0].shape[1]-2)
changearray = np.zeros(matrixsize)
#print(matrixsize, changearray)

#for the 1567 timesteps in each file
for i in range(len(arrays)):
    for row in range(arrays[i].shape[0]):
        if row < 1566:
            #substract the ith+1 - ith row
            changerow = arrays[i][row+1, 2:arrays[i].shape[1]] - arrays[i][row, 2:arrays[i].shape[1]]
            changearray[row,:] = changerow

    #only take the positive values from the substracted arrays
    positivearray = np.where(changearray > 0, changearray, 0)

    #for rows in the postivearray
    for j in range(positivearray.shape[0]):
        sumpositives = np.sum(positivearray[j]) + sum[i,j]
        sum[i,j+1] = sumpositives

file_list = []
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        name = os.path.splitext(file_name)[0]
        file_list.append(name)

for i in range(len(arrays)):
    plt.plot(timesteps_unin, sum[i])
    plt.xlabel('time [s]')
    plt.ylabel('Number of changed pixels')
    #plt.ylim(0,110)
    plt.savefig(f'unin_delta_cumm_to_time_10800/cummulativechange_{file_list[i]}.png')
    plt.clf()

for i in range(len(arrays)):
    plt.plot(timesteps_unin, sum[i])
    plt.xlabel('time [s]')
    plt.ylabel('Number of changed pixels')
plt.savefig('unin_delta_cumm_to_time_10800/cummulativechange_all.png')

#np.set_printoptions(threshold=sys.maxsize) 






    





    



