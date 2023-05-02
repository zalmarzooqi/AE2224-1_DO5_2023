from commonimports import *


def setup_gui():
    # Define Button Commands
    def dpb_onclick():
        global data_path
        data_path = askdirectory()
        if len(data_path) > 0:
            if len(data_path) < 25:
                data_path_sel.config(text=data_path, fg="blue")
            else:
                data_path_sel.config(text=".../"+data_path.split(r"/")[-1], fg="blue")

    def opb_onclick():
        global output_path
        output_path = askdirectory()
        if len(output_path) > 0:
            if len(output_path) < 25:
                output_path_sel.config(text=output_path, fg="blue")
            else:
                output_path_sel.config(text=".../"+output_path.split(r"/")[-1], fg="blue")
            output_path += r"/Output"

    def acb_onclick():
        case_1_sel.set(1)
        case_2_sel.set(1)
        case_3_sel.set(1)
        case_4_sel.set(1)

    def ncb_onclick():
        case_1_sel.set(0)
        case_2_sel.set(0)
        case_3_sel.set(0)
        case_4_sel.set(0)

    def apb_onclick():
        geom_perim_sel.set(1)
        geom_circ_sel.set(1)
        geom_feret_sel.set(1)
        geom_feretx_sel.set(1)
        geom_ferety_sel.set(1)
        geom_feretangle_sel.set(1)
        geom_minferet_sel.set(1)
        geom_ar_sel.set(1)
        geom_solidity_sel.set(1)
        geom_round_sel.set(1)

    def npb_onclick():
        geom_perim_sel.set(0)
        geom_circ_sel.set(0)
        geom_feret_sel.set(0)
        geom_feretx_sel.set(0)
        geom_ferety_sel.set(0)
        geom_feretangle_sel.set(0)
        geom_minferet_sel.set(0)
        geom_ar_sel.set(0)
        geom_solidity_sel.set(0)
        geom_round_sel.set(0)

    def rb_onclick():
        global data_path, output_path
        data_path = ""
        output_path = ""
        data_path_sel.config(text="No folder selected!", fg="red")
        output_path_sel.config(text="No folder selected!", fg="red")
        folder_mode_sel.set(0)
        ncb_onclick()
        npb_onclick()
        filter_mode_sel.set("Known")
        composition_mode.set("Standard")

    def fb_onclick():
        global geometry_parameters, compo_mode, filter_mode, folder_mode, cases
        geometry_parameters = []
        if geom_perim_sel.get() == 1:
            geometry_parameters.append("Perim.")
        if geom_circ_sel.get() == 1:
            geometry_parameters.append("Circ.")
        if geom_feret_sel.get() == 1:
            geometry_parameters.append("Feret")
        if geom_feretx_sel.get() == 1:
            geometry_parameters.append("FeretX")
        if geom_ferety_sel.get() == 1:
            geometry_parameters.append("FeretY")
        if geom_feretangle_sel.get() == 1:
            geometry_parameters.append("FeretAngle")
        if geom_minferet_sel.get() == 1:
            geometry_parameters.append("MinFeret")
        if geom_ar_sel.get() == 1:
            geometry_parameters.append("AR")
        if geom_solidity_sel.get() == 1:
            geometry_parameters.append("Solidity")
        if geom_round_sel.get() == 1:
            geometry_parameters.append("Round")

        cases = []
        if case_1_sel.get() == 1:
            cases.append("Uninhibited")
        if case_2_sel.get() == 1:
            cases.append("Inhibited")
        if case_3_sel.get() == 1:
            cases.append("Inhibited Delayed")
        if case_4_sel.get() == 1:
            cases.append("Reimmersion")

        folder_mode = folder_mode_sel.get()
        filter_mode = filter_mode_sel.get()
        compo_mode = composition_mode.get()

        root.destroy()

    # Window
    root = tk.Tk()
    root.title("Setup2")
    root.resizable(False, False)

    # Fonts
    title_font = tk.font.Font(root, family="Segoe UI", size=13, weight="bold", underline=True)
    middle_font = tk.font.Font(root, family="Segoe UI", size=11, weight="bold", underline=False)
    default_font = tk.font.Font(root, family="Segoe UI", size=9, weight="normal", underline=False)

    # Frames
    folder_frame = tk.Frame(root,
                            bd=5,
                            relief=tk.SUNKEN,
                            padx=5,
                            pady=5)
    folder_frame.grid(column=0, row=0, sticky=tk.NSEW)
    cases_frame = tk.Frame(root,
                           bd=5,
                           relief=tk.SUNKEN,
                           padx=5,
                           pady=5)
    cases_frame.grid(column=0, row=1, sticky=tk.NSEW)
    geometry_frame = tk.Frame(root,
                              bd=5,
                              relief=tk.SUNKEN,
                              padx=5,
                              pady=5)
    geometry_frame.grid(column=1, row=0, rowspan=2, sticky=tk.NSEW)
    composition_frame = tk.Frame(root,
                                 bd=5,
                                 relief=tk.SUNKEN,
                                 padx=5,
                                 pady=5)
    composition_frame.grid(column=0, row=2, sticky=tk.NSEW)
    do_frame = tk.Frame(root,
                        bd=5,
                        relief=tk.SUNKEN,
                        padx=5,
                        pady=5)
    # do_frame.grid(column=1, row=2, sticky=tk.NSEW)
    bottom_frame = tk.Frame(root,
                            bd=10,
                            relief=tk.SUNKEN,
                            padx=5,
                            pady=5)
    bottom_frame.grid(column=0, row=3, columnspan=2, sticky=tk.NSEW)

    # Folders Frame
    # Set Labels
    tk.Label(folder_frame, text="Folders", font=title_font).grid(column=0, row=0, columnspan=3)
    tk.Label(folder_frame, text="Select the following folders", font=middle_font).grid(column=0, row=1, columnspan=3)
    tk.Label(folder_frame, text="Data Folder:", font=default_font).grid(column=0, row=2, sticky=tk.W)
    tk.Label(folder_frame, text="Output Folder:", font=default_font).grid(column=0, row=3, sticky=tk.W)
    tk.Label(folder_frame, text="Selected Folders", font=middle_font).grid(column=0, row=4, sticky=tk.W)
    tk.Label(folder_frame, text="Data:", font=default_font).grid(column=0, row=5, sticky=tk.W)
    tk.Label(folder_frame, text="Output:", font=default_font).grid(column=0, row=6, sticky=tk.W)
    # Define Variables
    folder_mode_sel = tk.IntVar()
    folder_mode_sel.set(0)
    # Variable Widgets
    data_button = tk.Button(folder_frame, text="Select Folder", command=dpb_onclick, state="disabled")
    data_button.grid(column=1, row=2)
    output_button = tk.Button(folder_frame, text="Select Folder", command=opb_onclick)
    output_button.grid(column=1, row=3)
    folder_mode_cb = tk.Checkbutton(folder_frame, text="One folder?", font=default_font, variable=folder_mode_sel, state="disabled")
    folder_mode_cb.grid(column=2, row=2)
    data_path_sel = tk.Label(folder_frame, text="Deprecated, data is bundled", fg="green")
    data_path_sel.grid(column=1, row=5, columnspan=2, sticky=tk.W)
    output_path_sel = tk.Label(folder_frame, text="No folder selected!", fg="red")
    output_path_sel.grid(column=1, row=6, columnspan=2, sticky=tk.W)

    # Cases Frame
    # Set Labels
    tk.Label(cases_frame, text="Cases", font=title_font).grid(column=0, row=0, columnspan=3)
    tk.Label(cases_frame, text="Select which cases are to be analyzed", font=middle_font).grid(column=0, row=1, columnspan=3)
    # Define Variables
    case_1_sel = tk.IntVar()
    case_1_sel.set(0)
    case_2_sel = tk.IntVar()
    case_2_sel.set(0)
    case_3_sel = tk.IntVar()
    case_3_sel.set(0)
    case_4_sel = tk.IntVar()
    case_4_sel.set(0)
    # Variable Widgets
    case_1_cb = tk.Checkbutton(cases_frame, text="Uninhibited", font=default_font, variable=case_1_sel)
    case_1_cb.grid(column=0, row=2, sticky=tk.W)
    case_2_cb = tk.Checkbutton(cases_frame, text="Inhibited", font=default_font, variable=case_2_sel)
    case_2_cb.grid(column=0, row=3, sticky=tk.W)
    case_3_cb = tk.Checkbutton(cases_frame, text="Inhibited Delayed", font=default_font, variable=case_3_sel)
    case_3_cb.grid(column=0, row=4, sticky=tk.W)
    case_4_cb = tk.Checkbutton(cases_frame, text="Reimmersion", font=default_font, variable=case_4_sel)
    case_4_cb.grid(column=0, row=5, sticky=tk.W)
    all_cases_button = tk.Button(cases_frame, text="All Cases", command=acb_onclick)
    all_cases_button.grid(column=1, row=2)
    no_cases_button = tk.Button(cases_frame, text="No Cases", command=ncb_onclick)
    no_cases_button.grid(column=2, row=2)

    # Geometry Frame
    # Set Labels
    tk.Label(geometry_frame, text="Geometry", font=title_font).grid(column=0, row=0, columnspan=3)
    tk.Label(geometry_frame, text="Select geometry parameters", font=middle_font).grid(column=0, row=1, columnspan=3)
    tk.Label(geometry_frame, text="\nSelect filtering mode", font=middle_font).grid(column=0, row=8, columnspan=3)
    # Define Variables
    geom_perim_sel = tk.IntVar()
    geom_perim_sel.set(0)
    geom_circ_sel = tk.IntVar()
    geom_circ_sel.set(0)
    geom_feret_sel = tk.IntVar()
    geom_feret_sel.set(0)
    geom_feretx_sel = tk.IntVar()
    geom_feretx_sel.set(0)
    geom_ferety_sel = tk.IntVar()
    geom_ferety_sel.set(0)
    geom_feretangle_sel = tk.IntVar()
    geom_feretangle_sel.set(0)
    geom_minferet_sel = tk.IntVar()
    geom_minferet_sel.set(0)
    geom_ar_sel = tk.IntVar()
    geom_ar_sel.set(0)
    geom_solidity_sel = tk.IntVar()
    geom_solidity_sel.set(0)
    geom_round_sel = tk.IntVar()
    geom_round_sel.set(0)
    filter_mode_sel = tk.StringVar()
    filter_mode_sel.set("Known")
    # Variable Widgets
    geom_perim_cb = tk.Checkbutton(geometry_frame, text="Perimeter", variable=geom_perim_sel)
    geom_perim_cb.grid(column=0, row=2, sticky=tk.W)
    geom_circ_cb = tk.Checkbutton(geometry_frame, text="Circularity", variable=geom_circ_sel)
    geom_circ_cb.grid(column=0, row=3, sticky=tk.W)
    geom_solidity_cb = tk.Checkbutton(geometry_frame, text="Solidity", variable=geom_solidity_sel)
    geom_solidity_cb.grid(column=0, row=4, sticky=tk.W)
    geom_round_cb = tk.Checkbutton(geometry_frame, text="Roundness", variable=geom_round_sel)
    geom_round_cb.grid(column=0, row=5, sticky=tk.W)
    geom_ar_cb = tk.Checkbutton(geometry_frame, text="Aspect Ratio", variable=geom_ar_sel)
    geom_ar_cb.grid(column=0, row=6, sticky=tk.W)
    geom_feret_cb = tk.Checkbutton(geometry_frame, text="Feret Diameter", variable=geom_feret_sel)
    geom_feret_cb.grid(column=1, row=2, sticky=tk.W)
    geom_feretx_cb = tk.Checkbutton(geometry_frame, text="Feret Diameter (X)", variable=geom_feretx_sel)
    geom_feretx_cb.grid(column=1, row=3, sticky=tk.W)
    geom_ferety_cb = tk.Checkbutton(geometry_frame, text="Feret Diameter (Y)", variable=geom_ferety_sel)
    geom_ferety_cb.grid(column=1, row=4, sticky=tk.W)
    geom_feretangle_cb = tk.Checkbutton(geometry_frame, text="Feret Angle", variable=geom_feretangle_sel)
    geom_feretangle_cb.grid(column=1, row=5, sticky=tk.W)
    geom_minferet_cb = tk.Checkbutton(geometry_frame, text="Minimum Feret", variable=geom_minferet_sel)
    geom_minferet_cb.grid(column=1, row=6, sticky=tk.W)
    all_parameters_button = tk.Button(geometry_frame, text="All Parameters", command=apb_onclick)
    all_parameters_button.grid(column=0, row=7)
    no_parameters_button = tk.Button(geometry_frame, text="No Parameters", command=npb_onclick)
    no_parameters_button.grid(column=1, row=7)
    filter_option_known = tk.Radiobutton(geometry_frame, text="Known", variable=filter_mode_sel,
                                         value="Known", font=default_font)
    filter_option_known.grid(column=0, row=9)
    filter_option_full = tk.Radiobutton(geometry_frame, text="Full", variable=filter_mode_sel,
                                        value="Full", font=default_font)
    filter_option_full.grid(column=1, row=9)

    # Composition Frame
    # Set Labels
    tk.Label(composition_frame, text="Composition", font=title_font).grid(column=0, row=0, columnspan=3)
    tk.Label(composition_frame, text="Select composition mode", font=middle_font).grid(column=0, row=1, columnspan=3)
    # Define Variables
    composition_mode = tk.StringVar()
    composition_mode.set("Standard")
    # Variable Widgets
    composition_option_standard = tk.Radiobutton(composition_frame, text="Standard",
                                                 variable=composition_mode, value="Standard", font=default_font)
    composition_option_standard.grid(column=0, row=2)
    composition_option_extended = tk.Radiobutton(composition_frame, text="Extended",
                                                 variable=composition_mode, value="Extended", font=default_font)
    composition_option_extended.grid(column=1, row=2)

    # Do Frame
    # Set Labels
    tk.Label(do_frame, text="Execute", font=title_font).grid(column=0, row=0, columnspan=3)
    tk.Label(do_frame, text="this is for later", font=default_font).grid(column=0, row=1, columnspan=3)
    # Define Variables
    do_excel_filter = tk.IntVar()
    do_roi_sort = tk.IntVar()
    do_summary = tk.IntVar()
    # Variable Widgets
    do_ef_cb = tk.Checkbutton(do_frame, text="Excel Filtering", variable=do_excel_filter)
    do_ef_cb.grid(column=0, row=2, sticky=tk.W)
    do_rs_cb = tk.Checkbutton(do_frame, text="ROI Sorting", variable=do_roi_sort)
    do_rs_cb.grid(column=0, row=3, sticky=tk.W)
    do_s_cb = tk.Checkbutton(do_frame, text="Execution Summary", variable=do_summary)
    do_s_cb.grid(column=0, row=4, sticky=tk.W)

    # Bottom Frame
    # Set Labels
    tk.Label(bottom_frame, text="Bottom", font=title_font).grid(column=0, row=0, columnspan=3)
    # Define Variables

    # Variable Widgets
    reset_button = tk.Button(bottom_frame, text="Reset Defaults", command=rb_onclick)
    reset_button.grid(column=0, row=0, columnspan=1)
    finish_button = tk.Button(bottom_frame, text="Finish", command=fb_onclick)
    finish_button.grid(column=1, row=0)

    # Loop window
    root.mainloop()


if __name__ == "__main__":
    setup_gui()
