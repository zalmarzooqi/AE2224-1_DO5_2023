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



# Empty lists for use in per type plotting (all particles of one type)
type_matrix_abs = []
type_matrix_rel = []
type_timesteps = []

# Iterate over the different particles/csv files
file_path = r"../Data/CSV/1_Uninhibited/0428-1481.csv"
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

# Find t_start and slope
start_val = 5
for val in file_matrix_abs_smooth:
    if val > start_val:
        t_start = file_timesteps[file_matrix_abs_smooth_list.index(val)]
        val_start = val
        break
slope_val = 20
for val in file_matrix_abs_smooth:
    if val > slope_val:
        t_slope = file_timesteps[file_matrix_abs_smooth_list.index(val)]
        val_slope = val
        break
slope_est = (val_slope - val_start) / (t_slope - t_start)
model_list = [slope_est * (i-t_start) for i in file_timesteps]

# Find t_star
max_ratio = 3
for i in range(1, file_matrix_abs_smooth_list.index(val_slope),-1 ):
    diff1 = model_list[i-1] - file_matrix_abs_smooth_list[i-1]
    diff2 = model_list[i] - file_matrix_abs_smooth_list[i]
    ratio = diff2 / diff1
    if ratio > max_ratio:
        t_star = file_timesteps[i]
        break

# Plotting particle
plt.plot(file_timesteps, file_matrix_abs, label="Data")
plt.plot(file_timesteps[:-(window_size-1)], file_matrix_abs_smooth, label="Smoothed Data")
plt.plot(file_timesteps, model_list, label="Model k1")
#plt.vlines(t_star, 0, 100, linestyles="dashed", label="t_star")
plt.xlabel("Time [s]")
plt.ylabel("Percentage of pixels crossing the COC [%]")
plt.title(f"Particle test")
plt.ylim(0, 110)
plt.legend()
plt.savefig(os.path.join(main_out_path, f"plot_test_regression.png"))
plt.show()
