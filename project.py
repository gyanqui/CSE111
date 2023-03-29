import tkinter as tk
import sqlite3

def create_task_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  description TEXT,
                  due_date DATE,
                  priority INTEGER)''')
    conn.commit()
    conn.close()

def add_task(name, description, due_date, priority):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (name, description, due_date, priority) VALUES (?, ?, ?, ?)", (name, description, due_date, priority))
    conn.commit()
    conn.close()

def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()

def edit_task(id, name, description, due_date, priority):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET name=?, description=?, due_date=?, priority=? WHERE id=?", (name, description, due_date, priority, id))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

def main():
    create_task_table()

    # Create a window
    window = tk.Tk()
    window.title("To-Do List Manager")

    # Create widgets
    label = tk.Label(window, text="Welcome to your To-Do List Manager!")
    label.pack()

    name_label = tk.Label(window, text="Task Name:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    description_label = tk.Label(window, text="Task Description:")
    description_label.pack()
    description_entry = tk.Entry(window)
    description_entry.pack()

    due_date_label = tk.Label(window, text="Due Date:")
    due_date_label.pack()
    due_date_entry = tk.Entry(window)
    due_date_entry.pack()

    priority_label = tk.Label(window, text="Priority:")
    priority_label.pack()
    priority_entry = tk.Entry(window)
    priority_entry.pack()

    add_button = tk.Button(window, text="Add Task", command=lambda: add_task(name_entry.get(), description_entry.get(), due_date_entry.get(), priority_entry.get()))
    add_button.pack()

    view_button = tk.Button(window, text="View Tasks", command=lambda: print(view_tasks()))
    view_button.pack()

    delete_button = tk.Button(window, text="Delete Task", command=lambda: delete_task(1)) # Replace 1 with the actual task ID
    delete_button.pack()

    edit_button = tk.Button(window, text="Edit Task", command=lambda: edit_task(1, "New Name", "New Description", "New Due Date", "New Priority")) # Replace 1 with the actual task ID and update the values
    edit_button.pack()

    # Run the window
    window.mainloop()

if __name__ == '__main__':
    main()