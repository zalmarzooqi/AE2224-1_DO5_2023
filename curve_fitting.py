import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from corrosiononsetcolumn import timesteps_unin, matrixpercentabs, arrays

def model(x,a,b,c,d):
    return d + (a - d)/(1 + (x/c)**b)

popt, pcov = curve_fit(model, timesteps_unin, matrixpercentabs[0], p0=[3,2,-16,2])

a_opt, b_opt, c_opt, d_opt = popt
x_model = np.linspace(min(timesteps_unin), max(timesteps_unin), 100)
y_model = model(x_model, a_opt, b_opt, c_opt, d_opt) 
print(y_model)

'''
for i in range(len(arrays)):
    plt.plot(x_model, y_model, color='r')
    plt.show()
    '''