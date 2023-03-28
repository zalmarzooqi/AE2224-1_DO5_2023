import pandas as pd
import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename


# GUI
def dir_button():
    global folder_dir
    folder_dir = askdirectory()
    dir_sel_text.config(text=folder_dir, fg="blue")
    return folder_dir


def output_button():
    global output_dir
    output_dir = askdirectory()
    out_dir_sel_text.config(text=output_dir, fg="blue")
    return output_dir


def excel_button():
    global excel_dir
    excel_dir = askopenfilename()
    excel_dir_sel_text.config(text=excel_dir, fg="blue")

def finish_button():
    window.destroy()
    return


window = tk.Tk()
window.title("Setup")
window.geometry("500x400")
dir_text1 = tk.Label(text="\nSelect the folder containing all csv files")
dir_text1.pack()
dir_button = tk.Button(text="Select folder", command=dir_button)
dir_button.pack()
dir_text2 = tk.Label(text="Your folder:")
dir_text2.pack()
dir_sel_text = tk.Label(text="No folder selected.", fg="red")
dir_sel_text.pack()
excel_text1 = tk.Label(text="\n\nSelect the sorted excel file")
excel_text1.pack()
excel_button = tk.Button(text="Select file:", command=excel_button)
excel_button.pack()
excel_text2 = tk.Label(text="Your file:")
excel_text2.pack()
excel_dir_sel_text = tk.Label(text="No file selected.", fg="red")
excel_dir_sel_text.pack()
out_text1 = tk.Label(text="\n\nSelect the folder to save the data in")
out_text1.pack()
out_button = tk.Button(text="Select folder:", command=output_button)
out_button.pack()
out_text2 = tk.Label(text="Your folder:")
out_text2.pack()
out_dir_sel_text = tk.Label(text="No folder selected.", fg="red")
out_dir_sel_text.pack()
finish_button = tk.Button(text="Finish", command=finish_button)
finish_button.pack()
window.mainloop()

folders = ["S-phase", "Theta", "Secondary"]

if ("folder_dir" or "output_dir" or "excel_dir") not in globals():
    print("Something went wrong. Please try again.")
    exit()

if not os.path.exists(os.path.join(output_dir, "Sorted")):
    os.makedirs(os.path.join(output_dir, "Sorted"))
    for type in folders:
        os.makedirs(os.path.join(output_dir, "Sorted", type))

for type in folders:
    rois = []
    data = pd.read_excel(excel_dir, sheet_name=type)
    for i in range(data.max()[0]):
        rois.append(data.values[i][1])
    for file in os.listdir(folder_dir):
        roi_number = int(file[0:4])
        if roi_number in rois:
            shutil.copyfile(os.path.join(folder_dir, file), os.path.join(output_dir, "Sorted", type, file))
os.startfile(os.path.join(output_dir, "Sorted"))

