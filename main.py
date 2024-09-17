#!/usr/bin/python3

from newpage import newpage
from aimIT import add_task, view_tasks, delete_task, load_tasks, save_tasks


def main_menu():
    while True:
        newpage()
        print("=== Terminal Planner ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting planner...")
            break
        else:
            print("Invalid option. Please try again.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()

