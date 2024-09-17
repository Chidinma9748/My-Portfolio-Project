#!/usr/bin/python3
""This contains the bulk of actions for the planner involves adding,opening,saving and loading tasks""
import json
from datetime import datetime

PLANNER_FILE =  "my_planner_data.json"

def load_tasks():
    if not os.path.exists(PLANNER_FILE):
        return []
    with open(PLANNER_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(PLANNER_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    task = {
        "title": title,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} (Due: {task['due_date']}, Created: {task['created_at']})")

def delete_task():
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    task_index = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' deleted successfully!")
    else:
        print("Invalid task number.")

