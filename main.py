from TaskGUI import Taskapp
import tkinter as tk
 
root = tk.Tk()

app = Taskapp(root)


with open("tasks.txt", 'r') as file:
    for line in file:
        app.task_list.append(line.strip())
    
for item in app.task_list:
    app.task_listbox.insert(tk.END, item)
        
root.mainloop()

    
    


