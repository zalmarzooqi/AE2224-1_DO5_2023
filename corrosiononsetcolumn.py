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

sigcollst = []

for i in range(len(arrays)):
    totalpix = arrays[i][0, 3:arrays[i].shape[1]].sum()
    for j in range(3,arrays[i].shape[1]):
        if arrays[i][0,j] > 0:
            sigcol = j 
            sigcollst.append(sigcol)
            #print('Total number of pixels =', totalpix, '1st Column w/ pixels =', j)
            break

#rows = files, columns = timesteps, values = percentages of corrosion
matrixsize = (len(arrays), arrays[0].shape[0])
matrixpercentabs = np.zeros(matrixsize)
matrixpercentrel = np.zeros(matrixsize)

for i in range(len(arrays)):
    totalpix = arrays[i][0, 3:arrays[i].shape[1]].sum()
    for j in range(arrays[i].shape[0]):
        corpixels = arrays[i][j, 3:sigcollst[i]].sum()
        corpercent = corpixels / totalpix * 100
        matrixpercentabs[i,j] = corpercent
        if j == 0:
            matrixpercentrel[i,j] = corpercent
        else:
            matrixpercentrel[i,j] = corpercent - matrixpercentabs[i,j-1]

#np.set_printoptions(threshold=sys.maxsize)           
#print(matrixpercentrel[0])
#print(matrixpercentabs[0])

timesteps_unin = np.zeros(arrays[0].shape[0])

for i in range(arrays[0].shape[0]):
    timesteps_unin[i] = arrays[0][i, 1]

#filenames
file_list = []
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        name = os.path.splitext(file_name)[0]
        file_list.append(name)


for i in range(len(arrays)):
    plt.plot(timesteps_unin, matrixpercentabs[i])
    plt.xlabel('time [s]')
    plt.ylabel('Percetage [%]')
    plt.ylim(0,110)
    plt.savefig(f'unin_abs_corr_to_time_10800/plot_{file_list[i]}.png')
    plt.clf()

for i in range(len(arrays)):
    plt.plot(timesteps_unin, matrixpercentabs[i])
    plt.xlabel('time [s]')
    plt.ylabel('Percetage [%]')
plt.savefig('unin_abs_corr_to_time_10800/plot_all.png')







        




    




