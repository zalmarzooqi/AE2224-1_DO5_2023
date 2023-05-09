import csv
import matplotlib.pyplot as plt

import pandas as pd

def column(data, i):
    column=[]
    for j in range (1,(len(data))):
        column.append(float(data[j][i])) 
    return column

with open('CSVReimmersion_uninhibitedfiltered.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
print(len(data))
x=column(data,0)
for k in range (1,len(data[0])):
    y=column(data,k)
    for m in range(len(y)):
        y[m]=100*y[m]
    plt.xlim(0,x[-1])
    plt.xlabel("Time [s]")
    plt.ylabel("Percentage of changed pixels [%]")
    plt.plot(x,y)
plt.show()
