import numpy as np
import pandas as pd
from numpy import std, mean

data = pd.read_excel(r'C:\users\fbens\Downloads\ParticleGeomCompo_uninhb.xlsx')
df = pd.DataFrame(data, columns=['Area'])
#print(df)

Area_array = df
#print(Area_array)
#array_1 = [1, 2, 3, 4, 8, 12]

distance = std(Area_array) ** (1/2) #, dtype=np.float64
mean = mean(Area_array)

min = mean - distance
max = mean + distance

#print(mean)
#print(distance)
#print(mean, distance)
print(min, max)
min1 = 0
max1 = 4000

array_new = Area_array

for i in range(len(Area_array)):
    if data['Area'].loc[data.index[i]] < min:
        array_new = Area_array[i::]
    if data['Area'].loc[data.index[i]] > max:
        Area_array = Area_array[:i:]

"""""
for i in range(len(Area_array)):
    if Area_array[i] < min:
        min1 = i
    if max < Area_array[i] < max1:
        max1 = i

Area_array_2 = Area_array[min1, max1]
"""
print(Area_array_2)
