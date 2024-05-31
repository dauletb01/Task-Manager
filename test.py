import tkinter as tk

root = tk.Tk()
root.geometry('600x400')  # Установите размер окна

# Верхний фрейм
top_frame = tk.Frame(root, borderwidth=2, relief='groove')
top_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Левый фрейм
left_frame = tk.Frame(root, borderwidth=2, relief='groove')
left_frame.grid(row=1, column=0, sticky='nsew')

# Правый фрейм
right_frame = tk.Frame(root, borderwidth=2, relief='groove')
right_frame.grid(row=1, column=1, sticky='nsew')

# Установим веса для строк и столбцов
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=10)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Заполнение верхнего фрейма (если нужно)
top_label = tk.Label(top_frame, text="Task manager", borderwidth=2, relief='solid')
top_label.pack(expand=True, fill='both', padx=5, pady=5)

# Заполнение левого фрейма
for i in range(6):
    for j in range(3):
        label = tk.Label(left_frame, text=f"R{i}C{j}", borderwidth=2, relief='solid')
        label.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)

# Установим веса для строк и столбцов в левом фрейме
for i in range(6):
    left_frame.grid_rowconfigure(i, weight=1)
for j in range(3):
    left_frame.grid_columnconfigure(j, weight=1)

# Заполнение правого фрейма
for i in range(2):
    label = tk.Label(right_frame, text=f"R0C{i}", borderwidth=2, relief='solid')
    label.grid(row=0, column=i, sticky='nsew', padx=2, pady=2)

# Установим веса для строк и столбцов в правом фрейме
right_frame.grid_rowconfigure(0, weight=1)
for i in range(2):
    right_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
