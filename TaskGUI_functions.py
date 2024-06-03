import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import os

def update_date_time(self):
    current_date = datetime.now().strftime("%m-%d-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    self.LB_date.config(text=f"Date: {current_date}")
    self.LB_time.config(text=f"Time: {current_time}")

    self.master.after(1000, lambda: update_date_time(self))

def show_task_creation(self):
    self.last_frame.pack_forget()
    self.add_task_frame.pack(fill="x", padx= 130, pady=20)
    self.last_frame.pack(fill="both", expand=True)

def hide_task_creation(self):
    self.add_task_frame.pack_forget()

def submit_task(self):
    description = self.E_description.get("1.0", tk.END).strip() 
    due_date = self.E_due_date.get().strip() 
    task_num = len(self.task_list) + 1
    task = {
        "task_num": task_num,
        "description": description,
        "due_date": due_date}
    self.task_list.append(task)
        
    print(f"Number: {task_num}")
    print(f"Description: {description}")
    print(f"Due Date: {due_date}")
    
    self.E_description.delete("1.0", tk.END)
    self.E_due_date.delete(0, tk.END)
        
    update_tasks(self)
    hide_task_creation(self)

def update_tasks(self):
    self.task_box.delete(0, tk.END)
        
    for task in self.task_list:
        task_description = f"Task {task['task_num']}: {task['description']} (Due: {task['due_date']})"
        self.task_box.insert(tk.END, task_description)

def remove_tasks(self):
    try:
        selected_task = self.task_box.curselection()[0]
        self.task_box.delete(selected_task)
        del self.task_list[selected_task]
    except IndexError:
        messagebox.showwarning("Selection Error", "There are Currently No Tasks Selected.")
 
def curr_task(self):
    if self.task_list:
        first_task = self.task_list[0]
        self.first_task.config(text=f"{first_task['description']}")

        due_time_str = first_task['due_date']
        try:
            due_time = datetime.strptime(due_time_str, '%H:%M:%S').time()
            now = datetime.now()
            current_time = now.time()

            if due_time > current_time:
                time_left = datetime.combine(now.date(), due_time) - datetime.combine(now.date(), current_time)
            else:
                time_left = datetime.combine(now.date() + timedelta(days=1), due_time) - datetime.combine(now.date(), current_time)

            seconds = time_left.total_seconds()
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            seconds = int(seconds % 60)
            self.task_time_left.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        except ValueError:
            self.task_time_left.config(text="Invalid due time format. Use HH:MM:SS")
    else:
        self.first_task.config(text=" No tasks available.")
        self.task_time_left.config(text="No tasks available.")

    remove_expired_tasks(self)
    update_tasks(self)

    self.master.after(1000, lambda: curr_task(self))

def remove_expired_tasks(self):
    now = datetime.now()
    for task in self.task_list[:]:
        due_time_str = task['due_date']
        try:
            due_time = datetime.strptime(due_time_str, '%H:%M:%S').time()
            current_time = now.time()

            if due_time < current_time:
                self.task_list.remove(task)
                messagebox.showinfo("Task Expired", f"Task '{task['description']}' has expired.")
        except ValueError:
            continue