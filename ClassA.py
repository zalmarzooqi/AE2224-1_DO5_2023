#from corrosiononsetcolumn import arrays, timesteps_unin, matrixpercentabs, file_list
import numpy as np

# unin = Uninhibited
# r = row, c = column
#46 files in Secondary unin, 35 files in S unin, 15 files in theta unin
#1567 timesteps counting from 1
#timestep 941 from 1 = 4000 s
#timestep 741 from 1 = 4000 s

def matrix(len,param):
    matrixsize = (len,param) #len is the number of useful files, param is the number of size and geometry parameters
    matrix = np.zeros(matrixsize)
    return matrix

#for the unin Secondary-phase particles we only look at Class A particles (>= 60% corroded in 4000 s) to isolate the composition variable
def ClassAsec(arrays, matrixpercentabs):
    checkarray = [] 
    for i in range(len(arrays)):
        #for c in range(len(timesteps_unin)):
        if matrixpercentabs[i,940] >= 60:
            checkarray.append(1) #1 means Class A
        else:
            checkarray.append(0) #0 means not Class A
    return checkarray

#for the unin theta-phase particles we only look at Class A particles (>= 60% corroded in 2000 s) to isolate the composition variable
def ClassAthe(arrays, matrixpercentabs):
    checkarray = [] 
    for i in range(len(arrays)):
        #for c in range(len(timesteps_unin)):
        if matrixpercentabs[i,740] >= 60:
            checkarray.append(1) #1 means Class A
        else:
            checkarray.append(0) #0 means not Class A
    return checkarray





            




            
            
            

        

