import pandas as pd
import glob
import os
import numpy as np
import matplotlib as plt

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

percent = 50 #%

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
matrixpercent = np.zeros(matrixsize)

for i in range(len(arrays)):
    totalpix = arrays[i][0, 3:arrays[i].shape[1]].sum()
    for j in range(arrays[i].shape[0]):
        corpixels = arrays[i][j, 3:sigcollst[i]].sum()
        corpercent = corpixels / totalpix * 100
        if j == 0:
            matrixpercent[i,j] = corpercent
        else:
            matrixpercent[i,j] = corpercent - matrixpercent[i,j-1]
            
print(matrixpercent)






        




    




