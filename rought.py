import tkinter as tk
import sqlite3

def create_task_table():
    my_tasks = sqlite3.connect('tasklist.db')
    c = my_tasks.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mytasks
                (id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                description TEXT,
                start_date DATE,
                due_date DATE,
                priority INTEGER)''')
    my_tasks.commit()
    my_tasks.close()

def add_task(name, description, start_date, due_date, priority):
    my_tasks = sqlite3.connect('tasklist.db')
    c = my_tasks.cursor()
    c.execute("INSERT INTO mytasks (name, description, start_date, due_date, priority) VALUES (?, ?, ?, ?, ?)", (name, description, start_date, due_date, priority))
    my_tasks.commit()
    my_tasks.close()

def delete_task(id):
    my_tasks = sqlite3.connect('tasklist.db')
    c = my_tasks.cursor()
    c.execute("DELETE FROM mytasks WHERE id=?", (id,))
    my_tasks.commit()
    my_tasks.close()

def edit_task(id, name, description, start_date, due_date, priority):
    my_tasks = sqlite3.connect('tasklist.db')
    c = my_tasks.cursor()
    c.execute("UPDATE mytasks SET name=?, description=?, start_date=?, due_date=?, priority=? WHERE id=?", (name, description, start_date, due_date, priority, id))
    my_tasks.commit()
    my_tasks.close()

def view_task():
    my_tasks = sqlite3.connect('tasklist.db')
    c = my_tasks.cursor()
    c.execute("SELECT * FROM mytasks")
    mytasks = c.fetchall()
    my_tasks.close()
    return mytasks

def main():
    create_task_table()

    # Create window
    window = tk.Tk()
    window.title("DailyTasks")

    # Create widgets
    label = tk.Label(window, text="Welcome, I am here to help you manage your tasks with Deadlines and Reminders. YOU CAN DO IT!! :)")
    label.pack()

    # Create task name
    name_label = tk.Label(window, text="Write our new task name :3: ")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    # Create task details
    description_label = tk.Label(window, text="Let's keep some details of the task to help us remember!")
    description_label.pack()
    description_entry = tk.Entry(window)
    description_entry.pack()

    # Create start_date
    start_date_label = tk.Label(window, text="Let's set up a start date O.O")
    start_date_label.pack()
    start_date_entry = tk.Entry(window)
    start_date_entry.pack()

    # Create due_date
    due_date_label = tk.Label(window, text="Let's set up a due date")
    due_date_label.pack()
    due_date_entry = tk.Entry(window)
    due_date_entry.pack()

    # Create priority
    priority_label = tk.Label(window, text="Let's set up the priority of the task")
    priority_label.pack()
    priority_entry = tk.Entry(window)
    priority_entry.pack()

    # Create Add button
    add_button = tk.Button(window, text="Add New Task", command=lambda: add_task(name_entry.get(), description_entry.get(), start_date_entry.get(), due_date_entry.get(), priority_entry.get()))
    add_button.pack()
    
    # Create View button
    view_button = tk.Button(window,text="View All Tasks", command=lambda: print(view_task()))
    view_button.pack()

    # Create delete button
    delete_button = tk.Button(window, text="Delete task", command=lambda:delete_task(1))  # Set up 1 to replace it with the actual task ID
    delete_button.pack()

    # Create Edit button
    edit_button = tk.Button(window, text="Edit task", command=lambda:edit_task(1, "New Name", "New Description", "New Start Date", "New Due Date", "New Priority"))
    edit_button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()