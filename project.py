# Simple To-Do List App

tasks = []  # empty list to store tasks

while True:
    print("\n===== To-Do List App =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # Add task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
            remove_task = input("Enter task number or name to remove: ")

            # If input is a number → remove by index
            if remove_task.isdigit():
                remove_index = int(remove_task)
                if 1 <= remove_index <= len(tasks):
                    removed = tasks.pop(remove_index - 1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid task number.")
            
            # Otherwise → remove by exact name
            else:
                if remove_task in tasks:
                    tasks.remove(remove_task)
                    print(f"Task '{remove_task}' removed.")
                else:
                    print("Task not found.")  # Wrong name case

    # Exit
    elif choice == "4":
        print("Exiting To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
