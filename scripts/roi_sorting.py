from commonimports import *
from scripts import excel_filtering
import shutil


# Function definition
def roi_sort(excel_path, csv_path, output_path):

    # Remove output path if it exists and create again (wipe and/or create)
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.makedirs(output_path)

    # Iterate over the three different particle types
    for type in excel_filtering.types:

        # Create type folder
        os.makedirs(os.path.join(output_path, type))

        # Find the ROIs in the sorted Excel sheet
        rois = []
        data = pd.read_excel(excel_path, sheet_name=type)
        for i in range(data.max()[0]):
            rois.append(data.values[i][1])

        # Copy and paste the csv file to the folder if the particle is in the sorted Excel sheet
        for csv_file in os.listdir(csv_path):
            roi_number = int(csv_file[0:4])
            if roi_number in rois:
                shutil.copyfile(os.path.join(csv_path, csv_file), os.path.join(output_path, type, csv_file))
