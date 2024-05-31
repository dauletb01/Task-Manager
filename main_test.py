import tkinter as tk
from tkinter import *
import json

config_file_name = "config.json"
task_file_name = "task.json"


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

def write_task(task_data):

    with open(task_file_name, "w", encoding="utf-8") as file:
        json.dump(task_data, file)

    return task_data

def checkbutton_changed(id):
    tasks = get_task()

    for task in tasks:
        if task["id"] == id: 
            task["status"] = not(task["status"])
            break
    
    write_task(tasks)
    task_draw()


def task_draw():

    for widget in frame_left.winfo_children():
        widget.destroy()

    tasks = get_task()

    i = 0
    for task in tasks:
        
        enabled = IntVar()
        number=tk.Label(frame_left, text=f"{task["id"]}", borderwidth=2, relief='solid',padx=10, pady=10)
        text=tk.Label(frame_left, text=f"{task["task"]}", borderwidth=2, relief='solid',padx=10, pady=10, justify=tk.LEFT)
        # status = tk.Checkbutton(frame_left, text= "Done" if task["status"] else "In progress" , borderwidth=2, variable=enabled, command=checkbutton_changed(task["id"]), relief='solid', padx=10, pady=10)
        status = tk.Checkbutton(frame_left, text="Done" if task['status'] else "In progress", borderwidth=2, variable=enabled, command=lambda task_id=task['id']: checkbutton_changed(task_id), relief='solid', padx=10, pady=10)


        number.grid(row=i, column=0, sticky='nsew')
        text.grid(row=i, column=1, sticky='nsew')
        status.grid(row=i, column=2, sticky='nsew')

        i+=1

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

task_draw()



frame_right = tk.Frame(root, borderwidth=2, relief='groove', width=200)
frame_right.pack(side=tk.LEFT, fill=Y)

frame_right_button = tk.Frame(frame_right, borderwidth=2, relief='groove', padx=10, pady=10, width=200)
frame_right_button.pack(side=tk.TOP, fill=Y)

add_button = tk.Button(frame_right_button, borderwidth=2, relief='groove', padx=5, pady=5, text="Add task", width=8, height=1)
delate_button = tk.Button(frame_right_button, borderwidth=2, relief='groove', padx=5, pady=5, text="Delate task", width=8, height=1)


add_button.pack(side=tk.LEFT)
delate_button.pack(side=tk.LEFT)


frame_right_status = tk.Frame(frame_right, borderwidth=2, relief='groove', padx=10, pady=10, width=200)
frame_right_status.pack(side=tk.TOP, fill=X)

lable_done = tk.Label(frame_right_status, text=f"Done:", font=("Arial", 10, 'bold'))
lable_done.pack( side=tk.LEFT, fill=Y)
lable_done_count = tk.Label(frame_right_status, text=f"2", font=("Arial", 10, 'bold'))
lable_done_count.pack(side=tk.LEFT, fill=Y)


lable_progres = tk.Label(frame_right_status, text=f"In progres:", font=("Arial", 10, 'bold'))
lable_progres.pack( side=tk.LEFT, fill=Y)
lable_progres_count = tk.Label(frame_right_status, text=f"1", font=("Arial", 10, 'bold'))
lable_progres_count.pack( side=tk.LEFT, fill=Y)

root.mainloop()