from commonimports import *


def error_message(data_path, error_code="not_found"):
    def onclick():
        root.destroy()
        sys.exit()


    root = tk.Tk()
    root.title("Error")
    icon_path = os.path.join(data_path, "Icons/error.png")
    icon = tk.PhotoImage(file=icon_path)
    root.iconphoto(False, icon)

    # Fonts
    title_font = tk.font.Font(root, family="Segoe UI", size=13, weight="bold", underline=True)
    middle_font = tk.font.Font(root, family="Segoe UI", size=11, weight="bold", underline=False)
    default_font = tk.font.Font(root, family="Segoe UI", size=9, weight="normal", underline=False)

    frame = tk.Frame(root, bd=5, relief=tk.SUNKEN, padx=5, pady=5)
    frame.grid(column=0, row=0)

    message = tk.Label(frame,
                       text="An error has occurred. Please try again.",
                       font=middle_font)
    message.grid(column=0, row=0)

    code_message = tk.Label(frame,
                            text=f"Error Code: {error_code}",
                            font=middle_font,
                            fg="red")
    code_message.grid(column=0, row=1)

    reference_message = tk.Label(frame,
                                 text="For more information, "
                                      "please refer to the program documentation found in its repository.",
                                 font=default_font)
    reference_message.grid(column=0, row=2)

    exit_button = tk.Button(frame,
                            text="Exit",
                            font=middle_font,
                            command=onclick,
                            padx=15,
                            pady=5)
    exit_button.grid(column=0, row=3, sticky=tk.S, pady=15)

    root.mainloop()

    sys.exit()


if __name__ == "__main__":
    error_message(r"../Data", "test message")
