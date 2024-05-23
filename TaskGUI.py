import tkinter as tk
from tkinter import messagebox
import datetime



class Taskapp:
    def __init__(self,master):
        # APP SPECIFIC INFO
        self.master = master
        master.title("TaskForge")
        self.task_list = []

        #Title of the application
        self.LB_title = tk.Label(master, text = "TaskForge", font=("Helvetica", 20))
        self.LB_title.pack()

        self.LB_description = tk.Label(master, text="What would you like to do?:")
        self.LB_description.pack()

        #Updates the label with crurent time constantly
        self.LB_time = tk.Label(master, text = '')
        self.LB_time.pack()
        
       
        # Application functionality using buttons
        self.BT_new_task = tk.Button(master, text="New Task", command= self.create_tast)
        self.BT_new_task.pack()

        self.BT_close_tasks = tk.Button(master, text="Close Task Menu", command = self.close_task)
        
      
        # List for tasks
        self.task_listbox = tk.Listbox(master, width=100, height=20, font=("Helvetica", 20))
        self.BT_view_tasks = tk.Button(master, text="View Tasks", command= self.view_tasks)
        self.BT_view_tasks.pack()

        self.LB_task_num = tk.Label(master, text = ' ')
        self.task_description = tk.Entry(master)
        self.BT_submit = tk.Button(master, text="Submit")
        self.BT_cancel = tk.Button(master, text="Cancel", command=self.cancel_new)



        self.initialize_tasklist()
        self.update_time()


    def initialize_tasklist(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task = line.strip()  
                    if task:  
                        self.task_list.append(task)
                        print(f"Appended task: {task}")  
        except FileNotFoundError:
            # If "tasks.txt" is not found, create a new file and inform the user
            with open("tasks.txt", "w"):
                messagebox.showinfo("New File Created", "A new 'tasks.txt' file was created.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # This updates time for the application
    def update_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.LB_time.config(text=current_time)
        self.master.after(1000, self.update_time)


    def create_tast(self):
        task_num = len(self.task_list) + 1
        self.LB_task_num.config(text=f"Task Number: {task_num}")
        

        self.BT_view_tasks.pack_forget()
        self.BT_new_task.pack_forget()
        self.LB_task_num.pack()
        self.task_description.pack()
        self.BT_submit.pack()
        self.BT_cancel.pack()


    # This allows the button to view each task appended.
    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for tasks in self.task_list:
            self.task_listbox.insert(tk.END, tasks)
        self.BT_view_tasks.pack_forget()
        self.BT_new_task.pack_forget()
        self.BT_close_tasks.pack()
        self.task_listbox.pack()
        

    # Closes task menu
    def close_task(self):
        self.BT_new_task.pack()
        self.BT_view_tasks.pack()
        self.BT_close_tasks.pack_forget()
        self.task_listbox.pack_forget()
        self.task_listbox.delete(0, tk.END)

    def cancel_new(self):
        self.LB_task_num.pack_forget()
        self.task_description.pack_forget()
        self.BT_submit.pack_forget()
        self.BT_cancel.pack_forget()
        self.BT_new_task.pack()
        self.BT_view_tasks.pack()
        