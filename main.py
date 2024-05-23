
from TaskGUI import Taskapp
import tkinter as tk
 


root = tk.Tk()
app = Taskapp(root)

# Opens the tasks and inserts them into the application
with open("tasks.txt", "r") as file:
    for line in file:
        task = line
        app.task_list.append(task)



def append_task():
    task_number = len(app.task_list) + 1
    task = input("Description: ")
    due_date = input("Due date?: ")
    with open("tasks.txt", "a") as file:
        file.write(f"{task_number}: {task} <{due_date}>\n")
        

app.update_tasks()
app.update_time()
root.mainloop()

    
    


