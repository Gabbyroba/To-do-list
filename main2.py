from tkinter import *

root = Tk()
root.title("To-Do List")

tasks = []

def add_task():
    task = task_entry.get()
    tasks.append(task)
    update_listbox()

def delete_task():
    task = listbox.get(ANCHOR)
    tasks.remove(task)
    update_listbox()

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

task_entry = Entry(root, width=30)
task_entry.pack(pady=10)

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

listbox = Listbox(root, width=50)
listbox.pack()

root.mainloop()
