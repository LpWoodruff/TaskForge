import tkinter as tk
from tkinter import messagebox
import datetime

class Taskapp:
    def __init__(self,master):
        self.master = master

        master.title("TaskForge")
        master.frame = tk.Frame(master)

        self.task_list = []

        self.time_label = tk.Label(master, text = '')
        self.time_label.pack()
        
        self.title_label = tk.Label(master, text = "TaskForge", font=("Helvetica", 20))
        self.title_label.pack()
        
        self.task_label = tk.Label(master, text="What would you like to do?:")
        self.task_label.pack()

        self.task_button = tk.Button(master, text="New Task")
        self.task_button.pack()
        
        self.task_button = tk.Button(master, text="View Tasks")
        self.task_button.pack()


        self.task_listbox = tk.Listbox(master, width=50, height=20)

    def update_tasks(self):
        for tasks in self.task_list:
            self.task_listbox.insert(tk.END, tasks)
        
        self.task_listbox.pack()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=current_time)
        # Schedule the update_time method to be called again after 1000 milliseconds (1 second)
        self.master.after(1000, self.update_time)

    