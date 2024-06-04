import tkinter as tk
from tkinter import messagebox

def get_checked_items():
    selected = []
    for i, var in enumerate(check_vars):
        if var.get():
            selected.append(options[i])
    messagebox.showinfo("Selected Items", ", ".join(selected))

root = tk.Tk()
root.title("Checkbutton Example")

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
check_vars = []

for option in options:
    var = tk.BooleanVar()
    check_vars.append(var)
    chk = tk.Checkbutton(root, text=option, variable=var)
    chk.pack(anchor='w')

btn = tk.Button(root, text="Get Selected", command=get_checked_items)
btn.pack()

root.mainloop()
