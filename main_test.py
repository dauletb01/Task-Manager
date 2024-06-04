import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json

config_file_name = "config.json"
task_file_name = "task.json"
statuss = "ALL"
add_window = None
delate_active = FALSE
delate_list =[]

def get_config():

    with open(config_file_name, "r", encoding="utf-8") as file:
        config_data = json.load(file)

    return config_data

def write_config():

    config_data = get_config()
    config_data["pothicion_x"] = root.winfo_x()
    config_data["pothicion_y"] = root.winfo_y()


    with open(config_file_name, "w", encoding="utf-8") as file:
         json.dump(config_data, file)

def on_closing():
    write_config()
    root.destroy()

def get_task():

    with open(task_file_name, "r", encoding="utf-8") as file:
        task_data = json.load(file)

    return task_data

def get_amaunt_task():
    tasks = get_task()
    amaunt_done = 0
    amaunt_progres = 0

    for task in tasks:
        if task["status"]: 
            amaunt_done+=1
        else:
            amaunt_progres+=1

    return amaunt_done, amaunt_progres

def write_task(task_data):

    with open(task_file_name, "w", encoding="utf-8") as file:
        json.dump(task_data, file)

    draw_task()

def checkbutton_changed(id):
    tasks = get_task()

    for task in tasks:
        if task["id"] == id: 
            task["status"] = not(task["status"])
            break
    
    write_task(tasks)
    draw_task()
    draw_status()

def draw_task():
    global statuss
    global delate_list
    delate_list =[]
    for widget in frame_left.winfo_children():
        widget.destroy()

    tasks = get_task()

    try: 
        if statuss == "ALL": draw_task_all(tasks)
        elif statuss == "done": draw_task_done(tasks)
        elif statuss == "progres": draw_task_progres(tasks)
    except NameError:
        draw_task_all(tasks)
        print("suka")
    else:
        print("Nothing went wrong")  

def draw_task_all(tasks):
    i = 0
    for task in tasks:
        var = BooleanVar()
        delate_list.append(var)

        enabled = IntVar()
        if delate_active:
            number=tk.Checkbutton(frame_left, text=f"{task["id"]}", borderwidth=2, relief='solid',padx=10, pady=10, variable=var)
        else:
            number=tk.Label(frame_left, text=f"{task["id"]}", borderwidth=2, relief='solid',padx=10, pady=10)

        text=tk.Label(frame_left, text=f"{task["task"]}", borderwidth=2, relief='solid',padx=10, pady=10, justify=tk.LEFT)
        # status = tk.Checkbutton(frame_left, text= "Done" if task["status"] else "In progress" , borderwidth=2, variable=enabled, command=checkbutton_changed(task["id"]), relief='solid', padx=10, pady=10)
        status = tk.Checkbutton(frame_left, text="Done" if task['status'] else "In progress", borderwidth=2, variable=enabled, command=lambda task_id=task['id']: checkbutton_changed(task_id), relief='solid', padx=10, pady=10)

        number.grid(row=i, column=0, sticky='nsew')
        text.grid(row=i, column=1, sticky='nsew')
        status.grid(row=i, column=2, sticky='nsew')

        i+=1

def draw_task_done(tasks):
    i = 0
    for task in tasks:
        if not(task["status"]): continue

        var = BooleanVar()
        delate_list.append(var)

        enabled = IntVar()
        if delate_active:
            number=tk.Checkbutton(frame_left, text=f"{task["id"]}", borderwidth=2, relief='solid',padx=10, pady=10, variable=var)
        else:
            number=tk.Label(frame_left, text=f"{task["id"]}", borderwidth=2, relief='solid',padx=10, pady=10)
        text=tk.Label(frame_left, text=f"{task["task"]}", borderwidth=2, relief='solid',padx=10, pady=10, justify=tk.LEFT)
        # status = tk.Checkbutton(frame_left, text= "Done" if task["status"] else "In progress" , borderwidth=2, variable=enabled, command=checkbutton_changed(task["id"]), relief='solid', padx=10, pady=10)
        status = tk.Checkbutton(frame_left, text="Done" if task['status'] else "In progress", borderwidth=2, variable=enabled, command=lambda task_id=task['id']: checkbutton_changed(task_id), relief='solid', padx=10, pady=10)


        number.grid(row=i, column=0, sticky='nsew')
        text.grid(row=i, column=1, sticky='nsew')
        status.grid(row=i, column=2, sticky='nsew')

        i+=1

