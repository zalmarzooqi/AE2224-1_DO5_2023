from commonimports import *
from scripts import data_smoothing, linear_regression, class_check


# Function Definition
def image_subtraction_plotting(csv_file, output_path, case, excel_path, mode=1):

    # Set empty list to store regression data
    is_regression_list = []

    # Read the filtered Excel files to get type of particle
    excel_data = pd.read_excel(excel_path, sheet_name="Geometry Unfiltered")

    # Read the csv file containing Schanged% over time for all particles
    data = pd.read_csv(csv_file)

    # Create a list for the timesteps
    time_list = data["Timestamp"].values.tolist()

    # Iterate over the columns (= particles) in the csv file
    for particle in data.columns[1:]:

        # Create a list for the data values
        data_list = data[particle].values.tolist()

        # Change the values to percentages (from [0, 1])
        data_list = [i*100 for i in data_list]

        # Smooth the data
        smoothdata = data_smoothing.data_smoothing(data_list)

        # Apply linear regression
        lr_output = linear_regression.linear_regression(int(particle[:4]), smoothdata, time_list)

        # Skip to next particle if linear regression fails
        if not lr_output:
            continue
        else:
            roi, k1_vals, k2_vals, t_s, t_k, t_f, k1_model, k2_model = lr_output

        # Set the type of the particle according to the Excel file based on ROI
        try:
            type = excel_data[excel_data.ROI == int(particle[:4])]["Type"].values[0]

            # Skip if the particle is not in the Excel file (unknown composition)
        except IndexError:
            continue

        # Set output path and create folders
        sp_output_path = os.path.join(output_path, f"Plots/Image Subtraction/{case}/{type}")
        if not os.path.exists(sp_output_path):
            os.makedirs(sp_output_path)

        # Create data plot
        plt.plot(time_list, data_list, label="Data")

        # Create smooth data plot
        plt.plot(time_list, smoothdata, label="Smooth Data")

        # Plot linear regression data
        if mode == 1:
            linear_regression.linear_regression_plotting(k1_model, k2_model, t_s, t_k, t_f)

        # Finalize plot area
        plt.xlim(0, 8000)
        plt.ylim(0, 105)
        plt.xlabel("Time [s]")
        plt.ylabel("Schanged% [%]")
        plt.title(f"{case[2:]}, {type} Particle {int(particle[:4])}")
        plt.legend()

        # Save figure and clear for the next particle
        plt.savefig(os.path.join(sp_output_path, f"plot_{particle}"))
        plt.clf()

        is_regression_list.append([roi, type, k1_vals[0], k2_vals[0], t_s, t_k, t_f])
    return is_regression_list

if __name__ == "__main__":
    image_subtraction_plotting(r"../Data/Image Subtraction CSV/ImStCSV_1_Uninhibited.csv", "test_folder", "Uninhibited", "S:\AE\BSc-2\TAS\Data\Output\Filtered Excels\Filtered_1_Uninhibited_ParticleMap.xlsx")
