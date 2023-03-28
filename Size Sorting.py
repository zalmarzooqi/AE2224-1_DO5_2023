# Import packages
import pandas as pd
import os
import numpy as np
import tkinter as tk
from tkinter.filedialog import askdirectory
import time


# OPTIONS GUI
# Define actions on button presses
# Select directory button
def directory_button():
    global folder_dir
    # Ask for the directory
    folder_dir = askdirectory()
    # Set the text to the chosen directory and make it blue
    selected_folder.config(text=folder_dir, fg="blue")
    return folder_dir


# Finish button
def finish_button():
    global geometry_parameter
    global mode_selection
    global folder_mode
    # Get the chosen geometry parameter
    geometry_parameter = parameter_menu.get()
    # Get the chosen mode
    mode_selection = mode_menu.get()
    folder_mode = folder_mode_menu.get()
    # Close the window
    window.destroy()
    return geometry_parameter, mode_selection, folder_mode



# Set up the window
window = tk.Tk()
window.title("Setup")
window.geometry("550x380")
# Display the folder selection text
folder_text = tk.Label(text="\nSelect the location of the \"Data\" folder."
                            "\nNote that the new files with the sorted data will also be stored in this folder, under \"Sorted Data\".")
folder_text.pack()
# Display the folder selection button
folder_button = tk.Button(text="Select folder", command=directory_button)
folder_button.pack()
folder_mode_text = tk.Label(text="Folder mode (default 0):")
folder_mode_text.pack()
folder_mode_menu = tk.StringVar()
folder_mode_menu.set(0)
mode_options = [0, 1]
menu3 = tk.OptionMenu(window, folder_mode_menu, *mode_options)
menu3.pack()
# Display the chosen folder
folder_text2 = tk.Label(text="Your folder:")
folder_text2.pack()
selected_folder = tk.Label(text="No folder selected", fg="red")
selected_folder.pack()
# Display the geometry selection text
geometry_text = tk.Label(text="\nSelect the parameter to be used for geometry.")
geometry_text.pack()
# Define the geometry parameter options
geometry_options = ['None', 'Perim.', 'BX', 'BY', 'Width', 'Height',
       'Circ.', 'Feret', 'FeretX', 'FeretY', 'FeretAngle', 'MinFeret', 'AR',
       'Round', 'Solidity']
parameter_menu = tk.StringVar()
parameter_menu.set("None")
# Display the drop-down menu for geometry parameter selection
menu = tk.OptionMenu(window, parameter_menu, *geometry_options)
menu.pack()
# Display the mode selection text
mode_text = tk.Label(text="Choose the geometry filter mode (default 0):")
mode_text.pack()
# Define mode selection options
mode_menu = tk.StringVar()
mode_menu.set(0)
# Display the drop-down menu for mode selection
menu2 = tk.OptionMenu(window, mode_menu, *mode_options)
menu2.pack()
# Display the final text
finish_text = tk.Label(text="\nWhen all options are set, click the button below.")
finish_text.pack()
# Display the final button
process_button = tk.Button(text="Pre-process Data", command=finish_button)
process_button.pack()
# Loop window
window.mainloop()

start_time = time.time()
# SET PARAMETERS AND CONSTANTS
# Add exit if no folder was specified
if "folder_dir" not in globals():
    print("No folder was specified. Please try again.")
    exit()

# Find the chosen geometry parameter and add it to the used columns
if "geometry_parameter" not in globals():               # Error
    print("Something went wrong. Please try again.")
    exit()
elif str(geometry_parameter) == "None":                 # No geometry parameter
    cols = ["ROI", "Area", "Type"]
else:                                                   # Chosen geometry parameter
    cols = ["ROI", "Area", str(geometry_parameter), "Type"]

