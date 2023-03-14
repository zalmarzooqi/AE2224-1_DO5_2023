import pandas as pd
import glob
import os

#use the glob module to get a list of all CSV files in the folder.
folder_path = 'Immersion Uninhibited/LocalAnalysis_Margin=004px_time=10800/1_LocalImgAnal_Num'
folder_path = os.path.abspath(folder_path)
csv_files = glob.glob(folder_path + '/*.csv')

#read each CSV file and store its data in a Pandas DataFrame object.
data_frames = []

for file in csv_files:
    df = pd.read_csv(file)
    data_frames.append(df)
    
#convert each DataFrame to a NumPy array by using the values attribute.
arrays = []

for df in data_frames:
    arr = df.values
    arrays.append(arr)

#138 csv files in Unhinhibited, so len(arrays) = 138
#for arridx in range(len(arrays)):

for row in arrays[0]:
    for i in range(3,len(row)):
        if row[i] > 0:
            cocol = row[i-1]
            #print(cocol, i-1)
            break
    break


for j in range(arrays[0].shape[1]):
    if arrays[0][0,j] > 0:
        print(j)
            



