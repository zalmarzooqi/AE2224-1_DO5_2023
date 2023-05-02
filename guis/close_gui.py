from commonimports import *


def close_gui(time="__seconds__"):
    if time != "__seconds__":
        time_used = round(time, 2)
    else:
        time_used = time

    def onclick():
        root.destroy()

    root = tk.Tk()
    # root.geometry("220x110")
    root.title("Done!")
    # set checkmark icon

    # Fonts
    title_font = tk.font.Font(root, family="Segoe UI", size=13, weight="bold", underline=True)
    middle_font = tk.font.Font(root, family="Segoe UI", size=11, weight="bold", underline=False)
    default_font = tk.font.Font(root, family="Segoe UI", size=9, weight="normal", underline=False)

    frame = tk.Frame(root, bd=5, relief=tk.SUNKEN, padx=5, pady=5)
    frame.grid(column=0, row=0, sticky=tk.NSEW)

    title = tk.Label(frame,
                     text="Done!",
                     font=title_font)
    title.grid(column=0, row=0)
    message = tk.Label(frame,
                       text=f"The program has finished in {time_used} seconds.",
                       font=default_font)
    message.grid(column=0, row=1)

    done_button = tk.Button(frame,
                            text="Done",
                            command=onclick,
                            font=middle_font,
                            padx=15,
                            pady=5)
    done_button.grid(column=0, row=2, pady=15)

    root.mainloop()
