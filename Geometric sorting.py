import pandas as pd
import matplotlib as plt
from scipy.interpolate import interp1d
from scipy.misc import derivative
import os
import copy

p = ['D:', '\Tudelft', '2nd year', 'Project', 'Q3', 'Sorted Data', 'Output'] # List of parts from yout path (instead of a "/", another part is added)

case_list = ['Sorted_ParticleGeomCompo_inhb_del.xlsx', 'Sorted_ParticleGeomCompo_inhb.xlsx', 'Sorted_ParticleGeomCompo_reim_uninhb.xlsx', 'Sorted_ParticleGeomCompo_uninhb.xlsx'] #Files where the information is stored
type_list = ['ROI', 'Area', 'Circ.', 'Feret', 'AR', 'Solidity'] #Information that will be extracted
comp_list = ['S-phase', 'Theta', 'Secondary'] #Initial seperation


value_list = [] #empty list, in which everything will be collected
typelist = copy.deepcopy(type_list) #Copy for later, don't worry about it

for i in range(len(case_list)): #To analyze each case
    path = os.path.join(*p, case_list[i]) #To get the correct path
    #print(path)
    data = pd.read_excel(path, sheet_name='Geometry Filtered') #Read the data in the file
    value_list.append([]) #Make another empty list in the list
    for l in range(len(comp_list)): #For each phase
        value_list[i].append([]) #Add another list inside the list
        data_phase = data[data.Type == comp_list[l]] #Collects the data from each phase
        #print(comp_list[l])
        for j in range(len(type_list)): #To analyze each geometrical aspect
            #print(type_list[j])
            typelist[j] = data_phase[type_list[j]].values.tolist() #Collects the actual values in a list
            for k, val in enumerate(typelist[j]): #To make sure a roundness of 1000 is not possible (we checked, there aren't any other 1000 values)
                if val == 1000:
                    typelist[j][k] = 1

            #print(typelist[j])
            value_list[i][l].append(typelist[j])    #Store the data in the list of lists

"""    for j in range(len(type_list)):
        typelist(case_list[i]).append(data_phase[type_list[j]].values.tolist())
        print(typelist[i][j]) """

print(value_list) #Take a guess what this does