def draw_task_progres(tasks):
    i = 0
    for task in tasks:
        if task["status"]: continue

        var = BooleanVar()
        delate_list.append(var)

        enabled = IntVar()
        if delate_active:
            number=tk.Checkbutton(frame_left, text=f"{task["id"]}", borderwidth=2, relief='solid',padx=10, pady=10, variable=var)
        else:
            number=tk.Label(frame_left, text=f"{task["id"]}", borderwidth=2, relief='solid',padx=10, pady=10)
        text=tk.Label(frame_left, text=f"{task["task"]}", borderwidth=2, relief='solid',padx=10, pady=10, justify=tk.LEFT)
        # status = tk.Checkbutton(frame_left, text= "Done" if task["status"] else "In progress" , borderwidth=2, variable=enabled, command=checkbutton_changed(task["id"]), relief='solid', padx=10, pady=10)
        status = tk.Checkbutton(frame_left, text="Done" if task['status'] else "In progress", borderwidth=2, variable=enabled, command=lambda task_id=task['id']: checkbutton_changed(task_id), relief='solid', padx=10, pady=10)


        number.grid(row=i, column=0, sticky='nsew')
        text.grid(row=i, column=1, sticky='nsew')
        status.grid(row=i, column=2, sticky='nsew')

        i+=1

def draw_status():
    amaunt_done, amaunt_prigres = get_amaunt_task()

    for widget in frame_right_status.winfo_children():
        widget.destroy()


    lable_done = tk.Label(frame_right_status, text=f"Done:", font=("Arial", 10, 'bold'))
    lable_done.grid( row=0, column=0)
    lable_done_count = tk.Label(frame_right_status, text= amaunt_done, font=("Arial", 10, 'bold'))
    lable_done_count.grid( row=0, column=1)


    lable_progres = tk.Label(frame_right_status, text=f"In progres:", font=("Arial", 10, 'bold'))
    lable_progres.grid( row=1, column=0)
    lable_progres_count = tk.Label(frame_right_status, text= amaunt_prigres, font=("Arial", 10, 'bold'))
    lable_progres_count.grid( row=1, column=1)

def btn_all_change():
    print("ALL")
    global statuss
    statuss = "ALL"
    draw_task()

def btn_done_change():
    print("done")
    global statuss
    statuss = "done"
    draw_task()

def btn_progres_change():
    print("progres")
    global statuss
    statuss = "progres"
    draw_task()

def create_add_window():
    global add_window
    if add_window is None or not tk.Toplevel.winfo_exists(add_window):
        add_window = Tk()
        add_window.title("ADD window")
        add_window.geometry("250x200")
        root.resizable(False, False)

        entr = Entry(add_window, font=("Arial", 15))
        entr.pack()

        add_button = tk.Button(add_window, borderwidth=2, relief='groove', padx=5, pady=5, text="Add task", command=lambda: write_task_to_json(entr.get()))
        add_button.pack()

        add_window.protocol("WM_DELETE_WINDOW", on_closing_new_window)

def write_task_to_json(text_task):
    # print(task)
    tasks = get_task()

    json_task = {"id": tasks[-1]["id"] + 1, "task": text_task, "status": FALSE}

    tasks.append(json_task)
    write_task(tasks)
    on_closing_new_window()
    draw_task()

def on_closing_new_window():
    global add_window
    add_window.destroy()
    add_window = None

