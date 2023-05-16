from commonimports import *


# Function definition
def create_summary(output_path=r"", geometry_parameters="parameters",
                   filter_mode="Known", cases="cases", composition_mode="Standard"):

    # Create file path
    path = os.path.join(output_path, "execution_summary.txt")

    # Open the file in "write" mode
    with open(path, "w") as f:

        # Write the chosen options
        f.write(f"Selected options:"
                f"\n - Geometry parameters: {geometry_parameters}"
                f"\n - Filter mode: {filter_mode}"
                f"\n - Cases: {cases}"
                f"\n - Composition mode: {composition_mode}\n")

        # Iterate over the different sorted Excel files
        for file in os.listdir(output_path):
            if file[-5:] == ".xlsx":

                # Create datasets per Excel sheet
                all_data = pd.read_excel(os.path.join(output_path, file), sheet_name="All")
                sphase_data = pd.read_excel(os.path.join(output_path, file), sheet_name="S-phase")
                theta_data = pd.read_excel(os.path.join(output_path, file), sheet_name="Theta")
                secondary_data = pd.read_excel(os.path.join(output_path, file), sheet_name="Secondary")
                geom_f_data = pd.read_excel(os.path.join(output_path, file), sheet_name="Geometry Filtered")
                if filter_mode == "Known":
                    geom_u_data = pd.read_excel(os.path.join(output_path, file), sheet_name="Geometry Unfiltered")
            else:
                continue

            # Write the number of particles per sheet
            f.write(f"\n\nFile: {file}"
                    f"\n - N particles (all): {int(all_data.max(numeric_only=True)[0])}"
                    f"\n - N particles (s-phase): {sphase_data.max(numeric_only=True)[0]}"
                    f"\n - N particles (theta): {theta_data.max(numeric_only=True)[0]}"
                    f"\n - N particles (secondary): {secondary_data.max(numeric_only=True)[0]}"
                    f"\n - N particles (geometry filtered): {geom_f_data.max(numeric_only=True)[0]}")
            if filter_mode == "Known":
                f.write(f"\n - N particles (geometry unfiltered): {geom_u_data.max(numeric_only=True)[0]}")
