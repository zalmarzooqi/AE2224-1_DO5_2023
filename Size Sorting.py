# Import packages
import pandas as pd
import os
import numpy as np

# Set directory names
folder_dir = r"S:\AE\BSc-2\TAS\Data"                        # Where the data folder is saved
new_folder_dir = r"S:\AE\BSc-2\TAS\Data\Sorted Data"        # Where you want to save the new files
file_dirs = [r"1_Immersion_Uninhibited\2_Particle Map\ParticleGeomCompo_uninhb.xlsx",
             r"2_Immersion_Inhibited\2_Particle Map\ParticleGeomCompo_inhb.xlsx",
             r"3_Immersion_Inhibited_delayed (60 s)\2_Particle Map\ParticleGeomCompo_inhb_del.xlsx",
             r"4_Reimmersion_Uninhibited\2_Particle Map\ParticleGeomCompo_reim_uninhb.xlsx"]
file_names = [r"uninhb_sorted.xlsx",
              r"inhb_sorted.xlsx",
              r"inhb_del_sorted.xlsx",
              r"reim_uninhb_sorted.xlsx"]
types = ['S-phase', 'Theta', 'Secondary']
i = 0

# Creates the new files or clears them if already present
df = np.random.randn(1, 1)
data = pd.DataFrame(df)
for file in file_names:
    file_dir = os.path.join(new_folder_dir, file)
    writer = pd.ExcelWriter(file_dir, engine='openpyxl', mode='w')
    data.to_excel(writer, sheet_name=types[0])
    writer.close()


# Iterate over old files
for file in file_dirs:
    file_dir = os.path.join(folder_dir, file)
    # noinspection PyTypeChecker
    data = pd.read_excel(file_dir, "Sheet1", usecols='A, B, AC')    # A is ROI, B is Area, AC is Type
    # iterate over the different types of particles
    for phase in types:
        data_filter = data[data.Type == phase]                  # Filter out the wanted type
        data_sorted = data_filter.sort_values(['Area', 'ROI'])  # Sort by area
        data_sorted = data_sorted.reset_index(drop=True)        # Reset the index value and add 1
        data_sorted.index = data_sorted.index + 1
        new_file_dir = os.path.join(new_folder_dir, file_names[i])
        # Write to the new files
        writer = pd.ExcelWriter(new_file_dir, engine='openpyxl', mode='a', if_sheet_exists='replace')
        data_sorted.to_excel(writer, sheet_name=phase)
        writer.close()
    i += 1