def delate_tasks():
    global delate_active
    global delate_select_button
    delate_active = not delate_active
    print(delate_active)

    if delate_active:
        delate_select_button = tk.Button(frame_right, borderwidth=2, relief='groove', padx=5, pady=5, text="Delate selection tasks", command=get_checked_items)
        delate_select_button.pack(side=tk.LEFT, anchor=NW, fill=X)
    else:
        delate_select_button.destroy()

    draw_task()

def get_checked_items():
    selected = []
    tasks = get_task()
    for i, var in enumerate(delate_list):
        print(var.get())
        if var.get():
            selected.append(str(tasks[i]["id"]))

    if selected:
        confirm = messagebox.askyesno("Confirmation", f"Вы выбрали: {', '.join(selected)}. Вы уверены?")
        if confirm:
            messagebox.showinfo("Selected Items", f"Вы выбрали: {', '.join(selected)}")
            delate_tasks_to_json(selected)
        else:
            messagebox.showinfo("Selected Items", "Выбор отменен")
    else:
        messagebox.showinfo("Selected Items", "Вы ничего не выбрали")

def delate_tasks_to_json(id):
    tasks = get_task()

    tasks_new = [item for item in tasks if not(str(item["id"]) in id)]

    write_task(tasks_new)

# --------------------------------

root = tk.Tk()


# получение данных
window_config = get_config()

root.title(window_config["title"])
root.resizable(False, False)
root.geometry(f"{window_config["width"]}x{window_config["hight"]}+{window_config["pothicion_x"]}+{window_config["pothicion_y"]}")

# действие на закрытие 
root.protocol("WM_DELETE_WINDOW", on_closing)


Lable = tk.Label(root, text="I am Daulet", borderwidth=2, relief='solid', padx=10, pady=10)
Lable.pack(anchor="n", fill=X)



frame_left = tk.Frame(root, borderwidth=2, relief='groove', padx=10, pady=10, width=600)
frame_left.pack(side=tk.LEFT, fill=Y)
frame_left.grid_columnconfigure(0, minsize=50,weight=1)
frame_left.grid_columnconfigure(1, minsize=400,weight=10)
frame_left.grid_columnconfigure(2, minsize=150,weight=1)

draw_task()



frame_right = tk.Frame(root, borderwidth=2, relief='groove', width=200)
frame_right.pack(side=tk.LEFT, fill=Y)

# Создание кнопак
frame_right_button = tk.Frame(frame_right, borderwidth=2, relief='groove', padx=10, pady=10, width=200)
frame_right_button.pack(side=tk.TOP, fill=Y)

add_button = tk.Button(frame_right_button, borderwidth=2, relief='groove', padx=5, pady=5, text="Add task", width=8, height=1, command=create_add_window)
delate_button = tk.Button(frame_right_button, borderwidth=2, relief='groove', padx=5, pady=5, text="Delate task", width=8, height=1, command=delate_tasks)

add_button.pack(side=tk.LEFT)
delate_button.pack(side=tk.LEFT)


# Создание показании статус
frame_right_status = tk.Frame(frame_right, borderwidth=2, relief='groove', padx=10, pady=10, width=200)
frame_right_status.pack(side=tk.TOP, fill=X)
draw_status()


# Создание выбора отображения
frame_right_select = tk.Frame(frame_right, borderwidth=2, relief='groove', padx=10, pady=10, width=200)
frame_right_select.pack(side=tk.TOP, fill=X)


position = {"padx":6, "pady":6, "anchor":NW}
status = StringVar(value="ALL")

btn_all = tk.Radiobutton(frame_right_select, text="ALL", value="ALL", variable=status, command=lambda statuss="ALL": btn_all_change() )
btn_all.pack(**position)
  
btn_done = tk.Radiobutton(frame_right_select, text="Done", value="done", variable=status, command=lambda statuss="done": btn_done_change())
btn_done.pack(**position)
 
btn_progres = tk.Radiobutton(frame_right_select, text="Progres", value="progres", variable=status, command=lambda statuss="progres": btn_progres_change())
btn_progres.pack(**position)



root.mainloop()