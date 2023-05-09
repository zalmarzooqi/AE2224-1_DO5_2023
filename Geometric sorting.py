import pandas as pd
import matplotlib as plt
from scipy.interpolate import interp1d
from scipy.misc import derivative
import os
import copy

p = ['D:', '\Tudelft', '2nd year', 'Project', 'Q3', 'Sorted Data', 'Output']

case_list = ['Sorted_ParticleGeomCompo_inhb_del.xlsx', 'Sorted_ParticleGeomCompo_inhb.xlsx', 'Sorted_ParticleGeomCompo_reim_uninhb.xlsx', 'Sorted_ParticleGeomCompo_uninhb.xlsx']
type_list = ['ROI', 'Area', 'Circ.', 'Feret', 'AR', 'Solidity']
comp_list = ['S-phase', 'Theta', 'Secondary']


value_list = []
typelist = copy.deepcopy(type_list)

for i in range(len(case_list)):
    path = os.path.join(*p, case_list[i])
    #print(path)
    data = pd.read_excel(path, sheet_name='Geometry Filtered')
    value_list.append([])
    for l in range(len(comp_list)):
        value_list[i].append([])
        data_secondary = data[data.Type == comp_list[l]]
        #print(comp_list[l])
        for j in range(len(type_list)):
            #print(type_list[j])
            typelist[j] = data_secondary[type_list[j]].values.tolist()
            for k, val in enumerate(typelist[j]):
                if val == 1000:
                    typelist[j][k] = 1

            #print(typelist[j])
            value_list[i][l].append(typelist[j])

"""    for j in range(len(type_list)):
        typelist(case_list[i]).append(data_secondary[type_list[j]].values.tolist())
        print(typelist[i][j]) """

print(value_list)