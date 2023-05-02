from commonimports import *


def setup_gui():
    def fb_onclick():
        global data_path
        data_path = askdirectory()
        if len(data_path) > 0:
            folder_sel_label2.config(text=data_path,
                                    fg="blue")

    def ob_onclick():
        global output_path
        output_path = askdirectory() + "/Output"
        if len(output_path) > 0:
            output_sel_label2.config(text=output_path,
                                     fg="blue")

    def finb_onclick():
        global cases
        global filter_mode
        global folder_mode
        global compo_mode
        global geometry_parameters
        cases = []
        geometry_parameters = []
        for case_used in cases_menu.curselection():
            cases.append(cases_menu.get(case_used))
        if geom_perim.get() == 1:
            geometry_parameters.append("Perim.")
        if geom_circ.get() == 1:
            geometry_parameters.append("Circ.")
        if geom_feret.get() == 1:
            geometry_parameters.append("Feret")
        if geom_feretx.get() == 1:
            geometry_parameters.append("FeretX")
        if geom_ferety.get() == 1:
            geometry_parameters.append("FeretY")
        if geom_feretangle.get() == 1:
            geometry_parameters.append("FeretAngle")
        if geom_minferet.get() == 1:
            geometry_parameters.append("MinFeret")
        if geom_ar.get() == 1:
            geometry_parameters.append("AR")
        if geom_solidity.get() == 1:
            geometry_parameters.append("Solidity")
        if geom_round.get() == 1:
            geometry_parameters.append("Round")
        filter_mode = filter_sel.get()
        folder_mode = folder_mode_sel.get()
        compo_mode = compo_mode_sel.get()
        root.destroy()

    root = tk.Tk()
    root.title("Setup")

    left_frame = tk.Frame(root)
    left_frame.grid(column=0, row=0)
    right_frame = tk.Frame(root)
    right_frame.grid(column=1, row=0)

    folder_label1 = tk.Label(left_frame,
                             text="Select your data folder.",
                             padx=10,
                             pady=10)
    folder_label1.pack()
    folder_button = tk.Button(left_frame,
                              text="Select folder",
                              command=fb_onclick)
    folder_button.pack()
    folder_sel_label1 = tk.Label(left_frame,
                                text="Your selected folder:",
                                padx=10,
                                pady=10)
    folder_sel_label1.pack()
    folder_sel_label2 = tk.Label(left_frame,
                                text="No folder selected!",
                                fg="red",
                                padx=10,
                                pady=5)
    folder_sel_label2.pack()

    folder_mode_label = tk.Label(left_frame,
                                 text="Select folder mode:",
                                 padx=10,
                                 pady=5)
    folder_mode_label.pack()
    folder_mode_options = [0, 1]
    folder_mode_sel = tk.StringVar()
    folder_mode_sel.set(0)
    folder_mode_menu = tk.OptionMenu(left_frame,
                                     folder_mode_sel,
                                     *folder_mode_options)
    folder_mode_menu.pack()

    cases_label = tk.Label(left_frame,
                           text="Select which cases are to be analyzed:",
                           padx=10,
                           pady=15)
    cases_label.pack()
    cases_options = ["Uninhibited",
                     "Inhibited",
                     "Inhibited Delayed",
                     "Reimmersed"]
    cases_menu = tk.Listbox(left_frame,
                            selectmode="multiple",
                            height=len(cases_options))
    cases_menu.pack()
    for case in cases_options:
        cases_menu.insert(tk.END, case)

    parameter_label = tk.Label(right_frame,
                               text="Select which geometry parameters are to be used in the analysis:",
                               padx=10,
                               pady=15)
    parameter_label.pack()

    geom_perim = tk.IntVar()
    geom_perim.set(0)
    tk.Checkbutton(right_frame, text="Perimeter", variable=geom_perim).pack()
    geom_circ = tk.IntVar()
    geom_circ.set(0)
    tk.Checkbutton(right_frame, text="Circularity", variable=geom_circ).pack()
    geom_feret = tk.IntVar()
    geom_feret.set(0)
    tk.Checkbutton(right_frame, text="Feret", variable=geom_feret).pack()
    geom_feretx = tk.IntVar()
    geom_feretx.set(0)
    tk.Checkbutton(right_frame, text="Feret X", variable=geom_feretx).pack()
    geom_ferety = tk.IntVar()
    geom_ferety.set(0)
    tk.Checkbutton(right_frame, text="Feret Y", variable=geom_ferety).pack()
    geom_feretangle = tk.IntVar()
    geom_feretangle.set(0)
    tk.Checkbutton(right_frame, text="Feret Angle", variable=geom_feretangle).pack()
    geom_minferet = tk.IntVar()
    geom_minferet.set(0)
    tk.Checkbutton(right_frame, text="Minimum Feret", variable=geom_minferet).pack()
    geom_ar = tk.IntVar()
    geom_ar.set(0)
    tk.Checkbutton(right_frame, text="Aspect Ratio", variable=geom_ar).pack()
    geom_round = tk.IntVar()
    geom_round.set(0)
    tk.Checkbutton(right_frame, text="Roundness", variable=geom_round).pack()
    geom_solidity = tk.IntVar()
    geom_solidity.set(0)
    tk.Checkbutton(right_frame, text="Solidity", variable=geom_solidity).pack()

    filter_label = tk.Label(right_frame,
                            text="Select geometry filter mode (default 0):",
                            padx=10,
                            pady=10)
    filter_label.pack()
    filter_options = [0, 1]
    filter_sel = tk.StringVar()
    filter_sel.set(0)
    filter_menu = tk.OptionMenu(right_frame,
                                filter_sel,
                                *filter_options)
    filter_menu.pack()

    compo_mode_label = tk.Label(left_frame,
                                text="Select composition mode:",
                                padx=10,
                                pady=10)
    compo_mode_label.pack()
    compo_mode_options = ["Standard",
                          "Extended"]
    compo_mode_sel = tk.StringVar()
    compo_mode_sel.set(compo_mode_options[0])
    compo_mode_menu = tk.OptionMenu(left_frame,
                                    compo_mode_sel,
                                    *compo_mode_options)
    compo_mode_menu.pack()

    output_label = tk.Label(left_frame,
                            text="Select the location where the output will be saved:",
                            padx=10,
                            pady=10)
    output_label.pack()
    output_button = tk.Button(left_frame,
                              text="Select Folder",
                              command=ob_onclick)
    output_button.pack()
    output_sel_label1 = tk.Label(left_frame,
                                 text="Selected folder:",
                                 padx=10,
                                 pady=10)
    output_sel_label1.pack()
    output_sel_label2 = tk.Label(left_frame,
                                 text="No folder selected!",
                                 fg="red",
                                 padx=10,
                                 pady=5)
    output_sel_label2.pack()

    finish_label = tk.Label(left_frame,
                            text="When all options are set, press the button below.",
                            padx=10,
                            pady=20)
    finish_label.pack()
    finish_button = tk.Button(left_frame,
                              text="Pre-process Data",
                              command=finb_onclick,
                              padx=3,
                              pady=10)
    finish_button.pack()

    root.mainloop()
