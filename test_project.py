from project import add_task, \
    create_task_table, delete_task, edit_task, view_tasks

import sqlite3
import pytest
import datetime


def test_create_task_table():
    create_task_table()
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
    result = c.fetchone()
    assert result[0] == 'tasks'
    conn.close()

def test_add_task():
    add_task("Task 1", "This is task 1", "2023-03-30", 1)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    result = c.fetchone()
    assert result[1] == 'Task 1'
    assert result[2] == 'This is task 1'
    assert result[3] == '2023-03-30'
    assert result[4] == 1
    conn.close()

def test_delete_task():
    add_task("Task 1", "This is task 1", "2023-03-30", 1)
    task_id = 1
    delete_task(task_id)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    result = c.fetchone()
    assert result is None
    conn.close()

def test_edit_task():
    add_task("Task 1", "This is task 1", "2023-03-30", 1)
    task_id = 1
    edit_task(task_id, "New Task Name", "New Task Description", "2023-04-01", 2)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    result = c.fetchone()
    assert result[1] == 'New Task Name'
    assert result[2] == 'New Task Description'
    assert result[3] == '2023-04-01'
    assert result[4] == 2
    conn.close()

def test_view_tasks():
    add_task("Task 1", "This is task 1", "2023-03-30", 1)
    add_task("Task 2", "This is task 2", "2023-04-01", 2)
    tasks = view_tasks()
    assert len(tasks) == 2
    assert tasks[0][1] == 'Task 1'
    assert tasks[1][1] == 'Task 2'
