from commonimports import *
from scripts import writing


# Function Definition
def subtraction_processing(csv_path, threshold, output_path):
    # Create output path if needed
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Begin list of headers
    headers = ["Index", "Timestamp"]

    # Add to add the first two columns once
    init = True

    # Iterate over the csv files in the folder
    for csv_file in os.listdir(csv_path):
        if csv_file[-4:] == ".csv":

            # Set file path
            file_dir = os.path.join(csv_path, csv_file)

            # Read csv file
            data = pd.read_csv(file_dir, header=None)

            # Add index and timestamps on first iteration
            if init:
                output_data = data.loc[:, 0:1]
                init = False

            pixels = data.sum(axis=1)[0]-1

            values = data.loc[:, 2:threshold+2].sum(axis=1)

            ratio = 1 - values / pixels

            output_data = pd.concat([output_data, ratio], axis=1)
            headers.append(csv_file[0:-4])

    writing.csv_writer(output_path, output_data, headers)


def subtraction_plotting():
    return

