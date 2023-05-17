import pandas as pd
import os


folder_dir = r"C:\AETestanalysis\Outputmatlab"
file_dirs = [r"Reimmersion_uninhibited\1_LocalImgAnal_Num"]
             #r"3_Inhb_del\1_LocalImgAnal_Num\1_LocalImgAnal_Num",
             #r"4_Reimm_uninhb\1_LocalImgAnal_Num\1_LocalImgAnal_Num"]

new_file_dirs = ["1.csv", "2.csv", "3.csv", "4.csv"]
i = 0
for folder in file_dirs:
    read_folder_dir = os.path.join(folder_dir, folder)
    headers = ["Index", "Timestamp"]
    j = True
    # csv_folder_dir = os.path.join(folder_dir, folder)
    new_file_dir = os.path.join(folder_dir, "Output"+new_file_dirs[i])
    for file in os.listdir(read_folder_dir):
        file_dir = os.path.join(read_folder_dir, file)
        data = pd.read_csv(file_dir, header=None)
        if j:
            output = data.loc[:, 0:1]
            j = False

        pixels = data.sum(axis=1)[0]-1

        threshold = 30
        threshold += 2

        values = data.loc[:, 2:threshold].sum(axis=1)

        ratio = 1 - values / pixels

        output = pd.concat([output, ratio], axis=1)
        headers.append(file[0:-4])
    output.to_csv(new_file_dir, index=False, mode="w", header=headers)

    i += 1

os.startfile(folder_dir)
