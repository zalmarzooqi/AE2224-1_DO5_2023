import numpy as np
import pandas as pd
from numpy import std, mean

data = pd.read_excel(r'C:\users\fbens\Downloads\ParticleGeomCompo_uninhb.xlsx')
df = pd.DataFrame(data, columns=['Area'])
#print(df)

Area_array = df
print(Area_array)
#array_1 = [1, 2, 3, 4, 8, 12]

distance = std(Area_array) / 2 #, dtype=np.float64
mean = mean(Area_array)

print(mean)
print(distance)
#print(mean, distance)
print(mean - distance, mean + distance)