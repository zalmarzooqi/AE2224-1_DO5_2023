from commonimports import *

try:
    data_path = os.path.join(sys._MEIPASS, r"Data")
except AttributeError:
    data_path = r"Data"

setup_gui_2.setup_gui(data_path)
start_time = time.time()

file_dirs = [r"ParticleGeomCompo_uninhb.xlsx",
             r"ParticleGeomCompo_inhb.xlsx",
             r"ParticleGeomCompo_inhb_del.xlsx",
             r"ParticleGeomCompo_reim_uninhb.xlsx"]

try:
    if len(setup_gui_2.cases) == 0:
        error_coding.error_message(data_path, 3)
except AttributeError:
    error_coding.error_message(data_path, 1)

try:
    output_path = setup_gui_2.output_path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
except AttributeError:
    error_coding.error_message(data_path, 4)

if len(setup_gui_2.geometry_parameters) == 0:
    cols = ["ROI", "Area", "Type"]
else:
    cols = ["ROI", "Area", "Type"]
    for par in setup_gui_2.geometry_parameters:
        cols.append(par)

extended_compos = ["Al At%",
                   "Cu At%",
                   "Mg At%",
                   "Fe At%",
                   "Mn At%",
                   "Si At%",
                   "O At%"]
if setup_gui_2.compo_mode == "Extended":
    cols.extend(extended_compos)

csvs = [r"1_Uninhibited",
        r"2_Inhibited",
        r"3_Inhibited Delayed",
        r"4_Reimmersed"]

csvs_used = []
file_dirs_used = []
if "Uninhibited" in setup_gui_2.cases:
    file_dirs_used.append(file_dirs[0])
    csvs_used.append(csvs[0])
if "Inhibited" in setup_gui_2.cases:
    file_dirs_used.append(file_dirs[1])
    csvs_used.append(csvs[1])
if "Inhibited Delayed" in setup_gui_2.cases:
    file_dirs_used.append(file_dirs[2])
    csvs_used.append(csvs[2])
if "Reimmersion" in setup_gui_2.cases:
    file_dirs_used.append(file_dirs[3])
    csvs_used.append(csvs[3])

# Filter the Excel files
i = 0
for case in file_dirs_used:
    try:
        excel_path = os.path.join(data_path, "Original", case)
    except AttributeError:
        error_coding.error_message(data_path, 2)
    if not os.path.exists(os.path.join(output_path, "Filtered Excels")):
        os.makedirs(os.path.join(output_path, "Filtered Excels"))
    sorted_excel_path = os.path.join(output_path, "Filtered Excels/Filtered_"+case)
    try:
        excel_filtering.excel_filtering(excel_path, sorted_excel_path, cols, setup_gui_2.filter_mode)
    except FileNotFoundError:
        error_coding.error_message(data_path, 5)

    try:
        csv_path = os.path.join(sys._MEIPASS, data_path, "CSV", csvs_used[i])
    except AttributeError:
        csv_path = os.path.join(data_path, "CSV", csvs_used[i])

    csv_output_path = os.path.join(output_path, "Sorted ROIs", csvs_used[i])
    try:
        roi_sorting.roi_sort(sorted_excel_path, csv_path, csv_output_path)
    except FileNotFoundError:
        error_coding.error_message(data_path, 6)

    i += 1

# Plot the COC vs time graphs
try:
    # Execute if it is selected
    if setup_gui_2.exec_coc_plotting == 1:
        try:
            # Create directory to save the parameter Excel files in
            if not os.path.exists(os.path.join(output_path, "Extracted Parameters")):
                os.makedirs(os.path.join(output_path, "Extracted Parameters"))

            # Iterate over the different cases
            for case in csvs_used:

                # Create an Excel file to store the parameters in
                df = pd.DataFrame([[0, 1], [2, 3]])
                param_out_path = os.path.join(output_path, f"Extracted Parameters/{case}_regr_params.xlsx")
                writing.writer_new(param_out_path, df, "S-phase")

                # Iterate over the different types
                for type in excel_filtering.types:

                    # Set headers and path
                    parameters = []
                    folder_path = os.path.join(output_path, f"Sorted ROIs/{case}/{type}")

                    # Iterate over the different particles
                    for csv_file in os.listdir(os.path.join(output_path, f"Sorted ROIs/{case}/{type}")):

                        # Set path, find regression parameters and plot
                        file_path = os.path.join(folder_path, csv_file)
                        coc_regression_out = coc_plotting.coc_plotting(case, type, file_path, output_path)

                        # If parameters are found, add them to list
                        if coc_regression_out:
                            parameters.append(coc_regression_out)

                    # Plot all particles together
                    coc_plotting.coc_plotting_all(case, type, folder_path, output_path)

                    # Write the regression parameters to Excel
                    regr_output = pd.DataFrame(parameters, columns=["ROI", "k1", "k2", "t_s", "t_k", "t_f"])
                    writing.writer_add(param_out_path, regr_output, type)

        # Stop if the csv files are not found
        except FileNotFoundError:
            error_coding.error_message(data_path, 7)

# Stop in case of many scenarios (error in code, error in setup GUI, ...)
except AttributeError:
    error_coding.error_message(data_path, 8)

# Create execution summary
try:
    if setup_gui_2.exec_execution_summary == 1:
        execution_summary.create_summary(output_path, setup_gui_2.geometry_parameters, setup_gui_2.filter_mode,
                                         setup_gui_2.cases, setup_gui_2.compo_mode)
except AttributeError:
    error_coding.error_message(data_path, 9)

# Show final GUI and open the output folder
close_gui.close_gui(data_path, time.time()-start_time)
os.startfile(output_path)
