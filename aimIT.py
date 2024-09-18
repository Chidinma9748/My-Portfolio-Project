#!/usr/bin/python3
# This contains the bulk of actions for the planner involves adding,opening,saving and loading tasks
import os
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
    name = input("Enter task name: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    task = {
        "name": name,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task '{}' added successfully!".format(name))

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, start=1):
        print("{index}. {name} (Due: {due_date}, Created: {created_at})".format(
    index=index,
    name=task['name'],
    due_date=task['due_date'],
    created_at=task['created_at']
))


def delete_task():
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    task_index = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print("Task '{}' added successfully!".format(name))

    else:
        print("Invalid task number.")

