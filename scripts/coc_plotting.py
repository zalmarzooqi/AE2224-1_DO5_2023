from commonimports import *


# Function Definition
def coc_plotting(data_folder, output_folder, cases):
    # Set file and folder paths
    main_out_path = os.path.join(output_folder, r"Plots")
    type_paths = ["S-phase", "Theta", "Secondary"]

    if not os.path.exists(main_out_path):
        for case in cases:
            os.makedirs(os.path.join(main_out_path, case))
            for type in type_paths:
                os.makedirs(os.path.join(main_out_path, case, type))

    # Iterate over the different cases
    for case in cases:

        # Iterate over the different particle types
        for type in type_paths:

            # Set path to folder of current case and type
            folder = os.path.join(data_folder, case, type)

            # Empty lists for use in per type plotting (all particles of one type)
            type_matrix_abs = []
            type_matrix_rel = []
            type_timesteps = []

            # Iterate over the different particles/csv files
            for file in os.listdir(folder):
                if file[-4:] == ".csv":
                    file_path = os.path.join(folder, file)
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
                            print(f"No pixels outside of col. C found in file {file} ({case}, {type})")
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

                    # Plotting single particle
                    plt.plot(file_timesteps, file_matrix_abs)
                    plt.xlabel("Time [s]")
                    plt.ylabel("Percentage of pixels crossing the COC [%]")
                    plt.title(f"{case[2:]}, {type} Particle {int(file[-12:-9])}")
                    plt.ylim(0, 110)
                    plt.savefig(os.path.join(main_out_path, f"{case}/{type}/plot_{file[-13:-4]}.png"))
                    plt.clf()

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
            plt.savefig(os.path.join(main_out_path, f"{case}/{type}/plot_all_particles.png"))
            plt.clf()
