import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

def update_date_time(self):
    current_date = datetime.now().strftime("%m-%d-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    self.LB_date.config(text=f"Date: {current_date}")
    self.LB_time.config(text=f"Time: {current_time}")

    self.master.after(1000, lambda: update_date_time(self))

def update_tasks(self):
    self.Task_box.delete(0, tk.END)
    for task in self.task_list:
        self.Task_box.insert(tk.END, task)

    
def load_tasks(self):
    try:
        with open("tasks.txt", 'r') as file:
            self.task_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        messagebox.showwarning("Warning", "tasks.txt not found. Starting with an empty task list.")
    update_tasks(self)

def check_file_modification(self):
    try:
        current_modified_time = os.path.getmtime("tasks.txt")
        if current_modified_time != self.last_modified_time:
            self.last_modified_time = current_modified_time
            load_tasks(self)
    except FileNotFoundError:
        pass

    self.master.after(1000, lambda: check_file_modification(self))
