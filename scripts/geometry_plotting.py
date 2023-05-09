from commonimports import *


# Function Definition
def geometry_plotting(excel_file_dir, output_path, geometry_parameter, rois, k1, k2, t_onset, t_star):
    data = pd.read_excel(excel_file_dir, sheet_name="Sheet1", usecols=["ROI", geometry_parameter])
    particle_data = []
    labels = ["k1", "k2", "t_onset", "t_star"]
    for i, roi in enumerate(rois):
        one_particle = [roi, k1[i], k2[i], t_onset[i], t_star[i], data[data.ROI == roi][geometry_parameter].values[0]]
        particle_data.append(one_particle)

    for i in range(4):
        x = [j[-1] for j in particle_data]
        y = [k[i+1] for k in particle_data]
        plt.scatter(x, y)
        plt.title(f"{geometry_parameter} vs {labels[i]}")
        plt.xlabel(geometry_parameter)
        plt.ylabel(labels[i])
        plt.savefig(os.path.join(output_path, f"geometry_plot_{labels[i]}.png"))
        plt.clf()


if __name__ == "__main__":
    excel_dir = r"../Data/Original/ParticleGeomCompo_uninhb.xlsx"
    geometry_param = "Circ."
    rois = [1, 2, 3, 4, 5]
    k1 = [0.1, 0.2, 0.3, 0.2, 0.1]
    k2 = [0.1, 0.2, 0.3, 0.2, 0.1]
    t_onset = [10, 10, 10, 10, 10]
    t_star = [10, 10, 10, 10, 10]
    output = r""

    geometry_plotting(excel_dir, output, geometry_param, rois, k1, k2, t_onset, t_star)