# Set file names within the data folder
if str(folder_mode) == "0":
    file_dirs = [r"1_Immersion_Uninhibited\2_Particle Map\ParticleGeomCompo_uninhb.xlsx",
                r"2_Immersion_Inhibited\2_Particle Map\ParticleGeomCompo_inhb.xlsx",
                r"3_Immersion_Inhibited_delayed (60 s)\2_Particle Map\ParticleGeomCompo_inhb_del.xlsx",
                r"4_Reimmersion_Uninhibited\2_Particle Map\ParticleGeomCompo_reim_uninhb.xlsx"]
else:
    file_dirs = [r"ParticleGeomCompo_uninhb.xlsx",
                r"ParticleGeomCompo_inhb.xlsx",
                r"ParticleGeomCompo_inhb_del.xlsx",
                r"ParticleGeomCompo_reim_uninhb.xlsx"]

# Set file names for the pre-processed files
file_names = [r"uninhb_sorted.xlsx",
              r"inhb_sorted.xlsx",
              r"inhb_del_sorted.xlsx",
              r"reim_uninhb_sorted.xlsx"]

# Set names for the three types of particles
types = ['S-phase', 'Theta', 'Secondary']

# Set iteration constant
i = 0

# FILE CREATION
# Create the directory where the new files are saved if it does not exist yet
new_folder_dir = os.path.join(folder_dir, "Sorted Data")
if not os.path.exists(new_folder_dir):
    os.makedirs(new_folder_dir)

# Create files if they do not exist, and wipe if they do
df = np.random.randn(1, 1)
data = pd.DataFrame(df)
for file in file_names:
    file_dir = os.path.join(new_folder_dir, file)
    writer = pd.ExcelWriter(file_dir, engine='openpyxl', mode='w')
    data.to_excel(writer, sheet_name="All")
    writer.close()

# PREPARE ORIGINAL FILES
for file in file_dirs:
    file_dir = os.path.join(folder_dir, file)
    if not os.path.exists(file_dir):
        print("Error:", file, "does not exist. Skipping.")
        continue
    data = pd.read_excel(file_dir, "Sheet1", header=None)
    data.iloc[0, 0] = "ROI"
    if str(data.iloc[1, 0]).upper() == "NAN":
        data.drop(index=data.index[1], axis=0, inplace=True)
    writer = pd.ExcelWriter(file_dir, engine="openpyxl", mode="w")
    data.to_excel(writer, sheet_name="Sheet1", header=None)
    writer.close()

# SORTING
# Iterate over the four files
for file in file_dirs:
    # Set file directories
    file_dir = os.path.join(folder_dir, file)
    if not os.path.exists(file_dir):
        file_dirs.remove(file)
        # print("Error:", file, "does not exist. Skipping.")
        continue
    new_file_dir = os.path.join(new_folder_dir, file_names[i])
    # Read only the wanted columns (ROI, Area, Type and geometry parameter if specified)
    data = pd.read_excel(file_dir, "Sheet1", usecols=cols)
    # Write all data to the new file
    data = data.reset_index(drop=True)
    data.index = data.index + 1
    writer = pd.ExcelWriter(new_file_dir, engine='openpyxl', mode='w')
    data.to_excel(writer, sheet_name="All")
    writer.close()
    # Iterate over the three different particle types
    for phase in types:
        # Filter out only the current type
        data_filter = data[data.Type == phase]
        # Sort based on area (and ROI in case two areas are equal)
        data_sorted = data_filter.sort_values(['Area', 'ROI'])
        # Reset the indices
        data_sorted = data_sorted.reset_index(drop=True)
        data_sorted.index = data_sorted.index + 1
        # Write to the new file
        writer = pd.ExcelWriter(new_file_dir, engine='openpyxl', mode='a', if_sheet_exists='replace')
        data_sorted.to_excel(writer, sheet_name=phase)
        writer.close()

    # Select data for geometry based on chosen mode
    if mode_selection == "0":       # Only the data with a known particle type is used
        data_geom = data[(data.Type == types[0]) | (data.Type == types[1]) | (data.Type == types[2])]
        # Write all geometry data to the new file
        data_geom = data_geom.reset_index(drop=True)
        data_geom.index = data_geom.index + 1
        writer = pd.ExcelWriter(new_file_dir, engine='openpyxl', mode='a', if_sheet_exists='replace')
        data_geom.to_excel(writer, sheet_name="Geometry Unfiltered")
        writer.close()
    elif mode_selection == "1":     # All data is used
        data_geom = data
    else:                           # Error
        print("Something went wrong. Please try again.")
        exit()
    # Find the upper and lower quartiles
    lower_q = data_geom.quantile(0.25, numeric_only=True)[1]
    upper_q = data_geom.quantile(0.75, numeric_only=True)[1]
    # Filter out data which has and area outside the whiskers (outliers)
    data_geom = data_geom[data_geom.Area >= lower_q - (upper_q - lower_q) * 1.5]
    data_geom = data_geom[data_geom.Area <= upper_q + (upper_q - lower_q) * 1.5]
    # Sort the data by geometry parameter in case there is one (and area and ROI as before)
    if len(cols) == 3:
        data_geom = data_geom.sort_values([cols[1], cols[0]])
    elif len(cols) == 4:
        data_geom = data_geom.sort_values([cols[2],cols[1],cols[0]])
    else:
        print("An error has occurred. Please try again.")
        exit()
    # Reset the indices
    data_geom = data_geom.reset_index(drop=True)
    data_geom.index = data_geom.index + 1
    # Write to the new file
    writer = pd.ExcelWriter(new_file_dir, engine='openpyxl', mode='a', if_sheet_exists='replace')
    data_geom.to_excel(writer, sheet_name="Geometry Filtered")
    writer.close()

    # Increase iteration constant
    i += 1

