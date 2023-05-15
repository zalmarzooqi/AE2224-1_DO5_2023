from commonimports import *
from scripts import writing, data_correction

# Set Constants
types = ["S-phase", "Theta", "Secondary"]


# Function Definition
def excel_filtering(excel_path, sorted_path, cols, filter_mode):

    # Define Indexing function (used multiple times throughout the program, function is easier than copy and paste)
    def indexing(df):
        df = df.reset_index(drop=True)
        df.index += 1
        return df

    # Read Excel file, reset indices, correct the data and write to new file
    data = pd.read_excel(excel_path, "Sheet1", usecols=cols)
    data_correction.data_correction(data)
    data = indexing(data)
    writing.writer_new(sorted_path, data, "All")

    # Iterate over the different types
    for phase in types:

        # Filter out the type
        data_filter = data[data.Type == phase]

        # Sort by Area and ROI, reset indices and write to new file
        data_sorted = data_filter.sort_values(["Area", "ROI"])
        data_sorted = indexing(data_sorted)
        writing.writer_add(sorted_path, data_sorted, phase)

    # Find unfiltered data
    if filter_mode == "Known":
        data_geom = data[(data.Type == types[0]) | (data.Type == types[1]) | (data.Type == types[2])]
        data_geom = indexing(data_geom)
        writing.writer_add(sorted_path, data_geom, "Geometry Unfiltered")
    elif filter_mode == "Full":
        data_geom = data
    else:
        # Exit if something goes wrong (extra coding, error message is in main.py)
        sys.exit()

    # Find upper and lower quantiles
    lower_q = data_geom.quantile(0.25, numeric_only=True)[1]
    upper_q = data_geom.quantile(0.75, numeric_only=True)[1]

    # Filter out data outside the ranges (quantiles +- 1.5*IQR)
    data_geom = data_geom[data_geom.Area >= lower_q - (upper_q - lower_q) * 1.5]
    data_geom = data_geom[data_geom.Area <= lower_q + (upper_q - lower_q) * 1.5]

    # Sort by first geometry parameter (if present), Area, ROI
    if len(cols) in [3+len(setup_gui_2.geometry_parameters), 10+len(setup_gui_2.geometry_parameters)]:
        data_geom = data_geom.sort_values([cols[1], cols[0]])
    elif len(cols) in [4+len(setup_gui_2.geometry_parameters), 11+len(setup_gui_2.geometry_parameters)]:
        data_geom = data_geom.sort_values([cols[2], cols[1], cols[0]])

    # Reset indices and write to new file
    data_geom = indexing(data_geom)
    writing.writer_add(sorted_path, data_geom, "Geometry Filtered")
