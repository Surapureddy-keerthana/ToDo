import tkinter as tk
from tkinter import messagebox

# --- Functions ---
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(True, True)

# Configure grid weights for responsiveness
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# --- Entry Box ---
entry = tk.Entry(root, font=("Helvetica", 14))
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# --- Listbox with Scrollbar ---
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, font=("Helvetica", 12), yscrollcommand=scrollbar.set, selectbackground="#8ecae6")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# --- Buttons ---
btn_add = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=add_task,
                    bg="#219ebc", fg="white", relief="raised", bd=5)
btn_add.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

btn_delete = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task,
                       bg="#ffb703", fg="black", relief="ridge", bd=5)
btn_delete.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

root.mainloop()
