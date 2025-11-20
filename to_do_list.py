# -------------------------------------------
# TO-DO LIST APPLICATION (Worksheet 7 Project)
# -------------------------------------------

tasks = []  # list to store tasks


def add_task():
    """Add a new task to the list"""
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!\n")


def view_tasks():
    """Display all tasks with index"""
    if not tasks:
        print("No tasks yet.\n")
        return

    print("\nYOUR TASKS:")
    for i, t in enumerate(tasks):
        print(f"{i}. {t}")
    print()


def delete_task():
    """Delete a task using its index"""
    if not tasks:
        print("No tasks to delete.\n")
        return

    view_tasks()
    index = input("Enter index to delete: ")

    if not index.isdigit():
        print("Invalid index!\n")
        return

    index = int(index)

    if index < 0 or index >= len(tasks):
        print("Index out of range!\n")
        return

    removed = tasks.pop(index)
    print(f"Deleted: {removed}\n")


def main():
    """Main loop"""
    print("=== TO-DO LIST APP ===")

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit\n")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Uncomment to run:
# -------------------------------------------
# TO-DO LIST APPLICATION (Worksheet 7 Project)
# -------------------------------------------

tasks = []  # list to store tasks


def add_task():
    """Add a new task to the list"""
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!\n")


def view_tasks():
    """Display all tasks with index"""
    if not tasks:
        print("No tasks yet.\n")
        return

    print("\nYOUR TASKS:")
    for i, t in enumerate(tasks):
        print(f"{i}. {t}")
    print()


def delete_task():
    """Delete a task using its index"""
    if not tasks:
        print("No tasks to delete.\n")
        return

    view_tasks()
    index = input("Enter index to delete: ")

    if not index.isdigit():
        print("Invalid index!\n")
        return

    index = int(index)

    if index < 0 or index >= len(tasks):
        print("Index out of range!\n")
        return

    removed = tasks.pop(index)
    print(f"Deleted: {removed}\n")


def main():
    """Main loop"""
    print("=== TO-DO LIST APP ===")

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit\n")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Uncomment to run:
# main()

