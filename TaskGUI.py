from TaskGUI_functions import *
class Taskapp:
    def __init__(self, master):
        color_primary = "LightGrey"
        color_secondary = "White"

        # APP SPECIFIC INFO
        self.master = master
        master.title("TaskForge")
        master.configure(bg=color_primary)
        master.geometry("1000x700")
        self.task_list = []

        # The Header
        self.heading_frame = tk.Frame(master, bg=color_secondary)
        
        self.LB_title = tk.Label(self.heading_frame, text="TaskForge", font=("Impact", 34, "bold"), bg=color_secondary, width=30)
        self.LB_title.grid(row=0, column=1)

        self.LB_date = tk.Label(self.heading_frame, text="Date", font=("Helvetica", 14), bg=color_primary)
        self.LB_date.grid(row=1, column=0, sticky="w")

        self.LB_time = tk.Label(self.heading_frame, text="Time", font=("Helvetica", 14), bg=color_primary)
        self.LB_time.grid(row=1, column=2, sticky="e")

        self.heading_frame.grid_columnconfigure(0, weight=1)
        self.heading_frame.grid_columnconfigure(1, weight=1)
        self.heading_frame.grid_columnconfigure(2, weight=1)

        self.heading_frame.pack(fill='x')
        update_date_time(self)

        # Main Body - shows current task
        self.curr_frame = tk.Frame(master, bg=color_primary)
        
        self.curr_task = tk.Label(self.curr_frame, text="Current Task:", font=("Impact", 20), bg=color_primary)
        self.curr_task.grid(row=0, column=0, sticky="nsew")

        self.first_task = tk.Label(self.curr_frame, text="<Placeholder Texts Until Tasks are Appended>", bg=color_secondary, font=("Impact", 16), pady= 5)
        self.first_task.grid(row=1, column=0)

        self.time_left = tk.Label(self.curr_frame, text="Time Left:", font=("Impact", 20), bg=color_primary)
        self.time_left.grid(row=2,column=0)

        self.task_time_left = tk.Label(self.curr_frame, text="<Curr time - Timestamp>", bg=color_secondary, font=("Impact", 16), pady= 5, padx= 5)
        self.task_time_left.grid(row=3, column= 0)

        self.curr_frame.grid_columnconfigure(0, weight=1)
        self.curr_frame.grid_rowconfigure(0, weight=1)
        self.curr_frame.grid_rowconfigure(1, weight=1)
        self.curr_frame.grid_rowconfigure(2, weight=1)
        self.curr_frame.grid_rowconfigure(3, weight=1)
        
        self.curr_frame.pack(fill="x")
        
        # Shows tasks
        self.task_frame = tk.Frame(master, bg=color_primary,padx=20)

        self.task_frame.grid_rowconfigure(0, weight=1)
        self.task_frame.grid_rowconfigure(1, weight=1)
        self.task_frame.grid_columnconfigure(0, weight=1)
        self.task_frame.grid_columnconfigure(1, weight=1)

        self.task_box = tk.Listbox(self.task_frame, background=color_secondary, font=("Helvetica", 16), height=3)
        self.task_box.grid(row=0, column=0, columnspan= 2, sticky='nsew')


        self.BT_add_task = tk.Button(self.task_frame, text="Add Task", height=2, command= lambda: show_task_creation(self))
        self.BT_add_task.grid(row=1, column=0, sticky='nsew')
        self.BT_rm_task = tk.Button(self.task_frame,text="Remove Task", height=2, command= lambda: remove_tasks(self))
        self.BT_rm_task.grid(row=1, column=1, sticky='nsew')
        self.task_frame.pack(fill='x')

        # Add Tasks Menu
        self.add_task_frame = tk.Frame(master, bg=color_primary)

        self.LB_description = tk.Label(self.add_task_frame, text="Description:", font=("Impact", 16))
        self.E_description = tk.Text(self.add_task_frame, height=3, padx=40)  # Added height for better visibility

        self.LB_due_date = tk.Label(self.add_task_frame, text="Time Due:", font=("Impact", 16))
        self.E_due_date = tk.Entry(self.add_task_frame)

        self.BT_submit = tk.Button(self.add_task_frame, text="Submit", command= lambda: submit_task(self))
        self.BT_cancel = tk.Button(self.add_task_frame, text="Cancel", command= lambda: hide_task_creation(self))

        self.LB_description.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.E_description.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.LB_due_date.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.E_due_date.grid(row=3, column=0, columnspan=2, sticky='nsew')
        self.BT_submit.grid(row=4, column=0, sticky='nsew')
        self.BT_cancel.grid(row=4, column=1, sticky='nsew')

        self.add_task_frame.grid_rowconfigure(0, weight=1)
        self.add_task_frame.grid_rowconfigure(1, weight=1)
        self.add_task_frame.grid_rowconfigure(2, weight=1)
        self.add_task_frame.grid_rowconfigure(3, weight=1)
        self.add_task_frame.grid_rowconfigure(4, weight=1)
        self.add_task_frame.grid_rowconfigure(4, weight=1)
        self.add_task_frame.grid_columnconfigure(0, weight=1)
        self.add_task_frame.grid_columnconfigure(1, weight=1)
      

        # Additional Functionality
        self.last_frame = tk.Frame(master, bg=color_primary)
        self.last_frame.pack(fill="both", expand=True)

        self.BT_exit = tk.Button(self.last_frame, text="Exit", command=master.destroy, height=2, width=10, bg="red", fg="white", font=("Helvetica", 12, "bold"))
        self.BT_exit.pack(side="bottom", anchor="se", padx=20, pady=20)

        self.last_frame.pack_propagate(False) 

        curr_task(self)
