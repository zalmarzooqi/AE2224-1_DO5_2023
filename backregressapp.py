
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
# Basic modules
import os
import sys
import time
import shutil

# Installed modules
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.font
from tkinter.filedialog import askdirectory, askopenfilename

# # Custom modules
# from guis import *
# from scripts import *

def slope_k1(file_matrix_abs_smooth,file_timesteps,file_matrix_abs_smooth_list):
# Find t_start and slope
    margin  = 0.95
    start_val = 5
    for val in file_matrix_abs_smooth:
        if val > start_val:
            t_start = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_start = val
            break
    slope_val = 25
    for val in file_matrix_abs_smooth:
        if val>slope_val:
            t_slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_slope = val
            break
    
    k1 = (val_slope - val_start) / (t_slope - t_start)
    y_inter1 = val_slope-t_slope*k1
    model_listk1 = [k1 * (i-t_start)+y_inter1 for i in file_timesteps ]
    return t_start, k1, y_inter1, model_listk1

def slope_k2(file_matrix_abs_smooth,file_timesteps,file_matrix_abs_smooth_list):
#Find t100
    margin  = 0.95
    slope100_val = 93
    for val in file_matrix_abs_smooth:
        if val > slope100_val:
            t_100slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_100slope = val
            break
    slope80_val = 83
    for val in file_matrix_abs_smooth:
        if val > slope80_val:
            t_80slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
            val_80slope = val
            break
    if t_100slope > 600:
        rounded_t_100slope = round(t_100slope/10)*10
    else:
        rounded_t_100slope = round(t_100slope)
    k2 = (val_100slope-val_80slope)/(t_100slope-t_80slope)
    y_inter2 = val_100slope-k2*t_100slope
    model_listk2 = [k2*(i-t_80slope)+y_inter2 for i in file_timesteps]
    return t_100slope,rounded_t_100slope, k2, y_inter2, model_listk2

def intersect(k1,y_inter1,k2,y_inter2,file_matrix_abs_smooth_list,file_timesteps):
    t_star = (y_inter2-y_inter1)/(k1-k2)
    if t_star > 600:
        rounded_t_star = round(t_star/10)*10
    else:
        rounded_t_star = round(t_star)
    val_star = file_matrix_abs_smooth_list[file_timesteps.index(rounded_t_star)]
    return t_star,rounded_t_star, val_star

# Empty lists for use in per type plotting (all particles of one type)
type_matrix_abs = []
type_matrix_rel = []
type_timesteps = []

# Iterate over the different particles/csv files
file_path = r"Sorted\S-phase//0022-0074.csv"
main_out_path = r""
data = pd.read_csv(file_path, header=None)          # Read file
total_pixels = data.iloc[0, 3:].sum()               # Get the total amount of pixels
print(total_pixels)
# Empty lists for use in per particle plotting
file_matrix_abs = []
file_matrix_rel = []
file_timesteps = []

# Iterate over the different columns to find the threshold column
for i in range(3, data.shape[1]):
    if data.iloc[0, i] > 0:
        sig_col = i                                 # Stop looking in the columns when the
        break                                       # one has been found

    # Some files are weird and do not have any values past the "C" column in the csv
    # Currently I just skip these files/particles, but we may need to take a better look at them
    if i == data.shape[1]-1:
        print(f"No pixels outside of col. C found in file)")
        sig_col = "Stop"

# Iterate over the different rows to find the number of pixels that have passed the COC
for j in range(data.shape[0]):
    corroded_pixels = data.iloc[j, 3:sig_col].sum()
    corroded_percentage = corroded_pixels / total_pixels * 100
    file_matrix_abs.append(corroded_percentage)
    if j == 0:
        file_matrix_rel.append(corroded_percentage)
    else:
        file_matrix_rel.append(corroded_percentage-file_matrix_abs[j-1])

    # Find the timesteps
    file_timesteps.append(data.iloc[j, 1])
    if file_timesteps[-1] >= 74000:
        break

# Smoothing data
window_size = 15
weights = np.repeat(1.0, window_size) / window_size
file_matrix_abs_smooth = np.convolve(file_matrix_abs, weights, 'valid')
file_matrix_abs_smooth_list = file_matrix_abs_smooth.tolist()

t_start, k1, y_inter1, model_listk1 = slope_k1(file_matrix_abs_smooth,file_timesteps,file_matrix_abs_smooth_list)
t_100slope,rounded_t100slope, k2, y_inter2, model_listk2 = slope_k2(file_matrix_abs_smooth,file_timesteps,file_matrix_abs_smooth_list)
t_star,rounded_t_star, val_star = intersect(k1,y_inter1,k2,y_inter2,file_matrix_abs_smooth_list,file_timesteps)

k1new = LinearRegression().fit(np.array(file_timesteps[:file_timesteps.index(rounded_t_star)]).reshape(-1,1),np.array(file_matrix_abs_smooth_list[:file_timesteps.index(rounded_t_star)]).reshape(-1,1))


k2new = LinearRegression().fit(np.array(file_timesteps[file_timesteps.index(rounded_t_star):file_timesteps.index(rounded_t100slope)]).reshape(-1,1),np.array(file_matrix_abs_smooth_list[file_timesteps.index(rounded_t_star):file_timesteps.index(rounded_t100slope)]).reshape(-1,1))

new_model_listk1 = [k1new.coef_[0] * (i-t_start)+k1new.intercept_[0] for i in file_timesteps ]
new_model_listk1 = k1new.coef_[0] * file_timesteps+k1new.intercept_[0]


new_model_listk2 = k2new.coef_[0] * file_timesteps+k2new.intercept_[0]
print(np.shape(new_model_listk1))
plt.plot(file_timesteps, file_matrix_abs, label="Data")
plt.plot(file_timesteps[:-(window_size-1)], file_matrix_abs_smooth, label="Smoothed Data")
# plt.plot(file_timesteps[:len(model_listk1)], model_listk1, label="Model k1")
# plt.plot(file_timesteps[:len(model_listk2)], model_listk2, label="Model k2")
plt.plot(file_timesteps[:len(model_listk1)], new_model_listk1, label="Model k1new")
plt.plot(file_timesteps[:len(model_listk2)], new_model_listk2, label="Model k2new")
#plt.vlines(t_star, 0, 100, linestyles="dashed", label="t_star")
plt.xlabel("Time [s]")
plt.ylabel("Percentage of pixels crossing the COC [%]")
plt.title(f"Particle test")
plt.ylim(0, 110)
plt.legend()
plt.savefig(os.path.join(main_out_path, f"plot_test_regression.png"))
plt.show()