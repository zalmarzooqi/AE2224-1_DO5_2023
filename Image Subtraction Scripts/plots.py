import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def column(data,i,a):
    column=[]
    for j in range (a,(len(data))):
        column.append((data[j][i]))
    column=np.array(column)
    return column

def histograms(compl,compl2):
    counts2,bins2=np.histogram(compl2)
    plt.hist(bins2[:-1],bins2,weights=counts2)

    counts,bins=np.histogram(compl)
    plt.hist(bins[:-1],80,weights=counts)
    plt.show()

def boxplots(compl,compl2):
    x=[compl2,compl]
    plt.ylabel('Time to reach 100%')
    plt.boxplot(x)
    plt.show()
with open('CSVReimmersion_uninhibitedfiltered.csv', newline='') as csvfile:
    reim = list(csv.reader(csvfile))
with open('CSVImmersion_uninhibited.csv', newline='') as csvfile:
    unin = list(csv.reader(csvfile))
compl=[]
for i in range (1,len(reim[0])):
    col=column(reim,i,1)
    one=0
    for j in range(0,len(col)):
        if float(col[j])==1 and one==0:
            b=column(reim,0,1)
            c=b[j]
            compl.append(int(c))
            one+=1
compl2=[]
for i in range (1,len(unin[0])):
    col=column(unin,i,1)
    one=0
    for j in range(0,len(col)):
        if float(col[j])==1 and one==0:
            b=column(unin,0,1)
            c=b[j]
            compl2.append(int(c))
            one+=1
compl=np.array(compl)
compl2=np.array(compl2)

#uncomment which plot you want and comment the other:

histograms(compl,compl2)
# boxplots(compl,compl2)


