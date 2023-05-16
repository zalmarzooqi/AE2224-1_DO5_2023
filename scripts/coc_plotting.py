from commonimports import *
from scripts import data_smoothing, class_check, linear_regression


# Function Definition
def coc_plotting(case, type, csv_file, output_folder, mode=1):
    # Set file and folder paths
    main_out_path = os.path.join(output_folder, f"Plots/COC/{case}/{type}")
    file_name = csv_file.split("\\")[-1]
    if not os.path.exists(main_out_path):
        os.makedirs(main_out_path)

    # Iterate over the different particles/csv files
    if csv_file[-4:] == ".csv":
        data = pd.read_csv(csv_file, header=None)          # Read file
        total_pixels = data.iloc[0, 3:].sum()               # Get the total amount of pixels

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
                print(f"No pixels outside of col. C found in file {file_name[:-4]}")
                sig_col = "Stop"
        if sig_col == "Stop":
            return

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

        # Skip particle if it is not of class A
        if not class_check.classA_check(type, file_matrix_abs, file_timesteps):
            print(file_name[:-4], "is not a class A particle, skipping...")
            return

        # Smoothen data
        smooth_abs = data_smoothing.data_smoothing(file_matrix_abs)

        # Linear regression
        roi = int(csv_file[-12:-9])
        lin_regr_output = linear_regression.linear_regression(roi, smooth_abs, file_timesteps)
        if not lin_regr_output:
            return False
        else:
            roi, k1_vals, k2_vals, t_s, t_k, t_f, k1_model, k2_model = lin_regr_output

        # Plotting single particle
        plt.plot(file_timesteps, file_matrix_abs, label="Data")
        plt.plot(file_timesteps, smooth_abs, label="Smooth Data")
        if mode == 1:
            linear_regression.linear_regression_plotting(k1_model, k2_model, t_s, t_k, t_f)
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Percentage of pixels crossing the COC [%]")
        plt.title(f"{case[2:]}, {type} Particle {int(csv_file[-12:-9])}")
        plt.ylim(0, 110)
        plt.xlim(0, 8000)
        plt.savefig(os.path.join(main_out_path, f"plot_{file_name[:-4]}.png"))
        plt.clf()

        # Save values in list
        coc_regression_output = [roi, k1_vals[0], k2_vals[0], t_s, t_k, t_f]
        return coc_regression_output


def coc_plotting_all(case, type, csv_folder, output_folder):
    # Set file and folder paths
    main_out_path = os.path.join(output_folder, f"Plots/COC/{case}/{type}")

    if not os.path.exists(main_out_path):
        os.makedirs(main_out_path)

    # Empty lists for use in per type plotting (all particles of one type)
    type_matrix_abs = []
    type_matrix_rel = []
    type_timesteps = []

    # Iterate over the different particles/csv files
    for file in os.listdir(csv_folder):
        if file[-4:] == ".csv":
            file_path = os.path.join(csv_folder, file)
            data = pd.read_csv(file_path, header=None)          # Read file
            total_pixels = data.iloc[0, 3:].sum()               # Get the total amount of pixels

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
                    # print(f"No pixels outside of col. C found in file {file} ({case}, {type})")
                    sig_col = "Stop"
            if sig_col == "Stop":
                continue

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

            if not class_check.classA_check(type, file_matrix_abs, file_timesteps):
                # print("ALL:",file, "is not a class A particle, skipping...")
                continue

            # Add the particle parameters to the type list, so it can be used in the plot of all particles
            type_matrix_abs.append(file_matrix_abs)
            type_matrix_rel.append(file_matrix_rel)
            type_timesteps.append(file_timesteps)

    # Plotting all particles
    for k in range(len(type_matrix_abs)):
        plt.plot(type_timesteps[k], type_matrix_abs[k])
    plt.xlabel("Time [s]")
    plt.ylabel("Percentage of pixels crossing the COC [%]")
    plt.title(f"{case[2:]}, all {type} particles")
    plt.ylim(0, 110)
    plt.xlim(0, 8000)
    plt.savefig(os.path.join(main_out_path, f"plot_all_particles.png"))
    plt.clf()
