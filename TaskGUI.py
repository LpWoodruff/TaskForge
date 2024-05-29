from task_methods import *

class Taskapp:
    def __init__(self, master):
        # APP SPECIFIC INFO
        self.master = master
        master.title("TaskForge")
        master.configure(bg="White")
        master.geometry("1000x700")
        self.task_list = []
        self.last_modified_time = 0
        
        self.heading_frame = tk.Frame(master, bg="red")
        
        self.LB_title = tk.Label(self.heading_frame, text="TaskForge", font=("Helvetica", 24, "bold"), bg="White")
        self.LB_title.grid(row=0, column=1, pady=(10, 20))

        self.LB_date = tk.Label(self.heading_frame, text="Date", font=("Helvetica", 14), bg="White")
        self.LB_date.grid(row=1, column=0, padx=(20, 10), sticky="w")

        self.LB_time = tk.Label(self.heading_frame, text="Time", font=("Helvetica", 14), bg="White")
        self.LB_time.grid(row=1, column=2, sticky="e")

        self.heading_frame.grid_columnconfigure(0, weight=1)
        self.heading_frame.grid_columnconfigure(1, weight=1)
        self.heading_frame.grid_columnconfigure(2, weight=1)

        self.heading_frame.pack(fill='x')
    
        update_date_time(self)

        # Main Body - shows tasks
        self.task_frame = tk.Frame(master, bg="white")
        self.task_frame.pack(fill='x', expand=True)

        self.task_frame.grid_rowconfigure(0, weight=1)
        self.task_frame.grid_columnconfigure(0, weight=1)

        self.Task_box = tk.Listbox(self.task_frame, background="red")
        self.Task_box.grid(row=0, column=0, sticky='nsew')



        self.functionality_frame = tk.Frame(master, bg="white")
        self.functionality_frame.pack(fill='both', expand=True, pady=20)
        
        self.BT_add_task = tk.Button(self.functionality_frame, text="Add Task")
        self.BT_remove_task = tk.Button(self.functionality_frame, text="Remove Task")
        self.BT_add_task.grid(row=0, column=0, sticky="e")
        self.BT_remove_task.grid(row=0, column=1, sticky="e")


        load_tasks(self)
        update_tasks(self)
        check_file_modification(self)  # Start checking for file modifications

