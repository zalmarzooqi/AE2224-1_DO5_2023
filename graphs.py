import csv
import matplotlib.pyplot as plt

import pandas as pd

def column(data, i):
    column=[]
    for j in range (1,(len(data))):
        column.append(float(data[j][i])) 
    return column
figure, axis = plt.subplots(3)
with open('CSVReimmersion_uninhibitedfiltered.csv', newline='') as csvfile:
    data1 = list(csv.reader(csvfile))
print(len(data1))
x1=column(data1,0)
for k1 in range (1,len(data1[0])):
    y1=column(data1,k1)
    for m in range(len(y1)):
        y1[m]=100*y1[m]
    axis[0].set(xlabel="Time [s]",ylabel="Percentage of changed pixels [%]",xlim=(0,x1[-1]))
    axis[0].plot(x1,y1)
    axis[0].set_title("Reimmersion Uninhibited")
with open('CSVImmersion_uninhibited.csv', newline='') as csvfile:
    data2 = list(csv.reader(csvfile))
print(len(data2))
x2=column(data2,0)
for k2 in range (1,len(data2[0])):
    y2=column(data2,k2)
    for m in range(len(y2)):
        y2[m]=100*y2[m]
    axis[1].set(xlabel="Time [s]",ylabel="Percentage of changed pixels [%]",xlim=(0,x2[-1]))
    axis[1].plot(x2,y2)
    axis[1].set_title("Immersion Uninhibited")
with open('CSVDelayed.csv', newline='') as csvfile:
    data3 = list(csv.reader(csvfile))
print(len(data3))
x3=column(data3,0)
for k3 in range (1,len(data3[0])):
    y3=column(data3,k3)
    for m in range(len(y3)):
        y3[m]=100*y3[m]
    axis[2].set(xlabel="Time [s]",ylabel="Percentage of changed pixels [%]",xlim=(0,x3[-1]))
    axis[2].plot(x3,y3)
    axis[2].set_title("Delayed")
    #plt.plot(x,y)
plt.show()
