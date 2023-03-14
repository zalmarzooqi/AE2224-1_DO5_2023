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
    df = pd.read_csv(file, header = None)
    data_frames.append(df)
    
#convert each DataFrame to a NumPy array by using the values attribute.
arrays = []

for df in data_frames:
    arr = df.values
    arrays.append(arr)


#print(arrays[0].shape[1])
for i in range(len(arrays)):
    for j in range(3,arrays[i].shape[1]):
        if arrays[i][0,j] >0: 
        
            print(j)
            break

