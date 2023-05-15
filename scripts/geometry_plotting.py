from commonimports import *


# Function Definition
def extracted_plotting(parameter_path, excel_path, output_path, case):

    # Create output path if it does not exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Open the Excel file with the area and geometry data
    particlemap_data = pd.read_excel(excel_path, sheet_name="Geometry Filtered")

    # Set the columns to only the area and geometry parameters
    columns = particlemap_data.columns.tolist()[2:-1]

    # Read the extracted parameter Excel files, one per case
    s_extracted_data = pd.read_excel(parameter_path, sheet_name="S-phase")
    th_extracted_data = pd.read_excel(parameter_path, sheet_name="Theta")
    sec_extracted_data = pd.read_excel(parameter_path, sheet_name="Secondary")

    # Set a list to the five extracted parameters
    params = s_extracted_data.columns.tolist()[2:]

    # Iterate over the different geometry parameters
    for i in range(len(columns)):

        # Set figure title
        plt.suptitle(f"{columns[i]} vs regression parameters ({case})")

        # Iterate over the different extracted parameters
        for j in range(len(params)):

            # Set empty lists for plots (x_parameters = x list, x_extracted = y list)
            s_parameters = []
            s_extracted = []
            th_parameters = []
            th_extracted = []
            sec_parameters = []
            sec_extracted = []

            # Iterate over the different ROIs in the filtered geometry Excel file
            for roi in particlemap_data["ROI"].values:

                # Check whether the particle has extracted parameters (S-phase)
                if roi in s_extracted_data["ROI"].values:

                    # Add x and y values
                    s_parameters.append(particlemap_data[particlemap_data["ROI"] == roi][columns[i]].values[0])
                    s_extracted.append(s_extracted_data[s_extracted_data["ROI"] == roi][params[j]].values[0])

                # Check whether the particle has extracted parameters (Theta)
                if roi in th_extracted_data["ROI"].values:

                    # Add x and y values
                    th_parameters.append(particlemap_data[particlemap_data["ROI"] == roi][columns[i]].values[0])
                    th_extracted.append(th_extracted_data[th_extracted_data["ROI"] == roi][params[j]].values[0])

                # Check whether the particle has extracted parameters (Secondary)
                if roi in sec_extracted_data["ROI"].values:
                    # Add x and y values
                    sec_parameters.append(particlemap_data[particlemap_data["ROI"] == roi][columns[i]].values[0])
                    sec_extracted.append(sec_extracted_data[sec_extracted_data["ROI"] == roi][params[j]].values[0])

            # Plot subplot
            plt.subplot(321+j)
            plt.title(columns[i]+" vs "+params[j])
            plt.xlabel(columns[i])
            plt.ylabel(params[j])
            plt.scatter(s_parameters, s_extracted, label="S-phase")
            plt.scatter(th_parameters, th_extracted, label="Theta")
            plt.scatter(sec_parameters, sec_extracted, label="Secondary")

        # Save figure
        # plt.legend()
        plt.savefig(output_path + f"/{case}_{columns[i]}_regression_plot.png")
        plt.clf()


if __name__ == "__main__":
    parameter_dir = r"S:\AE\BSc-2\TAS\Data\Output\Output\Extracted Parameters\1_Uninhibited_regr_params.xlsx"
    excel_dir = r"S:\AE\BSc-2\TAS\Data\Output\Output\Filtered Excels\Filtered_ParticleGeomCompo_uninhb.xlsx"
    output_path = r"test_folder"
    extracted_plotting(parameter_dir, excel_dir, output_path, "Uninhibited")