# TEXT FILE CREATION
# Define some constants and variables
sets = ["Uninhibited", "Inhibited", "Delayed", "Reimmersed"]
if mode_selection == "0":
    sheets = ["All", "Geometry Filtered", "Geometry Unfiltered"]
elif mode_selection == "1":
    sheets = ["All", "Geometry Filtered"]
else:
    print("Something went wrong. Please try again.")
    exit()
i = 0
# Create text file
with open(os.path.join(new_folder_dir, "pre-processing summary.txt"), 'w') as f:
    # Print selected options
    f.write("Chosen geometry parameter: "+str(geometry_parameter)+"\nChosen filter mode: "+str(mode_selection)+"\n\n")
    for file in file_names:
        test = pd.read_excel(os.path.join(new_folder_dir, file), sheet_name=None)
        if "S-phase" not in test.keys():
            continue
        # Print the test type
        data = pd.read_excel(os.path.join(new_folder_dir, file), sheet_name=sheets)
        f.write("\n"+sets[i]+":")
        # Print the size and geometry parameter ranges
        for sheet in sheets:
            f.write("\n - Number of particles "+sheet+": "+str(int(data[sheet].max(numeric_only=True)[0])))
            f.write("\n     - Minimum size: "+str(int(data[sheet].min(numeric_only=True)[2])))
            f.write("\n     - Maximum size: "+str(int(data[sheet].max(numeric_only=True)[2])))
            if geometry_parameter != "None":
                f.write("\n     - Minimum "+str(geometry_parameter)+": "+str(int(data[sheet].min(numeric_only=True)[3])))
                f.write("\n     - Maximum "+str(geometry_parameter)+": "+str(int(data[sheet].max(numeric_only=True)[3])))
        f.write("\n\n")
        # Increase iteration constant
        i += 1

# GUI 2
# Define what happens on button click
def done_button():
    window2.destroy()


# Set up window
window2 = tk.Tk()
window2.title("Done!")
window2.geometry("220x90")
# Display text
message = tk.Label(text=f"\nPre-processing has finished in {time.time()-start_time:.2f} s.\n")
message.pack()
# Display button
done_button = tk.Button(text="Done", command=done_button)
done_button.pack()
# Loop window
window2.mainloop()

# OPEN FOLDER
os.startfile(new_folder_dir)
