from tkinter import *

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        pass

root = Tk()
root.title("My To-Do List")
root.geometry("400x400")  # Changed window size

# Background color to Midnight Blue
root.configure(bg="#6A5ACD")

# Status Title Label
status_label = Label(root, text="To-Do List Application", font=("Helvetica", 16, "bold"), bg="#4682B4", fg="white")
status_label.pack(pady=15)

# Widgets
entry = Entry(root, width=30)
addButton = Button(root, text="Add Task", bg="#008080", fg="white", command=add_task)
listbox = Listbox(root, width=50)
delButton = Button(root, text="Delete Task", bg="#B22222", fg="white", command=delete_task)

# Made by Onkar label
made_by_label = Label(root, text="Made by Onkar", font=("Arial", 10), bg="#191970", fg="white")
made_by_label.pack(side=BOTTOM, pady=10)

# GUI Layout with separation
entry.pack(pady=10)
addButton.pack(pady=5)
listbox.pack(pady=10)
delButton.pack(pady=5)

root.mainloop()
