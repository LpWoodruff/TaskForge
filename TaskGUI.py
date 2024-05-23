import tkinter as tk
from tkinter import messagebox
import datetime



class Taskapp:
    def __init__(self,master):
        # APP SPECIFIC INFO
        self.master = master
        master.title("TaskForge")
        master.configure(bg="Grey")
        self.task_list = []
        master.geometry("600x500")

        #Title of the application
        self.main_frame = tk.Frame(master, background="Red")
        self.LB_title = tk.Label(self.main_frame, text = "TaskForge", font=("Impact", 36), background="Red")
        self.LB_title.pack()
        self.LB_time2 = tk.Label(self.main_frame, text = '', background="Red", font=("Impact", 20))
        self.LB_time = tk.Label(self.main_frame, text = '', background="Red", font=("Impact", 20))
        self.LB_time.pack()
        self.LB_time2.pack()
        #Updates the label with crurent time constantly
        

        self.main_frame.pack(fill=tk.X)
        
        #The main menu Frame
        self.menu_frame = tk.Frame(master, background="DarkGrey")
        ## its elements
        self.LB_description = tk.Label(self.menu_frame, text="What would you like to do?", font=("Helvetica", 20), background="DarkGrey")
        self.LB_description.pack()
        self.BT_new_task = tk.Button(self.menu_frame, text="New Task", command= self.create_task)
        self.BT_view_tasks = tk.Button(self.menu_frame, text="View Tasks", command= self.view_tasks)
        self.BT_new_task.pack()
        self.BT_view_tasks.pack()

        #The View Tasks Frame
        self.view_task_frame = tk.Frame(master, background="DarkGrey")
        ## its elements
        self.BT_close_tasks = tk.Button(self.view_task_frame, text="Close Task Menu", command = self.close_task)
        self.task_listbox = tk.Listbox(self.view_task_frame, width=100, height=20, font=("Helvetica", 20), background="Red")
        self.BT_close_tasks.pack()
        self.task_listbox.pack()
    
       
        # The New Tasks frame
        self.new_task_frame = tk.Frame(master, background="DarkGrey")
        ## its elements
        self.LB_task_num = tk.Label(self.new_task_frame, text = ' ', font=("Helvetica", 20), background="Red")
        self.LB_task_description = tk.Label(self.new_task_frame, text = 'Description:', font=("Helvetica", 20), background="DarkGrey")
        self.task_description = tk.Text(self.new_task_frame, width=100, height=5)
        self.BT_submit = tk.Button(self.new_task_frame, text="Submit", width=100, background="Red")
        self.BT_cancel = tk.Button(self.new_task_frame, text="Cancel", command=self.cancel_new, width=100, background="Red")
        
        
        self.LB_task_num.pack()
        self.LB_task_description.pack()
        self.task_description.pack()
        self.BT_submit.pack()
        self.BT_cancel.pack()

        self.menu_frame.pack(fill=tk.BOTH)
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
        current_date = datetime.datetime.now().strftime("%m-%d-%Y")
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.LB_time.config(text=current_date)
        self.LB_time2.config(text=current_time)
        self.master.after(1000, self.update_time)


    def create_task(self):
        task_num = len(self.task_list) + 1
        self.LB_task_num.config(text=f"Task Number: {task_num}")
        

        self.new_task_frame.pack(fill=tk.BOTH)
        self.menu_frame.pack_forget()


    # This allows the button to view each task appended.
    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for tasks in self.task_list:
            self.task_listbox.insert(tk.END, tasks)
        self.view_task_frame.pack()
        self.menu_frame.pack_forget()

    # Closes task menu
    def close_task(self):
        self.view_task_frame.pack_forget()
        self.menu_frame.pack(fill=tk.BOTH)

    def cancel_new(self):
       self.new_task_frame.pack_forget()
       self.menu_frame.pack(fill=tk.BOTH)
        