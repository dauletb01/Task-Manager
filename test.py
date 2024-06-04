import tkinter as tk
from tkinter import messagebox

def get_checked_items():
    selected = []
    for i, var in enumerate(check_vars):
        if var.get():
            selected.append(options[i])
    
    if selected:
        confirm = messagebox.askyesno("Confirmation", f"Вы выбрали: {', '.join(selected)}. Вы уверены?")
        if confirm:
            messagebox.showinfo("Selected Items", f"Вы выбрали: {', '.join(selected)}")
        else:
            messagebox.showinfo("Selected Items", "Выбор отменен")
    else:
        messagebox.showinfo("Selected Items", "Вы ничего не выбрали")

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