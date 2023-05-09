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
with open('CSVReimmersion_uninhibitedfiltered.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))#unsorted data
with open('ParticleGeomCompo_reim_uninhb.csv', newline='') as csvfile:
    comp= list(csv.reader(csvfile))#particle composition csv
types=column(comp,28,1)#list of particle types
index=column(comp,0,1)#index names corresponding to particle types
seccheck=0 #checks number of particles in secondary
scheck=0
tcheck=0
secondary=pd.DataFrame(column(data,0,0))
sphase=pd.DataFrame(column(data,0,0))
theta=pd.DataFrame(column(data,0,0))
for j in range(1,len(data[0])):
    for i in range(len(index)):
        if int(data[0][j][0:4])==int(index[i]):
            if types[i]=='Secondary':
                seccheck+=1
                secondary.insert(1,str(data[0][j]),(column(data,j,0)))
            elif types[i]=='S-phase':
                scheck+=1
                sphase.insert(1,str(data[0][j]),(column(data,j,0)))
            elif types[i]=='Theta':
                tcheck+=1
                theta.insert(1,str(data[0][j]),(column(data,j,0)))
pd.DataFrame(secondary).to_csv("secondary_reimmersion_particles.csv")
pd.DataFrame(sphase).to_csv("S-Phase_reimmersion_particles.csv")
pd.DataFrame(theta).to_csv("theta-phase_reimmersion_particles.csv")
secondary=secondary.to_numpy()
sphase=sphase.to_numpy()
theta=theta.to_numpy()
print(secondary)
print(sphase)
print(theta)

def columns(data, i):
    columns=[]
    for j in range (1,(len(data))):
        columns.append(float(data[j][i])) 
    return columns
figure, axis = plt.subplots(3)
x=columns(secondary,0)
for k in range (2,len(secondary[0])):
    y=columns(secondary,k)
    for m in range(len(y)):
        y[m]=100*y[m]
    #smoothing
    kernel_size = 3
    kernel = np.ones(kernel_size) / kernel_size
    y_convolved = np.convolve(y, kernel, mode='same')
    #plt.xlim(0,x[-1])
    axis[0].set(xlabel="Time [s]",ylabel="Percentage of changed pixels [%]",xlim=(0,1400))
    axis[0].plot(x,y_convolved)
    axis[0].set_title("Secondary")
    #plt.plot(x,y_convolved)
t=columns(sphase,0)
for k in range (2,len(sphase[0])):
    u=columns(sphase,k)
    for m in range(len(u)):
        u[m]=100*u[m]
    #smoothing
    kernel_size = 5
    kernel = np.ones(kernel_size) / kernel_size
    u_convolved = np.convolve(u, kernel, mode='same')
    axis[1].set(xlabel="Time [s]",ylabel="Percentage of changed pixels [%]",xlim=(0,5000))
    axis[1].plot(t,u_convolved)
    axis[1].set_title("S-Phase")
v=columns(theta,0)
for k in range (2,len(theta[0])):
    w=columns(theta,k)
    for m in range(len(w)):
        w[m]=100*w[m]
    #smoothing
    kernel_size = 5
    kernel = np.ones(kernel_size) / kernel_size
    w_convolved = np.convolve(w, kernel, mode='same')
    axis[2].set(xlabel="Time [s]",ylabel="Percentage of changed pixels [%]",xlim=(0,5000))
    axis[2].plot(v,w_convolved)
    axis[2].set_title("Theta-Phase")
plt.show()
plt.savefig("Reimmersion_sorted_plots")
