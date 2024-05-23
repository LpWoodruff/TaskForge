import tkinter as tk
from tkinter import messagebox
from datetime import datetime



class Taskapp:
    def __init__(self,master):
        # APP SPECIFIC INFO
        self.master = master
        master.title("TaskForge")
        master.configure(bg="White")
        
        master.geometry("600x500")
        self.task_list = []

    #Header Frame
        self.header_frame = tk.Frame(
            master, 
            bg="Grey",
            bd=2,
            border=1,
            relief=tk.SOLID
            )
        self.header_frame.pack(fill=tk.X)

        self.LB_title = tk.Label(
            self.header_frame, 
            bg="White",
            fg="Black",
            border=1, 
            relief=tk.SOLID,
            text="TaskForge", 
            font=("Impact", 36))
        self.LB_title.pack(side=tk.TOP)

        self.LB_date = tk.Label(
            self.header_frame, 
            background="Darkgrey", 
            text=" ",  
            font=("Impact", 20))
        self.LB_date.pack(side=tk.RIGHT)

        self.LB_time = tk.Label(
            self.header_frame, 
            background="Darkgrey", 
            text=" ",  
            font=("Impact", 20))
        self.LB_time.pack(side=tk.LEFT)
        
        

        #Controls Frame
        self.controls_frame = tk.Frame(
            master, 
            pady= 10,
            )
        self.controls_frame.pack(fill=tk.BOTH)

        self.BT_create_task = tk.Button(
            self.controls_frame,
            text="Create Task",
            command=self.create_task)
        self.BT_create_task.pack(side=tk.LEFT)

        self.BT_remove_task = tk.Button(
            self.controls_frame,
            text="Remove Task")
        self.BT_remove_task.pack(side=tk.LEFT)

        self.BT_quit = tk.Button(
            self.controls_frame,
            text="Quit",
            command= self.master.destroy)
        self.BT_quit.pack(side=tk.RIGHT)

        #Task Creation Frame
        self.creation_frame = tk.Frame(
            master, 
            bg="DarkGrey",
            border=1,
            relief=tk.SOLID,
            padx=25, pady=25)

        self.LB_description = tk.Label(
            self.creation_frame,
            text="Description:")
        self.LB_description.pack(anchor=tk.CENTER)

        self.description_entry = tk.Text(
            self.creation_frame, 
            height=2)
        self.description_entry.pack(anchor= tk.CENTER)

        self.LB_due_date = tk.Label(
            self.creation_frame, 
            text="Due Date:")
        self.LB_due_date.pack(anchor=tk.CENTER)

        self.date_entry = tk.Entry(self.creation_frame)
        self.date_entry.pack(anchor=tk.CENTER)

        self.BT_submit = tk.Button(self.creation_frame, text="Submit")
        self.BT_submit.pack(anchor=tk.CENTER)
        
        self.BT_cancel = tk.Button(self.creation_frame, text="Cancel", command=self.cancel_button)
        self.BT_cancel.pack(anchor=tk.CENTER)

        #Task List Frame
        self.task_frame = tk.Frame(master, bg="Grey")
        self.task_frame.pack(fill=tk.X)

        self.task_listbox = tk.Listbox(self.task_frame, bg="White")
        self.task_listbox.pack(fill=tk.BOTH)

        self.update_time_date()

    def update_time_date(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        self.LB_time.config(text=current_time)
        self.LB_date.config(text=current_date)
        self.master.after(1000, self.update_time_date)

    def create_task(self):
        self.creation_frame.pack(fill=tk.BOTH, anchor=tk.CENTER)

    def cancel_button(self):
        self.creation_frame.pack_forget()
        