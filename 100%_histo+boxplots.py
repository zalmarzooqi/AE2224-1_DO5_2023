import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#functions:
def column(data,i,a):
    column=[]
    for j in range (a,(len(data))):
        column.append((data[j][i]))
    column=np.array(column)
    return column

def histograms(compl,compl2):
    counts2,bins2=np.histogram(compl2)
    plt.hist(bins2[:-1],5,weights=counts2,label='Uninhibited')

    counts,bins=np.histogram(compl)
    plt.hist(bins[:-1],20,weights=counts,label='Reimmersion')
    plt.title('Comparison of '+names[caseno]+' particles for reimmersion vs uninhbited conditions')
    plt.xlabel('Time to reach 100% [s]')
    plt.ylabel('Number of particles')
    plt.legend()
    plt.savefig('Histo_'+names[caseno]+'_particles_reim_vs_uninhib.png')
    plt.show()
    

def boxplots(compl,compl2):
    x=[compl2,compl]
    plt.ylabel('Time to reach 100% [s]')
    plt.boxplot(x)
    plt.xticks([1, 2], ['Uninhibited', 'Reimmersion'])
    plt.title('Comparison of '+names[caseno]+' particles for reimmersion vs uninhbited conditions')
    plt.savefig('Boxplot_'+names[caseno]+'_particles_reim_vs_uninhib.png')
    plt.show()
    
caseno=3 #0 to 3, select which case you want after looking at the names below
names=['all','S-phase','secondary-phase','theta-phase']
reimnames=['CSVReimmersion_uninhibitedfiltered.csv','S-Phase_reimmersion_particles.csv','secondary_reimmersion_particles.csv','theta-phase_reimmersion_particles.csv']
uninhibnames=['CSVImmersion_uninhibited.csv','S-Phase_uninhib_particles.csv','secondary_uninhib_particles.csv','theta-phase_uninhib_particles.csv']
with open(reimnames[caseno], newline='') as csvfile:
    reim = list(csv.reader(csvfile))
with open(uninhibnames[caseno], newline='') as csvfile:
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
#boxplots(compl,compl2)

